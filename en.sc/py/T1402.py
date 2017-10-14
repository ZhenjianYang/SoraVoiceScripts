from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

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
            'ED6_DT21/T1402   ._SN',
            'ED6_DT21/T1402_1 ._SN',
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
        'Scherazard',                           # 9
        'Agate',                                # 10
        'Tita',                                 # 11
        'Zin',                                  # 12
        'Princess Klaudia',                     # 13
        'Prince Olivert',                       # 14
        'Lt. General Vander',                   # 15
        'General Morgan',                       # 16
        'Major Vander',                         # 17
        'Cassius',                              # 18
        'Professor Russell',                    # 19
        'Captain Schwarz',                      # 20
        'Father Kevin',                         # 21
        '王国軍将校',                           # 22
        '王国軍将校',                           # 23
        '蒸気戦車',                             # 24
        '蒸気戦車',                             # 25
        '蒸気戦車',                             # 26
        '蒸気戦車',                             # 27
        '蒸気戦車',                             # 28
        '蒸気戦車',                             # 29
        '蒸気戦車',                             # 30
        '蒸気戦車',                             # 31
        '蒸気戦車',                             # 32
        '蒸気戦車',                             # 33
        '蒸気戦車',                             # 34
        '蒸気戦車',                             # 35
        '蒸気戦車',                             # 36
        '蒸気戦車',                             # 37
        '飛行挺',                               # 38
        '飛行挺の影',                           # 39
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
        "Function_3_7B84",         # 03, 3
        "Function_4_7BBE",         # 04, 4
        "Function_5_7BE4",         # 05, 5
        "Function_6_7C0A",         # 06, 6
        "Function_7_7C30",         # 07, 7
        "Function_8_7C56",         # 08, 8
        "Function_9_7C7C",         # 09, 9
        "Function_10_7CA2",        # 0A, 10
        "Function_11_7CBE",        # 0B, 11
        "Function_12_7CDF",        # 0C, 12
        "Function_13_7CFB",        # 0D, 13
        "Function_14_7D1C",        # 0E, 14
        "Function_15_7F4C",        # 0F, 15
        "Function_16_82C7",        # 10, 16
        "Function_17_8642",        # 11, 17
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
    Event(1, 2)

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
    OP_DB()
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
    OP_DE("Haken Gate")
    FadeToBright(1000, 0)

    def lambda_2A3D():
        OP_6D(-3610, -30, 118060, 9000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2A3D)
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

    def lambda_30D7():
        OP_8E(0xFE, 0xFFFFF8DA, 0x32, 0x17606, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_30D7)
    SetChrPos(0x27, -2870, -20, 116520, 180)
    SetChrPos(0x28, -1230, 30, 116650, 180)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x27, 0x200)
    ClearChrFlags(0x28, 0x200)

    def lambda_3128():
        OP_8E(0xFE, 0xFFFFF52E, 0x32, 0x17F66, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_3128)

    def lambda_3143():
        OP_8E(0xFE, 0xFFFFFC86, 0x0, 0x17F66, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_3143)
    OP_0D()

    def lambda_315F():
        OP_6D(20, 20, 49800, 10000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_315F)

    def lambda_3177():
        OP_67(0, 3950, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3177)

    def lambda_318F():
        OP_6B(3000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_318F)

    def lambda_319F():
        OP_6C(141000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_319F)
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
    OP_DC()

    ChrTalk(    #0
        0xF,
        (
            "#162F#5PExplain yourself, General Vander!\x02\x03",

            "Why is a division of the Imperial\x01",
            "Army on our literal doorstep?!\x02\x03",

            "Does the Empire truly forget\x01",
            "the pacts it signs so quickly?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xE,
        (
            "#882F#6PGeneral Morgan.\x01",
            "I'm the one who would like an explanation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xF,
        "#161F#5PWhat are you--\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xE,
        (
            "#884F#6PFor the past 24 hours or more, orbments all\x01",
            "across the southern marches of His Majesty's\x01",
            "domain have ceased function.\x02\x03",

            "And, at the exact same time, it seems\x01",
            "a massive, heretofore unknown structure\x01",
            "appeared above your Valleria Lake.\x02\x03",

            "#880FNow I ask you, Morgan:\x01",
            "what is going on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xF,
        (
            "#166F#5PIt is...just as you say.\x02\x03",

            "We are as confused as anyone\x01",
            "else about the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xE,
        (
            "#884F#6PSo it would seem.\x02\x03",

            "#882FBut your 'situation' is, as I said,\x01",
            "affecting a large swathe of Imperial\x01",
            "territory.\x02\x03",

            "Given that...you know full well why\x01",
            "I'm here, General.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xF,
        (
            "#160F#5PHrmph. Here to try and raise the Stallion\x01",
            "above us while we're weak, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xE,
        (
            "#884F#6PWe intend nothing of the sort.\x02\x03",

            "#881FWe are given to understanding that a criminal\x01",
            "organization of some sort has been taking\x01",
            "advantage of this situation.\x02\x03",

            "All we wish is to see if we can be\x01",
            "of aid to the allies whom we have\x01",
            "signed a non-aggression pact with.\x02\x03",

            "Those are the orders I received from\x01",
            "the Imperial government.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xF,
        (
            "#162F#5PNonsense!\x01",
            "What are those tanks doing here, then?!\x02\x03",

            "I've never heard of a tank that runs\x01",
            "on steam and combustion until now!\x02\x03",

            "How is it that you suddenly have these\x01",
            "tanks which CONVENIENTLY require no\x01",
            "orbal power?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xE,
        (
            "#884F#6PThat...is a military secret.\x02\x03",

            "#881FI would think you would welcome us, though,\x01",
            "Morgan. These vehicles are perfectly\x01",
            "suited for helping to keep the peace.\x02\x03",

            "In Liberl, that is, while this...crisis runs\x01",
            "its course. You understand my meaning, yes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xF,
        "#166F#5PGh...\x02",
    )

    CloseMessageWindow()
    SetChrPos(0xC, -800, 0, 82000, 0)

    NpcTalk(    #11
        0xC,
        "Girl's Voice",
        "#5PWe deeply appreciate your thoughtfulness.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xF,
        "#161F#5PWhat...?!\x02",
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

    def lambda_3B8C():
        OP_91(0xFE, 0x0, 0x0, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_3B8C)

    def lambda_3BA7():
        OP_91(0xFE, 0x0, 0x0, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3BA7)

    def lambda_3BC2():
        OP_91(0xFE, 0x0, 0x0, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3BC2)

    def lambda_3BDD():
        OP_91(0xFE, 0x0, 0x0, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3BDD)

    def lambda_3BF8():
        OP_91(0xFE, 0x0, 0x0, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3BF8)

    def lambda_3C13():
        OP_91(0xFE, 0x0, 0x0, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3C13)

    def lambda_3C2E():
        OP_91(0xFE, 0x0, 0x0, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3C2E)

    def lambda_3C49():

        label("loc_3C49")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_3C49")

    QueueWorkItem2(0xF, 1, lambda_3C49)
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
            "#161F#2PImpossible!\x02\x03",

            "(Y-Your Highness! What are you--)\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3D54():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_3D54)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x200, 0x4B, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x200, 0xFFFFFF, 0x0, "C_VIS224._CH")
    OP_C6(0x0, 0x0, 55000, 50000, 0)
    OP_C6(0x0, 0x0, 105000, 50000, 500)
    OP_C6(0x0, 0x3, -1, 1000, 0)
    Sleep(1000)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("Princess Klaudia")

    AnonymousTalk(    #14
        (
            "(Morgan, well done.)\x02\x03",

            "(Please, leave the rest of this to me.)\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("General Morgan")

    AnonymousTalk(    #15
        "#161F(But, Your Highness...)\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, 16777215, 250, 0)
    OP_44(0xF, 0x1)
    OP_8C(0xF, 180, 400)
    Sleep(300)

    ChrTalk(    #16
        0xF,
        "#162F#5P(And what are THEY doing here?!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x101,
        (
            "#1006F#4P(WE are the royal bodyguards!\x01",
            "Sorta. Temporarily.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x102,
        (
            "#1040F#4P(Should the worst happen, we'll\x01",
            "protect Kloe... Klaudia. We swear.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xF,
        "#160F#5P(Mmmph...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xC,
        (
            "#1167F#1P(I may be inexperienced as a negotiator...)\x02\x03",

            "#1162F(This is, however, the proper\x01",
            "time for me to step forward and\x01",
            "assume my duties as heir.)\x02\x03",

            "(Morgan...please.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xF,
        "#163F#5P(...As you wish, Your Highness.)\x02",
    )

    CloseMessageWindow()
    OP_8C(0xF, 90, 400)
    Sleep(300)

    ChrTalk(    #22
        0xF,
        (
            "#166F#2P(Just...keep in mind who you are going out\x01",
            "there to parley with, my princess.)\x02\x03",

            "(If anything happens, be ready\x01",
            "to run for the gate.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xC,
        "#1168F#1P(I understand.)\x02",
    )

    CloseMessageWindow()
    OP_8C(0xC, 0, 400)
    Sleep(500)

    def lambda_40F5():

        label("loc_40F5")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_40F5")

    QueueWorkItem2(0xF, 1, lambda_40F5)

    def lambda_4106():
        OP_6D(-380, 80, 55800, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4106)

    def lambda_411E():
        OP_67(0, 5920, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_411E)

    def lambda_4136():
        OP_6B(2120, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4136)

    def lambda_4146():
        OP_6C(32000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4146)

    def lambda_4156():
        OP_6E(414, 3000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_4156)
    OP_8E(0xC, 0xFFFFFCD6, 0xA, 0xD764, 0x5DC, 0x0)
    WaitChrThread(0x101, 0x0)
    OP_44(0xF, 0x1)

    def lambda_4183():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_4183)

    def lambda_4191():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_4191)
    OP_8C(0x16, 0, 400)
    SetChrPos(0xE, -1230, 60, 73610, 180)
    SetChrFlags(0xE, 0x80)

    ChrTalk(    #24
        0xE,
        (
            "#880FIt seems I will be trading words\x01",
            "with someone else now, hmm?\x02\x03",

            "I'm afraid I don't recognize you,\x01",
            "though your bearing is quite noble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xC,
        (
            "#1167F#4PThis is the first time we have met, sir.\x02\x03",

            "#1162FI am Klaudia von Auslese, princess of Liberl,\x01",
            "granddaughter to the queen...\x02\x03",

            "...and newly-invested heir to the throne.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xE,
        (
            "#883F#3S(Gah!)#2S\x02\x03",

            "F-Forgive my impertinence, Your Highness!\x02\x03",

            "#882FI am Zechs Vander, Your Highness.\x02\x03",

            "Lieutenant general of the 3rd division\x01",
            "of the Imperial Army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xC,
        (
            "#1160F#4PYes, word of your accomplishments\x01",
            "in battle has reached even us, General\x01",
            "Vander.\x02",
        )
    )

    CloseMessageWindow()
    OP_6D(-190, 20, 50280, 1500)

    ChrTalk(    #28
        0x101,
        "#1015F#5P(Hey, is that guy famous?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x102,
        (
            "#1042F#2P(Yes, that's 'One-Eyed Zechs.' He's one of\x01",
            "the best field commanders Erebonia has.)\x02",
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
            "#883F#6PIf I may be so bold, Your Highness,\x01",
            "I have actually seen pictures of you before.\x02\x03",

            "Have you cut your hair recently?\x01",
            "Now that I look, your face is familiar, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xC,
        (
            "#1165F#5PHaha, ah, this is a bit embarrassing...\x01",
            "I, ah, cut it for the investiture ceremony.\x02\x03",

            "#1382FConsider it a little girl's way of\x01",
            "showing her resolve to take up\x01",
            "a burden too heavy for her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xE,
        (
            "#884F#6PHardly, Princess Klaudia.\x01",
            "It looks very good on you--if I may be forward.\x02\x03",

            "#881FAllow this servant of the Empire to congratulate\x01",
            "you on becoming the heir to the throne.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xC,
        "#1168F#5PThank you, General.\x02",
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
            "#882F#5PWell, then...what brings the\x01",
            "princess of Liberl here?\x02\x03",

            "Are you here to raise protest against\x01",
            "us like my good colleague Morgan?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xC,
        (
            "#1167F#6PNo, that is not my intent.\x02\x03",

            "I am sure that our neighbors in Erebonia\x01",
            "must be terrified at the moment.\x02\x03",

            "#1169FThe darkness at night, the cold, the\x01",
            "complete shutdown of communications...\x02\x03",

            "Believe me, I know how any one of\x01",
            "these could inspire terror in people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xE,
        "#880F#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xC,
        (
            "#1162F#6PWhat I ask is for you to consider your actions.\x02\x03",

            "Consider what would happen if your\x01",
            "forces were to enter our country.\x02\x03",

            "#1167FYou say that large portions of the Empire\x01",
            "are disordered at the moment. I assure\x01",
            "you, in every part of Liberl, it is worse.\x02\x03",

            "And while we no longer bear Erebonia ill will,\x01",
            "many of our citizens are agitated and afraid.\x02\x03",

            "#1163FI could not bear it if the good intentions\x01",
            "of our allies were misunderstood.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xE,
        "#883F#5PEr, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xC,
        (
            "#1160F#6PAs you can see, we are investigating these\x01",
            "strange events as quickly as we are able.\x02\x03",

            "Furthermore, we have managed to suppress\x01",
            "most of the activities of the aforementioned\x01",
            "criminal group on our own.\x02\x03",

            "#1167FAnd so I ask, for the sake of continued\x01",
            "friendship between Erebonia and Liberl,\x01",
            "a relationship we value highly.\x02\x03",

            "#1162FGive us a little more time, General.\x01",
            "We will make this right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xE,
        "#884F#5PMmm...\x02",
    )

    CloseMessageWindow()
    SetChrPos(0xD, -1200, 0, 67260, 180)

    NpcTalk(    #41
        0xD,
        "Young Man's Voice",
        (
            "#5PPretty words. But they are, alas, sound\x01",
            "and fury. Signifying nothing.\x02",
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

    def lambda_4E6D():
        OP_8E(0xFE, 0xFFFFF8B2, 0xA, 0x19014, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4E6D)

    def lambda_4E88():
        OP_8E(0xFE, 0xFFFFF542, 0x1E, 0x19528, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4E88)
    OP_0D()

    def lambda_4EA4():
        OP_6D(-2000, 100, 103900, 6000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4EA4)

    def lambda_4EBC():
        OP_67(0, 3090, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4EBC)

    def lambda_4ED4():
        OP_6B(2760, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4ED4)

    def lambda_4EE4():
        OP_6E(340, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4EE4)
    OP_8C(0xE, 0, 400)
    OP_8C(0x27, 0, 400)
    OP_8C(0x28, 0, 400)
    Sleep(2000)
    OP_43(0x27, 0x0, 0x0, 0xC)
    OP_43(0x28, 0x0, 0x0, 0xD)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #42
        0xE,
        "#883F#5PYour Highness...\x02",
    )

    CloseMessageWindow()
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x200, 0x4B, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x200, 0xFFFFFF, 0x0, "C_VIS223._CH")
    OP_C6(0x1, 0x0, 70000, 50000, 0)
    OP_C6(0x1, 0x0, 120000, 50000, 500)
    OP_C6(0x1, 0x3, -1, 1000, 0)
    Sleep(1200)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("Young Man in Uniform")

    AnonymousTalk(    #43
        (
            "I shall take the reins.\x02\x03",

            "You are relieved, General.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("Lt. General Vander")

    AnonymousTalk(    #44
        "#884FAs you wish, Your Highness.\x02",
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
        "#1020F#6PWha...? Wha...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x8,
        "#023F#4PHe can't be...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x9,
        "#055F#4PYou have got to be SHITTING me.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(-20, 10, 101410, 0)
    OP_67(0, 4580, -10000, 0)
    OP_6B(3350, 0)
    OP_6C(44000, 0)
    OP_6E(299, 0)

    def lambda_51A8():
        OP_6D(-990, 20, 95740, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_51A8)

    def lambda_51C0():
        OP_6B(2890, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_51C0)

    def lambda_51D0():
        OP_8E(0xFE, 0xFFFFF876, 0x32, 0x171F6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_51D0)
    Sleep(200)

    def lambda_51F0():
        OP_8E(0xFE, 0xFFFFFA24, 0x14, 0x17B38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_51F0)
    Sleep(500)
    OP_8C(0xE, 90, 400)

    def lambda_5217():
        OP_8F(0xFE, 0xFFFFF2CC, 0xFFFFFFD8, 0x17692, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5217)
    WaitChrThread(0xD, 0x1)
    WaitChrThread(0xE, 0x1)
    OP_8C(0xE, 180, 400)
    WaitChrThread(0x10, 0x1)
    WaitChrThread(0x101, 0x0)
    OP_8C(0x27, 180, 400)
    OP_8C(0x28, 180, 400)

    NpcTalk(    #48
        0xD,
        "Young Man in Uniform",
        (
            "#894F#6PI believe this is our first formal\x01",
            "acquaintance, Princess Klaudia.\x02\x03",

            "#895FI am Olivert Reise Arnor, a son of\x01",
            "His Majesty, Emperor Eugent III.\x02",
        )
    )

    CloseMessageWindow()
    OP_C6(0x0, 0x6, 0, 0, 0)
    OP_C6(0x1, 0x6, 0, 0, 0)
    SetChrPos(0x101, -5000, 10, 85000, 0)
    SetChrPos(0x8, -5000, 10, 85000, 0)

    ChrTalk(    #49
        0x101,
        (
            "#1020F#1PWHA...?!?!...\x02\x03",

            "#1005F(One of the sons of...\x01",
            "He's an IMPERIAL PRINCE?!)\x02\x03",

            "(Schera, did you know about this?!)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x8,
        (
            "#023F#1P(You're KIDDING, right?!)\x02\x03",

            "#025F(I thought he was just some sort of\x01",
            "agent for Imperial Intelligence!)\x02",
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
            "#1164F#5POlivert Reise Arnor...? I recognize\x01",
            "the name, but I don't know the man...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xD,
        (
            "#891F#6PHahaha. Even though I am a 'prince,'\x01",
            "I am little more than a royal bastard.\x02\x03",

            "I rarely attend to public matters of state,\x01",
            "so I am unsurprised you do not know my face.\x02\x03",

            "#895FIt does still sting a little, though, I fear.\x02\x03",

            "For the lovely girl who was once to be\x01",
            "my bride to not even know my face.\x01",
            "An arrow, my heart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        (
            "#1020F#5PWha...?\x02\x03",

            "#1019F(There are no other words.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x102,
        (
            "#1043F#2P(I see. That's what Colonel Richard\x01",
            "had in mind a while back.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xC,
        (
            "#1163F#5PI am sorry, I was unaware.\x02\x03",

            "#1167FAllow me to apologize for\x01",
            "the slight against you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xD,
        (
            "#894F#6PWell, I do understand it was conducted\x01",
            "without the queen's consent.\x02\x03",

            "That sort of slight we can overlook...\x02\x03",

            "#896FBut this?\x01",
            "No, Erebonia cannot overlook this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xC,
        "#1163F#5P...Oh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xD,
        (
            "#896F#6PMy enchanting princess.\x02\x03",

            "Are you aware, I wonder, of a little rumor\x01",
            "making its rounds across our great Empire?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xC,
        "#1169F#5PI don't believe I am...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xD,
        (
            "#899F#6PAllow me to tell you, then.\x02\x03",

            "#897FRumor has it that immense structure\x01",
            "in the distance is Liberl's new weapon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xC,
        "#1164F#5P#3SWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xD,
        (
            "#899F#6P'Liberl has developed a groundbreaking\x01",
            "new weapon that allows them to stop orbal\x01",
            "energy.'\x02\x03",

            "'They intend to use it to make us pay for\x01",
            "the war ten years ago.''\x02\x03",

            "#897FIt is a rumor which finds fertile ground in\x01",
            "the ears of our citizens. And leadership.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xC,
        (
            "#1163F#5PIt... It can't be...\x02\x03",

            "#1166FThat's absolutely untrue!\x01",
            "We would NEVER--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xD,
        (
            "#896F#6PThen you can prove it, yes?\x01",
            "Prove that it is a misunderstanding?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xC,
        "#1169F#5PErm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xD,
        (
            "#899F#6PIf you cannot, then we must act upon\x01",
            "the evidence of our senses.\x02\x03",

            "Indeed, if the rumors are true, this is a\x01",
            "monstrous betrayal of all civilization.\x01",
            "Using the pact to hide your intentions...\x02\x03",

            "#896FHeh heh... What choice would we have, then,\x01",
            "but to be defenders of the free world?\x02",
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
        (
            "#1005F#4P#4SOkay. What in the HELL is\x01",
            "this, Olivier?!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_5D44():

        label("loc_5D44")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_5D44")

    QueueWorkItem2(0x102, 1, lambda_5D44)
    Sleep(50)

    def lambda_5D5A():

        label("loc_5D5A")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_5D5A")

    QueueWorkItem2(0xC, 1, lambda_5D5A)
    Sleep(50)

    def lambda_5D70():

        label("loc_5D70")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_5D70")

    QueueWorkItem2(0x9, 1, lambda_5D70)
    Sleep(50)

    def lambda_5D86():

        label("loc_5D86")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_5D86")

    QueueWorkItem2(0xA, 1, lambda_5D86)
    Sleep(50)

    def lambda_5D9C():

        label("loc_5D9C")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_5D9C")

    QueueWorkItem2(0xF, 1, lambda_5D9C)

    ChrTalk(    #68
        0x102,
        "#1044F#6PEstelle!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xA,
        "#065F#6PE-Estelle...!\x02",
    )

    CloseMessageWindow()

    def lambda_5DDF():
        OP_6D(-1800, 50, 54200, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5DDF)

    def lambda_5DF7():
        OP_6B(2950, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5DF7)
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
            "#1005F#4PI can't just stand here, listening to\x01",
            "you blather on as you please!\x02\x03",

            "Olivier, you know DAMN WELL\x01",
            "just what's going on here!\x02\x03",

            "Why are you being such a jerk?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xC,
        "#1163F#6PEstelle, wait...\x02",
    )

    CloseMessageWindow()
    SetChrPos(0xD, -5500, 20, 67000, 180)

    ChrTalk(    #72
        0xD,
        (
            "#897F#2PHave we...met?\x02\x03",

            "You seem to know me, even if you\x01",
            "did not get the name quite right.\x01",
            "Did we meet at a party once?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x101,
        "#1004F#4PHuh?!\x02",
    )

    CloseMessageWindow()
    OP_8C(0xC, 0, 400)

    ChrTalk(    #74
        0xD,
        (
            "#890F#2PMmm. No, you lack the refinement of nobility.\x02\x03",

            "Yes, no matter how I look at you, you\x01",
            "must be nothing more than a commoner.\x02\x03",

            "#891FSo, who are you?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #75
        0x101,
        (
            "#1019F#4P...Okay. Fine then.\x01",
            "You wanna play dumb no matter what?\x02\x03",

            "You aren't the only one who\x01",
            "can bust out a surprise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xD,
        "#895F#2POh...?\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_64E3")

    ChrTalk(    #77
        0x101,
        (
            "#1005F#4PMY NAME is Estelle Bright!\x01",
            "I am a bona fide A-rank bracer of the\x01",
            "Bracer Guild of Liberl!\x02\x03",

            "In accordance with the laws of the guild...\x02\x03",

            "I am involving myself in this dispute\x01",
            "as a neutral arbitrator!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_8C(0xC, 270, 400)

    ChrTalk(    #78
        0xC,
        "#1164F#6PEstelle...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xD,
        (
            "#898F#2POh! An A-rank bracer...\x02\x03",

            "#891F(...Haha, ah!\x01",
            "Not a whit less than I expected.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x101,
        "#1004F#4PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xD,
        (
            "#899F#2PAh, pardon me.\x02\x03",

            "#897FFrom what I understand, A-rank bracers are\x01",
            "among the most capable bracers alive.\x02\x03",

            "You will forgive me, but I find it a little\x01",
            "difficult to believe that a young girl such\x01",
            "as yourself could hold that rank.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x101,
        (
            "#1006F#4PThen you're welcome to inquire with the guild\x01",
            "headquarters in Leman to confirm it.\x02\x03",

            "I think you'd have to halt negotiations while you\x01",
            "check, though, right? And with no working phones\x01",
            "for how many selge? What a pain that'll be!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xD,
        (
            "#895F#2PHeh... Very well.\x02\x03",

            "#896FSo what do you intend to do about our\x01",
            "little situation, 'neutral arbitrator'?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E73")

    label("loc_64E3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_6758")

    ChrTalk(    #84
        0x101,
        (
            "#1005F#4PMY NAME is Estelle Bright!\x01",
            "I am a B-rank bracer of the\x01",
            "Bracer Guild of Liberl!\x02\x03",

            "In accordance with the laws of the guild...\x02\x03",

            "I am involving myself in this dispute\x01",
            "as a neutral arbitrator!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_8C(0xC, 270, 400)

    ChrTalk(    #85
        0xC,
        "#1164F#6PEstelle...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xD,
        (
            "#898F#2PAh, I see, you're a bracer.\x02\x03",

            "#895FMmm, B-rank... That would make you\x01",
            "a veteran bracer who could be trusted\x01",
            "with an arbitration of this scope, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x101,
        (
            "#1002F#4PTrying to say you can't trust\x01",
            "a bracer's word, 'Prince Olivert'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xD,
        (
            "#894F#2PNot at all, forgive me.\x02\x03",

            "#896FSo what do you intend to do about our\x01",
            "little situation, 'neutral arbitrator'?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E73")

    label("loc_6758")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_6920")

    ChrTalk(    #89
        0x101,
        (
            "#1005F#4PMY NAME is Estelle Bright!\x01",
            "I am a C-rank bracer of the\x01",
            "Bracer Guild of Liberl!\x02\x03",

            "In accordance with the laws of the guild...\x02\x03",

            "I am involving myself in this dispute\x01",
            "as a neutral arbitrator!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_8C(0xC, 270, 400)

    ChrTalk(    #90
        0xC,
        "#1164F#6PEstelle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xD,
        (
            "#895F#2PAh, I see, you're a bracer.\x02\x03",

            "#894FC-rank means you are a bracer\x01",
            "of some standing. Very well.\x02\x03",

            "#896FSo what do you intend to do about our\x01",
            "little situation, 'neutral arbitrator'?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E73")

    label("loc_6920")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_6BAE")

    ChrTalk(    #92
        0x101,
        (
            "#1005F#4PMY NAME is Estelle Bright!\x01",
            "I am a bona fide D-rank bracer of the\x01",
            "Bracer Guild of Liberl!\x02\x03",

            "In accordance with the laws of the guild...\x02\x03",

            "I am involving myself in this dispute\x01",
            "as a neutral arbitrator!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_8C(0xC, 270, 400)

    ChrTalk(    #93
        0xC,
        "#1164F#6PAh, Estelle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xD,
        (
            "#895F#2PAh, I see, you're a bracer.\x02\x03",

            "#894FHmm... Unless I am mistaken, the guild\x01",
            "possesses seven ranks, G to A, does it not?\x02\x03",

            "#896FHow much trust can a mid-rank Liberlian\x01",
            "bracer really be given here, I wonder?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x101,
        "#1026F#4PEr, well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xD,
        (
            "#890F#2PNonetheless, I will permit you\x01",
            "to speak.\x02\x03",

            "So what do you intend to do about our\x01",
            "little situation, 'neutral arbitrator'?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E73")

    label("loc_6BAE")


    ChrTalk(    #97
        0x101,
        (
            "#1005F#4PMY NAME is Estelle Bright!\x01",
            "I am an E-rank bracer of the\x01",
            "Bracer Guild of Liberl!\x02\x03",

            "In accordance with the laws of the guild...\x02\x03",

            "I am involving myself in this dispute\x01",
            "as a neutral arbitrator!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_8C(0xC, 270, 400)

    ChrTalk(    #98
        0xC,
        "#1164F#6PErm, Estelle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xD,
        (
            "#898F#2PAh, I see, you're a bracer.\x02\x03",

            "#895FHmm... Unless I am mistaken, the guild\x01",
            "possesses seven ranks, G to A, does it not?\x02\x03",

            "How does someone who cannot even\x01",
            "claim middle rank in the guild intend to\x01",
            "'arbitrate' this situation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x101,
        (
            "#1019F#4PEr. Well. I'll arbitrate. Stuff.\x01",
            "You know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xD,
        (
            "#891F#2PI suppose I can respect courage, if\x01",
            "nothing else. You may speak.\x02\x03",

            "#895FSo what do you intend to do about our\x01",
            "little situation, 'neutral arbitrator'?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6E73")

    OP_8C(0xC, 0, 400)

    ChrTalk(    #102
        0x101,
        (
            "#1005F#4PFrom the evidence, I judge that Erebonia's\x01",
            "claim is false; the floating city is NOT\x01",
            "a Liberlian weapon!\x02\x03",

            "I swear it on the honor of the\x01",
            "Bracer Guild's supporting gauntlet!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xD,
        (
            "#895F#2POh! On the honor of the guild's emblem itself.\x01",
            "A bold statement.\x02\x03",

            "#899FCertainly, a statement from the Bracer Guild\x01",
            "holds enough weight that it cannot be ignored\x01",
            "outright. However...\x02\x03",

            "#897FI shall pose the same question to you, then,\x01",
            "Miss Bright. What is your evidence of\x01",
            "this claim?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x101,
        (
            "#1007F#4P'Evidence'?\x01",
            "What we've seen for ourselves!\x02\x03",

            "#1002FThe group which made the floating city appear is\x01",
            "the criminal Society of Ouroboros, which is still\x01",
            "operating in Liberl!\x02\x03",

            "We of the guild have been cooperating with the\x01",
            "Royal Army to try and put a stop to the society's\x01",
            "operations.\x02\x03",

            "#1006FHeck, if you like, we can have records of\x01",
            "everything forwarded to the Imperial government.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xD,
        (
            "#894F#2PHmmmm...\x02\x03",

            "That would certainly satisfy our need\x01",
            "for evidence against Liberl's possible\x01",
            "malfeasance. However...\x02\x03",

            "#896FYou have, I think, missed a key\x01",
            "point, Miss Bright.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x101,
        "#1026F#4PHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xD,
        (
            "#897F#2PAssuming, then, that the perpetrators\x01",
            "are this 'Society of Ouroboros'...\x02\x03",

            "Are Liberl and the guild capable of\x01",
            "putting a stop to this crisis?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #108
        0x101,
        "#1003F#4PEr, well, we...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xD,
        (
            "#895F#2PIf you do not, then the Empire will\x01",
            "not sit here wringing its hands.\x02\x03",

            "The weaponry we have brought,\x01",
            "including the cannons of our tanks,\x01",
            "all use gunpowder.\x02\x03",

            "Would that not be perfect for laying\x01",
            "siege to, and destroying, this little\x01",
            "'rogue city' of yours?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x101,
        (
            "#1020F#4PYou've got to be joking!\x02\x03",

            "What'll cannons do against\x01",
            "something that big?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xD,
        (
            "#896F#2PHeh... You never know until\x01",
            "you try, Miss Bright.\x02\x03",

            "#894FRegardless...I can say one thing\x01",
            "for sure.\x02\x03",

            "#897FYou do not have the ability to\x01",
            "put a stop to our...'goodwill.'\x01",
            "Or our need to defend ourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x101,
        "#1003F#4PGh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xC,
        (
            "#1162F#6P...\x02\x03",

            "#1167FWell, then, Prince Olivert.\x01",
            "Would action satisfy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xD,
        "#898F#2PHm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xC,
        (
            "#1162F#6PIf we can prove that we can, even in\x01",
            "these circumstances, do something\x01",
            "about that city...\x02\x03",

            "Would you give us the time to do so?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xD,
        (
            "#899F#2PHmmm. Well.\x02\x03",

            "#895FI suppose that for some time, at least,\x01",
            "civility would force our hand, hmm?\x02",
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
        "#883F#6P(My prince?!)\x02",
    )

    CloseMessageWindow()
    OP_8C(0xD, 270, 400)
    Sleep(300)

    ChrTalk(    #118
        0xD,
        (
            "#896F#4P(Calm down, General.)\x02\x03",

            "(Consider it the bare minimum of\x01",
            "courtesy to a minor power we have\x01",
            "a pact with.)\x02\x03",

            "(This assumes they can even\x01",
            "prove anything.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xE,
        "#884F#6P(...As you wish.)\x02",
    )

    CloseMessageWindow()
    OP_8C(0xD, 180, 400)
    Sleep(500)

    ChrTalk(    #120
        0xD,
        (
            "#899F#6PSo, then.\x02\x03",

            "#895FIf you can show me you have some hope of\x01",
            "stopping all this, our forces will withdraw.\x02\x03",

            "On the crest of the golden stallion\x01",
            "and my name as a member of the\x01",
            "Arnor family, I swear it.\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Man's Voice")

    AnonymousTalk(    #121
        "\x07\x05Good, that came through loud and clear.\x02",
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
        "#1004F#5PWha...? That voice!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x8,
        "#023F#4PIs that...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xB,
        "#070F#4PYes... No doubt about it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x9,
        "#055F#4PNow you're REALLY kidding me!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x102,
        "#1044F#6P...Dad.\x02",
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

    def Function_3_7B84(): pass

    label("Function_3_7B84")

    SetChrPos(0xC, -1360, 30, 43020, 0)
    OP_8E(0xFE, 0xFFFFFE0C, 0x32, 0xC0B2, 0x7D0, 0x0)
    OP_8E(0xFE, 0x0, 0x14, 0xCF62, 0x7D0, 0x0)
    Return()

    # Function_3_7B84 end

    def Function_4_7BBE(): pass

    label("Function_4_7BBE")

    SetChrPos(0x101, -1300, 40, 40490, 0)
    OP_8E(0xFE, 0xFFFFFAEC, 0x50, 0xBAFE, 0x7D0, 0x0)
    Return()

    # Function_4_7BBE end

    def Function_5_7BE4(): pass

    label("Function_5_7BE4")

    SetChrPos(0x102, 360, 20, 41150, 0)
    OP_8E(0xFE, 0x168, 0x50, 0xBA2C, 0x7D0, 0x0)
    Return()

    # Function_5_7BE4 end

    def Function_6_7C0A(): pass

    label("Function_6_7C0A")

    SetChrPos(0x8, -1530, -20, 38220, 0)
    OP_8E(0xFE, 0xFFFFFA06, 0x14, 0xB540, 0x7D0, 0x0)
    Return()

    # Function_6_7C0A end

    def Function_7_7C30(): pass

    label("Function_7_7C30")

    SetChrPos(0xA, 610, 20, 39320, 0)
    OP_8E(0xFE, 0x262, 0xFFFFFFE2, 0xB52C, 0x7D0, 0x0)
    Return()

    # Function_7_7C30 end

    def Function_8_7C56(): pass

    label("Function_8_7C56")

    SetChrPos(0x9, 1350, 20, 37510, 0)
    OP_8E(0xFE, 0x546, 0x32, 0xB130, 0x7D0, 0x0)
    Return()

    # Function_8_7C56 end

    def Function_9_7C7C(): pass

    label("Function_9_7C7C")

    SetChrPos(0xB, 0, 30, 35900, 0)
    OP_8E(0xFE, 0x0, 0x50, 0xAF00, 0x7D0, 0x0)
    Return()

    # Function_9_7C7C end

    def Function_10_7CA2(): pass

    label("Function_10_7CA2")

    OP_8C(0xFE, 270, 400)
    OP_8F(0xFE, 0x640, 0xFFFFFFEC, 0xC5A8, 0x7D0, 0x0)
    Return()

    # Function_10_7CA2 end

    def Function_11_7CBE(): pass

    label("Function_11_7CBE")

    Sleep(100)
    OP_8C(0xFE, 90, 400)
    OP_8F(0xFE, 0xFFFFF2D6, 0x1E, 0xC5C6, 0x7D0, 0x0)
    Return()

    # Function_11_7CBE end

    def Function_12_7CDF(): pass

    label("Function_12_7CDF")

    OP_8C(0xFE, 90, 400)
    OP_8F(0xFE, 0xFFFFF0C4, 0x14, 0x18010, 0x7D0, 0x0)
    Return()

    # Function_12_7CDF end

    def Function_13_7CFB(): pass

    label("Function_13_7CFB")

    Sleep(100)
    OP_8C(0xFE, 270, 400)
    OP_8F(0xFE, 0x28, 0xA, 0x17F5C, 0x7D0, 0x0)
    Return()

    # Function_13_7CFB end

    def Function_14_7D1C(): pass

    label("Function_14_7D1C")


    def lambda_7D22():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_7D22)
    Sleep(170)

    def lambda_7D42():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_7D42)

    def lambda_7D5D():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_7D5D)
    Sleep(200)

    def lambda_7D7D():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_7D7D)

    def lambda_7D98():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_7D98)
    Sleep(160)

    def lambda_7DB8():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_7DB8)

    def lambda_7DD3():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_7DD3)
    Sleep(230)

    def lambda_7DF3():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_7DF3)

    def lambda_7E0E():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_7E0E)
    Sleep(150)

    def lambda_7E2E():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_7E2E)

    def lambda_7E49():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_7E49)
    Sleep(180)

    def lambda_7E69():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_7E69)

    def lambda_7E84():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_7E84)
    Sleep(150)

    def lambda_7EA4():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_7EA4)
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

    # Function_14_7D1C end

    def Function_15_7F4C(): pass

    label("Function_15_7F4C")


    def lambda_7F52():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_7F52)
    Sleep(80)

    def lambda_7F72():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_7F72)

    def lambda_7F8D():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_7F8D)
    Sleep(50)

    def lambda_7FAD():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_7FAD)
    Sleep(100)

    def lambda_7FCD():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_7FCD)

    def lambda_7FE8():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_7FE8)
    Sleep(50)

    def lambda_8008():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_8008)
    Sleep(40)

    def lambda_8028():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x31, 1, lambda_8028)

    def lambda_8043():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2F, 1, lambda_8043)
    Sleep(70)

    def lambda_8063():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x30, 1, lambda_8063)

    def lambda_807E():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_807E)
    Sleep(80)

    def lambda_809E():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x32, 1, lambda_809E)

    def lambda_80B9():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_80B9)
    Sleep(60)

    def lambda_80D9():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x37, 1, lambda_80D9)

    def lambda_80F4():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x34, 1, lambda_80F4)
    Sleep(80)

    def lambda_8114():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x36, 1, lambda_8114)

    def lambda_812F():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x38, 1, lambda_812F)
    Sleep(100)

    def lambda_814F():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x35, 1, lambda_814F)
    Sleep(30)

    def lambda_816F():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x3E, 1, lambda_816F)

    def lambda_818A():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x3A, 1, lambda_818A)
    Sleep(80)

    def lambda_81AA():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x3C, 1, lambda_81AA)

    def lambda_81C5():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_81C5)
    Sleep(90)

    def lambda_81E5():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x3B, 1, lambda_81E5)

    def lambda_8200():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x3D, 1, lambda_8200)
    Sleep(100)

    def lambda_8220():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x42, 1, lambda_8220)

    def lambda_823B():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x3F, 1, lambda_823B)
    Sleep(30)

    def lambda_825B():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x40, 1, lambda_825B)

    def lambda_8276():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x43, 1, lambda_8276)
    Sleep(60)

    def lambda_8296():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x41, 1, lambda_8296)

    def lambda_82B1():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x44, 1, lambda_82B1)
    Return()

    # Function_15_7F4C end

    def Function_16_82C7(): pass

    label("Function_16_82C7")


    def lambda_82CD():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x46, 1, lambda_82CD)
    Sleep(80)

    def lambda_82ED():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x47, 1, lambda_82ED)

    def lambda_8308():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x49, 1, lambda_8308)
    Sleep(50)

    def lambda_8328():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x48, 1, lambda_8328)
    Sleep(100)

    def lambda_8348():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x45, 1, lambda_8348)

    def lambda_8363():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x4A, 1, lambda_8363)
    Sleep(50)

    def lambda_8383():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x4B, 1, lambda_8383)
    Sleep(40)

    def lambda_83A3():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x4F, 1, lambda_83A3)

    def lambda_83BE():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x4D, 1, lambda_83BE)
    Sleep(70)

    def lambda_83DE():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x4E, 1, lambda_83DE)

    def lambda_83F9():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x4C, 1, lambda_83F9)
    Sleep(80)

    def lambda_8419():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x50, 1, lambda_8419)

    def lambda_8434():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x51, 1, lambda_8434)
    Sleep(60)

    def lambda_8454():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x55, 1, lambda_8454)

    def lambda_846F():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x52, 1, lambda_846F)
    Sleep(80)

    def lambda_848F():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x54, 1, lambda_848F)

    def lambda_84AA():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x56, 1, lambda_84AA)
    Sleep(100)

    def lambda_84CA():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x53, 1, lambda_84CA)
    Sleep(30)

    def lambda_84EA():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x5C, 1, lambda_84EA)

    def lambda_8505():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x58, 1, lambda_8505)
    Sleep(80)

    def lambda_8525():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x5A, 1, lambda_8525)

    def lambda_8540():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x57, 1, lambda_8540)
    Sleep(90)

    def lambda_8560():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x59, 1, lambda_8560)

    def lambda_857B():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x5B, 1, lambda_857B)
    Sleep(100)

    def lambda_859B():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x60, 1, lambda_859B)

    def lambda_85B6():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x5D, 1, lambda_85B6)
    Sleep(30)

    def lambda_85D6():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x5E, 1, lambda_85D6)

    def lambda_85F1():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x61, 1, lambda_85F1)
    Sleep(60)

    def lambda_8611():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x5F, 1, lambda_8611)

    def lambda_862C():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x62, 1, lambda_862C)
    Return()

    # Function_16_82C7 end

    def Function_17_8642(): pass

    label("Function_17_8642")

    Sleep(80)

    def lambda_864D():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x65, 1, lambda_864D)

    def lambda_8668():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x67, 1, lambda_8668)
    Sleep(50)

    def lambda_8688():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x66, 1, lambda_8688)
    Sleep(100)

    def lambda_86A8():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x68, 1, lambda_86A8)
    Sleep(50)
    Sleep(40)

    def lambda_86CD():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x6D, 1, lambda_86CD)

    def lambda_86E8():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x6B, 1, lambda_86E8)
    Sleep(70)

    def lambda_8708():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x6C, 1, lambda_8708)
    Sleep(80)

    def lambda_8728():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x6E, 1, lambda_8728)
    Sleep(60)

    def lambda_8748():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x73, 1, lambda_8748)
    Sleep(80)

    def lambda_8768():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x72, 1, lambda_8768)

    def lambda_8783():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x74, 1, lambda_8783)
    Sleep(100)

    def lambda_87A3():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x71, 1, lambda_87A3)
    Sleep(30)

    def lambda_87C3():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x7A, 1, lambda_87C3)
    Sleep(80)

    def lambda_87E3():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x78, 1, lambda_87E3)
    Sleep(90)

    def lambda_8803():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x77, 1, lambda_8803)

    def lambda_881E():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x79, 1, lambda_881E)
    Sleep(100)

    def lambda_883E():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x7C, 1, lambda_883E)
    Sleep(30)

    def lambda_885E():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x7D, 1, lambda_885E)
    Sleep(60)

    def lambda_887E():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x7B, 1, lambda_887E)

    def lambda_8899():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x7E, 1, lambda_8899)
    Return()

    # Function_17_8642 end

    SaveToFile()

Try(main)
