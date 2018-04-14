from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'R4101   ._SN',
        MapName             = 'Grancel',
        Location            = 'R4101.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60029",
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
        '希德中校',                             # 9
        '贝尔克副队长',                         # 10
        '王国军士兵',                           # 11
        '士兵',                                 # 12
        '士兵',                                 # 13
        '士兵',                                 # 14
        '士兵',                                 # 15
        '士兵',                                 # 16
        '士兵',                                 # 17
        '士兵',                                 # 18
        '士兵',                                 # 19
        '士兵',                                 # 20
        '士兵',                                 # 21
        '士兵',                                 # 22
        '士兵',                                 # 23
        '士兵',                                 # 24
        '士兵',                                 # 25
        '士兵',                                 # 26
        '士兵',                                 # 27
        '士兵',                                 # 28
        '士兵',                                 # 29
        '士兵',                                 # 30
        '士兵',                                 # 31
        '士兵',                                 # 32
        '士兵',                                 # 33
        '士兵',                                 # 34
        '士兵',                                 # 35
        '士兵',                                 # 36
        '士兵',                                 # 37
        '士兵',                                 # 38
        '士兵',                                 # 39
        '士兵',                                 # 40
        '强化猎兵',                             # 41
        '强化猎兵',                             # 42
        '强化猎兵',                             # 43
        '强化猎兵',                             # 44
        '强化猎兵',                             # 45
        '强化猎兵',                             # 46
        '强化猎兵',                             # 47
        '强化猎兵',                             # 48
        '强化猎兵',                             # 49
        '强化猎兵',                             # 50
        '强化猎兵',                             # 51
        '强化猎兵',                             # 52
        '强化猎兵',                             # 53
        '强化猎兵',                             # 54
        '强化猎兵',                             # 55
        '强化猎兵',                             # 56
        '亡命守护者',                           # 57
        '亡命守护者',                           # 58
        '亡命守护者',                           # 59
        '亡命守护者',                           # 60
        '装甲猎豹',                             # 61
        '装甲猎豹',                             # 62
        '装甲猎豹',                             # 63
        '装甲猎豹',                             # 64
        '装甲猎豹',                             # 65
        '王国军士官',                           # 66
        '王国军士官',                           # 67
        '王国军士官',                           # 68
        '怪盗布卢布兰',                         # 69
        '瘦狼瓦鲁特',                           # 70
        '歼灭天使玲',                           # 71
        '幻惑之铃露茜奥拉',                     # 72
        '结社艇',                               # 73
        '结社艇影',                             # 74
        '结社艇影',                             # 75
        '结社艇影',                             # 76
        '圣海姆门方向',                         # 77
        '王都格兰赛尔方向',                     # 78
        '格鲁纳门方向',                         # 79
        '沼泽剑齿吸血魔',                       # 80
        '丘陵毒蜂',                             # 81
        '迅猛小鹫',                             # 82
        '好战蝙蝠',                             # 83
        '沼泽剑齿吸血魔',                       # 84
        '迅猛小鹫',                             # 85
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
        'ED6_DT09/CH10780 ._CH',             # 00
        'ED6_DT09/CH10781 ._CH',             # 01
        'ED6_DT09/CH10790 ._CH',             # 02
        'ED6_DT09/CH10791 ._CH',             # 03
        'ED6_DT09/CH10050 ._CH',             # 04
        'ED6_DT09/CH10051 ._CH',             # 05
        'ED6_DT09/CH10800 ._CH',             # 06
        'ED6_DT09/CH10801 ._CH',             # 07
        'ED6_DT09/CH10810 ._CH',             # 08
        'ED6_DT09/CH10811 ._CH',             # 09
        'ED6_DT09/CH10820 ._CH',             # 0A
        'ED6_DT09/CH10821 ._CH',             # 0B
        'ED6_DT09/CH11220 ._CH',             # 0C
        'ED6_DT09/CH11221 ._CH',             # 0D
        'ED6_DT09/CH11230 ._CH',             # 0E
        'ED6_DT09/CH11231 ._CH',             # 0F
        'ED6_DT27/CH03590 ._CH',             # 10
        'ED6_DT07/CH01600 ._CH',             # 11
        'ED6_DT07/CH01300 ._CH',             # 12
        'ED6_DT06/CH20043 ._CH',             # 13
        'ED6_DT26/CH20335 ._CH',             # 14
        'ED6_DT07/CH01640 ._CH',             # 15
        'ED6_DT26/CH20419 ._CH',             # 16
    )

    AddCharChipPat(
        'ED6_DT09/CH10780P._CP',             # 00
        'ED6_DT09/CH10781P._CP',             # 01
        'ED6_DT09/CH10790P._CP',             # 02
        'ED6_DT09/CH10791P._CP',             # 03
        'ED6_DT09/CH10050P._CP',             # 04
        'ED6_DT09/CH10051P._CP',             # 05
        'ED6_DT09/CH10800P._CP',             # 06
        'ED6_DT09/CH10801P._CP',             # 07
        'ED6_DT09/CH10810P._CP',             # 08
        'ED6_DT09/CH10811P._CP',             # 09
        'ED6_DT09/CH10820P._CP',             # 0A
        'ED6_DT09/CH10821P._CP',             # 0B
        'ED6_DT09/CH11220P._CP',             # 0C
        'ED6_DT09/CH11221P._CP',             # 0D
        'ED6_DT09/CH11230P._CP',             # 0E
        'ED6_DT09/CH11231P._CP',             # 0F
        'ED6_DT27/CH03590P._CP',             # 10
        'ED6_DT07/CH01600P._CP',             # 11
        'ED6_DT07/CH01300P._CP',             # 12
        'ED6_DT06/CH20043P._CP',             # 13
        'ED6_DT26/CH20335P._CP',             # 14
        'ED6_DT07/CH01640P._CP',             # 15
        'ED6_DT26/CH20419P._CP',             # 16
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        X                   = -5160,
        Z                   = -50,
        Y                   = -7520,
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
        X                   = -39160,
        Z                   = 0,
        Y                   = 152720,
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
        X                   = 61180,
        Z                   = 0,
        Y                   = 83020,
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


    DeclMonster(
        X                   = -6830,
        Z                   = 90,
        Y                   = 29510,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x297,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 16290,
        Z                   = 70,
        Y                   = 76970,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x295,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 31220,
        Z                   = 40,
        Y                   = 83060,
        Unknown_0C          = 0,
        Unknown_0E          = 14,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x29C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -33000,
        Z                   = 20,
        Y                   = 72240,
        Unknown_0C          = 0,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x29A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -17830,
        Z                   = 10,
        Y                   = 103860,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x297,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -61630,
        Z                   = 70,
        Y                   = 108700,
        Unknown_0C          = 0,
        Unknown_0E          = 14,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x29C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -44700,
        Y                   = -2000,
        Z                   = 142100,
        Range               = -33800,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x231B8,
        Unknown_18          = 0x0,
        Unknown_1C          = 7,
    )

    DeclEvent(
        X                   = -48550,
        Y                   = -2000,
        Z                   = 98420,
        Range               = -29640,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x1762E,
        Unknown_18          = 0x0,
        Unknown_1C          = 113,
    )

    DeclEvent(
        X                   = -44700,
        Y                   = -2000,
        Z                   = 142700,
        Range               = -33800,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x23A50,
        Unknown_18          = 0x0,
        Unknown_1C          = 4,
    )


    DeclActor(
        TriggerX            = -13540,
        TriggerZ            = 0,
        TriggerY            = 63650,
        TriggerRange        = 1500,
        ActorX              = -13540,
        ActorZ              = 1700,
        ActorY              = 63650,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 115,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 130,
        TriggerZ            = 0,
        TriggerY            = 56450,
        TriggerRange        = 1500,
        ActorX              = 130,
        ActorZ              = 1700,
        ActorY              = 56450,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 116,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -1460,
        TriggerZ            = 0,
        TriggerY            = 53030,
        TriggerRange        = 1500,
        ActorX              = -1460,
        ActorZ              = 1700,
        ActorY              = 53030,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 117,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_BB6",          # 00, 0
        "Function_1_C16",          # 01, 1
        "Function_2_D39",          # 02, 2
        "Function_3_D4F",          # 03, 3
        "Function_4_D9C",          # 04, 4
        "Function_5_DAB",          # 05, 5
        "Function_6_1150",         # 06, 6
        "Function_7_1269",         # 07, 7
        "Function_8_12F9",         # 08, 8
        "Function_9_155B",         # 09, 9
        "Function_10_17F7",        # 0A, 10
        "Function_11_18A5",        # 0B, 11
        "Function_12_18C4",        # 0C, 12
        "Function_13_18E3",        # 0D, 13
        "Function_14_199D",        # 0E, 14
        "Function_15_19DE",        # 0F, 15
        "Function_16_1A1F",        # 10, 16
        "Function_17_24BE",        # 11, 17
        "Function_18_29D7",        # 12, 18
        "Function_19_30E9",        # 13, 19
        "Function_20_3196",        # 14, 20
        "Function_21_3243",        # 15, 21
        "Function_22_3284",        # 16, 22
        "Function_23_32BA",        # 17, 23
        "Function_24_3633",        # 18, 24
        "Function_25_38CD",        # 19, 25
        "Function_26_38E7",        # 1A, 26
        "Function_27_394F",        # 1B, 27
        "Function_28_39BC",        # 1C, 28
        "Function_29_3A29",        # 1D, 29
        "Function_30_3A96",        # 1E, 30
        "Function_31_3AB0",        # 1F, 31
        "Function_32_3ACA",        # 20, 32
        "Function_33_3B0B",        # 21, 33
        "Function_34_3B51",        # 22, 34
        "Function_35_3B97",        # 23, 35
        "Function_36_3BDD",        # 24, 36
        "Function_37_3C23",        # 25, 37
        "Function_38_3C69",        # 26, 38
        "Function_39_3CAF",        # 27, 39
        "Function_40_3CF5",        # 28, 40
        "Function_41_3D3B",        # 29, 41
        "Function_42_3D81",        # 2A, 42
        "Function_43_3DC7",        # 2B, 43
        "Function_44_3E0D",        # 2C, 44
        "Function_45_3E53",        # 2D, 45
        "Function_46_3E99",        # 2E, 46
        "Function_47_3EDF",        # 2F, 47
        "Function_48_3F25",        # 30, 48
        "Function_49_3F6B",        # 31, 49
        "Function_50_3FB1",        # 32, 50
        "Function_51_3FF7",        # 33, 51
        "Function_52_403D",        # 34, 52
        "Function_53_4083",        # 35, 53
        "Function_54_40C9",        # 36, 54
        "Function_55_410F",        # 37, 55
        "Function_56_4155",        # 38, 56
        "Function_57_419B",        # 39, 57
        "Function_58_41E1",        # 3A, 58
        "Function_59_4227",        # 3B, 59
        "Function_60_4241",        # 3C, 60
        "Function_61_425B",        # 3D, 61
        "Function_62_4275",        # 3E, 62
        "Function_63_429B",        # 3F, 63
        "Function_64_42C1",        # 40, 64
        "Function_65_42E7",        # 41, 65
        "Function_66_430D",        # 42, 66
        "Function_67_4333",        # 43, 67
        "Function_68_4359",        # 44, 68
        "Function_69_437F",        # 45, 69
        "Function_70_43A5",        # 46, 70
        "Function_71_43CB",        # 47, 71
        "Function_72_43F1",        # 48, 72
        "Function_73_4417",        # 49, 73
        "Function_74_443D",        # 4A, 74
        "Function_75_4463",        # 4B, 75
        "Function_76_4489",        # 4C, 76
        "Function_77_44AF",        # 4D, 77
        "Function_78_44D5",        # 4E, 78
        "Function_79_44F4",        # 4F, 79
        "Function_80_4513",        # 50, 80
        "Function_81_4532",        # 51, 81
        "Function_82_4551",        # 52, 82
        "Function_83_4570",        # 53, 83
        "Function_84_458F",        # 54, 84
        "Function_85_45AE",        # 55, 85
        "Function_86_45CD",        # 56, 86
        "Function_87_463B",        # 57, 87
        "Function_88_46A9",        # 58, 88
        "Function_89_4717",        # 59, 89
        "Function_90_4785",        # 5A, 90
        "Function_91_47F3",        # 5B, 91
        "Function_92_4861",        # 5C, 92
        "Function_93_48CF",        # 5D, 93
        "Function_94_493D",        # 5E, 94
        "Function_95_49AB",        # 5F, 95
        "Function_96_4A19",        # 60, 96
        "Function_97_4A87",        # 61, 97
        "Function_98_4AF5",        # 62, 98
        "Function_99_4B63",        # 63, 99
        "Function_100_4BD1",       # 64, 100
        "Function_101_4C3F",       # 65, 101
        "Function_102_4CAD",       # 66, 102
        "Function_103_4D1B",       # 67, 103
        "Function_104_4D89",       # 68, 104
        "Function_105_4DF7",       # 69, 105
        "Function_106_4E65",       # 6A, 106
        "Function_107_4ED3",       # 6B, 107
        "Function_108_4F41",       # 6C, 108
        "Function_109_4FAF",       # 6D, 109
        "Function_110_501D",       # 6E, 110
        "Function_111_54C7",       # 6F, 111
        "Function_112_54DD",       # 70, 112
        "Function_113_554F",       # 71, 113
        "Function_114_5CDF",       # 72, 114
        "Function_115_5D32",       # 73, 115
        "Function_116_5D75",       # 74, 116
        "Function_117_5DC6",       # 75, 117
    )


    def Function_0_BB6(): pass

    label("Function_0_BB6")

    Call(0, 5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_BD9")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x5B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 6)
    Jump("loc_C15")

    label("loc_BD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_BFA")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F1)
    OP_B5(0x0)
    SetMapFlags(0x10000000)
    Event(0, 8)
    Jump("loc_C15")

    label("loc_BFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C15")
    OP_B5(0x0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 16)

    label("loc_C15")

    Return()

    # Function_0_BB6 end

    def Function_1_C16(): pass

    label("Function_1_C16")

    OP_16(0x2, 0xFA0, 0xFFFDF0A8, 0xFFFF15A0, 0x23003C)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C52")
    SetChrFlags(0x4F, 0x80)
    SetChrFlags(0x50, 0x80)
    SetChrFlags(0x51, 0x80)
    SetChrFlags(0x52, 0x80)
    SetChrFlags(0x53, 0x80)
    SetChrFlags(0x54, 0x80)

    label("loc_C52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 0)), scpexpr(EXPR_END)), "loc_C67")
    SetMapFlags(0x2000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C67")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x2710), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C7C")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C7C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x2711), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C91")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C91")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x2712), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CA6")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CA6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x2713), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CBB")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CD3")
    OP_B1("R4101_y")
    Jump("loc_CDC")

    label("loc_CD3")

    OP_B1("R4101_n")

    label("loc_CDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 2)), scpexpr(EXPR_END)), "loc_CE7")
    Call(0, 5)

    label("loc_CE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CF8")
    OP_1B(0x0, 0x0, 0x72)

    label("loc_CF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D38")
    OP_B5(0x0)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_D1A"),
        (101, "loc_D29"),
        (SWITCH_DEFAULT, "loc_D38"),
    )


    label("loc_D1A")

    OP_A3(0x10F3)
    SetMapFlags(0x10000000)
    Event(0, 19)
    Jump("loc_D38")

    label("loc_D29")

    OP_A3(0x10F3)
    SetMapFlags(0x10000000)
    Event(0, 20)
    Jump("loc_D38")

    label("loc_D38")

    Return()

    # Function_1_C16 end

    def Function_2_D39(): pass

    label("Function_2_D39")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D4E")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_D39")

    label("loc_D4E")

    Return()

    # Function_2_D39 end

    def Function_3_D4F(): pass

    label("Function_3_D4F")

    EventBegin(0x1)
    SetChrSubChip(0x1, 3)
    SetChrSubChip(0x2, 3)
    SetChrSubChip(0x3, 3)
    FadeToDark(500, 0, -1)
    OP_8C(0x0, 0, 0)

    def lambda_D77():
        OP_91(0xFE, 0x0, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_D77)
    ClearMapFlags(0x2000000)
    OP_0D()
    NewScene("ED6_DT21/T4100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_D4F end

    def Function_4_D9C(): pass

    label("Function_4_D9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DA5")
    Return()

    label("loc_DA5")

    ClearMapFlags(0x2000000)
    Return()

    # Function_4_D9C end

    def Function_5_DAB(): pass

    label("Function_5_DAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 1)), scpexpr(EXPR_END)), "loc_114F")
    ClearChrFlags(0x41, 0x80)
    SetChrFlags(0x41, 0x20)
    ClearChrFlags(0x41, 0x1)
    SetChrChipByIndex(0x41, 20)
    SetChrPos(0x41, -38950, 0, 125450, 180)
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
    SetChrFlags(0xA, 0x20)
    SetChrFlags(0xB, 0x20)
    SetChrFlags(0xC, 0x20)
    SetChrFlags(0xD, 0x20)
    SetChrFlags(0xE, 0x20)
    SetChrFlags(0xF, 0x20)
    SetChrFlags(0x10, 0x20)
    SetChrFlags(0x11, 0x20)
    SetChrFlags(0x12, 0x20)
    SetChrFlags(0x13, 0x20)
    SetChrFlags(0x14, 0x20)
    SetChrFlags(0x15, 0x20)
    SetChrFlags(0x16, 0x20)
    SetChrFlags(0x17, 0x20)
    SetChrFlags(0x18, 0x20)
    SetChrFlags(0x19, 0x20)
    SetChrFlags(0x1A, 0x20)
    SetChrFlags(0x1B, 0x20)
    SetChrFlags(0x1C, 0x20)
    SetChrFlags(0x1D, 0x20)
    SetChrFlags(0x1E, 0x20)
    SetChrFlags(0x1F, 0x20)
    SetChrFlags(0x20, 0x20)
    SetChrFlags(0x21, 0x20)
    ClearChrFlags(0xA, 0x1)
    ClearChrFlags(0xB, 0x1)
    ClearChrFlags(0xC, 0x1)
    ClearChrFlags(0xD, 0x1)
    ClearChrFlags(0xE, 0x1)
    ClearChrFlags(0xF, 0x1)
    ClearChrFlags(0x10, 0x1)
    ClearChrFlags(0x11, 0x1)
    ClearChrFlags(0x12, 0x1)
    ClearChrFlags(0x13, 0x1)
    ClearChrFlags(0x14, 0x1)
    ClearChrFlags(0x15, 0x1)
    ClearChrFlags(0x16, 0x1)
    ClearChrFlags(0x17, 0x1)
    ClearChrFlags(0x18, 0x1)
    ClearChrFlags(0x19, 0x1)
    ClearChrFlags(0x1A, 0x1)
    ClearChrFlags(0x1B, 0x1)
    ClearChrFlags(0x1C, 0x1)
    ClearChrFlags(0x1D, 0x1)
    ClearChrFlags(0x1E, 0x1)
    ClearChrFlags(0x1F, 0x1)
    ClearChrFlags(0x20, 0x1)
    ClearChrFlags(0x21, 0x1)
    SetChrChipByIndex(0xA, 22)
    SetChrChipByIndex(0xB, 19)
    SetChrChipByIndex(0xC, 19)
    SetChrChipByIndex(0xD, 22)
    SetChrChipByIndex(0xE, 22)
    SetChrChipByIndex(0xF, 19)
    SetChrChipByIndex(0x10, 19)
    SetChrChipByIndex(0x11, 22)
    SetChrChipByIndex(0x12, 19)
    SetChrChipByIndex(0x13, 19)
    SetChrChipByIndex(0x14, 22)
    SetChrChipByIndex(0x15, 19)
    SetChrChipByIndex(0x16, 22)
    SetChrChipByIndex(0x17, 19)
    SetChrChipByIndex(0x18, 22)
    SetChrChipByIndex(0x19, 19)
    SetChrChipByIndex(0x1A, 19)
    SetChrChipByIndex(0x1B, 22)
    SetChrChipByIndex(0x1C, 19)
    SetChrChipByIndex(0x1D, 19)
    SetChrChipByIndex(0x1E, 19)
    SetChrChipByIndex(0x1F, 22)
    SetChrChipByIndex(0x20, 22)
    SetChrChipByIndex(0x21, 19)
    SetChrPos(0xA, -32360, 0, 119050, 45)
    SetChrPos(0xB, -30880, 0, 120220, 315)
    SetChrPos(0xC, -32770, 0, 122700, 180)
    SetChrPos(0xD, -30610, 250, 124400, 270)
    SetChrPos(0xE, -30670, 250, 127190, 135)
    SetChrPos(0xF, -34040, 0, 126930, 45)
    SetChrPos(0x10, -29470, 250, 125310, 315)
    SetChrPos(0x11, -32520, 0, 127180, 0)
    SetChrPos(0x12, -44210, 0, 117600, 180)
    SetChrPos(0x13, -46830, 0, 119130, 0)
    SetChrPos(0x14, -44450, 0, 119820, 45)
    SetChrPos(0x15, -47450, 0, 121690, 180)
    SetChrPos(0x16, -43440, 0, 122980, 0)
    SetChrPos(0x17, -46070, 250, 125390, 135)
    SetChrPos(0x18, -49300, 0, 122100, 270)
    SetChrPos(0x19, -48780, 250, 125590, 180)
    SetChrPos(0x1A, -33410, 0, 124960, 1350)
    SetChrPos(0x1B, -30660, 250, 129020, 0)
    SetChrPos(0x1C, -28390, 0, 121800, 315)
    SetChrPos(0x1D, -33200, 0, 129930, 270)
    SetChrPos(0x1E, -45060, 0, 122340, 135)
    SetChrPos(0x1F, -44090, 0, 125830, 225)
    SetChrPos(0x20, -46660, 250, 127320, 270)
    SetChrPos(0x21, -54520, 0, 121790, 180)

    label("loc_114F")

    Return()

    # Function_5_DAB end

    def Function_6_1150(): pass

    label("Function_6_1150")

    EventBegin(0x0)
    RemoveParty(0x5, 0xFF)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x6, 0xFF)
    RemoveParty(0x4, 0xFF)
    RemoveParty(0x7, 0xFF)
    SetChrPos(0x101, -38810, 0, 147550, 180)
    OP_6D(-38810, 0, 139930, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(33000, 0)
    OP_6E(262, 0)

    def lambda_11B5():
        OP_8E(0xFE, 0xFFFF6866, 0x0, 0x2229A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11B5)
    FadeToBright(1000, 0)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #0
        0x101,
        (
            "#1003F哈哈哈……\x02\x03",

            "格鲁纳门的\x01",
            "长城『亚宁堡』上……\x02\x03",

            "#1002F必须要赶快过去……！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1636)
    OP_28(0x8C, 0x1, 0x200)
    OP_28(0x8C, 0x4, 0x10)
    OP_28(0x8D, 0x4, 0x2)
    OP_28(0x8D, 0x4, 0x8)
    OP_28(0x8D, 0x1, 0x1)
    OP_28(0x8D, 0x1, 0x2)
    OP_1B(0x0, 0x0, 0x72)
    OP_20(0x3E8)
    OP_21()
    OP_1D(0x1D)
    Sleep(500)
    EventEnd(0x0)
    Return()

    # Function_6_1150 end

    def Function_7_1269(): pass

    label("Function_7_1269")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1276")
    Return()

    label("loc_1276")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12F8")
    EventBegin(0x2)

    ChrTalk(    #1
        0x101,
        (
            "#1003F（离傍晚\x01",
            "　没多少时间了……)\x02\x03",

            "#1002F（得快点……得快点\x01",
            "　赶到格鲁纳门才行！）\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_12F8")

    Return()

    # Function_7_1269 end

    def Function_8_12F9(): pass

    label("Function_8_12F9")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_72(0x2, 0x4)
    OP_72(0x3, 0x4)
    OP_72(0x4, 0x4)
    OP_72(0x5, 0x4)
    SetChrPos(0x44, -35200, 0, 128000, 0)
    SetChrPos(0x45, -35200, 0, 135000, 0)
    SetChrPos(0x46, -41700, 0, 128000, 0)
    SetChrPos(0x47, -41700, 0, 135000, 0)
    OP_A1(0x44, 0x2)
    OP_A1(0x45, 0x3)
    OP_A1(0x46, 0x4)
    OP_A1(0x47, 0x5)
    OP_6D(-39360, 250, 110440, 0)
    OP_67(0, 12030, -10000, 0)
    OP_6B(4620, 0)
    OP_6C(33000, 0)
    OP_6E(381, 0)
    SetChrPos(0x8, -31690, 250, 129009, 270)
    SetChrPos(0x9, -30900, 250, 128050, 270)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    OP_43(0x101, 0x2, 0x0, 0x9)

    def lambda_13F1():
        OP_6D(-40190, 0, 126470, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_13F1)

    def lambda_1409():
        OP_6C(69000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1409)
    OP_C8(0x200, 0x46, "C_PLAC04._CH", 0x0, 0x3E8)
    FadeToBright(1000, 0)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    Sleep(1000)
    Fade(1000)
    OP_6D(-32450, 250, 129930, 0)
    OP_67(0, 8780, -10000, 0)
    OP_6B(2290, 0)
    OP_6C(45000, 0)
    OP_6E(354, 0)
    OP_0D()

    ChrTalk(    #2
        0x9,
        (
            "呼，总算是在傍晚前\x01",
            "将那些机器人解决了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x9,
        "终于可以喘口气了。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 400)
    Sleep(500)

    ChrTalk(    #4
        0x8,
        (
            "#703F#5P是啊……\x01",
            "士兵们也累了吧。\x02\x03",

            "#701F接下来的警戒就交给预备队，\x01",
            "今天让他们先好好休息一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x9,
        "明白。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F2)
    NewScene("ED6_DT21/C3100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_8_12F9 end

    def Function_9_155B(): pass

    label("Function_9_155B")

    SetChrPos(0xA, -37500, 0, 114000, 0)
    SetChrPos(0xB, -39300, 0, 114000, 0)
    SetChrPos(0xC, -37500, 0, 112000, 0)
    SetChrPos(0xD, -39300, 0, 112000, 0)
    SetChrPos(0xE, -37500, 0, 110000, 0)
    SetChrPos(0xF, -39300, 0, 110000, 0)
    SetChrPos(0x10, -37500, 0, 108000, 0)
    SetChrPos(0x11, -39300, 0, 108000, 0)
    SetChrPos(0x12, -37500, 0, 106000, 0)
    SetChrPos(0x13, -39300, 0, 106000, 0)
    SetChrPos(0x14, -37500, 0, 104000, 0)
    SetChrPos(0x15, -39300, 0, 104000, 0)
    SetChrPos(0x16, -37500, 0, 102000, 0)
    SetChrPos(0x17, -39300, 0, 102000, 0)
    SetChrPos(0x18, -37500, 0, 100000, 0)
    SetChrPos(0x19, -39300, 0, 100000, 0)
    SetChrPos(0x1A, -37500, 0, 98000, 0)
    SetChrPos(0x1B, -39300, 0, 98000, 0)
    SetChrPos(0x1C, -37500, 0, 96000, 0)
    SetChrPos(0x1D, -39300, 0, 96000, 0)
    SetChrPos(0x1E, -37500, 0, 94000, 0)
    SetChrPos(0x1F, -39300, 0, 94000, 0)
    SetChrPos(0x20, -37500, 0, 92000, 0)
    SetChrPos(0x21, -39300, 0, 92000, 0)
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
    ClearChrFlags(0xA, 0x40)
    ClearChrFlags(0xB, 0x40)
    ClearChrFlags(0xC, 0x40)
    ClearChrFlags(0xD, 0x40)
    ClearChrFlags(0xE, 0x40)
    ClearChrFlags(0xF, 0x40)
    ClearChrFlags(0x10, 0x40)
    ClearChrFlags(0x11, 0x40)
    ClearChrFlags(0x12, 0x40)
    ClearChrFlags(0x13, 0x40)
    ClearChrFlags(0x14, 0x40)
    ClearChrFlags(0x15, 0x40)
    ClearChrFlags(0x16, 0x40)
    ClearChrFlags(0x17, 0x40)
    ClearChrFlags(0x18, 0x40)
    ClearChrFlags(0x19, 0x40)
    ClearChrFlags(0x1A, 0x40)
    ClearChrFlags(0x1B, 0x40)
    ClearChrFlags(0x1C, 0x40)
    ClearChrFlags(0x1D, 0x40)
    ClearChrFlags(0x1E, 0x40)
    ClearChrFlags(0x1F, 0x40)
    ClearChrFlags(0x20, 0x40)
    ClearChrFlags(0x21, 0x40)
    OP_43(0x101, 0x3, 0x0, 0xA)
    WaitChrThread(0x101, 0x3)
    OP_43(0x101, 0x3, 0x0, 0xD)
    Return()

    # Function_9_155B end

    def Function_10_17F7(): pass

    label("Function_10_17F7")

    OP_43(0xA, 0x1, 0x0, 0xB)
    OP_43(0xB, 0x1, 0x0, 0xC)
    OP_43(0xC, 0x1, 0x0, 0xB)
    OP_43(0xD, 0x1, 0x0, 0xC)
    OP_43(0xE, 0x1, 0x0, 0xB)
    OP_43(0xF, 0x1, 0x0, 0xC)
    OP_43(0x10, 0x1, 0x0, 0xB)
    OP_43(0x11, 0x1, 0x0, 0xC)
    OP_43(0x12, 0x1, 0x0, 0xB)
    OP_43(0x13, 0x1, 0x0, 0xC)
    OP_43(0x14, 0x1, 0x0, 0xB)
    OP_43(0x15, 0x1, 0x0, 0xC)
    OP_43(0x16, 0x1, 0x0, 0xB)
    OP_43(0x17, 0x1, 0x0, 0xC)
    OP_43(0x18, 0x1, 0x0, 0xB)
    OP_43(0x19, 0x1, 0x0, 0xC)
    OP_43(0x1A, 0x1, 0x0, 0xB)
    OP_43(0x1B, 0x1, 0x0, 0xC)
    OP_43(0x1C, 0x1, 0x0, 0xB)
    OP_43(0x1D, 0x1, 0x0, 0xC)
    OP_43(0x1E, 0x1, 0x0, 0xB)
    OP_43(0x1F, 0x1, 0x0, 0xC)
    OP_43(0x20, 0x1, 0x0, 0xB)
    OP_43(0x21, 0x1, 0x0, 0xC)
    WaitChrThread(0xF, 0x1)
    Return()

    # Function_10_17F7 end

    def Function_11_18A5(): pass

    label("Function_11_18A5")

    SetChrChipByIndex(0xFE, 21)
    OP_8E(0xFE, 0xFFFF6D84, 0x0, 0x220EC, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_11_18A5 end

    def Function_12_18C4(): pass

    label("Function_12_18C4")

    SetChrChipByIndex(0xFE, 21)
    OP_8E(0xFE, 0xFFFF667C, 0x0, 0x220EC, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_12_18C4 end

    def Function_13_18E3(): pass

    label("Function_13_18E3")

    OP_43(0xA, 0x1, 0x0, 0xE)
    OP_43(0xB, 0x1, 0x0, 0xF)
    Sleep(800)
    OP_43(0xC, 0x1, 0x0, 0xE)
    OP_43(0xD, 0x1, 0x0, 0xF)
    Sleep(800)
    OP_43(0xE, 0x1, 0x0, 0xE)
    OP_43(0xF, 0x1, 0x0, 0xF)
    Sleep(800)
    OP_43(0x10, 0x1, 0x0, 0xE)
    OP_43(0x11, 0x1, 0x0, 0xF)
    Sleep(800)
    OP_43(0x12, 0x1, 0x0, 0xE)
    OP_43(0x13, 0x1, 0x0, 0xF)
    Sleep(800)
    OP_43(0x14, 0x1, 0x0, 0xE)
    OP_43(0x15, 0x1, 0x0, 0xF)
    Sleep(800)
    OP_43(0x16, 0x1, 0x0, 0xE)
    OP_43(0x17, 0x1, 0x0, 0xF)
    Sleep(800)
    OP_43(0x18, 0x1, 0x0, 0xE)
    OP_43(0x19, 0x1, 0x0, 0xF)
    Sleep(800)
    OP_43(0x1A, 0x1, 0x0, 0xE)
    OP_43(0x1B, 0x1, 0x0, 0xF)
    Sleep(800)
    OP_43(0x1C, 0x1, 0x0, 0xE)
    OP_43(0x1D, 0x1, 0x0, 0xF)
    Return()

    # Function_13_18E3 end

    def Function_14_199D(): pass

    label("Function_14_199D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_19DD")
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -37500, 0, 120000, 0)
    SetChrChipByIndex(0xFE, 21)
    OP_8E(0xFE, 0xFFFF6D84, 0x0, 0x215FC, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Jump("Function_14_199D")

    label("loc_19DD")

    Return()

    # Function_14_199D end

    def Function_15_19DE(): pass

    label("Function_15_19DE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1A1E")
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -39300, 0, 120000, 0)
    SetChrChipByIndex(0xFE, 21)
    OP_8E(0xFE, 0xFFFF667C, 0x0, 0x215FC, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Jump("Function_15_19DE")

    label("loc_1A1E")

    Return()

    # Function_15_19DE end

    def Function_16_1A1F(): pass

    label("Function_16_1A1F")

    EventBegin(0x0)
    OP_D2(0x702FC, 0x70303, 0x0)
    OP_D2(0x702FD, 0x70304, 0x1)
    OP_D2(0x2701C9, 0x2701CE, 0x17)
    OP_D2(0x2701C6, 0x2701CB, 0x18)
    OP_D2(0x260003, 0x260008, 0x19)
    OP_D2(0x2701C8, 0x2701CD, 0x1A)
    OP_D2(0x702EE, 0x702F5, 0x2)
    OP_D2(0x702EF, 0x702F6, 0x3)
    OP_D2(0x70302, 0x70309, 0x4)
    OP_D2(0x260052, 0x260057, 0x5)
    OP_D2(0x27023F, 0x270249, 0x6)
    OP_D2(0x270253, 0x27025D, 0x7)
    OP_D2(0x26008F, 0x260094, 0x8)
    OP_D2(0x27026B, 0x270275, 0x9)
    OP_D2(0x260090, 0x260095, 0xA)
    OP_D2(0x2600A0, 0x2600A5, 0xB)
    OP_6D(-38970, 0, 100000, 0)
    OP_67(0, 12930, -10000, 0)
    OP_6B(3880, 0)
    OP_6C(0, 0)
    OP_6E(516, 0)
    OP_A1(0x48, 0x0)
    OP_A1(0x49, 0x1)
    OP_A1(0x4A, 0x7)
    OP_A1(0x4B, 0x9)
    OP_72(0x0, 0x4)
    OP_72(0x1, 0x4)
    OP_72(0x7, 0x4)
    OP_72(0x9, 0x4)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 800)
    OP_70(0x0, 0x384)
    OP_22(0x79, 0x1, 0x64)
    LoadEffect(0x0, "map\\\\mp021_00.eff")
    SetChrPos(0x48, -39000, 10000, 60000, 0)
    SetChrPos(0x49, -39000, 0, 60000, 0)
    SetChrPos(0x4A, -28000, 2000, 70000, 0)
    SetChrPos(0x4B, -50000, 2000, 70000, 0)
    SetChrChipByIndex(0x44, 8)
    SetChrChipByIndex(0x46, 6)
    SetChrChipByIndex(0x45, 5)
    SetChrChipByIndex(0x47, 7)
    SetChrSubChip(0x45, 2)
    SetChrFlags(0x44, 0x4)
    SetChrFlags(0x46, 0x4)
    SetChrFlags(0x45, 0x4)
    SetChrFlags(0x47, 0x4)
    SetChrPos(0x44, -39150, 6000, 105360, 0)
    SetChrPos(0x46, -37150, 6000, 105360, 0)
    SetChrPos(0x45, -41150, 6000, 105360, 0)
    SetChrPos(0x47, -42150, 6000, 105360, 0)
    SetChrChipByIndex(0x41, 0)
    SetChrChipByIndex(0xA, 2)
    SetChrChipByIndex(0xB, 2)
    SetChrChipByIndex(0xC, 2)
    SetChrChipByIndex(0xD, 2)
    SetChrChipByIndex(0xE, 2)
    SetChrChipByIndex(0xF, 2)
    SetChrChipByIndex(0x10, 2)
    SetChrChipByIndex(0x11, 2)
    SetChrChipByIndex(0x12, 2)
    SetChrChipByIndex(0x13, 2)
    SetChrChipByIndex(0x14, 2)
    SetChrChipByIndex(0x15, 2)
    SetChrChipByIndex(0x16, 2)
    SetChrChipByIndex(0x17, 2)
    SetChrChipByIndex(0x18, 2)
    SetChrChipByIndex(0x19, 2)
    SetChrChipByIndex(0x1A, 2)
    SetChrChipByIndex(0x1B, 2)
    SetChrChipByIndex(0x1C, 2)
    SetChrChipByIndex(0x1D, 2)
    SetChrChipByIndex(0x1E, 2)
    SetChrChipByIndex(0x1F, 2)
    SetChrChipByIndex(0x20, 2)
    SetChrChipByIndex(0x21, 2)
    FadeToBright(1000, 0)

    def lambda_1C93():
        OP_6D(-38970, 0, 108000, 15000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1C93)

    def lambda_1CAB():
        OP_67(0, 10000, -10000, 15000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1CAB)

    def lambda_1CC3():
        OP_6E(385, 10000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1CC3)
    OP_43(0x4A, 0x1, 0x0, 0x1E)
    Sleep(2000)
    OP_43(0x4B, 0x1, 0x0, 0x1F)
    Sleep(4000)
    OP_43(0x49, 0x1, 0x0, 0x18)
    WaitChrThread(0x49, 0x1)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #6
        0x44,
        (
            "#230F#6P那么……\x01",
            "差不多可以开始了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x45,
        (
            "#252F#2P真是的，如果『剑圣』在的话，\x01",
            "多少会更有意思些……\x02\x03",

            "不能开枪的士兵，\x01",
            "拿来热身都不够啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x46,
        (
            "#261F#5P呵呵，这不也挺好吗？\x02\x03",

            "#265F一边解决这些小木偶，\x01",
            "一边前进也挺开心的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x47,
        (
            "#240F#4P帕蒂尔·玛蒂尔\x01",
            "就不要叫出来了。\x02\x03",

            "不然他们一转眼\x01",
            "就会跑个精光了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x46,
        (
            "#268F#5P唉，真没劲。\x02\x03",

            "#1306F我本来还想砸碎\x01",
            "那座美丽的城堡呢⊙\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x44,
        (
            "#231F#6P被蹂躏毁灭的美吗……\x01",
            "听起来似乎也不坏嘛。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(-39180, 0, 114670, 0)
    OP_67(0, 6100, -10000, 0)
    OP_6B(1870, 0)
    OP_6C(36000, 0)
    OP_6E(478, 0)
    OP_43(0xA, 0x1, 0x0, 0x20)
    OP_43(0xB, 0x1, 0x0, 0x21)
    OP_43(0xC, 0x1, 0x0, 0x22)
    OP_43(0xD, 0x1, 0x0, 0x23)
    OP_43(0xE, 0x1, 0x0, 0x24)
    OP_43(0xF, 0x1, 0x0, 0x25)
    OP_43(0x10, 0x1, 0x0, 0x26)
    OP_43(0x11, 0x1, 0x0, 0x27)
    OP_43(0x12, 0x1, 0x0, 0x28)
    OP_43(0x13, 0x1, 0x0, 0x29)
    OP_43(0x14, 0x1, 0x0, 0x2A)
    OP_43(0x15, 0x1, 0x0, 0x2B)
    OP_43(0x16, 0x1, 0x0, 0x2C)
    OP_43(0x17, 0x1, 0x0, 0x2D)
    OP_43(0x18, 0x1, 0x0, 0x2E)
    OP_43(0x19, 0x1, 0x0, 0x2F)
    OP_43(0x1A, 0x1, 0x0, 0x30)
    OP_43(0x1B, 0x1, 0x0, 0x31)
    OP_43(0x1C, 0x1, 0x0, 0x32)
    OP_43(0x1D, 0x1, 0x0, 0x33)
    OP_43(0x1E, 0x1, 0x0, 0x34)
    OP_43(0x1F, 0x1, 0x0, 0x35)
    OP_43(0x20, 0x1, 0x0, 0x36)
    OP_43(0x21, 0x1, 0x0, 0x37)
    OP_43(0x41, 0x1, 0x0, 0x38)
    OP_0D()

    def lambda_1F9C():
        OP_6D(-38780, 0, 125730, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1F9C)

    def lambda_1FB4():
        OP_6E(491, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1FB4)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x41, 0x1)

    ChrTalk(    #12
        0x41,
        "#5P你们是『噬身之蛇』！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x41,
        (
            "#5P可恶……\x01",
            "现在竟然还能使用飞艇……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(-38410, 0, 114210, 0)
    OP_67(0, 6520, -10000, 0)
    OP_6B(2080, 0)
    OP_6C(147000, 0)
    OP_6E(477, 0)

    def lambda_205C():

        label("loc_205C")

        TurnDirection(0xFE, 0x47, 400)
        OP_48()
        Jump("loc_205C")

    QueueWorkItem2(0xA, 1, lambda_205C)

    def lambda_206D():

        label("loc_206D")

        TurnDirection(0xFE, 0x47, 400)
        OP_48()
        Jump("loc_206D")

    QueueWorkItem2(0xB, 1, lambda_206D)

    def lambda_207E():

        label("loc_207E")

        TurnDirection(0xFE, 0x46, 400)
        OP_48()
        Jump("loc_207E")

    QueueWorkItem2(0x12, 1, lambda_207E)

    def lambda_208F():

        label("loc_208F")

        TurnDirection(0xFE, 0x46, 400)
        OP_48()
        Jump("loc_208F")

    QueueWorkItem2(0x13, 1, lambda_208F)

    def lambda_20A0():

        label("loc_20A0")

        TurnDirection(0xFE, 0x46, 400)
        OP_48()
        Jump("loc_20A0")

    QueueWorkItem2(0x14, 1, lambda_20A0)

    def lambda_20B1():

        label("loc_20B1")

        TurnDirection(0xFE, 0x46, 400)
        OP_48()
        Jump("loc_20B1")

    QueueWorkItem2(0x15, 1, lambda_20B1)

    def lambda_20C2():
        OP_6D(-38290, 0, 118490, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_20C2)

    def lambda_20DA():
        OP_67(0, 5290, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_20DA)

    def lambda_20F2():
        OP_6E(488, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_20F2)
    SetChrChipByIndex(0x44, 23)
    SetChrSubChip(0x44, 0)

    def lambda_210C():
        OP_8E(0xFE, 0xFFFF6A50, 0x0, 0x1CC6E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x44, 1, lambda_210C)
    Sleep(200)

    def lambda_212C():
        OP_8E(0xFE, 0xFFFF700E, 0x0, 0x1C7E6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x46, 1, lambda_212C)
    Sleep(50)

    def lambda_214C():
        OP_8E(0xFE, 0xFFFF62A8, 0x0, 0x1C822, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x47, 1, lambda_214C)
    Sleep(200)
    SetChrFlags(0x45, 0x40)
    SetChrChipByIndex(0x45, 24)

    def lambda_2176():
        OP_8E(0xFE, 0xFFFF6A00, 0x0, 0x1C4A8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x45, 1, lambda_2176)
    WaitChrThread(0x44, 0x1)
    SetChrChipByIndex(0x44, 9)
    SetChrSubChip(0x44, 0)
    WaitChrThread(0x45, 0x1)
    SetChrChipByIndex(0x45, 11)
    SetChrSubChip(0x45, 0)
    Sleep(200)

    ChrTalk(    #14
        0x44,
        (
            "#231F#5P呵呵，初次见面。\x02\x03",

            "鄙人的名字是\x01",
            "『怪盗绅士』布卢布兰。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x45,
        (
            "#252F#2P嘿嘿……\x01",
            "我是『瘦狼』瓦鲁特。\x02\x03",

            "你们就尽情享受恐惧的滋味吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x47,
        (
            "#244F#2P我是『幻惑之铃』露茜奥拉。\x02\x03",

            "#240F虽然只能相聚片刻，\x01",
            "但希望能给各位留下个好印象……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x46,
        (
            "#261F#5P嘻嘻……\x01",
            "我是『歼灭天使』玲。\x02\x03",

            "#1306F你们会发出\x01",
            "怎样的惨叫声呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x41,
        "#5P还、还有闲情来自报家门……！\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0x41, 0)
    SetChrChipByIndex(0x41, 4)
    OP_0D()

    ChrTalk(    #19
        0x41,
        "#5P#3S全体准备！\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrSubChip(0x41, 1)

    ChrTalk(    #20
        0x41,
        "#5P#3S突击！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_43(0xA, 0x1, 0x0, 0x3E)
    OP_43(0xB, 0x1, 0x0, 0x3F)
    OP_43(0xC, 0x1, 0x0, 0x40)
    OP_43(0xD, 0x1, 0x0, 0x41)
    OP_43(0xE, 0x1, 0x0, 0x42)
    OP_43(0xF, 0x1, 0x0, 0x43)
    OP_43(0x10, 0x1, 0x0, 0x44)
    OP_43(0x11, 0x1, 0x0, 0x45)
    OP_43(0x12, 0x1, 0x0, 0x46)
    OP_43(0x13, 0x1, 0x0, 0x47)
    OP_43(0x14, 0x1, 0x0, 0x48)
    OP_43(0x15, 0x1, 0x0, 0x49)
    OP_43(0x16, 0x1, 0x0, 0x4A)
    OP_43(0x17, 0x1, 0x0, 0x4B)
    OP_43(0x18, 0x1, 0x0, 0x4C)
    OP_43(0x19, 0x1, 0x0, 0x4D)
    SetChrFlags(0x20, 0x40)
    SetChrFlags(0x21, 0x40)
    OP_43(0x1A, 0x1, 0x0, 0x4E)
    OP_43(0x1B, 0x1, 0x0, 0x4F)
    OP_43(0x1C, 0x1, 0x0, 0x50)
    OP_43(0x1D, 0x1, 0x0, 0x51)
    OP_43(0x1E, 0x1, 0x0, 0x52)
    OP_43(0x1F, 0x1, 0x0, 0x53)
    OP_43(0x20, 0x1, 0x0, 0x54)
    OP_43(0x21, 0x1, 0x0, 0x55)
    OP_44(0x101, 0xFF)
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
    Battle(0x2710, 0x30000F, 0x0, 0x0, 0xFF)
    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0x2711, 0x300010, 0x0, 0x0, 0xFF)
    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0x2712, 0x300011, 0x0, 0x0, 0xFF)
    Call(0, 17)
    Return()

    # Function_16_1A1F end

    def Function_17_24BE(): pass

    label("Function_17_24BE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_44(0x45, 0x1)
    OP_44(0x46, 0x1)
    OP_44(0x47, 0x1)
    OP_44(0xA, 0x1)
    OP_44(0xB, 0x1)
    OP_44(0xC, 0x1)
    OP_44(0xD, 0x1)
    OP_44(0xE, 0x1)
    OP_44(0xF, 0x1)
    OP_44(0x10, 0x1)
    OP_44(0x11, 0x1)
    OP_44(0x12, 0x1)
    OP_44(0x13, 0x1)
    OP_44(0x14, 0x1)
    OP_44(0x15, 0x1)
    OP_44(0x16, 0x1)
    OP_44(0x17, 0x1)
    OP_44(0x18, 0x1)
    OP_44(0x19, 0x1)
    OP_D2(0x702FC, 0x70303, 0x0)
    OP_D2(0x702FD, 0x70304, 0x1)
    OP_D2(0x2701C9, 0x2701CE, 0x17)
    OP_D2(0x2701C6, 0x2701CB, 0x18)
    OP_D2(0x260003, 0x260008, 0x19)
    OP_D2(0x2701C8, 0x2701CD, 0x1A)
    OP_D2(0x702EE, 0x702F5, 0x2)
    OP_D2(0x702EF, 0x702F6, 0x3)
    OP_D2(0x70302, 0x70309, 0x4)
    OP_D2(0x702F1, 0x702F8, 0x5)
    OP_D2(0x60053, 0x60058, 0x6)
    OP_D2(0x70300, 0x70307, 0x7)
    OP_D2(0x2600A0, 0x2600A5, 0x8)
    OP_D2(0x27026B, 0x270275, 0x9)
    OP_D2(0x26024A, 0x26024F, 0x1B)
    OP_6D(-38500, 0, 119490, 0)
    OP_67(0, 5160, -10000, 0)
    OP_6B(1730, 0)
    OP_6C(180000, 0)
    OP_6E(498, 0)
    SetChrFlags(0x44, 0x80)
    ClearChrFlags(0x41, 0x80)
    SetChrSubChip(0x41, 0)
    SetChrChipByIndex(0x41, 0)
    SetChrSubChip(0x41, 0)
    SetChrPos(0x41, -38950, 0, 126850, 180)
    ClearChrFlags(0x45, 0x80)
    ClearChrFlags(0x46, 0x80)
    ClearChrFlags(0x47, 0x80)
    SetChrPos(0x45, -38310, 0, 120840, 0)
    SetChrPos(0x46, -35960, 0, 120330, 45)
    SetChrPos(0x47, -40360, 0, 119490, 315)
    SetChrChipByIndex(0x45, 8)
    SetChrChipByIndex(0x46, 25)
    SetChrChipByIndex(0x47, 26)
    SetChrChipByIndex(0x44, 9)
    SetChrSubChip(0x45, 0)
    SetChrSubChip(0x46, 0)
    SetChrSubChip(0x47, 0)
    OP_A1(0x48, 0x0)
    OP_A1(0x49, 0x1)
    OP_72(0x0, 0x4)
    OP_72(0x1, 0x4)
    SetChrPos(0x48, -39020, 0, 97470, 0)
    SetChrPos(0x49, -39020, 100, 98470, 0)
    OP_72(0x0, 0x20)
    OP_6F(0x0, 1100)
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
    ClearMapFlags(0x10)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)

    def lambda_2727():
        OP_6D(-38500, 0, 121000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2727)

    def lambda_273F():
        OP_6B(2000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_273F)
    OP_43(0xA, 0x1, 0x0, 0x56)
    OP_43(0xB, 0x1, 0x0, 0x57)
    OP_43(0xC, 0x1, 0x0, 0x58)
    OP_43(0xD, 0x1, 0x0, 0x59)
    OP_43(0xE, 0x1, 0x0, 0x5A)
    OP_43(0xF, 0x1, 0x0, 0x5B)
    OP_43(0x10, 0x1, 0x0, 0x5C)
    OP_43(0x11, 0x1, 0x0, 0x5D)
    OP_43(0x12, 0x1, 0x0, 0x5E)
    OP_43(0x13, 0x1, 0x0, 0x5F)
    OP_43(0x14, 0x1, 0x0, 0x60)
    OP_43(0x15, 0x1, 0x0, 0x61)
    OP_43(0x16, 0x1, 0x0, 0x62)
    OP_43(0x17, 0x1, 0x0, 0x63)
    OP_43(0x18, 0x1, 0x0, 0x64)
    OP_43(0x19, 0x1, 0x0, 0x65)
    OP_43(0x1A, 0x1, 0x0, 0x66)
    OP_43(0x1B, 0x1, 0x0, 0x67)
    OP_43(0x1C, 0x1, 0x0, 0x68)
    OP_43(0x1D, 0x1, 0x0, 0x69)
    OP_43(0x1E, 0x1, 0x0, 0x6A)
    OP_43(0x1F, 0x1, 0x0, 0x6B)
    OP_43(0x20, 0x1, 0x0, 0x6C)
    OP_43(0x21, 0x1, 0x0, 0x6D)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x21, 0x1)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    SetMapFlags(0x10)
    OP_62(0x41, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x41)
    Sleep(500)

    ChrTalk(    #21
        0x41,
        "#5P……啊。\x02",
    )

    CloseMessageWindow()

    def lambda_2844():
        OP_6D(-39000, 0, 125640, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2844)

    def lambda_285C():
        OP_67(0, 5520, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_285C)
    SetChrFlags(0x44, 0x20)
    SetChrFlags(0x44, 0x4)
    SetChrPos(0x44, -39060, 1500, 130190, 180)
    OP_9F(0x44, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x44, 0x80)
    OP_22(0x99, 0x0, 0x64)
    SetChrFlags(0x44, 0x20)

    def lambda_28A9():
        OP_8F(0xFE, 0xFFFF676C, 0x0, 0x1FC8E, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x44, 1, lambda_28A9)
    OP_9F(0x44, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x44, 0x1)
    ClearChrFlags(0x44, 0x20)

    ChrTalk(    #22
        0x44,
        "#230F──这就是所谓的“世事如梦幻”。\x02",
    )

    CloseMessageWindow()
    OP_62(0x41, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x41, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_2937():
        OP_8C(0xFE, 0, 600)
        ExitThread()

    QueueWorkItem(0x41, 1, lambda_2937)
    WaitChrThread(0x41, 0x1)

    ChrTalk(    #23
        0x41,
        "#5P啊……\x02",
    )

    CloseMessageWindow()
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
    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0x2713, 0x300012, 0x0, 0x0, 0xFF)
    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 18)
    Return()

    # Function_17_24BE end

    def Function_18_29D7(): pass

    label("Function_18_29D7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_44(0x44, 0x1)
    OP_D2(0x702FC, 0x70303, 0x0)
    OP_D2(0x702FD, 0x70304, 0x1)
    OP_D2(0x2701C9, 0x2701CE, 0x17)
    OP_D2(0x2701C6, 0x2701CB, 0x18)
    OP_D2(0x260003, 0x260008, 0x19)
    OP_D2(0x2701C8, 0x2701CD, 0x1A)
    OP_D2(0x702EE, 0x702F5, 0x2)
    OP_D2(0x702EF, 0x702F6, 0x3)
    OP_D2(0x70302, 0x70309, 0x4)
    OP_D2(0x702F1, 0x702F8, 0x5)
    OP_D2(0x60053, 0x60058, 0x6)
    OP_D2(0x70300, 0x70307, 0x7)
    OP_D2(0x26000D, 0x260012, 0x8)
    OP_D2(0x290142, 0x290146, 0x9)
    OP_D2(0x290143, 0x290147, 0xA)
    OP_D2(0x29014C, 0x290150, 0xB)
    OP_D2(0x29014D, 0x290151, 0xC)
    OP_D2(0x26000E, 0x260013, 0xD)
    OP_D2(0x2600A0, 0x2600A5, 0xE)
    OP_D2(0x260096, 0x26009B, 0xF)
    OP_D2(0x26024A, 0x26024F, 0x1B)
    ClearChrFlags(0x45, 0x80)
    ClearChrFlags(0x46, 0x80)
    ClearChrFlags(0x47, 0x80)
    SetChrPos(0x45, -38410, 0, 118740, 0)
    SetChrPos(0x46, -36890, 0, 117820, 0)
    SetChrPos(0x47, -39620, 0, 117750, 0)
    SetChrChipByIndex(0x46, 25)
    SetChrChipByIndex(0x47, 26)
    SetChrChipByIndex(0x45, 14)
    SetChrSubChip(0x45, 0)
    ClearChrFlags(0x44, 0x80)
    SetChrPos(0x44, -38760, 0, 123350, 180)
    SetChrChipByIndex(0x44, 23)
    LoadEffect(0x0, "map\\\\mp021_00.eff")
    OP_A1(0x48, 0x0)
    OP_A1(0x49, 0x1)
    OP_72(0x0, 0x4)
    OP_72(0x1, 0x4)
    SetChrPos(0x48, -39020, 0, 97470, 0)
    SetChrPos(0x49, -39020, 100, 98470, 0)
    OP_72(0x0, 0x20)
    OP_6F(0x0, 1100)
    Call(0, 23)
    ClearChrFlags(0x41, 0x80)
    SetChrPos(0x41, -38950, 0, 125450, 0)
    SetChrSubChip(0x41, 0)
    SetChrChipByIndex(0x41, 7)
    OP_6D(-38720, 0, 124180, 0)
    OP_67(0, 6440, -10000, 0)
    OP_6B(1910, 0)
    OP_6C(134000, 0)
    OP_6E(428, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_99(0x41, 0x0, 0x3, 0x5DC)
    Fade(250)
    OP_22(0x20C, 0x0, 0x64)
    ClearChrFlags(0x41, 0x1)
    SetChrPos(0x41, -39500, 0, 126600, 0)
    SetChrSubChip(0x41, 0)
    SetChrChipByIndex(0x41, 20)
    Sleep(1500)

    def lambda_2C29():
        OP_6D(-37580, 0, 118220, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2C29)

    def lambda_2C41():
        OP_6B(2000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2C41)

    def lambda_2C51():
        OP_8E(0xFE, 0xFFFF6B4A, 0x0, 0x1D72C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x44, 0, lambda_2C51)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x44, 0x0)

    ChrTalk(    #24
        0x45,
        "#254F#2P哼哼，一群小杂鱼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x46,
        (
            "#266F真是的……\x01",
            "也太不禁打了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x47,
        (
            "#241F#2P呵呵……别要求太高。\x02\x03",

            "算了，不知女王陛下的亲卫队\x01",
            "能不能给我们一点惊喜呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x44,
        (
            "#230F#6P嗯，但愿如此啊。\x02\x03",

            "#231F……那么……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)

    def lambda_2D49():
        OP_6D(-37380, 0, 116150, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2D49)

    def lambda_2D61():
        OP_8E(0xFE, 0xFFFF6BFE, 0x0, 0x1C75A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x44, 0, lambda_2D61)

    def lambda_2D7C():

        label("loc_2D7C")

        TurnDirection(0xFE, 0x44, 400)
        OP_48()
        Jump("loc_2D7C")

    QueueWorkItem2(0x46, 2, lambda_2D7C)

    def lambda_2D8D():

        label("loc_2D8D")

        TurnDirection(0xFE, 0x44, 400)
        OP_48()
        Jump("loc_2D8D")

    QueueWorkItem2(0x47, 2, lambda_2D8D)
    Sleep(100)
    OP_43(0x45, 0x0, 0x0, 0x15)
    WaitChrThread(0x44, 0x0)
    OP_44(0x46, 0x2)
    OP_44(0x47, 0x2)
    OP_44(0x45, 0x2)

    def lambda_2DBB():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x46, 1, lambda_2DBB)

    def lambda_2DC9():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x47, 1, lambda_2DC9)
    OP_8C(0x45, 180, 400)
    WaitChrThread(0x101, 0x0)
    PlayEffect(0x0, 0x0, 0x48, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x79, 0x1, 0x64)
    OP_22(0xCC, 0x0, 0x64)

    def lambda_2E22():
        OP_6D(-38930, 0, 112070, 6000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2E22)

    def lambda_2E3A():
        OP_67(0, 10930, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2E3A)

    def lambda_2E52():
        OP_6B(1370, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2E52)

    def lambda_2E62():
        OP_6E(578, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2E62)

    def lambda_2E72():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x45, 1, lambda_2E72)
    Sleep(100)

    def lambda_2E85():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x46, 1, lambda_2E85)
    Sleep(100)

    def lambda_2E98():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x47, 1, lambda_2E98)
    Sleep(1800)
    OP_43(0x48, 0x3, 0x0, 0x16)

    def lambda_2EB2():
        OP_8E(0xFE, 0xFFFF6794, 0x2710, 0x19FE6, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x48, 1, lambda_2EB2)

    def lambda_2ECD():
        OP_8E(0xFE, 0xFFFF6794, 0x0, 0x19FE6, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x49, 1, lambda_2ECD)
    Sleep(1000)

    def lambda_2EED():
        OP_8E(0xFE, 0xFFFF6794, 0x2710, 0x19FE6, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x48, 1, lambda_2EED)

    def lambda_2F08():
        OP_8E(0xFE, 0xFFFF6794, 0x0, 0x19FE6, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x49, 1, lambda_2F08)
    Sleep(2000)

    def lambda_2F28():
        OP_8E(0xFE, 0xFFFF6794, 0x2710, 0x1C6F6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x48, 1, lambda_2F28)

    def lambda_2F43():
        OP_8E(0xFE, 0xFFFF6794, 0x0, 0x1C6F6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x49, 1, lambda_2F43)
    Sleep(2000)

    def lambda_2F63():
        OP_8E(0xFE, 0xFFFF6794, 0x2710, 0x23C26, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x48, 1, lambda_2F63)

    def lambda_2F7E():
        OP_8E(0xFE, 0xFFFF6794, 0x0, 0x23C26, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x49, 1, lambda_2F7E)
    OP_82(0x0, 0x2)
    OP_23(0xCC)
    OP_43(0x28, 0x2, 0x0, 0x6E)
    OP_43(0x28, 0x3, 0x0, 0x70)
    WaitChrThread(0x28, 0x2)
    OP_44(0x28, 0x3)
    OP_23(0x13A)
    WaitChrThread(0x101, 0x0)
    Fade(500)
    OP_6D(-37770, 0, 112810, 0)
    OP_67(0, 6180, -10000, 0)
    OP_6B(1900, 0)
    OP_6C(134000, 0)
    OP_6E(470, 0)
    OP_23(0x79)
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x7, 0x4)
    OP_71(0x9, 0x4)
    OP_0D()
    Sleep(500)

    ChrTalk(    #28
        0x44,
        (
            "#234F#6P我们执行者现在\x01",
            "开始前往格兰赛尔城！\x02\x03",

            "你们就照原定计划，\x01",
            "格兰赛尔的市区！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    SetMessageWindowPos(350, 100, -1, -1)
    SetChrName("强化猎兵们")

    AnonymousTalk(    #29
        "\x07\x00#5S明白了！！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30DC")
    OP_A2(0x10F3)
    NewScene("ED6_DT21/R4101   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_30E8")

    label("loc_30DC")

    OP_A2(0x10F3)
    NewScene("ED6_DT21/R4101   ._SN", 101, 0, 0)
    IdleLoop()

    label("loc_30E8")

    Return()

    # Function_18_29D7 end

    def Function_19_30E9(): pass

    label("Function_19_30E9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-5000, 0, 7380, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -5000, 0, 7380, 0)
    SetChrPos(0x1, -5000, 0, 7380, 0)
    SetChrPos(0x2, -5000, 0, 7380, 0)
    SetChrPos(0x3, -5000, 0, 7380, 0)
    OP_69(0x0, 0x0)
    OP_A2(0x2039)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_19_30E9 end

    def Function_20_3196(): pass

    label("Function_20_3196")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(46870, 0, 83250, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 46870, 0, 83250, 270)
    SetChrPos(0x1, 46870, 0, 83250, 270)
    SetChrPos(0x2, 46870, 0, 83250, 270)
    SetChrPos(0x3, 46870, 0, 83250, 270)
    OP_69(0x0, 0x0)
    OP_A2(0x2039)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_20_3196 end

    def Function_21_3243(): pass

    label("Function_21_3243")

    SetChrChipByIndex(0xFE, 24)
    OP_8C(0xFE, 90, 400)
    OP_8F(0xFE, 0xFFFF6802, 0x0, 0x1D0BA, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 14)
    Sleep(100)

    def lambda_3278():

        label("loc_3278")

        TurnDirection(0xFE, 0x44, 400)
        OP_48()
        Jump("loc_3278")

    QueueWorkItem2(0xFE, 2, lambda_3278)
    Return()

    # Function_21_3243 end

    def Function_22_3284(): pass

    label("Function_22_3284")

    OP_6F(0x0, 561)
    OP_70(0x0, 0x28A)
    OP_73(0x0)
    OP_6F(0x0, 651)
    OP_70(0x0, 0x2A8)
    OP_73(0x0)
    OP_71(0x0, 0x8)
    OP_6F(0x0, 680)
    OP_70(0x0, 0x30C)
    Return()

    # Function_22_3284 end

    def Function_23_32BA(): pass

    label("Function_23_32BA")

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
    SetChrFlags(0xA, 0x20)
    SetChrFlags(0xB, 0x20)
    SetChrFlags(0xC, 0x20)
    SetChrFlags(0xD, 0x20)
    SetChrFlags(0xE, 0x20)
    SetChrFlags(0xF, 0x20)
    SetChrFlags(0x10, 0x20)
    SetChrFlags(0x11, 0x20)
    SetChrFlags(0x12, 0x20)
    SetChrFlags(0x13, 0x20)
    SetChrFlags(0x14, 0x20)
    SetChrFlags(0x15, 0x20)
    SetChrFlags(0x16, 0x20)
    SetChrFlags(0x17, 0x20)
    SetChrFlags(0x18, 0x20)
    SetChrFlags(0x19, 0x20)
    SetChrFlags(0x1A, 0x20)
    SetChrFlags(0x1B, 0x20)
    SetChrFlags(0x1C, 0x20)
    SetChrFlags(0x1D, 0x20)
    SetChrFlags(0x1E, 0x20)
    SetChrFlags(0x1F, 0x20)
    SetChrFlags(0x20, 0x20)
    SetChrFlags(0x21, 0x20)
    ClearChrFlags(0xA, 0x1)
    ClearChrFlags(0xB, 0x1)
    ClearChrFlags(0xC, 0x1)
    ClearChrFlags(0xD, 0x1)
    ClearChrFlags(0xE, 0x1)
    ClearChrFlags(0xF, 0x1)
    ClearChrFlags(0x10, 0x1)
    ClearChrFlags(0x11, 0x1)
    ClearChrFlags(0x12, 0x1)
    ClearChrFlags(0x13, 0x1)
    ClearChrFlags(0x14, 0x1)
    ClearChrFlags(0x15, 0x1)
    ClearChrFlags(0x16, 0x1)
    ClearChrFlags(0x17, 0x1)
    ClearChrFlags(0x18, 0x1)
    ClearChrFlags(0x19, 0x1)
    ClearChrFlags(0x1A, 0x1)
    ClearChrFlags(0x1B, 0x1)
    ClearChrFlags(0x1C, 0x1)
    ClearChrFlags(0x1D, 0x1)
    ClearChrFlags(0x1E, 0x1)
    ClearChrFlags(0x1F, 0x1)
    ClearChrFlags(0x20, 0x1)
    ClearChrFlags(0x21, 0x1)
    SetChrChipByIndex(0xA, 19)
    SetChrChipByIndex(0xB, 27)
    SetChrChipByIndex(0xC, 19)
    SetChrChipByIndex(0xD, 19)
    SetChrChipByIndex(0xE, 27)
    SetChrChipByIndex(0xF, 19)
    SetChrChipByIndex(0x10, 27)
    SetChrChipByIndex(0x11, 19)
    SetChrChipByIndex(0x12, 19)
    SetChrChipByIndex(0x13, 27)
    SetChrChipByIndex(0x14, 27)
    SetChrChipByIndex(0x15, 19)
    SetChrChipByIndex(0x16, 19)
    SetChrChipByIndex(0x17, 27)
    SetChrChipByIndex(0x18, 27)
    SetChrChipByIndex(0x19, 19)
    SetChrChipByIndex(0x1A, 19)
    SetChrChipByIndex(0x1B, 27)
    SetChrChipByIndex(0x1C, 19)
    SetChrChipByIndex(0x1D, 27)
    SetChrChipByIndex(0x1E, 27)
    SetChrChipByIndex(0x1F, 19)
    SetChrChipByIndex(0x20, 27)
    SetChrChipByIndex(0x21, 19)
    SetChrPos(0xA, -32360, 0, 119050, 315)
    SetChrPos(0xB, -30880, 0, 120220, 90)
    SetChrPos(0xC, -32770, 0, 122700, 225)
    SetChrPos(0xD, -30610, 250, 124400, 270)
    SetChrPos(0xE, -30670, 250, 127190, 135)
    SetChrPos(0xF, -34040, 0, 126930, 45)
    SetChrPos(0x10, -29470, 250, 125310, 45)
    SetChrPos(0x11, -30310, 250, 127840, 0)
    SetChrPos(0x12, -44210, 0, 117600, 180)
    SetChrPos(0x13, -46380, 0, 119590, 225)
    SetChrPos(0x14, -44450, 0, 119820, 225)
    SetChrPos(0x15, -47450, 0, 121690, 45)
    SetChrPos(0x16, -43440, 0, 122980, 270)
    SetChrPos(0x17, -46070, 250, 125390, 135)
    SetChrPos(0x18, -49300, 0, 122100, 315)
    SetChrPos(0x19, -48780, 250, 125590, 180)
    SetChrPos(0x1A, -35240, 0, 125600, 135)
    SetChrPos(0x1B, -33350, 0, 124670, 45)
    SetChrPos(0x1C, -36960, 0, 125620, 180)
    SetChrPos(0x1D, -36270, 0, 128990, 0)
    SetChrPos(0x1E, -42380, 0, 125390, 315)
    SetChrPos(0x1F, -41140, 0, 127160, 0)
    SetChrPos(0x20, -42200, 0, 123740, 270)
    SetChrPos(0x21, -43690, 0, 127730, 180)
    Return()

    # Function_23_32BA end

    def Function_24_3633(): pass

    label("Function_24_3633")


    def lambda_3639():
        OP_8E(0xFE, 0xFFFF6794, 0x2710, 0x151C6, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x48, 2, lambda_3639)

    def lambda_3654():
        OP_8E(0xFE, 0xFFFF6794, 0x64, 0x151C6, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x49, 2, lambda_3654)
    Sleep(1000)

    def lambda_3674():
        OP_8E(0xFE, 0xFFFF6794, 0x2710, 0x151C6, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x48, 2, lambda_3674)

    def lambda_368F():
        OP_8E(0xFE, 0xFFFF6794, 0x64, 0x151C6, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x49, 2, lambda_368F)
    Sleep(500)

    def lambda_36AF():
        OP_8E(0xFE, 0xFFFF6794, 0x2710, 0x151C6, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x48, 2, lambda_36AF)

    def lambda_36CA():
        OP_8E(0xFE, 0xFFFF6794, 0x64, 0x151C6, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x49, 2, lambda_36CA)
    Sleep(500)

    def lambda_36EA():
        OP_8E(0xFE, 0xFFFF6794, 0x2710, 0x151C6, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0x48, 2, lambda_36EA)

    def lambda_3705():
        OP_8E(0xFE, 0xFFFF6794, 0x64, 0x151C6, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0x49, 2, lambda_3705)
    WaitChrThread(0x48, 0x2)

    def lambda_3725():
        OP_8E(0xFE, 0xFFFF6794, 0x0, 0x17CBE, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0x48, 2, lambda_3725)

    def lambda_3740():
        OP_8E(0xFE, 0xFFFF6794, 0x64, 0x17CBE, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0x49, 2, lambda_3740)
    Sleep(1000)

    def lambda_3760():
        OP_8E(0xFE, 0xFFFF6794, 0x0, 0x17CBE, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x48, 2, lambda_3760)

    def lambda_377B():
        OP_8E(0xFE, 0xFFFF6794, 0x64, 0x17CBE, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x49, 2, lambda_377B)
    Sleep(1000)

    def lambda_379B():
        OP_8E(0xFE, 0xFFFF6794, 0x0, 0x17CBE, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x48, 2, lambda_379B)

    def lambda_37B6():
        OP_8E(0xFE, 0xFFFF6794, 0x64, 0x180A6, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x49, 2, lambda_37B6)
    PlayEffect(0x0, 0x0, 0x48, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xCC, 0x0, 0x64)
    OP_44(0x101, 0x1)
    OP_44(0x101, 0x2)
    OP_44(0x101, 0x3)
    Fade(500)
    OP_6D(-38120, 6130, 109760, 0)
    OP_67(0, 4550, -10000, 0)
    OP_6B(2300, 0)
    OP_6C(134000, 0)
    OP_6E(473, 0)
    OP_43(0x48, 0x3, 0x0, 0x19)
    OP_0D()

    def lambda_3861():
        OP_6D(-38120, 0, 109760, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3861)
    Sleep(1500)
    OP_43(0x44, 0x1, 0x0, 0x1A)
    Sleep(100)
    OP_43(0x45, 0x1, 0x0, 0x1C)
    Sleep(100)
    OP_43(0x46, 0x1, 0x0, 0x1B)
    Sleep(100)
    OP_43(0x47, 0x1, 0x0, 0x1D)
    WaitChrThread(0x48, 0x2)
    WaitChrThread(0x48, 0x3)
    OP_82(0x0, 0x2)
    OP_23(0xCC)
    OP_23(0x79)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x64, 0x0, 0x1388, 0x3E8)
    Return()

    # Function_24_3633 end

    def Function_25_38CD(): pass

    label("Function_25_38CD")

    OP_72(0x0, 0x20)
    OP_73(0x0)
    OP_6F(0x0, 1021)
    OP_70(0x0, 0x44C)
    OP_73(0x0)
    Return()

    # Function_25_38CD end

    def Function_26_38E7(): pass

    label("Function_26_38E7")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x44, 0x80)
    ClearChrFlags(0x44, 0x1)
    OP_7D(0x0, 0x44, 0x32, 0x1F4)

    def lambda_390A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_390A)
    OP_22(0x99, 0x0, 0x64)
    OP_96(0x44, 0xFFFF65BE, 0x0, 0x1B7E2, 0xBB8, 0x1388)
    SetChrChipByIndex(0x44, 9)
    SetChrSubChip(0x44, 0)
    OP_22(0xA4, 0x0, 0x64)
    OP_7D(0x1, 0x44, 0x0, 0x0)
    SetChrFlags(0x44, 0x1)
    Return()

    # Function_26_38E7 end

    def Function_27_394F(): pass

    label("Function_27_394F")

    Sleep(100)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x46, 0x80)
    ClearChrFlags(0x46, 0x1)
    OP_7D(0x0, 0x46, 0x32, 0x1F4)

    def lambda_3977():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3977)
    OP_22(0x99, 0x0, 0x64)
    OP_96(0x46, 0xFFFF6D52, 0x0, 0x1B56C, 0xBB8, 0x1388)
    SetChrChipByIndex(0x46, 25)
    SetChrSubChip(0x46, 0)
    OP_22(0xA4, 0x0, 0x64)
    OP_7D(0x1, 0x46, 0x0, 0x0)
    SetChrFlags(0x46, 0x1)
    Return()

    # Function_27_394F end

    def Function_28_39BC(): pass

    label("Function_28_39BC")

    Sleep(200)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x45, 0x80)
    ClearChrFlags(0x45, 0x1)
    OP_7D(0x0, 0x45, 0x32, 0x1F4)

    def lambda_39E4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_39E4)
    OP_22(0x99, 0x0, 0x64)
    OP_96(0x45, 0xFFFF67A8, 0x0, 0x1AF0E, 0xBB8, 0x1388)
    SetChrChipByIndex(0x45, 11)
    SetChrSubChip(0x45, 0)
    OP_22(0xA4, 0x0, 0x64)
    OP_7D(0x1, 0x45, 0x0, 0x0)
    SetChrFlags(0x45, 0x1)
    Return()

    # Function_28_39BC end

    def Function_29_3A29(): pass

    label("Function_29_3A29")

    Sleep(300)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x47, 0x80)
    ClearChrFlags(0x47, 0x1)
    OP_7D(0x0, 0x47, 0x32, 0x1F4)

    def lambda_3A51():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3A51)
    OP_22(0x99, 0x0, 0x64)
    OP_96(0x47, 0xFFFF6050, 0x0, 0x1B080, 0xBB8, 0x1388)
    SetChrChipByIndex(0x47, 26)
    SetChrSubChip(0x47, 0)
    OP_22(0xA4, 0x0, 0x64)
    OP_7D(0x1, 0x47, 0x0, 0x0)
    SetChrFlags(0x47, 0x1)
    Return()

    # Function_29_3A29 end

    def Function_30_3A96(): pass

    label("Function_30_3A96")

    OP_91(0xFE, 0x0, 0x0, 0x186A0, 0x7530, 0x0)
    OP_71(0x7, 0x4)
    Return()

    # Function_30_3A96 end

    def Function_31_3AB0(): pass

    label("Function_31_3AB0")

    OP_91(0xFE, 0x0, 0x0, 0x186A0, 0x7530, 0x0)
    OP_71(0x9, 0x4)
    Return()

    # Function_31_3AB0 end

    def Function_32_3ACA(): pass

    label("Function_32_3ACA")

    SetChrFlags(0xFE, 0x40)
    SetChrChipByIndex(0xFE, 3)
    SetChrPos(0xFE, -37450, 0, 134600, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF8243, 0x0, 0x1D09C, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 2)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_32_3ACA end

    def Function_33_3B0B(): pass

    label("Function_33_3B0B")

    SetChrFlags(0xFE, 0x40)
    SetChrChipByIndex(0xFE, 3)
    Sleep(400)
    SetChrPos(0xFE, -37450, 0, 134600, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF86DE, 0x0, 0x1D524, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 2)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_33_3B0B end

    def Function_34_3B51(): pass

    label("Function_34_3B51")

    SetChrFlags(0xFE, 0x40)
    SetChrChipByIndex(0xFE, 3)
    Sleep(800)
    SetChrPos(0xFE, -37450, 0, 134600, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF7F2C, 0x0, 0x1D6D2, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 2)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_34_3B51 end

    def Function_35_3B97(): pass

    label("Function_35_3B97")

    SetChrFlags(0xFE, 0x40)
    SetChrChipByIndex(0xFE, 3)
    Sleep(1200)
    SetChrPos(0xFE, -37450, 0, 134600, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF8346, 0x0, 0x1DABA, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 2)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_35_3B97 end

    def Function_36_3BDD(): pass

    label("Function_36_3BDD")

    SetChrFlags(0xFE, 0x40)
    SetChrChipByIndex(0xFE, 3)
    Sleep(1600)
    SetChrPos(0xFE, -37450, 0, 133600, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF7C5C, 0x0, 0x1DBDC, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 2)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_36_3BDD end

    def Function_37_3C23(): pass

    label("Function_37_3C23")

    SetChrFlags(0xFE, 0x40)
    SetChrChipByIndex(0xFE, 3)
    Sleep(2000)
    SetChrPos(0xFE, -37450, 0, 134600, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF7FFE, 0x0, 0x1E078, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 2)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_37_3C23 end

    def Function_38_3C69(): pass

    label("Function_38_3C69")

    SetChrFlags(0xFE, 0x40)
    SetChrChipByIndex(0xFE, 3)
    Sleep(2400)
    SetChrPos(0xFE, -37450, 0, 134600, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF79FA, 0x0, 0x1E0B4, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 2)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_38_3C69 end

    def Function_39_3CAF(): pass

    label("Function_39_3CAF")

    SetChrFlags(0xFE, 0x40)
    SetChrChipByIndex(0xFE, 3)
    Sleep(2800)
    SetChrPos(0xFE, -37450, 0, 134600, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF7DB0, 0x0, 0x1E582, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 2)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_39_3CAF end

    def Function_40_3CF5(): pass

    label("Function_40_3CF5")

    SetChrFlags(0xFE, 0x40)
    SetChrChipByIndex(0xFE, 3)
    Sleep(50)
    SetChrPos(0xFE, -40590, 0, 134600, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF4FC0, 0x0, 0x1CFDE, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 2)
    OP_8C(0xFE, 135, 400)
    Return()

    # Function_40_3CF5 end

    def Function_41_3D3B(): pass

    label("Function_41_3D3B")

    SetChrFlags(0xFE, 0x40)
    SetChrChipByIndex(0xFE, 3)
    Sleep(450)
    SetChrPos(0xFE, -40590, 0, 134600, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF4B38, 0x0, 0x1D48E, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 2)
    OP_8C(0xFE, 135, 400)
    Return()

    # Function_41_3D3B end

    def Function_42_3D81(): pass

    label("Function_42_3D81")

    SetChrFlags(0xFE, 0x40)
    SetChrChipByIndex(0xFE, 3)
    Sleep(850)
    SetChrPos(0xFE, -40590, 0, 134600, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF5236, 0x0, 0x1D664, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 2)
    OP_8C(0xFE, 135, 400)
    Return()

    # Function_42_3D81 end

    def Function_43_3DC7(): pass

    label("Function_43_3DC7")

    SetChrFlags(0xFE, 0x40)
    SetChrChipByIndex(0xFE, 3)
    Sleep(1250)
    SetChrPos(0xFE, -40590, 0, 134600, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF4D90, 0x0, 0x1DA42, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 2)
    OP_8C(0xFE, 135, 400)
    Return()

    # Function_43_3DC7 end

    def Function_44_3E0D(): pass

    label("Function_44_3E0D")

    SetChrFlags(0xFE, 0x40)
    SetChrChipByIndex(0xFE, 3)
    Sleep(1650)
    SetChrPos(0xFE, -40590, 0, 134600, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF54FC, 0x0, 0x1DCA4, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 2)
    OP_8C(0xFE, 135, 400)
    Return()

    # Function_44_3E0D end

    def Function_45_3E53(): pass

    label("Function_45_3E53")

    SetChrFlags(0xFE, 0x40)
    SetChrChipByIndex(0xFE, 3)
    Sleep(2050)
    SetChrPos(0xFE, -40590, 0, 134600, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF4FD4, 0x0, 0x1E064, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 2)
    OP_8C(0xFE, 135, 400)
    Return()

    # Function_45_3E53 end

    def Function_46_3E99(): pass

    label("Function_46_3E99")

    SetChrFlags(0xFE, 0x40)
    SetChrChipByIndex(0xFE, 3)
    Sleep(2450)
    SetChrPos(0xFE, -40590, 0, 134600, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF57CC, 0x64, 0x1E1EA, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 2)
    OP_8C(0xFE, 135, 400)
    Return()

    # Function_46_3E99 end

    def Function_47_3EDF(): pass

    label("Function_47_3EDF")

    SetChrFlags(0xFE, 0x40)
    SetChrChipByIndex(0xFE, 3)
    Sleep(2850)
    SetChrPos(0xFE, -40590, 0, 134600, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF536C, 0x0, 0x1E668, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 2)
    OP_8C(0xFE, 135, 400)
    Return()

    # Function_47_3EDF end

    def Function_48_3F25(): pass

    label("Function_48_3F25")

    SetChrFlags(0xFE, 0x40)
    SetChrChipByIndex(0xFE, 3)
    Sleep(100)
    SetChrPos(0xFE, -38990, 0, 134600, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF7284, 0x0, 0x1E1E0, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 2)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_48_3F25 end

    def Function_49_3F6B(): pass

    label("Function_49_3F6B")

    SetChrFlags(0xFE, 0x40)
    SetChrChipByIndex(0xFE, 3)
    Sleep(500)
    SetChrPos(0xFE, -38990, 0, 134600, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF6C80, 0x0, 0x1E316, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 2)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_49_3F6B end

    def Function_50_3FB1(): pass

    label("Function_50_3FB1")

    SetChrFlags(0xFE, 0x40)
    SetChrChipByIndex(0xFE, 3)
    Sleep(900)
    SetChrPos(0xFE, -38990, 0, 134600, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF651E, 0x0, 0x1E302, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 2)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_50_3FB1 end

    def Function_51_3FF7(): pass

    label("Function_51_3FF7")

    SetChrFlags(0xFE, 0x40)
    SetChrChipByIndex(0xFE, 3)
    Sleep(1300)
    SetChrPos(0xFE, -38990, 0, 134600, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF5E52, 0x0, 0x1E24E, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 2)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_51_3FF7 end

    def Function_52_403D(): pass

    label("Function_52_403D")

    SetChrFlags(0xFE, 0x40)
    SetChrChipByIndex(0xFE, 3)
    Sleep(1700)
    SetChrPos(0xFE, -38990, 0, 134600, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF73C4, 0x0, 0x1E73A, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 2)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_52_403D end

    def Function_53_4083(): pass

    label("Function_53_4083")

    SetChrFlags(0xFE, 0x40)
    SetChrChipByIndex(0xFE, 3)
    Sleep(2100)
    SetChrPos(0xFE, -38990, 0, 134600, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF6DE8, 0x0, 0x1E852, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 2)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_53_4083 end

    def Function_54_40C9(): pass

    label("Function_54_40C9")

    SetChrFlags(0xFE, 0x40)
    SetChrChipByIndex(0xFE, 3)
    Sleep(2500)
    SetChrPos(0xFE, -38990, 0, 134600, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF6438, 0x0, 0x1E85C, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 2)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_54_40C9 end

    def Function_55_410F(): pass

    label("Function_55_410F")

    SetChrFlags(0xFE, 0x40)
    SetChrChipByIndex(0xFE, 3)
    Sleep(2900)
    SetChrPos(0xFE, -38990, 0, 134600, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF5CAE, 0x0, 0x1E7C6, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 2)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_55_410F end

    def Function_56_4155(): pass

    label("Function_56_4155")

    SetChrFlags(0xFE, 0x40)
    SetChrChipByIndex(0xFE, 1)
    Sleep(3200)
    SetChrPos(0xFE, -38450, 0, 134600, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF699C, 0x0, 0x1EBF4, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_56_4155 end

    def Function_57_419B(): pass

    label("Function_57_419B")

    SetChrFlags(0xFE, 0x40)
    SetChrChipByIndex(0xFE, 1)
    Sleep(3550)
    SetChrPos(0xFE, -38590, 0, 134600, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF6B7C, 0x0, 0x1F427, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_57_419B end

    def Function_58_41E1(): pass

    label("Function_58_41E1")

    SetChrFlags(0xFE, 0x40)
    SetChrChipByIndex(0xFE, 1)
    Sleep(3600)
    SetChrPos(0xFE, -39990, 0, 134600, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF6424, 0x0, 0x1F409, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_58_41E1 end

    def Function_59_4227(): pass

    label("Function_59_4227")

    SetChrChipByIndex(0xFE, 24)
    OP_8E(0xFE, 0xFFFF6B5E, 0x0, 0x1D43E, 0x1388, 0x0)
    Return()

    # Function_59_4227 end

    def Function_60_4241(): pass

    label("Function_60_4241")

    Sleep(30)
    OP_8E(0xFE, 0xFFFF75EA, 0x0, 0x1CF34, 0x1388, 0x0)
    Return()

    # Function_60_4241 end

    def Function_61_425B(): pass

    label("Function_61_425B")

    Sleep(20)
    OP_8E(0xFE, 0xFFFF5E0C, 0x0, 0x1CD18, 0x1388, 0x0)
    Return()

    # Function_61_425B end

    def Function_62_4275(): pass

    label("Function_62_4275")

    Sleep(20)
    SetChrChipByIndex(0xFE, 3)
    OP_8C(0xFE, 270, 0)
    OP_8E(0xFE, 0xFFFF7B58, 0x0, 0x1CA48, 0x1388, 0x0)
    Return()

    # Function_62_4275 end

    def Function_63_429B(): pass

    label("Function_63_429B")

    Sleep(40)
    SetChrChipByIndex(0xFE, 3)
    OP_8C(0xFE, 270, 0)
    OP_8E(0xFE, 0xFFFF7B58, 0x0, 0x1CA48, 0x1388, 0x0)
    Return()

    # Function_63_429B end

    def Function_64_42C1(): pass

    label("Function_64_42C1")

    Sleep(50)
    SetChrChipByIndex(0xFE, 3)
    OP_8C(0xFE, 270, 0)
    OP_8E(0xFE, 0xFFFF7978, 0x0, 0x1CE44, 0x1388, 0x0)
    Return()

    # Function_64_42C1 end

    def Function_65_42E7(): pass

    label("Function_65_42E7")

    Sleep(40)
    SetChrChipByIndex(0xFE, 3)
    OP_8C(0xFE, 270, 0)
    OP_8E(0xFE, 0xFFFF7978, 0x0, 0x1CE44, 0x1388, 0x0)
    Return()

    # Function_65_42E7 end

    def Function_66_430D(): pass

    label("Function_66_430D")

    Sleep(30)
    SetChrChipByIndex(0xFE, 3)
    OP_8C(0xFE, 270, 0)
    OP_8E(0xFE, 0xFFFF7798, 0x0, 0x1D272, 0x1388, 0x0)
    Return()

    # Function_66_430D end

    def Function_67_4333(): pass

    label("Function_67_4333")

    Sleep(80)
    SetChrChipByIndex(0xFE, 3)
    OP_8C(0xFE, 270, 0)
    OP_8E(0xFE, 0xFFFF7798, 0x0, 0x1D272, 0x1388, 0x0)
    Return()

    # Function_67_4333 end

    def Function_68_4359(): pass

    label("Function_68_4359")

    Sleep(20)
    SetChrChipByIndex(0xFE, 3)
    OP_8C(0xFE, 270, 0)
    OP_8E(0xFE, 0xFFFF74AA, 0x0, 0x1D47A, 0x1388, 0x0)
    Return()

    # Function_68_4359 end

    def Function_69_437F(): pass

    label("Function_69_437F")

    Sleep(40)
    SetChrChipByIndex(0xFE, 3)
    OP_8C(0xFE, 270, 0)
    OP_8E(0xFE, 0xFFFF74AA, 0x0, 0x1D47A, 0x1388, 0x0)
    Return()

    # Function_69_437F end

    def Function_70_43A5(): pass

    label("Function_70_43A5")

    Sleep(10)
    SetChrChipByIndex(0xFE, 3)
    OP_8C(0xFE, 90, 0)
    OP_8E(0xFE, 0xFFFF5948, 0x0, 0x1C926, 0x1388, 0x0)
    Return()

    # Function_70_43A5 end

    def Function_71_43CB(): pass

    label("Function_71_43CB")

    Sleep(50)
    SetChrChipByIndex(0xFE, 3)
    OP_8C(0xFE, 90, 0)
    OP_8E(0xFE, 0xFFFF5948, 0x0, 0x1C926, 0x1388, 0x0)
    Return()

    # Function_71_43CB end

    def Function_72_43F1(): pass

    label("Function_72_43F1")

    Sleep(80)
    SetChrChipByIndex(0xFE, 3)
    OP_8C(0xFE, 90, 0)
    OP_8E(0xFE, 0xFFFF5B6E, 0x0, 0x1CCB4, 0x1388, 0x0)
    Return()

    # Function_72_43F1 end

    def Function_73_4417(): pass

    label("Function_73_4417")

    Sleep(20)
    SetChrChipByIndex(0xFE, 3)
    OP_8C(0xFE, 90, 0)
    OP_8E(0xFE, 0xFFFF5B6E, 0x0, 0x1CCB4, 0x1388, 0x0)
    Return()

    # Function_73_4417 end

    def Function_74_443D(): pass

    label("Function_74_443D")

    Sleep(40)
    SetChrChipByIndex(0xFE, 3)
    OP_8C(0xFE, 90, 0)
    OP_8E(0xFE, 0xFFFF5CB8, 0x0, 0x1CF70, 0x1388, 0x0)
    Return()

    # Function_74_443D end

    def Function_75_4463(): pass

    label("Function_75_4463")

    Sleep(90)
    SetChrChipByIndex(0xFE, 3)
    OP_8C(0xFE, 90, 0)
    OP_8E(0xFE, 0xFFFF5CB8, 0x0, 0x1CF70, 0x1388, 0x0)
    Return()

    # Function_75_4463 end

    def Function_76_4489(): pass

    label("Function_76_4489")

    Sleep(80)
    SetChrChipByIndex(0xFE, 3)
    OP_8C(0xFE, 90, 0)
    OP_8E(0xFE, 0xFFFF5EF2, 0x0, 0x1D330, 0x1388, 0x0)
    Return()

    # Function_76_4489 end

    def Function_77_44AF(): pass

    label("Function_77_44AF")

    Sleep(60)
    SetChrChipByIndex(0xFE, 3)
    OP_8C(0xFE, 90, 0)
    OP_8E(0xFE, 0xFFFF5EF2, 0x0, 0x1D330, 0x1388, 0x0)
    Return()

    # Function_77_44AF end

    def Function_78_44D5(): pass

    label("Function_78_44D5")

    Sleep(20)
    SetChrChipByIndex(0xFE, 3)
    OP_8E(0xFE, 0xFFFF7004, 0x0, 0x1D5B0, 0x1388, 0x0)
    Return()

    # Function_78_44D5 end

    def Function_79_44F4(): pass

    label("Function_79_44F4")

    Sleep(40)
    SetChrChipByIndex(0xFE, 3)
    OP_8E(0xFE, 0xFFFF6C30, 0x0, 0x1D704, 0x1388, 0x0)
    Return()

    # Function_79_44F4 end

    def Function_80_4513(): pass

    label("Function_80_4513")

    Sleep(50)
    SetChrChipByIndex(0xFE, 3)
    OP_8E(0xFE, 0xFFFF6834, 0x0, 0x1D6D2, 0x1388, 0x0)
    Return()

    # Function_80_4513 end

    def Function_81_4532(): pass

    label("Function_81_4532")

    Sleep(60)
    SetChrChipByIndex(0xFE, 3)
    OP_8E(0xFE, 0xFFFF6456, 0x0, 0x1D61E, 0x1388, 0x0)
    Return()

    # Function_81_4532 end

    def Function_82_4551(): pass

    label("Function_82_4551")

    Sleep(50)
    SetChrChipByIndex(0xFE, 3)
    OP_8E(0xFE, 0xFFFF7004, 0x0, 0x1D5B0, 0x1388, 0x0)
    Return()

    # Function_82_4551 end

    def Function_83_4570(): pass

    label("Function_83_4570")

    Sleep(80)
    SetChrChipByIndex(0xFE, 3)
    OP_8E(0xFE, 0xFFFF6C30, 0x0, 0x1D704, 0x1388, 0x0)
    Return()

    # Function_83_4570 end

    def Function_84_458F(): pass

    label("Function_84_458F")

    Sleep(10)
    SetChrChipByIndex(0xFE, 3)
    OP_8E(0xFE, 0xFFFF6834, 0x0, 0x1D6D2, 0x1388, 0x0)
    Return()

    # Function_84_458F end

    def Function_85_45AE(): pass

    label("Function_85_45AE")

    Sleep(90)
    SetChrChipByIndex(0xFE, 3)
    OP_8E(0xFE, 0xFFFF6456, 0x0, 0x1D61E, 0x1388, 0x0)
    Return()

    # Function_85_45AE end

    def Function_86_45CD(): pass

    label("Function_86_45CD")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -34880, 0, 119870, 270)
    Sleep(200)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 5)
    SetChrSubChip(0xFE, 0)
    OP_22(0x209, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_96(0xFE, 0xFFFF8198, 0x0, 0x1D10A, 0xFA0, 0xFA0)
    ClearChrFlags(0xFE, 0x1)
    OP_8C(0xFE, 315, 0)
    SetChrChipByIndex(0xFE, 19)
    OP_22(0x20C, 0x0, 0x64)
    Return()

    # Function_86_45CD end

    def Function_87_463B(): pass

    label("Function_87_463B")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -33980, 0, 120510, 270)
    Sleep(400)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 5)
    SetChrSubChip(0xFE, 0)
    OP_22(0x209, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_96(0xFE, 0xFFFF8760, 0x0, 0x1D59C, 0xFA0, 0xFA0)
    ClearChrFlags(0xFE, 0x1)
    OP_8C(0xFE, 90, 0)
    SetChrChipByIndex(0xFE, 27)
    OP_22(0x20C, 0x0, 0x64)
    Return()

    # Function_87_463B end

    def Function_88_46A9(): pass

    label("Function_88_46A9")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -34870, 0, 121180, 225)
    Sleep(500)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 5)
    SetChrSubChip(0xFE, 0)
    OP_22(0x209, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_96(0xFE, 0xFFFF7FFE, 0x0, 0x1DF4C, 0xFA0, 0xFA0)
    ClearChrFlags(0xFE, 0x1)
    OP_8C(0xFE, 225, 0)
    SetChrChipByIndex(0xFE, 19)
    OP_22(0x20C, 0x0, 0x64)
    Return()

    # Function_88_46A9 end

    def Function_89_4717(): pass

    label("Function_89_4717")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -34390, 0, 121970, 225)
    Sleep(400)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 5)
    SetChrSubChip(0xFE, 0)
    OP_22(0x209, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_96(0xFE, 0xFFFF886E, 0xFA, 0x1E5F0, 0xFA0, 0xFA0)
    ClearChrFlags(0xFE, 0x1)
    OP_8C(0xFE, 270, 0)
    SetChrChipByIndex(0xFE, 19)
    OP_22(0x20C, 0x0, 0x64)
    Return()

    # Function_89_4717 end

    def Function_90_4785(): pass

    label("Function_90_4785")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -35560, 0, 121900, 225)
    Sleep(300)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 5)
    SetChrSubChip(0xFE, 0)
    OP_22(0x209, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_96(0xFE, 0xFFFF8832, 0xFA, 0x1F0D6, 0xFA0, 0xFA0)
    ClearChrFlags(0xFE, 0x1)
    OP_8C(0xFE, 135, 0)
    SetChrChipByIndex(0xFE, 27)
    OP_22(0x20C, 0x0, 0x64)
    Return()

    # Function_90_4785 end

    def Function_91_47F3(): pass

    label("Function_91_47F3")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -35070, 0, 123090, 225)
    Sleep(800)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 5)
    SetChrSubChip(0xFE, 0)
    OP_22(0x209, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_96(0xFE, 0xFFFF7B08, 0x0, 0x1EFD2, 0xFA0, 0xFA0)
    ClearChrFlags(0xFE, 0x1)
    OP_8C(0xFE, 45, 0)
    SetChrChipByIndex(0xFE, 19)
    OP_22(0x20C, 0x0, 0x64)
    Return()

    # Function_91_47F3 end

    def Function_92_4861(): pass

    label("Function_92_4861")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -33590, 0, 121760, 225)
    Sleep(200)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 5)
    SetChrSubChip(0xFE, 0)
    OP_22(0x209, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_96(0xFE, 0xFFFF8CE2, 0xFA, 0x1E97E, 0xFA0, 0xFA0)
    ClearChrFlags(0xFE, 0x1)
    OP_8C(0xFE, 45, 0)
    SetChrChipByIndex(0xFE, 27)
    OP_22(0x20C, 0x0, 0x64)
    Return()

    # Function_92_4861 end

    def Function_93_48CF(): pass

    label("Function_93_48CF")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -34560, 0, 123170, 225)
    Sleep(400)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 5)
    SetChrSubChip(0xFE, 0)
    OP_22(0x209, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_96(0xFE, 0xFFFF899A, 0xFA, 0x1F360, 0xFA0, 0xFA0)
    ClearChrFlags(0xFE, 0x1)
    OP_8C(0xFE, 0, 0)
    SetChrChipByIndex(0xFE, 19)
    OP_22(0x20C, 0x0, 0x64)
    Return()

    # Function_93_48CF end

    def Function_94_493D(): pass

    label("Function_94_493D")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -41410, 0, 119170, 90)
    Sleep(100)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 5)
    SetChrSubChip(0xFE, 0)
    OP_22(0x209, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_96(0xFE, 0xFFFF534E, 0x0, 0x1CB60, 0xFA0, 0xFA0)
    ClearChrFlags(0xFE, 0x1)
    OP_8C(0xFE, 225, 0)
    SetChrChipByIndex(0xFE, 19)
    OP_22(0x20C, 0x0, 0x64)
    Return()

    # Function_94_493D end

    def Function_95_49AB(): pass

    label("Function_95_49AB")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -42020, 0, 120000, 90)
    Sleep(500)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 5)
    SetChrSubChip(0xFE, 0)
    OP_22(0x209, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_96(0xFE, 0xFFFF4AD4, 0x0, 0x1D326, 0xFA0, 0xFA0)
    ClearChrFlags(0xFE, 0x1)
    OP_8C(0xFE, 225, 0)
    SetChrChipByIndex(0xFE, 27)
    OP_22(0x20C, 0x0, 0x64)
    Return()

    # Function_95_49AB end

    def Function_96_4A19(): pass

    label("Function_96_4A19")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -41330, 0, 120560, 135)
    Sleep(800)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 5)
    SetChrSubChip(0xFE, 0)
    OP_22(0x209, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_96(0xFE, 0xFFFF525E, 0x0, 0x1D40C, 0xFA0, 0xFA0)
    ClearChrFlags(0xFE, 0x1)
    OP_8C(0xFE, 45, 0)
    SetChrChipByIndex(0xFE, 27)
    OP_22(0x20C, 0x0, 0x64)
    Return()

    # Function_96_4A19 end

    def Function_97_4A87(): pass

    label("Function_97_4A87")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -42310, 0, 121240, 135)
    Sleep(200)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 5)
    SetChrSubChip(0xFE, 0)
    OP_22(0x209, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_96(0xFE, 0xFFFF46A6, 0x0, 0x1DB5A, 0xFA0, 0xFA0)
    ClearChrFlags(0xFE, 0x1)
    OP_8C(0xFE, 270, 0)
    SetChrChipByIndex(0xFE, 19)
    OP_22(0x20C, 0x0, 0x64)
    Return()

    # Function_97_4A87 end

    def Function_98_4AF5(): pass

    label("Function_98_4AF5")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -40800, 0, 121420, 135)
    Sleep(400)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 5)
    SetChrSubChip(0xFE, 0)
    OP_22(0x209, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_96(0xFE, 0xFFFF5650, 0x0, 0x1E064, 0xFA0, 0xFA0)
    ClearChrFlags(0xFE, 0x1)
    OP_8C(0xFE, 135, 0)
    SetChrChipByIndex(0xFE, 19)
    OP_22(0x20C, 0x0, 0x64)
    Return()

    # Function_98_4AF5 end

    def Function_99_4B63(): pass

    label("Function_99_4B63")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -41440, 0, 122490, 135)
    Sleep(900)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 5)
    SetChrSubChip(0xFE, 0)
    OP_22(0x209, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_96(0xFE, 0xFFFF4C0A, 0xFA, 0x1E9CE, 0xFA0, 0xFA0)
    ClearChrFlags(0xFE, 0x1)
    OP_8C(0xFE, 315, 0)
    SetChrChipByIndex(0xFE, 27)
    OP_22(0x20C, 0x0, 0x64)
    Return()

    # Function_99_4B63 end

    def Function_100_4BD1(): pass

    label("Function_100_4BD1")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -42570, 0, 119320, 90)
    Sleep(800)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 5)
    SetChrSubChip(0xFE, 0)
    OP_22(0x209, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_96(0xFE, 0xFFFF3F6C, 0x0, 0x1DCF4, 0xFA0, 0xFA0)
    ClearChrFlags(0xFE, 0x1)
    OP_8C(0xFE, 270, 0)
    SetChrChipByIndex(0xFE, 27)
    OP_22(0x20C, 0x0, 0x64)
    Return()

    # Function_100_4BD1 end

    def Function_101_4C3F(): pass

    label("Function_101_4C3F")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -42820, 0, 120840, 135)
    Sleep(600)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 5)
    SetChrSubChip(0xFE, 0)
    OP_22(0x209, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_96(0xFE, 0xFFFF4174, 0xFA, 0x1EA96, 0xFA0, 0xFA0)
    ClearChrFlags(0xFE, 0x1)
    OP_8C(0xFE, 180, 0)
    SetChrChipByIndex(0xFE, 19)
    OP_22(0x20C, 0x0, 0x64)
    Return()

    # Function_101_4C3F end

    def Function_102_4CAD(): pass

    label("Function_102_4CAD")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -37210, 0, 121610, 225)
    Sleep(200)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 5)
    SetChrSubChip(0xFE, 0)
    OP_22(0x209, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_96(0xFE, 0xFFFF7658, 0x0, 0x1EAA0, 0xFA0, 0xFA0)
    ClearChrFlags(0xFE, 0x1)
    OP_8C(0xFE, 135, 0)
    SetChrChipByIndex(0xFE, 19)
    OP_22(0x20C, 0x0, 0x64)
    Return()

    # Function_102_4CAD end

    def Function_103_4D1B(): pass

    label("Function_103_4D1B")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -37130, 0, 122850, 225)
    Sleep(400)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 5)
    SetChrSubChip(0xFE, 0)
    OP_22(0x209, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_96(0xFE, 0xFFFF7DBA, 0x0, 0x1E6FE, 0xFA0, 0xFA0)
    ClearChrFlags(0xFE, 0x1)
    OP_8C(0xFE, 45, 0)
    SetChrChipByIndex(0xFE, 27)
    OP_22(0x20C, 0x0, 0x64)
    Return()

    # Function_103_4D1B end

    def Function_104_4D89(): pass

    label("Function_104_4D89")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -38020, 0, 122240, 180)
    Sleep(500)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 5)
    SetChrSubChip(0xFE, 0)
    OP_22(0x209, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_96(0xFE, 0xFFFF6FA0, 0x0, 0x1EAB4, 0xFA0, 0xFA0)
    ClearChrFlags(0xFE, 0x1)
    OP_8C(0xFE, 180, 0)
    SetChrChipByIndex(0xFE, 19)
    OP_22(0x20C, 0x0, 0x64)
    Return()

    # Function_104_4D89 end

    def Function_105_4DF7(): pass

    label("Function_105_4DF7")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -37880, 0, 123820, 180)
    Sleep(600)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 5)
    SetChrSubChip(0xFE, 0)
    OP_22(0x209, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_96(0xFE, 0xFFFF7252, 0x0, 0x1F7DE, 0xFA0, 0xFA0)
    ClearChrFlags(0xFE, 0x1)
    OP_8C(0xFE, 0, 0)
    SetChrChipByIndex(0xFE, 27)
    OP_22(0x20C, 0x0, 0x64)
    Return()

    # Function_105_4DF7 end

    def Function_106_4E65(): pass

    label("Function_106_4E65")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -38840, 0, 122190, 180)
    Sleep(500)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 5)
    SetChrSubChip(0xFE, 0)
    OP_22(0x209, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_96(0xFE, 0xFFFF5A74, 0x0, 0x1E9CE, 0xFA0, 0xFA0)
    ClearChrFlags(0xFE, 0x1)
    OP_8C(0xFE, 315, 0)
    SetChrChipByIndex(0xFE, 27)
    OP_22(0x20C, 0x0, 0x64)
    Return()

    # Function_106_4E65 end

    def Function_107_4ED3(): pass

    label("Function_107_4ED3")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -39210, 0, 123540, 180)
    Sleep(800)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 5)
    SetChrSubChip(0xFE, 0)
    OP_22(0x209, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_96(0xFE, 0xFFFF5F4C, 0x0, 0x1F0B8, 0xFA0, 0xFA0)
    ClearChrFlags(0xFE, 0x1)
    OP_8C(0xFE, 0, 0)
    SetChrChipByIndex(0xFE, 19)
    OP_22(0x20C, 0x0, 0x64)
    Return()

    # Function_107_4ED3 end

    def Function_108_4F41(): pass

    label("Function_108_4F41")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -39510, 0, 121560, 135)
    Sleep(100)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 5)
    SetChrSubChip(0xFE, 0)
    OP_22(0x209, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_96(0xFE, 0xFFFF5B28, 0x0, 0x1E35C, 0xFA0, 0xFA0)
    ClearChrFlags(0xFE, 0x1)
    OP_8C(0xFE, 270, 0)
    SetChrChipByIndex(0xFE, 27)
    OP_22(0x20C, 0x0, 0x64)
    Return()

    # Function_108_4F41 end

    def Function_109_4FAF(): pass

    label("Function_109_4FAF")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -40050, 0, 122630, 135)
    Sleep(900)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 5)
    SetChrSubChip(0xFE, 0)
    OP_22(0x209, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_96(0xFE, 0xFFFF5556, 0x0, 0x1F2F2, 0xFA0, 0xFA0)
    ClearChrFlags(0xFE, 0x1)
    OP_8C(0xFE, 135, 0)
    SetChrChipByIndex(0xFE, 19)
    OP_22(0x20C, 0x0, 0x64)
    Return()

    # Function_109_4FAF end

    def Function_110_501D(): pass

    label("Function_110_501D")

    SetChrChipByIndex(0x28, 8)
    SetChrChipByIndex(0x29, 8)
    SetChrChipByIndex(0x2A, 8)
    SetChrChipByIndex(0x2B, 8)
    SetChrChipByIndex(0x2C, 8)
    SetChrChipByIndex(0x2D, 8)
    SetChrChipByIndex(0x2E, 8)
    SetChrChipByIndex(0x2F, 8)
    SetChrChipByIndex(0x30, 13)
    SetChrChipByIndex(0x31, 13)
    SetChrChipByIndex(0x32, 13)
    SetChrChipByIndex(0x33, 13)
    SetChrChipByIndex(0x34, 13)
    SetChrChipByIndex(0x35, 13)
    SetChrChipByIndex(0x36, 13)
    SetChrChipByIndex(0x37, 13)
    SetChrChipByIndex(0x38, 10)
    SetChrChipByIndex(0x39, 10)
    SetChrChipByIndex(0x3A, 10)
    SetChrChipByIndex(0x3B, 10)
    SetChrPos(0x28, -35530, 0, 97120, 0)
    SetChrPos(0x29, -36530, 0, 97120, 0)
    SetChrPos(0x2A, -37530, 0, 97120, 0)
    SetChrPos(0x2B, -38530, 0, 97120, 0)
    SetChrPos(0x2C, -39530, 0, 97120, 0)
    SetChrPos(0x2D, -40530, 0, 97120, 0)
    SetChrPos(0x2E, -41530, 0, 97120, 0)
    SetChrPos(0x2F, -42530, 0, 97120, 0)
    SetChrPos(0x30, -35530, 0, 95750, 0)
    SetChrPos(0x31, -36530, 0, 95750, 0)
    SetChrPos(0x32, -37530, 0, 95750, 0)
    SetChrPos(0x33, -38530, 0, 95750, 0)
    SetChrPos(0x34, -39530, 0, 95750, 0)
    SetChrPos(0x35, -40530, 0, 95750, 0)
    SetChrPos(0x36, -41530, 0, 95750, 0)
    SetChrPos(0x37, -42530, 0, 95750, 0)
    SetChrPos(0x38, -35000, 500, 92930, 0)
    SetChrPos(0x39, -37800, 500, 92930, 0)
    SetChrPos(0x3A, -40200, 500, 92930, 0)
    SetChrPos(0x3B, -42600, 500, 92930, 0)
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
    ClearChrFlags(0x39, 0x80)
    ClearChrFlags(0x3A, 0x80)
    ClearChrFlags(0x3B, 0x80)
    SetChrFlags(0x38, 0x4)
    SetChrFlags(0x39, 0x4)
    SetChrFlags(0x3A, 0x4)
    SetChrFlags(0x3B, 0x4)
    SetChrFlags(0x3C, 0x4)
    SetChrFlags(0x3D, 0x4)
    SetChrFlags(0x3E, 0x4)
    SetChrFlags(0x3F, 0x4)
    SetChrFlags(0x40, 0x4)
    SetChrFlags(0x38, 0x800)
    SetChrFlags(0x39, 0x800)
    SetChrFlags(0x3A, 0x800)
    SetChrFlags(0x3B, 0x800)

    def lambda_5280():
        OP_94(0x0, 0xFE, 0x0, 0x3E80, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_5280)
    Sleep(10)

    def lambda_529B():
        OP_94(0x0, 0xFE, 0x0, 0x3E80, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_529B)
    Sleep(10)

    def lambda_52B6():
        OP_94(0x0, 0xFE, 0x0, 0x3E80, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_52B6)
    Sleep(10)

    def lambda_52D1():
        OP_94(0x0, 0xFE, 0x0, 0x3E80, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_52D1)
    Sleep(10)

    def lambda_52EC():
        OP_94(0x0, 0xFE, 0x0, 0x3E80, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_52EC)
    Sleep(10)

    def lambda_5307():
        OP_94(0x0, 0xFE, 0x0, 0x3E80, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_5307)
    Sleep(10)

    def lambda_5322():
        OP_94(0x0, 0xFE, 0x0, 0x3E80, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_5322)
    Sleep(10)

    def lambda_533D():
        OP_94(0x0, 0xFE, 0x0, 0x3E80, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x2F, 1, lambda_533D)
    Sleep(100)

    def lambda_5358():
        OP_94(0x0, 0xFE, 0x0, 0x3E80, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x30, 1, lambda_5358)
    Sleep(10)

    def lambda_5373():
        OP_94(0x0, 0xFE, 0x0, 0x3E80, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x31, 1, lambda_5373)
    Sleep(10)

    def lambda_538E():
        OP_94(0x0, 0xFE, 0x0, 0x3E80, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x32, 1, lambda_538E)
    Sleep(10)

    def lambda_53A9():
        OP_94(0x0, 0xFE, 0x0, 0x3E80, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_53A9)
    Sleep(10)

    def lambda_53C4():
        OP_94(0x0, 0xFE, 0x0, 0x3E80, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x34, 1, lambda_53C4)
    Sleep(10)

    def lambda_53DF():
        OP_94(0x0, 0xFE, 0x0, 0x3E80, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x35, 1, lambda_53DF)
    Sleep(10)

    def lambda_53FA():
        OP_94(0x0, 0xFE, 0x0, 0x3E80, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x36, 1, lambda_53FA)
    Sleep(10)

    def lambda_5415():
        OP_94(0x0, 0xFE, 0x0, 0x3E80, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x37, 1, lambda_5415)
    Sleep(500)

    def lambda_5430():
        OP_94(0x0, 0xFE, 0x0, 0x3E80, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x38, 1, lambda_5430)
    Sleep(50)

    def lambda_544B():
        OP_94(0x0, 0xFE, 0x0, 0x3E80, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_544B)
    Sleep(50)

    def lambda_5466():
        OP_94(0x0, 0xFE, 0x0, 0x3E80, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x3A, 1, lambda_5466)
    Sleep(50)

    def lambda_5481():
        OP_94(0x0, 0xFE, 0x0, 0x3E80, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x3B, 1, lambda_5481)
    WaitChrThread(0x3B, 0x1)
    SetChrChipByIndex(0x38, 9)
    SetChrChipByIndex(0x39, 9)
    SetChrChipByIndex(0x3A, 9)
    SetChrChipByIndex(0x3B, 9)
    OP_43(0x38, 0x2, 0x0, 0x6F)
    OP_43(0x39, 0x2, 0x0, 0x6F)
    OP_43(0x3A, 0x2, 0x0, 0x6F)
    OP_43(0x3B, 0x2, 0x0, 0x6F)
    Return()

    # Function_110_501D end

    def Function_111_54C7(): pass

    label("Function_111_54C7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_54DC")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_111_54C7")

    label("loc_54DC")

    Return()

    # Function_111_54C7 end

    def Function_112_54DD(): pass

    label("Function_112_54DD")

    OP_22(0x13A, 0x1, 0x28)
    Sleep(400)
    OP_24(0x13A, 0x2D)
    Sleep(400)
    OP_24(0x13A, 0x32)
    Sleep(400)
    OP_24(0x13A, 0x37)
    Sleep(400)
    OP_24(0x13A, 0x3C)
    Sleep(400)
    OP_24(0x13A, 0x41)
    Sleep(400)
    OP_24(0x13A, 0x46)
    Sleep(400)
    OP_24(0x13A, 0x4B)
    Sleep(400)
    OP_24(0x13A, 0x50)
    Sleep(400)
    OP_24(0x13A, 0x55)
    Sleep(400)
    OP_24(0x13A, 0x5A)
    Sleep(400)
    OP_24(0x13A, 0x5F)
    Sleep(400)
    OP_24(0x13A, 0x64)
    Return()

    # Function_112_54DD end

    def Function_113_554F(): pass

    label("Function_113_554F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_555C")
    Return()

    label("loc_555C")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(-38400, 0, 96420, 0)
    OP_67(0, 7590, -10000, 0)
    OP_6B(2390, 0)
    OP_6C(45000, 0)
    OP_6E(329, 0)
    SetChrPos(0x101, -39570, 0, 96480, 0)
    SetChrPos(0x102, -38490, 0, 96410, 0)
    SetChrPos(0xF8, -39910, 0, 95110, 0)
    SetChrPos(0xF9, -38480, 0, 95200, 0)
    Call(0, 5)
    OP_0D()
    Sleep(300)

    ChrTalk(    #30
        0x101,
        "#1020F#6P那、那是……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x102,
        "#1046F#2P……赶快！\x02",
    )

    CloseMessageWindow()

    def lambda_562A():
        OP_8E(0xFE, 0xFFFF67EE, 0x0, 0x1DE98, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_562A)
    Sleep(100)

    def lambda_564A():
        OP_8E(0xFE, 0xFFFF6CEE, 0x0, 0x1DE70, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_564A)
    Sleep(100)

    def lambda_566A():
        OP_8E(0xFE, 0xFFFF6848, 0x0, 0x1D9F2, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_566A)
    Sleep(100)

    def lambda_568A():
        OP_8E(0xFE, 0xFFFF6DCA, 0x0, 0x1D9D4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_568A)
    Sleep(500)
    Fade(500)
    OP_6D(-38910, 0, 122270, 0)
    OP_67(0, 7900, -10000, 0)
    OP_6B(2460, 0)
    OP_6C(134000, 0)
    OP_6E(383, 0)

    def lambda_56EC():
        OP_6D(-37600, 0, 121220, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_56EC)

    def lambda_5704():
        OP_67(0, 6850, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5704)

    def lambda_571C():
        OP_6B(2040, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_571C)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x101, 315, 400)
    WaitChrThread(0x102, 0x1)
    OP_8C(0x102, 45, 400)
    WaitChrThread(0xF8, 0x1)
    OP_8C(0xF8, 270, 400)
    WaitChrThread(0xF9, 0x1)
    OP_8C(0xF9, 90, 400)
    WaitChrThread(0x101, 0x3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5786")

    ChrTalk(    #32
        0x106,
        "#057F#5P这、这是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_57D9")

    label("loc_5786")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_57B1")

    ChrTalk(    #33
        0x103,
        "#023F#5P这、这是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_57D9")

    label("loc_57B1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_57D9")

    ChrTalk(    #34
        0x108,
        "#072F#5P……这是……\x02",
    )

    CloseMessageWindow()

    label("loc_57D9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5811")

    ChrTalk(    #35
        0x107,
        (
            "#065F#5P啊啊……\x01",
            "得、得包扎一下！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5876")

    label("loc_5811")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5845")

    ChrTalk(    #36
        0x108,
        (
            "#072F#5P看来……\x01",
            "得包扎一下。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5876")

    label("loc_5845")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5876")

    ChrTalk(    #37
        0x103,
        (
            "#022F#5P看来……\x01",
            "得包扎一下。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5876")


    ChrTalk(    #38
        0x41,
        "#6P没、没这个必要……\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_58F0")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_592E")

    label("loc_58F0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5917")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_592E")

    label("loc_5917")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_592E")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_595A")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5998")

    label("loc_595A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5981")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5998")

    label("loc_5981")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_5998")

    Sleep(1000)

    def lambda_59A3():
        OP_6D(-37860, 0, 122950, 1200)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_59A3)

    def lambda_59BB():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_59BB)
    Sleep(50)

    def lambda_59CE():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_59CE)
    Sleep(50)

    def lambda_59E1():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_59E1)
    Sleep(50)
    OP_8C(0xF9, 0, 400)
    WaitChrThread(0x101, 0x3)
    OP_9E(0x41, 0xF, 0x0, 0x12C, 0xBB8)
    Fade(500)
    OP_D2(0x70300, 0x70307, 0x0)
    SetChrChipByIndex(0x41, 0)
    SetChrSubChip(0x41, 3)
    SetChrFlags(0x41, 0x1)
    SetChrPos(0x41, -38200, 0, 125200, 180)
    OP_0D()
    OP_9E(0x41, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(500)

    ChrTalk(    #39
        0x101,
        "#1020F#2P没、没问题吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x41,
        "#6P你们是游击士吧……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x41,
        (
            "#6P刚才……\x01",
            "『结社』的执行者们\x01",
            "已经通过这里了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x41,
        (
            "#6P他们的目标……\x01",
            "……似乎是格兰赛尔城……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x102,
        "#1042F#5P果然……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x41,
        (
            "#6P其余的敌方部队\x01",
            "好像控制着市区……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x41,
        "#6P……拜托……请救救市区和王城……\x02",
    )

    CloseMessageWindow()
    OP_9E(0x41, 0xF, 0x0, 0x12C, 0xBB8)
    Fade(500)
    OP_22(0x20C, 0x0, 0x64)
    ClearChrFlags(0x41, 0x1)
    SetChrPos(0x41, -38950, 0, 125450, 180)
    SetChrSubChip(0x41, 0)
    SetChrChipByIndex(0x41, 20)
    OP_0D()
    Sleep(500)

    def lambda_5BA9():
        OP_6D(-37540, 0, 121320, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5BA9)
    TurnDirection(0x102, 0x101, 400)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #46
        0x102,
        "#1042F#5P艾丝蒂尔……！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 600)

    ChrTalk(    #47
        0x101,
        (
            "#1002F嗯……！\x02\x03",

            "#1005F虽然有点对不起士兵们，\x01",
            "不过我们还是先追上去吧！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(-39120, 0, 123180, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -39120, 0, 123180, 0)
    SetChrPos(0x1, -39120, 0, 123180, 0)
    SetChrPos(0x2, -39120, 0, 123180, 0)
    SetChrPos(0x3, -39120, 0, 123180, 0)
    OP_0D()
    OP_A2(0x203A)
    OP_28(0x9C, 0x1, 0x2)
    OP_28(0x9C, 0x1, 0x4)
    OP_28(0x9C, 0x1, 0x8)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_113_554F end

    def Function_114_5CDF(): pass

    label("Function_114_5CDF")

    EventBegin(0x1)

    ChrTalk(    #48
        0x101,
        (
            "#1003F（这边不是近道！\x01",
            "……必须一直向东才行！）\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_114_5CDF end

    def Function_115_5D32(): pass

    label("Function_115_5D32")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #49
        "\x07\x05西　王都格兰赛尔\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_115_5D32 end

    def Function_116_5D75(): pass

    label("Function_116_5D75")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #50
        "\x07\x05东　格鲁纳门　　　１６５塞尔矩\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_116_5D75 end

    def Function_117_5DC6(): pass

    label("Function_117_5DC6")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #51
        "\x07\x05南　圣海姆门　　　２２８塞尔矩\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_117_5DC6 end

    SaveToFile()

Try(main)
