from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1402   ._SN',
        MapName             = 'Bose',
        Location            = 'T1402.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
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
        '雪拉扎德',                             # 9
        '阿加特',                               # 10
        '提妲',                                 # 11
        '金',                                   # 12
        '科洛蒂娅公主',                         # 13
        '奥利维特皇子',                         # 14
        '赛克斯中将',                           # 15
        '摩尔根将军',                           # 16
        '穆拉少校',                             # 17
        '卡西乌斯',                             # 18
        '拉赛尔博士',                           # 19
        '尤莉亚上尉',                           # 20
        '凯文神父',                             # 21
        '王国军将校',                           # 22
        '王国军将校',                           # 23
        '蒸气坦克',                             # 24
        '蒸气坦克',                             # 25
        '蒸气坦克',                             # 26
        '蒸气坦克',                             # 27
        '蒸气坦克',                             # 28
        '蒸气坦克',                             # 29
        '蒸气坦克',                             # 30
        '蒸气坦克',                             # 31
        '蒸气坦克',                             # 32
        '蒸气坦克',                             # 33
        '蒸气坦克',                             # 34
        '蒸气坦克',                             # 35
        '蒸气坦克',                             # 36
        '蒸气坦克',                             # 37
        '飞船',                                 # 38
        '飞船的影子',                           # 39
        '帝国兵',                               # 40
        '帝国兵',                               # 41
        '帝国兵',                               # 42
        '帝国兵',                               # 43
        '帝国兵',                               # 44
        '帝国兵',                               # 45
        '帝国兵',                               # 46
        '帝国兵',                               # 47
        '帝国兵',                               # 48
        '帝国兵',                               # 49
        '帝国兵',                               # 50
        '帝国兵',                               # 51
        '帝国兵',                               # 52
        '帝国兵',                               # 53
        '帝国兵',                               # 54
        '帝国兵',                               # 55
        '帝国兵',                               # 56
        '帝国兵',                               # 57
        '帝国兵',                               # 58
        '帝国兵',                               # 59
        '帝国兵',                               # 60
        '帝国兵',                               # 61
        '帝国兵',                               # 62
        '帝国兵',                               # 63
        '帝国兵',                               # 64
        '帝国兵',                               # 65
        '帝国兵',                               # 66
        '帝国兵',                               # 67
        '帝国兵',                               # 68
        '帝国兵',                               # 69
        '帝国兵',                               # 70
        '帝国兵',                               # 71
        '帝国兵',                               # 72
        '帝国兵',                               # 73
        '帝国兵',                               # 74
        '帝国兵',                               # 75
        '帝国兵',                               # 76
        '帝国兵',                               # 77
        '帝国兵',                               # 78
        '帝国兵',                               # 79
        '帝国兵',                               # 80
        '帝国兵',                               # 81
        '帝国兵',                               # 82
        '帝国兵',                               # 83
        '帝国兵',                               # 84
        '帝国兵',                               # 85
        '帝国兵',                               # 86
        '帝国兵',                               # 87
        '帝国兵',                               # 88
        '帝国兵',                               # 89
        '帝国兵',                               # 90
        '帝国兵',                               # 91
        '帝国兵',                               # 92
        '帝国兵',                               # 93
        '帝国兵',                               # 94
        '帝国兵',                               # 95
        '帝国兵',                               # 96
        '帝国兵',                               # 97
        '帝国兵',                               # 98
        '帝国兵',                               # 99
        '帝国兵',                               # 100
        '帝国兵',                               # 101
        '帝国兵',                               # 102
        '帝国兵',                               # 103
        '帝国兵',                               # 104
        '帝国兵',                               # 105
        '帝国兵',                               # 106
        '帝国兵',                               # 107
        '帝国兵',                               # 108
        '帝国兵',                               # 109
        '帝国兵',                               # 110
        '帝国兵',                               # 111
        '帝国兵',                               # 112
        '帝国兵',                               # 113
        '帝国兵',                               # 114
        '帝国兵',                               # 115
        '帝国兵',                               # 116
        '帝国兵',                               # 117
        '帝国兵',                               # 118
        '帝国兵',                               # 119
        '帝国兵',                               # 120
        '帝国兵',                               # 121
        '帝国兵',                               # 122
        '帝国兵',                               # 123
        '帝国兵',                               # 124
        '帝国兵',                               # 125
        '帝国兵',                               # 126
        '帝国兵',                               # 127
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


    ScpFunction(
        "Function_0_F8A",          # 00, 0
        "Function_1_FBC",          # 01, 1
        "Function_2_FBD",          # 02, 2
        "Function_3_67F8",         # 03, 3
        "Function_4_6832",         # 04, 4
        "Function_5_6858",         # 05, 5
        "Function_6_687E",         # 06, 6
        "Function_7_68A4",         # 07, 7
        "Function_8_68CA",         # 08, 8
        "Function_9_68F0",         # 09, 9
        "Function_10_6916",        # 0A, 10
        "Function_11_6932",        # 0B, 11
        "Function_12_6953",        # 0C, 12
        "Function_13_696F",        # 0D, 13
        "Function_14_6990",        # 0E, 14
        "Function_15_6BC0",        # 0F, 15
        "Function_16_6F3B",        # 10, 16
        "Function_17_72B6",        # 11, 17
        "Function_18_7523",        # 12, 18
        "Function_19_D55D",        # 13, 19
        "Function_20_D63E",        # 14, 20
        "Function_21_D693",        # 15, 21
        "Function_22_D6FD",        # 16, 22
        "Function_23_D72A",        # 17, 23
        "Function_24_D766",        # 18, 24
        "Function_25_D798",        # 19, 25
        "Function_26_D7D4",        # 1A, 26
        "Function_27_D810",        # 1B, 27
        "Function_28_D84C",        # 1C, 28
        "Function_29_D888",        # 1D, 29
        "Function_30_D8BF",        # 1E, 30
        "Function_31_DA5D",        # 1F, 31
        "Function_32_DDD3",        # 20, 32
        "Function_33_E149",        # 21, 33
        "Function_34_E4BF",        # 22, 34
    )


    def Function_0_F8A(): pass

    label("Function_0_F8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_FA4")
    OP_A3(0x10F0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)
    Jump("loc_FBB")

    label("loc_FA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_FBB")
    OP_A3(0x10F1)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 18)

    label("loc_FBB")

    Return()

    # Function_0_F8A end

    def Function_1_FBC(): pass

    label("Function_1_FBC")

    Return()

    # Function_1_FBC end

    def Function_2_FBD(): pass

    label("Function_2_FBD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_A1(0x17, 0x3)
    OP_A1(0x18, 0x4)
    OP_A1(0x19, 0x5)
    OP_A1(0x1A, 0x6)
    OP_A1(0x1B, 0x7)
    OP_A1(0x1C, 0x8)
    OP_A1(0x1D, 0x9)
    OP_A1(0x1E, 0xA)
    OP_A1(0x1F, 0xB)
    OP_A1(0x20, 0xC)
    OP_A1(0x21, 0xD)
    OP_A1(0x22, 0xE)
    OP_A1(0x23, 0xF)
    OP_A1(0x24, 0x10)
    OP_71(0x3, 0x20)
    OP_71(0x4, 0x20)
    OP_71(0x5, 0x20)
    OP_71(0x6, 0x20)
    OP_71(0x7, 0x20)
    OP_71(0x8, 0x20)
    OP_71(0x9, 0x20)
    OP_71(0xA, 0x20)
    OP_71(0xB, 0x20)
    OP_71(0xC, 0x20)
    OP_71(0xD, 0x20)
    OP_71(0xE, 0x20)
    OP_71(0xF, 0x20)
    OP_71(0x10, 0x20)
    OP_6F(0x3, 91)
    OP_6F(0x4, 91)
    OP_6F(0x5, 91)
    OP_6F(0x6, 91)
    OP_6F(0x7, 91)
    OP_6F(0x8, 91)
    OP_6F(0x9, 91)
    OP_6F(0xA, 91)
    OP_6F(0xB, 91)
    OP_6F(0xC, 91)
    OP_6F(0xD, 91)
    OP_6F(0xE, 91)
    OP_6F(0xF, 91)
    OP_6F(0x10, 91)
    OP_70(0x3, 0x96)
    OP_70(0x4, 0x96)
    OP_70(0x5, 0x96)
    OP_70(0x6, 0x96)
    OP_70(0x7, 0x96)
    OP_70(0x8, 0x96)
    OP_70(0x9, 0x96)
    OP_70(0xA, 0x96)
    OP_70(0xB, 0x96)
    OP_70(0xC, 0x96)
    OP_70(0xD, 0x96)
    OP_70(0xE, 0x96)
    OP_70(0xF, 0x96)
    OP_70(0x10, 0x96)
    OP_D2(0x70020, 0x70028, 0x0)
    OP_D2(0x70050, 0x70058, 0x1)
    OP_D2(0x70060, 0x70068, 0x2)
    OP_D2(0x70070, 0x70078, 0x3)
    OP_D2(0x270398, 0x27039C, 0x4)
    OP_D2(0x2701E7, 0x2701EC, 0x5)
    OP_D2(0x2701EE, 0x2701F3, 0x6)
    OP_D2(0x70150, 0x70154, 0x7)
    OP_D2(0x2701D2, 0x2701D7, 0x8)
    OP_D2(0x270202, 0x270207, 0x9)
    OP_D2(0x700DB, 0x700DF, 0xA)
    OP_71(0x2, 0x4)
    OP_71(0x11, 0x4)
    OP_72(0x1, 0x10)
    OP_6F(0x1, 560)
    SetChrChipByIndex(0x8, 0)
    SetChrChipByIndex(0x9, 1)
    SetChrChipByIndex(0xA, 2)
    SetChrChipByIndex(0xB, 3)
    SetChrChipByIndex(0xC, 4)
    SetChrChipByIndex(0xD, 5)
    SetChrChipByIndex(0xE, 6)
    SetChrChipByIndex(0xF, 7)
    SetChrChipByIndex(0x10, 8)
    SetChrChipByIndex(0x27, 9)
    SetChrChipByIndex(0x28, 9)
    SetChrChipByIndex(0x29, 9)
    SetChrChipByIndex(0x2A, 9)
    SetChrChipByIndex(0x2B, 9)
    SetChrChipByIndex(0x2C, 9)
    SetChrChipByIndex(0x2D, 9)
    SetChrChipByIndex(0x2E, 9)
    SetChrChipByIndex(0x2F, 9)
    SetChrChipByIndex(0x30, 9)
    SetChrChipByIndex(0x31, 9)
    SetChrChipByIndex(0x32, 9)
    SetChrChipByIndex(0x33, 9)
    SetChrChipByIndex(0x34, 9)
    SetChrChipByIndex(0x35, 9)
    SetChrChipByIndex(0x36, 9)
    SetChrChipByIndex(0x37, 9)
    SetChrChipByIndex(0x38, 9)
    SetChrChipByIndex(0x39, 9)
    SetChrChipByIndex(0x3A, 9)
    SetChrChipByIndex(0x3B, 9)
    SetChrChipByIndex(0x3C, 9)
    SetChrChipByIndex(0x3D, 9)
    SetChrChipByIndex(0x3E, 9)
    SetChrChipByIndex(0x3F, 9)
    SetChrChipByIndex(0x40, 9)
    SetChrChipByIndex(0x41, 9)
    SetChrChipByIndex(0x42, 9)
    SetChrChipByIndex(0x43, 9)
    SetChrChipByIndex(0x44, 9)
    SetChrChipByIndex(0x45, 9)
    SetChrChipByIndex(0x46, 9)
    SetChrChipByIndex(0x47, 9)
    SetChrChipByIndex(0x48, 9)
    SetChrChipByIndex(0x49, 9)
    SetChrChipByIndex(0x4A, 9)
    SetChrChipByIndex(0x4B, 9)
    SetChrChipByIndex(0x4C, 9)
    SetChrChipByIndex(0x4D, 9)
    SetChrChipByIndex(0x4E, 9)
    SetChrChipByIndex(0x4F, 9)
    SetChrChipByIndex(0x50, 9)
    SetChrChipByIndex(0x51, 9)
    SetChrChipByIndex(0x52, 9)
    SetChrChipByIndex(0x53, 9)
    SetChrChipByIndex(0x54, 9)
    SetChrChipByIndex(0x55, 9)
    SetChrChipByIndex(0x56, 9)
    SetChrChipByIndex(0x57, 9)
    SetChrChipByIndex(0x58, 9)
    SetChrChipByIndex(0x59, 9)
    SetChrChipByIndex(0x5A, 9)
    SetChrChipByIndex(0x5B, 9)
    SetChrChipByIndex(0x5C, 9)
    SetChrChipByIndex(0x5D, 9)
    SetChrChipByIndex(0x5E, 9)
    SetChrChipByIndex(0x5F, 9)
    SetChrChipByIndex(0x60, 9)
    SetChrChipByIndex(0x61, 9)
    SetChrChipByIndex(0x62, 9)
    SetChrChipByIndex(0x63, 9)
    SetChrChipByIndex(0x64, 9)
    SetChrChipByIndex(0x65, 9)
    SetChrChipByIndex(0x66, 9)
    SetChrChipByIndex(0x67, 9)
    SetChrChipByIndex(0x68, 9)
    SetChrChipByIndex(0x69, 9)
    SetChrChipByIndex(0x6A, 9)
    SetChrChipByIndex(0x6B, 9)
    SetChrChipByIndex(0x6C, 9)
    SetChrChipByIndex(0x6D, 9)
    SetChrChipByIndex(0x6E, 9)
    SetChrChipByIndex(0x6F, 9)
    SetChrChipByIndex(0x70, 9)
    SetChrChipByIndex(0x71, 9)
    SetChrChipByIndex(0x72, 9)
    SetChrChipByIndex(0x73, 9)
    SetChrChipByIndex(0x74, 9)
    SetChrChipByIndex(0x75, 9)
    SetChrChipByIndex(0x76, 9)
    SetChrChipByIndex(0x77, 9)
    SetChrChipByIndex(0x78, 9)
    SetChrChipByIndex(0x79, 9)
    SetChrChipByIndex(0x7A, 9)
    SetChrChipByIndex(0x7B, 9)
    SetChrChipByIndex(0x7C, 9)
    SetChrChipByIndex(0x7D, 9)
    SetChrChipByIndex(0x7E, 9)
    SetChrChipByIndex(0x15, 10)
    SetChrChipByIndex(0x16, 10)
    SetChrPos(0x17, -7460, 0, 138890, 0)
    SetChrPos(0x18, 3360, 0, 138630, 0)
    SetChrPos(0x19, -7650, 0, 153070, 0)
    SetChrPos(0x1A, 3510, 0, 153050, 0)
    SetChrPos(0x1B, -18530, 0, 142310, 0)
    SetChrPos(0x1C, 15560, 0, 143270, 0)
    SetChrPos(0x1D, -19230, 0, 157310, 0)
    SetChrPos(0x1E, 14300, 0, 157350, 0)
    SetChrPos(0x1F, -8090, 0, 167010, 0)
    SetChrPos(0x20, 3690, 0, 166830, 0)
    SetChrPos(0x21, 2670, 0, 183120, 0)
    SetChrPos(0x22, -8410, 0, 183060, 0)
    SetChrPos(0x23, -19940, 0, 174900, 0)
    SetChrPos(0x24, 12450, 0, 174010, 0)
    LoadEffect(0x0, "map\\\\mp109_00.eff")
    LoadEffect(0x1, "map\\\\onsen00.eff")
    PlayEffect(0x0, 0xFF, 0x17, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x17, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x18, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x18, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x19, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x19, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1A, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1A, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1B, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1B, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1C, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1C, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1D, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1D, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1E, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1E, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1F, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1F, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x20, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x20, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x21, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x21, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x22, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x22, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x23, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x23, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x24, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x24, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x17, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x17, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x18, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x18, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x19, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x19, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1A, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1A, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1B, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1B, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1C, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1C, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1D, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1D, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1E, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1E, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1F, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1F, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x20, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x20, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x21, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x21, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x22, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x22, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x23, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x23, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x24, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x24, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x27, -7630, 0, 191450, 180)
    SetChrPos(0x28, -5660, -50, 191450, 180)
    SetChrPos(0x29, -3630, 0, 191450, 180)
    SetChrPos(0x2A, -1730, 90, 191450, 180)
    SetChrPos(0x2B, 230, -30, 191450, 180)
    SetChrPos(0x2C, 2070, -30, 191450, 180)
    SetChrPos(0x2D, -7630, 40, 193600, 180)
    SetChrPos(0x2E, -5660, 20, 193600, 180)
    SetChrPos(0x2F, -3630, -20, 193600, 180)
    SetChrPos(0x30, -1730, 50, 193600, 180)
    SetChrPos(0x31, 230, -20, 193600, 180)
    SetChrPos(0x32, 2070, -50, 193600, 180)
    SetChrPos(0x33, -7630, 30, 195750, 180)
    SetChrPos(0x34, -5660, 10, 195750, 180)
    SetChrPos(0x35, -3630, 20, 195750, 180)
    SetChrPos(0x36, -1730, 70, 195750, 180)
    SetChrPos(0x37, 230, -10, 195750, 180)
    SetChrPos(0x38, 2070, -30, 195750, 180)
    SetChrPos(0x39, -7630, -20, 197900, 180)
    SetChrPos(0x3A, -5660, -40, 197900, 180)
    SetChrPos(0x3B, -3630, -40, 197900, 180)
    SetChrPos(0x3C, -1730, 40, 197900, 180)
    SetChrPos(0x3D, 230, -40, 197900, 180)
    SetChrPos(0x3E, 2070, -20, 197900, 180)
    SetChrPos(0x3F, -7630, -40, 200050, 180)
    SetChrPos(0x40, -5660, 0, 200050, 180)
    SetChrPos(0x41, -3630, 30, 200050, 180)
    SetChrPos(0x42, -1730, 60, 200050, 180)
    SetChrPos(0x43, 230, 10, 200050, 180)
    SetChrPos(0x44, 2070, -20, 200050, 180)
    SetChrPos(0x45, 4000, 0, 191450, 180)
    SetChrPos(0x46, 5930, -50, 191450, 180)
    SetChrPos(0x47, 7900, 0, 191450, 180)
    SetChrPos(0x48, 9800, 90, 191450, 180)
    SetChrPos(0x49, 11700, -30, 191450, 180)
    SetChrPos(0x4A, 13540, -30, 191450, 180)
    SetChrPos(0x4B, 4000, 40, 193600, 180)
    SetChrPos(0x4C, 5930, 20, 193600, 180)
    SetChrPos(0x4D, 7900, -20, 193600, 180)
    SetChrPos(0x4E, 9800, 50, 193600, 180)
    SetChrPos(0x4F, 11700, -20, 193600, 180)
    SetChrPos(0x50, 13540, -50, 193600, 180)
    SetChrPos(0x51, 4000, 30, 195750, 180)
    SetChrPos(0x52, 5930, 10, 195750, 180)
    SetChrPos(0x53, 7900, 20, 195750, 180)
    SetChrPos(0x54, 9800, 70, 195750, 180)
    SetChrPos(0x55, 11700, -10, 195750, 180)
    SetChrPos(0x56, 13540, -30, 195750, 180)
    SetChrPos(0x57, 4000, -20, 197900, 180)
    SetChrPos(0x58, 5930, -40, 197900, 180)
    SetChrPos(0x59, 7900, -40, 197900, 180)
    SetChrPos(0x5A, 9800, 40, 197900, 180)
    SetChrPos(0x5B, 11700, -40, 197900, 180)
    SetChrPos(0x5C, 13540, -20, 197900, 180)
    SetChrPos(0x5D, 4000, -40, 200050, 180)
    SetChrPos(0x5E, 5930, 0, 200050, 180)
    SetChrPos(0x5F, 7900, 30, 200050, 180)
    SetChrPos(0x60, 9800, 60, 200050, 180)
    SetChrPos(0x61, 11700, 10, 200050, 180)
    SetChrPos(0x62, 13540, -20, 200050, 180)
    SetChrPos(0x63, -19030, 0, 191450, 180)
    SetChrPos(0x64, -17150, -50, 191450, 180)
    SetChrPos(0x65, -15270, 0, 191450, 180)
    SetChrPos(0x66, -13390, 90, 191450, 180)
    SetChrPos(0x67, -11510, -30, 191450, 180)
    SetChrPos(0x68, -9600, -30, 191450, 180)
    SetChrPos(0x69, -19030, 40, 193600, 180)
    SetChrPos(0x6A, -17150, 20, 193600, 180)
    SetChrPos(0x6B, -15270, -20, 193600, 180)
    SetChrPos(0x6C, -13390, 50, 193600, 180)
    SetChrPos(0x6D, -11510, -20, 193600, 180)
    SetChrPos(0x6E, -9600, -50, 193600, 180)
    SetChrPos(0x6F, -19030, 30, 195750, 180)
    SetChrPos(0x70, -17150, 10, 195750, 180)
    SetChrPos(0x71, -15270, 20, 195750, 180)
    SetChrPos(0x72, -13390, 70, 195750, 180)
    SetChrPos(0x73, -11510, -10, 195750, 180)
    SetChrPos(0x74, -9600, -30, 195750, 180)
    SetChrPos(0x75, -19030, -20, 197900, 180)
    SetChrPos(0x76, -17150, -40, 197900, 180)
    SetChrPos(0x77, -15270, -40, 197900, 180)
    SetChrPos(0x78, -13390, 40, 197900, 180)
    SetChrPos(0x79, -11510, -40, 197900, 180)
    SetChrPos(0x7A, -9600, -20, 197900, 180)
    SetChrPos(0x7B, -15270, 30, 200050, 180)
    SetChrPos(0x7C, -13390, 60, 200050, 180)
    SetChrPos(0x7D, -11510, 10, 200050, 180)
    SetChrPos(0x7E, -9600, -20, 200050, 180)
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
    ClearChrFlags(0x47, 0x80)
    ClearChrFlags(0x48, 0x80)
    ClearChrFlags(0x49, 0x80)
    ClearChrFlags(0x4A, 0x80)
    ClearChrFlags(0x4B, 0x80)
    ClearChrFlags(0x4C, 0x80)
    ClearChrFlags(0x4D, 0x80)
    ClearChrFlags(0x4E, 0x80)
    ClearChrFlags(0x4F, 0x80)
    ClearChrFlags(0x50, 0x80)
    ClearChrFlags(0x51, 0x80)
    ClearChrFlags(0x52, 0x80)
    ClearChrFlags(0x53, 0x80)
    ClearChrFlags(0x54, 0x80)
    ClearChrFlags(0x55, 0x80)
    ClearChrFlags(0x56, 0x80)
    ClearChrFlags(0x57, 0x80)
    ClearChrFlags(0x58, 0x80)
    ClearChrFlags(0x59, 0x80)
    ClearChrFlags(0x5A, 0x80)
    ClearChrFlags(0x5B, 0x80)
    ClearChrFlags(0x5C, 0x80)
    ClearChrFlags(0x5D, 0x80)
    ClearChrFlags(0x5E, 0x80)
    ClearChrFlags(0x5F, 0x80)
    ClearChrFlags(0x60, 0x80)
    ClearChrFlags(0x61, 0x80)
    ClearChrFlags(0x62, 0x80)
    ClearChrFlags(0x63, 0x80)
    ClearChrFlags(0x64, 0x80)
    ClearChrFlags(0x65, 0x80)
    ClearChrFlags(0x66, 0x80)
    ClearChrFlags(0x67, 0x80)
    ClearChrFlags(0x68, 0x80)
    ClearChrFlags(0x69, 0x80)
    ClearChrFlags(0x6A, 0x80)
    ClearChrFlags(0x6B, 0x80)
    ClearChrFlags(0x6C, 0x80)
    ClearChrFlags(0x6D, 0x80)
    ClearChrFlags(0x6E, 0x80)
    ClearChrFlags(0x6F, 0x80)
    ClearChrFlags(0x70, 0x80)
    ClearChrFlags(0x71, 0x80)
    ClearChrFlags(0x72, 0x80)
    ClearChrFlags(0x73, 0x80)
    ClearChrFlags(0x74, 0x80)
    ClearChrFlags(0x75, 0x80)
    ClearChrFlags(0x76, 0x80)
    ClearChrFlags(0x77, 0x80)
    ClearChrFlags(0x78, 0x80)
    ClearChrFlags(0x79, 0x80)
    ClearChrFlags(0x7A, 0x80)
    ClearChrFlags(0x7B, 0x80)
    ClearChrFlags(0x7C, 0x80)
    ClearChrFlags(0x7D, 0x80)
    ClearChrFlags(0x7E, 0x80)
    SetChrFlags(0x27, 0x200)
    SetChrFlags(0x28, 0x200)
    SetChrFlags(0x29, 0x200)
    SetChrFlags(0x2A, 0x200)
    SetChrFlags(0x2B, 0x200)
    SetChrFlags(0x2C, 0x200)
    SetChrFlags(0x2D, 0x200)
    SetChrFlags(0x2E, 0x200)
    SetChrFlags(0x2F, 0x200)
    SetChrFlags(0x30, 0x200)
    SetChrFlags(0x31, 0x200)
    SetChrFlags(0x32, 0x200)
    SetChrFlags(0x33, 0x200)
    SetChrFlags(0x34, 0x200)
    SetChrFlags(0x35, 0x200)
    SetChrFlags(0x36, 0x200)
    SetChrFlags(0x37, 0x200)
    SetChrFlags(0x38, 0x200)
    SetChrFlags(0x39, 0x200)
    SetChrFlags(0x3A, 0x200)
    SetChrFlags(0x3B, 0x200)
    SetChrFlags(0x3C, 0x200)
    SetChrFlags(0x3D, 0x200)
    SetChrFlags(0x3E, 0x200)
    SetChrFlags(0x3F, 0x200)
    SetChrFlags(0x40, 0x200)
    SetChrFlags(0x41, 0x200)
    SetChrFlags(0x42, 0x200)
    SetChrFlags(0x43, 0x200)
    SetChrFlags(0x44, 0x200)
    SetChrFlags(0x45, 0x200)
    SetChrFlags(0x46, 0x200)
    SetChrFlags(0x47, 0x200)
    SetChrFlags(0x48, 0x200)
    SetChrFlags(0x49, 0x200)
    SetChrFlags(0x4A, 0x200)
    SetChrFlags(0x4B, 0x200)
    SetChrFlags(0x4C, 0x200)
    SetChrFlags(0x4D, 0x200)
    SetChrFlags(0x4E, 0x200)
    SetChrFlags(0x4F, 0x200)
    SetChrFlags(0x50, 0x200)
    SetChrFlags(0x51, 0x200)
    SetChrFlags(0x52, 0x200)
    SetChrFlags(0x53, 0x200)
    SetChrFlags(0x54, 0x200)
    SetChrFlags(0x55, 0x200)
    SetChrFlags(0x56, 0x200)
    SetChrFlags(0x57, 0x200)
    SetChrFlags(0x58, 0x200)
    SetChrFlags(0x59, 0x200)
    SetChrFlags(0x5A, 0x200)
    SetChrFlags(0x5B, 0x200)
    SetChrFlags(0x5C, 0x200)
    SetChrFlags(0x5D, 0x200)
    SetChrFlags(0x5E, 0x200)
    SetChrFlags(0x5F, 0x200)
    SetChrFlags(0x60, 0x200)
    SetChrFlags(0x61, 0x200)
    SetChrFlags(0x62, 0x200)
    SetChrFlags(0x63, 0x200)
    SetChrFlags(0x64, 0x200)
    SetChrFlags(0x65, 0x200)
    SetChrFlags(0x66, 0x200)
    SetChrFlags(0x67, 0x200)
    SetChrFlags(0x68, 0x200)
    SetChrFlags(0x69, 0x200)
    SetChrFlags(0x6A, 0x200)
    SetChrFlags(0x6B, 0x200)
    SetChrFlags(0x6C, 0x200)
    SetChrFlags(0x6D, 0x200)
    SetChrFlags(0x6E, 0x200)
    SetChrFlags(0x6F, 0x200)
    SetChrFlags(0x70, 0x200)
    SetChrFlags(0x71, 0x200)
    SetChrFlags(0x72, 0x200)
    SetChrFlags(0x73, 0x200)
    SetChrFlags(0x74, 0x200)
    SetChrFlags(0x75, 0x200)
    SetChrFlags(0x76, 0x200)
    SetChrFlags(0x77, 0x200)
    SetChrFlags(0x78, 0x200)
    SetChrFlags(0x79, 0x200)
    SetChrFlags(0x7A, 0x200)
    SetChrFlags(0x7B, 0x200)
    SetChrFlags(0x7C, 0x200)
    SetChrFlags(0x7D, 0x200)
    SetChrFlags(0x7E, 0x200)
    OP_6D(-2280, 20, 175640, 0)
    OP_67(0, 6080, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(45000, 0)
    OP_6E(500, 0)
    OP_43(0x17, 0x3, 0x0, 0xE)
    Sleep(1500)
    OP_22(0x10F, 0x1, 0x64)
    OP_22(0x110, 0x1, 0x5A)
    OP_43(0x27, 0x3, 0x0, 0xF)
    OP_43(0x45, 0x3, 0x0, 0x10)
    OP_43(0x63, 0x3, 0x0, 0x11)
    WaitChrThread(0x27, 0x3)
    WaitChrThread(0x45, 0x3)
    WaitChrThread(0x63, 0x3)
    OP_C8(0x200, 0x46, "C_PLAC25._CH", 0x0, 0x3E8)
    FadeToBright(1000, 0)

    def lambda_2A30():
        OP_6D(-3610, -30, 118060, 9000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2A30)
    WaitChrThread(0x101, 0x1)
    Fade(1000)
    OP_6D(-1640, 90, 110610, 0)
    OP_67(0, 4500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(45000, 0)
    OP_6E(267, 0)
    LoadEffect(0x0, "battle\\\\btbomb00.eff")
    PlayEffect(0x1, 0xFF, 0x17, 1050, 4000, 1800, 0, 30, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x17, -1050, 4000, 1800, 0, 30, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x18, 1050, 4000, 1800, 0, 30, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x18, -1050, 4000, 1800, 0, 30, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x19, 1050, 4000, 1800, 0, 30, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x19, -1050, 4000, 1800, 0, 30, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1A, 1050, 4000, 1800, 0, 30, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1A, -1050, 4000, 1800, 0, 30, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1B, 1050, 4000, 1800, 0, 30, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1B, -1050, 4000, 1800, 0, 30, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1C, 1050, 4000, 1800, 0, 30, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1C, -1050, 4000, 1800, 0, 30, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1D, 1050, 4000, 1800, 0, 30, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1D, -1050, 4000, 1800, 0, 30, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1E, 1050, 4000, 1800, 0, 30, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1E, -1050, 4000, 1800, 0, 30, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1F, 1050, 4000, 1800, 0, 30, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1F, -1050, 4000, 1800, 0, 30, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x20, 1050, 4000, 1800, 0, 30, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x20, -1050, 4000, 1800, 0, 30, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x21, 1050, 4000, 1800, 0, 30, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x21, -1050, 4000, 1800, 0, 30, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x22, 1050, 4000, 1800, 0, 30, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x22, -1050, 4000, 1800, 0, 30, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x23, 1050, 4000, 1800, 0, 30, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x23, -1050, 4000, 1800, 0, 30, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x24, 1050, 4000, 1800, 0, 30, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x24, -1050, 4000, 1800, 0, 30, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    SetChrPos(0xF, -1440, 40, 53120, 0)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0x15, -630, 30, 51290, 0)
    SetChrPos(0x16, -2300, 50, 51290, 0)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0xE, -2040, 40, 115000, 180)
    ClearChrFlags(0xE, 0x80)

    def lambda_30CA():
        OP_8E(0xFE, 0xFFFFF8DA, 0x32, 0x17606, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_30CA)
    SetChrPos(0x27, -2870, -20, 116520, 180)
    SetChrPos(0x28, -1230, 30, 116650, 180)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x27, 0x200)
    ClearChrFlags(0x28, 0x200)

    def lambda_311B():
        OP_8E(0xFE, 0xFFFFF52E, 0x32, 0x17F66, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_311B)

    def lambda_3136():
        OP_8E(0xFE, 0xFFFFFC86, 0x0, 0x17F66, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_3136)
    OP_0D()

    def lambda_3152():
        OP_6D(20, 20, 49800, 10000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3152)

    def lambda_316A():
        OP_67(0, 3950, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_316A)

    def lambda_3182():
        OP_6B(3580, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3182)

    def lambda_3192():
        OP_6C(141000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3192)
    OP_6E(511, 10000)
    Sleep(1000)
    Fade(500)
    SetChrFlags(0x45, 0x80)
    SetChrFlags(0x46, 0x80)
    SetChrFlags(0x47, 0x80)
    SetChrFlags(0x48, 0x80)
    SetChrFlags(0x49, 0x80)
    SetChrFlags(0x4A, 0x80)
    SetChrFlags(0x4B, 0x80)
    SetChrFlags(0x4C, 0x80)
    SetChrFlags(0x4D, 0x80)
    SetChrFlags(0x4E, 0x80)
    SetChrFlags(0x4F, 0x80)
    SetChrFlags(0x50, 0x80)
    SetChrFlags(0x51, 0x80)
    SetChrFlags(0x52, 0x80)
    SetChrFlags(0x53, 0x80)
    SetChrFlags(0x54, 0x80)
    SetChrFlags(0x55, 0x80)
    SetChrFlags(0x56, 0x80)
    SetChrFlags(0x57, 0x80)
    SetChrFlags(0x58, 0x80)
    SetChrFlags(0x59, 0x80)
    SetChrFlags(0x5A, 0x80)
    SetChrFlags(0x5B, 0x80)
    SetChrFlags(0x5C, 0x80)
    SetChrFlags(0x5D, 0x80)
    SetChrFlags(0x5E, 0x80)
    SetChrFlags(0x5F, 0x80)
    SetChrFlags(0x60, 0x80)
    SetChrFlags(0x61, 0x80)
    SetChrFlags(0x62, 0x80)
    SetChrFlags(0x63, 0x80)
    SetChrFlags(0x64, 0x80)
    SetChrFlags(0x65, 0x80)
    SetChrFlags(0x66, 0x80)
    SetChrFlags(0x67, 0x80)
    SetChrFlags(0x68, 0x80)
    SetChrFlags(0x69, 0x80)
    SetChrFlags(0x6A, 0x80)
    SetChrFlags(0x6B, 0x80)
    SetChrFlags(0x6C, 0x80)
    SetChrFlags(0x6D, 0x80)
    SetChrFlags(0x6E, 0x80)
    SetChrFlags(0x6F, 0x80)
    SetChrFlags(0x70, 0x80)
    SetChrFlags(0x71, 0x80)
    SetChrFlags(0x72, 0x80)
    SetChrFlags(0x73, 0x80)
    SetChrFlags(0x74, 0x80)
    SetChrFlags(0x75, 0x80)
    SetChrFlags(0x76, 0x80)
    SetChrFlags(0x77, 0x80)
    SetChrFlags(0x78, 0x80)
    SetChrFlags(0x79, 0x80)
    SetChrFlags(0x7A, 0x80)
    SetChrFlags(0x7B, 0x80)
    SetChrFlags(0x7C, 0x80)
    SetChrFlags(0x7D, 0x80)
    SetChrFlags(0x7E, 0x80)
    OP_6D(-1840, 20, 98080, 0)
    OP_67(0, 2800, -10000, 0)
    OP_6B(2029, 0)
    OP_6C(359000, 0)
    OP_6E(554, 0)
    SetChrPos(0xF, -1500, 80, 82610, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #0
        0xF,
        (
            "#162F#5P解释一下吧！\x01",
            "赛克斯·范德尔中将！\x02\x03",

            "为何帝国军的师团\x01",
            "会出现在这里！？\x02\x03",

            "刚刚签订了互不侵犯条约，\x01",
            "可别说你已经忘了！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xE,
        (
            "#882F#5P摩尔根将军……\x01",
            "想得到解释的\x01",
            "倒不如说是我们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xF,
        "#161F#5P什么……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xE,
        (
            "#884F#5P前些日子，帝国南部街道上\x01",
            "的导力器全部无法工作了，\x01",
            "而且异常现象持续不断。\x02\x03",

            "这是因出现在贵国上空的\x01",
            "巨大谜之物体而造成的，\x01",
            "我们收到了这样的报告。\x02\x03",

            "#880F这到底是怎么一回事？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xF,
        (
            "#166F#5P……这没什么好问的，\x01",
            "就如你刚才所说的那样。\x02\x03",

            "我们王国也正因为突然出现的灾难\x01",
            "而处于混乱状态。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xE,
        (
            "#884F#5P看得出来。\x02\x03",

            "#882F但这灾祸正在侵蚀我们帝国\x01",
            "的领土也是事实。\x02\x03",

            "因此，我们会在这里的理由\x01",
            "你们应该也能够理解。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xF,
        (
            "#160F#5P你们……\x01",
            "打算乘虚而入吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xE,
        (
            "#884F#5P我先说在前头，\x01",
            "帝国方没这个意思。\x02\x03",

            "#881F有可疑的犯罪组织\x01",
            "趁着这异常现象在王国内\x01",
            "四处捣乱，这些我也听说了。\x02\x03",

            "作为缔结了互不侵犯条约的同盟国，\x01",
            "希望能够出份力……\x02\x03",

            "我们帝国政府\x01",
            "正是这样的意思。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xF,
        (
            "#162F#5P真是笑话……\x01",
            "那么那些战车是什么！？\x02\x03",

            "蒸气驱动的战车\x01",
            "我至今为止就没听说过！\x02\x03",

            "为什么那种东西恰巧\x01",
            "会在这种情形下被派遣到这里！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xE,
        (
            "#884F#5P这……我只能说是军事机密吧。\x02\x03",

            "#881F然而，正因为有这战车，\x01",
            "才能缓和市民们的不安，\x01",
            "它正适合解救贵国的困境，\x02\x03",

            "您能理解吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xF,
        "#166F#5P可…可恶…\x02",
    )

    CloseMessageWindow()
    SetChrPos(0xC, -800, 0, 82000, 0)

    NpcTalk(    #11
        0xC,
        "女孩的声音",
        (
            "#5P……你们这么费心，\x01",
            "我感到十分高兴。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xF,
        "#161F#5P！？\x02",
    )

    OP_62(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    CloseMessageWindow()
    Sleep(1000)
    Fade(1000)
    OP_6D(110, -20, 18300, 0)
    OP_67(0, 5340, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(139000, 0)
    OP_6E(302, 0)
    SetChrPos(0xF, -1440, 40, 53120, 0)
    SetChrPos(0xC, 140, -10, 19820, 0)
    SetChrPos(0x101, -420, -30, 18190, 0)
    SetChrPos(0x102, 790, 60, 18260, 0)
    SetChrPos(0x8, -1400, -20, 17170, 0)
    SetChrPos(0xA, 1680, 40, 16900, 0)
    SetChrPos(0xB, -830, -20, 15200, 0)
    SetChrPos(0x9, 1270, 20, 15600, 0)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xA, 0x80)

    def lambda_3916():
        OP_91(0xFE, 0x0, 0x0, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_3916)

    def lambda_3931():
        OP_91(0xFE, 0x0, 0x0, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3931)

    def lambda_394C():
        OP_91(0xFE, 0x0, 0x0, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_394C)

    def lambda_3967():
        OP_91(0xFE, 0x0, 0x0, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3967)

    def lambda_3982():
        OP_91(0xFE, 0x0, 0x0, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3982)

    def lambda_399D():
        OP_91(0xFE, 0x0, 0x0, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_399D)

    def lambda_39B8():
        OP_91(0xFE, 0x0, 0x0, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_39B8)

    def lambda_39D3():

        label("loc_39D3")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_39D3")

    QueueWorkItem2(0xF, 1, lambda_39D3)
    OP_8C(0x15, 180, 0)
    OP_8C(0x16, 180, 0)
    OP_0D()
    OP_6D(-50, 60, 23000, 3000)
    Fade(1000)
    OP_6D(640, 10, 51040, 0)
    OP_67(0, 4740, -10000, 0)
    OP_6B(3040, 0)
    OP_6C(135000, 0)
    OP_6E(322, 0)
    OP_43(0xC, 0x1, 0x0, 0x3)
    OP_43(0x101, 0x1, 0x0, 0x4)
    OP_43(0x102, 0x1, 0x0, 0x5)
    OP_43(0x8, 0x1, 0x0, 0x6)
    OP_43(0xA, 0x1, 0x0, 0x7)
    OP_43(0x9, 0x1, 0x0, 0x8)
    OP_43(0xB, 0x1, 0x0, 0x9)
    OP_0D()
    Sleep(1000)
    OP_43(0x15, 0x1, 0x0, 0xA)
    OP_43(0x16, 0x1, 0x0, 0xB)
    WaitChrThread(0xC, 0x1)
    OP_62(0xF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #13
        0xF,
        (
            "#161F#4P什…什么…！\x02\x03",

            "（公、公主殿下！？\x01",
            "  怎么会在这里！？）\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3AE5():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_3AE5)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x200, 0x4B, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x200, 0xFFFFFF, 0x0, "C_VIS224._CH")
    OP_C6(0x0, 0x0, 55000, 50000, 0)
    OP_C6(0x0, 0x0, 105000, 50000, 500)
    OP_C6(0x0, 0x3, -1, 1000, 0)
    Sleep(1000)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("科洛蒂娅公主")

    AnonymousTalk(    #14
        (
            "（摩尔根将军，您辛苦了。）\x02\x03",

            "（这里的谈判\x01",
            "  可以交给我吗？）\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("摩尔根将军")

    AnonymousTalk(    #15
        "#161F（可、可是……）\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, 16777215, 250, 0)
    OP_44(0xF, 0x1)
    OP_8C(0xF, 180, 400)
    Sleep(300)

    ChrTalk(    #16
        0xF,
        (
            "#162F#6P（而且为什么\x01",
            "  连你们都在这里！？）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x101,
        "#1006F#2P（算是科洛丝的护卫吧。）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x102,
        (
            "#1040F#2P（还有，万不得已的时候\x01",
            "  我们打算进行调停。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xF,
        "#160F#6P（……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xC,
        (
            "#1167F#5P（不成熟的我或许无法\x01",
            "  胜任交涉的任务……）\x02\x03",

            "#1162F（然而，身为王太女，我想现在应该是\x01",
            "  履行王太女义务的时候了。）\x02\x03",

            "（总之……拜托您了。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xF,
        "#163F#6P（……明白了。）\x02",
    )

    CloseMessageWindow()
    OP_8C(0xF, 90, 400)
    Sleep(300)

    ChrTalk(    #22
        0xF,
        (
            "#166F#4P（但是，现在不知道\x01",
            "  对方何时会发动攻击。）\x02\x03",

            "（万不得已的时候请立即\x01",
            "  做好退向大门的准备。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xC,
        "#1168F#5P（……明白了。）\x02",
    )

    CloseMessageWindow()
    OP_8C(0xC, 0, 400)
    Sleep(500)

    def lambda_3DFA():

        label("loc_3DFA")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_3DFA")

    QueueWorkItem2(0xF, 1, lambda_3DFA)

    def lambda_3E0B():
        OP_6D(-380, 80, 55800, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3E0B)

    def lambda_3E23():
        OP_67(0, 5920, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3E23)

    def lambda_3E3B():
        OP_6B(2120, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3E3B)

    def lambda_3E4B():
        OP_6C(32000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3E4B)

    def lambda_3E5B():
        OP_6E(414, 3000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_3E5B)
    OP_8E(0xC, 0xFFFFFCD6, 0xA, 0xD764, 0x5DC, 0x0)
    WaitChrThread(0x101, 0x0)
    OP_44(0xF, 0x1)

    def lambda_3E88():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_3E88)

    def lambda_3E96():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_3E96)
    OP_8C(0x16, 0, 400)
    SetChrPos(0xE, -1230, 60, 73610, 180)
    SetChrFlags(0xE, 0x80)

    ChrTalk(    #24
        0xE,
        (
            "#880F看来交涉对象\x01",
            "似乎换人了啊。\x02\x03",

            "看起来，好像是\x01",
            "身份相当高贵的人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xC,
        (
            "#1167F#4P幸会。\x02\x03",

            "#1162F我的名字是\x01",
            "科洛蒂娅·冯·奥赛雷丝。\x02\x03",

            "身为利贝尔女王艾莉茜雅的孙女，\x01",
            "前几天刚被立为下任女王。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xE,
        (
            "#883F#3S！！#2S\x02\x03",

            "这、这真是失敬！\x02\x03",

            "#882F在下名为\x01",
            "赛克斯·范德尔。\x02\x03",

            "埃雷波尼亚帝国军——\x01",
            "第３师团所属的中将。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xC,
        (
            "#1160F#4P您就是……\x01",
            "久闻大名。\x02",
        )
    )

    CloseMessageWindow()
    OP_6D(-190, 20, 50280, 1500)

    ChrTalk(    #28
        0x101,
        "#1015F#6P（那个大叔，很有名吗？）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x102,
        (
            "#1042F#2P（『独眼赛克斯』……\x01",
            "是帝国屈指可数的名将啊。）\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(-1840, 20, 98080, 0)
    OP_67(0, 2800, -10000, 0)
    OP_6B(2029, 0)
    OP_6C(359000, 0)
    OP_6E(554, 0)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xC, -1500, 80, 82610, 0)
    SetChrPos(0xE, -1830, 50, 95750, 180)
    OP_0D()
    Sleep(500)

    ChrTalk(    #30
        0xE,
        (
            "#883F#5P不过，以前\x01",
            "曾有幸见过殿下的照片……\x02\x03",

            "您剪过头发了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xC,
        (
            "#1165F#5P非常抱歉……\x01",
            "我刚刚完成王位继承的仪式。\x02\x03",

            "#1382F请视之为一名女子在面对重任时\x01",
            "表达决心的方式吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xE,
        (
            "#884F#5P不、不过这形象\x01",
            "也非常适合您啊。\x02\x03",

            "#881F那……\x01",
            "衷心祝贺您\x01",
            "成为王太女殿下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xC,
        "#1168F#5P非常感谢，中将。\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(-820, 30, 53250, 0)
    OP_67(0, 2970, -10000, 0)
    OP_6B(1750, 0)
    OP_6C(180000, 0)
    OP_6E(554, 0)
    SetChrPos(0xC, -810, 10, 55140, 0)
    SetChrPos(0xE, -800, 0, 67260, 180)
    SetChrPos(0x101, -900, 80, 47870, 0)
    SetChrPos(0x102, 60, 80, 47660, 0)
    SetChrPos(0x8, -1730, 20, 46400, 0)
    SetChrPos(0xA, 810, -30, 46380, 0)
    SetChrPos(0x9, 1400, 50, 45360, 0)
    SetChrPos(0xB, -100, 80, 44800, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #34
        0xE,
        (
            "#882F#5P那么……王太女殿下\x01",
            "怎么会出现在这种地方？\x02\x03",

            "是和摩尔根将军一样\x01",
            "来向我们抗议的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xC,
        (
            "#1167F#5P不……\x01",
            "并没有这个打算。\x02\x03",

            "帝国南部的居民\x01",
            "想必也经历了\x01",
            "不少不安的事吧。\x02\x03",

            "#1169F夜晚的黑暗、寒冷、信息的断绝……\x02\x03",

            "全都是十分\x01",
            "令人不安的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xE,
        "#880F#5P…………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xC,
        (
            "#1162F#5P然而，希望你们考虑一下。\x02\x03",

            "如果贵国的军队就这样进入\x01",
            "我国的话，将会造成何种局面。\x02\x03",

            "#1167F原本，我们全国就处在\x01",
            "比贵国更加混乱的状况下。\x02\x03",

            "就算你们没有其它意图，\x01",
            "但因此而动摇的市民也绝不会在少数……\x02\x03",

            "#1163F若是导致误解了贵国的善意，\x01",
            "我认为这对民众是莫大的损害。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xE,
        "#883F#5P可、可是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xC,
        (
            "#1160F#5P目前，我们\x01",
            "将以摸索、解决这次的异常现象\x01",
            "作为最优先的事项。\x02\x03",

            "而对于前面所说的犯罪组织，\x01",
            "我们也能够以自己的力量来应对。\x02\x03",

            "#1167F为了避免互不侵犯条约\x01",
            "所培养出的友情产生无意义的裂痕……\x02\x03",

            "#1162F请你们暂时\x01",
            "给我们一点时间好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xE,
        "#884F#5P………………………\x02",
    )

    CloseMessageWindow()
    SetChrPos(0xD, -1200, 0, 67260, 180)

    NpcTalk(    #41
        0xD,
        "青年的声音",
        (
            "#5P……很遗憾，\x01",
            "这只是你们的情况。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Fade(1000)
    OP_6D(-2390, 10, 114680, 0)
    OP_67(0, 7930, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(0, 0)
    OP_6E(440, 0)
    SetChrPos(0x10, -2720, -20, 116010, 180)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0xE, -1830, 50, 95750, 180)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xD, -1960, 50, 114500, 180)

    def lambda_4735():
        OP_8E(0xFE, 0xFFFFF8B2, 0xA, 0x19014, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4735)

    def lambda_4750():
        OP_8E(0xFE, 0xFFFFF542, 0x1E, 0x19528, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4750)
    OP_0D()

    def lambda_476C():
        OP_6D(-2000, 100, 103900, 6000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_476C)

    def lambda_4784():
        OP_67(0, 3090, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4784)

    def lambda_479C():
        OP_6B(2760, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_479C)

    def lambda_47AC():
        OP_6E(340, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_47AC)
    OP_8C(0xE, 0, 400)
    OP_8C(0x27, 0, 400)
    OP_8C(0x28, 0, 400)
    Sleep(2000)
    OP_43(0x27, 0x0, 0x0, 0xC)
    OP_43(0x28, 0x0, 0x0, 0xD)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #42
        0xE,
        "#883F#6P……皇子……\x02",
    )

    CloseMessageWindow()
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x200, 0x4B, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x200, 0xFFFFFF, 0x0, "C_VIS223._CH")
    OP_C6(0x1, 0x0, 70000, 50000, 0)
    OP_C6(0x1, 0x0, 120000, 50000, 500)
    OP_C6(0x1, 0x3, -1, 1000, 0)
    Sleep(1200)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("穿军装的青年")

    AnonymousTalk(    #43
        (
            "这里就交给我吧。\x02\x03",

            "你退下，中将。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("赛克斯中将")

    AnonymousTalk(    #44
        "#884F……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x1, 0x3, 16777215, 250, 0)
    Sleep(500)
    Fade(500)
    OP_6D(1670, -30, 48330, 0)
    OP_67(0, 4510, -10000, 0)
    OP_6B(3270, 0)
    OP_6C(135000, 0)
    OP_6E(304, 0)
    SetChrPos(0x101, -1300, 80, 47870, 0)
    SetChrPos(0x102, 360, 80, 47660, 0)
    SetChrPos(0x8, -1530, 20, 46400, 0)
    SetChrPos(0xA, 610, -30, 46380, 0)
    SetChrPos(0x9, 1350, 50, 45360, 0)
    SetChrPos(0xB, 0, 80, 44800, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #45
        0x101,
        "#1020F#5P……咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x8,
        "#023F#2P不会吧……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x9,
        "#055F#5P开玩笑吧……\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(-20, 10, 101410, 0)
    OP_67(0, 4580, -10000, 0)
    OP_6B(3350, 0)
    OP_6C(44000, 0)
    OP_6E(299, 0)

    def lambda_4A16():
        OP_6D(-990, 20, 95740, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4A16)

    def lambda_4A2E():
        OP_6B(2890, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4A2E)

    def lambda_4A3E():
        OP_8E(0xFE, 0xFFFFF876, 0x32, 0x171F6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4A3E)
    Sleep(200)

    def lambda_4A5E():
        OP_8E(0xFE, 0xFFFFFA24, 0x14, 0x17B38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4A5E)
    Sleep(500)
    OP_8C(0xE, 90, 400)

    def lambda_4A85():
        OP_8F(0xFE, 0xFFFFF2CC, 0xFFFFFFD8, 0x17692, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4A85)
    WaitChrThread(0xD, 0x1)
    WaitChrThread(0xE, 0x1)
    OP_8C(0xE, 180, 400)
    WaitChrThread(0x10, 0x1)
    WaitChrThread(0x101, 0x0)
    OP_8C(0x27, 180, 400)
    OP_8C(0x28, 180, 400)

    NpcTalk(    #48
        0xD,
        "穿军装的青年",
        (
            "#894F#5P幸会。\x01",
            "科洛蒂娅公主殿下。\x02\x03",

            "#895F我是埃雷波尼亚皇帝尤肯特之子，\x01",
            "奥利维特·莱泽·亚诺尔。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x101, -5000, 10, 85000, 0)
    SetChrPos(0x8, -5000, 10, 85000, 0)

    ChrTalk(    #49
        0x101,
        (
            "#1020F#1P！！！\x02\x03",

            "#1005F（皇帝之子……\x01",
            "  那、那不就是皇子殿下～！？）\x02\x03",

            "（雪拉姐，你知道的吗！？）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x8,
        (
            "#023F#1P（怎、怎么可能知道！）\x02\x03",

            "#025F（我还以为一定是\x01",
            "  帝国派来的情报员……）\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(-1840, 20, 98080, 0)
    OP_67(0, 2800, -10000, 0)
    OP_6B(2029, 0)
    OP_6C(359000, 0)
    OP_6E(554, 0)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xD, -1850, 50, 94710, 180)
    SetChrPos(0x10, -850, 20, 97080, 180)
    SetChrPos(0xE, -2850, -20, 96930, 180)
    SetChrPos(0xC, -1500, 80, 82610, 0)
    SetChrPos(0x101, -1600, 10, 82610, 0)
    SetChrPos(0x102, -1500, 10, 82610, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #51
        0xC,
        (
            "#1164F#5P奥利维特皇子……\x01",
            "虽然只知道名号。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xD,
        (
            "#891F#5P呵呵，虽说是皇子，\x01",
            "但并不是正室所生。\x02\x03",

            "很少出席正式场合，\x01",
            "所以不知道长相也不足为奇。\x02\x03",

            "#895F不过，话虽如此，\x01",
            "也还是吃了一惊啊。\x02\x03",

            "虽然最终还是无缘，\x01",
            "但至少也是曾经许婚的对象，\x01",
            "还以为至少会知道长相呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        (
            "#1020F#5P！？\x02\x03",

            "#1019F（什、什么～！？）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x102,
        (
            "#1043F#2P（是吗……\x01",
            "  上校说过的那件事吗。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xC,
        (
            "#1163F#5P是这样吗……\x02\x03",

            "#1167F虽然这件事我并未得知，\x01",
            "但真是对不起。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xD,
        (
            "#894F#5P听说这门婚事是在\x01",
            "女王陛下不知道的情况下进行的。\x02\x03",

            "所以请不必在意……\x02\x03",

            "#896F但是……\x01",
            "此次的事态就没有那么简单了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xC,
        "#1163F#5P……啊…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xD,
        (
            "#896F#5P科洛蒂娅公主。\x02\x03",

            "现在，帝国正在流传着\x01",
            "怎样的传闻，您知道吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xC,
        "#1169F#5P……不，我孤陋寡闻了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xD,
        (
            "#899F#5P那么我来告诉您吧。\x02\x03",

            "#897F远方看见的那个巨大构造物……\x01",
            "传闻是王国军研制的新兵器。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xC,
        "#1164F#5P#3S！！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xD,
        (
            "#899F#5P『利贝尔军发明了\x01",
            "  能够停止导力的跨时代新兵器。』\x02\x03",

            "『他们似乎想使用那座兵器\x01",
            "  谋划着对１０年前的报复。』\x02\x03",

            "#897F……这种传闻\x01",
            "正在帝国境内广泛地流传着。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xC,
        (
            "#1163F#5P怎、怎么会……\x02\x03",

            "#1166F这是误解！\x01",
            "我们怎么会……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xD,
        (
            "#896F#5P那么……\x01",
            "您能证明这是误解吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xC,
        "#1169F#5P……唔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xD,
        (
            "#899F#5P既然无法做到，\x01",
            "那我们也只好自行\x01",
            "做出相应的对策了。\x02\x03",

            "不仅如此，如果传言是真的，\x01",
            "那就是利用互不侵犯条约来掩人耳目，\x01",
            "暗中却策划着重大的背信行为。\x02\x03",

            "#896F呵呵……那样的话，我们\x01",
            "进行正当防卫，不也是理所当然的吗？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(1670, -30, 48330, 0)
    OP_67(0, 4550, -10000, 0)
    OP_6B(3270, 0)
    OP_6C(135000, 0)
    OP_6E(304, 0)
    SetChrPos(0x101, -1300, 80, 47870, 0)
    SetChrPos(0x8, -1530, 20, 46400, 0)
    SetChrPos(0xC, -810, 10, 55140, 0)
    SetChrPos(0x102, 360, 80, 47660, 0)
    OP_0D()
    OP_62(0x101, 0x0, 1900, 0x2C, 0x2F, 0x96, 0x1)
    OP_22(0x2F, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(    #67
        0x101,
        "#1005F#2P#4S你适可而止吧！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_52D5():

        label("loc_52D5")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_52D5")

    QueueWorkItem2(0x102, 1, lambda_52D5)
    Sleep(50)

    def lambda_52EB():

        label("loc_52EB")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_52EB")

    QueueWorkItem2(0xC, 1, lambda_52EB)
    Sleep(50)

    def lambda_5301():

        label("loc_5301")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_5301")

    QueueWorkItem2(0x9, 1, lambda_5301)
    Sleep(50)

    def lambda_5317():

        label("loc_5317")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_5317")

    QueueWorkItem2(0xA, 1, lambda_5317)
    Sleep(50)

    def lambda_532D():

        label("loc_532D")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_532D")

    QueueWorkItem2(0xF, 1, lambda_532D)

    ChrTalk(    #68
        0x102,
        "#1044F#5P艾丝蒂尔……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xA,
        "#065F#5P姐，姐姐！？\x02",
    )

    CloseMessageWindow()

    def lambda_5375():
        OP_6D(-1800, 50, 54200, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5375)

    def lambda_538D():
        OP_6B(2950, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_538D)
    OP_8E(0x101, 0xFFFFF614, 0x28, 0xD796, 0x1770, 0x0)
    OP_44(0x102, 0x1)
    OP_44(0xA, 0x1)
    OP_44(0x9, 0x1)
    OP_44(0xF, 0x1)
    OP_44(0xC, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0xA, 0x1)
    OP_8C(0x102, 0, 400)
    OP_8C(0xA, 0, 400)
    OP_8C(0xF, 0, 400)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #70
        0x101,
        (
            "#1005F#2P我们没出声，\x01",
            "你竟然就开始得意忘形，信口开河！\x02\x03",

            "奥利维尔也大致明白\x01",
            "我们的情况吧！？\x02\x03",

            "怎么还能说出\x01",
            "那么可恶的话来！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xC,
        "#1163F#5P艾、艾丝蒂尔……\x02",
    )

    CloseMessageWindow()
    SetChrPos(0xD, -5500, 20, 67000, 180)

    ChrTalk(    #72
        0xD,
        (
            "#897F#2P哎呀……你是谁？\x02\x03",

            "好像认识我一样，\x01",
            "是在哪个舞会上见过吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x101,
        "#1004F#2P咦……\x02",
    )

    CloseMessageWindow()
    OP_8C(0xC, 0, 400)

    ChrTalk(    #74
        0xD,
        (
            "#890F#2P不，以贵族来说\x01",
            "似乎略欠些气质……\x02\x03",

            "唔，怎么看都是\x01",
            "平民的女儿啊。\x02\x03",

            "#891F那，你是什么人？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #75
        0x101,
        (
            "#1019F#2P……好家伙。\x01",
            "要装傻到底是吧。\x02\x03",

            "既然你这么说，\x01",
            "我也有我的做法!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xD,
        "#895F#2P噢……？\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5867")

    ChrTalk(    #77
        0x101,
        (
            "#1005F#2P我的名字叫\x01",
            "艾丝蒂尔·布莱特！\x02\x03",

            "是从属于利贝尔游击士协会\x01",
            "的Ａ级游击士！\x02\x03",

            "就让我彻底从中立的立场\x01",
            "来介入这个问题吧！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_8C(0xC, 270, 400)

    ChrTalk(    #78
        0xC,
        "#1164F#5P艾丝蒂尔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xD,
        (
            "#898F#2P哦，Ａ级游击士……\x02\x03",

            "#891F（……哼哼。\x01",
            "　做得不错嘛。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x101,
        "#1004F#2P哎？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xD,
        (
            "#899F#2P失、失敬了……\x02\x03",

            "#897F所谓的Ａ级，无论在哪国的游击士协会\x01",
            "都是只有最顶级的强者才会\x01",
            "被授予的等级啊。\x02\x03",

            "老实说，像你这样的少女竟然也是Ａ级游击士，\x01",
            "实在让人很难相信。  \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x101,
        (
            "#1006F#2P那样的话，就请您\x01",
            "同游击士协会进行询问对质好了。\x02\x03",

            "不过在那期间，\x01",
            "交涉就要暂时中断了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xD,
        (
            "#895F#2P呼……不必了。\x02\x03",

            "#896F你说要站在中立的立场上介入,\x01",
            "那这个状况下你打算怎么做呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5EEB")

    label("loc_5867")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_59FD")

    ChrTalk(    #84
        0x101,
        (
            "#1005F#2P我的名字叫\x01",
            "艾丝蒂尔·布莱特！\x02\x03",

            "是从属于利贝尔游击士协会\x01",
            "的Ｂ级游击士！\x02\x03",

            "就让我彻底从中立的立场\x01",
            "来介入这个问题吧！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_8C(0xC, 270, 400)

    ChrTalk(    #85
        0xC,
        "#1164F#5P艾丝蒂尔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xD,
        (
            "#898F#2P原来如此，是游击士吗。\x02\x03",

            "#895F嗯，Ｂ级的话，\x01",
            "确实是相当高的等级，不过……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x101,
        "#1002F#2P还是不能信任吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xD,
        (
            "#894F#2P哪里的话，失敬了。\x02\x03",

            "#896F你说要站在中立的立场上介入,\x01",
            "那这个状况下你打算怎么做呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5EEB")

    label("loc_59FD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5B4E")

    ChrTalk(    #89
        0x101,
        (
            "#1005F#2P我的名字叫\x01",
            "艾丝蒂尔·布莱特！\x02\x03",

            "是从属于利贝尔游击士协会\x01",
            "的Ｃ级游击士！\x02\x03",

            "就让我彻底从中立的立场\x01",
            "来介入这个问题吧！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_8C(0xC, 270, 400)

    ChrTalk(    #90
        0xC,
        "#1164F#5P艾丝蒂尔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xD,
        (
            "#895F#2P原来如此，是游击士吗。\x02\x03",

            "#894F嗯，Ｃ级的话，\x01",
            "也算是有一定功绩的吧。\x02\x03",

            "#896F你说要站在中立的立场上介入,\x01",
            "那这个状况下你打算怎么做呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5EEB")

    label("loc_5B4E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5D18")

    ChrTalk(    #92
        0x101,
        (
            "#1005F#2P我的名字叫\x01",
            "艾丝蒂尔·布莱特！\x02\x03",

            "是从属于利贝尔游击士协会\x01",
            "的Ｄ级游击士！\x02\x03",

            "就让我彻底从中立的立场\x01",
            "来介入这个问题吧！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_8C(0xC, 270, 400)

    ChrTalk(    #93
        0xC,
        "#1164F#5P艾丝蒂尔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xD,
        (
            "#895F#2P喔，是游击士吗。\x02\x03",

            "#894F嗯……我听说游击士的等级\x01",
            "从Ｇ级到Ａ级共有七个等级。\x02\x03",

            "#896F区区一个Ｄ级游击士的话，\x01",
            "你认为会有多大的信服力呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x101,
        "#1026F#2P那、那个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xD,
        (
            "#890F#2P算了，继续说下去吧。\x02\x03",

            "你说站在中立的立场上介入，\x01",
            "那这个状况下你打算怎么做呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5EEB")

    label("loc_5D18")


    ChrTalk(    #97
        0x101,
        (
            "#1005F#2P我的名字叫\x01",
            "艾丝蒂尔·布莱特！\x02\x03",

            "是从属于利贝尔游击士协会\x01",
            "的Ｅ级游击士！\x02\x03",

            "就让我彻底从中立的立场\x01",
            "来介入这个问题吧！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_8C(0xC, 270, 400)

    ChrTalk(    #98
        0xC,
        "#1164F#5P艾丝蒂尔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xD,
        (
            "#898F#2P喔，是游击士吗。\x02\x03",

            "#895F嗯……我听说游击士的等级\x01",
            "从Ｇ级到Ａ级共有七个等级。\x02\x03",

            "你这种等级连中流都排不上，\x01",
            "又有什么好说的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x101,
        "#1019F#2P呜……那个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xD,
        (
            "#891F#2P算了，看在你拥有如此胆量\x01",
            "的面子上，就继续说下去吧。\x02\x03",

            "#895F你说站在中立的立场上介入,\x01",
            "那这个状况下你打算怎么做呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5EEB")

    OP_8C(0xC, 0, 400)

    ChrTalk(    #102
        0x101,
        (
            "#1005F#2P那个浮游都市\x01",
            "不是利贝尔的兵器。\x01",
            "我在此正式宣言！\x02\x03",

            "以我的『游击士徽章』作担保！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xD,
        (
            "#895F#2P噢……了不起。\x02\x03",

            "#899F游击士协会的发言确实\x01",
            "有着不可忽视的影响力……\x02\x03",

            "#897F然而这个宣言\x01",
            "有多少根据呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x101,
        (
            "#1007F#2P不需要根据，因为\x01",
            "从头到尾我们都亲眼见到了。\x02\x03",

            "#1002F让浮游都市出现的\x01",
            "就是现在在利贝尔暗中活动着的\x01",
            "一个叫『噬身之蛇』的结社组织。\x02\x03",

            "我们正和王国军协力\x01",
            "阻止他们的阴谋。\x02\x03",

            "#1006F想知道详细情况的话，我们向帝国政府\x01",
            "提出报告书也没问题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xD,
        (
            "#894F#2P唔……\x02\x03",

            "这样一说\x01",
            "不得不稍微考虑一下……\x02\x03",

            "#896F但你似乎\x01",
            "忽略了最关键的事情吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x101,
        "#1026F#2P咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xD,
        (
            "#897F#2P假设那个什么结社\x01",
            "是犯人……\x02\x03",

            "那么你们到底有没有\x01",
            "阻止这个异常现象的方法呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #108
        0x101,
        "#1003F#2P这、这个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xD,
        (
            "#895F#2P如果没有，我们\x01",
            "也不可能袖手旁观。\x02\x03",

            "蒸气坦克装载的\x01",
            "是火药式的大炮。\x02\x03",

            "要攻陷那个浮游都市，\x01",
            "你不认为正合适吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x101,
        (
            "#1020F#2P开、开玩笑吧！？\x02\x03",

            "大炮什么的怎么可能\x01",
            "打下那个巨大的城市！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xD,
        (
            "#896F#2P呵呵……\x01",
            "不试试看怎么知道。\x02\x03",

            "#894F无论如何……\x01",
            "现在有一件事可以确定。\x02\x03",

            "#897F就是你们\x01",
            "并没有拒绝我们善意行动\x01",
            "的理由和实力。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x101,
        "#1003F#2P可恶……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xC,
        (
            "#1162F#5P……………………………\x02\x03",

            "#1167F那么……\x01",
            "只要能证明就可以了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xD,
        "#898F#2P噢……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xC,
        (
            "#1162F#5P只要我们\x01",
            "能够证明可以独立查明那个\x01",
            "浮游都市的可能性……\x02\x03",

            "在时间上就可以给我们\x01",
            "一些宽限吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xD,
        (
            "#899F#2P唔，这个嘛……\x02\x03",

            "#895F虽然只是暂时的，\x01",
            "但也不得不如此了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(-990, 20, 95740, 0)
    OP_67(0, 4580, -10000, 0)
    OP_6B(3350, 0)
    OP_6C(44000, 0)
    OP_6E(299, 0)
    SetChrPos(0xD, -1930, 50, 94710, 180)
    SetChrPos(0x10, -1500, 20, 97080, 180)
    SetChrPos(0xE, -3070, -20, 96930, 180)
    OP_0D()
    OP_62(0xE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #117
        0xE,
        "#883F#5P（皇、皇子……！？）\x02",
    )

    CloseMessageWindow()
    OP_8C(0xD, 270, 400)
    Sleep(300)

    ChrTalk(    #118
        0xD,
        (
            "#896F#2P（镇定，中将。）\x02\x03",

            "（面对缔结了互不侵犯条约的对方，\x01",
            "　这是必要的礼仪吧。）\x02\x03",

            "（而且要他们能够证明才行。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xE,
        "#884F#5P（……是。）\x02",
    )

    CloseMessageWindow()
    OP_8C(0xD, 180, 400)
    Sleep(500)

    ChrTalk(    #120
        0xD,
        (
            "#899F#5P那么……\x02\x03",

            "#895F只要你们能够拿出王国拥有独力查明这个问题\x01",
            "的可能性，我便保证暂时撤退。\x02\x03",

            "以『黄金之军马』徽章，\x01",
            "以及我身为皇族的名誉为担保。\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("男性的声音")

    AnonymousTalk(    #121
        "\x07\x05这份宣言，我收下了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_62(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x27, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x28, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Fade(500)
    OP_6D(390, -20, 49480, 0)
    OP_67(0, 4550, -10000, 0)
    OP_6B(3600, 0)
    OP_6C(135000, 0)
    OP_6E(304, 0)
    SetChrPos(0x102, 360, 80, 47660, 0)
    SetChrPos(0x8, -1530, 20, 46400, 0)
    SetChrPos(0xA, 610, -30, 46380, 0)
    SetChrPos(0x9, 1350, 50, 45360, 0)
    SetChrPos(0xB, 0, 80, 44800, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #122
        0x101,
        "#1004F#5P刚、刚才的声音是……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x8,
        "#023F#2P难不成……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xB,
        "#070F#2P啊啊……不会错的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x9,
        "#055F#5P喂喂，真的假的！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x102,
        "#1044F#5P……父亲。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_23(0x10F)
    OP_A2(0x10FF)
    OP_A2(0x10FB)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_FBD end

    def Function_3_67F8(): pass

    label("Function_3_67F8")

    SetChrPos(0xC, -1360, 30, 43020, 0)
    OP_8E(0xFE, 0xFFFFFE0C, 0x32, 0xC0B2, 0x7D0, 0x0)
    OP_8E(0xFE, 0x0, 0x14, 0xCF62, 0x7D0, 0x0)
    Return()

    # Function_3_67F8 end

    def Function_4_6832(): pass

    label("Function_4_6832")

    SetChrPos(0x101, -1300, 40, 40490, 0)
    OP_8E(0xFE, 0xFFFFFAEC, 0x50, 0xBAFE, 0x7D0, 0x0)
    Return()

    # Function_4_6832 end

    def Function_5_6858(): pass

    label("Function_5_6858")

    SetChrPos(0x102, 360, 20, 41150, 0)
    OP_8E(0xFE, 0x168, 0x50, 0xBA2C, 0x7D0, 0x0)
    Return()

    # Function_5_6858 end

    def Function_6_687E(): pass

    label("Function_6_687E")

    SetChrPos(0x8, -1530, -20, 38220, 0)
    OP_8E(0xFE, 0xFFFFFA06, 0x14, 0xB540, 0x7D0, 0x0)
    Return()

    # Function_6_687E end

    def Function_7_68A4(): pass

    label("Function_7_68A4")

    SetChrPos(0xA, 610, 20, 39320, 0)
    OP_8E(0xFE, 0x262, 0xFFFFFFE2, 0xB52C, 0x7D0, 0x0)
    Return()

    # Function_7_68A4 end

    def Function_8_68CA(): pass

    label("Function_8_68CA")

    SetChrPos(0x9, 1350, 20, 37510, 0)
    OP_8E(0xFE, 0x546, 0x32, 0xB130, 0x7D0, 0x0)
    Return()

    # Function_8_68CA end

    def Function_9_68F0(): pass

    label("Function_9_68F0")

    SetChrPos(0xB, 0, 30, 35900, 0)
    OP_8E(0xFE, 0x0, 0x50, 0xAF00, 0x7D0, 0x0)
    Return()

    # Function_9_68F0 end

    def Function_10_6916(): pass

    label("Function_10_6916")

    OP_8C(0xFE, 270, 400)
    OP_8F(0xFE, 0x640, 0xFFFFFFEC, 0xC5A8, 0x7D0, 0x0)
    Return()

    # Function_10_6916 end

    def Function_11_6932(): pass

    label("Function_11_6932")

    Sleep(100)
    OP_8C(0xFE, 90, 400)
    OP_8F(0xFE, 0xFFFFF2D6, 0x1E, 0xC5C6, 0x7D0, 0x0)
    Return()

    # Function_11_6932 end

    def Function_12_6953(): pass

    label("Function_12_6953")

    OP_8C(0xFE, 90, 400)
    OP_8F(0xFE, 0xFFFFF0C4, 0x14, 0x18010, 0x7D0, 0x0)
    Return()

    # Function_12_6953 end

    def Function_13_696F(): pass

    label("Function_13_696F")

    Sleep(100)
    OP_8C(0xFE, 270, 400)
    OP_8F(0xFE, 0x28, 0xA, 0x17F5C, 0x7D0, 0x0)
    Return()

    # Function_13_696F end

    def Function_14_6990(): pass

    label("Function_14_6990")


    def lambda_6996():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_6996)
    Sleep(170)

    def lambda_69B6():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_69B6)

    def lambda_69D1():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_69D1)
    Sleep(200)

    def lambda_69F1():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_69F1)

    def lambda_6A0C():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_6A0C)
    Sleep(160)

    def lambda_6A2C():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_6A2C)

    def lambda_6A47():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_6A47)
    Sleep(230)

    def lambda_6A67():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_6A67)

    def lambda_6A82():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_6A82)
    Sleep(150)

    def lambda_6AA2():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_6AA2)

    def lambda_6ABD():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_6ABD)
    Sleep(180)

    def lambda_6ADD():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_6ADD)

    def lambda_6AF8():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_6AF8)
    Sleep(150)

    def lambda_6B18():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_6B18)
    WaitChrThread(0x17, 0x1)
    OP_72(0x3, 0x20)
    WaitChrThread(0x18, 0x1)
    OP_72(0x4, 0x20)
    WaitChrThread(0x1B, 0x1)
    OP_72(0x5, 0x20)
    WaitChrThread(0x1C, 0x1)
    OP_72(0x6, 0x20)
    WaitChrThread(0x19, 0x1)
    OP_72(0x7, 0x20)
    WaitChrThread(0x1A, 0x1)
    OP_72(0x8, 0x20)
    WaitChrThread(0x1D, 0x1)
    OP_72(0x9, 0x20)
    WaitChrThread(0x1E, 0x1)
    OP_72(0xA, 0x20)
    WaitChrThread(0x1F, 0x1)
    OP_72(0xB, 0x20)
    WaitChrThread(0x20, 0x1)
    OP_72(0xC, 0x20)
    WaitChrThread(0x23, 0x1)
    OP_72(0xD, 0x20)
    WaitChrThread(0x24, 0x1)
    OP_72(0xE, 0x20)
    WaitChrThread(0x21, 0x1)
    OP_72(0xF, 0x20)
    WaitChrThread(0x22, 0x1)
    OP_72(0x10, 0x20)
    OP_23(0x10F)
    OP_23(0x110)
    Return()

    # Function_14_6990 end

    def Function_15_6BC0(): pass

    label("Function_15_6BC0")


    def lambda_6BC6():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_6BC6)
    Sleep(80)

    def lambda_6BE6():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_6BE6)

    def lambda_6C01():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_6C01)
    Sleep(50)

    def lambda_6C21():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_6C21)
    Sleep(100)

    def lambda_6C41():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_6C41)

    def lambda_6C5C():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_6C5C)
    Sleep(50)

    def lambda_6C7C():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_6C7C)
    Sleep(40)

    def lambda_6C9C():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x31, 1, lambda_6C9C)

    def lambda_6CB7():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2F, 1, lambda_6CB7)
    Sleep(70)

    def lambda_6CD7():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x30, 1, lambda_6CD7)

    def lambda_6CF2():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_6CF2)
    Sleep(80)

    def lambda_6D12():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x32, 1, lambda_6D12)

    def lambda_6D2D():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_6D2D)
    Sleep(60)

    def lambda_6D4D():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x37, 1, lambda_6D4D)

    def lambda_6D68():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x34, 1, lambda_6D68)
    Sleep(80)

    def lambda_6D88():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x36, 1, lambda_6D88)

    def lambda_6DA3():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x38, 1, lambda_6DA3)
    Sleep(100)

    def lambda_6DC3():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x35, 1, lambda_6DC3)
    Sleep(30)

    def lambda_6DE3():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x3E, 1, lambda_6DE3)

    def lambda_6DFE():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x3A, 1, lambda_6DFE)
    Sleep(80)

    def lambda_6E1E():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x3C, 1, lambda_6E1E)

    def lambda_6E39():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_6E39)
    Sleep(90)

    def lambda_6E59():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x3B, 1, lambda_6E59)

    def lambda_6E74():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x3D, 1, lambda_6E74)
    Sleep(100)

    def lambda_6E94():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x42, 1, lambda_6E94)

    def lambda_6EAF():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x3F, 1, lambda_6EAF)
    Sleep(30)

    def lambda_6ECF():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x40, 1, lambda_6ECF)

    def lambda_6EEA():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x43, 1, lambda_6EEA)
    Sleep(60)

    def lambda_6F0A():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x41, 1, lambda_6F0A)

    def lambda_6F25():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x44, 1, lambda_6F25)
    Return()

    # Function_15_6BC0 end

    def Function_16_6F3B(): pass

    label("Function_16_6F3B")


    def lambda_6F41():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x46, 1, lambda_6F41)
    Sleep(80)

    def lambda_6F61():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x47, 1, lambda_6F61)

    def lambda_6F7C():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x49, 1, lambda_6F7C)
    Sleep(50)

    def lambda_6F9C():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x48, 1, lambda_6F9C)
    Sleep(100)

    def lambda_6FBC():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x45, 1, lambda_6FBC)

    def lambda_6FD7():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x4A, 1, lambda_6FD7)
    Sleep(50)

    def lambda_6FF7():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x4B, 1, lambda_6FF7)
    Sleep(40)

    def lambda_7017():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x4F, 1, lambda_7017)

    def lambda_7032():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x4D, 1, lambda_7032)
    Sleep(70)

    def lambda_7052():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x4E, 1, lambda_7052)

    def lambda_706D():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x4C, 1, lambda_706D)
    Sleep(80)

    def lambda_708D():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x50, 1, lambda_708D)

    def lambda_70A8():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x51, 1, lambda_70A8)
    Sleep(60)

    def lambda_70C8():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x55, 1, lambda_70C8)

    def lambda_70E3():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x52, 1, lambda_70E3)
    Sleep(80)

    def lambda_7103():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x54, 1, lambda_7103)

    def lambda_711E():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x56, 1, lambda_711E)
    Sleep(100)

    def lambda_713E():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x53, 1, lambda_713E)
    Sleep(30)

    def lambda_715E():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x5C, 1, lambda_715E)

    def lambda_7179():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x58, 1, lambda_7179)
    Sleep(80)

    def lambda_7199():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x5A, 1, lambda_7199)

    def lambda_71B4():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x57, 1, lambda_71B4)
    Sleep(90)

    def lambda_71D4():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x59, 1, lambda_71D4)

    def lambda_71EF():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x5B, 1, lambda_71EF)
    Sleep(100)

    def lambda_720F():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x60, 1, lambda_720F)

    def lambda_722A():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x5D, 1, lambda_722A)
    Sleep(30)

    def lambda_724A():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x5E, 1, lambda_724A)

    def lambda_7265():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x61, 1, lambda_7265)
    Sleep(60)

    def lambda_7285():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x5F, 1, lambda_7285)

    def lambda_72A0():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x62, 1, lambda_72A0)
    Return()

    # Function_16_6F3B end

    def Function_17_72B6(): pass

    label("Function_17_72B6")

    Sleep(80)

    def lambda_72C1():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x65, 1, lambda_72C1)

    def lambda_72DC():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x67, 1, lambda_72DC)
    Sleep(50)

    def lambda_72FC():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x66, 1, lambda_72FC)
    Sleep(100)

    def lambda_731C():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x68, 1, lambda_731C)
    Sleep(50)
    Sleep(40)

    def lambda_7341():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x6D, 1, lambda_7341)

    def lambda_735C():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x6B, 1, lambda_735C)
    Sleep(70)

    def lambda_737C():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x6C, 1, lambda_737C)
    Sleep(80)

    def lambda_739C():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x6E, 1, lambda_739C)
    Sleep(60)

    def lambda_73BC():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x73, 1, lambda_73BC)
    Sleep(80)

    def lambda_73DC():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x72, 1, lambda_73DC)

    def lambda_73F7():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x74, 1, lambda_73F7)
    Sleep(100)

    def lambda_7417():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x71, 1, lambda_7417)
    Sleep(30)

    def lambda_7437():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x7A, 1, lambda_7437)
    Sleep(80)

    def lambda_7457():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x78, 1, lambda_7457)
    Sleep(90)

    def lambda_7477():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x77, 1, lambda_7477)

    def lambda_7492():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x79, 1, lambda_7492)
    Sleep(100)

    def lambda_74B2():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x7C, 1, lambda_74B2)
    Sleep(30)

    def lambda_74D2():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x7D, 1, lambda_74D2)
    Sleep(60)

    def lambda_74F2():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x7B, 1, lambda_74F2)

    def lambda_750D():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x7E, 1, lambda_750D)
    Return()

    # Function_17_72B6 end

    def Function_18_7523(): pass

    label("Function_18_7523")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_A1(0x17, 0x3)
    OP_A1(0x18, 0x4)
    OP_A1(0x19, 0x5)
    OP_A1(0x1A, 0x6)
    OP_A1(0x1B, 0x7)
    OP_A1(0x1C, 0x8)
    OP_A1(0x1D, 0x9)
    OP_A1(0x1E, 0xA)
    OP_A1(0x1F, 0xB)
    OP_A1(0x20, 0xC)
    OP_A1(0x21, 0xD)
    OP_A1(0x22, 0xE)
    OP_A1(0x23, 0xF)
    OP_A1(0x24, 0x10)
    OP_72(0x3, 0x20)
    OP_72(0x4, 0x20)
    OP_72(0x5, 0x20)
    OP_72(0x6, 0x20)
    OP_72(0x7, 0x20)
    OP_72(0x8, 0x20)
    OP_72(0x9, 0x20)
    OP_72(0xA, 0x20)
    OP_72(0xB, 0x20)
    OP_72(0xC, 0x20)
    OP_72(0xD, 0x20)
    OP_72(0xE, 0x20)
    OP_72(0xF, 0x20)
    OP_72(0x10, 0x20)
    OP_D2(0x70020, 0x70028, 0x0)
    OP_D2(0x70050, 0x70058, 0x1)
    OP_D2(0x70060, 0x70068, 0x2)
    OP_D2(0x70070, 0x70078, 0x3)
    OP_D2(0x270398, 0x27039C, 0x4)
    OP_D2(0x2701E7, 0x2701EC, 0x5)
    OP_D2(0x2701EE, 0x2701F3, 0x6)
    OP_D2(0x70150, 0x70154, 0x7)
    OP_D2(0x2701D2, 0x2701D7, 0x8)
    OP_D2(0x270202, 0x270207, 0x9)
    OP_D2(0x70120, 0x70124, 0xA)
    OP_D2(0x2701E6, 0x2701EB, 0xB)
    OP_D2(0x60108, 0x6010D, 0xC)
    OP_D2(0x2701D3, 0x2701D8, 0xD)
    OP_D2(0x70142, 0x70146, 0xE)
    OP_D2(0x270080, 0x270084, 0xF)
    OP_D2(0x26023D, 0x260242, 0x10)
    OP_D2(0x270399, 0x27039D, 0x11)
    OP_D2(0x70021, 0x70029, 0x12)
    OP_D2(0x70051, 0x70059, 0x13)
    OP_D2(0x70061, 0x70069, 0x14)
    OP_D2(0x70071, 0x70079, 0x15)
    OP_72(0x1, 0x10)
    OP_6F(0x1, 560)
    SetChrChipByIndex(0x8, 0)
    SetChrChipByIndex(0x9, 1)
    SetChrChipByIndex(0xA, 2)
    SetChrChipByIndex(0xB, 3)
    SetChrChipByIndex(0xC, 4)
    SetChrChipByIndex(0xD, 5)
    SetChrChipByIndex(0xE, 6)
    SetChrChipByIndex(0xF, 7)
    SetChrChipByIndex(0x10, 8)
    SetChrChipByIndex(0x27, 9)
    SetChrChipByIndex(0x28, 9)
    SetChrChipByIndex(0x29, 9)
    SetChrChipByIndex(0x2A, 9)
    SetChrChipByIndex(0x2B, 9)
    SetChrChipByIndex(0x2C, 9)
    SetChrChipByIndex(0x2D, 9)
    SetChrChipByIndex(0x2E, 9)
    SetChrChipByIndex(0x2F, 9)
    SetChrChipByIndex(0x30, 9)
    SetChrChipByIndex(0x31, 9)
    SetChrChipByIndex(0x32, 9)
    SetChrChipByIndex(0x33, 9)
    SetChrChipByIndex(0x34, 9)
    SetChrChipByIndex(0x35, 9)
    SetChrChipByIndex(0x36, 9)
    SetChrChipByIndex(0x37, 9)
    SetChrChipByIndex(0x38, 9)
    SetChrChipByIndex(0x39, 9)
    SetChrChipByIndex(0x3A, 9)
    SetChrChipByIndex(0x3B, 9)
    SetChrChipByIndex(0x3C, 9)
    SetChrChipByIndex(0x3D, 9)
    SetChrChipByIndex(0x3E, 9)
    SetChrChipByIndex(0x3F, 9)
    SetChrChipByIndex(0x40, 9)
    SetChrChipByIndex(0x41, 9)
    SetChrChipByIndex(0x42, 9)
    SetChrChipByIndex(0x43, 9)
    SetChrChipByIndex(0x44, 9)
    SetChrChipByIndex(0x45, 9)
    SetChrChipByIndex(0x46, 9)
    SetChrChipByIndex(0x47, 9)
    SetChrChipByIndex(0x48, 9)
    SetChrChipByIndex(0x49, 9)
    SetChrChipByIndex(0x4A, 9)
    SetChrChipByIndex(0x4B, 9)
    SetChrChipByIndex(0x4C, 9)
    SetChrChipByIndex(0x4D, 9)
    SetChrChipByIndex(0x4E, 9)
    SetChrChipByIndex(0x4F, 9)
    SetChrChipByIndex(0x50, 9)
    SetChrChipByIndex(0x51, 9)
    SetChrChipByIndex(0x52, 9)
    SetChrChipByIndex(0x53, 9)
    SetChrChipByIndex(0x54, 9)
    SetChrChipByIndex(0x55, 9)
    SetChrChipByIndex(0x56, 9)
    SetChrChipByIndex(0x57, 9)
    SetChrChipByIndex(0x58, 9)
    SetChrChipByIndex(0x59, 9)
    SetChrChipByIndex(0x5A, 9)
    SetChrChipByIndex(0x5B, 9)
    SetChrChipByIndex(0x5C, 9)
    SetChrChipByIndex(0x5D, 9)
    SetChrChipByIndex(0x5E, 9)
    SetChrChipByIndex(0x5F, 9)
    SetChrChipByIndex(0x60, 9)
    SetChrChipByIndex(0x61, 9)
    SetChrChipByIndex(0x62, 9)
    SetChrChipByIndex(0x63, 9)
    SetChrChipByIndex(0x64, 9)
    SetChrChipByIndex(0x65, 9)
    SetChrChipByIndex(0x66, 9)
    SetChrChipByIndex(0x67, 9)
    SetChrChipByIndex(0x68, 9)
    SetChrChipByIndex(0x69, 9)
    SetChrChipByIndex(0x6A, 9)
    SetChrChipByIndex(0x6B, 9)
    SetChrChipByIndex(0x6C, 9)
    SetChrChipByIndex(0x6D, 9)
    SetChrChipByIndex(0x6E, 9)
    SetChrChipByIndex(0x6F, 9)
    SetChrChipByIndex(0x70, 9)
    SetChrChipByIndex(0x71, 9)
    SetChrChipByIndex(0x72, 9)
    SetChrChipByIndex(0x73, 9)
    SetChrChipByIndex(0x74, 9)
    SetChrChipByIndex(0x75, 9)
    SetChrChipByIndex(0x76, 9)
    SetChrChipByIndex(0x77, 9)
    SetChrChipByIndex(0x78, 9)
    SetChrChipByIndex(0x79, 9)
    SetChrChipByIndex(0x7A, 9)
    SetChrChipByIndex(0x7B, 9)
    SetChrChipByIndex(0x7C, 9)
    SetChrChipByIndex(0x7D, 9)
    SetChrChipByIndex(0x7E, 9)
    SetChrChipByIndex(0x15, 10)
    SetChrChipByIndex(0x16, 10)
    SetChrChipByIndex(0x11, 11)
    SetChrPos(0x17, -7460, 0, 104890, 0)
    SetChrPos(0x18, 3360, 0, 104630, 0)
    SetChrPos(0x19, -7650, 0, 119070, 0)
    SetChrPos(0x1A, 3510, 0, 119050, 0)
    SetChrPos(0x1B, -18530, 0, 108310, 0)
    SetChrPos(0x1C, 15560, 0, 109270, 0)
    SetChrPos(0x1D, -19230, 0, 123310, 0)
    SetChrPos(0x1E, 14300, 0, 123350, 0)
    SetChrPos(0x1F, -8090, 0, 133010, 0)
    SetChrPos(0x20, 3690, 0, 132830, 0)
    SetChrPos(0x21, 2670, 0, 149120, 0)
    SetChrPos(0x22, -8410, 0, 149060, 0)
    SetChrPos(0x23, -19940, 0, 140900, 0)
    SetChrPos(0x24, 12450, 0, 140010, 0)
    SetChrPos(0x27, -7630, 0, 157450, 180)
    SetChrPos(0x28, -5660, -50, 157450, 180)
    SetChrPos(0x29, -3630, 0, 157450, 180)
    SetChrPos(0x2A, -1730, 90, 157450, 180)
    SetChrPos(0x2B, 230, -30, 157450, 180)
    SetChrPos(0x2C, 2070, -30, 157450, 180)
    SetChrPos(0x2D, -7630, 40, 159600, 180)
    SetChrPos(0x2E, -5660, 20, 159600, 180)
    SetChrPos(0x2F, -3630, -20, 159600, 180)
    SetChrPos(0x30, -1730, 50, 159600, 180)
    SetChrPos(0x31, 230, -20, 159600, 180)
    SetChrPos(0x32, 2070, -50, 159600, 180)
    SetChrPos(0x33, -7630, 30, 161750, 180)
    SetChrPos(0x34, -5660, 10, 161750, 180)
    SetChrPos(0x35, -3630, 20, 161750, 180)
    SetChrPos(0x36, -1730, 70, 161750, 180)
    SetChrPos(0x37, 230, -10, 161750, 180)
    SetChrPos(0x38, 2070, -30, 161750, 180)
    SetChrPos(0x39, -7630, -20, 163900, 180)
    SetChrPos(0x3A, -5660, -40, 163900, 180)
    SetChrPos(0x3B, -3630, -40, 163900, 180)
    SetChrPos(0x3C, -1730, 40, 163900, 180)
    SetChrPos(0x3D, 230, -40, 163900, 180)
    SetChrPos(0x3E, 2070, -20, 163900, 180)
    SetChrPos(0x3F, -7630, -40, 166050, 180)
    SetChrPos(0x40, -5660, 0, 166050, 180)
    SetChrPos(0x41, -3630, 30, 166050, 180)
    SetChrPos(0x42, -1730, 60, 166050, 180)
    SetChrPos(0x43, 230, 10, 166050, 180)
    SetChrPos(0x44, 2070, -20, 166050, 180)
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
    SetChrFlags(0x27, 0x200)
    SetChrFlags(0x28, 0x200)
    SetChrFlags(0x29, 0x200)
    SetChrFlags(0x2A, 0x200)
    SetChrFlags(0x2B, 0x200)
    SetChrFlags(0x2C, 0x200)
    SetChrFlags(0x2D, 0x200)
    SetChrFlags(0x2E, 0x200)
    SetChrFlags(0x2F, 0x200)
    SetChrFlags(0x30, 0x200)
    SetChrFlags(0x31, 0x200)
    SetChrFlags(0x32, 0x200)
    SetChrFlags(0x33, 0x200)
    SetChrFlags(0x34, 0x200)
    SetChrFlags(0x35, 0x200)
    SetChrFlags(0x36, 0x200)
    SetChrFlags(0x37, 0x200)
    SetChrFlags(0x38, 0x200)
    SetChrFlags(0x39, 0x200)
    SetChrFlags(0x3A, 0x200)
    SetChrFlags(0x3B, 0x200)
    SetChrFlags(0x3C, 0x200)
    SetChrFlags(0x3D, 0x200)
    SetChrFlags(0x3E, 0x200)
    SetChrFlags(0x3F, 0x200)
    SetChrFlags(0x40, 0x200)
    SetChrFlags(0x41, 0x200)
    SetChrFlags(0x42, 0x200)
    SetChrFlags(0x43, 0x200)
    SetChrFlags(0x44, 0x200)
    SetChrFlags(0x45, 0x200)
    SetChrFlags(0x46, 0x200)
    SetChrFlags(0x47, 0x200)
    SetChrFlags(0x48, 0x200)
    SetChrFlags(0x49, 0x200)
    SetChrFlags(0x4A, 0x200)
    SetChrFlags(0x4B, 0x200)
    SetChrFlags(0x4C, 0x200)
    SetChrFlags(0x4D, 0x200)
    SetChrFlags(0x4E, 0x200)
    SetChrFlags(0x4F, 0x200)
    SetChrFlags(0x50, 0x200)
    SetChrFlags(0x51, 0x200)
    SetChrFlags(0x52, 0x200)
    SetChrFlags(0x53, 0x200)
    SetChrFlags(0x54, 0x200)
    SetChrFlags(0x55, 0x200)
    SetChrFlags(0x56, 0x200)
    SetChrFlags(0x57, 0x200)
    SetChrFlags(0x58, 0x200)
    SetChrFlags(0x59, 0x200)
    SetChrFlags(0x5A, 0x200)
    SetChrFlags(0x5B, 0x200)
    SetChrFlags(0x5C, 0x200)
    SetChrFlags(0x5D, 0x200)
    SetChrFlags(0x5E, 0x200)
    SetChrFlags(0x5F, 0x200)
    SetChrFlags(0x60, 0x200)
    SetChrFlags(0x61, 0x200)
    SetChrFlags(0x62, 0x200)
    SetChrFlags(0x63, 0x200)
    SetChrFlags(0x64, 0x200)
    SetChrFlags(0x65, 0x200)
    SetChrFlags(0x66, 0x200)
    SetChrFlags(0x67, 0x200)
    SetChrFlags(0x68, 0x200)
    SetChrFlags(0x69, 0x200)
    SetChrFlags(0x6A, 0x200)
    SetChrFlags(0x6B, 0x200)
    SetChrFlags(0x6C, 0x200)
    SetChrFlags(0x6D, 0x200)
    SetChrFlags(0x6E, 0x200)
    SetChrFlags(0x6F, 0x200)
    SetChrFlags(0x70, 0x200)
    SetChrFlags(0x71, 0x200)
    SetChrFlags(0x72, 0x200)
    SetChrFlags(0x73, 0x200)
    SetChrFlags(0x74, 0x200)
    SetChrFlags(0x75, 0x200)
    SetChrFlags(0x76, 0x200)
    SetChrFlags(0x77, 0x200)
    SetChrFlags(0x78, 0x200)
    SetChrFlags(0x79, 0x200)
    SetChrFlags(0x7A, 0x200)
    SetChrFlags(0x7B, 0x200)
    SetChrFlags(0x7C, 0x200)
    SetChrFlags(0x7D, 0x200)
    SetChrFlags(0x7E, 0x200)
    SetChrPos(0x15, 1600, -20, 50600, 315)
    SetChrPos(0x16, -3370, 30, 50630, 315)
    SetChrPos(0xF, -1440, 40, 53120, 315)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0x101, -2540, 40, 55190, 270)
    SetChrPos(0x102, 360, 80, 47660, 315)
    SetChrPos(0x8, -1530, 20, 46400, 315)
    SetChrPos(0x9, 1350, 50, 45360, 315)
    SetChrPos(0xB, 0, 80, 44800, 315)
    SetChrPos(0xA, 610, -30, 46380, 315)
    SetChrPos(0xC, -810, 10, 55140, 270)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xE, -3380, -40, 95890, 270)
    SetChrPos(0xD, -1930, 50, 94710, 270)
    SetChrPos(0x10, -1500, 20, 97080, 270)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x27, -3900, 20, 98320, 270)
    SetChrPos(0x28, 40, 10, 98140, 270)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x28, 0x80)
    OP_71(0x2, 0x20)
    OP_6F(0x2, 330)
    OP_70(0x2, 0x1AE)
    OP_A1(0x25, 0x2)
    SetChrPos(0x25, -38270, 26200, 57080, 30)
    OP_A1(0x26, 0x11)
    SetChrPos(0x26, -38270, 5000, 57080, 30)
    OP_75(0x11, 0x0, 0x0)
    OP_74(0x11, 0x0, 0x7)
    LoadEffect(0x0, "map\\\\mp021_00.eff")
    LoadEffect(0x1, "map\\\\onsen00.eff")
    OP_48()
    OP_89(0x11, -29500, 28800, 67950, 90)
    SetChrFlags(0x11, 0x4)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x20)
    SetChrFlags(0x11, 0x40)
    SetChrBattleFlags(0x11, 0x20)
    OP_48()
    ClearChrFlags(0x11, 0x4)
    OP_22(0x125, 0x1, 0x50)
    ClearMapFlags(0x100000)
    OP_6D(-36460, 10220, 60860, 0)
    OP_67(0, 15110, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(132000, 0)
    OP_6E(500, 0)
    FadeToBright(1000, 0)
    OP_43(0x25, 0x0, 0x0, 0x14)
    OP_43(0x26, 0x0, 0x0, 0x15)

    def lambda_8030():
        OP_6D(-35940, -30, 58750, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8030)

    def lambda_8048():
        OP_67(0, 6930, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8048)

    def lambda_8060():
        OP_6B(5550, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_8060)

    def lambda_8070():
        OP_6C(227000, 6000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8070)

    def lambda_8080():
        OP_6E(675, 6000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8080)
    StopSound(0x9C40, 0x2A23A, 0x1388)

    def lambda_809D():
        OP_8F(0xFE, 0xFFFF6A82, 0xC8, 0xDEF8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_809D)

    def lambda_80B8():
        OP_8F(0xFE, 0xFFFF6A82, 0x1450, 0xDEF8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_80B8)

    def lambda_80D3():
        OP_8F(0xFE, 0xFFFF8D78, 0x1DB0, 0x10A5E, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_80D3)
    Sleep(1500)

    def lambda_80F3():
        OP_8F(0xFE, 0xFFFF6A82, 0x1450, 0xDEF8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_80F3)
    PlayEffect(0x0, 0x0, 0xFF, -39070, -150, 58410, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_22(0xCC, 0x0, 0x64)
    Sleep(2000)

    def lambda_814D():
        OP_8F(0xFE, 0xFFFF6A82, 0x1450, 0xDEF8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_814D)
    WaitChrThread(0x25, 0x1)
    WaitChrThread(0x25, 0x0)
    OP_82(0x0, 0x2)
    OP_23(0xCC)
    OP_23(0x125)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    WaitChrThread(0x101, 0x1)
    Fade(1000)
    OP_48()
    OP_89(0x11, -29320, 7600, 68190, 90)
    ClearChrFlags(0x11, 0x4)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x20)
    SetChrFlags(0x11, 0x40)
    SetChrBattleFlags(0x11, 0x20)
    OP_6D(-29380, 7600, 68010, 0)
    OP_67(0, 6340, -10000, 0)
    OP_6B(1890, 0)
    OP_6C(255000, 0)
    OP_6E(474, 0)
    OP_11(0xA0, 0xB4, 0xFF, 0x9C40, 0x245C1, 0x0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #127
        0x11,
        (
            "#1125F#5P这就是此时此刻\x01",
            "我们能证明给你们看的东西。\x02\x03",

            "#1120F请随意观赏。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x101,
        "#1008F老爸……！\x02",
    )

    CloseMessageWindow()
    SetChrPos(0xE, -17920, -260, 72900, 180)
    SetChrPos(0xD, -17700, -290, 72030, 180)

    ChrTalk(    #129
        0xE,
        "#883F#5P卡、卡西乌斯·布莱特！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x11,
        (
            "#1120F#5P赛克斯少将，好久不见了。\x02\x03",

            "#1124F噢～……现在是中将了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xE,
        (
            "#886F#5P少说废话！\x02\x03",

            "#885F为、为什么你会来这里……\x01",
            "还有，那艘船是怎么回事！？\x02\x03",

            "在这样的状况下\x01",
            "怎么还能飞上天空的！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x11,
        (
            "#1125F#5P抱歉，我只能说这是\x01",
            "国家机密吧。\x02\x03",

            "#1122F就像贵国为何\x01",
            "留存有蒸气坦克一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xE,
        "#886F#5P可恶……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xD,
        (
            "#892F#5P唔……\x01",
            "这就是传说中的『埃尔赛尤』吗。\x02\x03",

            "而您就是那位有名的\x01",
            "卡西乌斯·布莱特准将吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x11,
        (
            "#1125F#5P幸会，殿下。\x02\x03",

            "#1120F虽然感觉似乎\x01",
            "曾经在哪里见过面……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xD,
        (
            "#894F#5P真是奇遇啊，准将。\x02\x03",

            "#890F我竟然也有\x01",
            "同感呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x11,
        "#1124F#5P那可真是巧啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xD,
        "#894F#5P说得没错……\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #139
        0xD,
        "#891F#5P哈哈哈哈哈。\x02",
    )


    ChrTalk(    #140
        0x11,
        "#1121F#5P哈哈哈哈哈。\x02",
    )

    OP_56(0x1)
    OP_59()

    ChrTalk(    #141
        0xE,
        "#885F#5P#4S皇、皇子！\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(-950, 40, 92660, 0)
    OP_67(0, 4310, -10000, 0)
    OP_6B(2060, 0)
    OP_6C(147000, 0)
    OP_6E(495, 0)
    SetChrPos(0xE, -3380, -40, 95890, 135)
    SetChrPos(0xD, -1930, 50, 94710, 270)

    def lambda_85C6():
        OP_8C(0xFE, 180, 0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_85C6)

    def lambda_85D4():
        OP_8C(0xFE, 180, 0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_85D4)

    def lambda_85E2():
        OP_8C(0xFE, 180, 0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_85E2)
    OP_8C(0xD, 180, 0)

    def lambda_85F7():
        OP_8C(0xFE, 180, 0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_85F7)
    OP_0D()
    Sleep(500)

    ChrTalk(    #142
        0xD,
        (
            "#890F#5P科洛蒂娅公主、艾丝蒂尔。\x02\x03",

            "我是高贵的埃雷波尼亚皇族。\x01",
            "之前的约定我会遵守的。\x02\x03",

            "我立即命令这附近的\x01",
            "帝国军部队全部撤退。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_868D():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_868D)

    def lambda_869B():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_869B)

    ChrTalk(    #143
        0x101,
        "#1017F#3P奥利维尔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xC,
        "#1168F#3P……非常感谢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xD,
        (
            "#894F#5P不过……\x02\x03",

            "仅仅展示了可能性，\x01",
            "我帝国的国民自然是无法认同的。\x02\x03",

            "#892F现在就让我亲自\x01",
            "乘上埃尔赛尤\x01",
            "视察一番如何呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0xE, 0xD, 400)

    ChrTalk(    #146
        0xE,
        "#883F#6P皇、皇子！？\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(-940, 0, 52290, 0)
    OP_67(0, 4550, -10000, 0)
    OP_6B(3410, 0)
    OP_6C(171000, 0)
    OP_6E(304, 0)
    SetChrPos(0x15, 1600, -20, 50600, 0)
    SetChrPos(0x16, -3370, 30, 50630, 0)
    SetChrPos(0xF, -1440, 40, 53120, 0)
    SetChrPos(0x101, -2540, 40, 55190, 0)
    SetChrPos(0x102, -500, 80, 47660, 0)
    SetChrPos(0x8, -1530, 20, 46400, 0)
    SetChrPos(0x9, 1350, 50, 45360, 0)
    SetChrPos(0xB, 0, 80, 44800, 0)
    SetChrPos(0xA, 610, -30, 46380, 0)
    SetChrPos(0xC, -810, 10, 55140, 0)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0x11, -12350, -70, 82680, 90)
    OP_0D()
    Sleep(500)

    ChrTalk(    #147
        0x11,
        (
            "#1125F#5P唔，皇子亲自视察的话\x01",
            "帝国政府应该就能接受了吧。\x02\x03",

            "#1120F如何呢，科洛蒂娅殿下？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xC,
        (
            "#1167F#5P当然，正合我意。\x02\x03",

            "利贝尔与埃雷波尼亚的友情\x01",
            "联结也将更加牢固吧。\x02\x03",

            "#1168F欢迎您。\x01",
            "奥利维特皇子殿下。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_6D(-1440, 30, 143110, 0)
    OP_67(0, 6820, -10000, 0)
    OP_6B(2120, 0)
    OP_6C(45000, 0)
    OP_6E(488, 0)
    SetChrPos(0xE, -2070, 40, 143810, 180)
    SetChrPos(0xD, -2510, 30, 141080, 0)
    SetChrPos(0x10, -1780, 50, 140180, 0)
    SetChrPos(0x27, -7630, 0, 157450, 180)
    SetChrPos(0x28, -5660, -50, 157450, 180)
    SetChrPos(0x11, -29320, 7500, 68190, 90)
    SetChrSubChip(0xE, 0)
    SetChrSubChip(0xD, 0)
    SetChrSubChip(0x10, 0)

    def lambda_8A4A():
        OP_6B(1700, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8A4A)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #149
        0xE,
        (
            "#885F#5P……皇子！\x01",
            "您到底作何打算？\x02\x03",

            "本以为您\x01",
            "难得露面，\x01",
            "结、结果却演了这么出猴子戏……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xD,
        (
            "#891F#6P哈哈哈。\x01",
            "还是被看穿了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xE,
        (
            "#886F#5P当然了！\x02\x03",

            "没想到皇子竟\x01",
            "在利贝尔谋划着这种事……\x02\x03",

            "#885F穆拉！\x01",
            "有你跟着，怎么还会发生这种事！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x10,
        (
            "#272F#4P恕我直言，叔叔……\x02\x03",

            "您认为这个人\x01",
            "会乖乖听我的话吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xE,
        "#886F#5P可恶……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x10,
        (
            "#270F#4P而且有些事情，\x01",
            "连我也无法接受。\x02\x03",

            "『哈梅尔的悲剧』……\x01",
            "由于这次的事件，我才终于知道了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xE,
        "#883F#5P！！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x10,
        "#276F#4P……您果然知道的吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xD,
        (
            "#891F#6P哈哈，老师不可能\x01",
            "不知道那件事吧？\x02\x03",

            "#890F当时您已经是\x01",
            "军队中的重要人物了嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xE,
        "#884F#5P…………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xD,
        (
            "#891F#6P不过，老师。\x01",
            "我并不是在责备您。\x02\x03",

            "那只是一部分主战派\x01",
            "的企图，和老师您完全\x01",
            "没有关系。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xD, 270, 400)
    Sleep(500)

    ChrTalk(    #160
        0xD,
        (
            "#894F#2P由于是重大的丑闻，\x01",
            "因此进行了彻底的情报管制……\x02\x03",

            "虽然难以赞成，但还是可以理解。\x02\x03",

            "将污点掩埋，祈祷女神的宽恕，\x01",
            "对国民来说，这就是国家的正义。\x02\x03",

            "#897F然而……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xD, 0, 400)
    Sleep(500)

    ChrTalk(    #161
        0xD,
        (
            "#896F#6P──我绝不允许\x01",
            "相同的欺瞒再发生第二次。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xE,
        "#883F#5P…………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xD,
        (
            "#897F#6P老师，您其实也\x01",
            "应该注意到了。\x02\x03",

            "过于唐突地出动蒸气坦克……\x02\x03",

            "还有在极其不自然的\x01",
            "时机发出的出击命令……\x02\x03",

            "#899F一切都是『铁血宰相』\x01",
            "吉利亚斯·奥斯本\x01",
            "所策划的行动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xE,
        "#882F#5P！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xD,
        (
            "#899F#6P这次的事情让我完全确信了。\x02\x03",

            "他一定\x01",
            "与『噬身之蛇』有所勾结。\x02\x03",

            "#895F这种事会为帝国\x01",
            "带来怎样的影响，\x01",
            "我目前还无法断言……\x02\x03",

            "但无论如何，这并不是\x01",
            "一国的宰相应有的举止吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xE,
        (
            "#884F#5P………………………\x02\x03",

            "#882F皇子，难不成您……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xD,
        (
            "#890F#6P呵呵，正是如此。\x02\x03",

            "#894F１０年前崭露头角后\x01",
            "成为帝国政府的中心人物，\x01",
            "军部出身的政治家……\x02\x03",

            "在帝国全境铺设铁路网，\x01",
            "武力合并数个自治州…\x01",
            "冷血而大胆无畏的改革者。\x02\x03",

            "#896F我已决心惩治那个\x01",
            "蚕食着帝国的怪物。\x02\x03",

            "这次的行动\x01",
            "就是对他的宣战布告。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xE,
        (
            "#884F#5P……既然如此。\x02\x03",

            "#882F皇子……\x01",
            "您能理解\x01",
            "这件事的困难程度吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0xD,
        (
            "#895F#6P这个当然。\x02\x03",

            "#893F政府自不必说，连军队也都有七成\x01",
            "都在他的控制之下。\x02\x03",

            "除了老师这样的中立派，\x01",
            "反对势力只剩下开始衰弱的诸侯了。\x02\x03",

            "而更糟糕的是\x01",
            "父亲对其的信赖也相当深厚。\x02\x03",

            "#892F真是个怪物一样的人物。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xE,
        "#885F#5P那为何还……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xD,
        (
            "#894F#6P哼，这还用说。\x02\x03",

            "#890F因为他的做法太缺乏美感了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xE,
        "#883F#5P！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xD,
        (
            "#891F#6P在利贝尔的旅行\x01",
            "让我更加确信，\x02\x03",

            "人和国家，只要有心\x01",
            "可以变得无比高贵。\x02\x03",

            "#890F而我希望我的祖国和同胞\x01",
            "也能拥有同样的高贵。\x02\x03",

            "可以的话，希望老师\x01",
            "也能协助我的理想。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xE,
        (
            "#883F#5P……………………………\x02\x03",

            "#884F……皇子。\x01",
            "您真是长大了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xD,
        (
            "#891F#6P呵呵，\x01",
            "士别三日当刮目相看嘛。\x02\x03",

            "#890F更何况，和老师学习武术和兵法\x01",
            "已经是７年前的事了。\x02\x03",

            "我也稍微成长了一点嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xE,
        (
            "#884F#5P呵呵……是啊。\x02\x03",

            "#882F……关于撤退我明白了。\x02\x03",

            "但是，我们第３师团\x01",
            "只不过是先驱部队而已。\x02\x03",

            "在帝都，宰相阁下已经\x01",
            "陆续集结了１０个师团。\x02\x03",

            "#884F包括今天一共３日……\x01",
            "不能再宽限更多了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xD,
        "#895F#6P啊啊……我明白。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xE,
        (
            "#881F#5P穆拉。\x01",
            "你也跟皇子一起去。\x02\x03",

            "要是情况危险的话，\x01",
            "就算揪着他的头发也都要把他给我拖回来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x10,
        "#277F#4P嗯嗯，原本就是这个打算。\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x45, 4000, 0, 157450, 180)
    SetChrPos(0x46, 5930, -50, 157450, 180)
    SetChrPos(0x47, 7900, 0, 157450, 180)
    SetChrPos(0x48, 9800, 90, 157450, 180)
    SetChrPos(0x49, 11700, -30, 157450, 180)
    SetChrPos(0x4A, 13540, -30, 157450, 180)
    SetChrPos(0x4B, 4000, 40, 159600, 180)
    SetChrPos(0x4C, 5930, 20, 159600, 180)
    SetChrPos(0x4D, 7900, -20, 159600, 180)
    SetChrPos(0x4E, 9800, 50, 159600, 180)
    SetChrPos(0x4F, 11700, -20, 159600, 180)
    SetChrPos(0x50, 13540, -50, 159600, 180)
    SetChrPos(0x51, 4000, 30, 161750, 180)
    SetChrPos(0x52, 5930, 10, 161750, 180)
    SetChrPos(0x53, 7900, 20, 161750, 180)
    SetChrPos(0x54, 9800, 70, 161750, 180)
    SetChrPos(0x55, 11700, -10, 161750, 180)
    SetChrPos(0x56, 13540, -30, 161750, 180)
    SetChrPos(0x57, 4000, -20, 163900, 180)
    SetChrPos(0x58, 5930, -40, 163900, 180)
    SetChrPos(0x59, 7900, -40, 163900, 180)
    SetChrPos(0x5A, 9800, 40, 163900, 180)
    SetChrPos(0x5B, 11700, -40, 163900, 180)
    SetChrPos(0x5C, 13540, -20, 163900, 180)
    SetChrPos(0x5D, 4000, -40, 166050, 180)
    SetChrPos(0x5E, 5930, 0, 166050, 180)
    SetChrPos(0x5F, 7900, 30, 166050, 180)
    SetChrPos(0x60, 9800, 60, 166050, 180)
    SetChrPos(0x61, 11700, 10, 166050, 180)
    SetChrPos(0x62, 13540, -20, 166050, 180)
    SetChrPos(0x67, -11510, -30, 157450, 180)
    SetChrPos(0x68, -9600, -30, 157450, 180)
    SetChrPos(0x6D, -11510, -20, 159600, 180)
    SetChrPos(0x6E, -9600, -50, 159600, 180)
    SetChrPos(0x73, -11510, -10, 161750, 180)
    SetChrPos(0x74, -9600, -30, 161750, 180)
    SetChrPos(0x79, -11510, -40, 163900, 180)
    SetChrPos(0x7A, -9600, -20, 163900, 180)
    SetChrPos(0x63, -9600, -30, 168200, 180)
    SetChrPos(0x64, -7630, -40, 168200, 180)
    SetChrPos(0x65, -5660, 0, 168200, 180)
    SetChrPos(0x66, -3630, 30, 168200, 180)
    SetChrPos(0x69, -1730, 60, 168200, 180)
    SetChrPos(0x6A, 230, 10, 168200, 180)
    SetChrPos(0x6B, 2070, -20, 168200, 180)
    SetChrPos(0x6C, 4000, 30, 168200, 180)
    SetChrPos(0x6F, -9600, -30, 170350, 180)
    SetChrPos(0x70, -7630, -40, 170350, 180)
    SetChrPos(0x71, -5660, 0, 170350, 180)
    SetChrPos(0x72, -3630, 30, 170350, 180)
    SetChrPos(0x75, -1730, 60, 170350, 180)
    SetChrPos(0x76, 230, 10, 170350, 180)
    SetChrPos(0x77, 2070, -20, 170350, 180)
    SetChrPos(0x78, 4000, 30, 170350, 180)
    ClearChrFlags(0x45, 0x80)
    ClearChrFlags(0x46, 0x80)
    ClearChrFlags(0x47, 0x80)
    ClearChrFlags(0x48, 0x80)
    ClearChrFlags(0x49, 0x80)
    ClearChrFlags(0x4A, 0x80)
    ClearChrFlags(0x4B, 0x80)
    ClearChrFlags(0x4C, 0x80)
    ClearChrFlags(0x4D, 0x80)
    ClearChrFlags(0x4E, 0x80)
    ClearChrFlags(0x4F, 0x80)
    ClearChrFlags(0x50, 0x80)
    ClearChrFlags(0x51, 0x80)
    ClearChrFlags(0x52, 0x80)
    ClearChrFlags(0x53, 0x80)
    ClearChrFlags(0x54, 0x80)
    ClearChrFlags(0x55, 0x80)
    ClearChrFlags(0x56, 0x80)
    ClearChrFlags(0x57, 0x80)
    ClearChrFlags(0x58, 0x80)
    ClearChrFlags(0x59, 0x80)
    ClearChrFlags(0x5A, 0x80)
    ClearChrFlags(0x5B, 0x80)
    ClearChrFlags(0x5C, 0x80)
    ClearChrFlags(0x5D, 0x80)
    ClearChrFlags(0x5E, 0x80)
    ClearChrFlags(0x5F, 0x80)
    ClearChrFlags(0x60, 0x80)
    ClearChrFlags(0x61, 0x80)
    ClearChrFlags(0x62, 0x80)
    ClearChrFlags(0x63, 0x80)
    ClearChrFlags(0x64, 0x80)
    ClearChrFlags(0x65, 0x80)
    ClearChrFlags(0x66, 0x80)
    ClearChrFlags(0x67, 0x80)
    ClearChrFlags(0x68, 0x80)
    ClearChrFlags(0x69, 0x80)
    ClearChrFlags(0x6A, 0x80)
    ClearChrFlags(0x6B, 0x80)
    ClearChrFlags(0x6C, 0x80)
    ClearChrFlags(0x6D, 0x80)
    ClearChrFlags(0x6E, 0x80)
    ClearChrFlags(0x6F, 0x80)
    ClearChrFlags(0x70, 0x80)
    ClearChrFlags(0x71, 0x80)
    ClearChrFlags(0x72, 0x80)
    ClearChrFlags(0x73, 0x80)
    ClearChrFlags(0x74, 0x80)
    ClearChrFlags(0x75, 0x80)
    ClearChrFlags(0x76, 0x80)
    ClearChrFlags(0x77, 0x80)
    ClearChrFlags(0x78, 0x80)
    ClearChrFlags(0x79, 0x80)
    ClearChrFlags(0x7A, 0x80)
    ClearChrFlags(0x7B, 0x80)
    ClearChrFlags(0x7C, 0x80)
    ClearChrFlags(0x7D, 0x80)
    ClearChrFlags(0x7E, 0x80)

    def lambda_99E8():
        OP_6D(-1410, 70, 152440, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_99E8)

    def lambda_9A00():
        OP_6B(2600, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9A00)
    OP_8C(0xE, 0, 400)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #180
        0xE,
        "#885F#2P#3S全军撤退！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #181
        0xE,
        (
            "#885F#2P#3S第３师团！\x01",
            "全体向帕鲁姆市郊外移动！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(800)
    SetMessageWindowPos(50, 90, -1, -1)
    SetChrName("帝国军士兵")

    AnonymousTalk(    #182
        "\x07\x00#5S是，长官！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_6D(-2140, 50, 142400, 0)
    OP_67(0, 6700, -10000, 0)
    OP_6B(3630, 0)
    OP_6C(45000, 0)
    OP_6E(340, 0)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrPos(0x27, -7630, 0, 89450, 0)
    SetChrPos(0x28, -5660, -50, 89450, 0)
    SetChrPos(0x29, -3630, 0, 89450, 0)
    SetChrPos(0x2A, -1730, 90, 89450, 0)
    SetChrPos(0x2B, 230, -30, 89450, 0)
    SetChrPos(0x2C, 2070, -30, 89450, 0)
    SetChrPos(0x2D, -7630, 40, 91600, 0)
    SetChrPos(0x2E, -5660, 20, 91600, 0)
    SetChrPos(0x2F, -3630, -20, 91600, 0)
    SetChrPos(0x30, -1730, 50, 91600, 0)
    SetChrPos(0x31, 230, -20, 91600, 0)
    SetChrPos(0x32, 2070, -50, 91600, 0)
    SetChrPos(0x33, -7630, 30, 93750, 0)
    SetChrPos(0x34, -5660, 10, 93750, 0)
    SetChrPos(0x35, -3630, 20, 93750, 0)
    SetChrPos(0x36, -1730, 70, 93750, 0)
    SetChrPos(0x37, 230, -10, 93750, 0)
    SetChrPos(0x38, 2070, -30, 93750, 0)
    SetChrPos(0x39, -7630, -20, 95900, 0)
    SetChrPos(0x3A, -5660, -40, 95900, 0)
    SetChrPos(0x3B, -3630, -40, 95900, 0)
    SetChrPos(0x3C, -1730, 40, 95900, 0)
    SetChrPos(0x3D, 230, -40, 95900, 0)
    SetChrPos(0x3E, 2070, -20, 95900, 0)
    SetChrPos(0x3F, -7630, -40, 98050, 0)
    SetChrPos(0x40, -5660, 0, 98050, 0)
    SetChrPos(0x41, -3630, 30, 98050, 0)
    SetChrPos(0x42, -1730, 60, 98050, 0)
    SetChrPos(0x43, 230, 10, 98050, 0)
    SetChrPos(0x44, 2070, -20, 98050, 0)
    SetChrPos(0x45, 4000, 0, 89450, 0)
    SetChrPos(0x46, 5930, -50, 89450, 0)
    SetChrPos(0x47, 7900, 0, 89450, 0)
    SetChrPos(0x48, 9800, 90, 89450, 0)
    SetChrPos(0x49, 11700, -30, 89450, 0)
    SetChrPos(0x4A, 13540, -30, 89450, 0)
    SetChrPos(0x4B, 4000, 40, 91600, 0)
    SetChrPos(0x4C, 5930, 20, 91600, 0)
    SetChrPos(0x4D, 7900, -20, 91600, 0)
    SetChrPos(0x4E, 9800, 50, 91600, 0)
    SetChrPos(0x4F, 11700, -20, 91600, 0)
    SetChrPos(0x50, 13540, -50, 91600, 0)
    SetChrPos(0x51, 4000, 30, 93750, 0)
    SetChrPos(0x52, 5930, 10, 93750, 0)
    SetChrPos(0x53, 7900, 20, 93750, 0)
    SetChrPos(0x54, 9800, 70, 93750, 0)
    SetChrPos(0x55, 11700, -10, 93750, 0)
    SetChrPos(0x56, 13540, -30, 93750, 0)
    SetChrPos(0x57, 4000, -20, 95900, 0)
    SetChrPos(0x58, 5930, -40, 95900, 0)
    SetChrPos(0x59, 7900, -40, 95900, 0)
    SetChrPos(0x5A, 9800, 40, 95900, 0)
    SetChrPos(0x5B, 11700, -40, 95900, 0)
    SetChrPos(0x5C, 13540, -20, 95900, 0)
    SetChrPos(0x5D, 4000, -40, 98050, 0)
    SetChrPos(0x5E, 5930, 0, 98050, 0)
    SetChrPos(0x5F, 7900, 30, 98050, 0)
    SetChrPos(0x60, 9800, 60, 98050, 0)
    SetChrPos(0x61, 11700, 10, 98050, 0)
    SetChrPos(0x62, 13540, -20, 98050, 0)
    SetChrPos(0x63, -19030, 0, 89450, 0)
    SetChrPos(0x64, -17150, -50, 89450, 0)
    SetChrPos(0x65, -15270, 0, 89450, 0)
    SetChrPos(0x66, -13390, 90, 89450, 0)
    SetChrPos(0x67, -11510, -30, 89450, 0)
    SetChrPos(0x68, -9600, -30, 89450, 0)
    SetChrPos(0x69, -19030, 40, 91600, 0)
    SetChrPos(0x6A, -17150, 20, 91600, 0)
    SetChrPos(0x6B, -15270, -20, 91600, 0)
    SetChrPos(0x6C, -13390, 50, 91600, 0)
    SetChrPos(0x6D, -11510, -20, 91600, 0)
    SetChrPos(0x6E, -9600, -50, 91600, 0)
    SetChrPos(0x6F, -19030, 30, 93750, 0)
    SetChrPos(0x70, -17150, 10, 93750, 0)
    SetChrPos(0x71, -15270, 20, 93750, 0)
    SetChrPos(0x72, -13390, 70, 93750, 0)
    SetChrPos(0x73, -11510, -10, 93750, 0)
    SetChrPos(0x74, -9600, -30, 93750, 0)
    SetChrPos(0x75, -19030, -20, 95900, 0)
    SetChrPos(0x76, -17150, -40, 95900, 0)
    SetChrPos(0x77, -15270, -40, 95900, 0)
    SetChrPos(0x78, -13390, 40, 95900, 0)
    SetChrPos(0x79, -11510, -40, 95900, 0)
    SetChrPos(0x7A, -9600, -20, 95900, 0)
    SetChrPos(0x7B, -19030, -40, 98050, 0)
    SetChrPos(0x7C, -17150, 0, 98050, 0)
    SetChrPos(0x7D, -15270, 30, 98050, 0)
    SetChrPos(0x7E, -13390, 60, 98050, 0)
    SetChrChipByIndex(0x15, 9)
    SetChrChipByIndex(0x16, 9)
    SetChrSubChip(0x15, 0)
    SetChrSubChip(0x16, 0)
    SetChrFlags(0x15, 0x200)
    SetChrFlags(0x16, 0x200)
    SetChrPos(0x15, -11510, 10, 98050, 0)
    SetChrPos(0x16, -9600, -20, 98050, 0)
    OP_8C(0x17, 180, 0)
    OP_8C(0x18, 180, 0)
    OP_8C(0x19, 180, 0)
    OP_8C(0x1A, 180, 0)
    OP_8C(0x1B, 180, 0)
    OP_8C(0x1C, 180, 0)
    OP_8C(0x1D, 180, 0)
    OP_8C(0x1E, 180, 0)
    OP_8C(0x1F, 180, 0)
    OP_8C(0x20, 180, 0)
    OP_8C(0x21, 180, 0)
    OP_8C(0x22, 180, 0)
    OP_8C(0x23, 180, 0)
    OP_8C(0x24, 180, 0)
    LoadEffect(0x0, "map\\\\mp109_00.eff")
    LoadEffect(0x1, "map\\\\onsen00.eff")
    PlayEffect(0x0, 0xFF, 0x17, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x17, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x18, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x18, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x19, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x19, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1A, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1A, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1B, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1B, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1C, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1C, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1D, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1D, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1E, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1E, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1F, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1F, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x20, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x20, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x21, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x21, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x22, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x22, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x23, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x23, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x24, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x24, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x17, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x17, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x18, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x18, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x19, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x19, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1A, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1A, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1B, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1B, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1C, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1C, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1D, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1D, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1E, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1E, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1F, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1F, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x20, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x20, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x21, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x21, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x22, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x22, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x23, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x23, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x24, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x24, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_6D(-2080, 50, 134590, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(45000, 0)
    OP_6E(500, 0)
    SetChrChipByIndex(0x13, 13)
    SetChrChipByIndex(0x12, 14)
    SetChrChipByIndex(0x14, 15)
    OP_22(0x10F, 0x1, 0x64)
    OP_22(0x110, 0x1, 0x5F)
    OP_43(0x17, 0x3, 0x0, 0x1E)
    WaitChrThread(0x17, 0x3)
    OP_43(0x27, 0x3, 0x0, 0x1F)
    OP_43(0x45, 0x3, 0x0, 0x20)
    OP_43(0x63, 0x3, 0x0, 0x21)
    WaitChrThread(0x27, 0x3)
    WaitChrThread(0x45, 0x3)
    WaitChrThread(0x63, 0x3)
    FadeToBright(1000, 0)
    OP_6D(-1520, 20, 117830, 6000)
    Fade(1000)
    OP_6D(-920, 20, 89290, 0)
    OP_67(0, 5080, -10000, 0)
    OP_6B(2450, 0)
    OP_6C(45000, 0)
    OP_6E(364, 0)
    SetChrPos(0xD, -1950, 40, 88980, 0)
    SetChrPos(0x10, -600, 70, 88900, 0)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0x10, 0x80)
    OP_0D()
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x29, 0x80)
    SetChrFlags(0x2A, 0x80)
    SetChrFlags(0x2B, 0x80)
    SetChrFlags(0x2C, 0x80)
    SetChrFlags(0x2D, 0x80)
    SetChrFlags(0x2E, 0x80)
    SetChrFlags(0x2F, 0x80)
    SetChrFlags(0x30, 0x80)
    SetChrFlags(0x31, 0x80)
    SetChrFlags(0x32, 0x80)
    SetChrFlags(0x33, 0x80)
    SetChrFlags(0x34, 0x80)
    SetChrFlags(0x35, 0x80)
    SetChrFlags(0x36, 0x80)
    SetChrFlags(0x37, 0x80)
    SetChrFlags(0x38, 0x80)
    SetChrFlags(0x39, 0x80)
    SetChrFlags(0x3A, 0x80)
    SetChrFlags(0x3B, 0x80)
    SetChrFlags(0x3C, 0x80)
    SetChrFlags(0x3D, 0x80)
    SetChrFlags(0x3E, 0x80)
    SetChrFlags(0x3F, 0x80)
    SetChrFlags(0x40, 0x80)
    SetChrFlags(0x41, 0x80)
    SetChrFlags(0x42, 0x80)
    SetChrFlags(0x43, 0x80)
    SetChrFlags(0x44, 0x80)
    SetChrFlags(0x45, 0x80)
    SetChrFlags(0x46, 0x80)
    SetChrFlags(0x47, 0x80)
    SetChrFlags(0x48, 0x80)
    SetChrFlags(0x49, 0x80)
    SetChrFlags(0x4A, 0x80)
    SetChrFlags(0x4B, 0x80)
    SetChrFlags(0x4C, 0x80)
    SetChrFlags(0x4D, 0x80)
    SetChrFlags(0x4E, 0x80)
    SetChrFlags(0x4F, 0x80)
    SetChrFlags(0x50, 0x80)
    SetChrFlags(0x51, 0x80)
    SetChrFlags(0x52, 0x80)
    SetChrFlags(0x53, 0x80)
    SetChrFlags(0x54, 0x80)
    SetChrFlags(0x55, 0x80)
    SetChrFlags(0x56, 0x80)
    SetChrFlags(0x57, 0x80)
    SetChrFlags(0x58, 0x80)
    SetChrFlags(0x59, 0x80)
    SetChrFlags(0x5A, 0x80)
    SetChrFlags(0x5B, 0x80)
    SetChrFlags(0x5C, 0x80)
    SetChrFlags(0x5D, 0x80)
    SetChrFlags(0x5E, 0x80)
    SetChrFlags(0x5F, 0x80)
    SetChrFlags(0x60, 0x80)
    SetChrFlags(0x61, 0x80)
    SetChrFlags(0x62, 0x80)
    SetChrFlags(0x63, 0x80)
    SetChrFlags(0x64, 0x80)
    SetChrFlags(0x65, 0x80)
    SetChrFlags(0x66, 0x80)
    SetChrFlags(0x67, 0x80)
    SetChrFlags(0x68, 0x80)
    SetChrFlags(0x69, 0x80)
    SetChrFlags(0x6A, 0x80)
    SetChrFlags(0x6B, 0x80)
    SetChrFlags(0x6C, 0x80)
    SetChrFlags(0x6D, 0x80)
    SetChrFlags(0x6E, 0x80)
    SetChrFlags(0x6F, 0x80)
    SetChrFlags(0x70, 0x80)
    SetChrFlags(0x71, 0x80)
    SetChrFlags(0x72, 0x80)
    SetChrFlags(0x73, 0x80)
    SetChrFlags(0x74, 0x80)
    SetChrFlags(0x75, 0x80)
    SetChrFlags(0x76, 0x80)
    SetChrFlags(0x77, 0x80)
    SetChrFlags(0x78, 0x80)
    SetChrFlags(0x79, 0x80)
    SetChrFlags(0x7A, 0x80)
    SetChrFlags(0x7B, 0x80)
    SetChrFlags(0x7C, 0x80)
    SetChrFlags(0x7D, 0x80)
    SetChrFlags(0x7E, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    OP_71(0x3, 0x0)
    OP_71(0x4, 0x0)
    OP_71(0x5, 0x0)
    OP_71(0x6, 0x0)
    OP_71(0x7, 0x0)
    OP_71(0x8, 0x0)
    OP_71(0x9, 0x0)
    OP_71(0xA, 0x0)
    OP_71(0xB, 0x0)
    OP_71(0xC, 0x0)
    OP_71(0xD, 0x0)
    OP_71(0xE, 0x0)
    OP_71(0xF, 0x0)
    OP_71(0x10, 0x0)
    OP_43(0xD, 0x3, 0x0, 0x22)
    Sleep(500)

    ChrTalk(    #183
        0xD,
        (
            "#890F#6P哎呀哎呀……\x01",
            "终于稍微争取了一点时间吗。\x02\x03",

            "#893F话说回来，我还\x01",
            "真是没信用啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 270, 400)
    Sleep(300)

    ChrTalk(    #184
        0x10,
        (
            "#276F#2P……当然啦，蠢货。\x02\x03",

            "#272F说实话，\x01",
            "真没想到会闹得这么大。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xD, 90, 400)
    Sleep(300)

    ChrTalk(    #185
        0xD,
        (
            "#890F#6P既然要做，\x01",
            "就要做得华丽啊～\x02\x03",

            "#891F而且你不是也\x01",
            "早就做了准备吗？\x02\x03",

            "可以说是共同享受甜蜜结果的\x01",
            "相亲相爱的共犯者。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x10,
        "#274F#2P别说得那么恶心。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x101,
        "#1P奥利维尔！\x02",
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_62(0x10, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(500)
    OP_6D(-2560, 70, 87160, 0)
    OP_67(0, 5080, -10000, 0)
    OP_6B(2450, 0)
    OP_6C(225000, 0)
    OP_6E(364, 0)

    def lambda_B267():
        OP_6D(-3120, -20, 84880, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B267)

    def lambda_B27F():
        OP_6E(381, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B27F)
    OP_43(0x101, 0x1, 0x0, 0x16)
    OP_43(0xC, 0x1, 0x0, 0x17)
    OP_43(0x102, 0x1, 0x0, 0x18)
    OP_43(0xA, 0x1, 0x0, 0x1B)
    OP_43(0x8, 0x1, 0x0, 0x19)
    OP_43(0x9, 0x1, 0x0, 0x1A)
    OP_43(0xB, 0x1, 0x0, 0x1C)
    OP_43(0xF, 0x1, 0x0, 0x1D)
    OP_8C(0xD, 180, 400)
    OP_8C(0x10, 180, 400)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #188
        0xD,
        (
            "#891F#4P呀，艾丝蒂尔。\x01",
            "你辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x101,
        (
            "#1009F#5P辛苦你个头啦！\x02\x03",

            "到底是怎么回事！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0xD,
        (
            "#890F#4P也没怎么回事啦，\x01",
            "嗯，就和你看到的一样嘛。\x02\x03",

            "#891F因为帝国内正进行着\x01",
            "可疑的阴谋。\x02\x03",

            "所以就稍微表演一下，\x01",
            "挫挫他们的锐气。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x101,
        "#1019F#5P表演一下……你啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0xD,
        (
            "#894F#4P要瞒过敌人\x01",
            "首先得瞒过自己人嘛。\x02\x03",

            "#890F先和你们认真交涉，\x01",
            "然后埃尔赛尤出场……\x02\x03",

            "这就是我和卡西乌斯先生\x01",
            "想出来的剧本。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0x101,
        "#1007F#5P果、果然……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x102,
        "#1040F#5P就知道是这样。\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xF, 0x1)
    ClearChrFlags(0x11, 0x20)
    SetChrPos(0x11, -17000, -130, 84330, 90)

    NpcTalk(    #195
        0x11,
        "男性的声音",
        "#3P……嗯，就是这么回事。\x02",
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_B5DA():
        OP_6D(-3420, -30, 84750, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B5DA)

    def lambda_B5F2():
        OP_6B(2590, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_B5F2)

    def lambda_B602():
        OP_6C(224000, 4000)
        ExitThread()

    QueueWorkItem(0xD, 3, lambda_B602)

    def lambda_B612():

        label("loc_B612")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_B612")

    QueueWorkItem2(0xD, 1, lambda_B612)

    def lambda_B623():

        label("loc_B623")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_B623")

    QueueWorkItem2(0x10, 1, lambda_B623)
    Sleep(50)

    def lambda_B639():

        label("loc_B639")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_B639")

    QueueWorkItem2(0xC, 1, lambda_B639)

    def lambda_B64A():

        label("loc_B64A")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_B64A")

    QueueWorkItem2(0x101, 1, lambda_B64A)
    Sleep(50)

    def lambda_B660():

        label("loc_B660")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_B660")

    QueueWorkItem2(0x102, 1, lambda_B660)

    def lambda_B671():

        label("loc_B671")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_B671")

    QueueWorkItem2(0x9, 1, lambda_B671)
    Sleep(50)

    def lambda_B687():

        label("loc_B687")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_B687")

    QueueWorkItem2(0x8, 1, lambda_B687)

    def lambda_B698():

        label("loc_B698")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_B698")

    QueueWorkItem2(0xA, 1, lambda_B698)
    Sleep(50)

    def lambda_B6AE():

        label("loc_B6AE")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_B6AE")

    QueueWorkItem2(0xB, 1, lambda_B6AE)

    def lambda_B6BF():

        label("loc_B6BF")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_B6BF")

    QueueWorkItem2(0xF, 1, lambda_B6BF)
    OP_8E(0x11, 0xFFFFE9B2, 0xFFFFFFE2, 0x14C4E, 0xBB8, 0x0)
    OP_8C(0x11, 90, 400)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #196
        0x101,
        "#1009F#6P老爸～！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x11,
        (
            "#1123F#2P别摆出这么可怕的表情嘛。\x02\x03",

            "#1120F我通过导力通信听到了，\x01",
            "真是场相当不错的谈判啊。\x02\x03",

            "托你的福，埃尔赛尤的登场\x01",
            "演出更有成效了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x101,
        "#1004F#6P用导力通信听到……\x02",
    )

    CloseMessageWindow()
    OP_44(0x8, 0x1)
    OP_8C(0x8, 0, 400)
    Sleep(300)

    ChrTalk(    #199
        0x8,
        (
            "#023F#5P难不成……\x01",
            "用那个古代遗物？\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0xD, 0x1)
    OP_8C(0xD, 180, 400)
    Sleep(300)

    ChrTalk(    #200
        0xD,
        (
            "#891F#6P哟，雪拉。\x01",
            "别说这个了。\x02\x03",

            "被他听见的话\x01",
            "稍微有点麻烦呢。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x14, -22110, -290, 84920, 90)
    SetChrPos(0x12, -21810, -280, 83150, 90)
    SetChrPos(0x13, -23280, -330, 83160, 90)

    NpcTalk(    #201
        0x14,
        "青年的声音",
        (
            "#3P……干嘛装模作样。\x01",
            "事到如今，再想掩饰也太迟了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B8B6():
        OP_6D(-5560, 20, 84410, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B8B6)

    def lambda_B8CE():
        OP_67(0, 4530, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B8CE)

    def lambda_B8E6():
        OP_6E(380, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_B8E6)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)

    def lambda_B905():

        label("loc_B905")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_B905")

    QueueWorkItem2(0xC, 1, lambda_B905)

    def lambda_B916():

        label("loc_B916")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_B916")

    QueueWorkItem2(0x101, 1, lambda_B916)

    def lambda_B927():

        label("loc_B927")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_B927")

    QueueWorkItem2(0x102, 1, lambda_B927)
    Sleep(100)

    def lambda_B93D():

        label("loc_B93D")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_B93D")

    QueueWorkItem2(0x9, 1, lambda_B93D)

    def lambda_B94E():

        label("loc_B94E")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_B94E")

    QueueWorkItem2(0x8, 1, lambda_B94E)
    Sleep(100)

    def lambda_B964():

        label("loc_B964")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_B964")

    QueueWorkItem2(0xA, 1, lambda_B964)

    def lambda_B975():

        label("loc_B975")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_B975")

    QueueWorkItem2(0xB, 1, lambda_B975)

    def lambda_B986():

        label("loc_B986")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_B986")

    QueueWorkItem2(0xF, 1, lambda_B986)
    Sleep(100)

    def lambda_B99C():

        label("loc_B99C")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_B99C")

    QueueWorkItem2(0xD, 1, lambda_B99C)

    def lambda_B9AD():

        label("loc_B9AD")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_B9AD")

    QueueWorkItem2(0x10, 1, lambda_B9AD)

    def lambda_B9BE():
        OP_8E(0xFE, 0xFFFFE75A, 0xFFFFFFF6, 0x14FF0, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_B9BE)
    Sleep(400)

    def lambda_B9DE():
        OP_8E(0xFE, 0xFFFFE778, 0xFFFFFFF6, 0x146AE, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_B9DE)
    Sleep(400)

    def lambda_B9FE():
        OP_8E(0xFE, 0xFFFFE188, 0xFFFFFFF6, 0x147EE, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_B9FE)
    WaitChrThread(0x14, 0x1)
    WaitChrThread(0x101, 0x0)
    OP_44(0x8, 0x1)
    OP_44(0x102, 0x1)

    def lambda_BA2B():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BA2B)
    Sleep(50)

    def lambda_BA3E():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_BA3E)

    ChrTalk(    #202
        0x101,
        "#1004F#6P凯、凯文先生！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xA,
        "#560F#6P爷，爷爷！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0xC,
        "#1168F#6P还有尤莉亚……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x13, 0x1)

    ChrTalk(    #205
        0x13,
        (
            "#176F殿下……\x01",
            "我听说王都被袭击了。\x02\x03",

            "#175F不过……您没事就好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0xC,
        (
            "#1169F#6P对不起……\x01",
            "让你担心了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x12,
        (
            "#101F#5P呀～埃尔赛尤的改造\x01",
            "如果能早些完成，王都的危机也\x01",
            "就不至于这么晚才解决了……\x02\x03",

            "比预想中\x01",
            "花费了更多时间啊。\x02\x03",

            "#100F不过，大家都没事就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x9,
        (
            "#055F#6P话，话说回来……\x02\x03",

            "为何埃尔赛尤\x01",
            "能飞上天空！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xA,
        (
            "#560F#6P难不成……\x01",
            "『零力场发生器』的大型版开发出来了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x12,
        (
            "#101F#5P嗯，没错。\x02\x03",

            "#100F给你们的是\x01",
            "为了开发大型版\x01",
            "而试制的原型。\x02\x03",

            "至今为止我都在埃尔赛尤上\x01",
            "闭关研究，总算是完成了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x102,
        "#1040F#6P原来是这样……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0x101,
        (
            "#1019F#6P也就是说，一切\x01",
            "都是老爸设的局了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0x11,
        (
            "#1123F#2P别说得这么伤人嘛。\x02\x03",

            "#1120F我只不过为了方便大家行动\x01",
            "而做了各种准备而已。\x02\x03",

            "你们也一直都是\x01",
            "按照自己的意思行事的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0x101,
        (
            "#1015F#6P话，话是没错啦……\x02\x03",

            "#1004F那，凯文先生\x01",
            "又为什么会在这里？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x14,
        (
            "#1062F#2P啊啊，其实大圣堂\x01",
            "收到了骑士团本部的联络。\x02\x03",

            "『辉之环』到底是怎样的东西，\x01",
            "怎样才能控制灾难，\x01",
            "现在大致都明白了。\x02\x03",

            "#1061F将情况告知给卡西乌斯先生之后\x01",
            "我就一起跟过来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0x101,
        "#1020F#6P咦咦！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0x102,
        "#1042F#6P『辉之环』的正体……是吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0x14,
        (
            "#1065F#2P啊啊……\x02\x03",

            "#1063F所谓『辉之环』\x01",
            "并不是那个浮游都市本身。\x02\x03",

            "而是引导都市全体的导力走向，\x01",
            "并且加以控制的古代遗物。\x02\x03",

            "而其终端\x01",
            "就是那个『福音』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0xC,
        "#1163F#6P管理都市的古代遗物……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0xA,
        (
            "#065F#6P但、但是为什么\x01",
            "那东西会引起导力停止现象？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x14,
        (
            "#1067F#2P现在只是推测……\x01",
            "环似乎具备排除\x01",
            "外界异物的功能。\x02\x03",

            "#1063F在如今的情况下，所谓的异物\x01",
            "就是现代所创造的新导力器──\x01",
            "也就是Orbment。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0xB,
        (
            "#074F#6P将影响范围内的异物\x01",
            "全部无力化……\x02\x03",

            "#072F可以说这是一种防卫架构吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x12,
        (
            "#104F#5P这个可能性很高。\x02\x03",

            "#102F而如果这是真的，\x01",
            "就可以看见一线光明了。\x02\x03",

            "由于过于巨大，要对都市本身\x01",
            "进行全面处理非常困难……\x02\x03",

            "但如果能够找到存放在都市\x01",
            "某处的环的实体，\x01",
            "应该就能做出对策了。  \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0x102,
        (
            "#1040F#6P原来如此……\x01",
            "是这么回事啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0x101,
        "#1006F#6P的、的确可能有希望……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0xD,
        (
            "#891F#6P嗯，这下最终目的\x01",
            "不就能确定了吗。\x02\x03",

            "#890F那么就马上乘上『埃尔赛尤』\x01",
            "前往那个浮游都市吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0x11,
        (
            "#1125F#2P要做这个决定，\x01",
            "得看拥有『埃尔赛尤』的\x01",
            "利贝尔王室了。\x02\x03",

            "#1122F公主殿下……请下决定吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0xC,
        (
            "#1167F#6P……我明白了。\x02\x03",

            "#1162F现在开始，『埃尔赛尤』\x01",
            "就向瓦雷利亚湖上出现的\x01",
            "古代浮游都市前进。\x02\x03",

            "尤莉亚上尉，准备起飞。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0x13,
        "#171F明白！\x02",
    )

    CloseMessageWindow()
    OP_8C(0x13, 270, 400)

    def lambda_C2E0():
        OP_8E(0xFE, 0xFFFFA510, 0xFFFFFEB6, 0x144D8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_C2E0)

    def lambda_C2FB():
        OP_6D(-3610, -30, 83240, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_C2FB)

    def lambda_C313():
        OP_67(0, 4980, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C313)

    def lambda_C32B():
        OP_6B(2450, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C32B)

    def lambda_C33B():
        OP_6C(224000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_C33B)

    def lambda_C34B():
        OP_6E(354, 2000)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_C34B)
    OP_44(0xC, 0x1)
    OP_8C(0xC, 215, 400)
    WaitChrThread(0x101, 0x0)
    Sleep(500)

    ChrTalk(    #230
        0xC,
        "#1167F#6P还有各位游击士……\x02",
    )

    CloseMessageWindow()

    def lambda_C391():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C391)

    def lambda_C39F():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C39F)
    Sleep(50)

    def lambda_C3B2():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_C3B2)

    def lambda_C3C0():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_C3C0)
    Sleep(50)

    def lambda_C3D3():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_C3D3)

    def lambda_C3E1():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_C3E1)

    def lambda_C3EF():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_C3EF)
    Sleep(50)

    def lambda_C402():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_C402)

    def lambda_C410():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_C410)
    Sleep(400)

    ChrTalk(    #231
        0xC,
        (
            "#1162F#6P请向困境中的利贝尔\x01",
            "伸出各位的援助之手。\x02\x03",

            "这恐怕是关于这次事件的\x01",
            "最后委托了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0x8,
        "#027F#5P呵呵……是啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0x9,
        (
            "#051F#5P嗯，答案简直\x01",
            "就是不言自明嘛……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0xB,
        (
            "#071F#5P现在就请一个\x01",
            "代表来回答吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xB, 400)

    ChrTalk(    #235
        0x101,
        "#1015F#4P嗯……代表？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #236
        0x9,
        (
            "#053F#5P我说……艾丝蒂尔。\x02\x03",

            "#555F当然是说你吧？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C54E():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C54E)
    Sleep(50)

    def lambda_C561():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_C561)
    Sleep(50)
    OP_8C(0xA, 270, 400)

    ChrTalk(    #237
        0x101,
        "#1004F#4P咦咦！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0x8,
        (
            "#021F#5P呵呵……\x01",
            "你那是什么表情。\x02\x03",

            "#524F确实，虽然大家\x01",
            "各有各的目的……\x02\x03",

            "但是，不管怎么说\x01",
            "我们大家都是和你\x01",
            "共同分享旅途的同伴。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0xB,
        (
            "#070F#5P这个意义上来说，艾丝蒂尔，\x02\x03",

            "你毫无疑问\x01",
            "就是我们的领导人了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0x101,
        "#1013F#4P啊、啊啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0x11,
        (
            "#1123F#2P哎呀哎呀……\x01",
            "是觉得担子太重了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0x102,
        (
            "#1035F#5P……不是那样的。\x02\x03",

            "#1040F无论在任何时候，艾丝蒂尔都是那么乐观，\x01",
            "从不会放弃希望。\x02\x03",

            "那耀眼的光辉自始至终都在\x01",
            "指引着我──还有大家。\x02\x03",

            "#1049F所以……\x01",
            "一定要是艾丝蒂尔才行。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #243
        0x101,
        "#1013F#4P等、等一下啦约修亚！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0xA,
        (
            "#061F#6P嘿嘿……\x01",
            "姐姐，你的脸通红了哟？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0x101,
        (
            "#1013F#4P～～～呜～～～～\x02\x03",

            "#1022F啊～真是的，知道了啦！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xC, 400)
    Sleep(500)

    ChrTalk(    #246
        0x101,
        (
            "#1006F#2P科洛丝的委托……\x01",
            "就让我们接受吧！\x02\x03",

            "我们一定会找到\x01",
            "那个浮游都市中的『辉之环』，\x01",
            "并解决如今的事态！\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #247
        0xC,
        "科洛丝",
        (
            "#1168F呵呵……\x01",
            "拜托你了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0x11,
        (
            "#1120F#2P哎呀哎呀……\x01",
            "终于整理好思路了吗。\x02\x03",

            "这样我也终于\x01",
            "能返回司令部了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C8F6():
        OP_6D(-4960, 10, 83700, 1200)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_C8F6)

    def lambda_C90E():

        label("loc_C90E")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_C90E")

    QueueWorkItem2(0x101, 1, lambda_C90E)

    def lambda_C91F():

        label("loc_C91F")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_C91F")

    QueueWorkItem2(0x102, 1, lambda_C91F)
    Sleep(50)

    def lambda_C935():

        label("loc_C935")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_C935")

    QueueWorkItem2(0xC, 1, lambda_C935)

    def lambda_C946():

        label("loc_C946")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_C946")

    QueueWorkItem2(0x9, 1, lambda_C946)

    def lambda_C957():

        label("loc_C957")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_C957")

    QueueWorkItem2(0x8, 1, lambda_C957)
    Sleep(50)

    def lambda_C96D():

        label("loc_C96D")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_C96D")

    QueueWorkItem2(0xB, 1, lambda_C96D)

    def lambda_C97E():

        label("loc_C97E")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_C97E")

    QueueWorkItem2(0xA, 1, lambda_C97E)
    Sleep(50)

    def lambda_C994():

        label("loc_C994")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_C994")

    QueueWorkItem2(0xB, 1, lambda_C994)

    def lambda_C9A5():

        label("loc_C9A5")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_C9A5")

    QueueWorkItem2(0xF, 1, lambda_C9A5)
    Sleep(50)

    def lambda_C9BB():

        label("loc_C9BB")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_C9BB")

    QueueWorkItem2(0xD, 1, lambda_C9BB)

    def lambda_C9CC():

        label("loc_C9CC")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_C9CC")

    QueueWorkItem2(0x10, 1, lambda_C9CC)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #249
        0x101,
        (
            "#1025F#6P老爸……你果然\x01",
            "不和我们一起来啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0x11,
        (
            "#1125F#2P啊啊……抱歉了。\x02\x03",

            "#1122F虽说暂时撤退了，\x01",
            "但帝国军的威胁仍不能忽视。\x02\x03",

            "不仅仅是哈肯大门，\x01",
            "也可能会有来自海上的攻击。\x02\x03",

            "当然，在王都发生的\x01",
            "『结社』的袭击可能也会再次出现吧。\x02\x03",

            "在这种状况下，我是不能\x01",
            "离开王国军的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0x101,
        (
            "#1012F#6P嗯……明白了。\x02\x03",

            "#1017F我也会加油的。\x02\x03",

            "和约修亚……\x01",
            "还有大家一起。\x02\x03",

            "因此老爸也要……\x01",
            "在身体能承受的范围内好好努力哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0x11,
        (
            "#1120F#2P啊啊……放心吧。\x02\x03",

            "#1125F约修亚……\x01",
            "这个交给你。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0x102,
        "#1044F#6P啊……\x02",
    )

    CloseMessageWindow()

    def lambda_CBC7():
        OP_8F(0xFE, 0xFFFFED18, 0xFFFFFFF6, 0x14B5E, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_CBC7)
    Sleep(300)
    OP_44(0x102, 0x1)
    OP_8F(0x102, 0xFFFFF038, 0xFFFFFFF6, 0x14A3C, 0x3E8, 0x0)
    WaitChrThread(0x101, 0x2)
    Fade(250)
    SetChrFlags(0x11, 0x2)
    SetChrChipByIndex(0x11, 16)
    SetChrSubChip(0x11, 0)
    OP_0D()
    Sleep(300)
    SetChrSubChip(0x11, 1)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #254
        "\x07\x05卡西乌斯交给约修亚一封信。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Sleep(100)
    Fade(250)
    ClearChrFlags(0x11, 0x2)
    SetChrSubChip(0x11, 0)
    SetChrChipByIndex(0x11, 11)
    OP_0D()
    Sleep(200)

    ChrTalk(    #255
        0x102,
        "#1044F#6P这是……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0x11,
        (
            "#1125F#2P嗯，为父的一点关心。\x02\x03",

            "#1120F这可是男人之间的对话，\x01",
            "就不要让艾丝蒂尔被刺激到了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0x101,
        "#1019F#6P什、什么意思……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0x102,
        (
            "#1040F#6P……明白了。\x01",
            "我稍后再看。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0x11,
        "#1120F#2P啊啊，这样就好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0x101,
        (
            "#1007F#6P真受不了……\x01",
            "男人总是这样。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_CD97():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CD97)
    Sleep(500)

    ChrTalk(    #261
        0x11,
        (
            "#1123F#2P好了，别闹别扭了。\x02\x03",

            "#1120F等一切都解决之后，\x01",
            "我也打算休假了。\x02\x03",

            "到时候就可以\x01",
            "悠闲自在地在家休息一阵了。\x02\x03",

            "#1121F到时候，艾丝蒂尔，\x01",
            "再给我做那个煎蛋卷吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0x101,
        (
            "#1004F#6P啊……\x02\x03",

            "#1017F……嗯，包在我身上！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x29, 0x80)
    SetChrFlags(0x2A, 0x80)
    SetChrFlags(0x2B, 0x80)
    SetChrFlags(0x2C, 0x80)
    SetChrFlags(0x2D, 0x80)
    SetChrFlags(0x2E, 0x80)
    SetChrFlags(0x2F, 0x80)
    SetChrFlags(0x30, 0x80)
    SetChrFlags(0x31, 0x80)
    SetChrFlags(0x32, 0x80)
    SetChrFlags(0x33, 0x80)
    SetChrFlags(0x34, 0x80)
    SetChrFlags(0x35, 0x80)
    SetChrFlags(0x36, 0x80)
    SetChrFlags(0x37, 0x80)
    SetChrFlags(0x38, 0x80)
    SetChrFlags(0x39, 0x80)
    SetChrFlags(0x3A, 0x80)
    SetChrFlags(0x3B, 0x80)
    SetChrFlags(0x3C, 0x80)
    SetChrFlags(0x3D, 0x80)
    SetChrFlags(0x3E, 0x80)
    SetChrFlags(0x3F, 0x80)
    SetChrFlags(0x40, 0x80)
    SetChrFlags(0x41, 0x80)
    SetChrFlags(0x42, 0x80)
    SetChrFlags(0x43, 0x80)
    SetChrFlags(0x44, 0x80)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_71(0x5, 0x4)
    OP_71(0x6, 0x4)
    OP_71(0x7, 0x4)
    OP_71(0x8, 0x4)
    OP_71(0x9, 0x4)
    OP_71(0xA, 0x4)
    OP_71(0xB, 0x4)
    OP_71(0xC, 0x4)
    OP_71(0xD, 0x4)
    OP_71(0xE, 0x4)
    OP_71(0xF, 0x4)
    OP_71(0x10, 0x4)
    OP_6D(-31630, -180, 59850, 0)
    OP_67(0, 10310, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(156000, 0)
    OP_6E(628, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_22(0x77, 0x0, 0x64)
    OP_22(0x125, 0x0, 0x64)
    OP_72(0x2, 0x20)
    OP_6F(0x2, 0)
    OP_70(0x2, 0x96)

    def lambda_D017():
        OP_6D(-26030, 2970, 49440, 10000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_D017)

    def lambda_D02F():
        OP_67(0, 9640, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D02F)

    def lambda_D047():
        OP_6E(600, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D047)

    def lambda_D057():
        OP_6C(138000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_D057)

    def lambda_D067():
        OP_6B(6000, 10000)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_D067)
    OP_43(0x25, 0x0, 0x0, 0x13)
    PlayEffect(0x0, 0x0, 0xFF, -39070, -150, 58410, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_22(0xCC, 0x0, 0x64)
    OP_73(0x2)
    OP_72(0x2, 0x20)
    OP_6F(0x2, 150)
    OP_70(0x2, 0x14A)
    Sleep(1500)
    OP_22(0xDD, 0x0, 0x64)
    OP_74(0x11, 0x0, 0x1)
    Sleep(180)
    OP_74(0x11, 0x0, 0x2)
    Sleep(170)
    OP_22(0xDD, 0x0, 0x64)
    OP_74(0x11, 0x0, 0x3)
    Sleep(180)
    OP_74(0x11, 0x0, 0x4)
    Sleep(170)
    OP_22(0xDD, 0x0, 0x64)
    OP_74(0x11, 0x0, 0x5)
    Sleep(180)
    OP_74(0x11, 0x0, 0x6)
    Sleep(170)
    OP_74(0x11, 0x0, 0x7)
    OP_73(0x2)
    OP_71(0x2, 0x20)
    OP_B0(0x2, 0x3C)
    OP_6F(0x2, 330)
    OP_70(0x2, 0x1AE)

    def lambda_D159():
        OP_8C(0xFE, 180, 10)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_D159)

    def lambda_D167():
        OP_8C(0xFE, 180, 10)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_D167)
    Sleep(300)

    def lambda_D17A():
        OP_8C(0xFE, 180, 20)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_D17A)

    def lambda_D188():
        OP_8C(0xFE, 180, 20)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_D188)
    Sleep(200)

    def lambda_D19B():
        OP_8C(0xFE, 180, 30)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_D19B)

    def lambda_D1A9():
        OP_8C(0xFE, 180, 30)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_D1A9)
    Sleep(100)

    def lambda_D1BC():
        OP_8C(0xFE, 180, 40)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_D1BC)

    def lambda_D1CA():
        OP_8C(0xFE, 180, 40)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_D1CA)
    Sleep(1500)

    def lambda_D1DD():
        OP_8C(0xFE, 180, 30)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_D1DD)

    def lambda_D1EB():
        OP_8C(0xFE, 180, 30)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_D1EB)
    Sleep(500)

    def lambda_D1FE():
        OP_8C(0xFE, 180, 20)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_D1FE)

    def lambda_D20C():
        OP_8C(0xFE, 180, 20)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_D20C)
    WaitChrThread(0x25, 0x0)
    WaitChrThread(0x25, 0x2)
    WaitChrThread(0x26, 0x2)
    OP_82(0x0, 0x2)
    OP_23(0xCC)
    Sleep(1500)

    def lambda_D234():
        OP_6D(-35800, 0, 22420, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_D234)

    def lambda_D24C():
        OP_67(0, 6500, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D24C)

    def lambda_D264():
        OP_6E(469, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D264)

    def lambda_D274():
        OP_6C(174000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_D274)

    def lambda_D284():
        OP_6B(8000, 2000)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_D284)

    def lambda_D294():
        OP_8F(0xFE, 0xFFFF4A20, 0xC350, 0xFFFA87F6, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_D294)

    def lambda_D2AF():
        OP_8F(0xFE, 0xFFFF4A20, 0x1388, 0xFFFA87F6, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_D2AF)
    Sleep(50)

    def lambda_D2CF():
        OP_8F(0xFE, 0xFFFF4A20, 0xC350, 0xFFFA87F6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_D2CF)

    def lambda_D2EA():
        OP_8F(0xFE, 0xFFFF4A20, 0x1388, 0xFFFA87F6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_D2EA)
    Sleep(50)

    def lambda_D30A():
        OP_8F(0xFE, 0xFFFF4A20, 0xC350, 0xFFFA87F6, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_D30A)

    def lambda_D325():
        OP_8F(0xFE, 0xFFFF4A20, 0x1388, 0xFFFA87F6, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_D325)
    Sleep(50)

    def lambda_D345():
        OP_8F(0xFE, 0xFFFF4A20, 0xC350, 0xFFFA87F6, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_D345)

    def lambda_D360():
        OP_8F(0xFE, 0xFFFF4A20, 0x1388, 0xFFFA87F6, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_D360)
    Sleep(50)

    def lambda_D380():
        OP_8F(0xFE, 0xFFFF4A20, 0xC350, 0xFFFA87F6, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_D380)

    def lambda_D39B():
        OP_8F(0xFE, 0xFFFF4A20, 0x1388, 0xFFFA87F6, 0x38A4, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_D39B)
    Sleep(50)

    def lambda_D3BB():
        OP_8F(0xFE, 0xFFFF4A20, 0xEA60, 0xFFFA87F6, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_D3BB)

    def lambda_D3D6():
        OP_8F(0xFE, 0xFFFF4A20, 0x1388, 0xFFFA87F6, 0x5014, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_D3D6)
    Sleep(50)
    OP_24(0x125, 0x5A)
    OP_24(0x77, 0x5A)

    def lambda_D3FE():
        OP_8F(0xFE, 0xFFFF4A20, 0x11170, 0xFFFA87F6, 0x6D60, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_D3FE)

    def lambda_D419():
        OP_8F(0xFE, 0xFFFF4A20, 0x1388, 0xFFFA87F6, 0x6F54, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_D419)
    Sleep(50)

    def lambda_D439():
        OP_8F(0xFE, 0xFFFF4A20, 0x13880, 0xFFFA87F6, 0x88B8, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_D439)

    def lambda_D454():
        OP_8F(0xFE, 0xFFFF4A20, 0x1388, 0xFFFA87F6, 0x88B8, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_D454)
    Sleep(50)

    def lambda_D474():
        OP_8F(0xFE, 0xFFFF4A20, 0x15F90, 0xFFFA87F6, 0xAFC8, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_D474)

    def lambda_D48F():
        OP_8F(0xFE, 0xFFFF4A20, 0x1388, 0xFFFA87F6, 0xAFC8, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_D48F)
    Sleep(50)

    def lambda_D4AF():
        OP_8F(0xFE, 0xFFFF4A20, 0x186A0, 0xFFFA87F6, 0xC350, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_D4AF)

    def lambda_D4CA():
        OP_8F(0xFE, 0xFFFF4A20, 0x1388, 0xFFFA87F6, 0xC350, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_D4CA)
    Sleep(150)
    OP_24(0x125, 0x50)
    OP_24(0x77, 0x50)
    Sleep(300)
    OP_24(0x125, 0x46)
    OP_24(0x77, 0x46)
    Sleep(300)
    OP_24(0x125, 0x3C)
    OP_24(0x77, 0x3C)
    Sleep(300)
    OP_24(0x125, 0x32)
    OP_24(0x77, 0x32)
    FadeToDark(1000, 0, -1)
    Sleep(300)
    OP_24(0x125, 0x28)
    OP_24(0x77, 0x28)
    Sleep(300)
    OP_24(0x125, 0x1E)
    OP_24(0x77, 0x1E)
    Sleep(300)
    OP_24(0x125, 0x14)
    OP_24(0x77, 0x14)
    Sleep(300)
    OP_23(0x125)
    OP_23(0x77)
    OP_0D()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T1400   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_18_7523 end

    def Function_19_D55D(): pass

    label("Function_19_D55D")

    Sleep(1500)

    def lambda_D568():
        OP_8F(0xFE, 0xFFFF63C0, 0x1388, 0xFE38, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_D568)

    def lambda_D583():
        OP_8F(0xFE, 0xFFFF63C0, 0x4E20, 0xFE38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_D583)
    Sleep(700)

    def lambda_D5A3():
        OP_8F(0xFE, 0xFFFF63C0, 0x1388, 0xFE38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_D5A3)

    def lambda_D5BE():
        OP_8F(0xFE, 0xFFFF63C0, 0x4E20, 0xFE38, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_D5BE)
    Sleep(500)

    def lambda_D5DE():
        OP_8F(0xFE, 0xFFFF63C0, 0x4E20, 0xFE38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_D5DE)
    Sleep(300)

    def lambda_D5FE():
        OP_8F(0xFE, 0xFFFF63C0, 0x4E20, 0xFE38, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_D5FE)
    Sleep(1000)

    def lambda_D61E():
        OP_8F(0xFE, 0xFFFF63C0, 0x4E20, 0xFE38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_D61E)
    WaitChrThread(0x25, 0x1)
    WaitChrThread(0x26, 0x1)
    Return()

    # Function_19_D55D end

    def Function_20_D63E(): pass

    label("Function_20_D63E")

    OP_72(0x2, 0x20)
    OP_73(0x2)
    OP_6F(0x2, 430)
    OP_70(0x2, 0x258)
    Sleep(1000)
    OP_75(0xB, 0x0, 0x2)
    OP_22(0xDD, 0x0, 0x64)
    Sleep(240)
    OP_22(0xDD, 0x0, 0x64)
    Sleep(240)
    OP_22(0xDD, 0x0, 0x64)
    Sleep(240)
    OP_73(0x2)
    OP_6F(0x2, 600)
    OP_70(0x2, 0x320)
    OP_73(0x2)
    Return()

    # Function_20_D63E end

    def Function_21_D693(): pass

    label("Function_21_D693")

    Sleep(2600)
    OP_75(0xB, 0x0, 0x2)
    OP_74(0x11, 0x0, 0x6)
    Sleep(150)
    OP_74(0x11, 0x0, 0x5)
    Sleep(150)
    OP_74(0x11, 0x0, 0x4)
    Sleep(150)
    OP_74(0x11, 0x0, 0x3)
    Sleep(150)
    OP_74(0x11, 0x0, 0x2)
    Sleep(150)
    OP_74(0x11, 0x0, 0x1)
    Sleep(150)
    OP_74(0x11, 0x0, 0x0)
    Return()

    # Function_21_D693 end

    def Function_22_D6FD(): pass

    label("Function_22_D6FD")

    SetChrPos(0xFE, -2790, 20, 65540, 0)
    OP_8E(0xFE, 0xFFFFF51A, 0x14, 0x14E1A, 0x1388, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_22_D6FD end

    def Function_23_D72A(): pass

    label("Function_23_D72A")

    SetChrChipByIndex(0xFE, 17)
    SetChrPos(0xFE, -1370, 0, 65129, 0)
    OP_8E(0xFE, 0xFFFFFAA6, 0x28, 0x14E6A, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 4)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_23_D72A end

    def Function_24_D766(): pass

    label("Function_24_D766")

    SetChrPos(0xFE, -2950, 20, 63670, 0)
    OP_8E(0xFE, 0xFFFFF47A, 0xFFFFFFC4, 0x148CA, 0x1388, 0x0)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_24_D766 end

    def Function_25_D798(): pass

    label("Function_25_D798")

    SetChrChipByIndex(0xFE, 18)
    SetChrPos(0xFE, -1710, 30, 62720, 0)
    OP_8E(0xFE, 0xFFFFF952, 0x1E, 0x14834, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 0)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_25_D798 end

    def Function_26_D7D4(): pass

    label("Function_26_D7D4")

    SetChrChipByIndex(0xFE, 19)
    SetChrPos(0xFE, -520, 30, 61080, 0)
    OP_8E(0xFE, 0xFFFFFDF8, 0xFFFFFFF6, 0x1465E, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 1)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_26_D7D4 end

    def Function_27_D810(): pass

    label("Function_27_D810")

    SetChrChipByIndex(0xFE, 20)
    SetChrPos(0xFE, -860, 10, 62910, 0)
    OP_8E(0xFE, 0xFFFFFCA4, 0x0, 0x14B22, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 2)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_27_D810 end

    def Function_28_D84C(): pass

    label("Function_28_D84C")

    SetChrChipByIndex(0xFE, 21)
    SetChrPos(0xFE, -2670, 30, 60510, 0)
    OP_8E(0xFE, 0xFFFFF592, 0x1E, 0x142E4, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 3)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_28_D84C end

    def Function_29_D888(): pass

    label("Function_29_D888")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -1890, 40, 61000, 0)
    OP_8E(0xFE, 0xFFFFF89E, 0x28, 0x13D4E, 0xBB8, 0x0)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_29_D888 end

    def Function_30_D8BF(): pass

    label("Function_30_D8BF")


    def lambda_D8C5():
        OP_91(0xFE, 0x0, 0x0, 0xABE0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_D8C5)
    Sleep(160)

    def lambda_D8E5():
        OP_91(0xFE, 0x0, 0x0, 0xABE0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_D8E5)

    def lambda_D900():
        OP_91(0xFE, 0x0, 0x0, 0xABE0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_D900)
    Sleep(200)

    def lambda_D920():
        OP_91(0xFE, 0x0, 0x0, 0xABE0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_D920)

    def lambda_D93B():
        OP_91(0xFE, 0x0, 0x0, 0xABE0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_D93B)
    Sleep(180)

    def lambda_D95B():
        OP_91(0xFE, 0x0, 0x0, 0xABE0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_D95B)

    def lambda_D976():
        OP_91(0xFE, 0x0, 0x0, 0xABE0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_D976)
    Sleep(230)

    def lambda_D996():
        OP_91(0xFE, 0x0, 0x0, 0xABE0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_D996)

    def lambda_D9B1():
        OP_91(0xFE, 0x0, 0x0, 0xABE0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_D9B1)
    Sleep(150)

    def lambda_D9D1():
        OP_91(0xFE, 0x0, 0x0, 0xABE0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_D9D1)

    def lambda_D9EC():
        OP_91(0xFE, 0x0, 0x0, 0xABE0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_D9EC)
    Sleep(190)

    def lambda_DA0C():
        OP_91(0xFE, 0x0, 0x0, 0xABE0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_DA0C)

    def lambda_DA27():
        OP_91(0xFE, 0x0, 0x0, 0xABE0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_DA27)
    Sleep(220)

    def lambda_DA47():
        OP_91(0xFE, 0x0, 0x0, 0xABE0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_DA47)
    Return()

    # Function_30_D8BF end

    def Function_31_DA5D(): pass

    label("Function_31_DA5D")


    def lambda_DA63():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x3F, 1, lambda_DA63)

    def lambda_DA7E():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x41, 1, lambda_DA7E)
    Sleep(100)

    def lambda_DA9E():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x40, 1, lambda_DA9E)
    Sleep(80)

    def lambda_DABE():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x42, 1, lambda_DABE)

    def lambda_DAD9():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x44, 1, lambda_DAD9)
    Sleep(70)

    def lambda_DAF9():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x43, 1, lambda_DAF9)
    Sleep(30)

    def lambda_DB19():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x3D, 1, lambda_DB19)
    Sleep(90)

    def lambda_DB39():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x3A, 1, lambda_DB39)

    def lambda_DB54():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x3E, 1, lambda_DB54)

    def lambda_DB6F():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x3B, 1, lambda_DB6F)
    Sleep(40)

    def lambda_DB8F():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_DB8F)

    def lambda_DBAA():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x3C, 1, lambda_DBAA)
    Sleep(30)

    def lambda_DBCA():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_DBCA)

    def lambda_DBE5():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x36, 1, lambda_DBE5)
    Sleep(70)

    def lambda_DC05():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x35, 1, lambda_DC05)

    def lambda_DC20():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x37, 1, lambda_DC20)
    Sleep(40)

    def lambda_DC40():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x34, 1, lambda_DC40)

    def lambda_DC5B():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x38, 1, lambda_DC5B)

    def lambda_DC76():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x31, 1, lambda_DC76)
    Sleep(50)

    def lambda_DC96():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_DC96)

    def lambda_DCB1():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x30, 1, lambda_DCB1)
    Sleep(30)

    def lambda_DCD1():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2F, 1, lambda_DCD1)
    Sleep(100)

    def lambda_DCF1():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_DCF1)

    def lambda_DD0C():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x32, 1, lambda_DD0C)
    Sleep(30)

    def lambda_DD2C():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_DD2C)

    def lambda_DD47():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_DD47)
    Sleep(60)

    def lambda_DD67():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_DD67)

    def lambda_DD82():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_DD82)
    Sleep(70)

    def lambda_DDA2():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_DDA2)

    def lambda_DDBD():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_DDBD)
    Return()

    # Function_31_DA5D end

    def Function_32_DDD3(): pass

    label("Function_32_DDD3")


    def lambda_DDD9():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x5D, 1, lambda_DDD9)

    def lambda_DDF4():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x5F, 1, lambda_DDF4)
    Sleep(100)

    def lambda_DE14():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x5E, 1, lambda_DE14)
    Sleep(80)

    def lambda_DE34():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x60, 1, lambda_DE34)

    def lambda_DE4F():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x62, 1, lambda_DE4F)
    Sleep(70)

    def lambda_DE6F():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x61, 1, lambda_DE6F)
    Sleep(30)

    def lambda_DE8F():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x5B, 1, lambda_DE8F)
    Sleep(90)

    def lambda_DEAF():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x58, 1, lambda_DEAF)

    def lambda_DECA():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x5C, 1, lambda_DECA)

    def lambda_DEE5():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x59, 1, lambda_DEE5)
    Sleep(40)

    def lambda_DF05():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x57, 1, lambda_DF05)

    def lambda_DF20():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x5A, 1, lambda_DF20)
    Sleep(30)

    def lambda_DF40():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x51, 1, lambda_DF40)

    def lambda_DF5B():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x54, 1, lambda_DF5B)
    Sleep(70)

    def lambda_DF7B():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x53, 1, lambda_DF7B)

    def lambda_DF96():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x55, 1, lambda_DF96)
    Sleep(40)

    def lambda_DFB6():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x52, 1, lambda_DFB6)

    def lambda_DFD1():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x56, 1, lambda_DFD1)

    def lambda_DFEC():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x4F, 1, lambda_DFEC)
    Sleep(50)

    def lambda_E00C():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x4B, 1, lambda_E00C)

    def lambda_E027():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x4E, 1, lambda_E027)
    Sleep(30)

    def lambda_E047():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x4D, 1, lambda_E047)
    Sleep(100)

    def lambda_E067():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x4C, 1, lambda_E067)

    def lambda_E082():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x50, 1, lambda_E082)
    Sleep(30)

    def lambda_E0A2():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x4A, 1, lambda_E0A2)

    def lambda_E0BD():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x47, 1, lambda_E0BD)
    Sleep(60)

    def lambda_E0DD():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x45, 1, lambda_E0DD)

    def lambda_E0F8():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x48, 1, lambda_E0F8)
    Sleep(70)

    def lambda_E118():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x46, 1, lambda_E118)

    def lambda_E133():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x49, 1, lambda_E133)
    Return()

    # Function_32_DDD3 end

    def Function_33_E149(): pass

    label("Function_33_E149")


    def lambda_E14F():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x7B, 1, lambda_E14F)

    def lambda_E16A():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x7D, 1, lambda_E16A)
    Sleep(100)

    def lambda_E18A():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x7C, 1, lambda_E18A)
    Sleep(80)

    def lambda_E1AA():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x7E, 1, lambda_E1AA)

    def lambda_E1C5():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_E1C5)
    Sleep(70)

    def lambda_E1E5():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_E1E5)
    Sleep(30)

    def lambda_E205():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x79, 1, lambda_E205)
    Sleep(90)

    def lambda_E225():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x76, 1, lambda_E225)

    def lambda_E240():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x7A, 1, lambda_E240)

    def lambda_E25B():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x77, 1, lambda_E25B)
    Sleep(40)

    def lambda_E27B():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x75, 1, lambda_E27B)

    def lambda_E296():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x78, 1, lambda_E296)
    Sleep(30)

    def lambda_E2B6():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x6F, 1, lambda_E2B6)

    def lambda_E2D1():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x72, 1, lambda_E2D1)
    Sleep(70)

    def lambda_E2F1():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x71, 1, lambda_E2F1)

    def lambda_E30C():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x73, 1, lambda_E30C)
    Sleep(40)

    def lambda_E32C():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x70, 1, lambda_E32C)

    def lambda_E347():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x74, 1, lambda_E347)

    def lambda_E362():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x6D, 1, lambda_E362)
    Sleep(50)

    def lambda_E382():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x69, 1, lambda_E382)

    def lambda_E39D():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x6C, 1, lambda_E39D)
    Sleep(30)

    def lambda_E3BD():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x6B, 1, lambda_E3BD)
    Sleep(100)

    def lambda_E3DD():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x6A, 1, lambda_E3DD)

    def lambda_E3F8():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x6E, 1, lambda_E3F8)
    Sleep(30)

    def lambda_E418():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x68, 1, lambda_E418)

    def lambda_E433():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x65, 1, lambda_E433)
    Sleep(60)

    def lambda_E453():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x63, 1, lambda_E453)

    def lambda_E46E():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x66, 1, lambda_E46E)
    Sleep(70)

    def lambda_E48E():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x64, 1, lambda_E48E)

    def lambda_E4A9():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x67, 1, lambda_E4A9)
    Return()

    # Function_33_E149 end

    def Function_34_E4BF(): pass

    label("Function_34_E4BF")

    OP_24(0x10F, 0x5F)
    OP_24(0x110, 0x5A)
    Sleep(350)
    OP_24(0x10F, 0x5A)
    OP_24(0x110, 0x55)
    Sleep(350)
    OP_24(0x10F, 0x55)
    OP_24(0x110, 0x50)
    Sleep(350)
    OP_24(0x10F, 0x50)
    OP_24(0x110, 0x4B)
    Sleep(350)
    OP_24(0x10F, 0x4B)
    OP_24(0x110, 0x46)
    Sleep(350)
    OP_24(0x10F, 0x46)
    OP_24(0x110, 0x41)
    Sleep(350)
    OP_24(0x10F, 0x41)
    OP_24(0x110, 0x3C)
    Sleep(350)
    OP_24(0x10F, 0x3C)
    OP_24(0x110, 0x37)
    Sleep(350)
    OP_24(0x10F, 0x37)
    OP_24(0x110, 0x32)
    Sleep(350)
    OP_24(0x10F, 0x32)
    OP_24(0x110, 0x2D)
    Sleep(350)
    OP_24(0x10F, 0x2D)
    OP_24(0x110, 0x28)
    Sleep(350)
    OP_24(0x10F, 0x28)
    OP_24(0x110, 0x23)
    Sleep(350)
    OP_24(0x10F, 0x23)
    OP_24(0x110, 0x1E)
    Sleep(350)
    OP_23(0x10F)
    OP_23(0x110)
    Return()

    # Function_34_E4BF end

    SaveToFile()

Try(main)
