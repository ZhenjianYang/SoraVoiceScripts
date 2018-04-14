from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1400   ._SN',
        MapName             = 'Bose',
        Location            = 'T1400.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60016",
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
        '卫兵',                                 # 9
        '卫兵',                                 # 10
        '王国军士兵',                           # 11
        '王国军士兵',                           # 12
        '卡尔科斯',                             # 13
        '龙谷',                                 # 14
        '斯丁克',                               # 15
        '王国军士兵',                           # 16
        '王国军士兵',                           # 17
        '王国军士兵',                           # 18
        '王国军士兵',                           # 19
        '王国军士兵',                           # 20
        '王国军士兵',                           # 21
        '王国军士官',                           # 22
        '王国军士兵',                           # 23
        '王国军士兵',                           # 24
        '王国军士兵',                           # 25
        '王国军士兵',                           # 26
        '王国军士兵',                           # 27
        '王国军士兵',                           # 28
        '王国军士兵',                           # 29
        '王国军士兵',                           # 30
        '王国军士兵',                           # 31
        '王国军士兵',                           # 32
        '王国军士兵',                           # 33
        '王国军士兵',                           # 34
        '王国军士兵',                           # 35
        '王国军士兵',                           # 36
        '王国军士兵',                           # 37
        '王国军士兵',                           # 38
        '王国军士兵',                           # 39
        '王国军士兵',                           # 40
        '王国军士兵',                           # 41
        '王国军士兵',                           # 42
        '王国军士兵',                           # 43
        '王国军士兵',                           # 44
        '王国军士兵',                           # 45
        '王国军士兵',                           # 46
        '王国军士兵',                           # 47
        '王国军士兵',                           # 48
        '王国军士兵',                           # 49
        '王国军士兵',                           # 50
        '王国军士兵',                           # 51
        '王国军士兵',                           # 52
        '王国军士兵',                           # 53
        '王国军士兵',                           # 54
        '王国军士兵',                           # 55
        '王国军士兵',                           # 56
        '王国军士兵',                           # 57
        '王国军士兵',                           # 58
        '王国军士兵',                           # 59
        '王国军士兵',                           # 60
        '王国军士兵',                           # 61
        '王国军士兵',                           # 62
        '王国军士兵',                           # 63
        '王国军士兵',                           # 64
        '王国军士兵',                           # 65
        '王国军士兵',                           # 66
        '王国军士兵',                           # 67
        '王国军士兵',                           # 68
        '王国军士兵',                           # 69
        '王国军士兵',                           # 70
        '王国军士兵',                           # 71
        '王国军士官',                           # 72
        '王国军士官',                           # 73
        '王国军士官',                           # 74
        '王国军士官',                           # 75
        '王国军士官',                           # 76
        '王国军士官',                           # 77
        '卡西乌斯',                             # 78
        '摩尔根将军',                           # 79
        '钢壁之路方向',                         # 80
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
        'ED6_DT07/CH01040 ._CH',             # 01
        'ED6_DT07/CH01660 ._CH',             # 02
        'ED6_DT27/CH03790 ._CH',             # 03
        'ED6_DT07/CH01310 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT07/CH01640P._CP',             # 00
        'ED6_DT07/CH01040P._CP',             # 01
        'ED6_DT07/CH01660P._CP',             # 02
        'ED6_DT27/CH03790P._CP',             # 03
        'ED6_DT07/CH01310P._CP',             # 04
    )

    DeclNpc(
        X                   = 9100,
        Z                   = 0,
        Y                   = -10190,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -2400,
        Z                   = 0,
        Y                   = -7500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -9000,
        Z                   = 11750,
        Y                   = 3000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 9000,
        Z                   = 11750,
        Y                   = 3000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -2100,
        Z                   = 0,
        Y                   = -20100,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 7620,
        Z                   = 10,
        Y                   = -18860,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -12650,
        Z                   = 0,
        Y                   = -26140,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -4570,
        Z                   = 0,
        Y                   = -8880,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 80,
        Z                   = 0,
        Y                   = -10570,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 1900,
        Z                   = 0,
        Y                   = -9630,
        Direction           = 303,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = -2620,
        Z                   = 0,
        Y                   = -11290,
        Direction           = 27,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 4010,
        Z                   = 0,
        Y                   = -9180,
        Direction           = 303,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 2430,
        Z                   = 0,
        Y                   = -11400,
        Direction           = 1,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = -14600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 262144,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = -14600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 262144,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = -14600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 262144,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = -14600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 262144,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = -14600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 262144,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = -14600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 262144,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = -14600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 262144,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
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
        X                   = 11890,
        Z                   = 40,
        Y                   = -60460,
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


    ScpFunction(
        "Function_0_9D2",          # 00, 0
        "Function_1_B01",          # 01, 1
        "Function_2_B68",          # 02, 2
        "Function_3_CE5",          # 03, 3
        "Function_4_D09",          # 04, 4
        "Function_5_D56",          # 05, 5
        "Function_6_DA3",          # 06, 6
        "Function_7_10AB",         # 07, 7
        "Function_8_12A4",         # 08, 8
        "Function_9_161A",         # 09, 9
        "Function_10_19B0",        # 0A, 10
        "Function_11_1DFF",        # 0B, 11
        "Function_12_2092",        # 0C, 12
        "Function_13_23BD",        # 0D, 13
        "Function_14_2530",        # 0E, 14
        "Function_15_2659",        # 0F, 15
        "Function_16_2740",        # 10, 16
        "Function_17_2955",        # 11, 17
        "Function_18_2A74",        # 12, 18
        "Function_19_2C3A",        # 13, 19
        "Function_20_2E21",        # 14, 20
        "Function_21_3557",        # 15, 21
    )


    def Function_0_9D2(): pass

    label("Function_0_9D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_A84")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    OP_43(0xA, 0x0, 0x0, 0x2)
    OP_43(0xB, 0x0, 0x0, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_A81")
    SetChrPos(0xF, -1400, 0, -12000, 0)
    SetChrPos(0x10, 0, 0, -12000, 0)
    SetChrPos(0x11, 1400, 0, -12000, 0)
    SetChrPos(0x12, -1400, 0, -13400, 0)
    SetChrPos(0x13, 0, 0, -13400, 0)
    SetChrPos(0x14, 1400, 0, -13400, 0)

    label("loc_A81")

    Jump("loc_AC5")

    label("loc_A84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_A98")
    SetChrChipByIndex(0xC, 1)
    ClearChrFlags(0xD, 0x80)
    Jump("loc_AC5")

    label("loc_A98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_AA7")
    ClearChrFlags(0xD, 0x80)
    Jump("loc_AC5")

    label("loc_AA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AC5")
    ClearChrFlags(0xE, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AC5")
    SetChrFlags(0xE, 0x10)

    label("loc_AC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_AE4")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 20)
    Jump("loc_B00")

    label("loc_AE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_B00")
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 21)

    label("loc_B00")

    Return()

    # Function_0_9D2 end

    def Function_1_B01(): pass

    label("Function_1_B01")

    OP_16(0x2, 0xFA0, 0xFFFE2370, 0xFFFE0430, 0x230045)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B3A")
    OP_72(0x3, 0x10)
    OP_6F(0x3, 560)
    OP_72(0x7, 0x4)
    OP_72(0x8, 0x4)
    OP_72(0x9, 0x4)

    label("loc_B3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B4E")
    OP_72(0x3, 0x10)
    OP_6F(0x3, 0)

    label("loc_B4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x411, 7)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B67")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B67")

    Return()

    # Function_1_B01 end

    def Function_2_B68(): pass

    label("Function_2_B68")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B8D")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_CCF")

    label("loc_B8D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BA6")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_CCF")

    label("loc_BA6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BBF")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_CCF")

    label("loc_BBF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BD8")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_CCF")

    label("loc_BD8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BF1")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_CCF")

    label("loc_BF1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C0A")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_CCF")

    label("loc_C0A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C23")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_CCF")

    label("loc_C23")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C3C")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_CCF")

    label("loc_C3C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C55")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_CCF")

    label("loc_C55")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C6E")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_CCF")

    label("loc_C6E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C87")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_CCF")

    label("loc_C87")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CA0")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_CCF")

    label("loc_CA0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CB9")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_CCF")

    label("loc_CB9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CCF")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_CCF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CE4")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_CCF")

    label("loc_CE4")

    Return()

    # Function_2_B68 end

    def Function_3_CE5(): pass

    label("Function_3_CE5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D08")
    OP_8D(0xFE, -7000, -13000, 3500, -25300, 2000)
    Jump("Function_3_CE5")

    label("loc_D08")

    Return()

    # Function_3_CE5 end

    def Function_4_D09(): pass

    label("Function_4_D09")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D55")
    OP_8E(0xFE, 0xFFFFDCD8, 0x2DE6, 0xBB8, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(3000)
    OP_8E(0xFE, 0xFFFFF63C, 0x2DE6, 0xBB8, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(3000)
    Jump("Function_4_D09")

    label("loc_D55")

    Return()

    # Function_4_D09 end

    def Function_5_D56(): pass

    label("Function_5_D56")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DA2")
    OP_8E(0xFE, 0x2328, 0x2DE6, 0xBB8, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(3000)
    OP_8E(0xFE, 0x9C4, 0x2DE6, 0xBB8, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(3000)
    Jump("Function_5_D56")

    label("loc_DA2")

    Return()

    # Function_5_D56 end

    def Function_6_DA3(): pass

    label("Function_6_DA3")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_DFE")

    ChrTalk(    #0
        0xFE,
        (
            "国境师团也接到\x01",
            "紧急召集命令……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "但是又不能用导力枪，\x01",
            "要怎样战斗呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10A7")

    label("loc_DFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_F1A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EC1")

    ChrTalk(    #2
        0xFE,
        (
            "把帝国来的货物搬进来时\x01",
            "发生了那个现象……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "于是就如你所见，\x01",
            "大门就开着停住了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "这，这个状态\x01",
            "就等于没有防御力了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "如果帝国军来了，\x01",
            "那可真是一刻也撑不住啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_F17")

    label("loc_EC1")


    ChrTalk(    #6
        0xFE,
        (
            "把帝国来的货物搬进来时\x01",
            "发生了那个现象……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "这，这个状态\x01",
            "就等于没有防御力了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F17")

    Jump("loc_10A7")

    label("loc_F1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_F70")

    ChrTalk(    #8
        0xFE,
        (
            "龙的事件总算\x01",
            "平安解决了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "这次没有大规模的\x01",
            "出动军队真是帮大忙了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10A7")

    label("loc_F70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_FBC")

    ChrTalk(    #10
        0xFE,
        (
            "将军阁下\x01",
            "在『埃尔赛尤』上。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "要亲自指挥\x01",
            "龙的捕获作战呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10A7")

    label("loc_FBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_10A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1044")

    ChrTalk(    #12
        0xFE,
        (
            "摩尔根将军终于\x01",
            "从签字仪式回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "这么说，今天开始\x01",
            "不振作精神可不行啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "一旦松懈\x01",
            "可是会被将军怪罪的哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10A7")

    label("loc_1044")


    ChrTalk(    #15
        0xFE,
        (
            "摩尔根将军终于\x01",
            "从签字仪式回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "才刚刚回来\x01",
            "就已经开始办公了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        "唉，真是铁人啊。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_10A7")

    TalkEnd(0x8)
    Return()

    # Function_6_DA3 end

    def Function_7_10AB(): pass

    label("Function_7_10AB")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_1191")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1119")

    ChrTalk(    #18
        0xFE,
        (
            "警戒态势解除了。\x01",
            "平静的日子到来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "呼，这么紧张…\x01",
            "还是自政变事件之后第一次呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_118E")

    label("loc_1119")


    ChrTalk(    #20
        0xFE,
        "欢迎来到哈肯大门！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "警戒态势解除了。\x01",
            "平静的日子到来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "呼，这么紧张…\x01",
            "还是自政变事件之后第一次呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_118E")

    Jump("loc_12A0")

    label("loc_1191")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_11E7")

    ChrTalk(    #23
        0xFE,
        (
            "因为龙的事件，\x01",
            "要塞这也是戒严状态呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "希望飞行舰队\x01",
            "早日捕获龙啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12A0")

    label("loc_11E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_12A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1237")

    ChrTalk(    #25
        0xFE,
        "欢迎来到哈肯大门！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "这道门的那边\x01",
            "就是埃雷波尼亚帝国。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12A0")

    label("loc_1237")


    ChrTalk(    #27
        0xFE,
        "欢迎来到哈肯大门！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "这道门的那边\x01",
            "就是埃雷波尼亚帝国。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "要通行的话\x01",
            "必须有王国发行的护照。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_12A0")

    TalkEnd(0x9)
    Return()

    # Function_7_10AB end

    def Function_8_12A4(): pass

    label("Function_8_12A4")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_13D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_135D")

    ChrTalk(    #30
        0xFE,
        (
            "不能用枪是很头痛，\x01",
            "不过飞船是个更大的问题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "王国的防卫体系很大部分\x01",
            "要依靠飞行舰队的力量嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "失去了最关键的战斗力，\x01",
            "对军队来说是最大的不安因素啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_13CD")

    label("loc_135D")


    ChrTalk(    #33
        0xFE,
        (
            "王国的防卫体系很大部分\x01",
            "要依靠飞行舰队的力量嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "失去了最关键的战斗力，\x01",
            "对军队来说是最大的不安因素呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13CD")

    Jump("loc_1616")

    label("loc_13D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1436")

    ChrTalk(    #35
        0xFE,
        (
            "大门一直开着，\x01",
            "就意味着防壁会被人趁虚而入。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "担任放哨任务的人\x01",
            "责任也比以往更重了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1616")

    label("loc_1436")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_14EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_148D")

    ChrTalk(    #37
        0xFE,
        (
            "这次龙的事件……\x01",
            "似乎是游击士解决的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "感觉功劳\x01",
            "都被抢走了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14E8")

    label("loc_148D")


    ChrTalk(    #39
        0xFE,
        "我听说……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "这次龙的事件……\x01",
            "似乎是游击士解决的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "好像功劳都被\x01",
            "抢走了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_14E8")

    Jump("loc_1616")

    label("loc_14EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_15BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1546")

    ChrTalk(    #42
        0xFE,
        (
            "龙的捕获作战\x01",
            "似乎很艰难啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "飞行舰队也会陷入苦战\x01",
            "实在难以想象。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15BA")

    label("loc_1546")


    ChrTalk(    #44
        0xFE,
        (
            "龙的捕获作战\x01",
            "似乎很艰难啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "还有传闻说\x01",
            "也派遣了地面部队呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "唉，肯定也是什么人\x01",
            "闲的无聊瞎说的吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_15BA")

    Jump("loc_1616")

    label("loc_15BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_1616")

    ChrTalk(    #47
        0xFE,
        (
            "互不侵犯条约的缔结\x01",
            "和国境警戒是两回事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "我们还是一如既往\x01",
            "严格进行警戒。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1616")

    TalkEnd(0xA)
    Return()

    # Function_8_12A4 end

    def Function_9_161A(): pass

    label("Function_9_161A")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_1674")

    ChrTalk(    #49
        0xFE,
        (
            "即使在这种非常时期\x01",
            "摩尔根将军还是很镇定啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        "不愧是身经百战的勇将。\x02",
    )

    CloseMessageWindow()
    Jump("loc_19AC")

    label("loc_1674")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1746")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1702")

    ChrTalk(    #51
        0xFE,
        (
            "那条古代龙出现之后，\x01",
            "我们又被召集起来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "不过，这次事态\x01",
            "好像相当严重啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "因为是关系到\x01",
            "王国命运的事件嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_1743")

    label("loc_1702")


    ChrTalk(    #54
        0xFE,
        (
            "这次的事态\x01",
            "非常的严重。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        "所以我们士兵的使命也相当重大。\x02",
    )

    CloseMessageWindow()

    label("loc_1743")

    Jump("loc_19AC")

    label("loc_1746")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_1817")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_17A7")

    ChrTalk(    #56
        0xFE,
        (
            "感觉将军阁下的表情\x01",
            "好像不太开心啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "事件都解决了，\x01",
            "到底怎么回事呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1814")

    label("loc_17A7")


    ChrTalk(    #58
        0xFE,
        (
            "刚才见到了\x01",
            "将军阁下……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "事件都已经解决了，\x01",
            "但却感觉表情不大开心似的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        "嗯，可能是我多心……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1814")

    Jump("loc_19AC")

    label("loc_1817")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_192F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_188A")

    ChrTalk(    #61
        0xFE,
        (
            "国境师团虽然也处在警戒状态，\x01",
            "但是并没有什么实质性的行动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "毕竟这里是\x01",
            "国境防卫的要地嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_192C")

    label("loc_188A")


    ChrTalk(    #63
        0xFE,
        (
            "为龙的事件出动的\x01",
            "主要是飞行舰队和王室亲卫队。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "国境师团虽然也处在警戒状态，\x01",
            "但是并没有什么实质性的行动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "所以，国境防备\x01",
            "和往常一样还是万无一失。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_192C")

    Jump("loc_19AC")

    label("loc_192F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_19AC")

    ChrTalk(    #66
        0xFE,
        (
            "１０年前的战争中\x01",
            "帝国突破了这里，\x01",
            "入侵了利贝尔国内。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "因为有这样的历史。\x01",
            "站在这里放哨\x01",
            "真是令人不禁紧张起来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19AC")

    TalkEnd(0xB)
    Return()

    # Function_9_161A end

    def Function_10_19B0(): pass

    label("Function_10_19B0")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_1BF8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x217, 5)), scpexpr(EXPR_END)), "loc_1A74")

    NpcTalk(    #68
        0xFE,
        "卡尔科斯",
        (
            "终于批准退伍了。\x01",
            "这下终于该和军服道别了。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #69
        0xFE,
        "卡尔科斯",
        (
            "虽然时间短暂，\x01",
            "但军队生活也很快乐呢。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #70
        0xFE,
        "卡尔科斯",
        (
            "嗯，人生就是要这样啊。\x01",
            "在军队里我对生活有了新的感悟。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BF5")

    label("loc_1A74")


    NpcTalk(    #71
        0xFE,
        "卡尔科斯",
        (
            "终于批准退伍了。\x01",
            "这下终于该和军服道别了。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #72
        0xFE,
        "卡尔科斯",
        (
            "作为退伍的纪念，\x01",
            "这本书就送给你吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #73
        "\x07\x00得到了\x1F\x42\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_59()
    OP_3E(0x242, 1)
    OP_A2(0x10BD)
    OP_0D()

    NpcTalk(    #74
        0xFE,
        "卡尔科斯",
        (
            "这本书曾是我\x01",
            "小小的乐趣呢。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #75
        0xFE,
        "卡尔科斯",
        (
            "回顾起来，虽然时间短暂，\x01",
            "但军队生活也很快乐呢……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #76
        0xFE,
        "卡尔科斯",
        (
            "好了～赶快\x01",
            "去领通行证吧。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #77
        0xFE,
        "卡尔科斯",
        (
            "虽说路程很长，\x01",
            "不过终于要出发去帝国旅行了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BF5")

    Jump("loc_1DFB")

    label("loc_1BF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_1CD3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1C4D")

    ChrTalk(    #78
        0xFE,
        (
            "入伍到现在的薪水\x01",
            "都存起来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "退伍批准以后\x01",
            "打算就去旅行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CD0")

    label("loc_1C4D")


    ChrTalk(    #80
        0xFE,
        (
            "旅费也存够了，\x01",
            "我想差不多也该\x01",
            "退伍了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "不巧正碰上警戒状态呢。\x01",
            "结果没获得批准。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "不过，这次事件\x01",
            "总算平安度过了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_1CD0")

    Jump("loc_1DFB")

    label("loc_1CD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_1DFB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1D3C")

    ChrTalk(    #83
        0xFE,
        (
            "我本来是为了去帝国旅行\x01",
            "才到这要塞来的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "中途旅费用完了，\x01",
            "没办法才当士兵的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DFB")

    label("loc_1D3C")


    ChrTalk(    #85
        0xFE,
        (
            "我本来是为了去帝国旅行\x01",
            "才到这要塞来的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        (
            "中途旅费用完了，\x01",
            "没办法才当士兵的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "军队生活虽然严格，\x01",
            "不过士兵们都是好人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "嗯，顺其自然的人生\x01",
            "好像也没有以前想象中的那么差。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_1DFB")

    TalkEnd(0xC)
    Return()

    # Function_10_19B0 end

    def Function_11_1DFF(): pass

    label("Function_11_1DFF")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_1F70")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1E9C")

    ChrTalk(    #89
        0xFE,
        (
            "龙好像没受什么伤\x01",
            "顺利逃走了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "不过，为什么这次的龙\x01",
            "会变得那么凶暴呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "这个问题对于我们研究人员来说\x01",
            "依然是个重大的谜题。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F6D")

    label("loc_1E9C")


    ChrTalk(    #92
        0xFE,
        (
            "龙好像没受什么伤\x01",
            "顺利逃走了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "作为古代生物的研究人员\x01",
            "对这次的事件也很不解啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "要是有作战中拍摄的照片，\x01",
            "研究就能有飞跃性的进展……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        (
            "但是能公开到什么程度，\x01",
            "就要看我们研究人员的交涉了吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_1F6D")

    Jump("loc_208E")

    label("loc_1F70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_208E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1FD5")

    ChrTalk(    #96
        0xFE,
        (
            "希望捕获作战\x01",
            "能慎重地进行啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "虽说危害了居民，\x01",
            "但龙可是无可替代的生物啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_208E")

    label("loc_1FD5")


    ChrTalk(    #98
        0xFE,
        (
            "听说由于王国军的作战\x01",
            "龙逃进迷雾峡谷了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        (
            "想试试看能不能亲眼看到它\x01",
            "我们才来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "总之希望军方对捕获作战\x01",
            "能慎重地进行啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "虽说危害了居民，\x01",
            "但龙可是无可替代的生物啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_208E")

    TalkEnd(0xD)
    Return()

    # Function_11_1DFF end

    def Function_12_2092(): pass

    label("Function_12_2092")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 7)), scpexpr(EXPR_END)), "loc_209F")
    OP_A2(0x6)

    label("loc_209F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_211B")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇在前篇遇到过斯丁克】\x01",        # 0
            "【◇在前篇没遇到过斯丁克】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_210F"),
        (1, "loc_2115"),
        (SWITCH_DEFAULT, "loc_211B"),
    )


    label("loc_210F")

    OP_A2(0x6)
    Jump("loc_211B")

    label("loc_2115")

    OP_A3(0x6)
    Jump("loc_211B")

    label("loc_211B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_23B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34A, 3)), scpexpr(EXPR_END)), "loc_2163")

    ChrTalk(    #102
        0xFE,
        (
            "库拉茨和亚妮拉丝\x01",
            "都不在啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        "……拜托你了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_23B9")

    label("loc_2163")


    ChrTalk(    #104
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2231")

    ChrTalk(    #105
        0x101,
        (
            "#1011F啊，你是……\x02\x03",

            "斯丁克……对吧？\x01",
            "柏斯支部的游击士。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #106
        0xFE,
        (
            "你是……\x01",
            "那时的准游击士吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        "不，看样子已经升任正游击士了啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x101,
        "#1016F嗯，是啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2280")

    label("loc_2231")


    ChrTalk(    #109
        0x101,
        (
            "#1015F（啊？这个人……）\x02\x03",

            "（仔细看看的话，\x01",
            "　竟然也戴着游击士的徽章啊？）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2280")


    ChrTalk(    #110
        0x106,
        (
            "#050F很久不见了，斯丁克。\x02\x03",

            "竟然来到这种地方，\x01",
            "是来消灭通缉魔兽的吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0xFE)
    TurnDirection(0xFE, 0x106, 400)

    ChrTalk(    #111
        0xFE,
        "阿加特……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        "是来柏斯工作的吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x106,
        (
            "#050F啊啊，暂时是这样。\x02\x03",

            "不过目前也只是\x01",
            "帮着消灭通缉魔兽。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "是吗……\x01",
            "这附近的魔兽实在太多了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        "……那就拜托你们了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x106,
        "#051F喔，就交给我们吧。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1A53)

    label("loc_23B9")

    TalkEnd(0xE)
    Return()

    # Function_12_2092 end

    def Function_13_23BD(): pass

    label("Function_13_23BD")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_24A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_245A")

    ChrTalk(    #117
        0xFE,
        (
            "稍微想了一下，敌人\x01",
            "应该也不能使用枪械的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "那要是这样的情况，\x01",
            "就应该不会攻过来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "……这么说来，\x01",
            "只能这样去想了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_24A3")

    label("loc_245A")


    ChrTalk(    #120
        0xFE,
        (
            "不能使用导力枪的话，\x01",
            "敌人也就不能攻过来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        "嗯，应该是这样的。\x02",
    )

    CloseMessageWindow()

    label("loc_24A3")

    Jump("loc_252C")

    label("loc_24A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_252C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2507")

    ChrTalk(    #122
        0xFE,
        (
            "这是怎么回事，\x01",
            "到底是什么情况呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "可，可恶……\x01",
            "今天明明是休假的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_252C")

    label("loc_2507")


    ChrTalk(    #124
        0xFE,
        (
            "可，可恶……\x01",
            "今天明明是休假的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_252C")

    TalkEnd(0xF)
    Return()

    # Function_13_23BD end

    def Function_14_2530(): pass

    label("Function_14_2530")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_25C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_259C")

    ChrTalk(    #125
        0xFE,
        (
            "可恶，为什么帝国军！\x01",
            "这么快就来了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        (
            "要是没有战争\x01",
            "就没有我活跃的机会了呢！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_25C5")

    label("loc_259C")


    ChrTalk(    #127
        0xFE,
        (
            "可恶，为什么帝国军！\x01",
            "这么快就来了！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25C5")

    Jump("loc_2655")

    label("loc_25C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2655")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_262E")

    ChrTalk(    #128
        0xFE,
        (
            "呵呵呵呵呵呵……\x01",
            "这个时刻终于来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "喂，来吧帝国军！\x01",
            "看我怎么收拾你们!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_2655")

    label("loc_262E")


    ChrTalk(    #130
        0xFE,
        (
            "呵呵呵呵呵呵……\x01",
            "喂，来吧帝国军！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2655")

    TalkEnd(0x10)
    Return()

    # Function_14_2530 end

    def Function_15_2659(): pass

    label("Function_15_2659")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_26AC")

    ChrTalk(    #131
        0xFE,
        (
            "旁，旁边这家伙\x01",
            "实在是太可疑了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "总之，\x01",
            "只能先装作听不到了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_273C")

    label("loc_26AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_273C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2715")

    ChrTalk(    #133
        0xFE,
        (
            "旁，旁边这家伙……\x01",
            "看举止好像很危险。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        (
            "希望不要扯上什么关系，\x01",
            "尽量远离他。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_273C")

    label("loc_2715")


    ChrTalk(    #135
        0xFE,
        (
            "旁，旁边这家伙……\x01",
            "看上去好可怕。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_273C")

    TalkEnd(0x11)
    Return()

    # Function_15_2659 end

    def Function_16_2740(): pass

    label("Function_16_2740")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_285F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_280C")

    ChrTalk(    #136
        0xFE,
        (
            "帝国军来的可能性\x01",
            "我想应该不大。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "我们不能用导力兵器，\x01",
            "帝国方也应该一样不能用的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        (
            "而且不管怎么说\x01",
            "才刚刚缔结互不侵犯条约。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        (
            "没有十分的胜算，\x01",
            "我想他们不会乱来的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)
    Jump("loc_285C")

    label("loc_280C")


    ChrTalk(    #140
        0xFE,
        (
            "帝国军来的可能性\x01",
            "我想应该不大。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        (
            "没有十分的胜算，\x01",
            "我想他们不会乱来的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_285C")

    Jump("loc_2951")

    label("loc_285F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2951")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28F5")

    ChrTalk(    #142
        0xFE,
        (
            "变成这样的情况\x01",
            "我一开始就做好准备了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        (
            "事到如今我也\x01",
            "不会丢王国军的脸的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        (
            "基于作为入伍时的志愿，\x01",
            "我要尽自己的责任。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)
    Jump("loc_2951")

    label("loc_28F5")


    ChrTalk(    #145
        0xFE,
        (
            "从立下志愿的时候开始\x01",
            "我就已经做好准备了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        (
            "正因为如此，\x01",
            "我作为士兵要尽自己的责任。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2951")

    TalkEnd(0x12)
    Return()

    # Function_16_2740 end

    def Function_17_2955(): pass

    label("Function_17_2955")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_29E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29B2")

    ChrTalk(    #147
        0xFE,
        "北面的平原上什么也看不见哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        (
            "真想就这样\x01",
            "平平安安地结束呀。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)
    Jump("loc_29E5")

    label("loc_29B2")


    ChrTalk(    #149
        0xFE,
        (
            "北面的平原上有什么呢。\x01",
            "从这里什么也看不见哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29E5")

    Jump("loc_2A70")

    label("loc_29E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2A70")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A4F")

    ChrTalk(    #150
        0xFE,
        (
            "啊，那边开始\x01",
            "已经是帝国的领土了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        (
            "呼，呼……\x01",
            "光是看着我就难以呼吸了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)
    Jump("loc_2A70")

    label("loc_2A4F")


    ChrTalk(    #152
        0xFE,
        (
            "呼，呼……\x01",
            "好像有点紧张呀。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A70")

    TalkEnd(0x13)
    Return()

    # Function_17_2955 end

    def Function_18_2A74(): pass

    label("Function_18_2A74")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_2B82")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B19")

    ChrTalk(    #153
        0xFE,
        (
            "现在，\x01",
            "好像还没有发现帝国军进攻的动向。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xFE,
        (
            "一定是对方的战车也不能动了，\x01",
            "所以正不知道该怎么办。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        (
            "呼，看来我们也\x01",
            "开始疑神疑鬼了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)
    Jump("loc_2B7F")

    label("loc_2B19")


    ChrTalk(    #156
        0xFE,
        (
            "现在，\x01",
            "好像还没有发现帝国军进攻的动向。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        (
            "一定是对方的战车也不能动了，\x01",
            "所以正不知道该怎么办。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B7F")

    Jump("loc_2C36")

    label("loc_2B82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2C36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BF9")

    ChrTalk(    #158
        0xFE,
        (
            "正在搬送物资的时候\x01",
            "门停了下来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xFE,
        (
            "我想这时机也\x01",
            "实在太巧了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xFE,
        "说实话这太可疑了……\x02",
    )

    CloseMessageWindow()
    OP_A2(0xC)
    Jump("loc_2C36")

    label("loc_2BF9")


    ChrTalk(    #161
        0xFE,
        (
            "正在搬送物资的时候\x01",
            "门停了下来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        "嗯，真可疑呀……\x02",
    )

    CloseMessageWindow()

    label("loc_2C36")

    TalkEnd(0x14)
    Return()

    # Function_18_2A74 end

    def Function_19_2C3A(): pass

    label("Function_19_2C3A")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_2CEE")

    ChrTalk(    #163
        0xFE,
        (
            "虽为了以防万一还在继续警戒，\x01",
            "但我觉得不用这样提心吊胆的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xFE,
        (
            "我们不能用导力兵器，\x01",
            "帝国方也应该一样不能用的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        (
            "就算出兵，\x01",
            "现在这情况也是不能运送兵力的吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E1D")

    label("loc_2CEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2E1D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DB7")

    ChrTalk(    #166
        0xFE,
        (
            "门一直开着的话\x01",
            "在防卫上确实是个大问题……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xFE,
        (
            "那个门是用防弹钢板造的。\x01",
            "用人力是不可能推动的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        (
            "直到导力器的机能恢复之前\x01",
            "只能继续这样了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0xFE,
        (
            "对我们来说\x01",
            "只有加强警备了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)
    Jump("loc_2E1D")

    label("loc_2DB7")


    ChrTalk(    #170
        0xFE,
        (
            "那个门是用防弹钢板造的。\x01",
            "用人力是不可能推动的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xFE,
        (
            "直到导力器的机能恢复之前\x01",
            "继续维持这个状态。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E1D")

    TalkEnd(0x15)
    Return()

    # Function_19_2C3A end

    def Function_20_2E21(): pass

    label("Function_20_2E21")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x47, 0x80)
    ClearChrFlags(0x48, 0x80)
    ClearChrFlags(0x49, 0x80)
    ClearChrFlags(0x4A, 0x80)
    ClearChrFlags(0x4B, 0x80)
    ClearChrFlags(0x4C, 0x80)
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
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)
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
    ClearChrFlags(0x3C, 0x80)
    ClearChrFlags(0x3D, 0x80)
    ClearChrFlags(0x3E, 0x80)
    ClearChrFlags(0x3F, 0x80)
    ClearChrFlags(0x40, 0x80)
    ClearChrFlags(0x41, 0x80)
    ClearChrFlags(0x42, 0x80)
    ClearChrFlags(0x43, 0x80)
    ClearChrFlags(0x44, 0x80)
    ClearChrFlags(0x45, 0x80)
    ClearChrFlags(0x46, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x4D, 0x80)
    ClearChrFlags(0x4E, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x47, -4520, 0, -11180, 180)
    SetChrPos(0x16, -5920, 0, -13010, 0)
    SetChrPos(0x17, -4880, 0, -13070, 0)
    SetChrPos(0x18, -3760, 0, -13080, 0)
    SetChrPos(0x19, -6040, 0, -14600, 0)
    SetChrPos(0x1A, -4880, -10, -14630, 0)
    SetChrPos(0x1B, -3730, 0, -14620, 0)
    SetChrPos(0x2E, -5930, 0, -16510, 0)
    SetChrPos(0x2F, -4820, 0, -16500, 0)
    SetChrPos(0x30, -3620, 0, -16520, 0)
    SetChrPos(0x48, -1050, 0, -11060, 180)
    SetChrPos(0x1C, -2210, 0, -13070, 0)
    SetChrPos(0x1D, -1050, 0, -13020, 0)
    SetChrPos(0x1E, -10, 0, -13090, 0)
    SetChrPos(0x1F, -2180, 0, -14600, 0)
    SetChrPos(0x20, -1060, 0, -14610, 0)
    SetChrPos(0x21, 0, 0, -14650, 0)
    SetChrPos(0x31, -2150, 0, -16530, 0)
    SetChrPos(0x32, -1020, 0, -16510, 0)
    SetChrPos(0x33, 80, 0, -16500, 0)
    SetChrPos(0x49, 2240, 0, -11070, 180)
    SetChrPos(0x22, 1170, 0, -12720, 0)
    SetChrPos(0x23, 2150, 0, -12770, 0)
    SetChrPos(0x24, 3180, 0, -12700, 0)
    SetChrPos(0x25, 1140, 0, -14640, 0)
    SetChrPos(0x26, 2180, 0, -14620, 0)
    SetChrPos(0x27, 3210, 0, -14600, 0)
    SetChrPos(0x34, 1210, 0, -16570, 0)
    SetChrPos(0x35, 2200, 0, -16530, 0)
    SetChrPos(0x36, 3260, 0, -16590, 0)
    SetChrPos(0x4A, 5410, 0, -11150, 180)
    SetChrPos(0x28, 4290, 0, -13090, 0)
    SetChrPos(0x29, 5340, 0, -13070, 0)
    SetChrPos(0x2A, 6390, 0, -13060, 0)
    SetChrPos(0x2B, 4370, 0, -14630, 0)
    SetChrPos(0x2C, 5370, 0, -14640, 0)
    SetChrPos(0x2D, 6390, 0, -14610, 0)
    SetChrPos(0x37, 4390, 0, -16570, 0)
    SetChrPos(0x38, 5310, 0, -16510, 0)
    SetChrPos(0x39, 6420, 0, -16530, 0)
    SetChrPos(0x15, -2900, 0, -18790, 180)
    SetChrPos(0x8, -4150, 0, -20160, 0)
    SetChrPos(0x9, -2970, 0, -20180, 0)
    SetChrPos(0xA, -1750, -10, -20160, 0)
    SetChrPos(0xB, -4100, 0, -22060, 0)
    SetChrPos(0xC, -2920, 0, -22000, 0)
    SetChrPos(0xF, -1710, 10, -22060, 0)
    SetChrPos(0x10, -4110, -10, -23710, 0)
    SetChrPos(0x11, -2930, 10, -23790, 0)
    SetChrPos(0x12, -1760, 0, -23740, 0)
    OP_43(0x15, 0x0, 0x0, 0x2)
    OP_43(0x9, 0x0, 0x0, 0x2)
    OP_43(0xA, 0x0, 0x0, 0x2)
    OP_43(0xB, 0x0, 0x0, 0x2)
    OP_43(0xC, 0x0, 0x0, 0x2)
    OP_43(0xF, 0x0, 0x0, 0x2)
    OP_43(0x10, 0x0, 0x0, 0x2)
    OP_43(0x11, 0x0, 0x0, 0x2)
    OP_43(0x12, 0x0, 0x0, 0x2)
    SetChrPos(0x4B, 870, -10, -18600, 180)
    SetChrPos(0x13, -360, -30, -20250, 0)
    SetChrPos(0x14, 690, -30, -20200, 0)
    SetChrPos(0x3A, 1960, 0, -20330, 0)
    SetChrPos(0x3B, -370, 10, -22080, 0)
    SetChrPos(0x3C, 780, 10, -22010, 0)
    SetChrPos(0x3D, 1970, 10, -22010, 0)
    SetChrPos(0x3E, -290, 0, -23840, 0)
    SetChrPos(0x3F, 820, 0, -23860, 0)
    SetChrPos(0x40, 1970, 10, -23820, 0)
    OP_43(0x13, 0x0, 0x0, 0x2)
    OP_43(0x14, 0x0, 0x0, 0x2)
    OP_43(0x15, 0x0, 0x0, 0x2)
    SetChrPos(0x4C, 4560, 30, -18680, 180)
    SetChrPos(0x41, 3390, 20, -20080, 0)
    SetChrPos(0x42, 4570, 0, -20160, 0)
    SetChrPos(0x43, 5840, 30, -20190, 0)
    SetChrPos(0x44, 3430, 10, -22080, 0)
    SetChrPos(0x45, 4630, 10, -22040, 0)
    SetChrPos(0x46, 5900, 0, -22070, 0)
    SetChrPos(0xE, 3410, 10, -23910, 0)
    SetChrPos(0x4D, 4640, -10, -23920, 0)
    SetChrPos(0x4E, 5860, 0, -23900, 0)
    SetChrChipByIndex(0xE, 0)
    SetChrChipByIndex(0x4D, 0)
    SetChrChipByIndex(0x4E, 0)
    OP_6D(0, -500, -17000, 0)
    OP_67(0, 4980, -10000, 0)
    OP_6B(2100, 0)
    OP_6C(334000, 0)
    OP_6E(538, 0)

    def lambda_34E1():
        OP_6D(-3500, 1000, -3000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_34E1)

    def lambda_34F9():
        OP_67(0, 3500, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_34F9)

    def lambda_3511():
        OP_6B(3000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3511)

    def lambda_3521():
        OP_6E(550, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3521)
    Sleep(5000)
    FadeToBright(1000, 0)
    OP_0D()
    SetMapFlags(0x2000000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T1402   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_20_2E21 end

    def Function_21_3557(): pass

    label("Function_21_3557")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_D2(0x2701E6, 0x2701EB, 0x5)
    OP_D2(0x70150, 0x70154, 0x6)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrChipByIndex(0x4D, 5)
    SetChrChipByIndex(0x4E, 6)
    SetChrPos(0x4E, -500, 11750, -3000, 180)
    SetChrPos(0x4D, 500, 11750, -3000, 180)
    ClearChrFlags(0x4D, 0x80)
    ClearChrFlags(0x4E, 0x80)
    OP_6D(630, 11750, -1740, 0)
    OP_67(0, 5040, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(33000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #172
        0x4D,
        "#1128F#5P……………………………………\x02",
    )

    CloseMessageWindow()
    OP_8C(0x4E, 90, 400)
    Sleep(500)

    ChrTalk(    #173
        0x4E,
        (
            "#166F#6P这样好吗……卡西乌斯？\x02\x03",

            "既然那么担心的话，\x01",
            "跟着一起去不就行了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x4D, 270, 400)
    Sleep(400)

    ChrTalk(    #174
        0x4D,
        (
            "#1125F#2P不，还是算了。\x02\x03",

            "#1122F那个叫怀斯曼的男人……\x01",
            "危险程度超乎我的想象。\x02\x03",

            "如果我也一起同行的话，\x01",
            "恐怕他就会不择手段了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x4E,
        (
            "#163F#6P你是怕他会用最极端的手段吗……\x02\x03",

            "#165F……哎呀哎呀。\x01",
            "对方似乎很看重你的能力呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x4D,
        (
            "#1123F#2P我才不希望被他们看重呢。\x02\x03",

            "#1120F不过，反过来说，\x01",
            "这样我们才有了抓住空隙的机会。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x4E,
        (
            "#163F#6P虚虚实实地互相试探吗……\x02\x03",

            "#160F『铁血宰相』那边怎么样了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x4D,
        (
            "#1122F#2P那位宰相大人依旧还是\x01",
            "那么麻烦……\x02\x03",

            "#1125F嗯，不过只要我们不露出破绽，\x01",
            "应该也就没什么问题了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x4E,
        (
            "#166F#6P嗯，是吗……\x02\x03",

            "#163F全部事情就交给\x01",
            "『埃尔赛尤』上的那帮人了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x4D,
        "#1128F#2P啊…唉…\x02",
    )

    CloseMessageWindow()
    OP_8C(0x4D, 180, 400)

    def lambda_3909():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x4E, 1, lambda_3909)
    Sleep(500)

    ChrTalk(    #181
        0x4D,
        (
            "#1122F#5P（莱娜……还有空之女神呀……）\x02\x03",

            "（请为那些孩子\x01",
            "  指明前进的方向吧……）\x02\x03",

            "#1125F（在这广阔的天空下……\x01",
            "  希望他们能找到自己的道路。）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_AD(0x2400B5, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_A2(0x208F)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x12A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-162160, 0, -33060, 0)
    FadeToBright(0, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        240,
        180,
        0,
        (
            "【保存进度】\x01",        # 0
            "【进入下一章】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A30")
    ShowSaveMenu()

    label("loc_3A30")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_AE(0xC8)
    OP_20(0x1388)
    Sleep(2000)
    OP_21()
    ClearParty()
    AddParty(0x0, 0xF6, 0xFF)
    AddParty(0x1, 0xF7, 0xFF)
    OP_A3(0x208F)
    ClearMapFlags(0x100000)
    OP_4F(0x4, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x10F7)
    NewScene("ED6_DT21/E0800   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_21_3557 end

    SaveToFile()

Try(main)
