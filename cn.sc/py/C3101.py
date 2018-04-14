from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'C3101   ._SN',
        MapName             = 'Zeiss',
        Location            = 'C3101.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60034",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/C3101   ._SN',
            'ED6_DT21/C3101_1 ._SN',
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
        '卡西乌斯',                             # 9
        '尤莉亚上尉',                           # 10
        '摩尔根将军',                           # 11
        '希德中校',                             # 12
        '格斯塔夫维修长',                       # 13
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
        '亲卫队',                               # 30
        '亲卫队',                               # 31
        '亲卫队',                               # 32
        '亲卫队',                               # 33
        '亲卫队',                               # 34
        '亲卫队',                               # 35
        '王国军士官',                           # 36
        '目标用照相机',                         # 37
        '贝尔克副队长',                         # 38
        '士兵',                                 # 39
        '士兵',                                 # 40
        '士兵',                                 # 41
        '士兵',                                 # 42
        '士兵',                                 # 43
        '士兵',                                 # 44
        '士兵',                                 # 45
        '士兵',                                 # 46
        '士兵',                                 # 47
        '士兵',                                 # 48
        '士兵',                                 # 49
        '士兵',                                 # 50
        '士兵',                                 # 51
        '士兵',                                 # 52
        '士兵',                                 # 53
        '士兵',                                 # 54
        '士兵',                                 # 55
        '士兵',                                 # 56
        '士兵',                                 # 57
        '士兵',                                 # 58
        '士兵',                                 # 59
        '士兵',                                 # 60
        '士兵',                                 # 61
        '士兵',                                 # 62
        '士兵',                                 # 63
        '士兵',                                 # 64
        '士兵',                                 # 65
        '士兵',                                 # 66
        '士兵',                                 # 67
        '士兵',                                 # 68
        '士兵',                                 # 69
        '士兵',                                 # 70
        '王国军士官',                           # 71
        '王国军士官',                           # 72
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
        'ED6_DT27/CH03670 ._CH',             # 00
        'ED6_DT27/CH03580 ._CH',             # 01
        'ED6_DT07/CH02080 ._CH',             # 02
        'ED6_DT27/CH03590 ._CH',             # 03
        'ED6_DT07/CH02440 ._CH',             # 04
        'ED6_DT07/CH01300 ._CH',             # 05
        'ED6_DT07/CH01320 ._CH',             # 06
        'ED6_DT27/CH04580 ._CH',             # 07
        'ED6_DT07/CH01600 ._CH',             # 08
        'ED6_DT07/CH00322 ._CH',             # 09
        'ED6_DT07/CH00321 ._CH',             # 0A
        'ED6_DT27/CH04000 ._CH',             # 0B
        'ED6_DT27/CH04004 ._CH',             # 0C
        'ED6_DT07/CH00120 ._CH',             # 0D
        'ED6_DT07/CH00124 ._CH',             # 0E
        'ED6_DT07/CH00130 ._CH',             # 0F
        'ED6_DT07/CH00134 ._CH',             # 10
        'ED6_DT07/CH00140 ._CH',             # 11
        'ED6_DT07/CH00144 ._CH',             # 12
        'ED6_DT07/CH00150 ._CH',             # 13
        'ED6_DT07/CH00154 ._CH',             # 14
        'ED6_DT07/CH00320 ._CH',             # 15
        'ED6_DT07/CH00324 ._CH',             # 16
        'ED6_DT07/CH00330 ._CH',             # 17
        'ED6_DT07/CH00334 ._CH',             # 18
        'ED6_DT07/CH00137 ._CH',             # 19
        'ED6_DT26/CH20290 ._CH',             # 1A
        'ED6_DT26/CH20307 ._CH',             # 1B
        'ED6_DT26/CH20296 ._CH',             # 1C
        'ED6_DT26/CH20297 ._CH',             # 1D
        'ED6_DT07/CH01640 ._CH',             # 1E
        'ED6_DT07/CH00331 ._CH',             # 1F
        'ED6_DT27/CH04590 ._CH',             # 20
        'ED6_DT27/CH04594 ._CH',             # 21
    )

    AddCharChipPat(
        'ED6_DT27/CH03670P._CP',             # 00
        'ED6_DT27/CH03580P._CP',             # 01
        'ED6_DT07/CH02080P._CP',             # 02
        'ED6_DT27/CH03590P._CP',             # 03
        'ED6_DT07/CH02440P._CP',             # 04
        'ED6_DT07/CH01300P._CP',             # 05
        'ED6_DT07/CH01320P._CP',             # 06
        'ED6_DT27/CH04580P._CP',             # 07
        'ED6_DT07/CH01600P._CP',             # 08
        'ED6_DT07/CH00322P._CP',             # 09
        'ED6_DT07/CH00321P._CP',             # 0A
        'ED6_DT27/CH04000P._CP',             # 0B
        'ED6_DT27/CH04004P._CP',             # 0C
        'ED6_DT07/CH00120P._CP',             # 0D
        'ED6_DT07/CH00124P._CP',             # 0E
        'ED6_DT07/CH00130P._CP',             # 0F
        'ED6_DT07/CH00134P._CP',             # 10
        'ED6_DT07/CH00140P._CP',             # 11
        'ED6_DT07/CH00144P._CP',             # 12
        'ED6_DT07/CH00150P._CP',             # 13
        'ED6_DT07/CH00154P._CP',             # 14
        'ED6_DT07/CH00320P._CP',             # 15
        'ED6_DT07/CH00324P._CP',             # 16
        'ED6_DT07/CH00330P._CP',             # 17
        'ED6_DT07/CH00334P._CP',             # 18
        'ED6_DT07/CH00137P._CP',             # 19
        'ED6_DT26/CH20290P._CP',             # 1A
        'ED6_DT26/CH20307P._CP',             # 1B
        'ED6_DT26/CH20296P._CP',             # 1C
        'ED6_DT26/CH20297P._CP',             # 1D
        'ED6_DT07/CH01640P._CP',             # 1E
        'ED6_DT07/CH00331P._CP',             # 1F
        'ED6_DT27/CH04590P._CP',             # 20
        'ED6_DT27/CH04594P._CP',             # 21
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
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
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
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
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_9BA",          # 00, 0
        "Function_1_9FE",          # 01, 1
        "Function_2_9FF",          # 02, 2
        "Function_3_D7C",          # 03, 3
        "Function_4_DA1",          # 04, 4
        "Function_5_DC9",          # 05, 5
        "Function_6_E03",          # 06, 6
        "Function_7_E42",          # 07, 7
        "Function_8_E81",          # 08, 8
        "Function_9_EAF",          # 09, 9
        "Function_10_EEE",         # 0A, 10
        "Function_11_F2D",         # 0B, 11
        "Function_12_52DC",        # 0C, 12
        "Function_13_644D",        # 0D, 13
        "Function_14_6478",        # 0E, 14
        "Function_15_64A3",        # 0F, 15
        "Function_16_64C7",        # 10, 16
        "Function_17_64F2",        # 11, 17
        "Function_18_650C",        # 12, 18
        "Function_19_6526",        # 13, 19
        "Function_20_6540",        # 14, 20
        "Function_21_655A",        # 15, 21
        "Function_22_659E",        # 16, 22
        "Function_23_65E2",        # 17, 23
        "Function_24_6609",        # 18, 24
        "Function_25_6630",        # 19, 25
        "Function_26_6657",        # 1A, 26
    )


    def Function_0_9BA(): pass

    label("Function_0_9BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_9D0")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 11)
    Jump("loc_9FD")

    label("loc_9D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_9EF")
    OP_A3(0x10F1)
    SetMapFlags(0x2000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x56), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)
    Jump("loc_9FD")

    label("loc_9EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_9FD")
    OP_A3(0x10F2)
    Event(1, 0)

    label("loc_9FD")

    Return()

    # Function_0_9BA end

    def Function_1_9FE(): pass

    label("Function_1_9FE")

    Return()

    # Function_1_9FE end

    def Function_2_9FF(): pass

    label("Function_2_9FF")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x23, -850, 0, 30150, 180)
    SetChrPos(0xD, -2850, 0, 28150, 90)
    SetChrPos(0xE, 1250, 0, 28150, 270)
    SetChrPos(0xF, -2850, 0, 26150, 90)
    SetChrPos(0x10, 1250, 0, 26150, 270)
    SetChrPos(0x11, -2850, 0, 24150, 90)
    SetChrPos(0x12, 1250, 0, 24150, 270)
    SetChrChipByIndex(0xD, 9)
    SetChrChipByIndex(0xE, 9)
    SetChrChipByIndex(0xF, 9)
    SetChrChipByIndex(0x10, 9)
    SetChrChipByIndex(0x11, 9)
    SetChrChipByIndex(0x12, 9)
    OP_6D(-980, 0, 27500, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_43(0xD, 0x1, 0x0, 0x4)
    Sleep(50)
    OP_43(0xF, 0x1, 0x0, 0x4)
    Sleep(50)
    OP_43(0xE, 0x1, 0x0, 0x4)
    Sleep(50)
    OP_43(0x11, 0x1, 0x0, 0x4)
    Sleep(50)
    OP_43(0x10, 0x1, 0x0, 0x4)
    Sleep(50)
    OP_43(0x12, 0x1, 0x0, 0x4)
    FadeToBright(2000, 0)
    Sleep(3500)
    OP_22(0x85, 0x0, 0x64)

    def lambda_B66():

        label("loc_B66")

        OP_7C(0xC8, 0x0, 0x7D0, 0xBB8)
        OP_48()
        Jump("loc_B66")

    QueueWorkItem2(0x101, 3, lambda_B66)
    Sleep(500)
    OP_A2(0x0)
    OP_44(0xD, 0xFF)
    OP_44(0xE, 0xFF)
    OP_44(0xF, 0xFF)
    OP_44(0x10, 0xFF)
    OP_44(0x11, 0xFF)
    OP_44(0x12, 0xFF)
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x23, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #0
        0xD,
        "什、什么！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x12,
        "敌、敌人的轰炸！？\x02",
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_62(0xE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_62(0xF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_62(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_62(0x12, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_43(0xD, 0x1, 0x0, 0x5)
    OP_43(0xE, 0x1, 0x0, 0x6)
    OP_43(0xF, 0x1, 0x0, 0x7)
    OP_43(0x10, 0x1, 0x0, 0x8)
    OP_43(0x11, 0x1, 0x0, 0x9)
    OP_43(0x12, 0x1, 0x0, 0xA)
    OP_43(0x23, 0x1, 0x0, 0x3)
    Sleep(1000)
    OP_62(0x23, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    ChrTalk(    #2
        0x23,
        (
            "#5P冷、冷静一点！\x01",
            "只是地震！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x23,
        "#5P别乱了阵型，原地待命！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C3110   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_2_9FF end

    def Function_3_D7C(): pass

    label("Function_3_D7C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DA0")
    OP_8C(0xFE, 225, 400)
    Sleep(500)
    OP_8C(0xFE, 135, 400)
    Sleep(500)
    Jump("Function_3_D7C")

    label("loc_DA0")

    Return()

    # Function_3_D7C end

    def Function_4_DA1(): pass

    label("Function_4_DA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DC8")
    OP_99(0xFE, 0x0, 0x4, 0xA28)
    Sleep(500)
    OP_99(0xFE, 0x4, 0x0, 0xA28)
    Sleep(1500)
    Jump("Function_4_DA1")

    label("loc_DC8")

    Return()

    # Function_4_DA1 end

    def Function_5_DC9(): pass

    label("Function_5_DC9")

    SetChrChipByIndex(0xFE, 10)

    label("loc_DCE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E02")
    OP_90(0xFE, 0xFFFFFE0C, 0x0, 0x1F4, 0x1004, 0x0)
    OP_90(0xFE, 0x1F4, 0x0, 0xFFFFFE0C, 0x1068, 0x0)
    Jump("loc_DCE")

    label("loc_E02")

    Return()

    # Function_5_DC9 end

    def Function_6_E03(): pass

    label("Function_6_E03")

    SetChrChipByIndex(0xFE, 10)
    Sleep(50)

    label("loc_E0D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E41")
    OP_90(0xFE, 0xFFFFFCE0, 0x0, 0xFFFFFCE0, 0x1068, 0x0)
    OP_90(0xFE, 0x320, 0x0, 0x320, 0x10CC, 0x0)
    Jump("loc_E0D")

    label("loc_E41")

    Return()

    # Function_6_E03 end

    def Function_7_E42(): pass

    label("Function_7_E42")

    SetChrChipByIndex(0xFE, 10)
    Sleep(50)

    label("loc_E4C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E80")
    OP_90(0xFE, 0xFFFFFC18, 0x0, 0x0, 0xED8, 0x0)
    OP_90(0xFE, 0x3E8, 0x0, 0x0, 0xF3C, 0x0)
    Jump("loc_E4C")

    label("loc_E80")

    Return()

    # Function_7_E42 end

    def Function_8_E81(): pass

    label("Function_8_E81")

    SetChrChipByIndex(0xFE, 10)

    label("loc_E86")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EAE")
    OP_8C(0xFE, 90, 400)
    OP_8C(0xFE, 0, 400)
    OP_8C(0xFE, 270, 400)
    OP_8C(0xFE, 180, 400)
    Jump("loc_E86")

    label("loc_EAE")

    Return()

    # Function_8_E81 end

    def Function_9_EAF(): pass

    label("Function_9_EAF")

    SetChrChipByIndex(0xFE, 10)
    Sleep(50)

    label("loc_EB9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EED")
    OP_90(0xFE, 0x1F4, 0x0, 0xFFFFFE0C, 0xFA0, 0x0)
    OP_90(0xFE, 0xFFFFFE0C, 0x0, 0x1F4, 0x1004, 0x0)
    Jump("loc_EB9")

    label("loc_EED")

    Return()

    # Function_9_EAF end

    def Function_10_EEE(): pass

    label("Function_10_EEE")

    SetChrChipByIndex(0xFE, 10)
    Sleep(50)

    label("loc_EF8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F2C")
    OP_90(0xFE, 0x0, 0x0, 0xFFFFFC18, 0x1068, 0x0)
    OP_90(0xFE, 0x0, 0x0, 0x3E8, 0x10CC, 0x0)
    Jump("loc_EF8")

    label("loc_F2C")

    Return()

    # Function_10_EEE end

    def Function_11_F2D(): pass

    label("Function_11_F2D")

    EventBegin(0x0)
    ClearMapFlags(0x10)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    SetChrPos(0x8, -2300, 0, 17510, 0)
    SetChrPos(0x9, -2300, 0, 24240, 180)
    SetChrPos(0xA, -4980, 0, 20880, 90)
    SetChrPos(0xD, -12080, 0, 15010, 90)
    SetChrPos(0xE, -12900, 0, 16840, 90)
    SetChrPos(0xF, -13490, 0, 18730, 90)
    SetChrPos(0x10, -14010, 0, 15710, 90)
    SetChrPos(0x11, -14670, 0, 17570, 90)
    SetChrPos(0x12, -15200, 0, 19820, 90)
    SetChrPos(0x1D, -13510, 0, 22660, 90)
    SetChrPos(0x1E, -12880, 0, 24340, 90)
    SetChrPos(0x1F, -11920, 0, 26130, 90)
    SetChrPos(0x20, -15170, 0, 22090, 90)
    SetChrPos(0x21, -14580, 0, 23690, 90)
    SetChrPos(0x22, -13960, 0, 25780, 90)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 1)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 6)
    LoadEffect(0x0, "map\\\\mp009_00.eff")
    OP_6D(-16450, 0, 14000, 0)
    OP_67(0, 7580, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(247000, 0)
    OP_6E(316, 0)
    FadeToBright(1000, 0)

    def lambda_1106():
        OP_6D(-16450, 0, 28000, 5000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1106)

    def lambda_111E():
        OP_6C(310000, 5000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_111E)
    WaitChrThread(0x8, 0x1)

    def lambda_1133():
        OP_6D(-2680, 0, 21130, 3000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1133)

    def lambda_114B():
        OP_67(0, 4810, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_114B)

    def lambda_1163():
        OP_6B(2760, 4500)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_1163)

    def lambda_1173():
        OP_6C(296000, 4500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1173)

    def lambda_1183():
        OP_6E(443, 4500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1183)
    WaitChrThread(0x9, 0x1)
    Fade(500)
    OP_6D(-5790, 0, 20930, 0)
    OP_67(0, 4810, -10000, 0)
    OP_6B(2380, 0)
    OP_6C(271000, 0)
    OP_6E(443, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #4
        0xA,
        "#163F#5P双方，预备！\x02",
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x9, 28)
    SetChrSubChip(0x9, 4)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #5
        0xA,
        "#162F#5P#5S开始！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_59()
    OP_51(0x24, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x24, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x24, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_1286():
        OP_8F(0xFE, 0xFFFFD3B4, 0x0, 0x5190, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_1286)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x40)

    def lambda_12B5():
        OP_6D(-2710, 0, 25430, 600)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_12B5)

    def lambda_12CD():
        OP_6B(1740, 600)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12CD)

    def lambda_12DD():
        OP_6C(336000, 600)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_12DD)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 7)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #6 op#A op#5
        0x9,
        "#177F#2P#8A──呀啊啊啊啊啊！\x05\x02",
    )

    CloseMessageWindow()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_1333():
        OP_6D(-3520, 0, 18740, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1333)

    def lambda_134B():
        OP_6B(1840, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_134B)

    def lambda_135B():
        OP_6C(296000, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_135B)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 8)

    def lambda_1375():
        OP_8E(0xFE, 0xFFFFF704, 0x0, 0x5140, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_1375)
    WaitChrThread(0x9, 0x0)
    SetChrChipByIndex(0x9, 28)
    SetChrSubChip(0x9, 4)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 1)

    def lambda_13A9():
        OP_8F(0xFE, 0xFFFFF704, 0x0, 0x4A4C, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_13A9)

    def lambda_13C4():
        OP_99(0xFE, 0x4, 0x6, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_13C4)

    def lambda_13D4():
        OP_8F(0xFE, 0xFFFFF704, 0x0, 0x433A, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_13D4)
    WaitChrThread(0x9, 0x0)
    PlayEffect(0x0, 0xFF, 0x8, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(400)

    def lambda_143C():
        OP_6C(278000, 600)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_143C)

    def lambda_144C():
        OP_6B(2040, 600)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_144C)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 5)

    def lambda_1466():
        OP_96(0xFE, 0xFFFFF704, 0x0, 0x544C, 0x190, 0xFA0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_1466)
    WaitChrThread(0x9, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 7)
    Sleep(200)

    def lambda_149D():
        OP_6D(-3520, 0, 18250, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_149D)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 8)

    def lambda_14C8():
        OP_8E(0xFE, 0xFFFFF704, 0x0, 0x4F10, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_14C8)
    WaitChrThread(0x9, 0x0)
    SetChrChipByIndex(0x9, 28)
    SetChrSubChip(0x9, 9)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 7)

    def lambda_14FC():
        OP_8F(0xFE, 0xFFFFF704, 0x0, 0x49E8, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_14FC)

    def lambda_1517():
        OP_99(0xFE, 0x9, 0xA, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1517)

    def lambda_1527():
        OP_8F(0xFE, 0xFFFFF704, 0x0, 0x420E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1527)
    PlayEffect(0x0, 0xFF, 0x8, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(400)

    def lambda_158A():
        OP_6D(-3520, 0, 15920, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_158A)

    def lambda_15A2():
        OP_6C(226000, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_15A2)
    SetChrChipByIndex(0x9, 28)
    SetChrSubChip(0x9, 7)
    Sleep(300)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 2)

    def lambda_15D4():
        OP_8F(0xFE, 0xFFFFF704, 0x0, 0x4600, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_15D4)

    def lambda_15EF():
        OP_99(0xFE, 0x7, 0x8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_15EF)

    def lambda_15FF():
        OP_8F(0xFE, 0xFFFFF704, 0x0, 0x3EEE, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_15FF)
    OP_23(0xD6)
    PlayEffect(0x0, 0xFF, 0x8, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)

    def lambda_1665():
        OP_6D(-3520, 0, 16120, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1665)

    def lambda_167D():
        OP_6B(1840, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_167D)

    def lambda_168D():
        OP_9E(0xFE, 0xA, 0x0, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_168D)

    def lambda_16A7():
        OP_9E(0xFE, 0xA, 0x0, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_16A7)

    def lambda_16C1():
        OP_8F(0xFE, 0xFFFFF704, 0x0, 0x40B0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_16C1)
    Sleep(150)
    SetChrChipByIndex(0x9, 28)
    SetChrSubChip(0x9, 1)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 7)
    WaitChrThread(0x9, 0x1)
    WaitChrThread(0x8, 0x1)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 6)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 4)

    def lambda_171C():
        OP_96(0xFE, 0xFFFFF704, 0x0, 0x3E6C, 0x190, 0x4E20)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_171C)
    WaitChrThread(0x8, 0x0)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_1744():
        OP_99(0xFE, 0x6, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1744)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 3)
    Sleep(100)
    PlayEffect(0x0, 0xFF, 0x9, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_17A6():
        OP_6D(-2750, 0, 20070, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_17A6)

    def lambda_17BE():
        OP_6C(192000, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_17BE)

    def lambda_17CE():
        OP_67(0, 7000, -10000, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_17CE)

    def lambda_17E6():
        OP_6B(1840, 400)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_17E6)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 6)

    def lambda_1800():
        OP_96(0xFE, 0xFFFFF704, 0x0, 0x56EA, 0x320, 0xFA0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_1800)
    WaitChrThread(0x9, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 5)

    def lambda_1832():
        OP_96(0xFE, 0xFFFFF704, 0x0, 0x5D98, 0x190, 0xFA0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_1832)
    WaitChrThread(0x9, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 7)
    Sleep(1000)

    def lambda_1869():
        OP_6D(-2470, 0, 19840, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1869)

    def lambda_1881():
        OP_6C(184000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1881)

    def lambda_1891():
        OP_67(0, 3850, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1891)

    def lambda_18A9():
        OP_6B(1720, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_18A9)
    Sleep(200)
    SetChrChipByIndex(0x9, 28)
    SetChrSubChip(0x9, 4)
    Sleep(200)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 0)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_18F4():
        OP_6D(-2280, 0, 18410, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_18F4)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 8)

    def lambda_1916():
        OP_8E(0xFE, 0xFFFFF704, 0x0, 0x46D2, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_1916)
    Sleep(200)
    SetChrPos(0x9, -2300, 0, 23960, 180)

    def lambda_1947():
        OP_8E(0xFE, 0xFFFFF704, 0x0, 0x46D2, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_1947)
    OP_6D(-2250, 0, 22320, 0)
    OP_67(0, 3850, -10000, 0)
    OP_6B(1660, 0)
    OP_6C(1000, 0)
    OP_6E(443, 0)

    def lambda_199F():
        OP_6D(-2250, 0, 19120, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_199F)
    WaitChrThread(0x9, 0x0)
    SetChrChipByIndex(0x9, 28)
    SetChrSubChip(0x9, 0)

    def lambda_19C6():
        OP_8F(0xFE, 0xFFFFF704, 0x0, 0x427C, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_19C6)

    def lambda_19E1():
        OP_99(0xFE, 0x0, 0x1, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_19E1)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 1)
    OP_8C(0x8, 45, 0)

    def lambda_1A02():
        OP_8F(0xFE, 0xFFFFF43E, 0x0, 0x3D40, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1A02)
    Sleep(100)
    OP_22(0x84, 0x0, 0x64)
    WaitChrThread(0x8, 0x0)
    WaitChrThread(0x9, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    SetChrChipByIndex(0x9, 28)
    SetChrSubChip(0x9, 2)
    OP_8C(0x9, 225, 0)
    Sleep(200)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_1A5E():
        OP_6D(-3820, 0, 16950, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1A5E)

    def lambda_1A76():
        OP_6C(315000, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A76)

    def lambda_1A86():
        OP_8F(0xFE, 0xFFFFF5C4, 0x0, 0x3FC9, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_1A86)

    def lambda_1AA1():
        OP_99(0xFE, 0x2, 0x3, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1AA1)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 6)
    OP_8C(0x8, 0, 0)

    def lambda_1AC2():
        OP_8F(0xFE, 0xFFFFF682, 0x0, 0x39F8, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1AC2)
    Sleep(200)
    OP_22(0x84, 0x0, 0x64)
    WaitChrThread(0x8, 0x0)
    WaitChrThread(0x9, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)

    def lambda_1AFF():
        OP_6D(-3120, 0, 16810, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1AFF)

    def lambda_1B17():
        OP_67(0, 4680, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B17)

    def lambda_1B2F():
        OP_6B(2200, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1B2F)
    OP_8C(0x9, 0, 1000)
    OP_8C(0x9, 90, 1000)

    def lambda_1B4D():
        OP_8C(0xFE, 180, 1000)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_1B4D)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 9)

    def lambda_1B65():
        OP_96(0xFE, 0xFFFFF81C, 0x0, 0x4CEA, 0x7D0, 0x1770)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1B65)
    OP_51(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x9, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x9, 28)
    SetChrSubChip(0x9, 4)

    def lambda_1BA6():
        OP_8F(0xFE, 0xFFFFF81C, 0x0, 0x3278, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_1BA6)

    def lambda_1BC1():
        OP_99(0xFE, 0x4, 0x6, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1BC1)
    OP_22(0xA3, 0x0, 0x64)
    Sleep(100)
    OP_22(0x84, 0x0, 0x64)
    WaitChrThread(0x8, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    OP_51(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 4)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(600)

    def lambda_1C0D():
        OP_6D(-3120, 0, 19040, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1C0D)

    def lambda_1C25():
        OP_6C(270000, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1C25)

    def lambda_1C35():
        OP_6B(1820, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1C35)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 7)
    OP_8C(0x9, 90, 1000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_1C5F():
        OP_8C(0xFE, 0, 1000)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_1C5F)

    def lambda_1C6D():
        OP_8F(0xFE, 0xFFFFF81C, 0x0, 0x3E94, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1C6D)
    WaitChrThread(0x9, 0x0)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 8)
    WaitChrThread(0x9, 0x1)
    SetChrChipByIndex(0x9, 28)
    SetChrSubChip(0x9, 4)

    def lambda_1CA6():
        OP_8F(0xFE, 0xFFFFF81C, 0x0, 0x4484, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_1CA6)

    def lambda_1CC1():
        OP_99(0xFE, 0x4, 0x6, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1CC1)
    Sleep(100)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 5)

    def lambda_1CE0():
        OP_8F(0xFE, 0xFFFFF880, 0x0, 0x4CEA, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1CE0)
    WaitChrThread(0x9, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x0, 0xFF, 0x8, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)

    def lambda_1D43():
        OP_9E(0xFE, 0xA, 0x0, 0x190, 0xFA0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1D43)
    Sleep(600)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_1D67():
        OP_6D(-3120, 0, 15960, 600)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1D67)

    def lambda_1D7F():
        OP_6C(235000, 600)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1D7F)

    def lambda_1D8F():
        OP_6B(2240, 600)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1D8F)
    TurnDirection(0x8, 0x9, 0)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 4)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 7)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_1DC3():
        OP_8F(0xFE, 0xFFFFF880, 0x0, 0x4916, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1DC3)
    WaitChrThread(0x8, 0x0)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 5)
    Sleep(100)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x209, 0x0, 0x64)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 6)

    def lambda_1E0A():
        OP_8F(0xFE, 0xFFFFF880, 0x0, 0x366A, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_1E0A)
    WaitChrThread(0x9, 0x0)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 4)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 6)

    def lambda_1E3E():
        OP_9E(0xFE, 0xA, 0x0, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1E3E)
    Sleep(1000)

    ChrTalk(    #7
        0x9,
        "#172F#5P唔……\x02",
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #8
        0x8,
        (
            "#1126F#6P怎么回事！？\x01",
            "行动太过直线化！\x02\x03",

            "你用的是细剑，就应该使出\x01",
            "流畅的进攻套路！\x02\x03",

            "想想我教过你的东西！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x9,
        (
            "#173F#5P是……\x02\x03",

            "#177F……是！\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x9, 28)
    SetChrSubChip(0x9, 4)
    OP_0D()

    def lambda_1F2B():
        OP_6D(-3120, 0, 12880, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1F2B)

    def lambda_1F43():
        OP_6B(1940, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1F43)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)

    def lambda_1F5D():
        OP_6D(-2360, 0, 19240, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1F5D)

    def lambda_1F75():
        OP_6C(322000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1F75)

    def lambda_1F85():
        OP_6B(2440, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1F85)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 8)
    OP_7D(0x0, 0x9, 0x32, 0x1F4)

    def lambda_1FA7():

        label("loc_1FA7")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_1FA7")

    QueueWorkItem2(0x9, 3, lambda_1FA7)

    def lambda_1FB8():
        OP_96(0xFE, 0xBFE, 0x0, 0x48BC, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_1FB8)
    WaitChrThread(0x9, 0x0)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_1FE0():
        OP_96(0xFE, 0xFFFFF880, 0x0, 0x5A82, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_1FE0)
    WaitChrThread(0x9, 0x0)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_2008():
        OP_96(0xFE, 0xFFFFE4DA, 0x0, 0x48BC, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_2008)
    WaitChrThread(0x9, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    OP_7D(0x1, 0x9, 0x0, 0x0)
    OP_44(0x9, 0x3)
    Fade(500)
    OP_8C(0x9, 79, 0)
    OP_6D(-7350, 0, 21010, 0)
    OP_67(0, 2370, -10000, 0)
    OP_6B(2380, 0)
    OP_6C(304000, 0)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 7)
    Sleep(400)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 8)

    def lambda_209E():
        OP_6D(-5290, 0, 21010, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_209E)

    def lambda_20B6():
        OP_8F(0xFE, 0xFFFFEF20, 0x0, 0x48BC, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_20B6)
    WaitChrThread(0x9, 0x0)
    SetChrChipByIndex(0x9, 28)
    SetChrSubChip(0x9, 4)

    def lambda_20E0():
        OP_8F(0xFE, 0xFFFFF39E, 0x0, 0x48BC, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_20E0)

    def lambda_20FB():
        OP_99(0xFE, 0x4, 0x6, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_20FB)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 1)
    OP_8C(0x8, 349, 0)

    def lambda_211C():
        OP_8F(0xFE, 0xFFFFFCA4, 0x0, 0x46F0, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_211C)
    Sleep(100)
    OP_22(0x84, 0x0, 0x64)
    WaitChrThread(0x9, 0x0)
    WaitChrThread(0x8, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(400)

    def lambda_2159():
        OP_6D(-4680, 0, 19770, 600)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2159)

    def lambda_2171():
        OP_67(0, 4800, -10000, 600)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2171)

    def lambda_2189():

        label("loc_2189")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_2189")

    QueueWorkItem2(0x8, 3, lambda_2189)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 5)

    def lambda_21A4():
        OP_96(0xFE, 0xFFFFEA0C, 0x0, 0x48BC, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_21A4)
    WaitChrThread(0x9, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 7)
    OP_44(0x8, 0x3)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 0)

    def lambda_21E4():
        OP_6D(-4690, 0, 18490, 800)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_21E4)

    def lambda_21FC():
        OP_6C(270000, 800)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_21FC)

    def lambda_220C():
        OP_67(0, 3680, -10000, 800)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_220C)
    OP_7D(0x0, 0x9, 0x32, 0xC8)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 8)

    def lambda_2236():

        label("loc_2236")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_2236")

    QueueWorkItem2(0x9, 3, lambda_2236)

    def lambda_2247():
        OP_8F(0xFE, 0xFFFFF24A, 0x0, 0x5190, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_2247)
    WaitChrThread(0x9, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    OP_7D(0x1, 0x9, 0x0, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0x9, 0x3)
    SetChrChipByIndex(0x9, 28)
    SetChrSubChip(0x9, 2)

    def lambda_228B():
        OP_96(0xFE, 0xFFFFF862, 0x0, 0x4B5A, 0x320, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_228B)
    OP_8C(0x9, 214, 2000)
    OP_8C(0x9, 304, 2000)
    OP_8C(0x9, 34, 2000)
    OP_8C(0x9, 124, 2000)
    WaitChrThread(0x9, 0x0)
    SetChrChipByIndex(0x9, 28)
    SetChrSubChip(0x9, 3)
    PlayEffect(0x0, 0xFF, 0x8, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 7)
    OP_8C(0x8, 315, 0)

    def lambda_231F():
        OP_8F(0xFE, 0x17C, 0x0, 0x4484, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_231F)
    WaitChrThread(0x8, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 5)

    def lambda_2357():
        OP_96(0xFE, 0xFFFFF218, 0x0, 0x4F88, 0x258, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_2357)
    OP_22(0xA4, 0x0, 0x64)
    WaitChrThread(0x9, 0x0)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 0)

    def lambda_2389():
        OP_6D(-370, 0, 16280, 800)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2389)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 8)
    OP_7D(0x0, 0x9, 0x32, 0x1F4)

    def lambda_23B3():
        OP_96(0xFE, 0x1068, 0x0, 0x39E4, 0x7D0, 0xFA0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_23B3)
    OP_51(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0xA3, 0x0, 0x64)
    WaitChrThread(0x9, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    OP_7D(0x1, 0x9, 0x0, 0x0)
    OP_51(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_240C():
        OP_6D(-2090, 0, 18000, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_240C)

    def lambda_2424():
        OP_6C(258000, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2424)
    SetChrChipByIndex(0x9, 28)
    SetChrSubChip(0x9, 4)

    def lambda_243E():
        OP_8F(0xFE, 0x780, 0x0, 0x4006, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_243E)

    def lambda_2459():
        OP_99(0xFE, 0x4, 0x6, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2459)

    def lambda_2469():
        OP_8C(0xFE, 306, 2000)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2469)
    Sleep(100)
    OP_22(0x84, 0x0, 0x64)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 9)

    def lambda_248B():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_248B)

    def lambda_2499():
        OP_96(0xFE, 0xFFFFF3F8, 0x0, 0x4EC0, 0x7D0, 0xFA0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_2499)
    OP_51(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 3)
    WaitChrThread(0x8, 0x0)
    OP_51(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0x8, 0x3)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 4)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_24FD():
        OP_6D(-3700, 0, 19950, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_24FD)

    def lambda_2515():
        OP_6C(282000, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2515)

    def lambda_2525():
        OP_6B(2000, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2525)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 8)
    OP_7D(0x0, 0x9, 0x32, 0xC8)

    def lambda_2547():

        label("loc_2547")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_2547")

    QueueWorkItem2(0x9, 3, lambda_2547)

    def lambda_2558():
        OP_8F(0xFE, 0xFFFFFBBE, 0x0, 0x48BC, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_2558)
    WaitChrThread(0x9, 0x0)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 0)

    def lambda_2582():
        OP_6D(-5530, 0, 18670, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2582)

    def lambda_259A():
        OP_96(0xFE, 0xFFFFF02E, 0x0, 0x3FF2, 0x258, 0xFA0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_259A)
    OP_22(0xA4, 0x0, 0x64)
    WaitChrThread(0x9, 0x0)
    OP_44(0x9, 0x3)
    OP_7D(0x1, 0x9, 0x0, 0x0)

    def lambda_25CE():
        OP_6D(-4720, 0, 20630, 800)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_25CE)

    def lambda_25E6():
        OP_67(0, 3060, -10000, 800)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_25E6)

    def lambda_25FE():
        OP_6C(258000, 800)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_25FE)
    SetChrChipByIndex(0x9, 28)
    SetChrSubChip(0x9, 12)

    def lambda_2618():
        OP_96(0xFE, 0xFFFFF3B2, 0x0, 0x49FC, 0x578, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_2618)
    OP_51(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0xA4, 0x0, 0x64)
    Sleep(100)
    SetChrChipByIndex(0x9, 28)
    SetChrSubChip(0x9, 0)
    WaitChrThread(0x9, 0x0)
    OP_51(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x9, 28)
    SetChrSubChip(0x9, 1)
    PlayEffect(0x0, 0xFF, 0x8, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 2)
    OP_8C(0x8, 213, 0)

    def lambda_26BA():
        OP_8F(0xFE, 0xFFFFF86C, 0x0, 0x5870, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_26BA)

    def lambda_26D5():
        OP_9E(0xFE, 0x14, 0x0, 0x190, 0xFA0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_26D5)
    WaitChrThread(0x8, 0x0)
    Sleep(200)

    def lambda_26F9():
        OP_6D(-3540, 0, 21820, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_26F9)

    def lambda_2711():
        OP_67(0, 4059, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2711)

    def lambda_2729():
        OP_6C(234000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2729)

    def lambda_2739():
        OP_6B(2400, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2739)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 3)

    def lambda_2753():
        OP_96(0xFE, 0xFFFFFCFE, 0x0, 0x65FE, 0x258, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_2753)

    def lambda_2771():
        OP_8C(0xFE, 189, 200)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2771)
    WaitChrThread(0x8, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 4)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 0)
    OP_0D()
    Sleep(200)
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x9, 28)
    SetChrSubChip(0x9, 4)
    OP_0D()
    Sleep(500)

    ChrTalk(    #10
        0x8,
        (
            "#1125F#6P这就对了……\x02\x03",

            "#1122F那么，接招吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 9, 0)
    OP_8C(0x8, 189, 0)

    def lambda_281A():
        OP_6D(-2150, 0, 25310, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_281A)

    def lambda_2832():
        OP_67(0, 3360, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2832)

    def lambda_284A():
        OP_6B(1800, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_284A)
    Fade(250)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 8)
    OP_0D()
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    Sleep(400)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_2887():
        OP_6D(-5080, 0, 19800, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2887)

    def lambda_289F():
        OP_6C(270000, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_289F)

    def lambda_28AF():
        OP_6B(2200, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_28AF)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 9)
    SetChrFlags(0x8, 0x4)

    def lambda_28CE():
        OP_96(0xFE, 0xFFFFF3B2, 0xC8, 0x4F38, 0x960, 0x1F40)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_28CE)
    OP_51(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0xA3, 0x0, 0x64)
    Sleep(250)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 4)

    def lambda_290B():
        OP_99(0xFE, 0x4, 0x5, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_290B)
    WaitChrThread(0x8, 0x0)
    PlayEffect(0x0, 0xFF, 0x9, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 2)

    def lambda_2964():
        OP_9E(0xFE, 0xA, 0x0, 0x258, 0xFA0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2964)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)

    def lambda_298C():
        OP_6D(-5080, 0, 23430, 800)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_298C)

    def lambda_29A4():
        OP_67(0, 4360, -10000, 800)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_29A4)

    def lambda_29BC():
        OP_6C(315000, 800)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_29BC)

    def lambda_29CC():
        OP_8F(0xFE, 0xFFFFF3B2, 0x0, 0x4808, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_29CC)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 3)
    ClearChrFlags(0x8, 0x4)

    def lambda_29F6():
        OP_96(0xFE, 0xFFFFF3B2, 0x0, 0x5D02, 0x7D0, 0x1388)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_29F6)
    WaitChrThread(0x8, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    OP_51(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 4)
    Sleep(200)

    def lambda_2A38():
        OP_6D(-4860, 0, 20850, 200)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2A38)

    def lambda_2A50():
        OP_6B(1960, 200)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2A50)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 9)

    def lambda_2A73():
        OP_8F(0xFE, 0xFFFFF3B2, 0x0, 0x52BC, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_2A73)
    WaitChrThread(0x8, 0x0)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 0)
    Sleep(100)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 1)

    def lambda_2AAC():
        OP_8F(0xFE, 0xFFFFF3B2, 0x0, 0x4DF8, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_2AAC)
    PlayEffect(0x0, 0xFF, 0x9, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 3)

    def lambda_2B0B():
        OP_8F(0xFE, 0xFFFFF3B2, 0x0, 0x45CE, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_2B0B)

    def lambda_2B26():
        OP_9E(0xFE, 0xA, 0x0, 0x190, 0xFA0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2B26)
    Sleep(200)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 0)
    Sleep(200)

    def lambda_2B5D():
        OP_6D(-4860, 0, 19860, 200)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2B5D)

    def lambda_2B75():
        OP_6B(1760, 200)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2B75)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 1)

    def lambda_2B98():
        OP_8F(0xFE, 0xFFFFF3B2, 0x0, 0x4A6A, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_2B98)
    PlayEffect(0x0, 0xFF, 0x9, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 3)

    def lambda_2BF7():
        OP_8F(0xFE, 0xFFFFF3B2, 0x0, 0x4240, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_2BF7)

    def lambda_2C12():
        OP_9E(0xFE, 0xA, 0x0, 0x190, 0xFA0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2C12)
    Sleep(200)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 0)
    Sleep(150)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 5)

    def lambda_2C53():
        OP_96(0xFE, 0xFFFFE7C8, 0x0, 0x3C64, 0x258, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_2C53)
    WaitChrThread(0x8, 0x0)
    Sleep(50)

    def lambda_2C7B():
        OP_6D(-4860, 0, 18870, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2C7B)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 1)

    def lambda_2C9D():
        OP_8F(0xFE, 0xFFFFF3B2, 0x0, 0x46DC, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_2C9D)
    OP_22(0x84, 0x0, 0x64)
    Sleep(300)

    def lambda_2CC2():
        OP_6D(-4860, 0, 17620, 200)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2CC2)

    def lambda_2CDA():
        OP_6B(2060, 200)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2CDA)

    def lambda_2CEA():
        OP_67(0, 3360, -10000, 200)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2CEA)

    def lambda_2D02():
        OP_6C(304000, 200)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2D02)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 6)
    OP_7D(0x0, 0x8, 0x14, 0xC8)
    OP_8C(0x8, 259, 0)

    def lambda_2D2B():
        OP_96(0xFE, 0xFFFFE7C8, 0x0, 0x4204, 0x190, 0x1F40)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_2D2B)
    WaitChrThread(0x9, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 2)
    WaitChrThread(0x8, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    OP_7D(0x1, 0x8, 0x0, 0x0)
    OP_8C(0x8, 214, 800)
    OP_8C(0x8, 169, 800)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 7)

    def lambda_2D87():
        OP_6D(-7640, 0, 14240, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2D87)
    PlayEffect(0x0, 0xFF, 0x9, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 6)

    def lambda_2DE3():
        OP_96(0xFE, 0xFFFFE7C8, 0x0, 0x328C, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_2DE3)
    WaitChrThread(0x9, 0x0)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_2E0B():
        OP_96(0xFE, 0xFFFFE7C8, 0x0, 0x2738, 0x258, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_2E0B)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 3)

    def lambda_2E33():
        OP_96(0xFE, 0xFFFFE7C8, 0x0, 0x4FD8, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_2E33)
    WaitChrThread(0x9, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 4)
    WaitChrThread(0x8, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 4)
    Sleep(200)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 9)

    def lambda_2E91():
        OP_8F(0xFE, 0xFFFFE7C8, 0x0, 0x2F94, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_2E91)
    Sleep(200)
    SetChrPos(0x8, -6200, 0, 20440, 180)

    def lambda_2EC2():
        OP_8F(0xFE, 0xFFFFE7C8, 0x0, 0x2F94, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_2EC2)
    Fade(500)
    OP_6D(-7500, 0, 12160, 0)
    OP_6C(220000, 0)
    OP_6E(443, 0)

    def lambda_2F05():
        OP_6D(-7460, 0, 9900, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2F05)

    def lambda_2F1D():
        OP_6B(1800, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2F1D)
    Sleep(100)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x9, 28)
    SetChrSubChip(0x9, 11)
    WaitChrThread(0x8, 0x0)

    def lambda_2F4A():
        OP_6D(-7460, 0, 10900, 200)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2F4A)
    SetChrChipByIndex(0x9, 28)
    SetChrSubChip(0x9, 10)

    def lambda_2F6C():
        OP_8F(0xFE, 0xFFFFE7C8, 0x0, 0x2B84, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_2F6C)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 6)
    OP_7D(0x0, 0x8, 0x14, 0xC8)

    def lambda_2F99():
        OP_8F(0xFE, 0xFFFFE408, 0x0, 0x35B6, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_2F99)
    WaitChrThread(0x8, 0x0)
    OP_7D(0x1, 0x8, 0x0, 0x0)
    OP_22(0x84, 0x0, 0x64)
    Sleep(300)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_2FD4():
        OP_6D(-5960, 0, 10310, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2FD4)

    def lambda_2FEC():
        OP_6B(2060, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2FEC)

    def lambda_2FFC():
        OP_67(0, 4360, -10000, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2FFC)

    def lambda_3014():
        OP_6C(110000, 400)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3014)

    def lambda_3024():
        OP_8F(0xFE, 0xFFFFDFE4, 0x0, 0x2A30, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_3024)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 2)

    def lambda_3049():
        OP_8C(0xFE, 245, 400)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_3049)
    OP_8C(0x8, 90, 1500)
    OP_8C(0x8, 0, 1500)
    OP_8C(0x8, 270, 1500)
    OP_8C(0x8, 180, 1500)
    OP_8C(0x8, 90, 1500)
    OP_8C(0x8, 66, 1500)
    WaitChrThread(0x8, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x9, 0x4)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 7)
    PlayEffect(0x0, 0xFF, 0x9, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 6)

    def lambda_30EC():
        OP_96(0xFE, 0xFFFFFE5C, 0x0, 0x3458, 0x960, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_30EC)
    OP_51(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)

    def lambda_311A():
        OP_6D(-1220, 0, 8000, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_311A)

    def lambda_3132():
        OP_67(0, 3400, -10000, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3132)

    def lambda_314A():
        OP_6C(154000, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_314A)

    def lambda_315A():
        OP_6B(2320, 400)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_315A)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 9)

    def lambda_3174():
        OP_96(0xFE, 0xFFFFFE5C, 0x0, 0x3458, 0x7D0, 0x1770)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_3174)
    OP_51(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0xA3, 0x0, 0x64)
    Sleep(100)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 4)

    def lambda_31B1():
        OP_99(0xFE, 0x4, 0x5, 0x708)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_31B1)
    WaitChrThread(0x8, 0x1)
    OP_44(0x8, 0x0)
    OP_44(0x9, 0x0)

    def lambda_31CE():
        OP_9E(0xFE, 0x14, 0x0, 0x12C, 0xFA0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_31CE)
    OP_22(0x209, 0x0, 0x64)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)
    Sleep(200)
    WaitChrThread(0x9, 0x0)

    def lambda_320B():
        OP_6D(-2640, 0, 11340, 600)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_320B)

    def lambda_3223():
        OP_67(0, 6180, -10000, 600)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3223)

    def lambda_323B():
        OP_6C(130000, 600)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_323B)

    def lambda_324B():
        OP_96(0xFE, 0xD0C, 0x0, 0x3480, 0x7D0, 0x2328)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_324B)

    def lambda_3269():
        OP_96(0xFE, 0xFFFFDF44, 0x0, 0x2C74, 0x7D0, 0xFA0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_3269)
    Sleep(100)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 3)
    WaitChrThread(0x8, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    OP_51(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_32AB():
        OP_6D(-710, 0, 11560, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_32AB)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 9)

    def lambda_32CD():
        OP_96(0xFE, 0xFFFFEBA6, 0x0, 0x2E72, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_32CD)
    WaitChrThread(0x9, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    OP_51(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 4)
    ClearChrFlags(0x8, 0x4)
    ClearChrFlags(0x9, 0x4)

    def lambda_3314():
        OP_9E(0xFE, 0xA, 0x0, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3314)
    WaitChrThread(0x8, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 0)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #11
        0x9,
        "#175F#5P唔……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x9, 0x1)
    Fade(500)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x9, 28)
    SetChrSubChip(0x9, 4)
    OP_0D()

    ChrTalk(    #12
        0x8,
        (
            "#1127F#6P防守基本相同！\x02\x03",

            "注意对方动作的意图，\x01",
            "同时想好攻守的步骤！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x9,
        "#178F#5P是！\x02",
    )

    CloseMessageWindow()

    def lambda_33D4():
        OP_6D(1340, 0, 10040, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_33D4)

    def lambda_33EC():
        OP_67(0, 2660, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_33EC)
    Sleep(500)

    ChrTalk(    #14 op#A op#5
        0x9,
        "#177F#5P#3S#15A哈啊啊啊啊啊啊！\x05\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 7)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Sleep(500)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 8)
    OP_7D(0x0, 0x9, 0x32, 0x1F4)

    def lambda_3480():

        label("loc_3480")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_3480")

    QueueWorkItem2(0x9, 3, lambda_3480)

    def lambda_3491():
        OP_96(0xFE, 0x67C, 0x0, 0x3F01, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_3491)
    WaitChrThread(0x9, 0x0)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_34B9():
        OP_8F(0xFE, 0xFFFFF77C, 0x0, 0x358E, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_34B9)
    WaitChrThread(0x9, 0x0)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_34DE():
        OP_96(0xFE, 0xFFFFFD3A, 0x0, 0x2530, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_34DE)
    WaitChrThread(0x9, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    OP_7D(0x1, 0x9, 0x0, 0x0)
    OP_44(0x9, 0x3)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_351B():
        OP_6D(-2540, 0, 11300, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_351B)

    def lambda_3533():
        OP_67(0, 4420, -10000, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3533)
    SetChrChipByIndex(0x9, 28)
    SetChrSubChip(0x9, 12)

    def lambda_3555():
        OP_96(0xFE, 0xFFFFF218, 0x0, 0x2954, 0x640, 0xFA0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_3555)
    OP_51(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    SetChrChipByIndex(0x9, 28)
    SetChrSubChip(0x9, 0)
    Sleep(200)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 3)

    def lambda_359C():

        label("loc_359C")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_359C")

    QueueWorkItem2(0x8, 3, lambda_359C)

    def lambda_35AD():
        OP_96(0xFE, 0xFFFFEACA, 0x0, 0x3DFE, 0x258, 0x1388)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_35AD)
    WaitChrThread(0x9, 0x0)
    OP_22(0x84, 0x0, 0x64)
    OP_51(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x9, 28)
    SetChrSubChip(0x9, 1)
    WaitChrThread(0x8, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 4)
    Sleep(100)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_360C():
        OP_6D(-5430, 0, 14290, 600)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_360C)

    def lambda_3624():
        OP_6C(190000, 600)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3624)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 3)

    def lambda_363E():
        OP_96(0xFE, 0xFFFFEA02, 0x0, 0x4C36, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_363E)
    WaitChrThread(0x8, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 4)
    Sleep(100)
    OP_44(0x8, 0x3)

    def lambda_3679():
        OP_6D(-6870, 0, 16030, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3679)

    def lambda_3691():
        OP_67(0, 3360, -10000, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3691)

    def lambda_36A9():
        OP_6C(238000, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_36A9)

    def lambda_36B9():
        OP_6B(2180, 400)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_36B9)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 8)
    OP_7D(0x0, 0x9, 0x32, 0x1F4)
    TurnDirection(0x9, 0x8, 0)

    def lambda_36E2():
        OP_8F(0xFE, 0xFFFFED7C, 0x0, 0x3ECF, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_36E2)
    Sleep(100)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 0)
    Sleep(200)
    OP_7D(0x1, 0x9, 0x0, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_3722():
        OP_8F(0xFE, 0xFFFFEB38, 0x0, 0x4736, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_3722)
    WaitChrThread(0x9, 0x0)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 3)
    WaitChrThread(0x8, 0x0)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 1)
    PlayEffect(0x0, 0xFF, 0x9, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)

    def lambda_37A3():
        OP_6D(-6250, 0, 15120, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_37A3)

    def lambda_37BB():
        OP_6B(1980, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_37BB)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 0)
    Sleep(400)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_37E3():
        OP_8F(0xFE, 0xFFFFEC82, 0x0, 0x431C, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_37E3)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 1)

    def lambda_3808():
        OP_8F(0xFE, 0xFFFFF038, 0x0, 0x3B9C, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_3808)
    WaitChrThread(0x8, 0x0)
    PlayEffect(0x0, 0xFF, 0x9, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)

    def lambda_3870():
        OP_6D(-5360, 0, 13720, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3870)

    def lambda_3888():
        OP_6C(236000, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3888)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 5)

    def lambda_38B5():
        OP_96(0xFE, 0xFFFFF650, 0x0, 0x2C10, 0x258, 0xFA0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_38B5)
    Sleep(400)

    def lambda_38D8():
        OP_8F(0xFE, 0xFFFFEE44, 0x0, 0x3F48, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_38D8)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 1)
    WaitChrThread(0x9, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x9, 28)
    SetChrSubChip(0x9, 5)

    def lambda_3911():
        OP_8F(0xFE, 0xFFFFF36C, 0x0, 0x32E6, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_3911)
    WaitChrThread(0x8, 0x0)
    PlayEffect(0x0, 0xFF, 0x8, 0, 500, -1500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)

    def lambda_3979():
        OP_6B(1780, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3979)

    def lambda_3989():
        OP_9E(0xFE, 0xA, 0x0, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3989)

    def lambda_39A3():
        OP_9E(0xFE, 0xA, 0x0, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_39A3)
    WaitChrThread(0x101, 0x0)
    PlayEffect(0x0, 0xFF, 0x8, 0, 500, -2000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x9, 0, 500, 2000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)

    def lambda_3A31():
        OP_6D(-3420, 0, 13940, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3A31)

    def lambda_3A49():
        OP_67(0, 6500, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3A49)

    def lambda_3A61():
        OP_6C(148000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3A61)

    def lambda_3A71():
        OP_6B(2180, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3A71)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 2)
    SetChrChipByIndex(0x9, 28)
    SetChrSubChip(0x9, 3)
    OP_43(0x8, 0x3, 0x0, 0xD)

    def lambda_3A9C():
        OP_96(0xFE, 0xFFFFECC8, 0x0, 0x2B84, 0x4B0, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_3A9C)
    OP_51(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0x9, 0x3, 0x0, 0xE)

    def lambda_3ACC():
        OP_96(0xFE, 0xFFFFF542, 0x0, 0x4862, 0x4B0, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_3ACC)
    OP_51(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x9, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    OP_51(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x9, 28)
    SetChrSubChip(0x9, 4)
    WaitChrThread(0x8, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    OP_51(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 0)
    Sleep(200)

    def lambda_3B38():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x258, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_3B38)
    WaitChrThread(0x9, 0x0)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_3B60():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x320, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_3B60)
    WaitChrThread(0x9, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    OP_7D(0x0, 0x9, 0x32, 0x1F4)

    def lambda_3B90():
        OP_6D(-3810, 0, 12730, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3B90)

    def lambda_3BA8():
        OP_67(0, 4600, -10000, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3BA8)

    def lambda_3BC0():

        label("loc_3BC0")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_3BC0")

    QueueWorkItem2(0x9, 3, lambda_3BC0)

    def lambda_3BD1():

        label("loc_3BD1")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_3BD1")

    QueueWorkItem2(0x8, 3, lambda_3BD1)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 8)

    def lambda_3BEC():
        OP_96(0xFE, 0xFFFFF164, 0x0, 0x3B38, 0x320, 0x1388)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_3BEC)
    WaitChrThread(0x9, 0x0)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_3C14():
        OP_6C(204000, 800)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3C14)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 8)

    def lambda_3C2E():
        OP_96(0xFE, 0xFFFFF7A4, 0x0, 0x2E40, 0x320, 0x1388)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_3C2E)
    WaitChrThread(0x9, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 5)

    def lambda_3C60():
        OP_96(0xFE, 0xFFFFFA2E, 0x0, 0x3A34, 0x320, 0x1388)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_3C60)
    WaitChrThread(0x9, 0x0)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_3C88():
        OP_6C(122000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3C88)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 8)

    def lambda_3CA2():
        OP_96(0xFE, 0xFFFFEFE8, 0x0, 0x367E, 0x320, 0x1388)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_3CA2)
    WaitChrThread(0x9, 0x0)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_3CCA():
        OP_6D(-3690, 0, 10320, 800)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3CCA)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 5)

    def lambda_3CEC():
        OP_96(0xFE, 0xFFFFE994, 0x0, 0x3D40, 0x320, 0x1388)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_3CEC)
    WaitChrThread(0x9, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 8)

    def lambda_3D1E():
        OP_96(0xFE, 0xFFFFE1A6, 0x0, 0x3340, 0x320, 0x1388)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_3D1E)
    WaitChrThread(0x9, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    OP_7D(0x1, 0x9, 0x0, 0x0)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 7)
    OP_44(0x9, 0x3)
    OP_44(0x8, 0x3)
    Sleep(200)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_3D6E():
        OP_6D(-400, 0, 8240, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3D6E)

    def lambda_3D86():
        OP_67(0, 3300, -10000, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3D86)
    SetChrChipByIndex(0x9, 28)
    SetChrSubChip(0x9, 4)

    def lambda_3DA8():
        OP_8F(0xFE, 0xFFFFF9CA, 0x0, 0x231E, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_3DA8)

    def lambda_3DC3():
        OP_99(0xFE, 0x4, 0x6, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3DC3)
    Sleep(100)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 2)
    OP_8C(0x8, 205, 0)

    def lambda_3DE9():
        OP_8F(0xFE, 0xFFFFF0CE, 0x0, 0x319C, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_3DE9)

    def lambda_3E04():
        OP_9E(0xFE, 0x14, 0x0, 0x190, 0xFA0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3E04)
    PlayEffect(0x0, 0xFF, 0x8, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)
    WaitChrThread(0x9, 0x0)
    WaitChrThread(0x8, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_3E79():
        OP_6D(-1000, 0, 11820, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3E79)
    SetChrChipByIndex(0x9, 28)
    SetChrSubChip(0x9, 4)

    def lambda_3E9B():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x258, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_3E9B)
    OP_43(0x9, 0x3, 0x0, 0x10)
    WaitChrThread(0x9, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(200)

    def lambda_3ECF():
        OP_8F(0xFE, 0xFFFFE6A6, 0x0, 0x3EEE, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_3ECF)

    def lambda_3EEA():
        OP_99(0xFE, 0x4, 0x6, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3EEA)
    Sleep(50)
    OP_22(0x84, 0x0, 0x64)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 3)
    OP_8C(0x8, 257, 0)

    def lambda_3F15():
        OP_96(0xFE, 0xFFFFFF38, 0x0, 0x3584, 0x320, 0x1B58)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_3F15)
    WaitChrThread(0x8, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 4)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)

    def lambda_3F55():
        OP_6D(-1000, 0, 13940, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3F55)

    def lambda_3F6D():
        OP_6C(118000, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3F6D)
    SetChrChipByIndex(0x9, 28)
    SetChrSubChip(0x9, 4)

    def lambda_3F87():
        OP_96(0xFE, 0xFFFFF236, 0x0, 0x4A4C, 0x4B0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_3F87)
    OP_43(0x9, 0x3, 0x0, 0xE)
    WaitChrThread(0x9, 0x3)
    OP_8C(0x9, 147, 0)
    WaitChrThread(0x9, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 3)
    Sleep(50)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 4)
    OP_43(0x8, 0x3, 0x0, 0xF)
    Sleep(200)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x4)

    def lambda_3FF5():
        OP_6D(1360, 0, 15090, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3FF5)

    def lambda_400D():
        OP_6C(64000, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_400D)

    def lambda_401D():
        OP_6B(1780, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_401D)

    def lambda_402D():
        OP_8F(0xFE, 0xFFFFFC4A, 0x190, 0x396C, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_402D)
    WaitChrThread(0x9, 0x0)

    def lambda_404D():
        OP_9E(0xFE, 0x14, 0x0, 0x12C, 0xFA0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_404D)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 5)
    OP_22(0x209, 0x0, 0x64)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 6)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x9, 0x0)

    def lambda_408E():
        OP_6D(-1170, 0, 17520, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_408E)

    def lambda_40A6():
        OP_67(0, 4340, -10000, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_40A6)

    def lambda_40BE():
        OP_6B(2240, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_40BE)

    def lambda_40CE():
        OP_6C(45000, 400)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_40CE)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 4)
    OP_43(0x8, 0x3, 0x0, 0xF)
    ClearChrFlags(0x9, 0x4)

    def lambda_40F4():
        OP_96(0xFE, 0xFFFFEC64, 0x0, 0x4C86, 0x4B0, 0xFA0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_40F4)
    OP_51(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x8, 0x3)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 6)
    WaitChrThread(0x9, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    OP_51(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 4)

    def lambda_414B():
        OP_9E(0xFE, 0xA, 0x0, 0x190, 0xFA0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_414B)
    Sleep(200)

    def lambda_416A():
        OP_6D(-1660, 0, 17640, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_416A)

    def lambda_4182():
        OP_6C(80000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4182)
    Fade(250)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 8)
    OP_0D()
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)

    def lambda_41AC():
        OP_6D(-4760, 0, 21530, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_41AC)

    def lambda_41C4():
        OP_6B(1800, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_41C4)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 9)
    OP_7D(0x0, 0x8, 0xA, 0x1F4)

    def lambda_41EF():
        OP_96(0xFE, 0xFFFFE110, 0x0, 0x59C4, 0xC8, 0x1388)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_41EF)
    Sleep(100)
    OP_22(0x9B, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x9, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 7)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 3)
    WaitChrThread(0x8, 0x0)

    def lambda_4265():
        OP_9E(0xFE, 0x1E, 0x0, 0x190, 0x1770)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4265)
    OP_7D(0x1, 0x8, 0x0, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)

    def lambda_4295():
        OP_6D(-5050, 0, 21050, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4295)

    def lambda_42AD():
        OP_6B(2160, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_42AD)

    def lambda_42BD():
        OP_6C(8000, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_42BD)

    def lambda_42CD():
        OP_8C(0xFE, 35, 400)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_42CD)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 3)
    OP_7D(0x0, 0x8, 0x32, 0xC8)

    def lambda_42ED():
        OP_96(0xFE, 0xFFFFE304, 0x0, 0x3F0C, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_42ED)
    WaitChrThread(0x9, 0x3)

    def lambda_4310():
        OP_8C(0xFE, 305, 400)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_4310)
    WaitChrThread(0x8, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    OP_7D(0x1, 0x8, 0x0, 0x0)

    def lambda_4330():
        OP_6D(-3930, 0, 22440, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4330)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 6)

    def lambda_435B():
        OP_8F(0xFE, 0xFFFFE8AE, 0x0, 0x4704, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_435B)
    OP_8C(0x8, 270, 1000)
    OP_8C(0x8, 180, 1000)
    OP_8C(0x8, 90, 1000)
    TurnDirection(0x8, 0x9, 1000)
    WaitChrThread(0x8, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x0, 0xFF, 0x9, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 7)
    TurnDirection(0x9, 0x8, 0)

    def lambda_43EB():
        OP_96(0xFE, 0xFFFFF704, 0x0, 0x5EB0, 0x578, 0xFA0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_43EB)
    OP_51(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x9, 0x0)
    OP_51(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 4)
    Sleep(400)

    def lambda_4438():
        OP_6D(-2680, 0, 21130, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4438)

    def lambda_4450():
        OP_6B(1820, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4450)

    def lambda_4460():
        OP_6C(296000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4460)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 9)

    def lambda_447A():

        label("loc_447A")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_447A")

    QueueWorkItem2(0x8, 3, lambda_447A)

    def lambda_448B():
        OP_96(0xFE, 0xFFFFF704, 0x0, 0x4466, 0x258, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_448B)

    def lambda_44A9():

        label("loc_44A9")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_44A9")

    QueueWorkItem2(0x9, 3, lambda_44A9)
    WaitChrThread(0x8, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    OP_44(0x8, 0x3)
    OP_44(0x9, 0x3)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 0)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    Sleep(500)

    ChrTalk(    #15
        0xA,
        "#163F#7P嗯，到此为止。\x02",
    )

    CloseMessageWindow()
    Sleep(100)

    def lambda_450B():
        OP_67(0, 4810, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_450B)

    def lambda_4523():
        OP_6B(2760, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4523)
    OP_22(0xBF, 0x0, 0x64)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x40)
    ClearChrFlags(0x9, 0x20)
    ClearChrFlags(0x9, 0x40)

    ChrTalk(    #16
        0x9,
        "#175F#2P呼、呼、呼……\x02",
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 6)
    OP_0D()
    Sleep(500)

    ChrTalk(    #17
        0x8,
        (
            "#1125F#6P呵呵，真了不起。\x02\x03",

            "#1120F之前，我只是教了你一些\x01",
            "基础的东西而已……\x02\x03",

            "没想到，你竟能靠自己的努力达到如此的水平。\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #18
        0x9,
        (
            "#171F#2P哪……哪里……\x02\x03",

            "我还有很多的不足之处……\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0xA, 0xFFFFEC8C, 0x0, 0x5190, 0xDAC, 0x0)

    ChrTalk(    #19
        0xA,
        "#165F#5P这场比试很有水准。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x9,
        "#175F#2P将军，可是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xA,
        (
            "#163F#5P说实话，我没想到你\x01",
            "能达到这个地步。\x02\x03",

            "就算是有相当水准的人，\x01",
            "只要和卡西乌斯交手几个回合，\x01",
            "剑也会脱手的。\x02\x03",

            "#165F你可以说是年轻一辈中最强的了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x9,
        (
            "#173F#2P惭、惭愧……\x02\x03",

            "#176F不过机会难得……\x02\x03",

            "#172F真希望能够一直打到\x01",
            "我被击溃为止。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xA,
        (
            "#164F#5P哈哈哈哈！\x01",
            "真有志气。\x02\x03",

            "#165F怎么样，卡西乌斯？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        (
            "#1125F#6P呵呵，我也想\x01",
            "奉陪到底啊……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xB, 12950, 0, 21590, 270)
    SetChrPos(0xC, 13170, 0, 22870, 270)
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x8, 0)
    SetChrSubChip(0x8, 0)
    OP_0D()
    Sleep(500)
    TurnDirection(0x8, 0xB, 400)
    Sleep(500)

    ChrTalk(    #25
        0x8,
        "#1120F#5P不过好像有客人来了。\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_62(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrChipByIndex(0x9, 1)
    SetChrSubChip(0x9, 0)

    def lambda_48AE():
        OP_6D(6670, 0, 21130, 2000)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_48AE)

    def lambda_48C6():
        TurnDirection(0x9, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_48C6)

    def lambda_48D4():

        label("loc_48D4")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_48D4")

    QueueWorkItem2(0x8, 1, lambda_48D4)
    WaitChrThread(0x9, 0x2)
    Sleep(500)

    def lambda_48EF():

        label("loc_48EF")

        TurnDirection(0x9, 0xB, 400)
        OP_48()
        Jump("loc_48EF")

    QueueWorkItem2(0x9, 1, lambda_48EF)

    def lambda_4900():
        OP_8E(0xFE, 0x226, 0x0, 0x4D44, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_4900)
    Sleep(500)

    def lambda_4920():
        OP_8E(0xFE, 0x5E6, 0x0, 0x5302, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_4920)
    OP_69(0x24, 0x1388)
    WaitChrThread(0xB, 0x1)
    WaitChrThread(0xC, 0x1)
    OP_44(0x8, 0x1)
    OP_44(0x9, 0x1)

    ChrTalk(    #26
        0xC,
        (
            "#692F哎呀～真是让我\x01",
            "大饱眼福了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xB,
        "#703F两位辛苦了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x9, 400)
    Sleep(300)

    ChrTalk(    #28
        0xB,
        (
            "#701F#6P舒华兹上尉，\x01",
            "你实在是非常出色。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x9,
        "#171F希德中校……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0xC, 400)
    Sleep(300)

    ChrTalk(    #30
        0x9,
        "#173F请问这位是……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x9, 400)
    Sleep(300)

    ChrTalk(    #31
        0xC,
        (
            "#691F#6P我是中央工房派来的，\x01",
            "叫格斯塔夫。\x02\x03",

            "#693F请多指教，队长。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x9,
        (
            "#173F失、失礼了。\x02\x03",

            "#176F我是王室亲卫队中队长。\x01",
            "尤莉亚·舒华兹上尉。\x02\x03",

            "#170F也请你多多指教。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xA,
        (
            "#165F#5P嗯，看来该做的事\x01",
            "都已经做完了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4AE5():
        OP_6D(-6760, 0, 19100, 1500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4AE5)
    OP_8C(0x8, 302, 400)
    WaitChrThread(0x8, 0x1)

    ChrTalk(    #34
        0x8,
        (
            "#1120F#6P各位，余兴节目结束。\x02\x03",

            "请返回各自的工作岗位。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4B44():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_4B44)
    Sleep(50)

    def lambda_4B57():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_4B57)

    def lambda_4B65():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4B65)
    Sleep(50)

    def lambda_4B78():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_4B78)

    def lambda_4B86():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4B86)
    Sleep(50)

    def lambda_4B99():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_4B99)

    def lambda_4BA7():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_4BA7)
    Sleep(50)

    def lambda_4BBA():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_4BBA)

    def lambda_4BC8():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4BC8)
    Sleep(50)

    def lambda_4BDB():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_4BDB)

    def lambda_4BE9():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_4BE9)
    Sleep(50)

    def lambda_4BFC():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_4BFC)
    Sleep(500)
    SetMessageWindowPos(140, 120, -1, -1)
    SetChrName("士兵们")

    AnonymousTalk(    #35
        "\x07\x00#5S是，长官！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_43(0x8, 0x0, 0x0, 0x15)
    OP_43(0x8, 0x1, 0x0, 0x16)
    WaitChrThread(0x8, 0x0)
    WaitChrThread(0x8, 0x1)

    def lambda_4C67():
        OP_69(0xFE, 0x7D0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_4C67)
    TurnDirection(0x8, 0x9, 400)
    WaitChrThread(0x24, 0x1)

    ChrTalk(    #36
        0xC,
        (
            "#691F#6P那么，能不能\x01",
            "马上让我看看机关部？\x02\x03",

            "我想尽可能在今天之内\x01",
            "找到头绪。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x9,
        "#171F嗯，明白了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 400)
    Sleep(500)

    ChrTalk(    #38
        0x9,
        (
            "#176F#2P那么我先告退了！\x02\x03",

            "#171F准将，感谢您\x01",
            "今天给予我的指导！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x8,
        (
            "#1121F#6P这不算什么。\x01",
            "我也算是好好锻炼了一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xA,
        (
            "#165F#5P维修长，上尉。\x01",
            "埃尔赛尤号就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x9,
        "#172F#2P是！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xA, 400)
    Sleep(300)

    ChrTalk(    #42
        0xC,
        "#691F请交给我们吧。\x02",
    )

    CloseMessageWindow()

    def lambda_4DD8():

        label("loc_4DD8")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_4DD8")

    QueueWorkItem2(0x8, 3, lambda_4DD8)

    def lambda_4DE9():

        label("loc_4DE9")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_4DE9")

    QueueWorkItem2(0xB, 3, lambda_4DE9)
    OP_8C(0x9, 70, 400)

    def lambda_4E01():
        OP_6D(-1480, 0, 22850, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4E01)

    def lambda_4E19():
        OP_8E(0xFE, 0x3DF4, 0x0, 0x5BC2, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4E19)
    OP_8C(0xC, 70, 400)

    def lambda_4E3B():
        OP_8E(0xFE, 0x3DF4, 0x0, 0x5BC2, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_4E3B)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0xC, 0x1)
    Sleep(500)

    def lambda_4E65():
        OP_6D(-3450, 0, 20710, 2000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4E65)

    def lambda_4E7D():
        OP_6C(308000, 2000)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4E7D)

    def lambda_4E8D():
        OP_6E(325, 2000)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_4E8D)
    WaitChrThread(0xB, 0x1)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xC, 0x80)
    OP_44(0x8, 0x3)
    OP_44(0xB, 0x3)

    ChrTalk(    #43
        0xB,
        (
            "#701F#5P呵呵……\x01",
            "她真是不简单呢。\x02\x03",

            "今后还会不断成长的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x8,
        (
            "#1125F#5P嗯，是啊。\x02\x03",

            "#1120F跟你和理查德\x01",
            "只差一两步了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xA,
        (
            "#164F#5P呼，看到这样的年轻人\x01",
            "连我这把老骨头也热血沸腾了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 148, 400)
    Sleep(300)

    ChrTalk(    #46
        0xA,
        "#165F#5P卡西乌斯，一会儿也和我切磋切磋吧？\x02",
    )

    CloseMessageWindow()

    def lambda_4FA8():
        OP_8C(0xFE, 344, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4FA8)

    def lambda_4FB6():
        OP_8C(0xFE, 267, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_4FB6)
    WaitChrThread(0x8, 0x1)
    Sleep(300)

    ChrTalk(    #47
        0x8,
        (
            "#1123F#6P将军……\x02\x03",

            "还是应该考虑\x01",
            "一下您的年龄吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xA,
        "#160F#5P唔唔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x8,
        (
            "#1120F#6P听说您在去年的武术大会上\x01",
            "也大出了风头一番是吗？\x02\x03",

            "是不是也该让年轻人\x01",
            "有点进步的余地？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xA,
        (
            "#163F#5P哼，所以我才\x01",
            "把司令的位置交给你了。\x02\x03",

            "#165F你既然都这么说了，\x01",
            "那以后就不能再对工作有所抱怨了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x8,
        "#1123F#6P呀，早知道就不提了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xB,
        "#701F#6P呵呵……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xB, 400)
    Sleep(300)

    ChrTalk(    #53
        0xA,
        (
            "#161F#5P对了，希德中校。\x01",
            "今天好像要出发了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xB,
        (
            "#701F#6P是的，正午时分。\x02\x03",

            "预计率领2艘警备艇\x01",
            "三个中队前去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xA,
        (
            "#165F#5P我也会去参加签字仪式的，\x01",
            "不过在此之前抽不开身来。\x02\x03",

            "守卫王都的任务就拜托你了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xB,
        (
            "#703F#6P请您放心。\x02\x03",

            "#701F我会和游击士协会\x01",
            "一起妥善应对的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xA,
        (
            "#161F#5P嗯、嗯……\x02\x03",

            "#163F虽然十分遗憾，\x01",
            "不过这次实在没办法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x8,
        (
            "#1120F#6P呵呵，将军你也开始变得\x01",
            "不再那样讨厌游击士协会了吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_20(0x7D0)
    OP_21()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C3100   ._SN", 100, 0, 0)
    IdleLoop()
    SetMapFlags(0x10)
    Return()

    # Function_11_F2D end

    def Function_12_52DC(): pass

    label("Function_12_52DC")

    EventBegin(0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    SetChrPos(0x8, -2300, 0, 17510, 0)
    SetChrPos(0x9, -2300, 0, 24240, 180)
    SetChrPos(0xA, -4300, 0, 20880, 90)
    SetChrPos(0xD, -12080, 0, 15010, 90)
    SetChrPos(0xE, -12900, 0, 16840, 90)
    SetChrPos(0xF, -13490, 0, 18730, 90)
    SetChrPos(0x10, -14010, 0, 15710, 90)
    SetChrPos(0x11, -14670, 0, 17570, 90)
    SetChrPos(0x12, -15200, 0, 19820, 90)
    SetChrPos(0x1D, -13510, 0, 22660, 90)
    SetChrPos(0x1E, -12880, 0, 24340, 90)
    SetChrPos(0x1F, -11920, 0, 26130, 90)
    SetChrPos(0x20, -15170, 0, 22090, 90)
    SetChrPos(0x21, -14580, 0, 23690, 90)
    SetChrPos(0x22, -13960, 0, 25780, 90)
    SetChrChipByIndex(0x9, 1)
    SetChrSubChip(0x9, 0)
    OP_6D(-16450, 0, 14000, 0)
    OP_67(0, 7580, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(247000, 0)
    OP_6E(316, 0)
    FadeToBright(1000, 0)

    def lambda_547E():
        OP_6D(-16450, 0, 28000, 5000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_547E)

    def lambda_5496():
        OP_6C(310000, 5000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_5496)
    WaitChrThread(0x8, 0x1)

    def lambda_54AB():
        OP_6D(-2680, 0, 21130, 3000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_54AB)

    def lambda_54C3():
        OP_67(0, 4810, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_54C3)

    def lambda_54DB():
        OP_6B(2760, 4500)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_54DB)

    def lambda_54EB():
        OP_6C(296000, 4500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_54EB)

    def lambda_54FB():
        OP_6E(443, 4500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_54FB)
    WaitChrThread(0x9, 0x1)
    Sleep(1000)

    ChrTalk(    #59
        0xA,
        (
            "#160F#4P双方，预备！\x02\x03",

            "#3S开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x24, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x24, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x24, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(    #60
        0x9,
        "#170F#6P──呀啊啊啊啊啊！\x02",
    )

    CloseMessageWindow()

    def lambda_5599():
        OP_96(0xFE, 0xFFFFF704, 0x0, 0x4F9C, 0x2BC, 0x1B58)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5599)

    def lambda_55B7():
        OP_96(0xFE, 0xFFFFF704, 0x0, 0x5384, 0x2BC, 0x1B58)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_55B7)
    WaitChrThread(0x8, 0x1)
    Sleep(500)

    def lambda_55DF():
        OP_96(0xFE, 0xFFFFF704, 0x0, 0x4466, 0x2BC, 0x1B58)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_55DF)

    def lambda_55FD():
        OP_96(0xFE, 0xFFFFF704, 0x0, 0x5EB0, 0x2BC, 0x1B58)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_55FD)
    WaitChrThread(0x8, 0x1)
    Sleep(1000)

    ChrTalk(    #61
        0x9,
        "#170F#6P唔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x8,
        (
            "#1120F#6P怎么回事！？\x01",
            "行动太过直线化！\x02\x03",

            "你用的是细剑，就应该使出\x01",
            "流畅的进攻套路！\x02\x03",

            "想想我教过你的东西！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x9,
        (
            "#170F#6P是……\x02\x03",

            "……是！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_56C4():
        OP_96(0xFE, 0xFFFFF704, 0x0, 0x4F9C, 0x2BC, 0x1B58)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_56C4)

    def lambda_56E2():
        OP_96(0xFE, 0xFFFFF704, 0x0, 0x5384, 0x2BC, 0x1B58)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_56E2)
    WaitChrThread(0x8, 0x1)
    Sleep(500)

    def lambda_570A():
        OP_96(0xFE, 0xFFFFF704, 0x0, 0x4466, 0x2BC, 0x1B58)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_570A)

    def lambda_5728():
        OP_96(0xFE, 0xFFFFF704, 0x0, 0x5EB0, 0x2BC, 0x1B58)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5728)
    WaitChrThread(0x8, 0x1)
    Sleep(1000)

    ChrTalk(    #64
        0x8,
        (
            "#1120F#6P这就对了……\x02\x03",

            "那么，接招吧！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_577B():
        OP_96(0xFE, 0xFFFFF704, 0x0, 0x4F9C, 0x2BC, 0x1B58)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_577B)

    def lambda_5799():
        OP_96(0xFE, 0xFFFFF704, 0x0, 0x5384, 0x2BC, 0x1B58)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5799)
    WaitChrThread(0x8, 0x1)
    Sleep(500)

    def lambda_57C1():
        OP_96(0xFE, 0xFFFFF704, 0x0, 0x4466, 0x2BC, 0x1B58)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_57C1)

    def lambda_57DF():
        OP_96(0xFE, 0xFFFFF704, 0x0, 0x5EB0, 0x2BC, 0x1B58)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_57DF)
    WaitChrThread(0x8, 0x1)
    Sleep(1000)

    ChrTalk(    #65
        0x9,
        "#170F#6P唔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x8,
        (
            "#1120F#6P防守基本相同！\x02\x03",

            "注意对方动作的意图，\x01",
            "同时想好攻守的步骤！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x9,
        (
            "#170F#6P是！\x02\x03",

            "哈啊啊啊啊啊啊！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5887():
        OP_96(0xFE, 0xFFFFF704, 0x0, 0x4F9C, 0x2BC, 0x1B58)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5887)

    def lambda_58A5():
        OP_96(0xFE, 0xFFFFF704, 0x0, 0x5384, 0x2BC, 0x1B58)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_58A5)
    WaitChrThread(0x8, 0x1)
    Sleep(500)

    def lambda_58CD():
        OP_96(0xFE, 0xFFFFF704, 0x0, 0x4466, 0x2BC, 0x1B58)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_58CD)

    def lambda_58EB():
        OP_96(0xFE, 0xFFFFF704, 0x0, 0x5EB0, 0x2BC, 0x1B58)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_58EB)
    WaitChrThread(0x8, 0x1)
    Sleep(1000)
    OP_22(0xBF, 0x0, 0x64)
    Sleep(6000)

    ChrTalk(    #68
        0x9,
        "#170F#6P呼、呼、呼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x8,
        (
            "#1120F#6P呵呵，真了不起。\x02\x03",

            "以前我只是教给你一些\x01",
            "基础的东西而已……\x02\x03",

            "没想到，你竟能靠自己的努力达到如此的水平。\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x9, 1)
    OP_0D()

    ChrTalk(    #70
        0x9,
        (
            "#170F#6P不……不不……\x02\x03",

            "我还大有不足之处……\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0xA, 0xFFFFF362, 0x0, 0x5190, 0xBB8, 0x0)
    Sleep(1000)
    WaitChrThread(0xA, 0x0)

    ChrTalk(    #71
        0xA,
        (
            "#160F#4P嗯，到此为止吧。\x02\x03",

            "这场比试很有水准。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x9,
        "#170F#6P将军，可是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xA,
        (
            "#160F#4P说实话，我没想到你\x01",
            "能坚持到这一步。\x02\x03",

            "就算是有相当水准的人，\x01",
            "只要和卡西乌斯交手几个回合，\x01",
            "剑也会脱手的。\x02\x03",

            "能坚持到这一步。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x9,
        (
            "#170F#6P惭、惭愧……\x02\x03",

            "不过机会难得……\x02\x03",

            "真希望能够一直打到\x01",
            "我被击溃为止\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xA,
        (
            "#160F#4P哈哈哈哈！\x01",
            "真有志气。\x02\x03",

            "怎么样，卡西乌斯？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x8,
        (
            "#1120F#6P呵呵，我也想\x01",
            "奉陪到底啊……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xB, 12950, 0, 21590, 270)
    SetChrPos(0xC, 13170, 0, 22870, 270)
    TurnDirection(0x8, 0xB, 400)
    Sleep(1000)

    ChrTalk(    #77
        0x8,
        "#1120F#6P不过好像有客人来了。\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x9, 0xB, 400)
    Sleep(1000)

    def lambda_5C1B():

        label("loc_5C1B")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_5C1B")

    QueueWorkItem2(0x8, 1, lambda_5C1B)
    OP_6D(6670, 0, 21130, 2000)

    def lambda_5C3D():
        OP_8E(0xFE, 0x226, 0x0, 0x4D44, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_5C3D)
    Sleep(300)

    def lambda_5C5D():
        OP_8E(0xFE, 0x262, 0x0, 0x55B4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_5C5D)
    OP_69(0x24, 0x1388)
    WaitChrThread(0xB, 0x1)
    WaitChrThread(0xC, 0x1)
    Sleep(1000)
    OP_44(0x8, 0x1)

    ChrTalk(    #78
        0xC,
        (
            "#690F哎呀～真是让我\x01",
            "大饱眼福了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xB,
        (
            "#700F两位辛苦了。\x02\x03",

            "舒华兹上尉，\x01",
            "你干得真不错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x9,
        (
            "#170F希德中校……\x02\x03",

            "请问这位是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xC,
        (
            "#690F他是中央工房派来的，\x01",
            "叫格斯塔夫。\x02\x03",

            "请多指教，队长小姐。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x9,
        (
            "#170F失、失礼了。\x02\x03",

            "我是王室亲卫队的中队长，\x01",
            "尤莉亚·舒华兹上尉。\x02\x03",

            "也请你多多指教。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xA,
        (
            "#160F嗯，看来该做的事\x01",
            "都已经做完了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5DD7():
        OP_6D(-6760, 0, 19100, 2000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5DD7)
    OP_8C(0x8, 302, 400)
    Sleep(2000)

    ChrTalk(    #84
        0x8,
        (
            "#1120F#3P各位，余兴节目结束。\x02\x03",

            "请返回各自的工作岗位。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 160, -1, -1)
    SetChrName("士兵们")

    AnonymousTalk(    #85
        "\x07\x00#4S YES！SIR！！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_43(0xD, 0x1, 0x0, 0x11)
    OP_43(0x10, 0x1, 0x0, 0x12)
    OP_43(0x1F, 0x1, 0x0, 0x13)
    OP_43(0x22, 0x1, 0x0, 0x14)
    Sleep(300)
    OP_43(0xE, 0x1, 0x0, 0x11)
    OP_43(0x11, 0x1, 0x0, 0x12)
    OP_43(0x1E, 0x1, 0x0, 0x13)
    OP_43(0x21, 0x1, 0x0, 0x14)
    Sleep(300)
    OP_43(0xF, 0x1, 0x0, 0x11)
    OP_43(0x12, 0x1, 0x0, 0x12)
    OP_43(0x1D, 0x1, 0x0, 0x13)
    OP_43(0x20, 0x1, 0x0, 0x14)
    OP_69(0x24, 0x3E8)
    Sleep(1000)
    TurnDirection(0x8, 0xB, 400)
    Sleep(1000)

    ChrTalk(    #86
        0xC,
        (
            "#690F那么，能不能\x01",
            "马上让我看看机关部？\x02\x03",

            "我想尽可能在今天之内\x01",
            "找到头绪。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x9,
        "#170F嗯，明白了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 400)
    Sleep(1000)

    ChrTalk(    #88
        0x9,
        (
            "#170F那么我先告退了！\x02\x03",

            "准将，感谢您\x01",
            "今天给予我的指导！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 343, 400)
    Sleep(1000)

    ChrTalk(    #89
        0x8,
        (
            "#1120F没什么的。\x01",
            "我也正好做了不错的锻炼。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xA,
        (
            "#160F维修长，上尉。\x01",
            "『埃尔赛尤』就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x9,
        "#170F是！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xC,
        "#690F请交给我们吧。\x02",
    )

    CloseMessageWindow()

    def lambda_6032():
        OP_8E(0xFE, 0x3DF4, 0x0, 0x5BC2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6032)
    Sleep(1000)

    def lambda_6052():
        OP_8E(0xFE, 0x3DF4, 0x0, 0x5BC2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_6052)
    Sleep(2000)

    def lambda_6072():
        OP_6D(-2510, 0, 20260, 2000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_6072)

    def lambda_608A():
        OP_6C(308000, 2000)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_608A)

    def lambda_609A():
        OP_6E(325, 2000)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_609A)
    WaitChrThread(0xB, 0x1)
    Sleep(1000)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xC, 0x80)

    ChrTalk(    #93
        0xB,
        (
            "#700F呵呵……\x01",
            "她真是不简单呢。\x02\x03",

            "今后还会不断成长的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x8,
        (
            "#1120F嗯，是啊。\x02\x03",

            "跟你和理查德\x01",
            "只差一两步了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 148, 400)
    Sleep(1000)

    ChrTalk(    #95
        0xA,
        (
            "#160F呼，看到这样的年轻人\x01",
            "连我这把老骨头也热血沸腾了。\x02\x03",

            "卡西乌斯，一会儿也和我切磋切磋吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x8,
        (
            "#1120F将军……\x02\x03",

            "您还是应该考虑一下\x01",
            "您的年龄吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xA,
        "#160F唔唔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x8,
        (
            "#1120F听说您在去年的武术大会上\x01",
            "大大地活跃了一番是吗？\x02\x03",

            "是不是也该让年轻人\x01",
            "有点进步的余地？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xA,
        (
            "#160F哼，所以我才\x01",
            "把司令的位置交给你了。\x02\x03",

            "你既然都这么说了，\x01",
            "以后就不能再对工作有所抱怨。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x8,
        "#1120F哎呀，早知道就不提了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xB,
        "#700F呵呵……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xA,
        (
            "#160F对了，希德中校。\x01",
            "今天好像要出发了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xB,
        (
            "#700F是的，正午时分。\x02\x03",

            "预计率领２艘警备艇\x01",
            "和３个中队前去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xA,
        (
            "#160F我也会去参加签字仪式的，\x01",
            "不过在此之前抽不开身来。\x02\x03",

            "守卫王都的任务就拜托你了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xB,
        (
            "#700F请您放心。\x02\x03",

            "我会和游击士协会\x01",
            "一起行动的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xA,
        (
            "#160F嗯、嗯……\x02\x03",

            "虽然十分遗憾，\x01",
            "不过这次实在没办法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x8,
        (
            "#1120F呵呵，将军你也开始变得\x01",
            "不再那样讨厌游击士协会了吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C3100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_12_52DC end

    def Function_13_644D(): pass

    label("Function_13_644D")

    OP_8C(0xFE, 90, 1000)
    OP_8C(0xFE, 0, 1000)
    OP_8C(0xFE, 270, 1000)
    OP_8C(0xFE, 180, 1000)
    OP_8C(0xFE, 90, 1000)
    TurnDirection(0xFE, 0x9, 1000)
    Return()

    # Function_13_644D end

    def Function_14_6478(): pass

    label("Function_14_6478")

    OP_8C(0xFE, 270, 1000)
    OP_8C(0xFE, 180, 1000)
    OP_8C(0xFE, 90, 1000)
    OP_8C(0xFE, 0, 1000)
    OP_8C(0xFE, 270, 1000)
    TurnDirection(0xFE, 0x8, 1000)
    Return()

    # Function_14_6478 end

    def Function_15_64A3(): pass

    label("Function_15_64A3")

    OP_8C(0xFE, 0, 1000)
    OP_8C(0xFE, 90, 1000)
    OP_8C(0xFE, 180, 1000)
    OP_8C(0xFE, 270, 1000)
    TurnDirection(0xFE, 0x9, 1000)
    Return()

    # Function_15_64A3 end

    def Function_16_64C7(): pass

    label("Function_16_64C7")

    OP_8C(0xFE, 90, 1400)
    OP_8C(0xFE, 0, 1400)
    OP_8C(0xFE, 270, 1400)
    OP_8C(0xFE, 180, 1400)
    OP_8C(0xFE, 90, 1400)
    TurnDirection(0xFE, 0x8, 1400)
    Return()

    # Function_16_64C7 end

    def Function_17_64F2(): pass

    label("Function_17_64F2")

    OP_8E(0xFE, 0x1C2, 0x0, 0x1982, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_17_64F2 end

    def Function_18_650C(): pass

    label("Function_18_650C")

    OP_8E(0xFE, 0xFFFF437C, 0x0, 0x42CC, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_18_650C end

    def Function_19_6526(): pass

    label("Function_19_6526")

    OP_8E(0xFE, 0xFFFFFD80, 0x0, 0x8980, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_19_6526 end

    def Function_20_6540(): pass

    label("Function_20_6540")

    OP_8E(0xFE, 0xFFFF81AC, 0x0, 0xFCC5, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_20_6540 end

    def Function_21_655A(): pass

    label("Function_21_655A")

    OP_43(0xF, 0x1, 0x0, 0x17)
    Sleep(600)
    OP_43(0x10, 0x1, 0x0, 0x18)
    Sleep(200)
    OP_43(0x12, 0x1, 0x0, 0x18)
    Sleep(200)
    OP_43(0xE, 0x1, 0x0, 0x17)
    Sleep(400)
    OP_43(0x11, 0x1, 0x0, 0x18)
    Sleep(600)
    OP_43(0xD, 0x1, 0x0, 0x17)
    Return()

    # Function_21_655A end

    def Function_22_659E(): pass

    label("Function_22_659E")

    OP_43(0x21, 0x1, 0x0, 0x1A)
    Sleep(200)
    OP_43(0x1D, 0x1, 0x0, 0x19)
    Sleep(600)
    OP_43(0x20, 0x1, 0x0, 0x1A)
    Sleep(600)
    OP_43(0x1F, 0x1, 0x0, 0x19)
    Sleep(400)
    OP_43(0x1E, 0x1, 0x0, 0x19)
    Sleep(200)
    OP_43(0x22, 0x1, 0x0, 0x1A)
    Return()

    # Function_22_659E end

    def Function_23_65E2(): pass

    label("Function_23_65E2")

    OP_8B(0xFE, 0x1C2, 0x1982, 0x190)
    OP_8E(0xFE, 0x1C2, 0x0, 0x1982, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_23_65E2 end

    def Function_24_6609(): pass

    label("Function_24_6609")

    OP_8B(0xFE, 0xFFFF437C, 0x42CC, 0x190)
    OP_8E(0xFE, 0xFFFF437C, 0x0, 0x42CC, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_24_6609 end

    def Function_25_6630(): pass

    label("Function_25_6630")

    OP_8B(0xFE, 0xFFFFFD80, 0x8980, 0x190)
    OP_8E(0xFE, 0xFFFFFD80, 0x0, 0x8980, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_25_6630 end

    def Function_26_6657(): pass

    label("Function_26_6657")

    OP_8B(0xFE, 0xFFFF81AC, 0xFCC5, 0x190)
    OP_8E(0xFE, 0xFFFF81AC, 0x0, 0xFCC5, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_26_6657 end

    SaveToFile()

Try(main)
