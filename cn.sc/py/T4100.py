from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4100   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4100.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T4100_1 ._SN',
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
        '奥利维尔',                             # 9
        '玲',                                   # 10
        '士兵',                                 # 11
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
        '艾南',                                 # 31
        '亡命守护者',                           # 32
        '亡命守护者',                           # 33
        '亡命装甲兵',                           # 34
        '嘉瑟',                                 # 35
        '诺娜',                                 # 36
        '蒂库',                                 # 37
        '拉尔斯',                               # 38
        '托伊',                                 # 39
        '伯登',                                 # 40
        '拉塔娜',                               # 41
        '托朗老人',                             # 42
        '王国军士兵',                           # 43
        '王国军士兵',                           # 44
        '塔巴莎',                               # 45
        '萨米',                                 # 46
        '吉恩',                                 # 47
        '迪克斯',                               # 48
        '王都格兰赛尔·北街区',                 # 49
        '庭园大道方向',                         # 50
        '王都格兰赛尔·东街区',                 # 51
        '王都格兰赛尔·西街区',                 # 52
        '',                                     # 53
        '',                                     # 54
        '',                                     # 55
        '',                                     # 56
        '',                                     # 57
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
        'ED6_DT07/CH00030 ._CH',             # 00
        'ED6_DT27/CH03510 ._CH',             # 01
        'ED6_DT06/CH20043 ._CH',             # 02
        'ED6_DT07/CH01270 ._CH',             # 03
        'ED6_DT07/CH01050 ._CH',             # 04
        'ED6_DT07/CH01160 ._CH',             # 05
        'ED6_DT07/CH01470 ._CH',             # 06
        'ED6_DT07/CH01060 ._CH',             # 07
        'ED6_DT07/CH01200 ._CH',             # 08
        'ED6_DT07/CH01210 ._CH',             # 09
        'ED6_DT07/CH01100 ._CH',             # 0A
        'ED6_DT07/CH01640 ._CH',             # 0B
        'ED6_DT27/CH04610 ._CH',             # 0C
        'ED6_DT27/CH04611 ._CH',             # 0D
        'ED6_DT27/CH04620 ._CH',             # 0E
        'ED6_DT27/CH04621 ._CH',             # 0F
        'ED6_DT29/CH12570 ._CH',             # 10
        'ED6_DT29/CH12571 ._CH',             # 11
        'ED6_DT29/CH12350 ._CH',             # 12
        'ED6_DT29/CH12351 ._CH',             # 13
        'ED6_DT29/CH12320 ._CH',             # 14
        'ED6_DT29/CH12321 ._CH',             # 15
        'ED6_DT07/CH01130 ._CH',             # 16
        'ED6_DT07/CH01140 ._CH',             # 17
        'ED6_DT07/CH01150 ._CH',             # 18
        'ED6_DT07/CH01120 ._CH',             # 19
    )

    AddCharChipPat(
        'ED6_DT07/CH00030P._CP',             # 00
        'ED6_DT27/CH03510P._CP',             # 01
        'ED6_DT06/CH20043P._CP',             # 02
        'ED6_DT07/CH01270P._CP',             # 03
        'ED6_DT07/CH01050P._CP',             # 04
        'ED6_DT07/CH01160P._CP',             # 05
        'ED6_DT07/CH01470P._CP',             # 06
        'ED6_DT07/CH01060P._CP',             # 07
        'ED6_DT07/CH01200P._CP',             # 08
        'ED6_DT07/CH01210P._CP',             # 09
        'ED6_DT07/CH01100P._CP',             # 0A
        'ED6_DT07/CH01640P._CP',             # 0B
        'ED6_DT27/CH04610P._CP',             # 0C
        'ED6_DT27/CH04611P._CP',             # 0D
        'ED6_DT27/CH04620P._CP',             # 0E
        'ED6_DT27/CH04621P._CP',             # 0F
        'ED6_DT29/CH12570P._CP',             # 10
        'ED6_DT29/CH12571P._CP',             # 11
        'ED6_DT29/CH12350P._CP',             # 12
        'ED6_DT29/CH12351P._CP',             # 13
        'ED6_DT29/CH12320P._CP',             # 14
        'ED6_DT29/CH12321P._CP',             # 15
        'ED6_DT07/CH01130P._CP',             # 16
        'ED6_DT07/CH01140P._CP',             # 17
        'ED6_DT07/CH01150P._CP',             # 18
        'ED6_DT07/CH01120P._CP',             # 19
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -5720,
        Z                   = 0,
        Y                   = -36280,
        Direction           = 281,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 5550,
        Z                   = 0,
        Y                   = -54380,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -840,
        Z                   = 0,
        Y                   = -50090,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 710,
        Z                   = 0,
        Y                   = -50090,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -90,
        Z                   = 0,
        Y                   = -51500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 5760,
        Z                   = 0,
        Y                   = -46060,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = -2070,
        Z                   = 0,
        Y                   = -5120,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 3520,
        Z                   = 0,
        Y                   = 10640,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 4760,
        Z                   = 0,
        Y                   = -39600,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = -4540,
        Z                   = 0,
        Y                   = -29870,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = -9390,
        Z                   = 250,
        Y                   = -6510,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 8,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 8060,
        Z                   = 250,
        Y                   = 5500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = 8060,
        Z                   = 250,
        Y                   = 4120,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = 5990,
        Z                   = 0,
        Y                   = -7440,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = 10,
        Z                   = 250,
        Y                   = 36990,
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
        X                   = -50,
        Z                   = 0,
        Y                   = -90220,
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
        X                   = 54990,
        Z                   = 0,
        Y                   = -1130,
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
        X                   = -44420,
        Z                   = 0,
        Y                   = -19990,
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
        X                   = -430,
        Z                   = 0,
        Y                   = -39050,
        Unknown_0C          = 180,
        Unknown_0E          = 18,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x549,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -17930,
        Z                   = 0,
        Y                   = -20130,
        Unknown_0C          = 180,
        Unknown_0E          = 20,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x54A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -5660,
        Z                   = 0,
        Y                   = -1440,
        Unknown_0C          = 180,
        Unknown_0E          = 14,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x547,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 21340,
        Z                   = 0,
        Y                   = -230,
        Unknown_0C          = 180,
        Unknown_0E          = 12,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x546,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -13570,
        Z                   = 250,
        Y                   = -51100,
        Unknown_0C          = 180,
        Unknown_0E          = 16,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x548,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -5000,
        Y                   = -2000,
        Z                   = -65600,
        Range               = 5000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFF0344,
        Unknown_18          = 0x0,
        Unknown_1C          = 53,
    )

    DeclEvent(
        X                   = 9240,
        Y                   = 0,
        Z                   = -25000,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 61,
    )

    DeclEvent(
        X                   = -10280,
        Y                   = 0,
        Z                   = -11040,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 62,
    )

    DeclEvent(
        X                   = -14940,
        Y                   = 0,
        Z                   = -15750,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 62,
    )

    DeclEvent(
        X                   = -10290,
        Y                   = 0,
        Z                   = -30020,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 63,
    )

    DeclEvent(
        X                   = 9240,
        Y                   = 0,
        Z                   = -13010,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 64,
    )

    DeclEvent(
        X                   = 15900,
        Y                   = 0,
        Z                   = 6330,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 65,
    )


    DeclActor(
        TriggerX            = 9620,
        TriggerZ            = 500,
        TriggerY            = -25020,
        TriggerRange        = 800,
        ActorX              = 9620,
        ActorZ              = 1500,
        ActorY              = -25020,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 46,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 23690,
        TriggerZ            = 500,
        TriggerY            = -7620,
        TriggerRange        = 800,
        ActorX              = 23690,
        ActorZ              = 1500,
        ActorY              = -7620,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 46,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 16040,
        TriggerZ            = 500,
        TriggerY            = 6640,
        TriggerRange        = 800,
        ActorX              = 16040,
        ActorZ              = 1500,
        ActorY              = 6640,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 46,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -12480,
        TriggerZ            = 500,
        TriggerY            = -2460,
        TriggerRange        = 800,
        ActorX              = -12480,
        ActorZ              = 1500,
        ActorY              = -2460,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 46,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -10640,
        TriggerZ            = 500,
        TriggerY            = -11060,
        TriggerRange        = 800,
        ActorX              = -10640,
        ActorZ              = 1500,
        ActorY              = -11060,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 46,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -14870,
        TriggerZ            = 500,
        TriggerY            = -15350,
        TriggerRange        = 800,
        ActorX              = -14870,
        ActorZ              = 1500,
        ActorY              = -15350,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 46,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -10680,
        TriggerZ            = 500,
        TriggerY            = -29970,
        TriggerRange        = 800,
        ActorX              = -10680,
        ActorZ              = 1500,
        ActorY              = -29970,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 46,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -30,
        TriggerZ            = 300,
        TriggerY            = -43060,
        TriggerRange        = 800,
        ActorX              = -30,
        ActorZ              = 4300,
        ActorY              = -46060,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 0,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_986",          # 00, 0
        "Function_1_B2E",          # 01, 1
        "Function_2_CAF",          # 02, 2
        "Function_3_E2C",          # 03, 3
        "Function_4_E50",          # 04, 4
        "Function_5_EAD",          # 05, 5
        "Function_6_F3A",          # 06, 6
        "Function_7_FA9",          # 07, 7
        "Function_8_1018",         # 08, 8
        "Function_9_103C",         # 09, 9
        "Function_10_14F0",        # 0A, 10
        "Function_11_184A",        # 0B, 11
        "Function_12_1EC4",        # 0C, 12
        "Function_13_2133",        # 0D, 13
        "Function_14_2355",        # 0E, 14
        "Function_15_2B31",        # 0F, 15
        "Function_16_3013",        # 10, 16
        "Function_17_33BF",        # 11, 17
        "Function_18_353C",        # 12, 18
        "Function_19_3728",        # 13, 19
        "Function_20_38E8",        # 14, 20
        "Function_21_3A85",        # 15, 21
        "Function_22_3C5F",        # 16, 22
        "Function_23_3EC7",        # 17, 23
        "Function_24_4266",        # 18, 24
        "Function_25_4526",        # 19, 25
        "Function_26_4862",        # 1A, 26
        "Function_27_4894",        # 1B, 27
        "Function_28_48C6",        # 1C, 28
        "Function_29_48F8",        # 1D, 29
        "Function_30_4963",        # 1E, 30
        "Function_31_496F",        # 1F, 31
        "Function_32_5840",        # 20, 32
        "Function_33_5865",        # 21, 33
        "Function_34_58A9",        # 22, 34
        "Function_35_58ED",        # 23, 35
        "Function_36_591D",        # 24, 36
        "Function_37_594D",        # 25, 37
        "Function_38_597D",        # 26, 38
        "Function_39_59AD",        # 27, 39
        "Function_40_5CE4",        # 28, 40
        "Function_41_5F24",        # 29, 41
        "Function_42_6494",        # 2A, 42
        "Function_43_68F2",        # 2B, 43
        "Function_44_6920",        # 2C, 44
        "Function_45_694B",        # 2D, 45
        "Function_46_7135",        # 2E, 46
        "Function_47_716E",        # 2F, 47
        "Function_48_73E4",        # 30, 48
        "Function_49_765D",        # 31, 49
        "Function_50_76F6",        # 32, 50
        "Function_51_7777",        # 33, 51
        "Function_52_77F0",        # 34, 52
        "Function_53_7849",        # 35, 53
        "Function_54_7EEF",        # 36, 54
        "Function_55_7F0F",        # 37, 55
        "Function_56_7F2F",        # 38, 56
        "Function_57_7FB6",        # 39, 57
        "Function_58_803D",        # 3A, 58
        "Function_59_805D",        # 3B, 59
        "Function_60_807D",        # 3C, 60
        "Function_61_84CE",        # 3D, 61
        "Function_62_84D2",        # 3E, 62
        "Function_63_84D6",        # 3F, 63
        "Function_64_84DA",        # 40, 64
        "Function_65_84DE",        # 41, 65
    )


    def Function_0_986(): pass

    label("Function_0_986")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 2)), scpexpr(EXPR_END)), "loc_9D0")
    Call(0, 40)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x29, 0x80)
    SetChrFlags(0x2C, 0x80)
    SetChrFlags(0x2D, 0x80)
    SetChrFlags(0x2E, 0x80)
    SetChrFlags(0x2F, 0x80)
    Jump("loc_A5A")

    label("loc_9D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_9E4")
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x2B, 0x80)
    Jump("loc_A5A")

    label("loc_9E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_9F8")
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x2B, 0x80)
    Jump("loc_A5A")

    label("loc_9F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_A0C")
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x2B, 0x80)
    Jump("loc_A5A")

    label("loc_A0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_A20")
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x2B, 0x80)
    Jump("loc_A5A")

    label("loc_A20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A2E")
    Jump("loc_A5A")

    label("loc_A2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_A38")
    Jump("loc_A5A")

    label("loc_A38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_A42")
    Jump("loc_A5A")

    label("loc_A42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_A5A")
    SetChrPos(0x26, 16000, 250, 4030, 0)

    label("loc_A5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A81")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    Event(0, 30)

    label("loc_A81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_A9A")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    OP_A2(0x161A)
    Event(0, 24)
    Jump("loc_B2D")

    label("loc_A9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_AB3")
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    OP_A2(0x162D)
    Event(0, 25)
    Jump("loc_B2D")

    label("loc_AB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_AC9")
    OP_A3(0x10F2)
    SetMapFlags(0x10000000)
    Event(0, 31)
    Jump("loc_B2D")

    label("loc_AC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 3)), scpexpr(EXPR_END)), "loc_AE8")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F3)
    SetMapFlags(0x10000000)
    Event(0, 39)
    Jump("loc_B2D")

    label("loc_AE8")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_AF4"),
        (SWITCH_DEFAULT, "loc_B2D"),
    )


    label("loc_AF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B15")
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 42)
    Jump("loc_B2A")

    label("loc_B15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B2A")
    SetMapFlags(0x10000000)
    Event(0, 23)

    label("loc_B2A")

    Jump("loc_B2D")

    label("loc_B2D")

    Return()

    # Function_0_986 end

    def Function_1_B2E(): pass

    label("Function_1_B2E")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFDBDE0, 0x23005B)
    OP_51(0x35, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B6B")
    OP_B1("t4100_y")
    Jump("loc_B74")

    label("loc_B6B")

    OP_B1("t4100_n")

    label("loc_B74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 2)), scpexpr(EXPR_END)), "loc_BC6")
    OP_72(0x0, 0x10)
    OP_72(0x2, 0x10)
    OP_72(0x3, 0x10)
    OP_72(0x4, 0x10)
    OP_72(0x5, 0x10)
    OP_72(0x6, 0x10)
    OP_72(0x10, 0x10)
    OP_1B(0x9, 0x0, 0x30)
    OP_1B(0xA, 0x0, 0x2F)
    OP_77(0xFF, 0xBD, 0xA7, 0x0, 0x0)
    Call(0, 41)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)
    Jump("loc_BE4")

    label("loc_BC6")

    OP_64(0x0, 0x1)
    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)
    OP_64(0x3, 0x1)
    OP_64(0x4, 0x1)
    OP_64(0x5, 0x1)
    OP_64(0x6, 0x1)
    OP_B5(0x0)

    label("loc_BE4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x54F), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BF9")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C26")
    OP_1B(0x9, 0x0, 0x3B)
    OP_1B(0xA, 0x0, 0x3A)
    OP_1B(0xB, 0x0, 0x37)
    OP_1B(0xC, 0x0, 0x38)
    OP_1B(0xD, 0x0, 0x37)
    OP_1B(0xE, 0x0, 0x39)
    Jump("loc_C53")

    label("loc_C26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C53")
    OP_1B(0x9, 0x0, 0x3B)
    OP_1B(0xA, 0x0, 0x3A)
    OP_1B(0xB, 0x0, 0x37)
    OP_1B(0xC, 0x0, 0x38)
    OP_1B(0xD, 0x0, 0x37)
    OP_1B(0xE, 0x0, 0x39)
    Jump("loc_C53")

    label("loc_C53")

    OP_64(0x7, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x1, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C77")
    OP_65(0x7, 0x1)

    label("loc_C77")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C92")
    OP_82(0x84, 0x0)
    OP_82(0x88, 0x0)
    OP_82(0x89, 0x0)
    OP_82(0x8A, 0x0)
    Jump("loc_CAE")

    label("loc_C92")

    SoundDistance(0x1CB, 0x32, 0x0, 0xFFFF4A70, 0x7D0, 0x3A98, 0x64, 0x0)

    label("loc_CAE")

    Return()

    # Function_1_B2E end

    def Function_2_CAF(): pass

    label("Function_2_CAF")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CD4")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_E16")

    label("loc_CD4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CED")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_E16")

    label("loc_CED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D06")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_E16")

    label("loc_D06")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D1F")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_E16")

    label("loc_D1F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D38")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_E16")

    label("loc_D38")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D51")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_E16")

    label("loc_D51")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D6A")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_E16")

    label("loc_D6A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D83")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_E16")

    label("loc_D83")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D9C")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_E16")

    label("loc_D9C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DB5")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_E16")

    label("loc_DB5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DCE")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_E16")

    label("loc_DCE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DE7")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_E16")

    label("loc_DE7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E00")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_E16")

    label("loc_E00")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E16")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_E16")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E2B")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_E16")

    label("loc_E2B")

    Return()

    # Function_2_CAF end

    def Function_3_E2C(): pass

    label("Function_3_E2C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E4F")
    OP_8D(0xFE, 3700, -42040, 10110, -50100, 2000)
    Jump("Function_3_E2C")

    label("loc_E4F")

    Return()

    # Function_3_E2C end

    def Function_4_E50(): pass

    label("Function_4_E50")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EAC")
    OP_8E(0xFE, 0xFFFFF7EA, 0x0, 0xFFFF6E24, 0x8FC, 0x0)
    OP_8E(0xFE, 0x9CE, 0x0, 0xFFFF6E24, 0x8FC, 0x0)
    OP_8E(0xFE, 0x9CE, 0x0, 0x2166, 0x8FC, 0x0)
    OP_8E(0xFE, 0xFFFFF7EA, 0x0, 0x2166, 0x8FC, 0x0)
    Jump("Function_4_E50")

    label("loc_EAC")

    Return()

    # Function_4_E50 end

    def Function_5_EAD(): pass

    label("Function_5_EAD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F39")
    OP_8E(0xFE, 0xDC0, 0x0, 0xFFFF6532, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(2000)
    OP_8C(0xFE, 225, 400)
    Sleep(2000)
    OP_8E(0xFE, 0xFFFFF29A, 0x0, 0xFFFF6532, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(2000)
    OP_8C(0xFE, 270, 400)
    Sleep(2000)
    OP_8E(0xFE, 0xFFFFF29A, 0x0, 0x2990, 0x7D0, 0x0)
    OP_8E(0xFE, 0xDC0, 0x0, 0x2990, 0x7D0, 0x0)
    Jump("Function_5_EAD")

    label("loc_F39")

    Return()

    # Function_5_EAD end

    def Function_6_F3A(): pass

    label("Function_6_F3A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_FA8")
    OP_8E(0xFE, 0x1298, 0x0, 0xFFFF6550, 0x9C4, 0x0)
    Sleep(1500)
    OP_8C(0xFE, 90, 400)
    Sleep(1500)
    OP_8C(0xFE, 270, 400)
    Sleep(1500)
    OP_8E(0xFE, 0x1298, 0x0, 0xFFFFFB5A, 0x9C4, 0x0)
    Sleep(1500)
    OP_8C(0xFE, 90, 400)
    Sleep(1500)
    OP_8C(0xFE, 0, 400)
    Sleep(1500)
    Jump("Function_6_F3A")

    label("loc_FA8")

    Return()

    # Function_6_F3A end

    def Function_7_FA9(): pass

    label("Function_7_FA9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1017")
    OP_8E(0xFE, 0xFFFFEE44, 0x0, 0xFFFFAFC4, 0x9C4, 0x0)
    Sleep(1500)
    OP_8C(0xFE, 270, 400)
    Sleep(1500)
    OP_8C(0xFE, 90, 400)
    Sleep(1500)
    OP_8E(0xFE, 0xFFFFEEB2, 0x0, 0xFFFF6550, 0x9C4, 0x0)
    Sleep(1500)
    OP_8C(0xFE, 270, 400)
    Sleep(1500)
    OP_8C(0xFE, 90, 400)
    Sleep(1500)
    Jump("Function_7_FA9")

    label("loc_1017")

    Return()

    # Function_7_FA9 end

    def Function_8_1018(): pass

    label("Function_8_1018")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_103B")
    OP_8D(0xFE, -9540, -8220, -7490, -4270, 2000)
    Jump("Function_8_1018")

    label("loc_103B")

    Return()

    # Function_8_1018 end

    def Function_9_103C(): pass

    label("Function_9_103C")

    TalkBegin(0xFE)
    Call(6, 4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1059")
    OP_A9(0xD6)
    TalkEnd(0xFE)
    Return()

    label("loc_1059")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_106A")
    TalkEnd(0xFE)
    Return()

    label("loc_106A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_1074")
    Jump("loc_14EC")

    label("loc_1074")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1113")

    ChrTalk(    #0
        0xFE,
        (
            "我刚在试验像以前一样\x01",
            "用火力来做爆米花，失败了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "哈哈，我这个人一直不走运，\x01",
            "对麻烦已经习以为常了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "不久就会恢复了，\x01",
            "现在就努力克服吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14EC")

    label("loc_1113")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_11A9")

    ChrTalk(    #3
        0xFE,
        (
            "昨天我去进货，\x01",
            "以令人惊讶的价格\x01",
            "买到了爆米花的原料。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "机器虽然坏了，\x01",
            "不过说不定也是好事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "就像牧师大人说的那样，\x01",
            "应该向前看。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14EC")

    label("loc_11A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1253")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_121F")

    ChrTalk(    #6
        0xFE,
        (
            "制作爆米花的\x01",
            "机器坏了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        "那个，那个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "一定是神说你今天\x01",
            "别卖东西了，\x01",
            "去进货吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_1250")

    label("loc_121F")


    ChrTalk(    #9
        0xFE,
        (
            "一定要向前看，\x01",
            "向前看向前看……重复重复……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1250")

    Jump("loc_14EC")

    label("loc_1253")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_1286")

    ChrTalk(    #10
        0xFE,
        (
            "咦？　奇怪……\x01",
            "机器好像有问题了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14EC")

    label("loc_1286")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1346")

    ChrTalk(    #11
        0xFE,
        (
            "我在教会倾诉了\x01",
            "自己遭遇的不幸是如何的多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "利瓦尔牧师非常\x01",
            "亲切的听了我说的话。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "他说就算遭遇挫折，\x01",
            "还是要尽可能地\x01",
            "向前看。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "好，赶快从明天\x01",
            "开始实践～\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_13A9")

    label("loc_1346")


    ChrTalk(    #15
        0xFE,
        (
            "我在七耀教会倾诉了\x01",
            "自己遭遇的不幸是如何的多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "他说就算遭遇挫折，\x01",
            "还是要尽可能地\x01",
            "向前看。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13A9")

    Jump("loc_14EC")

    label("loc_13AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_141D")

    ChrTalk(    #17
        0xFE,
        (
            "咳，今天把钓鱼用的钱\x01",
            "忘在家里了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "给客人们\x01",
            "添麻烦了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "我的人生果然\x01",
            "是要持续遇到麻烦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14EC")

    label("loc_141D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_14A2")

    ChrTalk(    #20
        0xFE,
        (
            "……我的人生从来就是\x01",
            "麻烦不断。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "诞辰庆典时也因为摊子坏了，\x01",
            "没法提高销售额。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "是不是要在七耀教会\x01",
            "除一下魔呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14EC")

    label("loc_14A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_14EC")

    ChrTalk(    #23
        0xFE,
        "哟，欢迎来到王都格兰赛尔。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "趁着休息，要不要\x01",
            "吃点爆米花？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14EC")

    TalkEnd(0xFE)
    Return()

    # Function_9_103C end

    def Function_10_14F0(): pass

    label("Function_10_14F0")

    TalkBegin(0xFE)
    Call(6, 4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_150D")
    OP_A9(0xD5)
    TalkEnd(0xFE)
    Return()

    label("loc_150D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_151E")
    TalkEnd(0xFE)
    Return()

    label("loc_151E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_1528")
    Jump("loc_1846")

    label("loc_1528")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1593")

    ChrTalk(    #25
        0xFE,
        (
            "我打算租的\x01",
            "西街区的空房\x01",
            "似乎有人住进去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "好像要开店的样子，\x01",
            "不过是个挺可疑的大叔……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1846")

    label("loc_1593")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1654")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1622")

    ChrTalk(    #27
        0xFE,
        (
            "西街区的空房似乎\x01",
            "有人先签了合同。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "虽然有点不甘心，不过那边\x01",
            "昨天好像还发生了案件……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        "看来和我无缘，算了吧。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_1651")

    label("loc_1622")


    ChrTalk(    #30
        0xFE,
        (
            "不过，那处空房……\x01",
            "到底是什么人租下了呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1651")

    Jump("loc_1846")

    label("loc_1654")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_168C")

    ChrTalk(    #31
        0xFE,
        "你们怎么东张西望的？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        "难道是在找人？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1846")

    label("loc_168C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_16DA")

    ChrTalk(    #33
        0xFE,
        (
            "以前西街区就有\x01",
            "一处空房……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "我存的钱可能\x01",
            "够把那里租下来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1846")

    label("loc_16DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1736")

    ChrTalk(    #35
        0xFE,
        (
            "我从诞辰庆典前就\x01",
            "开始存钱了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "我是不是该认真\x01",
            "考虑一下过单身生活了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1846")

    label("loc_1736")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1769")

    ChrTalk(    #37
        0xFE,
        (
            "欢迎光临。\x01",
            "要不要来份美味的薄煎饼？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1846")

    label("loc_1769")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_17E7")

    ChrTalk(    #38
        0xFE,
        (
            "刚才王国军的大人物\x01",
            "从这儿过去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "虽然穿着军服，\x01",
            "不过看起来是个很随和的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        "给人一种温柔老爸的印象。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1846")

    label("loc_17E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1846")

    ChrTalk(    #41
        0xFE,
        (
            "这里是利贝尔的中枢，\x01",
            "王都格兰赛尔。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "虽然发生过政变，\x01",
            "不过现在已经完全复原了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1846")

    TalkEnd(0xFE)
    Return()

    # Function_10_14F0 end

    def Function_11_184A(): pass

    label("Function_11_184A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_1857")
    Jump("loc_1EC0")

    label("loc_1857")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_18A4")

    ChrTalk(    #43
        0xFE,
        "……真是的，太不方便了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "晚上漆黑一片的，\x01",
            "厕所也不能上。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EC0")

    label("loc_18A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_18F3")

    ChrTalk(    #45
        0xFE,
        (
            "好像昨天亲卫队在港口\x01",
            "和巨大的坦克发生了战斗哦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        "真了不得！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1EC0")

    label("loc_18F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_197C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C9, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CA, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_193F")

    ChrTalk(    #47
        0xFE,
        (
            "那、那个……今天穿白衣服的\x01",
            "趾高气扬的女人不在吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1979")

    label("loc_193F")


    ChrTalk(    #48
        0xFE,
        "唉，就没什么有意思的事吗～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        "今天实在是太无聊了。\x02",
    )

    CloseMessageWindow()

    label("loc_1979")

    Jump("loc_1EC0")

    label("loc_197C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_1BD7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C9, 7)), scpexpr(EXPR_END)), "loc_19DB")
    TurnDirection(0x24, 0x12F, 400)

    ChrTalk(    #50
        0xFE,
        "你、你好……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x12F,
        "#260F你是谁？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        "我、我们上次不是说过话啊～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1BD4")

    label("loc_19DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B77")
    TurnDirection(0x24, 0x12F, 0)

    ChrTalk(    #53
        0xFE,
        "……嗯？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        "喂、喂，你……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        "我说穿白衣服的那个！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x12F,
        "#264F……你莫非是在说玲？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "对、对，你，\x01",
            "还没过来跟我打招呼吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x12F,
        (
            "#264F咦，玲为什么非要\x01",
            "跟你打招呼呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "来、来到这个城市的人\x01",
            "都得跟我打招呼，\x01",
            "这是规矩！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x12F,
        (
            "#267F是嘛……\x02\x03",

            "#263F不过我不愿意。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        "你、你说什么～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x12F,
        (
            "#263F因为爸爸说过绅士\x01",
            "是会先主动\x01",
            "上前打招呼的。\x02\x03",

            "#260F玲不想和不懂礼貌的\x01",
            "人交朋友。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        "唔……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1650)
    Jump("loc_1BD4")

    label("loc_1B77")

    TurnDirection(0x12F, 0xFE, 0)

    ChrTalk(    #64
        0x12F,
        "#260F (盯)……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x24, 0x12F, 400)

    ChrTalk(    #65
        0xFE,
        "什、什么嘛……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "今天就放过你吧。\x01",
            "你、你可以走了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BD4")

    Jump("loc_1EC0")

    label("loc_1BD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C1C")

    ChrTalk(    #67
        0xFE,
        "啊～我肚子饿了～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "再不回去的话\x01",
            "会被老妈揍的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EC0")

    label("loc_1C1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1C71")

    ChrTalk(    #69
        0xFE,
        "名为互不侵犯条约的良药吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "不管怎样，\x01",
            "都不像是会顺利进行的样子。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EC0")

    label("loc_1C71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_1E78")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C9, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E1B")
    TurnDirection(0x24, 0x12F, 0)

    ChrTalk(    #71
        0xFE,
        "……嗯？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        "喂、喂，你……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        "我说穿白衣服的那个！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x12F, 0x24, 400)

    ChrTalk(    #74
        0x12F,
        "#264F……你莫非是在说玲？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "对、对，你，\x01",
            "还没过来跟我打招呼吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x12F,
        (
            "#264F咦，玲为什么非要\x01",
            "跟你打招呼呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "来、来到这个城市的人\x01",
            "都得跟我打招呼，\x01",
            "这是规矩！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x12F,
        (
            "#267F是嘛……\x02\x03",

            "#263F不过我不愿意。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        "你、你说什么～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x12F,
        (
            "#263F因为爸爸说过绅士\x01",
            "是会先主动\x01",
            "上前打招呼的。\x02\x03",

            "#260F玲不想和不懂礼貌的\x01",
            "人交朋友。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        "唔……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x164F)
    Jump("loc_1E75")

    label("loc_1E1B")

    TurnDirection(0x12F, 0x24, 400)

    ChrTalk(    #82
        0x12F,
        "#260F切……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x24, 0x12F, 400)

    ChrTalk(    #83
        0xFE,
        "什、什么嘛……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "今天就放过你吧。\x01",
            "你、你可以走了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E75")

    Jump("loc_1EC0")

    label("loc_1E78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1EC0")

    ChrTalk(    #85
        0xFE,
        (
            "……真是的。\x01",
            "托伊那家伙又迟到……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        "真想早点去港口玩……\x02",
    )

    CloseMessageWindow()

    label("loc_1EC0")

    TalkEnd(0xFE)
    Return()

    # Function_11_184A end

    def Function_12_1EC4(): pass

    label("Function_12_1EC4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_1ED1")
    Jump("loc_212F")

    label("loc_1ED1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1F2C")

    ChrTalk(    #87
        0xFE,
        (
            "蒂库胆子小，平时应该是\x01",
            "不敢一个人上厕所的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        "我是在问有没有什么改变。\x02",
    )

    CloseMessageWindow()
    Jump("loc_212F")

    label("loc_1F2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1F71")

    ChrTalk(    #89
        0xFE,
        (
            "听说有几个情报部的人\x01",
            "被抓了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        "真是一件大事啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_212F")

    label("loc_1F71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1FB9")

    ChrTalk(    #91
        0xFE,
        (
            "我也喜欢这种\x01",
            "悠闲的日子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "忧虑太多的话\x01",
            "人会变老的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_212F")

    label("loc_1FB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_1FF0")

    ChrTalk(    #93
        0xFE,
        (
            "蒂库心跳加快的\x01",
            "可能性是……９６·７％。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_212F")

    label("loc_1FF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2016")

    ChrTalk(    #94
        0xFE,
        "今天该要结束了吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_212F")

    label("loc_2016")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_203F")

    ChrTalk(    #95
        0xFE,
        (
            "你们两个……\x01",
            "我有点害羞。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_212F")

    label("loc_203F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_20DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C9, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_207E")

    ChrTalk(    #96
        0xFE,
        (
            "不出我的意料，托伊\x01",
            "果然是在途中耽搁了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20D9")

    label("loc_207E")


    ChrTalk(    #97
        0xFE,
        "呼…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "蒂库一见钟情后\x01",
            "以失恋告终的概率……９９．７％。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        "……真是笨拙啊。\x02",
    )

    CloseMessageWindow()

    label("loc_20D9")

    Jump("loc_212F")

    label("loc_20DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_212F")

    ChrTalk(    #100
        0xFE,
        (
            "托伊比预计时间\x01",
            "迟到的概率……８３％。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "途中耽搁的习惯\x01",
            "还是照旧啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_212F")

    TalkEnd(0xFE)
    Return()

    # Function_12_1EC4 end

    def Function_13_2133(): pass

    label("Function_13_2133")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_2140")
    Jump("loc_2351")

    label("loc_2140")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2187")

    ChrTalk(    #102
        0xFE,
        (
            "夜晚漆黑一片的，\x01",
            "可以看见很多星星。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        "真是很漂亮啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2351")

    label("loc_2187")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_21DC")

    ChrTalk(    #104
        0xFE,
        "昨天港口那边传来了很响的声音。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "灯也突然暗了，\x01",
            "到底发生了什么呢～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2351")

    label("loc_21DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_222B")

    ChrTalk(    #106
        0xFE,
        "啊～好想吃冰淇淋啊～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "你们知道吗，\x01",
            "东街区的冰淇淋很好吃哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2351")

    label("loc_222B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_2271")

    ChrTalk(    #108
        0xFE,
        (
            "蒂库虽然平时\x01",
            "趾高气扬的，不过跟女孩子\x01",
            "说话时就会紧张。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2351")

    label("loc_2271")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_229E")

    ChrTalk(    #109
        0xFE,
        (
            "肚子饿了啊～\x01",
            "我得回去了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2351")

    label("loc_229E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_22CD")

    ChrTalk(    #110
        0xFE,
        (
            "我可不想吃药，\x01",
            "想吃好吃的东西。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2351")

    label("loc_22CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_22FC")

    ChrTalk(    #111
        0xFE,
        (
            "嘿嘿……\x01",
            "又比约定的时间晚点了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2351")

    label("loc_22FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_2351")

    ChrTalk(    #112
        0xFE,
        (
            "哇～\x01",
            "好香啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "……咦？\x01",
            "我有没有跟什么人有约？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        "唔～让我想想……\x02",
    )

    CloseMessageWindow()

    label("loc_2351")

    TalkEnd(0xFE)
    Return()

    # Function_13_2133 end

    def Function_14_2355(): pass

    label("Function_14_2355")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_2362")
    Jump("loc_2B2D")

    label("loc_2362")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2402")

    ChrTalk(    #115
        0xFE,
        (
            "在工房当修理师的\x01",
            "多姆确实是个可信赖的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "如果他说这不是故障，\x01",
            "那应该是没问题的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "如果是塞森说的，\x01",
            "我倒是会怀疑他\x01",
            "是不是想买新的了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B2D")

    label("loc_2402")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_249A")

    ChrTalk(    #118
        0xFE,
        (
            "原情报部的凯诺娜上尉\x01",
            "是不是真的举兵谋反了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "港湾设施好像被导力坦克\x01",
            "破坏得一塌糊涂了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        "希望没有对互不侵犯条约产生太大的影响。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B2D")

    label("loc_249A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_25B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2571")

    ChrTalk(    #121
        0xFE,
        "杜南公爵和科洛蒂娅公主……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "艾莉茜雅女王准备\x01",
            "传位给哪一个呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "我个人觉得科洛蒂娅\x01",
            "公主比较好……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "其实我不太了解\x01",
            "科洛蒂娅公主。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_256B")

    ChrTalk(    #125
        0x105,
        "#042F………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_256B")

    OP_A2(0x3)
    Jump("loc_25B3")

    label("loc_2571")


    ChrTalk(    #126
        0xFE,
        (
            "其实我不太了解\x01",
            "科洛蒂娅公主。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        (
            "差不多只知道\x01",
            "她是个美人。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25B3")

    Jump("loc_2B2D")

    label("loc_25B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_2685")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_263A")

    ChrTalk(    #128
        0xFE,
        (
            "有不少市民希望\x01",
            "理查德上校复职呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "这也说明他的\x01",
            "言行是有足够魅力的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        (
            "说起来我有点\x01",
            "寂寞的心情呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_2682")

    label("loc_263A")


    ChrTalk(    #131
        0xFE,
        (
            "有不少市民希望\x01",
            "理查德上校复职呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "说起来我有点\x01",
            "寂寞的心情呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2682")

    Jump("loc_2B2D")

    label("loc_2685")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_26F3")

    ChrTalk(    #133
        0xFE,
        (
            "西街区的利贝尔通讯社\x01",
            "总是亮着灯哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        "一定很忙吧……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "市民都称呼西街区\x01",
            "为不夜城的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B2D")

    label("loc_26F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_288C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27E0")

    ChrTalk(    #136
        0xFE,
        (
            "你们要问路就问我\x01",
            "这个地道的格兰赛尔人吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "共和国大使馆在东街区的南侧，\x01",
            "帝国大使馆在东街区的北侧哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        (
            "女王住的格兰赛尔城\x01",
            "在北街区的最北头。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        (
            "利贝尔通讯社在西街区的南侧，\x01",
            "在狭窄的胡同里，可别看漏了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_2889")

    label("loc_27E0")


    ChrTalk(    #140
        0xFE,
        (
            "共和国大使馆在东街区的南侧，\x01",
            "帝国大使馆在东街区的北侧哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        (
            "女王住的格兰赛尔城\x01",
            "在北街区的最北头。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        (
            "利贝尔通讯社在西街区的南侧，\x01",
            "在狭窄的胡同里，可别看漏了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2889")

    Jump("loc_2B2D")

    label("loc_288C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_2988")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2925")

    ChrTalk(    #143
        0xFE,
        (
            "在格兰赛尔设有\x01",
            "下水道。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        (
            "在街上的很多地方\x01",
            "都有管理用的入口，\x01",
            "可以从那里进去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        (
            "听说里面全是魔兽，\x01",
            "还是不要进去为好啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_2985")

    label("loc_2925")


    ChrTalk(    #146
        0xFE,
        (
            "下水道里净是魔兽，\x01",
            "还是不要进去为好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        (
            "也只有承办了剿灭魔兽任务的\x01",
            "游击士才有资格进去。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2985")

    Jump("loc_2B2D")

    label("loc_2988")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_2B2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2ADD")

    ChrTalk(    #148
        0xFE,
        (
            "南街区这边有协会\x01",
            "和种种店铺鳞次栉比。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        (
            "北街区有王国最大的宾馆。\x01",
            "再往北就是格兰赛尔城了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xFE,
        (
            "西街区以大圣堂\x01",
            "和利贝尔通讯社\x01",
            "而为人们所知。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        (
            "而东街区\x01",
            "则林立着各国大使馆、格兰竞技场\x01",
            "和百货商店。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        "对了对了，我忘了一件要紧事！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        (
            "西街区的对面\x01",
            "有港口和仓库街。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xFE,
        (
            "就是发生政变时\x01",
            "被封锁而无法进入的地方。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_2B2D")

    label("loc_2ADD")


    ChrTalk(    #155
        0xFE,
        (
            "西街区的对面\x01",
            "有港口和仓库街。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xFE,
        (
            "就是发生政变时\x01",
            "被封锁而无法进入的地方。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B2D")

    TalkEnd(0xFE)
    Return()

    # Function_14_2355 end

    def Function_15_2B31(): pass

    label("Function_15_2B31")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_2B3E")
    Jump("loc_300F")

    label("loc_2B3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2B96")

    ChrTalk(    #157
        0xFE,
        (
            "啊，想不到阳光是\x01",
            "这么明亮和温暖……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xFE,
        (
            "夜晚又暗又冷，\x01",
            "令人越发不安啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_300F")

    label("loc_2B96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_2C2A")

    ChrTalk(    #159
        0xFE,
        (
            "理查德上校的副官\x01",
            "好像再次谋划了叛变。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xFE,
        (
            "我就觉得那张狐狸脸\x01",
            "肯定没打什么好主意……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        (
            "但是我能理解\x01",
            "她拼命想要帮助\x01",
            "上校的心情……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_300F")

    label("loc_2C2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_2C66")

    ChrTalk(    #162
        0xFE,
        "……穿白衣服的女孩子？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xFE,
        "抱歉，我没看见。\x02",
    )

    CloseMessageWindow()
    Jump("loc_300F")

    label("loc_2C66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_2D08")

    ChrTalk(    #164
        0xFE,
        "刚才我看见杜南公爵了哦！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        (
            "虽然我怀疑自己是不是看错了，\x01",
            "不过他那个发型不可能认错吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xFE,
        (
            "我听说他在离宫诚惶诚恐地过日子，\x01",
            "不过看来是回来了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_300F")

    label("loc_2D08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D74")

    ChrTalk(    #167
        0xFE,
        (
            "我相信理查德上校\x01",
            "是有苦衷的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        (
            "不过我完全无法\x01",
            "原谅杜南公爵。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0xFE,
        "你不这么认为吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_300F")

    label("loc_2D74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_2DC9")

    ChrTalk(    #170
        0xFE,
        "帝国大使和共和国大使……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xFE,
        (
            "两个人我都见过，\x01",
            "都各自有着不好的毛病。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_300F")

    label("loc_2DC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_2EC8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E6F")

    ChrTalk(    #172
        0xFE,
        (
            "条约的签字仪式近了，\x01",
            "王国军好像要对街道进行警戒。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xFE,
        (
            "……理查德上校现在\x01",
            "在哪里？又在干吗呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xFE,
        (
            "我现在仍然相信上校的\x01",
            "政变是事出有因的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_2EC5")

    label("loc_2E6F")


    ChrTalk(    #175
        0xFE,
        (
            "理查德上校现在\x01",
            "在哪里？又在干吗呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xFE,
        (
            "我现在仍然相信上校的\x01",
            "政变是事出有因的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EC5")

    Jump("loc_300F")

    label("loc_2EC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_300F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FA7")

    ChrTalk(    #177
        0xFE,
        (
            "想去艾尔贝离宫的话就从那边的\x01",
            "正门出去，然后从庭园大道往南走。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xFE,
        (
            "走到有指示牌的三叉路后\x01",
            "向格鲁纳门方向前进。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xFE,
        (
            "再一次到三叉路时\x01",
            "向南走就是艾尔贝离宫了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xFE,
        (
            "好好看指示牌的话\x01",
            "应该不会迷路的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_300F")

    label("loc_2FA7")


    ChrTalk(    #181
        0xFE,
        (
            "想去艾尔贝离宫的话就从那里的\x01",
            "正门出去，然后从庭园大道往南走。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0xFE,
        (
            "道旁有指示牌，\x01",
            "应该不会迷路的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_300F")

    TalkEnd(0xFE)
    Return()

    # Function_15_2B31 end

    def Function_16_3013(): pass

    label("Function_16_3013")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_3020")
    Jump("loc_33BB")

    label("loc_3020")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3093")

    ChrTalk(    #183
        0xFE,
        (
            "年轻人因为从小\x01",
            "生活在导力器环境下，\x01",
            "好像很惊慌呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0xFE,
        (
            "不过，那里的钓公师团的\x01",
            "家伙们好像很镇定呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33BB")

    label("loc_3093")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_3101")

    ChrTalk(    #185
        0xFE,
        (
            "理查德上校的部下们\x01",
            "好像发动了叛乱。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xFE,
        (
            "在女王脚下惹麻烦，真是一帮\x01",
            "直到最后也不太平的家伙……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33BB")

    label("loc_3101")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_315B")

    ChrTalk(    #187
        0xFE,
        (
            "好像卢安市长选举的\x01",
            "结果出来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xFE,
        (
            "过一会儿去买利贝尔通讯的\x01",
            "最新一期吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33BB")

    label("loc_315B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_3206")

    ChrTalk(    #189
        0xFE,
        (
            "互不侵犯条约本身\x01",
            "虽然大家心里都想……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0xFE,
        (
            "不过真正能付诸实施的也只有\x01",
            "像艾莉茜雅女王这样的人了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xFE,
        (
            "女王是利贝尔国民的骄傲……\x01",
            "那个理查德被抓真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33BB")

    label("loc_3206")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3258")

    ChrTalk(    #192
        0xFE,
        (
            "我早晨和傍晚\x01",
            "必定出来散步。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xFE,
        (
            "每天的散步\x01",
            "正是我健康的秘诀。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33BB")

    label("loc_3258")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_32AE")

    ChrTalk(    #194
        0xFE,
        (
            "听说艾莉茜雅女王得病的时候\x01",
            "我还真吓了一跳。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0xFE,
        (
            "理查德上校\x01",
            "真是无礼。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33BB")

    label("loc_32AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_3358")

    ChrTalk(    #196
        0xFE,
        (
            "前不久在王城前看到了\x01",
            "传说中的卡西乌斯准将。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xFE,
        (
            "虽然比摩尔根将军年轻，\x01",
            "不过我觉得他是一个\x01",
            "稳重、有威严的人物。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0xFE,
        (
            "可为什么百日战役的\x01",
            "英雄去当游击士了？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33BB")

    label("loc_3358")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_33BB")

    ChrTalk(    #199
        0xFE,
        (
            "前一阵子在那边的酒馆\x01",
            "里有个钢琴家,\x01",
            "演奏很了不起。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0xFE,
        (
            "虽然人怪怪的，\x01",
            "不过是真有水平。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33BB")

    TalkEnd(0xFE)
    Return()

    # Function_16_3013 end

    def Function_17_33BF(): pass

    label("Function_17_33BF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_33CC")
    Jump("loc_3538")

    label("loc_33CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3418")

    ChrTalk(    #201
        0xFE,
        (
            "王都总算是\x01",
            "恢复平静了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0xFE,
        (
            "这也是拜女王陛下\x01",
            "发布公告所赐。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3538")

    label("loc_3418")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_3449")

    ChrTalk(    #203
        0xFE,
        (
            "想不到凯诺娜上尉\x01",
            "会潜伏在王都……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3538")

    label("loc_3449")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_34C2")

    ChrTalk(    #204
        0xFE,
        (
            "王国军里也有很多\x01",
            "支持理查德的家伙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0xFE,
        (
            "但他犯了决\x01",
            "不能犯的错误。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0xFE,
        (
            "触犯军规的军人\x01",
            "受到处罚是当然的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3538")

    label("loc_34C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_350F")

    ChrTalk(    #207
        0xFE,
        "签字仪式的日子近了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0xFE,
        (
            "在希德中校的指挥下\x01",
            "王都将进行警戒。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3538")

    label("loc_350F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_351D")
    Jump("loc_3538")

    label("loc_351D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_3527")
    Jump("loc_3538")

    label("loc_3527")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_3531")
    Jump("loc_3538")

    label("loc_3531")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_3538")

    label("loc_3538")

    TalkEnd(0xFE)
    Return()

    # Function_17_33BF end

    def Function_18_353C(): pass

    label("Function_18_353C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_3549")
    Jump("loc_3724")

    label("loc_3549")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_358F")

    ChrTalk(    #209
        0xFE,
        (
            "虽然这么做，\x01",
            "不过到关键时刻不能开枪\x01",
            "还是令人不安啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3724")

    label("loc_358F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_3654")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3612")

    ChrTalk(    #210
        0xFE,
        (
            "王国军全力搜索过了，\x01",
            "不过还是没找到巨大机器人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0xFE,
        (
            "那种东西竟然也出现了，\x01",
            "利贝尔接下来会变得怎样呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_3651")

    label("loc_3612")


    ChrTalk(    #212
        0xFE,
        (
            "不，王国军\x01",
            "有那位卡西乌斯准将在……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0xFE,
        "他一定有办法的。\x02",
    )

    CloseMessageWindow()

    label("loc_3651")

    Jump("loc_3724")

    label("loc_3654")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_3697")

    ChrTalk(    #214
        0xFE,
        "没有异常！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0xFE,
        (
            "希望签字仪式之前\x01",
            "什么也不要发生……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3724")

    label("loc_3697")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_36FB")

    ChrTalk(    #216
        0xFE,
        (
            "如果你们看见可疑的人\x01",
            "请一定要毫不犹豫地举报。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xFE,
        (
            "因为有可能有人\x01",
            "欲图干扰签字仪式。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3724")

    label("loc_36FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3709")
    Jump("loc_3724")

    label("loc_3709")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_3713")
    Jump("loc_3724")

    label("loc_3713")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_371D")
    Jump("loc_3724")

    label("loc_371D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_3724")

    label("loc_3724")

    TalkEnd(0xFE)
    Return()

    # Function_18_353C end

    def Function_19_3728(): pass

    label("Function_19_3728")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_3735")
    Jump("loc_38E4")

    label("loc_3735")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3781")

    ChrTalk(    #218
        0xFE,
        (
            "有没有办法让\x01",
            "导力炉能用呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0xFE,
        (
            "没有炉子的话\x01",
            "做菜很麻烦……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38E4")

    label("loc_3781")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_37AC")

    ChrTalk(    #220
        0xFE,
        (
            "情报部一定想\x01",
            "妨碍签字仪式。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38E4")

    label("loc_37AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_37D0")

    ChrTalk(    #221
        0xFE,
        "士兵们也真不容易啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_38E4")

    label("loc_37D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_37FA")

    ChrTalk(    #222
        0xFE,
        "好，今天一整天也要努力了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_38E4")

    label("loc_37FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3820")

    ChrTalk(    #223
        0xFE,
        "得回去准备晚饭了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_38E4")

    label("loc_3820")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_3878")

    ChrTalk(    #224
        0xFE,
        (
            "（哈欠）……我要不要\x01",
            "回家去睡个午觉呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0xFE,
        (
            "为什么吃了午饭\x01",
            "就犯困了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38E4")

    label("loc_3878")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_389F")

    ChrTalk(    #226
        0xFE,
        (
            "今天的天气\x01",
            "也很爽朗呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38E4")

    label("loc_389F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_38E4")

    ChrTalk(    #227
        0xFE,
        (
            "你好。\x01",
            "今天也是个好天气。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0xFE,
        (
            "天气好的话\x01",
            "心情也会开朗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38E4")

    TalkEnd(0xFE)
    Return()

    # Function_19_3728 end

    def Function_20_38E8(): pass

    label("Function_20_38E8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_38F5")
    Jump("loc_3A81")

    label("loc_38F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3940")

    ChrTalk(    #229
        0xFE,
        (
            "那个飞天贝壳\x01",
            "好像从港口也能看见哦\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0xFE,
        "要不要现在就去看看？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A81")

    label("loc_3940")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_3987")

    ChrTalk(    #231
        0xFE,
        "不、不好了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0xFE,
        (
            "听说昨天情报部和特务兵\x01",
            "出现在港口了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A81")

    label("loc_3987")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_39B4")

    ChrTalk(    #233
        0xFE,
        (
            "卢安的市长\x01",
            "好像已经确定了吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A81")

    label("loc_39B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_39EF")

    ChrTalk(    #234
        0xFE,
        (
            "今天天气也不错，\x01",
            "要不要去艾尔贝离宫看看呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A81")

    label("loc_39EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3A28")

    ChrTalk(    #235
        0xFE,
        (
            "到底是吃鱼还是吃肉，\x01",
            "这可是个问题……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A81")

    label("loc_3A28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_3A46")

    ChrTalk(    #236
        0xFE,
        "晚饭吃什么呢？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A81")

    label("loc_3A46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_3A64")

    ChrTalk(    #237
        0xFE,
        "今天去哪儿呢？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A81")

    label("loc_3A64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_3A81")

    ChrTalk(    #238
        0xFE,
        "唔～快饿死了……\x02",
    )

    CloseMessageWindow()

    label("loc_3A81")

    TalkEnd(0xFE)
    Return()

    # Function_20_38E8 end

    def Function_21_3A85(): pass

    label("Function_21_3A85")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_3A92")
    Jump("loc_3C5B")

    label("loc_3A92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3ABB")

    ChrTalk(    #239
        0xFE,
        (
            "唔～现在实在\x01",
            "没那种心情。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C5B")

    label("loc_3ABB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_3B09")

    ChrTalk(    #240
        0xFE,
        (
            "特务兵就是\x01",
            "情报部的实战部队哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0xFE,
        (
            "明白？\x01",
            "就是说是一回事儿。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C5B")

    label("loc_3B09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_3B38")

    ChrTalk(    #242
        0xFE,
        (
            "……他总是有点微秒的\x01",
            "愣头愣脑。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C5B")

    label("loc_3B38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_3B6B")

    ChrTalk(    #243
        0xFE,
        (
            "……不知道吗？\x01",
            "离宫现在禁止进入哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C5B")

    label("loc_3B6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3BAE")

    ChrTalk(    #244
        0xFE,
        (
            "你一天中有半天的时间\x01",
            "都在为吃饭的事情而烦恼吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C5B")

    label("loc_3BAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_3BF9")

    ChrTalk(    #245
        0xFE,
        "你不是刚吃了午饭吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0xFE,
        (
            "肚子饱饱的，\x01",
            "现在什么都不想考虑。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C5B")

    label("loc_3BF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_3C37")

    ChrTalk(    #247
        0xFE,
        (
            "不一定非要\x01",
            "去什么地方啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0xFE,
        (
            "难得\x01",
            "悠闲一下。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C5B")

    label("loc_3C37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_3C5B")

    ChrTalk(    #249
        0xFE,
        (
            "呵呵，那么\x01",
            "赶紧吃饭吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C5B")

    TalkEnd(0xFE)
    Return()

    # Function_21_3A85 end

    def Function_22_3C5F(): pass

    label("Function_22_3C5F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_3C6C")
    Jump("loc_3EC3")

    label("loc_3C6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3CCA")

    ChrTalk(    #250
        0xFE,
        (
            "完全看不到\x01",
            "游客的影子了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0xFE,
        (
            "虽然这也是没办法的事，\x01",
            "不过还是令人感到萧瑟。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EC3")

    label("loc_3CCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_3D3A")

    ChrTalk(    #252
        0xFE,
        (
            "昨晚在西街区好像有\x01",
            "一阵子不能使用导力器了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0xFE,
        (
            "没关系，只要让多姆调查\x01",
            "一下马上就能知道原因啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EC3")

    label("loc_3D3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_3D73")

    ChrTalk(    #254
        0xFE,
        (
            "工房的塞森\x01",
            "确实有一套。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0xFE,
        "可是…………\x02",
    )

    CloseMessageWindow()
    Jump("loc_3EC3")

    label("loc_3D73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_3DC1")

    ChrTalk(    #256
        0xFE,
        (
            "昨晚到很晚工房的\x01",
            "３楼都有灯光。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0xFE,
        (
            "一定是多姆\x01",
            "在通宵修理吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EC3")

    label("loc_3DC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3DF2")

    ChrTalk(    #258
        0xFE,
        (
            "那就定在日落之前\x01",
            "回家好不好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EC3")

    label("loc_3DF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_3E46")

    ChrTalk(    #259
        0xFE,
        (
            "工房的多姆好像和\x01",
            "老板塞森大吵了一架。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0xFE,
        (
            "他们以前就\x01",
            "相处得不好……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EC3")

    label("loc_3E46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_3E95")

    ChrTalk(    #261
        0xFE,
        (
            "工房的多姆,本事\x01",
            "确实是一流的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0xFE,
        (
            "好像就没有\x01",
            "他不会修的东西。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EC3")

    label("loc_3E95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_3EC3")

    ChrTalk(    #263
        0xFE,
        (
            "这座城市的工房\x01",
            "有个亲切的修理师。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EC3")

    TalkEnd(0xFE)
    Return()

    # Function_22_3C5F end

    def Function_23_3EC7(): pass

    label("Function_23_3EC7")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3EE2")
    Call(0, 49)
    Call(0, 50)
    AddParty(0x2E, 0xFF, 0xFF)

    label("loc_3EE2")

    SetChrPos(0x101, 1530, 0, -62500, 180)
    SetChrPos(0x12F, 150, 0, -63240, 90)
    SetChrPos(0xF7, 2900, 0, -63290, 270)
    SetChrPos(0xF8, 2150, 0, -64519, 0)
    SetChrPos(0xF9, 1100, 0, -64430, 0)
    OP_6D(1530, 0, -62500, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(31000, 0)
    OP_6E(262, 0)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #264
        0x101,
        (
            "#1006F#5P好了……\x01",
            "我们赶快回协会吧。\x02\x03",

            "关于玲的事\x01",
            "必须和艾南先生商量一下。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4052")

    ChrTalk(    #265
        0x106,
        (
            "#552F这是不错，不过军队的\x01",
            "负责人也快要来了。\x02\x03",

            "你没忘记吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0x101,
        "#1004F#5P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0x106,
        "#053F真是的，拿你没办法。\x02",
    )

    CloseMessageWindow()
    Jump("loc_40C6")

    label("loc_4052")


    ChrTalk(    #268
        0x103,
        (
            "#027F这是不错，不过军队的\x01",
            "负责人也快要来了。\x02\x03",

            "你不会忘了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0x101,
        "#1004F#5P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0x103,
        "#025F呼，真拿你没办法。\x02",
    )

    CloseMessageWindow()

    label("loc_40C6")


    ChrTalk(    #271
        0x12F,
        (
            "#264F#6P咦？怎么了？\x02\x03",

            "记得你们是要把玲\x01",
            "带去那个什么协会吧？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4201")

    ChrTalk(    #272
        0x104,
        (
            "#031F呵呵，小小姐。\x01",
            "请赐我您的手。\x02\x03",

            "就让这个不肖的\x01",
            "奥利维尔来护送您吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0x12F,
        (
            "#263F#6P你的好意我心领了。\x02\x03",

            "玲希望姐姐\x01",
            "来带路。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0x104,
        "#036F唔。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 231, 400)

    ChrTalk(    #275
        0x101,
        (
            "#1016F#5P啊哈哈……\x01",
            "抱歉，奥利维尔。\x02\x03",

            "#1006F那么小玲，\x01",
            "我们去游击士协会吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4246")

    label("loc_4201")

    OP_8C(0x101, 231, 400)

    ChrTalk(    #276
        0x101,
        (
            "#1006F#5P啊，嗯，当然。\x02\x03",

            "那么小玲。\x01",
            "我们去游击士协会吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4246")


    ChrTalk(    #277
        0x12F,
        "#261F#6P嗯，拜托了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1619)
    EventEnd(0x0)
    Return()

    # Function_23_3EC7 end

    def Function_24_4266(): pass

    label("Function_24_4266")

    EventBegin(0x0)
    OP_4A(0x28, 255)
    OP_4A(0x29, 255)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x4, 0xFF)
    RemoveParty(0x6, 0xFF)
    RemoveParty(0x7, 0xFF)
    RemoveParty(0x2E, 0xFF)
    AddParty(0x4, 0xF7, 0xFF)
    AddParty(0x3, 0xF8, 0xFF)
    AddParty(0x7, 0xF9, 0xFF)
    SetChrPos(0x101, 5050, 0, -11050, 180)
    SetChrPos(0x108, 6200, 0, -12130, 270)
    SetChrPos(0x104, 4000, 0, -12230, 90)
    SetChrPos(0x105, 5130, 0, -13310, 360)
    OP_6D(5100, 0, -12050, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(32000, 0)
    OP_6E(262, 0)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #278
        0x101,
        (
            "#1011F#5P那么……\x01",
            "开始打听情况吧？\x02\x03",

            "嗯……从哪儿开始呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0x108,
        (
            "#070F算了，从哪儿开始都一样。\x02\x03",

            "如果是卡尔瓦德大使馆的话\x01",
            "我是可以自由出入的。\x02\x03",

            "我应该能马上\x01",
            "把你们介绍给大使的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0x104,
        (
            "#030F#6P我就负责埃雷波尼亚大使馆了。\x02\x03",

            "只要跟门卫士兵传达，\x01",
            "他们会郑重地领我们进去的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0x105,
        (
            "#040F有我在的话可以\x01",
            "直接进入格兰赛尔城。\x02\x03",

            "可能和祖母商量一下\x01",
            "是最好的了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0x101,
        (
            "#1006F#5P利贝尔通讯社\x01",
            "也没什么问题……\x02\x03",

            "好，我们就\x01",
            "一个个地来吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x8A, 0x4, 0x2)
    OP_28(0x8A, 0x4, 0x8)
    OP_28(0x8A, 0x1, 0x1)
    OP_28(0x8A, 0x1, 0x2)
    OP_28(0x8B, 0x4, 0x2)
    OP_28(0x8B, 0x4, 0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_44F0")
    OP_28(0x8B, 0x1, 0x2)
    Jump("loc_44FD")

    label("loc_44F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_44FD")
    OP_28(0x8B, 0x1, 0x1)

    label("loc_44FD")

    OP_28(0x8B, 0x1, 0x4)
    OP_28(0x8B, 0x1, 0x8)
    OP_28(0x8B, 0x1, 0x20)
    OP_28(0x8B, 0x1, 0x80)
    OP_28(0x8B, 0x1, 0x1000)
    EventEnd(0x0)
    OP_4B(0x28, 255)
    OP_4B(0x29, 255)
    Return()

    # Function_24_4266 end

    def Function_25_4526(): pass

    label("Function_25_4526")

    EventBegin(0x0)
    OP_4A(0x28, 255)
    OP_4A(0x29, 255)
    OP_4A(0x2A, 255)
    OP_4A(0x2B, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_454D")
    Call(0, 49)
    Call(0, 51)

    label("loc_454D")

    SetChrFlags(0x101, 0x80)
    SetChrFlags(0xF7, 0x80)
    SetChrFlags(0x107, 0x80)
    SetChrFlags(0xF9, 0x80)
    OP_6D(9240, 410, -13010, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1500, 0)
    OP_0D()
    OP_6F(0x1, 0)
    OP_70(0x1, 0x3B)
    OP_73(0x1)
    Sleep(500)
    OP_43(0x101, 0x1, 0x0, 0x1A)
    Sleep(800)
    OP_43(0xF7, 0x1, 0x0, 0x1B)
    Sleep(800)
    OP_43(0x107, 0x1, 0x0, 0x1C)
    Sleep(800)
    OP_43(0xF9, 0x1, 0x0, 0x1D)
    Sleep(2000)

    def lambda_45F4():
        OP_6D(4550, 0, -13010, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_45F4)
    OP_6C(32000, 3000)
    WaitChrThread(0xF9, 0x1)

    ChrTalk(    #283
        0x101,
        (
            "#1011F#6P那么……\x01",
            "关于那孩子去的地方，\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)
    Sleep(500)

    ChrTalk(    #284
        0x101,
        "#1006F#5P提妲，你有什么线索吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0x107,
        (
            "#561F嗯……\x02\x03",

            "#060F我们昨天在东街区\x01",
            "逛了很多地方……\x02\x03",

            "她有可能在其中的某个地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0x101,
        "#1004F#5P逛了很多地方？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0x107,
        (
            "#560F嗯，首先是在\x01",
            "百货商店买东西……\x02\x03",

            "然后去了历史资料馆……\x02\x03",

            "#061F最后在时钟台附近\x01",
            "吃了冰淇淋。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0x101,
        (
            "#1016F#5P原来如此，是不少。\x02\x03",

            "#1006F提妲你也挺\x01",
            "悠然自得的呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0x107,
        "#067F嘿嘿嘿……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_47D3")

    ChrTalk(    #290
        0x108,
        (
            "#070F首先调查一下\x01",
            "那一带吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47F5")

    label("loc_47D3")


    ChrTalk(    #291
        0x105,
        (
            "#048F首先调查一下\x01",
            "那一带吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4822")

    ChrTalk(    #292
        0x106,
        (
            "#051F#5P嗯。\x01",
            "赶紧把她领回来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_483F")

    label("loc_4822")


    ChrTalk(    #293
        0x103,
        (
            "#020F#5P嗯。\x01",
            "去看看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_483F")

    OP_28(0x8C, 0x4, 0x2)
    OP_28(0x8C, 0x4, 0x8)
    OP_28(0x8C, 0x1, 0x1)
    EventEnd(0x0)
    OP_4B(0x28, 255)
    OP_4B(0x29, 255)
    OP_4B(0x2A, 255)
    OP_4B(0x2B, 255)
    Return()

    # Function_25_4526 end

    def Function_26_4862(): pass

    label("Function_26_4862")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 11480, 750, -13010, 270)
    OP_8E(0xFE, 0xDDE, 0x0, 0xFFFFCD2E, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_26_4862 end

    def Function_27_4894(): pass

    label("Function_27_4894")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 11480, 750, -13010, 270)
    OP_8E(0xFE, 0x10F4, 0x0, 0xFFFFD0E4, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_27_4894 end

    def Function_28_48C6(): pass

    label("Function_28_48C6")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 11480, 750, -13010, 270)
    OP_8E(0xFE, 0x114E, 0x0, 0xFFFFC978, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_28_48C6 end

    def Function_29_48F8(): pass

    label("Function_29_48F8")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 11480, 750, -13010, 270)
    OP_8E(0xFE, 0x2418, 0x19A, 0xFFFFCD2E, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    OP_6F(0x1, 59)
    OP_70(0x1, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    OP_73(0x1)
    Sleep(500)
    OP_8C(0xFE, 270, 400)
    OP_8E(0xFE, 0x14A0, 0x0, 0xFFFFCD2E, 0x7D0, 0x0)
    Return()

    # Function_29_48F8 end

    def Function_30_4963(): pass

    label("Function_30_4963")

    EventBegin(0x0)
    NewScene("ED6_DT21/T4150   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_30_4963 end

    def Function_31_496F(): pass

    label("Function_31_496F")

    EventBegin(0x0)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x29, 0x80)
    SetChrFlags(0x2A, 0x80)
    SetChrFlags(0x2B, 0x80)
    SetChrFlags(0x2F, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_49C6")
    Call(0, 49)
    Call(0, 51)
    FadeToBright(0, 0)

    label("loc_49C6")

    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0xF7, 4670, 0, -3450, 180)
    SetChrPos(0x8, 3420, 0, -3270, 180)
    SetChrPos(0xF9, 4650, 0, -1250, 180)
    SetChrPos(0x107, 3640, 0, -1760, 180)
    SetChrPos(0x101, 4890, 0, 8950, 180)
    SetChrPos(0x9, 3730, 0, 10070, 180)
    OP_6D(5110, 0, 330, 0)
    OP_67(0, 7760, -10000, 0)
    OP_6B(2410, 0)
    OP_6C(45000, 0)
    OP_6E(320, 0)
    OP_43(0xF7, 0x1, 0x0, 0x21)
    OP_43(0x8, 0x1, 0x0, 0x22)
    OP_43(0xF9, 0x1, 0x0, 0x23)
    OP_43(0x107, 0x1, 0x0, 0x24)
    OP_43(0x101, 0x1, 0x0, 0x25)
    OP_43(0x9, 0x1, 0x0, 0x26)

    def lambda_4AA3():
        OP_6D(8590, 250, -13060, 8000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4AA3)
    FadeToBright(2000, 0)
    WaitChrThread(0xF7, 0x1)
    OP_72(0x1, 0x10)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x3B)
    OP_73(0x1)
    OP_43(0xF7, 0x1, 0x0, 0x20)
    Sleep(300)
    OP_43(0x8, 0x1, 0x0, 0x20)
    Sleep(300)
    OP_43(0xF9, 0x1, 0x0, 0x20)
    Sleep(300)
    OP_43(0x107, 0x1, 0x0, 0x20)
    WaitChrThread(0x107, 0x1)
    Sleep(300)
    OP_6F(0x1, 59)
    OP_70(0x1, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)

    def lambda_4B2A():
        OP_8E(0xFE, 0x2544, 0x1F4, 0xFFFFCCCA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4B2A)

    def lambda_4B45():
        OP_8E(0xFE, 0x1B4E, 0xFA, 0xFFFFCC98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4B45)
    WaitChrThread(0x9, 0x1)
    OP_8C(0x9, 90, 0)

    ChrTalk(    #294
        0x9,
        "#267F#6P我说，艾丝蒂尔……\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x101, 270, 400)
    OP_8E(0x101, 0x218E, 0xFA, 0xFFFFCCFC, 0x7D0, 0x0)

    ChrTalk(    #295
        0x101,
        (
            "#1006F#2P嗯？怎么了？\x02\x03",

            "我已经不生气了，\x01",
            "你可以放心了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0x9,
        (
            "#261F#6P呵呵，不是的。\x02\x03",

            "#265F首先，就算艾丝蒂尔生气\x01",
            "也一点都不可怕。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0x101,
        (
            "#1019F#2P唔……你这小鬼。\x02\x03",

            "#1015F那么是怎么了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0x9,
        (
            "#267F#6P我说啊……\x02\x03",

            "其实我有东西\x01",
            "要交给艾丝蒂尔。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0x101,
        "#1004F#2P东西？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0x9,
        (
            "#267F#6P嗯。\x01",
            "你可别吓一跳哦？\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0xBB8)
    OP_8F(0x9, 0x1F0E, 0xFA, 0xFFFFCCDE, 0x7D0, 0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #301
        "\x07\x05玲给了艾丝蒂尔一封信。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_8F(0x9, 0x1B4E, 0xFA, 0xFFFFCC98, 0x7D0, 0x0)

    ChrTalk(    #302
        0x101,
        (
            "#1004F咦#2P……？\x02\x03",

            "这是什么？给我的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #303
        0x9,
        "#260F#6P嗯，是啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #304
        0x101,
        "#1015F#2P谁给你的？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0x9,
        (
            "#263F#6P呵呵，你读过\x01",
            "就明白了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0x101,
        "#1011F#2P是、是吗？\x02",
    )

    CloseMessageWindow()
    OP_D2(0x260246, 0x26024B, 0x16)
    Sleep(200)
    Fade(250)
    SetChrChipByIndex(0x101, 22)
    SetChrSubChip(0x101, 0)
    OP_0D()
    Sleep(200)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #307
        "\x07\x05艾丝蒂尔拆开了信封。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_AD(0x240097, 0xBE, 0x64, 0x1F4)
    Sleep(1000)
    SetChrName("")
    SetMessageWindowPos(-1, 300, -1, 3)

    AnonymousTalk(    #308
        (
            "\x07\x05致艾丝蒂尔。\x02\x03",

            "我迷惑了很久，\x01",
            "不过还是有话必须\x01",
            "要跟你说。\x02\x03",

            "像那样离开了你，\x01",
            "我这种要求可能是太过分了。\x01",
            "不过能不能让我们单独见面？\x02\x03",

            "今天傍晚我在格鲁纳门一侧的\x01",
            "亚宁堡上等你。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_AE(0x1F4)
    Sleep(1500)
    Sleep(500)

    ChrTalk(    #309
        0x101,
        (
            "#1004F#2P………………………\x01",
            "…………啊………………\x02",
        )
    )

    CloseMessageWindow()
    OP_1D(0x5B)
    Sleep(500)

    ChrTalk(    #310
        0x9,
        (
            "#265F#6P呵呵，看来你明白了。\x02\x03",

            "玲也是听了你的话\x01",
            "以后才恍然大悟的⊙\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)

    ChrTalk(    #311
        0x101,
        (
            "#1020F#2P这、这是……\x02\x03",

            "谁给你的！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #312
        0x9,
        (
            "#260F#6P一个黑发、琥珀色\x01",
            "眼睛的帅哥哥给我的。\x02\x03",

            "我在空港的等候厅等\x01",
            "艾丝蒂尔你们的时候，\x01",
            "他让我把这个交给你。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #313
        0x101,
        "#1025F#2P……啊…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0x9,
        (
            "#261F#6P那个人就是艾丝蒂尔\x01",
            "你说的约修亚哥哥吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #315
        0x101,
        (
            "#1025F#2P嗯、嗯……\x02\x03",

            "笔迹也很像，\x01",
            "嗯，应该没错的……\x02\x03",

            "#1015F傍晚在格鲁纳门一侧的\x01",
            "亚宁堡上……\x02\x03",

            "#1020F傍晚……\x01",
            "不是快到了吗……\x02",
        )
    )

    CloseMessageWindow()
    OP_6F(0x1, 0)
    OP_70(0x1, 0x3B)
    OP_73(0x1)
    ClearChrFlags(0xF7, 0x80)

    def lambda_515A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xF7, 2, lambda_515A)

    def lambda_516C():
        OP_8E(0xFE, 0x251C, 0x19A, 0xFFFFCD2E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_516C)
    WaitChrThread(0xF7, 0x1)
    OP_72(0x1, 0x10)
    OP_6F(0x1, 59)
    OP_70(0x1, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    OP_73(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_54E9")

    ChrTalk(    #316
        0x106,
        (
            "#052F喂，你在干吗？\x02\x03",

            "艾南好像要\x01",
            "介绍各地的情况哦？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #317
        0x101,
        (
            "#1026F#6P阿加特……\x02\x03",

            "我应该……怎么办……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #318
        0x106,
        (
            "#055F咦……\x02\x03",

            "喂、喂，你怎么了？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #319
        "\x07\x05艾丝蒂尔默默地把信给阿加特看了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #320
        0x106,
        (
            "#052F……………………………\x02\x03",

            "#050F这是……约修亚吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0x101,
        (
            "#1026F#6P嗯……看来是的。\x02\x03",

            "玲说她是从一个很像\x01",
            "约修亚的人那里收到的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #322
        0x106,
        (
            "#053F原来如此啊……\x02\x03",

            "#051F好啊，去吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #323
        0x101,
        "#1004F#6P哎……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #324
        0x106,
        (
            "#051F别磨蹭了，快去。\x02\x03",

            "我会和其他人说\x01",
            "个合适的理由。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #325
        0x101,
        (
            "#1025F#6P啊……\x02\x03",

            "#1001F谢谢你，阿加特！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 600)
    Sleep(300)

    ChrTalk(    #326
        0x101,
        (
            "#1018F#2P还有玲……\x01",
            "谢谢你告诉我！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #327
        0x9,
        "#264F#6P啊……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 600)

    def lambda_5407():

        label("loc_5407")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_5407")

    QueueWorkItem2(0x9, 1, lambda_5407)

    def lambda_5418():
        OP_8E(0xFE, 0x2026, 0xFA, 0xFFFF8A62, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5418)
    Sleep(500)

    def lambda_5438():
        OP_6D(8540, 250, -16640, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5438)
    OP_8E(0xF7, 0x218E, 0xFA, 0xFFFFCCFC, 0x7D0, 0x0)
    OP_8C(0xF7, 180, 400)
    WaitChrThread(0x101, 0x1)
    OP_6D(8189, 250, -12990, 2000)

    ChrTalk(    #328
        0x9,
        (
            "#268F#6P她走了……\x02\x03",

            "#267F那么想见\x01",
            "那个人吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #329
        0x106,
        (
            "#051F#5P嗯……应该是。\x02\x03",

            "嘿嘿，该怎么\x01",
            "糊弄其他人呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_581E")

    label("loc_54E9")


    ChrTalk(    #330
        0x103,
        (
            "#020F艾丝蒂尔，你在干吗？\x02\x03",

            "艾南好像要向我们\x01",
            "介绍各地的情况哦？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #331
        0x101,
        (
            "#1026F#6P雪拉姐……\x02\x03",

            "我应该……怎么办……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #332
        0x103,
        (
            "#023F…………………………\x02\x03",

            "#022F怎么了，艾丝蒂尔？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #333
        "\x07\x05艾丝蒂尔默默地把信给雪拉扎德看了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #334
        0x103,
        (
            "#022F……………………………\x02\x03",

            "……是约修亚吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #335
        0x101,
        (
            "#1026F#6P嗯……看来是的。\x02\x03",

            "玲说她是从一个很像\x01",
            "约修亚的人那里收到的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #336
        0x103,
        (
            "#026F是的……\x02\x03",

            "#524F好啊，去吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #337
        0x101,
        "#1004F#6P哎……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #338
        0x103,
        (
            "#027F我会帮你搪塞\x01",
            "其他人的。\x02\x03",

            "我知道你想去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #339
        0x101,
        (
            "#1025F#6P啊……\x02\x03",

            "#1001F谢谢雪拉姐！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 600)
    Sleep(300)

    ChrTalk(    #340
        0x101,
        (
            "#1018F#2P还有玲……\x01",
            "谢谢你告诉我！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #341
        0x9,
        "#264F#6P啊……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 600)

    def lambda_574D():

        label("loc_574D")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_574D")

    QueueWorkItem2(0x9, 1, lambda_574D)

    def lambda_575E():
        OP_8E(0xFE, 0x2026, 0xFA, 0xFFFF8A62, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_575E)

    def lambda_5779():
        OP_6D(8540, 250, -16640, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5779)
    OP_8E(0xF7, 0x218E, 0xFA, 0xFFFFCCFC, 0x7D0, 0x0)
    OP_8C(0xF7, 180, 400)
    WaitChrThread(0x101, 0x1)
    OP_6D(8189, 250, -12990, 2000)

    ChrTalk(    #342
        0x9,
        (
            "#268F#6P她走了……\x02\x03",

            "#267F那么想见\x01",
            "那个人吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #343
        0x103,
        (
            "#524F#5P嗯，是啊。\x02\x03",

            "那是那孩子旅行的目的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_581E")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    SetMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/R4101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_31_496F end

    def Function_32_5840(): pass

    label("Function_32_5840")

    OP_8E(0xFE, 0x2CEC, 0x2EE, 0xFFFFCE1E, 0x7D0, 0x0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_32_5840 end

    def Function_33_5865(): pass

    label("Function_33_5865")

    OP_8E(0xFE, 0x12FC, 0x0, 0xFFFFDB2A, 0x7D0, 0x0)
    OP_8E(0xFE, 0x1EBE, 0xFA, 0xFFFFCE82, 0x7D0, 0x0)
    OP_8E(0xFE, 0x25C6, 0x1F4, 0xFFFFCD9C, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_33_5865 end

    def Function_34_58A9(): pass

    label("Function_34_58A9")

    OP_8E(0xFE, 0xDB6, 0x0, 0xFFFFD9D6, 0x7D0, 0x0)
    OP_8E(0xFE, 0x1AB8, 0xFA, 0xFFFFCB12, 0x7D0, 0x0)
    OP_8E(0xFE, 0x21CA, 0xFA, 0xFFFFCB26, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_34_58A9 end

    def Function_35_58ED(): pass

    label("Function_35_58ED")

    OP_8E(0xFE, 0x12FC, 0x0, 0xFFFFDB2A, 0x7D0, 0x0)
    OP_8E(0xFE, 0x1E5A, 0xFA, 0xFFFFCE14, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_35_58ED end

    def Function_36_591D(): pass

    label("Function_36_591D")

    OP_8E(0xFE, 0xDB6, 0x0, 0xFFFFD9D6, 0x7D0, 0x0)
    OP_8E(0xFE, 0x1CDE, 0xFA, 0xFFFFC9AA, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_36_591D end

    def Function_37_594D(): pass

    label("Function_37_594D")

    OP_8E(0xFE, 0x12FC, 0x0, 0xFFFFDB2A, 0x7D0, 0x0)
    OP_8E(0xFE, 0x161C, 0x0, 0xFFFFD044, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_37_594D end

    def Function_38_597D(): pass

    label("Function_38_597D")

    OP_8E(0xFE, 0xDB6, 0x0, 0xFFFFD9D6, 0x7D0, 0x0)
    OP_8E(0xFE, 0x140A, 0x0, 0xFFFFCC48, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_38_597D end

    def Function_39_59AD(): pass

    label("Function_39_59AD")

    EventBegin(0x0)
    OP_4A(0x28, 255)
    OP_4A(0x29, 255)
    OP_4A(0x2A, 255)
    OP_4A(0x2B, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_59D0")
    Call(0, 49)

    label("loc_59D0")

    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    OP_6D(106730, -1920, 53920, 0)
    SetChrName("")

    AnonymousTalk(    #344
        (
            "\x07\x05※进行队伍的重新编组。\x01",
            "　请选择２名固定成员以外的同行者。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_5A81")
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x5, 0x6, 0x3, 0x4, 0x7, 0xFFFF)
    Jump("loc_5AA1")

    label("loc_5A81")

    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0xFF, 0xFF, 0x2, 0x6, 0x3, 0x4, 0x7, 0xFFFF)

    label("loc_5AA1")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0xF7, 0x80)
    SetChrFlags(0xF8, 0x80)
    SetChrFlags(0xF9, 0x80)
    OP_6D(9240, 410, -13010, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_72(0x1, 0x10)
    OP_1D(0xE)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1, 0)
    OP_70(0x1, 0x3B)
    OP_73(0x1)
    Sleep(500)
    OP_43(0x101, 0x1, 0x0, 0x1A)
    Sleep(800)
    OP_43(0xF7, 0x1, 0x0, 0x1B)
    Sleep(800)
    OP_43(0xF8, 0x1, 0x0, 0x1C)
    Sleep(800)
    OP_43(0xF9, 0x1, 0x0, 0x1D)
    Sleep(2000)

    def lambda_5B62():
        OP_6D(4550, 0, -13010, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5B62)
    OP_6C(32000, 3000)
    WaitChrThread(0xF9, 0x1)

    ChrTalk(    #345
        0x101,
        (
            "#1011F#6P那么……\x01",
            "接下来是柏斯地区。\x02\x03",

            "准备完毕后\x01",
            "就马上去飞船坪吧？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_5C21")

    ChrTalk(    #346
        0x106,
        (
            "#051F#5P反正空贼事件\x01",
            "王国军应该正在搜查。\x02\x03",

            "也不紧急，\x01",
            "没必要马上去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C6D")

    label("loc_5C21")


    ChrTalk(    #347
        0x103,
        (
            "#020F#5P反正空贼事件\x01",
            "王国军应该正在搜查。\x02\x03",

            "也不紧急，\x01",
            "没必要马上去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C6D")


    ChrTalk(    #348
        0x101,
        (
            "#1006F#6P这样啊。\x02\x03",

            "就是说解决了剩下的\x01",
            "工作后再去不迟喽？\x02",
        )
    )

    CloseMessageWindow()
    OP_71(0x1, 0x10)
    OP_A2(0x163D)
    OP_28(0x8E, 0x1, 0x10)
    OP_28(0x8E, 0x1, 0x20)
    OP_28(0x8E, 0x1, 0x40)
    OP_28(0x8E, 0x1, 0x80)
    OP_28(0x8E, 0x1, 0x100)
    EventEnd(0x0)
    OP_4B(0x28, 255)
    OP_4B(0x29, 255)
    OP_4B(0x2A, 255)
    OP_4B(0x2B, 255)
    Return()

    # Function_39_59AD end

    def Function_40_5CE4(): pass

    label("Function_40_5CE4")

    SetChrPos(0xA, 4360, 0, -46020, 45)
    SetChrPos(0xB, 8590, 250, 4630, 135)
    SetChrPos(0xC, -20020, 0, -18430, 45)
    SetChrPos(0xD, -1290, 0, -27300, 225)
    SetChrPos(0xE, -9520, 250, -34120, 135)
    SetChrPos(0xF, -5550, 0, 10730, 45)
    SetChrPos(0x10, -2220, 0, -52660, 135)
    SetChrPos(0x11, 8320, 0, -54670, 135)
    SetChrPos(0x12, -6330, 0, -43560, 45)
    SetChrPos(0x13, -4470, 0, -43980, 315)
    SetChrPos(0x14, 7400, 250, -24080, 135)
    SetChrPos(0x15, -7630, 250, -23890, 180)
    SetChrPos(0x16, 1760, 0, 3810, 180)
    SetChrPos(0x17, 80, 0, -5910, 315)
    SetChrPos(0x18, 10730, 0, -660, 270)
    SetChrPos(0x19, -10270, 250, -2340, 90)
    SetChrPos(0x1A, -12400, 0, -18460, 90)
    SetChrPos(0x1B, 7690, 0, -41750, 180)
    SetChrPos(0x1C, 3030, 0, -21550, 180)
    SetChrPos(0x1D, -3210, 0, -13780, 180)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1D, 0x80)
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
    Return()

    # Function_40_5CE4 end

    def Function_41_5F24(): pass

    label("Function_41_5F24")

    LoadEffect(0x0, "map\\\\mpsmk0.eff")
    LoadEffect(0x1, "map\\\\mpfire2.eff")
    LoadEffect(0x2, "map\\\\mpkaji0.eff")
    OP_22(0x87, 0x1, 0x50)
    OP_22(0xAE, 0x1, 0x50)
    PlayEffect(0x2, 0xFF, 0xFF, -40, 250, -19800, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 6610, 1800, -55210, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 250, 4400, -9460, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, -6990, 1800, -36580, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, -10790, 5400, -31940, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, -12500, 5400, -3340, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 12600, 4800, -33570, 0, 0, 0, 1100, 1100, 1100, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 300, 3900, -2500, 0, 0, 0, 1500, 1800, 1300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, -740, 3210, -30070, 0, 0, 0, 1600, 1700, 1400, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 12400, 1900, -37980, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, -15780, 7900, -15450, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 10800, 4800, 9940, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 31290, 5000, -7600, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 6400, 1200, -55200, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 12720, 4600, -33670, 0, 0, 0, 1700, 1700, 1700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 12400, 1700, -38000, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, -1000, 2700, -29750, 0, 0, 0, 2200, 2200, 2200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, -15780, 7600, -15200, 0, 0, 0, 1800, 1800, 1800, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 1000, 2400, -2390, 0, 0, 0, 2500, 2500, 2500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 31290, 4500, -7600, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 340, 4000, -9320, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, -6720, 1500, -36580, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, -10840, 4800, -32049, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, -12750, 5200, -3340, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 10800, 4700, 9940, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_41_5F24 end

    def Function_42_6494(): pass

    label("Function_42_6494")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_64B4")
    Call(0, 49)
    Call(0, 52)
    FadeToBright(0, 0)

    label("loc_64B4")

    OP_D2(0x70371, 0x70376, 0x16)
    OP_D2(0x290144, 0x290148, 0x17)
    OP_D2(0x290144, 0x290148, 0x18)
    OP_D2(0x290144, 0x290148, 0x19)
    OP_D2(0x270110, 0x270120, 0x1B)
    OP_D2(0x270130, 0x270140, 0x1C)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_6509"),
        (5, "loc_6516"),
        (6, "loc_6523"),
        (7, "loc_6530"),
        (SWITCH_DEFAULT, "loc_653D"),
    )


    label("loc_6509")

    OP_D2(0x701D0, 0x701DC, 0x1D)
    Jump("loc_653D")

    label("loc_6516")

    OP_D2(0x70218, 0x70224, 0x1D)
    Jump("loc_653D")

    label("loc_6523")

    OP_D2(0x70230, 0x7023C, 0x1D)
    Jump("loc_653D")

    label("loc_6530")

    OP_D2(0x70248, 0x70254, 0x1D)
    Jump("loc_653D")

    label("loc_653D")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_6556"),
        (5, "loc_6563"),
        (6, "loc_6570"),
        (7, "loc_657D"),
        (SWITCH_DEFAULT, "loc_658A"),
    )


    label("loc_6556")

    OP_D2(0x701D0, 0x701DC, 0x1E)
    Jump("loc_658A")

    label("loc_6563")

    OP_D2(0x70218, 0x70224, 0x1E)
    Jump("loc_658A")

    label("loc_6570")

    OP_D2(0x70230, 0x7023C, 0x1E)
    Jump("loc_658A")

    label("loc_657D")

    OP_D2(0x70248, 0x70254, 0x1E)
    Jump("loc_658A")

    label("loc_658A")

    SetChrChipByIndex(0x1E, 22)
    SetChrPos(0x101, 630, 0, -62820, 0)
    SetChrPos(0x102, 1830, 0, -62880, 0)
    SetChrPos(0xF8, 270, 0, -64190, 0)
    SetChrPos(0xF9, 1700, 0, -64349, 0)
    SetChrFlags(0x34, 0x80)
    SetChrFlags(0x35, 0x80)
    SetChrFlags(0x36, 0x80)
    SetChrFlags(0x37, 0x80)
    SetChrFlags(0x38, 0x80)
    OP_6D(780, 250, 3690, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3370, 0)
    OP_6C(22000, 0)
    OP_6E(435, 0)
    OP_C8(0x200, 0x46, "C_PLAC04._CH", 0x0, 0x3E8)
    FadeToBright(1000, 0)

    def lambda_664D():
        OP_6D(1690, 0, -62710, 9000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_664D)

    def lambda_6665():
        OP_67(0, 8670, -10000, 9000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6665)

    def lambda_667D():
        OP_6B(1940, 9000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_667D)

    def lambda_668D():
        OP_6C(33000, 9000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_668D)
    OP_6E(389, 9000)

    ChrTalk(    #349
        0x101,
        "#1020F#5P真、真过分……！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_66E9")

    ChrTalk(    #350
        0x107,
        "#065F#6P怎、怎么会……\x02",
    )

    CloseMessageWindow()

    label("loc_66E9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6715")

    ChrTalk(    #351
        0x103,
        "#523F#6P真是触目惊心……\x02",
    )

    CloseMessageWindow()

    label("loc_6715")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_673D")

    ChrTalk(    #352
        0x108,
        "#077F#6P太惨烈了……\x02",
    )

    CloseMessageWindow()

    label("loc_673D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6763")

    ChrTalk(    #353
        0x106,
        "#057F#6P可恶……！\x02",
    )

    CloseMessageWindow()

    label("loc_6763")

    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0x102, 28)

    ChrTalk(    #354
        0x102,
        "#1046F#4P……敌人来了！\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    SetChrFlags(0x1F, 0x4)
    SetChrFlags(0x20, 0x4)
    SetChrChipByIndex(0x1F, 20)
    SetChrChipByIndex(0x20, 20)
    SetChrPos(0x1F, -3390, 1000, -51000, 180)
    SetChrPos(0x20, 2660, 1000, -51000, 180)

    def lambda_67F1():
        OP_6D(2080, 0, -60800, 1200)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_67F1)

    def lambda_6809():
        OP_67(0, 7000, -10000, 1200)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6809)

    def lambda_6821():
        OP_6B(1800, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6821)

    def lambda_6831():
        OP_6E(389, 1200)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_6831)
    SetChrChipByIndex(0x1F, 21)
    OP_43(0x1F, 0x3, 0x0, 0x2B)

    def lambda_684D():
        OP_8F(0xFE, 0x0, 0x1F4, 0xFFFF13AC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_684D)
    Sleep(200)
    SetChrChipByIndex(0x20, 21)

    def lambda_6872():
        OP_8F(0xFE, 0xB0E, 0x1F4, 0xFFFF15A0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_6872)
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 27)
    SetChrSubChip(0xF8, 0)
    SetChrChipByIndex(0xF8, 29)
    SetChrSubChip(0xF9, 0)
    SetChrChipByIndex(0xF9, 30)
    WaitChrThread(0x1F, 0x1)
    WaitChrThread(0x20, 0x1)
    OP_44(0x1F, 0x3)
    OP_23(0x13A)
    WaitChrThread(0x101, 0x0)
    OP_43(0x1F, 0x0, 0x0, 0x2C)
    Sleep(100)
    OP_43(0x20, 0x0, 0x0, 0x2C)
    WaitChrThread(0x1F, 0x0)
    OP_44(0x1F, 0xFF)
    OP_44(0x20, 0xFF)
    Battle(0x54F, 0x0, 0x0, 0x0, 0xFF)
    Call(0, 45)
    Return()

    # Function_42_6494 end

    def Function_43_68F2(): pass

    label("Function_43_68F2")

    OP_22(0x13A, 0x0, 0x64)
    Sleep(300)
    OP_22(0x13A, 0x0, 0x64)
    Sleep(300)
    OP_22(0x13A, 0x0, 0x64)
    Sleep(300)
    OP_22(0x13A, 0x0, 0x64)
    Sleep(300)
    OP_22(0x13A, 0x0, 0x64)
    Return()

    # Function_43_68F2 end

    def Function_44_6920(): pass

    label("Function_44_6920")

    SetChrChipByIndex(0xFE, 23)
    OP_99(0xFE, 0x0, 0x2, 0x5DC)
    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
    OP_99(0xFE, 0x3, 0x4, 0x9C4)
    Return()

    # Function_44_6920 end

    def Function_45_694B(): pass

    label("Function_45_694B")

    EventBegin(0x0)
    OP_D2(0x70371, 0x70376, 0x16)
    OP_D2(0x270110, 0x270120, 0x1B)
    OP_D2(0x270130, 0x270140, 0x1C)
    OP_44(0x1F, 0x1)
    OP_44(0x20, 0x1)
    OP_44(0x21, 0x1)
    OP_6D(30, 0, -56130, 0)
    OP_67(0, 7860, -10000, 0)
    OP_6B(2260, 0)
    OP_6C(359000, 0)
    OP_6E(371, 0)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x80)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0xF8, 65535)
    SetChrSubChip(0xF8, 0)
    SetChrChipByIndex(0xF9, 65535)
    SetChrSubChip(0xF9, 0)
    SetChrPos(0x101, -490, 0, -62350, 0)
    SetChrPos(0x102, 790, 0, -62340, 0)
    SetChrPos(0xF8, -870, 0, -64030, 0)
    SetChrPos(0xF9, 1170, 0, -64250, 0)
    SetChrFlags(0x34, 0x80)
    SetChrFlags(0x35, 0x80)
    SetChrFlags(0x36, 0x80)
    SetChrFlags(0x37, 0x80)
    SetChrFlags(0x38, 0x80)

    def lambda_6A4E():
        OP_6D(70, 0, -61320, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6A4E)

    def lambda_6A66():
        OP_6B(1990, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6A66)
    FadeToBright(1000, 0)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #355
        0x101,
        (
            "#1022F#5P哎呀……\x01",
            "怎、怎么办……\x02\x03",

            "#1005F在这种情况下\x01",
            "应该做什么才好呢……！\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x1E, 4920, 0, -49670, 225)
    ClearChrFlags(0x1E, 0x80)

    NpcTalk(    #356
        0x1E,
        "青年的声音",
        "#6P──各位！？\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B64")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_6BA2")

    label("loc_6B64")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B8B")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_6BA2")

    label("loc_6B8B")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_6BA2")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6BCE")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_6C0C")

    label("loc_6BCE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6BF5")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_6C0C")

    label("loc_6BF5")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_6C0C")

    Sleep(1000)

    def lambda_6C17():
        OP_6D(700, 0, -60230, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6C17)

    def lambda_6C2F():
        OP_67(0, 5480, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6C2F)

    def lambda_6C47():
        OP_6B(2720, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_6C47)

    def lambda_6C57():
        OP_6C(0, 3000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_6C57)

    def lambda_6C67():
        OP_6E(289, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6C67)

    def lambda_6C77():
        OP_8E(0xFE, 0x76C, 0x0, 0xFFFF1776, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_6C77)

    def lambda_6C92():

        label("loc_6C92")

        TurnDirection(0xFE, 0x1E, 400)
        OP_48()
        Jump("loc_6C92")

    QueueWorkItem2(0x101, 1, lambda_6C92)
    Sleep(50)

    def lambda_6CA8():

        label("loc_6CA8")

        TurnDirection(0xFE, 0x1E, 400)
        OP_48()
        Jump("loc_6CA8")

    QueueWorkItem2(0x102, 1, lambda_6CA8)
    Sleep(50)

    def lambda_6CBE():

        label("loc_6CBE")

        TurnDirection(0xFE, 0x1E, 400)
        OP_48()
        Jump("loc_6CBE")

    QueueWorkItem2(0xF8, 1, lambda_6CBE)
    Sleep(50)

    def lambda_6CD4():

        label("loc_6CD4")

        TurnDirection(0xFE, 0x1E, 400)
        OP_48()
        Jump("loc_6CD4")

    QueueWorkItem2(0xF9, 1, lambda_6CD4)
    WaitChrThread(0x1E, 0x1)
    OP_8C(0x1E, 225, 400)
    OP_44(0x102, 0x1)
    OP_8C(0x102, 45, 400)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #357
        0x101,
        "#1004F#6P艾南先生！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #358
        0x1E,
        (
            "#762F#2P你们来得正好！\x02\x03",

            "是为了女王陛下的\x01",
            "事来王都的吧！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #359
        0x102,
        "#1042F#6P嗯……现在的情况是？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #360
        0x1E,
        (
            "#764F#2P现在军队的守备队\x01",
            "正在东街区和西街区作战。\x02\x03",

            "形势很严峻，\x01",
            "不过现在也只有交给他们了。\x02\x03",

            "#762F各位请去追击\x01",
            "前往城堡的执行者们吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #361
        0x101,
        "#1020F#6P可、可是！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6E46")

    ChrTalk(    #362
        0x103,
        "#022F#6P市区要不要紧？\x02",
    )

    CloseMessageWindow()
    Jump("loc_6E9D")

    label("loc_6E46")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6E73")

    ChrTalk(    #363
        0x108,
        "#072F#6P市区要不要紧？\x02",
    )

    CloseMessageWindow()
    Jump("loc_6E9D")

    label("loc_6E73")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6E9D")

    ChrTalk(    #364
        0x106,
        "#057F#6P市区要不要紧？\x02",
    )

    CloseMessageWindow()

    label("loc_6E9D")


    ChrTalk(    #365
        0x1E,
        (
            "#762F#2P这附近的人\x01",
            "已经去协会避难了。\x02\x03",

            "在其他的街区也有\x01",
            "军队在引导人们避难。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #366
        0x101,
        (
            "#1007F#6P这样啊……\x02\x03",

            "#1002F……那么，虽然很抱歉，\x01",
            "但我们要抓紧时间赶去王城了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #367
        0x1E,
        (
            "#764F#2P嗯，拜托了。\x02\x03",

            "#760F对了……\x01",
            "不嫌弃的话，请把这个拿去。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1E, 0x102, 0x3E8, 0xBB8, 0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetChrName("")

    AnonymousTalk(    #368
        "\x07\x00得到了\x1F\x05\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_3E(0x205, 4)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_8F(0x1E, 0x76C, 0x0, 0xFFFF1776, 0x7D0, 0x0)

    ChrTalk(    #369
        0x102,
        "#1040F#6P那我们就愧领了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #370
        0x1E,
        (
            "#762F#2P祝你们旗开得胜……\x01",
            "请一定要小心。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7043():

        label("loc_7043")

        TurnDirection(0xFE, 0x1E, 400)
        OP_48()
        Jump("loc_7043")

    QueueWorkItem2(0x102, 1, lambda_7043)
    OP_8C(0x1E, 0, 600)
    OP_8E(0x1E, 0x116C, 0x0, 0xFFFF37BA, 0x1388, 0x0)
    SetChrFlags(0x1E, 0x80)
    Fade(500)
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    OP_6D(1560, 0, -61910, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 1560, 0, -61910, 0)
    SetChrPos(0x1, 1560, 0, -61910, 0)
    SetChrPos(0x2, 1560, 0, -61910, 0)
    SetChrPos(0x3, 1560, 0, -61910, 0)
    OP_0D()
    OP_A2(0x203B)
    OP_28(0x9C, 0x1, 0x10)
    OP_28(0x9C, 0x1, 0x20)
    ClearChrFlags(0x34, 0x80)
    ClearChrFlags(0x35, 0x80)
    ClearChrFlags(0x36, 0x80)
    ClearChrFlags(0x37, 0x80)
    ClearChrFlags(0x38, 0x80)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_45_694B end

    def Function_46_7135(): pass

    label("Function_46_7135")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #371
        "\x07\x05门上着锁。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    SetMapFlags(0x2000000)
    Return()

    # Function_46_7135 end

    def Function_47_716E(): pass

    label("Function_47_716E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7177")
    Return()

    label("loc_7177")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7197")
    Call(0, 49)
    Call(0, 52)
    FadeToBright(0, 0)

    label("loc_7197")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #372
        (
            "\x07\x05东街区断断续续地\x01",
            "传来枪声和剑戟的声音。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7236")

    ChrTalk(    #373
        0x101,
        (
            "#1002F（看来是军队在\x01",
            "和猎兵作战……)\x02\x03",

            "(我们得赶快\x01",
            "赶往城堡！)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_73C3")

    label("loc_7236")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7285")

    ChrTalk(    #374
        0x102,
        (
            "#1042F（这边布置了\x01",
            "军队……)\x02\x03",

            "(就交给他们吧，我们去城堡。)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_73C3")

    label("loc_7285")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_72D1")

    ChrTalk(    #375
        0x103,
        (
            "#022F（这边应该\x01",
            "有军队在作战……)\x02\x03",

            "(我们还是去城堡吧。)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_73C3")

    label("loc_72D1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7330")

    ChrTalk(    #376
        0x107,
        (
            "#062F（军队的失败们看来\x01",
            "正在结社的人作战……)\x02\x03",

            "(我们得赶快\x01",
            "赶往城堡……！)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_73C3")

    label("loc_7330")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7380")

    ChrTalk(    #377
        0x106,
        (
            "#057F（看来军队住在\x01",
            "和猎兵们作战……)\x02\x03",

            "(我们还是去城堡吧。)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_73C3")

    label("loc_7380")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_73C3")

    ChrTalk(    #378
        0x108,
        (
            "#072F（这边有军队\x01",
            "在守护……)\x02\x03",

            "(我们赶紧去王城吧)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_73C3")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)
    Return()

    # Function_47_716E end

    def Function_48_73E4(): pass

    label("Function_48_73E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_73ED")
    Return()

    label("loc_73ED")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_740D")
    Call(0, 49)
    Call(0, 52)
    FadeToBright(0, 0)

    label("loc_740D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #379
        (
            "\x07\x05西街区断断续续地\x01",
            "传来枪声和剑戟的声音。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_74AC")

    ChrTalk(    #380
        0x101,
        (
            "#1002F（看来是军队在\x01",
            "和猎兵作战……)\x02\x03",

            "(我们得赶快\x01",
            "赶往城堡！)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_763C")

    label("loc_74AC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_74FB")

    ChrTalk(    #381
        0x102,
        (
            "#1042F（这边布置了\x01",
            "军队……)\x02\x03",

            "(就交给他们吧，我们去城堡。)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_763C")

    label("loc_74FB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7547")

    ChrTalk(    #382
        0x103,
        (
            "#022F（这边应该\x01",
            "有军队在作战……)\x02\x03",

            "(我们还是去城堡吧。)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_763C")

    label("loc_7547")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_75A9")

    ChrTalk(    #383
        0x107,
        (
            "#062F（军队的士兵们看来\x01",
            "正在和结社的人作战……）\x02\x03",

            "(我们得赶快\x01",
            "赶往城堡……！)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_763C")

    label("loc_75A9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_75F9")

    ChrTalk(    #384
        0x106,
        (
            "#057F（看来军队正在\x01",
            "和猎兵们作战……)\x02\x03",

            "(我们还是去城堡吧。)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_763C")

    label("loc_75F9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_763C")

    ChrTalk(    #385
        0x108,
        (
            "#072F（这边有军队\x01",
            "在守护……)\x02\x03",

            "(我们赶紧去王城吧)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_763C")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)
    Return()

    # Function_48_73E4 end

    def Function_49_765D(): pass

    label("Function_49_765D")

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
        (0, "loc_76D7"),
        (1, "loc_76DD"),
        (SWITCH_DEFAULT, "loc_76E3"),
    )


    label("loc_76D7")

    OP_A2(0x1200)
    Jump("loc_76E3")

    label("loc_76DD")

    OP_A2(0x1201)
    Jump("loc_76E3")

    label("loc_76E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_76F1")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_76F5")

    label("loc_76F1")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_76F5")

    Return()

    # Function_49_765D end

    def Function_50_76F6(): pass

    label("Function_50_76F6")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_7739")
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x3, 0x4, 0x6, 0x7, 0xFFFF)
    Jump("loc_7757")

    label("loc_7739")

    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0xFF, 0xFF, 0x3, 0x4, 0x6, 0x7, 0xFFFF)

    label("loc_7757")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_50_76F6 end

    def Function_51_7777(): pass

    label("Function_51_7777")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_77B6")
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0x6, 0xFF, 0x4, 0x7, 0xFFFF)
    Jump("loc_77D0")

    label("loc_77B6")

    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0x6, 0xFF, 0x4, 0x7, 0xFFFF)

    label("loc_77D0")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_51_7777 end

    def Function_52_77F0(): pass

    label("Function_52_77F0")

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

    # Function_52_77F0 end

    def Function_53_7849(): pass

    label("Function_53_7849")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_7A31")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7899")

    ChrTalk(    #386
        0x101,
        (
            "#1002F（现在不能\x01",
            "离开王都……)\x02\x03",

            "(得赶紧赶往城堡！)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A0E")

    label("loc_7899")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_78E6")

    ChrTalk(    #387
        0x102,
        (
            "#1042F（现在不能\x01",
            "离开王都……)\x02\x03",

            "(得分秒必争地赶往城堡。)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A0E")

    label("loc_78E6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_792A")

    ChrTalk(    #388
        0x103,
        (
            "#022F（现在时间\x01",
            "十分宝贵……)\x02\x03",

            "(赶紧去城堡吧。)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A0E")

    label("loc_792A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_797D")

    ChrTalk(    #389
        0x107,
        (
            "#065F（啊……这边是出口哦。）\x02\x03",

            "#062F（总之现在\x01",
            "赶往城堡……！)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A0E")

    label("loc_797D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_79C9")

    ChrTalk(    #390
        0x106,
        (
            "#050F（没时间在这里\x01",
            "磨磨蹭蹭的了……)\x02\x03",

            "(得赶紧去城堡。)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A0E")

    label("loc_79C9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7A0E")

    ChrTalk(    #391
        0x108,
        (
            "#072F（没时间在这里\x01",
            "担搁了……)\x02\x03",

            "(我们赶紧去王城吧)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A0E")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)
    Jump("loc_7EEE")

    label("loc_7A31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7A99")
    EventBegin(0x1)
    TurnDirection(0x101, 0x0, 400)

    ChrTalk(    #392
        0x101,
        (
            "#1006F玲应该还在城里。\x02\x03",

            "那么\x01",
            "一定要把她找出来！\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_7EEE")

    label("loc_7A99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7CA6")
    EventBegin(0x1)
    TurnDirection(0x0, 0x1, 400)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B01")

    ChrTalk(    #393
        0x101,
        (
            "#1006F她一个人出城\x01",
            "总是不可能的吧。\x02\x03",

            "首先从东街区\x01",
            "附近开始找。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C88")

    label("loc_7B01")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B4F")

    ChrTalk(    #394
        0x103,
        (
            "#020F无法想象她会\x01",
            "一个人出城。\x02\x03",

            "总之先搜索\x01",
            "东街区附近吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C88")

    label("loc_7B4F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7BA7")

    ChrTalk(    #395
        0x107,
        (
            "#060F小玲应该还没\x01",
            "出城吧。\x02\x03",

            "首先从她昨天去过的\x01",
            "东街区附近开始找吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C88")

    label("loc_7BA7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7BEF")

    ChrTalk(    #396
        0x106,
        (
            "#050F她总不至于\x01",
            "出城吧。\x02\x03",

            "首先从东街区\x01",
            "附近开始找。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C88")

    label("loc_7BEF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C3B")

    ChrTalk(    #397
        0x108,
        (
            "#070F她应该不会\x01",
            "出城吧。\x02\x03",

            "总之先从东街区\x01",
            "附近开始找吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C88")

    label("loc_7C3B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C88")

    ChrTalk(    #398
        0x105,
        (
            "#040F我觉得她还不至于\x01",
            "一个人出城。\x02\x03",

            "总之从东街区\x01",
            "开始找吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7C88")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_7EEE")

    label("loc_7CA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7DB2")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7CF0")

    ChrTalk(    #399
        0x101,
        (
            "#1000F已经，差不多时间了。\x01",
            "该回协会了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7D94")

    label("loc_7CF0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D25")

    ChrTalk(    #400
        0x104,
        (
            "#030F太阳都要下山了。\x01",
            "回协会吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7D94")

    label("loc_7D25")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D58")

    ChrTalk(    #401
        0x108,
        (
            "#070F已经挺玩了。\x01",
            "赶紧回协会吧\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7D94")

    label("loc_7D58")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D94")

    ChrTalk(    #402
        0x105,
        (
            "#040F太阳都要下山了。\x01",
            "差不多该回协会了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D94")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_7EEE")

    label("loc_7DB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7EEE")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7DFC")

    ChrTalk(    #403
        0x101,
        (
            "#1000F没必要出城。\x02\x03",

            "赶快\x01",
            "去打听情况吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7ED3")

    label("loc_7DFC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E47")

    ChrTalk(    #404
        0x104,
        (
            "#030F恐吓信的调查\x01",
            "看来还没结束。\x02\x03",

            "我们快去打听情况吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7ED3")

    label("loc_7E47")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E8D")

    ChrTalk(    #405
        0x108,
        (
            "#070F就算出去\x01",
            "也找不到罪犯。\x02\x03",

            "赶快打听\x01",
            "好情况吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7ED3")

    label("loc_7E8D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7ED3")

    ChrTalk(    #406
        0x105,
        (
            "#040F恐吓信的调查\x01",
            "还没结束呢。\x02\x03",

            "赶快回去打听情况吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7ED3")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_7EEE")

    Return()

    # Function_53_7849 end

    def Function_54_7EEF(): pass

    label("Function_54_7EEF")

    Call(0, 60)
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_54_7EEF end

    def Function_55_7F0F(): pass

    label("Function_55_7F0F")

    Call(0, 60)
    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_55_7F0F end

    def Function_56_7F2F(): pass

    label("Function_56_7F2F")

    Call(0, 60)
    OP_59()

    def lambda_7F3A():
        OP_6D(-3370, 0, 9000, 1000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_7F3A)
    Fade(1000)
    SetChrPos(0x0, -3370, 0, 12430, 180)
    SetChrPos(0x1, -3370, 0, 12430, 180)
    SetChrPos(0x2, -3370, 0, 12430, 180)
    SetChrPos(0x3, -3370, 0, 12430, 180)
    SetChrPos(0x12F, -3370, 0, 12430, 180)
    OP_0D()
    OP_8C(0x0, 180, 0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_56_7F2F end

    def Function_57_7FB6(): pass

    label("Function_57_7FB6")

    Call(0, 60)
    OP_59()

    def lambda_7FC1():
        OP_6D(3370, 0, 9000, 1000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_7FC1)
    Fade(1000)
    SetChrPos(0x0, 3370, 0, 12430, 180)
    SetChrPos(0x1, 3370, 0, 12430, 180)
    SetChrPos(0x2, 3370, 0, 12430, 180)
    SetChrPos(0x3, 3370, 0, 12430, 180)
    SetChrPos(0x12F, 3370, 0, 12430, 180)
    OP_0D()
    OP_8C(0x0, 180, 0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_57_7FB6 end

    def Function_58_803D(): pass

    label("Function_58_803D")

    Call(0, 60)
    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_58_803D end

    def Function_59_805D(): pass

    label("Function_59_805D")

    Call(0, 60)
    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_59_805D end

    def Function_60_807D(): pass

    label("Function_60_807D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_824C")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_8139")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_80E9")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_80AF")
    TurnDirection(0x106, 0x1, 400)
    Jump("loc_80B6")

    label("loc_80AF")

    TurnDirection(0x106, 0x0, 400)

    label("loc_80B6")


    ChrTalk(    #407
        0x106,
        (
            "#050F……得赶快确认消息。\x01",
            "径直返回协会吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8136")

    label("loc_80E9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_80FF")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_8106")

    label("loc_80FF")

    TurnDirection(0x103, 0x0, 400)

    label("loc_8106")


    ChrTalk(    #408
        0x103,
        (
            "#020F……得赶快确认消息。\x01",
            "径直返回协会吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8136")

    Jump("loc_8249")

    label("loc_8139")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_8190")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8156")
    TurnDirection(0x106, 0x1, 400)
    Jump("loc_815D")

    label("loc_8156")

    TurnDirection(0x106, 0x0, 400)

    label("loc_815D")


    ChrTalk(    #409
        0x106,
        (
            "#050F……得赶快确认消息。\x01",
            "径直返回协会吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_81DD")

    label("loc_8190")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81A6")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_81AD")

    label("loc_81A6")

    TurnDirection(0x103, 0x0, 400)

    label("loc_81AD")


    ChrTalk(    #410
        0x103,
        (
            "#020F……得赶快确认消息。\x01",
            "径直返回协会吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_81DD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8209")
    TurnDirection(0x0, 0xF7, 400)

    ChrTalk(    #411
        0x101,
        "#1000F嗯，是啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_822F")

    label("loc_8209")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_822F")
    TurnDirection(0x0, 0xF7, 400)

    ChrTalk(    #412
        0x107,
        "#060F嗯，是啊\x02",
    )

    CloseMessageWindow()

    label("loc_822F")


    ChrTalk(    #413
        0x12F,
        "#268F啊，好无聊。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_8249")

    Jump("loc_84CD")

    label("loc_824C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_84CD")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8299")

    ChrTalk(    #414
        0x108,
        (
            "#070F军队的负责人\x01",
            "快要来了。\x02\x03",

            "赶紧回协会吧\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_84CD")

    label("loc_8299")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_8351")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_82F9")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_82BD")
    TurnDirection(0x106, 0x1, 400)
    Jump("loc_82C4")

    label("loc_82BD")

    TurnDirection(0x106, 0x0, 400)

    label("loc_82C4")


    ChrTalk(    #415
        0x106,
        (
            "#050F军队的负责人\x01",
            "快要来了。\x02\x03",

            "赶快回协会吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_834E")

    label("loc_82F9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_830F")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_8316")

    label("loc_830F")

    TurnDirection(0x103, 0x0, 400)

    label("loc_8316")


    ChrTalk(    #416
        0x103,
        (
            "#020F军队的负责人\x01",
            "也快要来了。\x02\x03",

            "我们赶快回协会吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_834E")

    Jump("loc_84CD")

    label("loc_8351")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_83AA")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_836E")
    TurnDirection(0x106, 0x1, 400)
    Jump("loc_8375")

    label("loc_836E")

    TurnDirection(0x106, 0x0, 400)

    label("loc_8375")


    ChrTalk(    #417
        0x106,
        (
            "#050F军队的负责人\x01",
            "快要来了。\x02\x03",

            "赶快回协会吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_83FF")

    label("loc_83AA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_83C0")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_83C7")

    label("loc_83C0")

    TurnDirection(0x103, 0x0, 400)

    label("loc_83C7")


    ChrTalk(    #418
        0x103,
        (
            "#020F军队的负责人\x01",
            "也快要来了。\x02\x03",

            "我们赶快回协会吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_83FF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_842D")
    TurnDirection(0x0, 0xF7, 400)

    ChrTalk(    #419
        0x101,
        "#1011F哎呀，是啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_84AF")

    label("loc_842D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8458")
    TurnDirection(0x0, 0xF7, 400)

    ChrTalk(    #420
        0x104,
        "#030F嗯，是啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_84AF")

    label("loc_8458")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8489")
    TurnDirection(0x0, 0xF7, 400)

    ChrTalk(    #421
        0x105,
        "#040F嗯嗯，是的是的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_84AF")

    label("loc_8489")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_84AF")
    TurnDirection(0x0, 0xF7, 400)

    ChrTalk(    #422
        0x107,
        "#060F嗯，是啊\x02",
    )

    CloseMessageWindow()

    label("loc_84AF")


    ChrTalk(    #423
        0x12F,
        "#264F咦？不是这边吗？\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_84CD")

    Return()

    # Function_60_807D end

    def Function_61_84CE(): pass

    label("Function_61_84CE")

    SetPlaceName(0xB9)
    Return()

    # Function_61_84CE end

    def Function_62_84D2(): pass

    label("Function_62_84D2")

    SetPlaceName(0xB0)
    Return()

    # Function_62_84D2 end

    def Function_63_84D6(): pass

    label("Function_63_84D6")

    SetPlaceName(0xB2)
    Return()

    # Function_63_84D6 end

    def Function_64_84DA(): pass

    label("Function_64_84DA")

    SetPlaceName(0xAE)
    Return()

    # Function_64_84DA end

    def Function_65_84DE(): pass

    label("Function_65_84DE")

    SetPlaceName(0xB3)
    Return()

    # Function_65_84DE end

    SaveToFile()

Try(main)
