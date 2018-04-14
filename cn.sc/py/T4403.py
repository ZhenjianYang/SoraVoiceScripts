from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4403   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60034",
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
        '军犬',                                 # 9
        '军犬',                                 # 10
        '军犬',                                 # 11
        '凯诺娜',                               # 12
        '杜南公爵',                             # 13
        '雪拉扎德',                             # 14
        '阿加特',                               # 15
        '奥利维尔',                             # 16
        '科洛丝',                               # 17
        '提妲',                                 # 18
        '金',                                   # 19
        '亚妮拉丝',                             # 20
        '歼灭天使玲',                           # 21
        '希德中校',                             # 22
        '管家菲利普',                           # 23
        '奈尔',                                 # 24
        '玲的爸爸',                             # 25
        '玲的妈妈',                             # 26
        '亲卫队队员',                           # 27
        '亲卫队队员',                           # 28
        '亲卫队队员',                           # 29
        '亲卫队队员',                           # 30
        '亲卫队队员',                           # 31
        '亲卫队队员',                           # 32
        '亲卫队队员',                           # 33
        '亲卫队队员',                           # 34
        '士兵',                                 # 35
        '士兵',                                 # 36
        '士兵',                                 # 37
        '士兵',                                 # 38
        '士兵',                                 # 39
        '士兵',                                 # 40
        '士兵',                                 # 41
        '士兵',                                 # 42
        '士兵',                                 # 43
        '士兵',                                 # 44
        '特务兵',                               # 45
        '特务兵',                               # 46
        '特务兵',                               # 47
        '导力战车『奥尔杰尤』',                 # 48
        '榴弹炮',                               # 49
        '榴弹炮',                               # 50
        '榴弹炮',                               # 51
        '帕蒂尔·玛蒂尔',                       # 52
        '王都格兰赛尔·西街区',                 # 53
        '王都格兰赛尔·码头北',                 # 54
        '侵蚀狼犬',                             # 55
        '侵蚀狼犬',                             # 56
        '侵蚀狼犬',                             # 57
        '侵蚀狼犬',                             # 58
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
        'ED6_DT27/CH04512 ._CH',             # 00
        'ED6_DT27/CH03120 ._CH',             # 01
        'ED6_DT07/CH02140 ._CH',             # 02
        'ED6_DT07/CH00020 ._CH',             # 03
        'ED6_DT07/CH00050 ._CH',             # 04
        'ED6_DT07/CH00030 ._CH',             # 05
        'ED6_DT07/CH00040 ._CH',             # 06
        'ED6_DT07/CH00060 ._CH',             # 07
        'ED6_DT07/CH00070 ._CH',             # 08
        'ED6_DT27/CH03090 ._CH',             # 09
        'ED6_DT26/CH20287 ._CH',             # 0A
        'ED6_DT27/CH03590 ._CH',             # 0B
        'ED6_DT07/CH02470 ._CH',             # 0C
        'ED6_DT07/CH02060 ._CH',             # 0D
        'ED6_DT26/CH20303 ._CH',             # 0E
        'ED6_DT26/CH20308 ._CH',             # 0F
        'ED6_DT07/CH01320 ._CH',             # 10
        'ED6_DT07/CH01650 ._CH',             # 11
        'ED6_DT07/CH00341 ._CH',             # 12
        'ED6_DT27/CH04586 ._CH',             # 13
        'ED6_DT27/CH04584 ._CH',             # 14
        'ED6_DT26/CH20309 ._CH',             # 15
        'ED6_DT27/CH04580 ._CH',             # 16
        'ED6_DT27/CH04120 ._CH',             # 17
        'ED6_DT07/CH00440 ._CH',             # 18
        'ED6_DT07/CH00341 ._CH',             # 19
        'ED6_DT07/CH00441 ._CH',             # 1A
        'ED6_DT27/CH04124 ._CH',             # 1B
        'ED6_DT06/CH20042 ._CH',             # 1C
        'ED6_DT26/CH20447 ._CH',             # 1D
        'ED6_DT09/CH10060 ._CH',             # 1E
        'ED6_DT09/CH10061 ._CH',             # 1F
        'ED6_DT27/CH04000 ._CH',             # 20
        'ED6_DT07/CH00150 ._CH',             # 21
        'ED6_DT07/CH00120 ._CH',             # 22
        'ED6_DT27/CH04080 ._CH',             # 23
        'ED6_DT26/CH20293 ._CH',             # 24
        'ED6_DT26/CH20294 ._CH',             # 25
        'ED6_DT26/CH20302 ._CH',             # 26
        'ED6_DT27/CH04001 ._CH',             # 27
        'ED6_DT07/CH00151 ._CH',             # 28
        'ED6_DT07/CH00121 ._CH',             # 29
        'ED6_DT27/CH04081 ._CH',             # 2A
        'ED6_DT27/CH04581 ._CH',             # 2B
        'ED6_DT27/CH04121 ._CH',             # 2C
        'ED6_DT26/CH20286 ._CH',             # 2D
        'ED6_DT27/CH04511 ._CH',             # 2E
        'ED6_DT27/CH04516 ._CH',             # 2F
        'ED6_DT07/CH00340 ._CH',             # 30
    )

    AddCharChipPat(
        'ED6_DT27/CH04512P._CP',             # 00
        'ED6_DT27/CH03120P._CP',             # 01
        'ED6_DT07/CH02140P._CP',             # 02
        'ED6_DT07/CH00020P._CP',             # 03
        'ED6_DT07/CH00050P._CP',             # 04
        'ED6_DT07/CH00030P._CP',             # 05
        'ED6_DT07/CH00040P._CP',             # 06
        'ED6_DT07/CH00060P._CP',             # 07
        'ED6_DT07/CH00070P._CP',             # 08
        'ED6_DT27/CH03090P._CP',             # 09
        'ED6_DT26/CH20287P._CP',             # 0A
        'ED6_DT27/CH03590P._CP',             # 0B
        'ED6_DT07/CH02470P._CP',             # 0C
        'ED6_DT07/CH02060P._CP',             # 0D
        'ED6_DT26/CH20303P._CP',             # 0E
        'ED6_DT26/CH20308P._CP',             # 0F
        'ED6_DT07/CH01320P._CP',             # 10
        'ED6_DT07/CH01650P._CP',             # 11
        'ED6_DT07/CH00341P._CP',             # 12
        'ED6_DT27/CH04586P._CP',             # 13
        'ED6_DT27/CH04584P._CP',             # 14
        'ED6_DT26/CH20309P._CP',             # 15
        'ED6_DT27/CH04580P._CP',             # 16
        'ED6_DT27/CH04120P._CP',             # 17
        'ED6_DT07/CH00440P._CP',             # 18
        'ED6_DT07/CH00341P._CP',             # 19
        'ED6_DT07/CH00441P._CP',             # 1A
        'ED6_DT27/CH04124P._CP',             # 1B
        'ED6_DT06/CH20042P._CP',             # 1C
        'ED6_DT26/CH20447P._CP',             # 1D
        'ED6_DT09/CH10060P._CP',             # 1E
        'ED6_DT09/CH10061P._CP',             # 1F
        'ED6_DT27/CH04000P._CP',             # 20
        'ED6_DT07/CH00150P._CP',             # 21
        'ED6_DT07/CH00120P._CP',             # 22
        'ED6_DT27/CH04080P._CP',             # 23
        'ED6_DT26/CH20293P._CP',             # 24
        'ED6_DT26/CH20294P._CP',             # 25
        'ED6_DT26/CH20302P._CP',             # 26
        'ED6_DT27/CH04001P._CP',             # 27
        'ED6_DT07/CH00151P._CP',             # 28
        'ED6_DT07/CH00121P._CP',             # 29
        'ED6_DT27/CH04081P._CP',             # 2A
        'ED6_DT27/CH04581P._CP',             # 2B
        'ED6_DT27/CH04121P._CP',             # 2C
        'ED6_DT26/CH20286P._CP',             # 2D
        'ED6_DT27/CH04511P._CP',             # 2E
        'ED6_DT27/CH04516P._CP',             # 2F
        'ED6_DT07/CH00340P._CP',             # 30
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
        Unknown3            = 45,
        ChipIndex           = 0x2D,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
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
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
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
        NpcIndex            = 0x189,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x189,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 60310,
        Z                   = 0,
        Y                   = -1230,
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
        X                   = -9950,
        Z                   = 0,
        Y                   = 71270,
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
        X                   = 9400,
        Z                   = 0,
        Y                   = -1180,
        Unknown_0C          = 180,
        Unknown_0E          = 30,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3DE,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -15030,
        Z                   = 0,
        Y                   = -9320,
        Unknown_0C          = 180,
        Unknown_0E          = 30,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3DE,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -11830,
        Z                   = 0,
        Y                   = 6760,
        Unknown_0C          = 180,
        Unknown_0E          = 30,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3DE,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -24660,
        Z                   = 0,
        Y                   = -820,
        Unknown_0C          = 180,
        Unknown_0E          = 30,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3DE,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 27000,
        Y                   = -2000,
        Z                   = -11000,
        Range               = 29500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x251C,
        Unknown_18          = 0x0,
        Unknown_1C          = 3,
    )

    DeclEvent(
        X                   = -18200,
        Y                   = -2000,
        Z                   = 32700,
        Range               = -6000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x878C,
        Unknown_18          = 0x0,
        Unknown_1C          = 15,
    )


    ScpFunction(
        "Function_0_8A2",          # 00, 0
        "Function_1_8DF",          # 01, 1
        "Function_2_934",          # 02, 2
        "Function_3_94A",          # 03, 3
        "Function_4_95B",          # 04, 4
        "Function_5_C7E",          # 05, 5
        "Function_6_E1E",          # 06, 6
        "Function_7_E47",          # 07, 7
        "Function_8_E70",          # 08, 8
        "Function_9_E99",          # 09, 9
        "Function_10_ECF",         # 0A, 10
        "Function_11_F05",         # 0B, 11
        "Function_12_F3B",         # 0C, 12
        "Function_13_F73",         # 0D, 13
        "Function_14_FAB",         # 0E, 14
        "Function_15_FD7",         # 0F, 15
        "Function_16_11D8",        # 10, 16
        "Function_17_11E5",        # 11, 17
        "Function_18_38D9",        # 12, 18
        "Function_19_3A25",        # 13, 19
        "Function_20_3A64",        # 14, 20
        "Function_21_3AA4",        # 15, 21
        "Function_22_3B75",        # 16, 22
        "Function_23_433D",        # 17, 23
        "Function_24_74BF",        # 18, 24
        "Function_25_74F5",        # 19, 25
        "Function_26_754A",        # 1A, 26
        "Function_27_75A9",        # 1B, 27
        "Function_28_75FE",        # 1C, 28
        "Function_29_761A",        # 1D, 29
        "Function_30_7636",        # 1E, 30
        "Function_31_766D",        # 1F, 31
        "Function_32_76A4",        # 20, 32
        "Function_33_76E7",        # 21, 33
        "Function_34_772A",        # 22, 34
        "Function_35_774D",        # 23, 35
        "Function_36_7763",        # 24, 36
        "Function_37_7783",        # 25, 37
        "Function_38_77A7",        # 26, 38
        "Function_39_7847",        # 27, 39
        "Function_40_786D",        # 28, 40
        "Function_41_7893",        # 29, 41
        "Function_42_78BE",        # 2A, 42
        "Function_43_78E9",        # 2B, 43
        "Function_44_7914",        # 2C, 44
        "Function_45_793F",        # 2D, 45
        "Function_46_796A",        # 2E, 46
        "Function_47_798B",        # 2F, 47
        "Function_48_79B6",        # 30, 48
        "Function_49_79E1",        # 31, 49
        "Function_50_7A0C",        # 32, 50
        "Function_51_7A37",        # 33, 51
        "Function_52_7A62",        # 34, 52
        "Function_53_7A8D",        # 35, 53
        "Function_54_7AB8",        # 36, 54
        "Function_55_7AE3",        # 37, 55
        "Function_56_7B0E",        # 38, 56
        "Function_57_7B39",        # 39, 57
        "Function_58_7B64",        # 3A, 58
        "Function_59_7E6A",        # 3B, 59
        "Function_60_7F03",        # 3C, 60
    )


    def Function_0_8A2(): pass

    label("Function_0_8A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8C2")
    SetChrFlags(0x36, 0x80)
    SetChrFlags(0x37, 0x80)
    SetChrFlags(0x38, 0x80)
    SetChrFlags(0x39, 0x80)

    label("loc_8C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_8DE")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x71), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 16)

    label("loc_8DE")

    Return()

    # Function_0_8A2 end

    def Function_1_8DF(): pass

    label("Function_1_8DF")

    OP_16(0x2, 0xFA0, 0xFFFE3AE0, 0xFFFE69C0, 0x23006D)
    OP_22(0x1C5, 0x0, 0x64)
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_71(0x5, 0x4)
    OP_71(0x6, 0x4)
    OP_71(0x7, 0x4)
    OP_1C(0x2, 0x0, 0x3C)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x44E), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_933")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_933")

    Return()

    # Function_1_8DF end

    def Function_2_934(): pass

    label("Function_2_934")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_949")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_934")

    label("loc_949")

    Return()

    # Function_2_934 end

    def Function_3_94A(): pass

    label("Function_3_94A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 3)), scpexpr(EXPR_END)), "loc_952")
    Return()

    label("loc_952")

    Call(0, 4)
    Call(0, 5)
    Return()

    # Function_3_94A end

    def Function_4_95B(): pass

    label("Function_4_95B")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_977")
    Call(0, 59)
    FadeToBright(0, 0)

    label("loc_977")

    Fade(1000)
    SetChrPos(0x101, 28170, 0, -970, 270)
    SetChrPos(0xF7, 28170, 0, 530, 270)
    SetChrPos(0x109, 29480, 0, -250, 270)
    OP_6D(28120, 0, -40, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(1850, 0)
    OP_6C(315000, 0)
    OP_6E(357, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A11")

    ChrTalk(    #0
        0x106,
        "#052F唔……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_A24")

    label("loc_A11")


    ChrTalk(    #1
        0x103,
        "#023F哈……！\x02",
    )

    CloseMessageWindow()

    label("loc_A24")

    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x8, 8490, 0, -970, 90)
    SetChrPos(0x9, 8380, 0, 530, 90)
    SetChrPos(0xA, 6950, 0, -250, 90)
    OP_43(0x8, 0x0, 0x0, 0x2)
    OP_43(0x9, 0x0, 0x0, 0x2)
    OP_43(0xA, 0x0, 0x0, 0x2)
    OP_20(0x7D0)
    OP_6D(20000, 0, -550, 2000)
    OP_43(0x8, 0x1, 0x0, 0x6)
    Sleep(100)
    OP_43(0x9, 0x1, 0x0, 0x7)
    Sleep(100)
    OP_43(0xA, 0x1, 0x0, 0x8)

    def lambda_AB6():
        OP_6D(25120, 0, 240, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AB6)

    def lambda_ACE():
        OP_67(0, 9180, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_ACE)

    def lambda_AE6():
        OP_6B(1990, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_AE6)

    def lambda_AF6():
        OP_6E(385, 1500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_AF6)
    OP_1D(0x35)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x8, 0x1)
    WaitChrThread(0x9, 0x1)
    WaitChrThread(0xA, 0x1)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 32)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x109, 35)
    SetChrSubChip(0x109, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B4F")
    SetChrChipByIndex(0x106, 33)
    SetChrSubChip(0x106, 0)
    Jump("loc_B59")

    label("loc_B4F")

    SetChrChipByIndex(0x103, 34)
    SetChrSubChip(0x103, 0)

    label("loc_B59")

    OP_0D()
    Sleep(500)
    OP_62(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #2
        0x109,
        (
            "#1061F#4P好、好凶的\x01",
            "狗狗啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x101,
        "#1005F#5P特务兵的军用犬……！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BEB")

    ChrTalk(    #4
        0x106,
        "#054F#2P……来了！\x02",
    )

    CloseMessageWindow()
    Jump("loc_C03")

    label("loc_BEB")


    ChrTalk(    #5
        0x103,
        "#024F#2P……来了！\x02",
    )

    CloseMessageWindow()

    label("loc_C03")

    OP_43(0x8, 0x1, 0x0, 0x9)
    Sleep(50)
    OP_43(0x9, 0x1, 0x0, 0xA)
    Sleep(50)
    OP_43(0xA, 0x1, 0x0, 0xB)

    def lambda_C28():
        OP_6D(26990, 0, 1000, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C28)

    def lambda_C40():
        OP_6B(1600, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C40)
    WaitChrThread(0x8, 0x1)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0x101, 0xFF)
    Battle(0x45B, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_C78"),
        (SWITCH_DEFAULT, "loc_C7D"),
    )


    label("loc_C78")

    OP_B4(0x0)
    Jump("loc_C7D")

    label("loc_C7D")

    Return()

    # Function_4_95B end

    def Function_5_C7E(): pass

    label("Function_5_C7E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Sleep(1000)
    OP_6D(28240, 0, -280, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 28170, 0, -970, 270)
    SetChrPos(0xF7, 28170, 0, 530, 270)
    SetChrPos(0x109, 29480, 0, -250, 270)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0xF7, 65535)
    SetChrChipByIndex(0x109, 65535)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    FadeToBright(2000, 0)
    OP_43(0x101, 0x1, 0x0, 0xC)
    Sleep(100)
    OP_43(0xF7, 0x1, 0x0, 0xD)
    Sleep(100)
    OP_43(0x109, 0x1, 0x0, 0xE)
    WaitChrThread(0x109, 0x1)
    OP_0D()

    ChrTalk(    #6
        0x109,
        (
            "#1068F呼～吓一大跳。\x02\x03",

            "#1060F不过『茶会』的会场\x01",
            "看来是这儿没错了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x101,
        "#1002F#1P嗯……是啊！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DDE")

    ChrTalk(    #8
        0x106,
        "#050F#5P好，慎重前进吧！\x02",
    )

    CloseMessageWindow()
    Jump("loc_DFE")

    label("loc_DDE")


    ChrTalk(    #9
        0x103,
        "#022F#5P好，要慎重前进哦！\x02",
    )

    CloseMessageWindow()

    label("loc_DFE")

    OP_A2(0x163B)
    OP_28(0x8E, 0x1, 0x2)
    ClearChrFlags(0x36, 0x80)
    ClearChrFlags(0x37, 0x80)
    ClearChrFlags(0x38, 0x80)
    ClearChrFlags(0x39, 0x80)
    EventEnd(0x0)
    Return()

    # Function_5_C7E end

    def Function_6_E1E(): pass

    label("Function_6_E1E")

    SetChrChipByIndex(0xFE, 31)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xFE, 0x5604, 0x0, 0xFFFFFC72, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 30)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_6_E1E end

    def Function_7_E47(): pass

    label("Function_7_E47")

    SetChrChipByIndex(0xFE, 31)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xFE, 0x565E, 0x0, 0x398, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 30)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_7_E47 end

    def Function_8_E70(): pass

    label("Function_8_E70")

    SetChrChipByIndex(0xFE, 31)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xFE, 0x50B4, 0x0, 0x1D6, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 30)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_8_E70 end

    def Function_9_E99(): pass

    label("Function_9_E99")

    SetChrChipByIndex(0xFE, 31)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xFE, 0x5D5C, 0x0, 0xFFFFFBFA, 0x1770, 0x0)
    OP_96(0xFE, 0x6B1C, 0x0, 0xFFFFFC22, 0x5DC, 0x1F40)
    Return()

    # Function_9_E99 end

    def Function_10_ECF(): pass

    label("Function_10_ECF")

    SetChrChipByIndex(0xFE, 31)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xFE, 0x5D52, 0x0, 0x23A, 0x1770, 0x0)
    OP_96(0xFE, 0x6A72, 0x0, 0x1B8, 0x5DC, 0x1F40)
    Return()

    # Function_10_ECF end

    def Function_11_F05(): pass

    label("Function_11_F05")

    SetChrChipByIndex(0xFE, 31)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xFE, 0x5870, 0x0, 0x0, 0x1770, 0x0)
    OP_96(0xFE, 0x6568, 0x0, 0xFFFFFFCE, 0x5DC, 0x1F40)
    Return()

    # Function_11_F05 end

    def Function_12_F3B(): pass

    label("Function_12_F3B")

    OP_8C(0xFE, 315, 400)
    Sleep(1000)
    OP_8C(0xFE, 225, 400)
    Sleep(1000)
    OP_8C(0xFE, 315, 400)
    Sleep(1000)
    OP_8C(0xFE, 225, 400)
    Sleep(1000)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_12_F3B end

    def Function_13_F73(): pass

    label("Function_13_F73")

    OP_8C(0xFE, 360, 400)
    Sleep(1000)
    OP_8C(0xFE, 270, 400)
    Sleep(1000)
    OP_8C(0xFE, 360, 400)
    Sleep(1000)
    OP_8C(0xFE, 270, 400)
    Sleep(1000)
    OP_8C(0xFE, 135, 400)
    Return()

    # Function_13_F73 end

    def Function_14_FAB(): pass

    label("Function_14_FAB")

    OP_8C(0xFE, 270, 400)
    Sleep(1000)
    OP_8C(0xFE, 90, 400)
    Sleep(1000)
    OP_8C(0xFE, 180, 400)
    Sleep(1000)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_14_FAB end

    def Function_15_FD7(): pass

    label("Function_15_FD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11D7")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10DF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_106C")

    ChrTalk(    #10
        0x106,
        "#052F等等，艾丝蒂尔。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x106, 270, 400)

    ChrTalk(    #11
        0x106,
        (
            "#552F这栋建筑\x01",
            "有人的气息。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)

    ChrTalk(    #12
        0x101,
        (
            "#1002F真的……\x01",
            "总之调查看看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10DC")

    label("loc_106C")


    ChrTalk(    #13
        0x103,
        "#023F等一下，艾丝蒂尔。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x103, 270, 400)

    ChrTalk(    #14
        0x103,
        (
            "#022F这栋建筑\x01",
            "有人的气息。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)

    ChrTalk(    #15
        0x101,
        (
            "#1002F真的……\x01",
            "总之调查看看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10DC")

    Jump("loc_11BC")

    label("loc_10DF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1155")

    ChrTalk(    #16
        0x101,
        "#1004F等一下！\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)

    ChrTalk(    #17
        0x101,
        (
            "#1002F这栋建筑\x01",
            "有人的气息。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x106, 270, 400)

    ChrTalk(    #18
        0x106,
        (
            "#552F哼……\x01",
            "总之调查看看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11BC")

    label("loc_1155")


    ChrTalk(    #19
        0x101,
        "#1004F等一下！\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)

    ChrTalk(    #20
        0x101,
        (
            "#1002F这栋建筑\x01",
            "有人的气息。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x103, 270, 400)

    ChrTalk(    #21
        0x103,
        (
            "#022F确实……\x01",
            "总之调查看看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11BC")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_11D7")

    Return()

    # Function_15_FD7 end

    def Function_16_11D8(): pass

    label("Function_16_11D8")

    Call(0, 17)
    Call(0, 22)
    Call(0, 23)
    Return()

    # Function_16_11D8 end

    def Function_17_11E5(): pass

    label("Function_17_11E5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1202")
    Call(0, 59)

    label("loc_1202")

    AddParty(0xE, 0xF9, 0xFF)
    LoadEffect(0x0, "monster\\ms30600d.eff")
    LoadEffect(0x1, "monster\\ms30600b.eff")
    LoadEffect(0x2, "monster\\ms30600a.eff")
    LoadEffect(0x3, "battle\\\\btbomb00.eff")
    PlayEffect(0x0, 0x1, 0x2F, 2000, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x2, 0x2F, -2000, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x3, 0x2F, -950, 2750, -1800, 0, -30, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x4, 0x2F, -950, 2800, -2370, 0, -30, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x5, 0x2F, 500, 1500, -2000, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x6, 0x2F, -500, 1500, -2000, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    ClearChrFlags(0x2F, 0x80)
    OP_72(0x5, 0x4)
    OP_A1(0x2F, 0x5)
    SetChrPos(0x2F, -11220, 0, 51980, 180)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xB, 0x40)
    SetChrFlags(0xB, 0x20)
    ClearChrFlags(0xB, 0x1)
    SetChrFlags(0xB, 0x80)
    SetChrPos(0xB, -12500, 2000, 51890, 180)
    OP_72(0x0, 0x10)
    OP_72(0x1, 0x10)
    OP_72(0x0, 0x4)
    OP_72(0x1, 0x4)
    OP_72(0x3, 0x4)
    OP_72(0x4, 0x4)
    OP_6F(0x0, 0)
    OP_6F(0x1, 0)
    OP_6F(0x3, 0)
    OP_6F(0x4, 0)
    OP_A1(0x30, 0x0)
    OP_A1(0x31, 0x1)
    OP_A1(0x32, 0x3)
    SetChrPos(0x30, 1540, 0, 3700, 90)
    SetChrPos(0x31, 1190, 0, -2000, 90)
    SetChrPos(0x32, -1450, 0, 8080, 45)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1A, 0x4)
    SetChrFlags(0x1B, 0x4)
    SetChrBattleFlags(0x1A, 0x20)
    SetChrBattleFlags(0x1B, 0x20)
    OP_89(0x1A, 1540, 750, 3700, 270)
    OP_89(0x1B, 1190, 750, -2000, 270)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    SetChrPos(0x10F, 4290, 0, 380, 270)
    SetChrPos(0x1C, 5510, 0, -1750, 270)
    SetChrPos(0x1D, 5700, 0, 520, 270)
    SetChrPos(0x1E, 5710, 0, -3450, 270)
    SetChrPos(0x1F, 5630, 0, 1960, 270)
    SetChrPos(0x20, 7090, 0, -1780, 270)
    SetChrPos(0x21, 7090, 0, -120, 270)

    def lambda_1541():

        label("loc_1541")

        OP_7C(0x32, 0x32, 0xBB8, 0x64)
        OP_48()
        Jump("loc_1541")

    QueueWorkItem2(0x2F, 3, lambda_1541)
    OP_22(0x10F, 0x0, 0x64)
    OP_22(0x110, 0x0, 0x64)
    SetChrFlags(0x36, 0x80)
    SetChrFlags(0x37, 0x80)
    SetChrFlags(0x38, 0x80)
    SetChrFlags(0x39, 0x80)
    OP_6D(-11130, 0, 7550, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(332000, 0)
    OP_6E(262, 0)

    def lambda_15B7():

        label("loc_15B7")

        OP_69(0x2F, 0x0)
        OP_48()
        Jump("loc_15B7")

    QueueWorkItem2(0x2F, 2, lambda_15B7)
    FadeToBright(2000, 0)

    def lambda_15D1():
        OP_8F(0xFE, 0xFFFFD42C, 0x0, 0xC94, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2F, 1, lambda_15D1)

    def lambda_15EC():
        OP_8F(0xFE, 0xFFFFCF2C, 0x7D0, 0x9D1C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_15EC)
    Sleep(1000)
    OP_22(0x6A, 0x0, 0x64)
    OP_B0(0x5, 0xF)
    OP_6F(0x5, 371)
    OP_70(0x5, 0x186)
    OP_73(0x5)
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xB, 0x80)

    def lambda_1636():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1636)

    def lambda_1648():
        OP_8F(0xFE, 0xFFFFCF2C, 0x8FC, 0xC94, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1648)
    Sleep(2000)

    def lambda_1668():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1668)
    WaitChrThread(0xB, 0x2)

    ChrTalk(    #22 op#A op#5
        0xB,
        (
            "#1181F#6P#30A呼呼……\x01",
            "似乎完全分开了。\x02\x03",

            "#1181F#6P#38A就这样将统治城的\x01",
            "女王陛下抓走的话……\x05\x02",
        )
    )

    Sleep(7700)
    PlayEffect(0x3, 0xFF, 0xFF, -11910, 0, -720, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x3E4CCCCD, 0xC8, 0x7D0, 0x64)
    Sleep(300)
    PlayEffect(0x3, 0xFF, 0xFF, -9980, 0, -1310, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x3E4CCCCD, 0xC8, 0x7D0, 0x64)
    Sleep(500)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    WaitChrThread(0x2F, 0x1)
    OP_23(0x110)
    OP_44(0x2F, 0x3)
    OP_44(0xB, 0x1)
    OP_82(0x1, 0x2)
    OP_82(0x2, 0x2)
    OP_20(0x0)
    Sleep(1000)

    def lambda_17AD():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_17AD)
    WaitChrThread(0xB, 0x2)

    ChrTalk(    #23
        0xB,
        "#1185F#6P什……！？\x02",
    )

    CloseMessageWindow()
    OP_6F(0x3, 0)
    OP_70(0x3, 0xA)
    OP_73(0x3)
    OP_6F(0x4, 0)
    OP_70(0x4, 0xA)
    OP_73(0x4)

    NpcTalk(    #24
        0x10F,
        "女性的声音",
        (
            "嗯……\x01",
            "看来赶上了。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x2F, 0x2)
    OP_1D(0x74)
    Sleep(500)

    def lambda_182A():
        OP_6D(-6040, 0, 4270, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_182A)

    def lambda_1842():
        OP_67(0, 4190, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1842)

    def lambda_185A():
        OP_6B(9600, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_185A)

    def lambda_186A():
        OP_6C(315000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_186A)

    def lambda_187A():
        OP_6E(156, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_187A)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)
    WaitChrThread(0x109, 0x1)
    WaitChrThread(0x109, 0x2)
    Sleep(500)

    ChrTalk(    #25
        0xB,
        (
            "#1185F王、王室亲卫队……！\x02\x03",

            "而且……\x01",
            "还有尤莉亚·舒华兹！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x10F,
        (
            "#176F#2P好久不见了，凯诺娜。\x02\x03",

            "#178F没想到会和你\x01",
            "在这种地方相见。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xB,
        (
            "#1185F你们……\x01",
            "你怎么在这里！？\x02\x03",

            "不是在雷斯顿要塞\x01",
            "进行飞行训练吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x10F,
        (
            "#170F#2P希德中校\x01",
            "有紧急的支援请求。\x02\x03",

            "好像格兰赛尔市街\x01",
            "发生了意外的事。\x02\x03",

            "所以我们就飞过来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xB,
        (
            "#1187F哼……\x01",
            "还以为就是个废物……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x10F,
        (
            "#170F#2P中校和理查德上校一样\x01",
            "原本是卡西乌斯准将的部下嘛。\x02\x03",

            "轻视他是你的错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xB,
        (
            "#1183F看来是了……\x02\x03",

            "#1180F对了，你们。\x01",
            "打算做什么？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x10F,
        "#173F#2P什么……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xB,
        (
            "#1181F埃尔赛尤搭载的\x01",
            "移动式的导力榴弹炮……\x02\x03",

            "想用那种东西\x01",
            "对抗这个\x01",
            "奥尔杰尤？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x10F,
        (
            "#178F#2P就算不能对抗\x01",
            "至少能拖拖后腿。\x02\x03",

            "很快希德中校的部队\x01",
            "应该也能到达这里了。\x02\x03",

            "投降对你自己比较好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xB,
        "#1181F哈哈哈……\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #36
        0xB,
        "#1188F#3S啊──哈哈哈！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #37
        0x10F,
        "#178F#2P……有什么好笑。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xB,
        (
            "#1320F你一点也没变呢，尤莉亚……\x02\x03",

            "直率凛然的性情\x01",
            "和士官学校时一样……\x02\x03",

            "以前每次碰头\x01",
            "就会相互挖苦……\x02\x03",

            "不过对你这种性格\x01",
            "我可是一点也不讨厌。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x10F,
        (
            "#175F#2P凯诺娜……\x01",
            "我也是一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xB,
        (
            "#1183F不过呢……\x02\x03",

            "#1182F要是阻挠解放理查德阁下的\x01",
            "计划，我可绝不宽恕！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x10F,
        "#173F#2P！！\x02",
    )

    CloseMessageWindow()
    OP_22(0xE6, 0x0, 0x64)
    OP_8F(0xB, 0xFFFFCF2C, 0x7D0, 0xC94, 0xFA0, 0x0)
    OP_B0(0x5, 0xF)
    OP_6F(0x5, 391)
    OP_70(0x5, 0x19A)
    OP_73(0x5)
    SetChrFlags(0xB, 0x80)
    OP_B0(0x5, 0x5)
    OP_6F(0x5, 251)
    OP_70(0x5, 0x104)
    OP_22(0x111, 0x0, 0x64)

    ChrTalk(    #42
        0x10F,
        (
            "#176F#2P没办法了……\x02\x03",

            "#172F１号、２号同时发射准备！\x01",
            "阻止坦克前进！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    SetMessageWindowPos(-1, 160, -1, -1)
    SetChrName("队员们")

    AnonymousTalk(    #43
        "\x07\x00#3S是·长官！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    LoadEffect(0x3, "map\\\\mp063_00.eff")
    LoadEffect(0x4, "map\\\\mp015_00.eff")
    LoadEffect(0x5, "map\\\\mp007_00.eff")
    LoadEffect(0x7, "map\\\\mp007_01.eff")
    PlayEffect(0x3, 0x2, 0xFF, -2070, 1500, 3480, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x355, 0x0, 0x64)
    Sleep(200)
    PlayEffect(0x3, 0x7, 0xFF, -2420, 1500, -2230, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x355, 0x0, 0x64)
    OP_B0(0x5, 0x5)
    OP_6F(0x5, 261)
    OP_70(0x5, 0x108)
    OP_73(0x5)
    OP_B0(0x5, 0xA)
    OP_6F(0x5, 264)
    OP_70(0x5, 0x10C)
    OP_73(0x5)
    OP_B0(0x5, 0xF)
    OP_6F(0x5, 268)
    OP_70(0x5, 0x10E)
    OP_73(0x5)
    OP_71(0x5, 0x20)
    OP_6F(0x5, 411)
    OP_70(0x5, 0x1AE)
    Sleep(1000)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10F, 19)
    SetChrSubChip(0x10F, 0)
    Sleep(500)
    OP_99(0x10F, 0x0, 0x1, 0x5DC)

    ChrTalk(    #44
        0x10F,
        "#177F#2P#3S发射──\x02",
    )

    CloseMessageWindow()
    OP_20(0x0)
    Play3DEffect(0x5, 0x0, 0x5, "Frame68__gospel__1_", 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_22(0x90, 0x0, 0x64)
    Play3DEffect(0x7, 0x1, 0x5, "Frame68__gospel__1_", 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Sleep(500)
    OP_22(0x91, 0x0, 0x64)

    def lambda_1F8E():
        OP_67(0, 6190, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1F8E)

    def lambda_1FA6():
        OP_6B(12600, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1FA6)
    PlayEffect(0x4, 0xFF, 0xFF, -11100, 2650, 2870, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    OP_82(0x1, 0x2)
    OP_23(0x10F)
    OP_1D(0x5C)
    OP_82(0x3, 0x2)
    OP_82(0x4, 0x2)
    OP_82(0x5, 0x2)
    OP_82(0x6, 0x2)
    OP_82(0x2, 0x2)
    OP_82(0x7, 0x2)
    OP_7B()
    Sleep(150)
    OP_79(0x2, 0x2)
    OP_7B()
    Sleep(150)
    OP_79(0x3, 0x2)
    OP_7B()
    Sleep(100)
    OP_6F(0x3, 0)
    OP_7B()
    Sleep(150)
    OP_6F(0x4, 0)
    OP_7B()
    Sleep(150)
    OP_79(0x4, 0x2)
    OP_7B()
    Sleep(100)
    OP_79(0x5, 0x2)
    OP_7B()
    Sleep(250)
    OP_6F(0x0, 1)
    OP_7B()
    Sleep(150)
    OP_6F(0x1, 1)
    OP_7B()
    Sleep(200)
    OP_79(0xC, 0x2)
    OP_7B()
    Sleep(100)
    OP_79(0xD, 0x2)
    OP_7B()
    Sleep(150)
    OP_79(0x1, 0x2)
    OP_79(0x0, 0x2)
    OP_79(0x6, 0x2)
    OP_79(0x7, 0x2)
    OP_79(0x8, 0x2)
    OP_79(0x9, 0x2)
    OP_79(0xA, 0x2)
    OP_79(0xB, 0x2)
    OP_7B()
    Sleep(500)
    SetChrChipByIndex(0x10F, 22)
    SetChrSubChip(0x10F, 0)
    Sleep(500)

    ChrTalk(    #45
        0x10F,
        "#173F#2P什…什么…！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x1A,
        (
            "#2P不、不行！\x01",
            "机能停止了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x10F,
        (
            "#177F#2P……导力停止现象吗！？\x02\x03",

            "但是，那样做\x01",
            "重要的坦克也……\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x10F, 0x0, 0x64)
    PlayEffect(0x1, 0x3, 0x2F, -950, 2750, -1800, 0, -30, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    PlayEffect(0x1, 0x4, 0x2F, -950, 2800, -2370, 0, -30, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x2, 0x5, 0x2F, 500, 1500, -2000, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x2, 0x6, 0x2F, -500, 1500, -2000, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_223D():

        label("loc_223D")

        OP_7C(0x32, 0x32, 0xBB8, 0x64)
        OP_48()
        Jump("loc_223D")

    QueueWorkItem2(0x2F, 3, lambda_223D)
    PlayEffect(0x0, 0x1, 0x2F, 2000, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x2, 0x2F, -2000, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_B0(0x5, 0xF)
    Sleep(300)
    OP_22(0x110, 0x0, 0x64)
    OP_8C(0x2F, 90, 50)
    OP_23(0x110)
    OP_44(0x2F, 0x3)
    OP_82(0x1, 0x2)
    OP_82(0x2, 0x2)

    ChrTalk(    #48
        0x10F,
        (
            "#173F#2P不、不可能！\x01",
            "为什么能动！？\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    LoadEffect(0x3, "scraft\\sc003_12.eff")
    LoadEffect(0x4, "battle\\\\btbomb00.eff")
    OP_0D()

    def lambda_2340():
        OP_67(0, 4190, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2340)

    def lambda_2358():
        OP_6B(9600, 7000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2358)
    OP_43(0x2F, 0x1, 0x0, 0x12)
    Sleep(500)
    LoadEffect(0x3, "monster\\ms30602a.eff")
    LoadEffect(0x4, "monster\\ms30602b.eff")
    OP_72(0x5, 0x20)
    OP_B0(0x5, 0xA)
    OP_6F(0x5, 121)
    OP_70(0x5, 0x91)
    OP_22(0x76, 0x0, 0x64)
    OP_73(0x5)
    OP_22(0x3E0, 0x0, 0x64)
    OP_73(0x1)
    Sleep(200)
    Sleep(300)
    Sleep(500)
    PlayEffect(0x3, 0xFF, 0x2F, 0, 2200, 3500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_240D():
        OP_8F(0xFE, 0xFFFFD044, 0x0, 0xC94, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2F, 1, lambda_240D)
    OP_6F(0x5, 161)
    OP_70(0x5, 0xBE)
    OP_22(0x3E1, 0x0, 0x64)
    OP_22(0x1FE, 0x0, 0x64)
    OP_7C(0xBB8, 0xBB8, 0x1388, 0xC8)
    PlayEffect(0x4, 0xFF, 0xFF, 290, 0, 3540, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_6F(0x0, 2)
    OP_70(0x0, 0x3C)
    Sleep(50)

    def lambda_249E():
        OP_96(0x1A, 0x852, 0x0, 0x1900, 0x7D0, 0x7D0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_249E)
    SetChrChipByIndex(0x1A, 21)
    SetChrSubChip(0x1A, 3)
    WaitChrThread(0x1A, 0x1)
    SetChrFlags(0x1A, 0x2)
    SetChrChipByIndex(0x1A, 29)
    SetChrSubChip(0x1A, 0)
    OP_73(0x0)
    Sleep(200)
    OP_73(0x1)
    Sleep(200)

    ChrTalk(    #49
        0x10F,
        "#177F#2P什…什么…\x02",
    )

    CloseMessageWindow()
    LoadEffect(0x3, "monster\\msc0311.eff")
    LoadEffect(0x4, "map\\\\mp003_00.eff")
    OP_B0(0x5, 0xF)
    OP_6F(0x5, 191)
    OP_70(0x5, 0xD2)
    OP_22(0x76, 0x0, 0x64)
    OP_73(0x5)
    OP_6F(0x5, 101)
    OP_70(0x5, 0x78)
    OP_73(0x5)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    PlayEffect(0x3, 0x7, 0x2F, 500, 3000, 2300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x4, 0xFF, 0xFF, 4019, 0, -1270, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x4, 0xFF, 0xFF, 6310, 0, 580, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x4, 0xFF, 0xFF, 6820, 0, 1440, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    ChrTalk(    #50 op#A op#5
        0x1F,
        "#10A#2P呜哦……\x05\x02",
    )

    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x4, 0xFF, 0xFF, 7720, 0, -1790, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x4, 0xFF, 0xFF, 4030, 0, 1650, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x4, 0xFF, 0xFF, 7690, 0, 210, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x4, 0xFF, 0xFF, 5160, 0, -4490, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x4, 0xFF, 0xFF, 6820, 0, -3850, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_82(0x7, 0x0)
    SetChrChipByIndex(0x10F, 20)
    SetChrChipByIndex(0x1C, 21)
    SetChrChipByIndex(0x1D, 21)
    SetChrChipByIndex(0x1E, 21)
    SetChrChipByIndex(0x1F, 21)
    SetChrChipByIndex(0x20, 21)
    SetChrChipByIndex(0x21, 21)
    SetChrSubChip(0x10F, 0)
    SetChrSubChip(0x1C, 0)
    SetChrSubChip(0x1D, 0)
    SetChrSubChip(0x1E, 0)
    SetChrSubChip(0x1F, 0)
    SetChrSubChip(0x20, 0)
    SetChrSubChip(0x21, 0)

    def lambda_2803():
        OP_99(0x1E, 0x0, 0x3, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_2803)
    OP_22(0x20C, 0x0, 0x64)
    Sleep(50)

    def lambda_281D():
        OP_99(0x1F, 0x0, 0x3, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_281D)
    OP_22(0x20C, 0x0, 0x64)
    Sleep(100)

    def lambda_2837():
        OP_99(0x1C, 0x0, 0x3, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_2837)
    OP_22(0x20C, 0x0, 0x64)
    Sleep(50)

    def lambda_2851():
        OP_99(0x20, 0x0, 0x3, 0x3E8)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_2851)
    OP_22(0x20C, 0x0, 0x64)
    Sleep(50)

    def lambda_286B():
        OP_99(0x1D, 0x0, 0x3, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_286B)
    OP_22(0x20C, 0x0, 0x64)
    Sleep(100)

    def lambda_2885():
        OP_99(0x21, 0x0, 0x3, 0x3E8)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_2885)
    OP_22(0x20C, 0x0, 0x64)
    Sleep(200)

    def lambda_289F():
        OP_99(0x10F, 0x0, 0x3, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_289F)
    OP_22(0x20C, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x6A, 0x0, 0x64)
    OP_B0(0x5, 0xF)
    OP_6F(0x5, 271)
    OP_70(0x5, 0x122)
    OP_73(0x5)
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xB, -12290, 2000, 1850, 90)
    ClearChrFlags(0xB, 0x80)

    def lambda_28F4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_28F4)
    OP_8F(0xB, 0xFFFFCFFE, 0x9C4, 0x73A, 0x7D0, 0x0)
    Sleep(1000)

    ChrTalk(    #51
        0xB,
        (
            "#1181F#6P使周围的导力器停止，\x01",
            "同时连接的机体还能动的元件……\x02\x03",

            "哈哈哈……超过预想的力量呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x10F,
        (
            "#175F#2P凯诺娜……\x02\x03",

            "那个『福音』到底是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xB,
        (
            "#1181F#6P呵呵，从某条道得到的秘密武器。\x02\x03",

            "作为帮忙『实验』的交换。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(-11440, 0, 35260, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2770, 0)
    OP_6C(320000, 0)
    OP_6E(262, 0)
    ClearMapFlags(0x10)
    SetChrPos(0x101, -11270, 0, 40480, 180)
    SetChrPos(0xF7, -10400, 0, 41140, 180)
    SetChrPos(0x109, -12300, 0, 41220, 180)

    def lambda_2A75():
        OP_8E(0xFE, 0xFFFFD42C, 0x0, 0x8598, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2A75)
    Sleep(100)

    def lambda_2A95():
        OP_8E(0xFE, 0xFFFFD760, 0x0, 0x8944, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_2A95)
    Sleep(100)

    def lambda_2AB5():
        OP_8E(0xFE, 0xFFFFCFF4, 0x0, 0x8994, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2AB5)
    WaitChrThread(0x109, 0x1)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B03")

    ChrTalk(    #54
        0x106,
        "#055F#2P那、那是什么！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B23")

    label("loc_2B03")


    ChrTalk(    #55
        0x103,
        "#023F#2P那、那是什么啊！？\x02",
    )

    CloseMessageWindow()

    label("loc_2B23")


    ChrTalk(    #56
        0x101,
        (
            "#1020F#6P使用新型福音\x01",
            "『噬身之蛇』的实验……！\x02\x03",

            "竟、竟然以这样的形式来做！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x109,
        (
            "#1067F#5P啊……这下不妙。\x02\x03",

            "那个工作的时候\x01",
            "魔法之类的也不能使用。\x02\x03",

            "#1065F既然如此……\x01",
            "看来只有使用杀手锏了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 400)
    Sleep(100)
    TurnDirection(0xF7, 0x109, 400)

    ChrTalk(    #58
        0x101,
        "#1004F#6P咦……！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D08")

    ChrTalk(    #59
        0x109,
        (
            "#1063F#5P艾丝蒂尔、阿加特。\x02\x03",

            "接下来的行动如果能成功，\x01",
            "说不定可以暂时\x01",
            "令『福音』停止。\x02\x03",

            "我们就趁机拖住坦克吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x106,
        "#052F你说什么！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x101,
        "#1002F#6P这、这能做到吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x109,
        (
            "#1066F#5P几率是一半对一半……\x02\x03",

            "大家一起\x01",
            "向女神祈祷吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DED")

    label("loc_2D08")


    ChrTalk(    #63
        0x109,
        (
            "#1063F#5P艾丝蒂尔、雪拉小姐。\x02\x03",

            "接下来的行动如果能成功，\x01",
            "说不定可以暂时\x01",
            "令『福音』停止。\x02\x03",

            "我们就趁机拖住坦克吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x103,
        "#023F什么！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x101,
        "#1002F#6P这、这能做到吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x109,
        (
            "#1066F#5P几率是一半对一半……\x02\x03",

            "大家一起\x01",
            "向女神祈祷吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DED")

    Sleep(250)
    SetChrFlags(0x109, 0x2)
    SetChrChipByIndex(0x109, 36)
    SetChrSubChip(0x109, 8)
    OP_0D()
    Sleep(500)

    def lambda_2E0D():
        OP_6D(-12300, 0, 35220, 1000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2E0D)

    def lambda_2E25():
        OP_6E(246, 1000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2E25)
    OP_99(0x109, 0x8, 0xB, 0x5DC)
    OP_22(0xD5, 0x0, 0x64)
    SetChrFlags(0x109, 0x2000)
    OP_D7(0x1, 15000, 265)
    OP_99(0x109, 0xB, 0xF, 0x5DC)
    OP_43(0x109, 0x0, 0x0, 0x23)
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #67
        0x101,
        "#1004F啊……那不是！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x109,
        (
            "#1065F『封印宝杖』……\x02\x03",

            "#1063F戴尔蒙市长持有的\x01",
            "禁制之古代遗物！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2EE2():

        label("loc_2EE2")

        TurnDirection(0xFE, 0x109, 400)
        OP_48()
        Jump("loc_2EE2")

    QueueWorkItem2(0x101, 3, lambda_2EE2)

    def lambda_2EF3():

        label("loc_2EF3")

        TurnDirection(0xFE, 0x109, 400)
        OP_48()
        Jump("loc_2EF3")

    QueueWorkItem2(0xF7, 1, lambda_2EF3)

    def lambda_2F04():
        OP_6D(-13800, 0, 3000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2F04)

    def lambda_2F1C():
        OP_67(0, 4000, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2F1C)

    def lambda_2F34():
        OP_6B(2800, 5000)
        ExitThread()

    QueueWorkItem(0xF7, 3, lambda_2F34)

    def lambda_2F44():
        OP_6C(200000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2F44)

    def lambda_2F54():
        OP_6E(402, 5000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2F54)
    OP_44(0x109, 0x0)
    ClearChrFlags(0x109, 0x2)
    SetChrFlags(0x109, 0x1000)
    SetChrChipByIndex(0x109, 37)
    SetChrSubChip(0x109, 0)
    OP_8E(0x109, 0xFFFFD3FA, 0x0, 0x2C7E, 0x1770, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_2F99():
        OP_6D(-14370, 0, -1260, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2F99)

    def lambda_2FB1():
        OP_6B(2500, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2FB1)

    ChrTalk(    #69 op#A op#5
        0x109,
        "#1069F#5P#3S#8A接招！\x05\x02",
    )

    OP_8E(0x109, 0xFFFFD120, 0x0, 0x2328, 0x1770, 0x0)
    SetChrFlags(0x109, 0x2)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x109, 0x40)
    ClearChrFlags(0x109, 0x1000)
    SetChrChipByIndex(0x109, 36)
    SetChrSubChip(0x109, 24)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_3013():
        OP_96(0x109, 0xFFFFCE00, 0xDAC, 0x1770, 0xFA0, 0x1770)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3013)
    OP_56(0x0)
    OP_99(0x109, 0x19, 0x1C, 0x5DC)
    OP_22(0xEE, 0x0, 0x64)
    LoadEffect(0x3, "Scraft\\\\sc008_02.eff")
    OP_20(0x0)
    OP_23(0x10F)
    OP_23(0x90)
    PlayEffect(0x3, 0xFF, 0xFF, -12000, 4600, 5930, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(2000)
    OP_82(0x0, 0x2)
    FadeToDark(2000, 16777215, -1)

    ChrTalk(    #70 op#A op#5
        0xB,
        "#1189F#6P#10A呀啊啊啊！？\x05\x02",
    )


    def lambda_30C9():
        OP_96(0x109, 0xFFFFCE00, 0x0, 0x1E50, 0xC8, 0x1388)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_30C9)
    OP_99(0x109, 0x1D, 0x20, 0x2EE)
    OP_0D()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_82(0x3, 0x0)
    OP_82(0x4, 0x0)
    OP_82(0x5, 0x0)
    OP_82(0x6, 0x0)
    OP_44(0x10F, 0x0)
    OP_44(0x10F, 0x3)
    SetChrPos(0x10F, -3000, 0, 1690, 270)
    ClearChrFlags(0x109, 0x4)
    SetChrPos(0x109, -11320, 0, 9220, 180)
    ClearChrFlags(0x109, 0x2)
    SetChrSubChip(0x109, 0)
    SetChrChipByIndex(0x109, 65535)
    OP_6D(-11790, 0, 4700, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2390, 0)
    OP_6C(224000, 0)
    OP_6E(402, 0)
    OP_8C(0x109, 180, 0)
    OP_8C(0x10F, 270, 0)
    CloseMessageWindow()
    OP_7A(0xFF, 0x2)
    OP_7B()
    ClearChrFlags(0x109, 0x2000)
    OP_6F(0x3, 10)
    OP_6F(0x4, 10)
    SetMapFlags(0x10)
    Sleep(2000)
    FadeToBright(3000, 16777215)
    OP_D7(0x0, 0, 0)
    LoadEffect(0x3, "Scraft\\\\sc000_31.eff")
    PlayEffect(0x3, 0x7, 0xFF, -11960, 4500, 5930, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_43(0x10F, 0x0, 0x0, 0x14)
    Sleep(3000)
    OP_82(0x7, 0x0)
    WaitChrThread(0x10F, 0x0)

    ChrTalk(    #71
        0x10F,
        (
            "#173F#7P照、照明恢复了……\x02\x03",

            "导力停止现象失效了吗！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xB, 0, 400)
    OP_62(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #72
        0xB,
        (
            "#1185F#6P怎、怎么会……\x02\x03",

            "你到底，做了什么！？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #73
        0x109,
        (
            "#1066F嘿嘿，没什么大不了的。\x02\x03",

            "只是将古代遗物破坏时\x01",
            "释放的庞大导力\x01",
            "打了过去。\x02\x03",

            "就连福音也\x01",
            "短路了呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xB,
        "#1187F#6P不、不可能……\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x101, -12110, 0, 16900, 180)
    SetChrPos(0xF7, -9990, 0, 16900, 180)

    def lambda_3359():
        OP_8E(0xFE, 0xFFFFD0B2, 0x0, 0x2940, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3359)
    Sleep(100)

    def lambda_3379():
        OP_8E(0xFE, 0xFFFFD8FA, 0x0, 0x2940, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_3379)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0xF7, 0x1)

    ChrTalk(    #75
        0x101,
        "#1018F#2P凯文先生，太棒了！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33EA")

    ChrTalk(    #76
        0x106,
        "#051F#5P干得好，不良神父！\x02",
    )

    CloseMessageWindow()
    Jump("loc_340C")

    label("loc_33EA")


    ChrTalk(    #77
        0x103,
        "#021F#5P成功了呢，神父先生！\x02",
    )

    CloseMessageWindow()

    label("loc_340C")


    ChrTalk(    #78
        0x109,
        "#1071F#5P呀～过奖过奖。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xB,
        (
            "#1187F#6P呜……\x01",
            "那又怎么样！\x02\x03",

            "就算不用什么福音\x01",
            "你们也不是我的对手！\x02\x03",

            "#1186F奥尔杰尤的力量，就让你们见识见识！\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_1D(0x29)
    Sleep(500)
    OP_8F(0xB, 0xFFFFCFFE, 0x7D0, 0x73A, 0x7D0, 0x0)

    def lambda_34BE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_34BE)
    OP_22(0xE6, 0x0, 0x64)
    OP_B0(0x5, 0xA)
    OP_6F(0x5, 331)
    OP_70(0x5, 0x15E)
    OP_73(0x5)
    SetChrFlags(0xB, 0x80)

    def lambda_34EF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_34EF)
    Sleep(500)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 32)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x109, 35)
    SetChrSubChip(0x109, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3539")
    SetChrChipByIndex(0x106, 33)
    SetChrSubChip(0x106, 0)
    Jump("loc_3543")

    label("loc_3539")

    SetChrChipByIndex(0x103, 34)
    SetChrSubChip(0x103, 0)

    label("loc_3543")

    OP_0D()
    OP_22(0x10F, 0x0, 0x64)
    OP_43(0x2F, 0x0, 0x0, 0x15)
    OP_8C(0x109, 90, 400)
    OP_6D(-9950, 0, 4770, 1500)

    ChrTalk(    #80
        0x109,
        (
            "#1069F#2P尤莉亚上尉！\x02\x03",

            "受到福音短路影响\x01",
            "坦克的机能应该也下降了！\x02\x03",

            "要阻止它只有趁现在！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x10F,
        "#178F是吗……明白了！\x02",
    )

    CloseMessageWindow()
    OP_8C(0x109, 180, 400)

    ChrTalk(    #82
        0x101,
        "#1006F#2P尤莉亚小姐，拜托了！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_364D")

    ChrTalk(    #83
        0x106,
        (
            "#051F#2P大叔真传的剑技，\x01",
            "就让我们见识见识吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3680")

    label("loc_364D")


    ChrTalk(    #84
        0x103,
        (
            "#526F#2P先生真传的剑技，\x01",
            "就让我们见识见识吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3680")


    ChrTalk(    #85
        0x10F,
        "#171F呼……明白了！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x2F, 0x0)
    Fade(250)
    PlayEffect(0x1, 0x3, 0x2F, -950, 2750, -1800, 0, -30, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x4, 0x2F, -950, 2800, -2370, 0, -30, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x5, 0x2F, 500, 1500, -2000, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x6, 0x2F, -500, 1500, -2000, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(250)

    def lambda_3783():
        OP_6D(-11160, 0, 3600, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3783)

    def lambda_379B():
        OP_6B(2000, 400)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_379B)
    SetChrFlags(0x10F, 0x1000)
    SetChrFlags(0x109, 0x1000)
    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0xF7, 0x1000)
    SetChrChipByIndex(0x10F, 43)

    def lambda_37C4():
        OP_8F(0xFE, 0xFFFFDBA2, 0x0, 0x55A, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_37C4)
    Sleep(50)
    SetChrChipByIndex(0x109, 42)

    def lambda_37E9():
        OP_8F(0xFE, 0xFFFFCEA0, 0x0, 0x1284, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_37E9)
    Sleep(50)
    SetChrChipByIndex(0x101, 39)

    def lambda_380E():
        OP_8F(0xFE, 0xFFFFCBDA, 0x0, 0x15FE, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_380E)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_383E")
    SetChrChipByIndex(0x106, 40)
    Jump("loc_3843")

    label("loc_383E")

    SetChrChipByIndex(0x103, 41)

    label("loc_3843")


    def lambda_3849():
        OP_8F(0xFE, 0xFFFFD396, 0x0, 0x164E, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_3849)
    Sleep(400)
    OP_31(0xE, 0x0, 0x3B)
    OP_31(0xE, 0x3, 0xFA)
    OP_31(0xE, 0x5, 0x6E)
    OP_31(0xE, 0xFE, 0x0)
    OP_41(0xE, 0x82, 0xFF)
    OP_41(0xE, 0x101, 0xFF)
    OP_41(0xE, 0x122, 0xFF)
    OP_35(0xE, 0x0)
    OP_37(0xE, 0x0)
    OP_37(0xE, 0x1)
    OP_37(0xE, 0x2)
    OP_37(0xE, 0x3)
    OP_37(0xE, 0x4)
    OP_37(0xE, 0x5)
    OP_34(0xE, 0x6F)
    OP_34(0xE, 0x73)
    OP_34(0xE, 0x39)
    OP_34(0xE, 0x46)
    OP_34(0xE, 0x47)
    OP_34(0xE, 0x18)
    OP_BB(0xE, 0x6, 0x11A)
    OP_44(0x101, 0xFF)
    OP_44(0x109, 0xFF)
    OP_44(0x10F, 0xFF)
    OP_44(0xF7, 0xFF)
    Battle(0x44E, 0x0, 0x0, 0x0, 0xFF)
    Return()

    # Function_17_11E5 end

    def Function_18_38D9(): pass

    label("Function_18_38D9")

    PlayEffect(0x3, 0x1, 0xFF, -9700, 1500, 1670, 90, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x3, 0x2, 0xFF, -9700, 1500, 1000, 90, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(400)
    PlayEffect(0x4, 0xFF, 0xFF, -800, 250, -1940, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x1, 0x0)
    OP_6F(0x1, 2)
    OP_70(0x1, 0xA)
    Sleep(100)
    PlayEffect(0x4, 0xFF, 0xFF, -800, 250, -1940, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x2, 0x0)
    Sleep(100)
    OP_6F(0x1, 11)
    OP_70(0x1, 0x3C)

    def lambda_39E9():
        OP_96(0x1B, 0x5B4, 0x0, 0xFFFFE7DC, 0x7D0, 0x7D0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_39E9)
    SetChrChipByIndex(0x1B, 21)
    SetChrSubChip(0x1B, 3)
    Sleep(100)
    WaitChrThread(0x1B, 0x1)
    SetChrFlags(0x1B, 0x2)
    SetChrChipByIndex(0x1B, 29)
    SetChrSubChip(0x1B, 1)
    Return()

    # Function_18_38D9 end

    def Function_19_3A25(): pass

    label("Function_19_3A25")


    def lambda_3A2B():

        label("loc_3A2B")

        OP_9E(0xFE, 0x1E, 0x0, 0x1388, 0x7D0)
        OP_48()
        Jump("loc_3A2B")

    QueueWorkItem2(0xFE, 3, lambda_3A2B)
    Sleep(500)
    OP_99(0xFE, 0x3, 0x0, 0x3E8)
    OP_44(0xFE, 0x3)
    SetChrChipByIndex(0xFE, 22)
    SetChrSubChip(0xFE, 0)
    Sleep(500)
    Return()

    # Function_19_3A25 end

    def Function_20_3A64(): pass

    label("Function_20_3A64")

    SetChrChipByIndex(0xFE, 43)
    OP_8E(0xFE, 0xFFFFEC78, 0x0, 0x69A, 0x3E8, 0x0)
    OP_44(0xFE, 0x3)
    SetChrChipByIndex(0x10F, 22)
    SetChrSubChip(0x10F, 0)
    OP_8C(0x10F, 0, 400)
    Sleep(500)
    OP_8C(0x10F, 270, 400)
    Sleep(500)
    Return()

    # Function_20_3A64 end

    def Function_21_3AA4(): pass

    label("Function_21_3AA4")


    def lambda_3AAA():

        label("loc_3AAA")

        OP_7C(0x32, 0x32, 0xBB8, 0x64)
        OP_48()
        Jump("loc_3AAA")

    QueueWorkItem2(0x2F, 3, lambda_3AAA)
    OP_22(0x110, 0x0, 0x64)
    PlayEffect(0x0, 0x1, 0x2F, 2000, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x2, 0x2F, -2000, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_8C(0x2F, 45, 20)
    Sleep(500)
    OP_8F(0x2F, 0xFFFFCDA6, 0x0, 0xA28, 0x3E8, 0x0)
    Sleep(500)
    OP_8F(0x2F, 0xFFFFC5FE, 0x0, 0x4B0, 0x3E8, 0x0)
    OP_23(0x110)
    OP_44(0x2F, 0x3)
    OP_82(0x1, 0x2)
    OP_82(0x2, 0x2)
    Return()

    # Function_21_3AA4 end

    def Function_22_3B75(): pass

    label("Function_22_3B75")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_23(0x10F)
    AddParty(0xE, 0xF9, 0xFF)
    OP_82(0x3, 0x0)
    OP_82(0x4, 0x0)
    OP_82(0x5, 0x0)
    OP_82(0x6, 0x0)
    ClearChrFlags(0x2F, 0x80)
    OP_72(0x5, 0x4)
    SetChrPos(0x2F, -14380, 0, -8330, 0)
    OP_A1(0x2F, 0x5)
    OP_6F(0x5, 311)
    LoadEffect(0x0, "map\\\\mpsmk0.eff")
    PlayEffect(0x0, 0x0, 0xFF, -13200, 3500, -5000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0xFF, 2000, 600, 3460, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x2, 0xFF, 1220, 600, -2270, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x101, -14540, 0, -1200, 180)
    SetChrPos(0x10F, -12870, 0, -1230, 180)
    SetChrPos(0xF7, -14350, 0, 570, 180)
    SetChrPos(0x109, -12660, 0, 750, 180)
    SetChrChipByIndex(0x101, 32)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x109, 35)
    SetChrSubChip(0x109, 0)
    SetChrChipByIndex(0x10F, 22)
    SetChrSubChip(0x10F, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3CE9")
    SetChrChipByIndex(0x106, 33)
    SetChrSubChip(0x106, 0)
    Jump("loc_3CF3")

    label("loc_3CE9")

    SetChrChipByIndex(0x103, 34)
    SetChrSubChip(0x103, 0)

    label("loc_3CF3")

    OP_72(0x0, 0x10)
    OP_72(0x1, 0x10)
    OP_72(0x0, 0x4)
    OP_72(0x1, 0x4)
    OP_A1(0x30, 0x0)
    OP_A1(0x31, 0x1)
    SetChrPos(0x30, 1540, 0, 3700, 90)
    SetChrPos(0x31, 1190, 0, -2000, 90)
    OP_6F(0x0, 60)
    OP_6F(0x1, 60)
    OP_72(0x3, 0x4)
    OP_72(0x4, 0x4)
    OP_6F(0x3, 10)
    OP_6F(0x4, 10)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    SetChrBattleFlags(0x1A, 0x20)
    SetChrBattleFlags(0x1B, 0x20)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    SetChrPos(0x1A, 2130, 0, 6400, 270)
    SetChrPos(0x1B, 1460, 0, -6180, 270)
    SetChrPos(0x1C, 5510, 0, -1750, 270)
    SetChrPos(0x1D, 5700, 0, 520, 270)
    SetChrPos(0x1E, 5710, 0, -3450, 270)
    SetChrPos(0x1F, 5630, 0, 1960, 270)
    SetChrPos(0x20, 7090, 0, -1780, 270)
    SetChrPos(0x21, 7090, 0, -120, 270)
    SetChrChipByIndex(0x1A, 21)
    SetChrChipByIndex(0x1B, 21)
    SetChrChipByIndex(0x1C, 21)
    SetChrChipByIndex(0x1D, 21)
    SetChrChipByIndex(0x1E, 21)
    SetChrChipByIndex(0x1F, 21)
    SetChrChipByIndex(0x20, 21)
    SetChrChipByIndex(0x21, 21)
    SetChrSubChip(0x1A, 3)
    SetChrSubChip(0x1B, 3)
    SetChrSubChip(0x1C, 3)
    SetChrSubChip(0x1D, 3)
    SetChrSubChip(0x1E, 3)
    SetChrSubChip(0x1F, 3)
    SetChrSubChip(0x20, 3)
    SetChrSubChip(0x21, 3)
    SetChrFlags(0x36, 0x80)
    SetChrFlags(0x37, 0x80)
    SetChrFlags(0x38, 0x80)
    SetChrFlags(0x39, 0x80)
    OP_6D(-15120, 0, -4350, 0)
    OP_67(0, 6960, -10000, 0)
    OP_6B(2400, 0)
    OP_6C(224000, 0)
    OP_6E(422, 0)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #86
        0x101,
        "#1018F#2P成、成功了……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x10F,
        (
            "#171F#5P啊啊……\x01",
            "看来完全停住了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3F0C():
        OP_6D(-15080, 0, -6490, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3F0C)

    def lambda_3F24():
        OP_67(0, 8370, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3F24)

    def lambda_3F3C():
        OP_6B(2250, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3F3C)
    OP_22(0x6A, 0x0, 0x64)
    OP_B0(0x5, 0xA)
    OP_6F(0x5, 311)
    OP_70(0x5, 0x14A)
    OP_73(0x5)
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xB, -13000, 2000, -8200, 0)
    SetChrFlags(0xB, 0x1)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xB, 0x40)

    def lambda_3F96():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xC8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_3F96)
    OP_8F(0xB, 0xFFFFCD38, 0x9C4, 0xFFFFDFF8, 0x7D0, 0x0)
    Sleep(500)

    ChrTalk(    #88
        0xB,
        (
            "#1187F#6P呜……\x01",
            "干得不错嘛……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x10F,
        (
            "#178F#5P凯诺娜，你输了。\x02\x03",

            "老老实实投降吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xB,
        (
            "#1185F#6P开什么玩笑！\x02\x03",

            "怎能因为这种事\x01",
            "就放弃解放阁下！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4051():
        OP_67(0, 7100, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_4051)

    def lambda_4069():
        OP_6B(2590, 3000)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_4069)
    SetChrChipByIndex(0xB, 44)
    SetChrSubChip(0xB, 4)
    OP_22(0x23B, 0x0, 0x64)
    OP_96(0xB, 0xFFFFCB30, 0xABE, 0xFFFFE278, 0x3E8, 0x1388)
    SetChrChipByIndex(0xB, 23)
    SetChrSubChip(0xB, 0)
    Sleep(300)
    OP_22(0x6A, 0x0, 0x64)
    Sleep(500)
    OP_43(0x2C, 0x1, 0x0, 0x19)
    Sleep(300)
    OP_43(0x2D, 0x1, 0x0, 0x1A)
    Sleep(300)
    OP_43(0x2E, 0x1, 0x0, 0x1B)
    WaitChrThread(0x2E, 0x1)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    OP_1D(0x33)

    ChrTalk(    #91
        0xB,
        (
            "#1186F#6P尤莉亚！　游击士！\x01",
            "这是最后一战了！\x02\x03",

            "来堂堂正正地决个胜负吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x101,
        (
            "#1007F#2P用完坦克\x01",
            "之后才说这种话……\x02\x03",

            "#1006F好啊！\x01",
            "要来就来吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x10F,
        (
            "#176F#5P看来和你\x01",
            "一决胜负的时刻已经到来了……\x02\x03",

            "#177F……来吧，凯诺娜！\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x101, 0x1000)
    SetChrChipByIndex(0x101, 39)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_41E4")
    SetChrFlags(0x106, 0x1000)
    SetChrChipByIndex(0x106, 40)
    Jump("loc_41EE")

    label("loc_41E4")

    SetChrFlags(0x103, 0x1000)
    SetChrChipByIndex(0x103, 41)

    label("loc_41EE")

    SetChrFlags(0x109, 0x1000)
    SetChrChipByIndex(0x109, 42)
    SetChrFlags(0x10F, 0x1000)
    SetChrChipByIndex(0x10F, 43)
    SetChrChipByIndex(0xB, 44)
    SetChrChipByIndex(0x2C, 25)
    SetChrChipByIndex(0x2D, 26)
    SetChrChipByIndex(0x2E, 25)

    def lambda_421C():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF830, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_421C)

    def lambda_4237():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF830, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_4237)

    def lambda_4252():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF830, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4252)

    def lambda_426D():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF830, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_426D)

    def lambda_4288():
        OP_90(0xFE, 0xFFFFFE0C, 0x0, 0x7D0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_4288)

    def lambda_42A3():
        OP_90(0xFE, 0xFFFFFE0C, 0x0, 0x7D0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_42A3)

    def lambda_42BE():
        OP_90(0xFE, 0x1F4, 0x0, 0x7D0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_42BE)

    def lambda_42D9():
        OP_6B(2000, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_42D9)
    Sleep(300)
    OP_44(0x101, 0xFF)
    OP_44(0x10F, 0xFF)
    OP_44(0x109, 0xFF)
    OP_44(0xF7, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0x2C, 0xFF)
    OP_44(0x2D, 0xFF)
    OP_44(0x2E, 0xFF)
    Battle(0x45E, 0x0, 0x0, 0x0, 0xFF)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_20(0x0)
    Return()

    # Function_22_3B75 end

    def Function_23_433D(): pass

    label("Function_23_433D")

    OP_7E(0x3E8, 0xF830, 0xFE0C, 0x50, 0x0)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_20(0x0)
    Sleep(1000)
    OP_1D(0x54)
    AddParty(0xE, 0xF9, 0xFF)
    SetChrPos(0x101, -18580, 0, -1200, 270)
    SetChrPos(0xF7, -17350, 0, 170, 270)
    SetChrPos(0x109, -17070, 0, -1450, 270)
    SetChrPos(0x10F, -18780, 0, 320, 270)
    SetChrChipByIndex(0x101, 32)
    SetChrSubChip(0x101, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_43CE")
    SetChrChipByIndex(0x106, 33)
    SetChrSubChip(0x106, 0)
    Jump("loc_43D8")

    label("loc_43CE")

    SetChrChipByIndex(0x103, 34)
    SetChrSubChip(0x103, 0)

    label("loc_43D8")

    SetChrChipByIndex(0x109, 35)
    SetChrSubChip(0x109, 0)
    SetChrChipByIndex(0x10F, 22)
    SetChrSubChip(0x10F, 0)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x2C, 0x80)
    ClearChrFlags(0x2D, 0x80)
    ClearChrFlags(0x2E, 0x80)
    SetChrPos(0xB, -23470, 0, -40, 90)
    SetChrPos(0x2C, -23800, 0, 2380, 90)
    SetChrPos(0x2D, -25000, 0, 1040, 90)
    SetChrPos(0x2E, -24000, 0, -1130, 90)
    SetChrFlags(0x2C, 0x2)
    SetChrFlags(0x2D, 0x2)
    SetChrFlags(0x2E, 0x2)
    SetChrFlags(0x2C, 0x800)
    SetChrFlags(0x2D, 0x800)
    SetChrFlags(0x2E, 0x800)
    SetChrChipByIndex(0xB, 27)
    SetChrChipByIndex(0x2C, 28)
    SetChrChipByIndex(0x2D, 28)
    SetChrChipByIndex(0x2E, 28)
    SetChrSubChip(0xB, 3)
    SetChrSubChip(0x2C, 1)
    SetChrSubChip(0x2D, 4)
    SetChrSubChip(0x2E, 7)
    ClearChrFlags(0x2F, 0x80)
    OP_72(0x5, 0x4)
    SetChrPos(0x2F, -14380, 0, -8330, 0)
    OP_A1(0x2F, 0x5)
    OP_6F(0x5, 330)
    LoadEffect(0x0, "map\\\\mpsmk0.eff")
    PlayEffect(0x0, 0x0, 0xFF, -14380, 2500, -6590, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0xFF, 2000, 600, 3460, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x2, 0xFF, 1220, 600, -2270, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    LoadEffect(0x1, "map\\\\mp064_01.eff")
    LoadEffect(0x2, "map\\\\mp065_01.eff")
    LoadEffect(0x3, "map\\\\mp064_00.eff")
    LoadEffect(0x4, "map\\\\mp065_00.eff")
    LoadEffect(0x5, "map\\\\mp021_00.eff")
    OP_72(0x0, 0x10)
    OP_72(0x1, 0x10)
    OP_72(0x0, 0x4)
    OP_72(0x1, 0x4)
    OP_A1(0x30, 0x0)
    OP_A1(0x31, 0x1)
    SetChrPos(0x30, 1540, 0, 3700, 90)
    SetChrPos(0x31, 1190, 0, -2000, 90)
    OP_6F(0x0, 60)
    OP_6F(0x1, 60)
    OP_72(0x3, 0x4)
    OP_72(0x4, 0x4)
    OP_6F(0x3, 10)
    OP_6F(0x4, 10)
    SetChrFlags(0x36, 0x80)
    SetChrFlags(0x37, 0x80)
    SetChrFlags(0x38, 0x80)
    SetChrFlags(0x39, 0x80)
    OP_6D(-21000, 0, -490, 0)
    OP_67(0, 10150, -10000, 0)
    OP_6B(1700, 0)
    OP_6C(224000, 0)
    OP_6E(422, 0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    SetChrBattleFlags(0x1A, 0x20)
    SetChrBattleFlags(0x1B, 0x20)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    SetChrPos(0x1A, 2130, 0, 6400, 270)
    SetChrPos(0x1B, 1460, 0, -6180, 270)
    SetChrPos(0x1C, 5510, 0, -1750, 270)
    SetChrPos(0x1D, 5700, 0, 520, 270)
    SetChrPos(0x1E, 5710, 0, -3450, 270)
    SetChrPos(0x1F, 5630, 0, 1960, 270)
    SetChrPos(0x20, 7090, 0, -1780, 270)
    SetChrPos(0x21, 7090, 0, -120, 270)
    SetChrChipByIndex(0x1A, 21)
    SetChrChipByIndex(0x1B, 21)
    SetChrChipByIndex(0x1C, 21)
    SetChrChipByIndex(0x1D, 21)
    SetChrChipByIndex(0x1E, 21)
    SetChrChipByIndex(0x1F, 21)
    SetChrChipByIndex(0x20, 21)
    SetChrChipByIndex(0x21, 21)
    SetChrSubChip(0x1A, 3)
    SetChrSubChip(0x1B, 3)
    SetChrSubChip(0x1C, 3)
    SetChrSubChip(0x1D, 3)
    SetChrSubChip(0x1E, 3)
    SetChrSubChip(0x1F, 3)
    SetChrSubChip(0x20, 3)
    SetChrSubChip(0x21, 3)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #94
        0xB,
        (
            "#1321F#2P呜……唔唔……\x02\x03",

            "理查德阁下……\x01",
            "实在……抱歉……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x10F,
        (
            "#175F#6P呼呼……\x02\x03",

            "终、终于结束了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x101,
        "#1007F#5P真、真是累死人了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x109,
        (
            "#1068F#5P呼呼……\x01",
            "因、因为是连续作战啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4885")

    ChrTalk(    #98
        0x106,
        (
            "#556F#6P哦……\x01",
            "总算成功了啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48AE")

    label("loc_4885")


    ChrTalk(    #99
        0x103,
        (
            "#524F#6P呼……\x01",
            "看来总算成功了呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48AE")

    SetChrFlags(0xC, 0x40)
    SetChrPos(0xC, -17890, 0, -11940, 0)

    NpcTalk(    #100
        0xC,
        "男人的声音",
        "#4P结、结束了吗……？\x02",
    )

    CloseMessageWindow()
    Fade(500)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    Sleep(100)
    ClearChrFlags(0xF7, 0x2)
    SetChrChipByIndex(0xF7, 65535)
    SetChrSubChip(0xF7, 0)
    Sleep(100)
    ClearChrFlags(0x109, 0x2)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    Sleep(100)
    ClearChrFlags(0x10F, 0x2)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    OP_0D()
    Sleep(100)

    def lambda_4946():
        OP_6D(-19790, 0, -4520, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4946)

    def lambda_495E():
        OP_6B(2009, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_495E)
    ClearChrFlags(0xC, 0x80)

    def lambda_4973():
        OP_8E(0xC, 0xFFFFB9B0, 0x0, 0xFFFFDCB0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_4973)

    def lambda_498E():

        label("loc_498E")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_498E")

    QueueWorkItem2(0x101, 2, lambda_498E)
    Sleep(100)

    def lambda_49A4():

        label("loc_49A4")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_49A4")

    QueueWorkItem2(0xF7, 2, lambda_49A4)
    Sleep(50)

    def lambda_49BA():

        label("loc_49BA")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_49BA")

    QueueWorkItem2(0x109, 2, lambda_49BA)
    Sleep(50)

    def lambda_49D0():

        label("loc_49D0")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_49D0")

    QueueWorkItem2(0x10F, 2, lambda_49D0)
    WaitChrThread(0xC, 0x1)
    OP_8C(0xC, 0, 400)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #101
        0x101,
        "#1004F#2P啊，公爵先生……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x109,
        (
            "#1060F#5P怎么……\x01",
            "原来被关在坦克里了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xC,
        "#220F#6P唔，算是吧……\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0x2)
    OP_44(0xF7, 0x2)
    OP_44(0x109, 0x2)
    OP_44(0x10F, 0x2)

    def lambda_4A6B():
        OP_6D(-18080, 0, -2070, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4A6B)

    def lambda_4A83():
        OP_6B(1670, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4A83)
    OP_8E(0xC, 0xFFFFBA50, 0x0, 0xFFFFF38A, 0x7D0, 0x0)
    OP_8C(0xC, 0, 400)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #104
        0xC,
        (
            "#220F#5P看来这次\x01",
            "不得不向你们道谢了……\x02\x03",

            "#221F作为答谢，就把我秘藏多年的\x01",
            "连环画佳作让给你们吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0xF7, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x10F, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #105
        0x101,
        (
            "#1016F心、心领了……\x02\x03",

            "#1006F不过，真没想到会被公爵先生\x01",
            "感谢呢──\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_4BDC():
        OP_6D(-17930, 0, -2800, 800)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4BDC)
    OP_8F(0x101, 0xFFFFB924, 0x0, 0xFFFFF600, 0x1388, 0x0)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #106
        0x101,
        (
            "#1020F#4P#3S玲呢！？#2S\x02\x03",

            "#3S玲没事吗！？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #107
        0xC,
        (
            "#226F#5P怎、怎么突然说什么……\x02\x03",

            "谁啊，那个叫玲的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x101,
        (
            "#1005F#4P是个女孩子啦！\x01",
            "穿白裙子的！\x02\x03",

            "不在坦克里吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xC,
        (
            "#222F#5P除、除了那些家伙之外\x01",
            "就只有我在了……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 600)
    Sleep(500)

    def lambda_4D05():
        OP_6D(-22590, 0, -220, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4D05)

    def lambda_4D1D():
        OP_8F(0xFE, 0xFFFFAC04, 0x0, 0xFFFFFF56, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4D1D)

    def lambda_4D38():

        label("loc_4D38")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_4D38")

    QueueWorkItem2(0xC, 2, lambda_4D38)

    def lambda_4D49():

        label("loc_4D49")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_4D49")

    QueueWorkItem2(0xF7, 2, lambda_4D49)

    def lambda_4D5A():

        label("loc_4D5A")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_4D5A")

    QueueWorkItem2(0x109, 2, lambda_4D5A)

    def lambda_4D6B():

        label("loc_4D6B")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_4D6B")

    QueueWorkItem2(0x10F, 2, lambda_4D6B)
    WaitChrThread(0x101, 0x0)
    OP_8C(0x101, 270, 400)
    OP_44(0xC, 0x2)
    OP_44(0xF7, 0x2)
    OP_44(0x109, 0x2)
    OP_44(0x10F, 0x2)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #110
        0x101,
        (
            "#1005F#6P喂！\x01",
            "玲怎么样了！？\x02\x03",

            "被关在哪里！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xB,
        (
            "#1182F……？\x01",
            "你说什么呢……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x101,
        (
            "#1009F#6P到、到了这个地步\x01",
            "别再装傻了！\x02\x03",

            "当然就是你们\x01",
            "从协会掳走的女孩啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xB,
        (
            "#1184F从协会掳走……\x02\x03",

            "#1183F……是吗……\x01",
            "是这么回事啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x101,
        "#1004F#6P哎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xB,
        "#1181F哈哈哈……\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_20(0x7D0)

    ChrTalk(    #116
        0xB,
        "#1188F#3S啊哈哈哈哈哈哈哈哈哈哈哈！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #117
        0x101,
        "#1020F#6P等、等等……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x10F,
        (
            "#173F#5P凯诺娜……\x01",
            "到底怎么回事？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xB,
        (
            "#1181F这能\x01",
            "不让人发笑吗！\x02\x03",

            "#1189F我！\x02\x03",

            "为阁下完成众多\x01",
            "谋略的我！\x02\x03",

            "#1187F……竟然被那种小丫头\x01",
            "完全利用了……！\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x14, 0x1)
    SetChrFlags(0x14, 0x4)
    SetChrPos(0x14, -27100, 7300, -880, 90)
    Sleep(500)

    NpcTalk(    #120
        0x14,
        "少女的声音",
        (
            "#3P嘻嘻。\x01",
            "叫人家小丫头多没礼貌呀。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xF7, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_1D(0x5A)
    Sleep(500)

    def lambda_50A1():
        OP_6D(-29980, 870, -950, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_50A1)

    def lambda_50B9():
        OP_67(0, 5490, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_50B9)

    def lambda_50D1():
        OP_6B(2810, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_50D1)

    def lambda_50E1():
        OP_6E(599, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_50E1)
    OP_6C(270000, 4000)
    WaitChrThread(0x101, 0x3)
    Sleep(500)

    ChrTalk(    #121
        0x101,
        (
            "#1004F#5P………………………………\x02\x03",

            "……………咦。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(-34440, 890, 2870, 0)
    OP_67(0, 7990, -10000, 0)
    OP_6B(3420, 0)
    OP_6C(297000, 0)
    OP_6E(272, 0)
    OP_0D()

    def lambda_5183():
        OP_8E(0xFE, 0xFFFFAF10, 0x0, 0xFFFFFB96, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_5183)
    Sleep(200)

    def lambda_51A3():
        OP_8E(0xFE, 0xFFFFAF10, 0x0, 0x37A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_51A3)
    Sleep(100)

    def lambda_51C3():
        OP_8E(0xFE, 0xFFFFB41A, 0x0, 0xFFFFFFC4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_51C3)

    NpcTalk(    #122
        0x14,
        "玲",
        (
            "#261F哈哈哈，晚上好。\x01",
            "今晚月色真美。\x02\x03",

            "今宵的茶会…\x01",
            "大家尽情享受到了吗？\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xF7, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0x109, 0x0)

    ChrTalk(    #123
        0x109,
        "#1064F#5P什、什么……！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5281")

    ChrTalk(    #124
        0x106,
        "#055F#5P小孩……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_529D")

    label("loc_5281")


    ChrTalk(    #125
        0x103,
        "#023F#5P女孩子……！？\x02",
    )

    CloseMessageWindow()

    label("loc_529D")


    ChrTalk(    #126
        0x101,
        (
            "#1026F#2P……玲………………\x02\x03",

            "你、你在干什么。\x01",
            "爬到那种地方……\x02\x03",

            "#1020F很、很危险的呀！？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #127
        0x14,
        "玲",
        "#263F………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x101,
        (
            "#1025F#2P真是的……\x01",
            "真像只猫一样。\x02\x03",

            "现在就去救你\x01",
            "在那里等一下……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #129
        0x14,
        "玲",
        (
            "#1305F哈哈哈，没那个必要。\x02\x03",

            "因为这里\x01",
            "可是最上等的席位。\x02\x03",

            "作为举办茶会的主人，\x01",
            "当然有权利站在这里呀～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x101,
        "#1026F#2P……咦…………\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x14, 0)
    SetChrSubChip(0x14, 8)
    OP_0D()
    Sleep(500)

    def lambda_5412():
        OP_99(0x14, 0x8, 0x2, 0x7D0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_5412)
    Sleep(200)
    Fade(500)

    def lambda_542C():
        OP_6B(3300, 0)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_542C)
    OP_22(0x1F9, 0x0, 0x64)
    WaitChrThread(0x14, 0x1)
    Sleep(500)

    def lambda_544B():
        OP_99(0x14, 0x2, 0x1, 0x5DC)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_544B)
    WaitChrThread(0x14, 0x1)
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x14, 10)
    SetChrSubChip(0x14, 0)
    OP_0D()
    Sleep(500)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x200, 0x4B, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x200, 0xFFFFFF, 0x0, "C_VIS116._CH")
    OP_C6(0x0, 0x0, 100000, 0, 500)
    OP_C6(0x0, 0x3, -1, 500, 0)
    Sleep(1000)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("玲")

    AnonymousTalk(    #131
        (
            "#1306F执行者ＮＯ．ⅩⅤ。\x01",
            "『歼灭天使』玲──\x02\x03",

            "大家都是这样称呼我的。\x02\x03",

            "有点没品位的名字，\x01",
            "我并不是很喜欢呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, 16777215, 250, 0)
    Sleep(1000)

    ChrTalk(    #132
        0x101,
        "#1020F#2P…………骗人……………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x10F,
        (
            "#173F#5P这，这样的孩子…\x01",
            "竟是『噬身之蛇』的一员！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x14,
        (
            "#263F哈哈哈。\x01",
            "『结社』不分孩子和大人。\x02\x03",

            "只分有用和没用。\x02\x03",

            "#1305F玲很有用。\x02\x03",

            "就像从前的『漆黑之牙』一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x101,
        "#1020F#2P！！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x109,
        (
            "#1069F#5P这、这么说……那个是？\x02\x03",

            "发信给我的\x01",
            "是小妹妹你！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x14,
        (
            "#1306F嗯嗯，是玲哦。\x02\x03",

            "#263F恐吓信一共发了９封。\x02\x03",

            "教会的哥哥１封。\x02\x03",

            "情报部的姐姐１封。\x02\x03",

            "还有，艾丝蒂尔１封。\x02\x03",

            "#1305F总共１２封──哈哈哈，\x01",
            "好像一直在写信呢，\x02\x03",

            "莱维会夸奖我吗。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_576F")

    ChrTalk(    #138
        0x106,
        (
            "#057F#5P这、这一切阴谋难道\x01",
            "全部是你设计的吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_57A0")

    label("loc_576F")


    ChrTalk(    #139
        0x103,
        (
            "#022F#5P难、难道这一切\x01",
            "全部是你设计的吗……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57A0")


    ChrTalk(    #140
        0x14,
        (
            "#263F因为玲是招待大家\x01",
            "来参加茶会的主人嘛。\x02\x03",

            "让出席的客人\x01",
            "感到无聊可不行啊。\x02\x03",

            "我很努力的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x101,
        (
            "#1003F#2P……那………\x02\x03",

            "#1005F那么，爸爸和妈妈呢？\x02\x03",

            "玲的爸爸妈妈\x01",
            "到底怎样了啊！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x14,
        (
            "#264F？？？\x02\x03",

            "#269F啊啊，怎么。\x01",
            "还没发现啊。\x02\x03",

            "#263F哈哈哈，是玲\x01",
            "太厉害了呢……\x02\x03",

            "还是艾丝蒂尔你们\x01",
            "太迟钝了呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x101,
        "#1019F#2P你、你说什么……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x14,
        (
            "#1306F哈哈哈，生气可不好哦。\x02\x03",

            "……是说这个吧？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_22(0xBD, 0x0, 0x64)
    SetChrPos(0x18, -27000, 8500, -2300, 90)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x20)
    SetChrFlags(0x18, 0x4)
    OP_9F(0x18, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_5959():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_5959)

    def lambda_596B():
        OP_8F(0xFE, 0xFFFF9688, 0x1F40, 0xFFFFF704, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 3, lambda_596B)
    Sleep(300)
    OP_22(0xBD, 0x0, 0x64)
    SetChrPos(0x19, -27000, 8500, -3200, 90)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x20)
    SetChrFlags(0x19, 0x4)
    OP_9F(0x19, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_59BB():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_59BB)

    def lambda_59CD():
        OP_8F(0xFE, 0xFFFF9688, 0x1F40, 0xFFFFF380, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 3, lambda_59CD)
    WaitChrThread(0x19, 0x3)
    Sleep(500)

    ChrTalk(    #145
        0x18,
        "#1364F#5P……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x19,
        "#1373F#5P……………………………\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #147
        0x101,
        "#1020F#2P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x14,
        (
            "#263F这不是玲的\x01",
            "爸爸妈妈。\x02\x03",

            "#1306F已经用完了\x01",
            "……就要这样！\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x14, 0x20)
    OP_8C(0x14, 180, 400)
    ClearChrFlags(0x14, 0x20)
    Fade(250)
    SetChrChipByIndex(0x14, 0)
    SetChrSubChip(0x14, 1)
    OP_22(0xD5, 0x0, 0x64)
    OP_0D()
    Sleep(500)
    SetChrFlags(0x18, 0x20)
    SetChrFlags(0x19, 0x20)
    SetChrFlags(0x18, 0x800)
    SetChrFlags(0x19, 0x800)
    ClearChrFlags(0x18, 0x1)
    ClearChrFlags(0x19, 0x1)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_5AE5():
        OP_6D(-34440, 1890, 1870, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5AE5)

    def lambda_5AFD():
        OP_67(0, 7000, -10000, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5AFD)

    def lambda_5B15():
        OP_6B(3200, 500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5B15)

    def lambda_5B25():
        OP_96(0xFE, 0xFFFF9566, 0x2260, 0xFFFFFA24, 0x7D0, 0x2710)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_5B25)
    Sleep(200)
    OP_22(0x1F9, 0x0, 0x64)

    def lambda_5B4D():
        OP_99(0x14, 0x1, 0x7, 0xBB8)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_5B4D)
    OP_43(0x14, 0x1, 0x0, 0x26)
    WaitChrThread(0x14, 0x0)
    OP_96(0x14, 0xFFFF9566, 0x1C84, 0xFFFFFA24, 0x0, 0xBB8)
    OP_22(0xA4, 0x0, 0x64)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)
    Fade(500)
    OP_6D(-22230, 0, -20, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2009, 0)
    OP_6C(315000, 0)
    OP_6E(336, 0)
    OP_0D()

    def lambda_5BD7():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5BD7)

    def lambda_5BE5():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_5BE5)
    Sleep(100)

    def lambda_5BF8():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5BF8)

    def lambda_5C06():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_5C06)
    WaitChrThread(0x14, 0x1)

    ChrTalk(    #149
        0x10F,
        "#173F#2P什么！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x101,
        (
            "#1020F#5P啊啊？\x02\x03",

            "#1022F你、你、你……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 500)
    Sleep(500)

    ChrTalk(    #151
        0x101,
        "#1005F#6P#3S在干什么啊啊啊！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_8C(0xF7, 270, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5CD7")

    ChrTalk(    #152
        0x106,
        (
            "#054F#6P镇定，艾丝蒂尔！\x02\x03",

            "并没有出血！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D03")

    label("loc_5CD7")


    ChrTalk(    #153
        0x103,
        (
            "#024F#6P艾丝蒂尔，冷静点！\x02\x03",

            "没出血吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D03")


    ChrTalk(    #154
        0x101,
        "#1004F#6P咦……啊……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)
    Sleep(500)

    ChrTalk(    #155
        0x101,
        "#1026F#5P……真……真的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x109,
        (
            "#1067F#2P『结社』制造的自动人偶……\x01",
            "而且和人一模一样……\x02\x03",

            "#1065F真是不得了……\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x14, 10)
    SetChrSubChip(0x14, 0)
    SetChrPos(0x14, -27290, 7300, -880, 90)
    Sleep(100)
    Fade(500)
    OP_6D(-34440, 890, 2870, 0)
    OP_67(0, 7990, -10000, 0)
    OP_6B(3420, 0)
    OP_6C(297000, 0)
    OP_6E(272, 0)
    OP_8C(0x101, 180, 0)
    OP_8C(0xF7, 180, 0)
    OP_8C(0x109, 180, 0)
    OP_8C(0x10F, 180, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #157
        0x14,
        (
            "#263F哈哈哈，玲不在旁边\x01",
            "就不能操纵得像人一样了。\x02\x03",

            "但也有不输给\x01",
            "『人偶骑士』佩德罗的自信哦。\x02\x03",

            "#1306F啊，不过这次又找了乐子\x01",
            "又成为茶会的主人……\x02\x03",

            "扮演蒂娅公主的角色也真多啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x109,
        "#1068F#5P开、开啥玩笑……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x14,
        (
            "#1305F好了，得叫\x01",
            "真正的爸爸妈妈来了。\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x14, 47)
    SetChrSubChip(0x14, 0)
    OP_0D()
    OP_22(0xD5, 0x0, 0x64)
    OP_99(0x14, 0x0, 0x1, 0x3E8)
    Sleep(500)

    ChrTalk(    #160
        0x14,
        "#263F来吧——帕蒂尔·玛蒂尔。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_22(0x113, 0x1, 0x46)
    OP_24(0x113, 0x46)
    Sleep(500)

    def lambda_5F7E():

        label("loc_5F7E")

        OP_7C(0x14, 0x14, 0x7D0, 0x64)
        OP_48()
        Jump("loc_5F7E")

    QueueWorkItem2(0x2F, 3, lambda_5F7E)
    Sleep(1000)
    OP_A3(0x0)
    OP_43(0x101, 0x1, 0x0, 0x1E)
    Sleep(50)
    OP_43(0xF7, 0x1, 0x0, 0x1F)
    Sleep(50)
    OP_43(0x109, 0x1, 0x0, 0x20)
    Sleep(50)
    OP_43(0x10F, 0x1, 0x0, 0x21)
    Sleep(50)
    OP_43(0xC, 0x1, 0x0, 0x1E)

    def lambda_5FD8():
        OP_6D(-24790, 0, -7120, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5FD8)

    def lambda_5FF0():
        OP_6C(225000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5FF0)

    def lambda_6000():
        OP_6B(4300, 10000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_6000)
    OP_24(0x113, 0x50)
    Sleep(1000)
    OP_24(0x113, 0x55)
    Sleep(1000)
    OP_24(0x113, 0x5A)
    Sleep(1000)
    OP_24(0x113, 0x5F)
    Sleep(1000)
    OP_24(0x113, 0x64)

    def lambda_6038():

        label("loc_6038")

        OP_7C(0x32, 0x32, 0xBB8, 0x64)
        OP_48()
        Jump("loc_6038")

    QueueWorkItem2(0x2F, 3, lambda_6038)
    WaitChrThread(0x101, 0x3)
    OP_A2(0x0)

    ChrTalk(    #161
        0x101,
        "#1026F#5P这、这声音是……\x02",
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #162
        0x10F,
        "#177F#2P上面！　当心！\x02",
    )

    CloseMessageWindow()
    OP_A1(0x33, 0x6)
    SetChrFlags(0x33, 0x4)
    ClearChrFlags(0x33, 0x80)
    SetChrFlags(0x33, 0x8)
    OP_72(0x6, 0x4)
    SetChrPos(0x33, -21490, 15000, -8050, 0)
    SetChrFlags(0x33, 0x1)
    OP_51(0x33, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x33, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x40)
    OP_71(0x6, 0x20)
    OP_B0(0x6, 0xF)
    OP_6F(0x6, 241)
    OP_70(0x6, 0x104)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xF7, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_B0(0x6, 0xF)
    OP_6F(0x6, 260)
    OP_70(0x6, 0xF1)

    def lambda_61C3():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_61C3)

    def lambda_61D1():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_61D1)
    Sleep(100)

    def lambda_61E4():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_61E4)

    def lambda_61F2():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_61F2)

    def lambda_6200():
        OP_8F(0x33, 0xFFFFAC0E, 0x0, 0xFFFFE08E, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_6200)
    Sleep(500)
    OP_72(0x6, 0x20)
    OP_6F(0x6, 221)
    OP_70(0x6, 0xF0)
    WaitChrThread(0x33, 0x1)
    SetChrChipByIndex(0x14, 10)
    SetChrSubChip(0x14, 0)
    OP_6D(-22260, 0, -9450, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(212000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x19, 0x800)
    ClearMapFlags(0x10)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0x2F, 0x3)
    OP_23(0x113)
    OP_22(0x88, 0x0, 0x64)
    OP_22(0xF5, 0x0, 0x64)
    OP_7C(0x0, 0x190, 0x1388, 0x5DC)
    OP_73(0x6)
    OP_71(0x6, 0x20)
    OP_D8(0x6, 0x1F4)
    OP_6F(0x6, 1)
    OP_70(0x6, 0x28)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    SetMapFlags(0x10)

    ChrTalk(    #163
        0x101,
        "#1020F#3S什！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xC,
        "#226F#3S#5P呀呀！？\x02",
    )

    CloseMessageWindow()
    OP_43(0xC, 0x1, 0x0, 0x25)
    OP_43(0xC, 0x0, 0x0, 0x24)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6346")

    ChrTalk(    #165
        0x106,
        "#055F好、好大……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_6361")

    label("loc_6346")


    ChrTalk(    #166
        0x103,
        "#523F怎么这么大……！\x02",
    )

    CloseMessageWindow()

    label("loc_6361")


    ChrTalk(    #167
        0x109,
        "#1069F#5P什、什么呀！这东西！？\x02",
    )

    CloseMessageWindow()

    def lambda_638C():
        OP_6C(237000, 2500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_638C)
    OP_72(0x6, 0x20)

    def lambda_63A1():
        OP_8C(0xFE, 45, 60)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_63A1)
    OP_6F(0x6, 201)
    OP_70(0x6, 0xD2)
    OP_22(0xEC, 0x0, 0x64)
    Sleep(300)
    OP_22(0xEC, 0x0, 0x64)
    Sleep(300)
    OP_22(0xEC, 0x0, 0x64)
    WaitChrThread(0x33, 0x1)
    OP_73(0x6)
    Sleep(500)
    OP_22(0x115, 0x0, 0x64)
    OP_B0(0x6, 0xA)
    OP_6F(0x6, 301)
    OP_70(0x6, 0x13B)
    OP_73(0x6)
    OP_6F(0x5, 231)
    OP_70(0x5, 0xFA)
    OP_7C(0x12C, 0x12C, 0xBB8, 0x64)
    OP_6F(0x6, 316)
    OP_70(0x6, 0x154)
    OP_22(0x3C6, 0x0, 0x64)
    OP_73(0x6)
    OP_71(0x6, 0x20)
    OP_6F(0x6, 341)
    OP_70(0x6, 0x17C)

    ChrTalk(    #168
        0x101,
        "#1026F#1P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x10F,
        "#173F#1P把『福音』！？\x02",
    )

    CloseMessageWindow()
    Sleep(100)

    def lambda_647B():
        OP_6D(-31920, 0, -6080, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_647B)
    OP_B0(0x6, 0x19)
    OP_72(0x6, 0x20)
    OP_6F(0x6, 381)
    OP_70(0x6, 0x1A4)
    OP_22(0x115, 0x0, 0x64)
    Sleep(800)
    OP_7D(0x0, 0x14, 0x32, 0x1F4)

    def lambda_64BC():
        OP_6D(-25540, 0, -10760, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_64BC)

    def lambda_64D4():
        OP_67(0, 5750, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_64D4)

    def lambda_64EC():
        OP_6B(3750, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_64EC)

    def lambda_64FC():
        OP_6C(225000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_64FC)

    def lambda_650C():
        OP_6E(250, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_650C)
    SetChrChipByIndex(0x14, 46)
    SetChrSubChip(0x14, 4)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_652B():
        OP_96(0x14, 0xFFFFAA10, 0xBB8, 0xFFFFEC78, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_652B)
    Sleep(700)
    OP_CF(0x14, 0x6, "Frame85__ren")
    ClearChrFlags(0x14, 0x4)
    ClearChrFlags(0x14, 0x1)
    SetChrFlags(0x14, 0x20)
    SetChrChipByIndex(0x14, 0)
    SetChrSubChip(0x14, 0)
    OP_22(0xA4, 0x0, 0x64)
    OP_7D(0x1, 0x14, 0x0, 0x0)
    ClearChrFlags(0x14, 0x1)
    OP_8C(0x14, 0, 400)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #170
        0x14,
        (
            "#1306F#5P这就是玲的爸爸妈妈『帕蒂尔·玛蒂尔』。\x02\x03",

            "像爸爸一样强大，\x01",
            "像妈妈一样温柔。\x02\x03",

            "除此以外\x01",
            "不需要别的爸爸妈妈了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Sleep(500)
    SetChrPos(0x22, -10900, 0, 230, 270)
    SetChrPos(0x23, -10370, 0, -1430, 270)

    NpcTalk(    #171
        0x22,
        "男人的声音",
        "#2P发、发现目标！\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #172
        0x23,
        "女孩的声音",
        "#5P哇哇，那是什么！？\x02",
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_66A4():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_66A4)

    def lambda_66B2():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_66B2)

    def lambda_66C0():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_66C0)

    def lambda_66CE():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_66CE)

    def lambda_66DC():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_66DC)
    Fade(1000)
    OP_6D(-21560, 0, -7400, 0)
    OP_67(0, 4560, -10000, 0)
    OP_6B(8250, 0)
    OP_6C(223000, 0)
    OP_6E(165, 0)
    OP_D2(0x2702EA, 0x2702F4, 0x1D)
    OP_D2(0x2702EB, 0x2702F5, 0x1E)
    OP_D2(0x702EF, 0x702F6, 0x1F)
    OP_D2(0x70021, 0x70029, 0x20)
    OP_D2(0x70051, 0x70059, 0x21)
    OP_D2(0x70031, 0x70039, 0x22)
    OP_D2(0x70041, 0x70049, 0x23)
    OP_D2(0x70061, 0x70069, 0x24)
    OP_D2(0x70071, 0x70079, 0x25)
    OP_D2(0x270091, 0x270095, 0x27)
    SetChrFlags(0xF, 0x40)
    SetChrFlags(0x10, 0x40)
    SetChrFlags(0x11, 0x40)
    SetChrFlags(0x12, 0x40)
    SetChrFlags(0x13, 0x40)
    SetChrFlags(0x16, 0x40)
    SetChrFlags(0x15, 0x40)
    SetChrFlags(0x22, 0x40)
    SetChrFlags(0x23, 0x40)
    SetChrFlags(0x24, 0x40)
    SetChrFlags(0x25, 0x40)
    SetChrFlags(0x26, 0x40)
    SetChrFlags(0x27, 0x40)
    SetChrFlags(0x28, 0x40)
    SetChrFlags(0x29, 0x40)
    SetChrFlags(0x2A, 0x40)
    SetChrFlags(0x2B, 0x40)
    SetChrPos(0x13, 6000, 0, -1790, 270)
    SetChrPos(0x11, 6000, 0, -1370, 270)
    SetChrPos(0x12, 6000, 0, -3420, 270)
    SetChrPos(0x10, 6000, 0, -2160, 270)
    SetChrPos(0xF, 6000, 0, -2300, 270)
    SetChrPos(0x16, 6000, 0, -3260, 270)
    SetChrPos(0x15, 8000, 0, 510, 270)
    SetChrPos(0x22, 8000, 0, 2500, 270)
    SetChrPos(0x23, 8000, 0, 2400, 270)
    SetChrPos(0x24, 8000, 0, 800, 270)
    SetChrPos(0x25, 8000, 0, -90, 270)
    SetChrPos(0x26, 8000, 0, 2110, 270)
    SetChrPos(0x27, 8000, 0, 270, 270)
    SetChrPos(0x28, 8000, 0, 1610, 270)
    SetChrPos(0x29, 8000, 0, 2750, 270)
    SetChrPos(0x2A, 8000, 0, 2170, 270)
    SetChrPos(0x2B, 8000, 0, 1040, 270)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x15, 0x80)
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_6981")
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x40)
    SetChrPos(0xE, 6000, 0, -3010, 270)
    OP_43(0xE, 0x0, 0x0, 0x28)
    Jump("loc_69A3")

    label("loc_6981")

    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x40)
    SetChrPos(0xD, 6000, 0, -3010, 270)
    OP_43(0xD, 0x0, 0x0, 0x27)

    label("loc_69A3")

    OP_43(0x13, 0x0, 0x0, 0x29)
    OP_43(0x11, 0x0, 0x0, 0x2B)
    OP_43(0x10, 0x0, 0x0, 0x2C)
    OP_43(0x12, 0x0, 0x0, 0x2A)
    OP_43(0xF, 0x0, 0x0, 0x2D)
    OP_43(0x16, 0x0, 0x0, 0x2E)
    OP_43(0x15, 0x0, 0x0, 0x2F)
    OP_43(0x22, 0x0, 0x0, 0x30)
    OP_43(0x23, 0x0, 0x0, 0x31)
    OP_43(0x24, 0x0, 0x0, 0x32)
    OP_43(0x25, 0x0, 0x0, 0x33)
    OP_43(0x26, 0x0, 0x0, 0x34)
    OP_43(0x27, 0x0, 0x0, 0x35)
    OP_43(0x28, 0x0, 0x0, 0x36)
    OP_43(0x29, 0x0, 0x0, 0x37)
    OP_43(0x2A, 0x0, 0x0, 0x38)
    OP_43(0x2B, 0x0, 0x0, 0x39)
    WaitChrThread(0x13, 0x0)
    Sleep(500)

    ChrTalk(    #173
        0x13,
        "#1317F#6P巨、巨人！？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x15, 0x0)

    ChrTalk(    #174
        0x15,
        "#702F#4P怎可能……！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_6A88")

    ChrTalk(    #175
        0xE,
        "#054F#3P怎、怎么回事！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_6AA8")

    label("loc_6A88")


    ChrTalk(    #176
        0xD,
        "#024F#3P怎、怎么回事啊！？\x02",
    )

    CloseMessageWindow()

    label("loc_6AA8")


    ChrTalk(    #177
        0x11,
        "#065F#6P玲、玲……！？\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #178
        0x101,
        "#1026F#5P大家……\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(1000)
    OP_6D(-30740, 0, -15630, 0)
    OP_67(0, 2870, -10000, 0)
    OP_6B(5020, 0)
    OP_6C(225000, 0)
    OP_6E(245, 0)
    OP_8C(0x14, 0, 0)
    OP_8C(0x13, 270, 0)
    OP_8C(0x12, 270, 0)
    OP_8C(0xF, 270, 0)
    OP_8C(0x17, 270, 0)
    OP_8C(0x16, 270, 0)
    OP_8C(0x11, 270, 0)
    OP_8C(0x10, 270, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #179
        0x14,
        (
            "#263F#5P哈哈哈，安眠药的效果\x01",
            "看来发挥得正是时候。\x02\x03",

            "就像以前约修亚教的一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x101,
        "#1002F#2P！！！\x02",
    )

    CloseMessageWindow()

    def lambda_6BD1():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6BD1)

    def lambda_6BDF():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_6BDF)
    Sleep(100)

    def lambda_6BF2():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6BF2)

    def lambda_6C00():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_6C00)
    Sleep(100)

    def lambda_6C13():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_6C13)

    ChrTalk(    #181
        0x14,
        (
            "#1305F#5P其实啊，本来想\x01",
            "杀了艾丝蒂尔的。\x02\x03",

            "因为教授，\x01",
            "说约修亚不回来\x01",
            "是因为艾丝蒂尔嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x101,
        "#1020F#2P咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x14,
        (
            "#261F#5P不过，因为很开心\x01",
            "这次就特别饶了你。\x02\x03",

            "哈哈哈，是特别优待哦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x101,
        "#1020F#2P等、等等，玲！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x11,
        (
            "#065F#5P玲、玲！\x01",
            "这是怎么回事？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x14,
        (
            "#263F#5P哈哈哈，提妲也再见啦。\x02\x03",

            "和你在一起很开心\x01",
            "以后再一起吃冰淇淋吧。\x02\x03",

            "#1306F那么各位……\x02\x03",

            "今宵大家能出席茶会，\x01",
            "实在是感激不尽。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    def lambda_6DAA():
        OP_6D(-21660, 3000, -6840, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6DAA)

    def lambda_6DC2():
        OP_6B(2400, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6DC2)
    OP_22(0x113, 0x0, 0x64)
    Sleep(500)

    def lambda_6DDC():

        label("loc_6DDC")

        OP_7C(0x32, 0x32, 0xBB8, 0x64)
        OP_48()
        Jump("loc_6DDC")

    QueueWorkItem2(0x2F, 3, lambda_6DDC)
    OP_22(0x85, 0x1, 0x50)

    def lambda_6DFC():
        OP_67(0, 32810, -10000, 25000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6DFC)

    def lambda_6E14():
        OP_6C(0, 25000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6E14)
    ClearChrFlags(0x2C, 0x800)
    ClearChrFlags(0x2D, 0x800)
    ClearChrFlags(0x2E, 0x800)
    SetChrFlags(0x14, 0x20)
    SetChrFlags(0x14, 0x2)
    SetChrSubChip(0x14, 6)
    PlayEffect(0x5, 0x5, 0x33, 0, -500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xCC, 0x0, 0x64)
    PlayEffect(0x3, 0x3, 0x33, 4400, 3000, 0, 0, 0, 15, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x4, 0x33, -4400, 3000, 0, 0, 0, 345, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x114, 0x0, 0x64)

    def lambda_6EEB():
        OP_8F(0x33, 0xFFFFAC0E, 0x1388, 0xFFFFE08E, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_6EEB)
    OP_B0(0x6, 0xA)
    OP_71(0x6, 0x20)
    OP_D8(0x6, 0x7D0)
    OP_6F(0x6, 461)
    OP_70(0x6, 0x1E0)
    PlayEffect(0x1, 0x3, 0x33, 4400, 3000, 0, 0, 0, 15, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x4, 0x33, -4400, 3000, 0, 0, 0, 345, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_6F8B():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_6F8B)

    def lambda_6F99():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_6F99)

    def lambda_6FA7():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_6FA7)

    def lambda_6FB5():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_6FB5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_6FD5")

    def lambda_6FCA():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_6FCA)
    Jump("loc_6FE3")

    label("loc_6FD5")


    def lambda_6FDB():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_6FDB)

    label("loc_6FE3")


    def lambda_6FE9():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_6FE9)

    def lambda_6FF7():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_6FF7)

    def lambda_7005():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_7005)

    def lambda_7013():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x22, 0, lambda_7013)

    def lambda_7021():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x23, 0, lambda_7021)

    def lambda_702F():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_702F)

    def lambda_703D():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x25, 0, lambda_703D)

    def lambda_704B():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x26, 0, lambda_704B)

    def lambda_7059():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_7059)

    def lambda_7067():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x27, 0, lambda_7067)
    Sleep(1000)

    def lambda_707A():
        OP_8F(0x33, 0xFFFFAC0E, 0x1388, 0xFFFFE08E, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_707A)
    Sleep(1000)

    def lambda_709A():
        OP_8F(0x33, 0xFFFFAC0E, 0x1388, 0xFFFFE08E, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_709A)
    OP_71(0x6, 0x20)
    OP_B0(0x6, 0xA)
    OP_82(0x5, 0x2)
    Sleep(800)

    def lambda_70C6():
        OP_8F(0x33, 0xFFFFAC0E, 0x1388, 0xFFFFE08E, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_70C6)
    Sleep(800)
    WaitChrThread(0x33, 0x1)

    def lambda_70EB():
        OP_8C(0x33, 180, 50)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_70EB)
    Sleep(500)
    SetChrSubChip(0x14, 7)
    Sleep(1000)
    SetChrSubChip(0x14, 0)
    WaitChrThread(0x33, 0x1)

    def lambda_7112():
        OP_6D(-21660, 3000, -15000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7112)

    def lambda_712A():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_712A)

    def lambda_7138():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_7138)

    def lambda_7146():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_7146)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_7166")

    def lambda_715B():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_715B)
    Jump("loc_7174")

    label("loc_7166")


    def lambda_716C():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_716C)

    label("loc_7174")


    def lambda_717A():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_717A)

    def lambda_7188():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_7188)

    def lambda_7196():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_7196)
    OP_72(0x6, 0x20)
    OP_6F(0x6, 481)
    OP_70(0x6, 0x1F4)
    OP_22(0x116, 0x0, 0x64)
    OP_73(0x6)
    OP_71(0x6, 0x20)
    OP_6F(0x6, 501)
    OP_70(0x6, 0x208)
    OP_22(0x114, 0x0, 0x64)
    PlayEffect(0x1, 0x3, 0x33, 500, -3300, -3600, 0, 80, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x4, 0x33, -500, -3300, -3600, 0, 80, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0x33, 1000, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0x33, 400, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0x33, -1000, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0x33, -400, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_7315():
        OP_90(0x33, 0x0, 0x2710, 0xFFFF2928, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_7315)
    Sleep(1500)
    ClearChrFlags(0x33, 0x1)

    def lambda_733A():
        OP_90(0x33, 0x0, 0x7530, 0xFFFF2928, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_733A)
    Sleep(1500)
    OP_43(0x14, 0x3, 0x0, 0x3A)

    def lambda_7361():

        label("loc_7361")

        OP_7C(0x1F4, 0x1F4, 0xBB8, 0x64)
        OP_48()
        Jump("loc_7361")

    QueueWorkItem2(0x2F, 3, lambda_7361)

    def lambda_737C():
        OP_90(0x33, 0x0, 0x9C40, 0xFFFF2928, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_737C)
    Sleep(1500)

    def lambda_739C():
        OP_90(0x33, 0x1388, 0xEA60, 0xFFFF2928, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_739C)
    Sleep(1000)

    def lambda_73BC():
        OP_90(0x33, 0x1388, 0x186A0, 0xFFFF2928, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_73BC)
    Sleep(1000)
    SetChrSubChip(0x14, 7)

    def lambda_73E1():
        OP_90(0x33, 0x1388, 0x249F0, 0xFFFF2928, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_73E1)
    Sleep(1000)
    SetChrSubChip(0x14, 6)

    def lambda_7406():
        OP_90(0x33, 0x1388, 0x3D090, 0xFFFF2158, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_7406)
    OP_24(0x113, 0x64)
    Sleep(1000)

    ChrTalk(    #187 op#A op#5
        0x101,
        "#5S#30A#5P玲～～！！\x05\x02",
    )

    FadeToDark(4000, 0, -1)
    OP_24(0x113, 0x50)
    OP_24(0x85, 0x50)
    Sleep(1000)
    OP_24(0x113, 0x3C)
    OP_24(0x85, 0x3C)
    Sleep(1000)
    OP_24(0x113, 0x28)
    OP_24(0x85, 0x28)
    Sleep(1000)
    OP_24(0x113, 0x14)
    OP_24(0x85, 0x14)
    Sleep(1000)
    OP_23(0x113)
    OP_20(0xBB8)
    OP_44(0x2F, 0x3)
    OP_23(0x85)
    OP_44(0x33, 0x1)
    SetChrFlags(0x14, 0x80)
    OP_71(0x6, 0x4)
    WaitChrThread(0x101, 0x1)
    OP_21()
    OP_0D()
    ClearChrFlags(0x101, 0x40)
    OP_44(0x101, 0x1)
    OP_44(0x101, 0x2)
    Sleep(1000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T4313   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_23_433D end

    def Function_24_74BF(): pass

    label("Function_24_74BF")

    OP_96(0xFE, 0xFFFFBD02, 0x0, 0xFFFFEE80, 0x5DC, 0x1388)
    OP_96(0xFE, 0xFFFFB3F2, 0x0, 0xFFFFFFD8, 0x3E8, 0x1388)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_24_74BF end

    def Function_25_74F5(): pass

    label("Function_25_74F5")

    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)
    SetChrPos(0xFE, -14240, 0, -12370, 0)
    OP_8E(0xFE, 0xFFFFD60C, 0x0, 0xFFFFD0D0, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFD620, 0x0, 0xFFFFE3EA, 0x1388, 0x0)
    OP_8C(0xFE, 0, 400)
    SetChrChipByIndex(0xFE, 48)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_25_74F5 end

    def Function_26_754A(): pass

    label("Function_26_754A")

    SetChrChipByIndex(0xFE, 26)
    SetChrSubChip(0xFE, 0)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)
    SetChrPos(0xFE, -14240, 0, -12370, 0)
    OP_8E(0xFE, 0xFFFFD60C, 0x0, 0xFFFFD0D0, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFD88C, 0x0, 0xFFFFDEA4, 0x1388, 0x0)
    OP_8C(0xFE, 0, 400)
    SetChrChipByIndex(0xFE, 24)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_26_754A end

    def Function_27_75A9(): pass

    label("Function_27_75A9")

    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)
    SetChrPos(0xFE, -14240, 0, -12370, 0)
    OP_8E(0xFE, 0xFFFFBADC, 0x0, 0xFFFFCE8C, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFBAF0, 0x0, 0xFFFFE39A, 0x1388, 0x0)
    OP_8C(0xFE, 0, 400)
    SetChrChipByIndex(0xFE, 48)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_27_75A9 end

    def Function_28_75FE(): pass

    label("Function_28_75FE")

    OP_8E(0xFE, 0xFFFFCBB2, 0x0, 0xA0, 0xFA0, 0x0)
    TurnDirection(0xFE, 0x14, 400)
    Return()

    # Function_28_75FE end

    def Function_29_761A(): pass

    label("Function_29_761A")

    OP_8E(0xFE, 0xFFFFD1B6, 0x0, 0x33E, 0xFA0, 0x0)
    TurnDirection(0xFE, 0x14, 400)
    Return()

    # Function_29_761A end

    def Function_30_7636(): pass

    label("Function_30_7636")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_766C")
    Sleep(200)
    OP_8C(0xFE, 180, 400)
    Sleep(500)
    OP_8C(0xFE, 270, 400)
    OP_8C(0xFE, 0, 400)
    Sleep(500)
    OP_8C(0xFE, 270, 400)
    Jump("Function_30_7636")

    label("loc_766C")

    Return()

    # Function_30_7636 end

    def Function_31_766D(): pass

    label("Function_31_766D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_76A3")
    Sleep(50)
    OP_8C(0xFE, 0, 400)
    Sleep(500)
    OP_8C(0xFE, 270, 400)
    OP_8C(0xFE, 180, 400)
    Sleep(500)
    OP_8C(0xFE, 270, 400)
    Jump("Function_31_766D")

    label("loc_76A3")

    Return()

    # Function_31_766D end

    def Function_32_76A4(): pass

    label("Function_32_76A4")

    OP_8C(0xFE, 90, 400)
    Sleep(500)

    label("loc_76B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_76E6")
    Sleep(150)
    OP_8C(0xFE, 0, 400)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    OP_8C(0xFE, 180, 400)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    Jump("loc_76B0")

    label("loc_76E6")

    Return()

    # Function_32_76A4 end

    def Function_33_76E7(): pass

    label("Function_33_76E7")

    OP_8C(0xFE, 90, 400)
    Sleep(500)

    label("loc_76F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7729")
    Sleep(100)
    OP_8C(0xFE, 180, 400)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    OP_8C(0xFE, 0, 400)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    Jump("loc_76F3")

    label("loc_7729")

    Return()

    # Function_33_76E7 end

    def Function_34_772A(): pass

    label("Function_34_772A")


    def lambda_7730():
        OP_8F(0xFE, 0xFFFFC3CE, 0x1B58, 0xFFFFF448, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7730)
    OP_8C(0xFE, 180, 100)
    Return()

    # Function_34_772A end

    def Function_35_774D(): pass

    label("Function_35_774D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7762")
    OP_99(0x109, 0xC, 0xF, 0x5DC)
    Jump("Function_35_774D")

    label("loc_7762")

    Return()

    # Function_35_774D end

    def Function_36_7763(): pass

    label("Function_36_7763")

    OP_8E(0xFE, 0xFFFFB744, 0x0, 0x622, 0xFA0, 0x0)
    OP_44(0xC, 0x1)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_36_7763 end

    def Function_37_7783(): pass

    label("Function_37_7783")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_77A6")
    OP_62(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)
    Jump("Function_37_7783")

    label("loc_77A6")

    Return()

    # Function_37_7783 end

    def Function_38_77A7(): pass

    label("Function_38_77A7")

    Sleep(200)
    OP_22(0x38F, 0x0, 0x64)

    def lambda_77B7():
        OP_99(0xFE, 0x0, 0x4, 0x5DC)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_77B7)

    def lambda_77C7():
        OP_96(0x18, 0xFFFFA272, 0x0, 0xFFFFF36C, 0x32, 0x1B58)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_77C7)
    Sleep(50)
    OP_22(0x38F, 0x0, 0x64)

    def lambda_77EF():
        OP_99(0xFE, 0x0, 0x4, 0x5DC)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_77EF)

    def lambda_77FF():
        OP_96(0x19, 0xFFFFA7F4, 0x0, 0xFFFFEF34, 0x32, 0x1B58)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_77FF)
    WaitChrThread(0x18, 0x1)
    OP_22(0xD1, 0x0, 0x64)

    def lambda_7827():
        OP_99(0xFE, 0x5, 0x7, 0x5DC)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_7827)
    WaitChrThread(0x19, 0x1)

    def lambda_783C():
        OP_99(0xFE, 0x5, 0x7, 0x5DC)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_783C)
    Return()

    # Function_38_77A7 end

    def Function_39_7847(): pass

    label("Function_39_7847")

    SetChrChipByIndex(0xFE, 32)
    OP_8E(0xFE, 0xFFFFBFFA, 0x0, 0xFFFFF43E, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 3)
    OP_8C(0xFE, 215, 400)
    Return()

    # Function_39_7847 end

    def Function_40_786D(): pass

    label("Function_40_786D")

    SetChrChipByIndex(0xFE, 33)
    OP_8E(0xFE, 0xFFFFBFFA, 0x0, 0xFFFFF43E, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 4)
    OP_8C(0xFE, 215, 400)
    Return()

    # Function_40_786D end

    def Function_41_7893(): pass

    label("Function_41_7893")

    Sleep(200)
    SetChrChipByIndex(0xFE, 39)
    OP_8E(0xFE, 0xFFFFBCC6, 0x0, 0xFFFFF902, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 9)
    OP_8C(0xFE, 215, 400)
    Return()

    # Function_41_7893 end

    def Function_42_78BE(): pass

    label("Function_42_78BE")

    Sleep(400)
    SetChrChipByIndex(0xFE, 37)
    OP_8E(0xFE, 0xFFFFC64E, 0x0, 0xFFFFF2A4, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 8)
    OP_8C(0xFE, 215, 400)
    Return()

    # Function_42_78BE end

    def Function_43_78E9(): pass

    label("Function_43_78E9")

    Sleep(600)
    SetChrChipByIndex(0xFE, 36)
    OP_8E(0xFE, 0xFFFFC20C, 0x0, 0xFFFFFAA6, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 7)
    OP_8C(0xFE, 215, 400)
    Return()

    # Function_43_78E9 end

    def Function_44_7914(): pass

    label("Function_44_7914")

    Sleep(800)
    SetChrChipByIndex(0xFE, 35)
    OP_8E(0xFE, 0xFFFFC5CC, 0x0, 0xFFFFF790, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 6)
    OP_8C(0xFE, 215, 400)
    Return()

    # Function_44_7914 end

    def Function_45_793F(): pass

    label("Function_45_793F")

    Sleep(1000)
    SetChrChipByIndex(0xFE, 34)
    OP_8E(0xFE, 0xFFFFCB76, 0x0, 0xFFFFF704, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 5)
    OP_8C(0xFE, 215, 400)
    Return()

    # Function_45_793F end

    def Function_46_796A(): pass

    label("Function_46_796A")

    Sleep(1200)
    OP_8E(0xFE, 0xFFFFCDBA, 0x0, 0xFFFFF344, 0x1388, 0x0)
    OP_8C(0xFE, 215, 400)
    Return()

    # Function_46_796A end

    def Function_47_798B(): pass

    label("Function_47_798B")

    Sleep(1500)
    SetChrChipByIndex(0xFE, 30)
    OP_8E(0xFE, 0xFFFFBE88, 0x0, 0x1FE, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 29)
    OP_8C(0xFE, 215, 400)
    Return()

    # Function_47_798B end

    def Function_48_79B6(): pass

    label("Function_48_79B6")

    Sleep(1700)
    SetChrChipByIndex(0xFE, 31)
    OP_8E(0xFE, 0xFFFFC400, 0x0, 0x1D6, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 17)
    OP_8C(0xFE, 215, 400)
    Return()

    # Function_48_79B6 end

    def Function_49_79E1(): pass

    label("Function_49_79E1")

    Sleep(1900)
    SetChrChipByIndex(0xFE, 31)
    OP_8E(0xFE, 0xFFFFC1A8, 0x0, 0x960, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 17)
    OP_8C(0xFE, 215, 400)
    Return()

    # Function_49_79E1 end

    def Function_50_7A0C(): pass

    label("Function_50_7A0C")

    Sleep(2100)
    SetChrChipByIndex(0xFE, 31)
    OP_8E(0xFE, 0xFFFFC9FA, 0x0, 0x320, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 17)
    OP_8C(0xFE, 215, 400)
    Return()

    # Function_50_7A0C end

    def Function_51_7A37(): pass

    label("Function_51_7A37")

    Sleep(2300)
    SetChrChipByIndex(0xFE, 31)
    OP_8E(0xFE, 0xFFFFCC3E, 0x0, 0xFFFFFFA6, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 17)
    OP_8C(0xFE, 215, 400)
    Return()

    # Function_51_7A37 end

    def Function_52_7A62(): pass

    label("Function_52_7A62")

    Sleep(2500)
    SetChrChipByIndex(0xFE, 31)
    OP_8E(0xFE, 0xFFFFC7F2, 0x0, 0x83E, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 17)
    OP_8C(0xFE, 215, 400)
    Return()

    # Function_52_7A62 end

    def Function_53_7A8D(): pass

    label("Function_53_7A8D")

    Sleep(2600)
    SetChrChipByIndex(0xFE, 31)
    OP_8E(0xFE, 0xFFFFD256, 0x0, 0x10E, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 17)
    OP_8C(0xFE, 215, 400)
    Return()

    # Function_53_7A8D end

    def Function_54_7AB8(): pass

    label("Function_54_7AB8")

    Sleep(2700)
    SetChrChipByIndex(0xFE, 31)
    OP_8E(0xFE, 0xFFFFD102, 0x0, 0x64A, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 17)
    OP_8C(0xFE, 215, 400)
    Return()

    # Function_54_7AB8 end

    def Function_55_7AE3(): pass

    label("Function_55_7AE3")

    Sleep(2900)
    SetChrChipByIndex(0xFE, 31)
    OP_8E(0xFE, 0xFFFFCE6E, 0x0, 0xABE, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 17)
    OP_8C(0xFE, 215, 400)
    Return()

    # Function_55_7AE3 end

    def Function_56_7B0E(): pass

    label("Function_56_7B0E")

    Sleep(3100)
    SetChrChipByIndex(0xFE, 31)
    OP_8E(0xFE, 0xFFFFD6DE, 0x0, 0x87A, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 17)
    OP_8C(0xFE, 215, 400)
    Return()

    # Function_56_7B0E end

    def Function_57_7B39(): pass

    label("Function_57_7B39")

    Sleep(3300)
    SetChrChipByIndex(0xFE, 31)
    OP_8E(0xFE, 0xFFFFDA12, 0x0, 0x410, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 17)
    OP_8C(0xFE, 215, 400)
    Return()

    # Function_57_7B39 end

    def Function_58_7B64(): pass

    label("Function_58_7B64")

    SetChrFlags(0x101, 0x40)

    def lambda_7B6F():
        OP_8E(0x101, 0xFFFFAD6C, 0x0, 0xFFFFC4E6, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7B6F)
    Sleep(800)

    def lambda_7B8F():
        OP_8E(0xFE, 0xFFFFA600, 0x0, 0xFFFFC52C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_7B8F)
    Sleep(200)

    def lambda_7BAF():
        OP_8E(0xFE, 0xFFFFB28A, 0x0, 0xFFFFC658, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7BAF)
    Sleep(200)

    def lambda_7BCF():
        OP_8E(0xFE, 0xFFFFAD1C, 0x0, 0xFFFFCA40, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_7BCF)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_7C0E")

    def lambda_7BF6():
        OP_8E(0xFE, 0xFFFFB1A4, 0x0, 0xFFFFCA72, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_7BF6)
    Jump("loc_7C29")

    label("loc_7C0E")


    def lambda_7C14():
        OP_8E(0xFE, 0xFFFFB1A4, 0x0, 0xFFFFCA72, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_7C14)

    label("loc_7C29")

    Sleep(200)

    def lambda_7C34():
        OP_8E(0xFE, 0xFFFFB474, 0x0, 0xFFFFCEC8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_7C34)
    Sleep(300)

    def lambda_7C54():
        OP_8E(0xFE, 0xFFFFA8D0, 0x0, 0xFFFFCA04, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_7C54)
    Sleep(300)

    def lambda_7C74():
        OP_8E(0xFE, 0xFFFFAB96, 0x0, 0xFFFFD0A8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_7C74)
    Sleep(200)

    def lambda_7C94():
        OP_8E(0xFE, 0xFFFFAF4C, 0x0, 0xFFFFD4AE, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_7C94)
    Sleep(200)

    def lambda_7CB4():
        OP_8E(0xFE, 0xFFFFB3DE, 0x0, 0xFFFFD864, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_7CB4)
    Sleep(300)

    def lambda_7CD4():
        OP_8E(0xFE, 0xFFFFAAEC, 0x0, 0xFFFFE2FA, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_7CD4)
    Sleep(200)

    def lambda_7CF4():
        OP_8E(0xFE, 0xFFFFAE7A, 0x0, 0xFFFFE4A8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_7CF4)
    Sleep(300)
    SetChrChipByIndex(0x15, 11)

    def lambda_7D19():
        OP_8E(0xFE, 0xFFFFAE7A, 0x0, 0xFFFFDC1A, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_7D19)
    Sleep(300)

    def lambda_7D39():
        OP_8E(0xFE, 0xFFFFAC36, 0x0, 0xFFFFEB10, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 0, lambda_7D39)
    Sleep(200)

    def lambda_7D59():
        OP_8E(0xFE, 0xFFFFB23A, 0x0, 0xFFFFEB42, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 0, lambda_7D59)
    Sleep(300)

    def lambda_7D79():
        OP_8E(0xFE, 0xFFFFB884, 0x0, 0xFFFFE994, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_7D79)

    def lambda_7D94():
        OP_8E(0xFE, 0xFFFFAF88, 0x0, 0xFFFFF06A, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 0, lambda_7D94)
    Sleep(300)

    def lambda_7DB4():
        OP_8E(0xFE, 0xFFFFB546, 0x0, 0xFFFFEFB6, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 0, lambda_7DB4)
    Sleep(200)

    def lambda_7DD4():
        OP_8E(0xFE, 0xFFFFBBE0, 0x0, 0xFFFFEE62, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 0, lambda_7DD4)
    Sleep(200)

    def lambda_7DF4():
        OP_8E(0xFE, 0xFFFFB5D2, 0x0, 0xFFFFF588, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 0, lambda_7DF4)
    Sleep(200)

    def lambda_7E14():
        OP_8E(0xFE, 0xFFFFBCA8, 0x0, 0xFFFFF3EE, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 0, lambda_7E14)
    Sleep(200)

    def lambda_7E34():
        OP_8E(0xFE, 0xFFFFBD16, 0x0, 0xFFFFFA42, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 0, lambda_7E34)
    Sleep(200)

    def lambda_7E54():
        OP_8E(0xFE, 0xFFFFC2C0, 0x0, 0xFFFFF470, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 0, lambda_7E54)
    Return()

    # Function_58_7B64 end

    def Function_59_7E6A(): pass

    label("Function_59_7E6A")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
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
        (0, "loc_7EE4"),
        (1, "loc_7EEA"),
        (SWITCH_DEFAULT, "loc_7EF0"),
    )


    label("loc_7EE4")

    OP_A2(0x1200)
    Jump("loc_7EF0")

    label("loc_7EEA")

    OP_A2(0x1201)
    Jump("loc_7EF0")

    label("loc_7EF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_7EFE")
    AddParty(0x5, 0xF7, 0xFF)
    Jump("loc_7F02")

    label("loc_7EFE")

    AddParty(0x2, 0xF7, 0xFF)

    label("loc_7F02")

    Return()

    # Function_59_7E6A end

    def Function_60_7F03(): pass

    label("Function_60_7F03")

    TalkBegin(0xFF)
    TalkEnd(0xFF)
    Return()

    # Function_60_7F03 end

    SaveToFile()

Try(main)
