from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2500   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2500.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '乔儿',                                 # 9
        '汉斯',                                 # 10
        '基库',                                 # 11
        '米克',                                 # 12
        '芙拉瑟',                               # 13
        '蕾娜',                                 # 14
        '坎诺',                                 # 15
        '帕布尔',                               # 16
        '艾福托老师',                           # 17
        '巴克斯',                               # 18
        '奥利维尔',                             # 19
        '布卢布兰的亡灵',                       # 20
        '强化猎兵',                             # 21
        '强化猎兵',                             # 22
        '强化猎兵',                             # 23
        '强化猎兵',                             # 24
        '装甲猎豹',                             # 25
        '装甲猎豹',                             # 26
        '哨兵',                                 # 27
        '哨兵',                                 # 28
        '王国军士兵',                           # 29
        '王国军士兵',                           # 30
        '卡露娜',                               # 31
        '库拉茨',                               # 32
        '罗迪',                                 # 33
        '巴托姆',                               # 34
        '王立学院·小道',                       # 35
        '街景林道方向',                         # 36
        '',                                     # 37
        '',                                     # 38
        '',                                     # 39
        '',                                     # 40
        '',                                     # 41
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
        'ED6_DT07/CH02390 ._CH',             # 00
        'ED6_DT07/CH02550 ._CH',             # 01
        'ED6_DT07/CH02320 ._CH',             # 02
        'ED6_DT26/CH20238 ._CH',             # 03
        'ED6_DT07/CH02323 ._CH',             # 04
        'ED6_DT07/CH01080 ._CH',             # 05
        'ED6_DT07/CH01090 ._CH',             # 06
        'ED6_DT07/CH01370 ._CH',             # 07
        'ED6_DT07/CH01580 ._CH',             # 08
        'ED6_DT07/CH01093 ._CH',             # 09
        'ED6_DT07/CH01460 ._CH',             # 0A
        'ED6_DT07/CH01020 ._CH',             # 0B
        'ED6_DT06/CH20045 ._CH',             # 0C
        'ED6_DT26/CH20270 ._CH',             # 0D
        'ED6_DT26/CH20422 ._CH',             # 0E
        'ED6_DT26/CH20424 ._CH',             # 0F
        'ED6_DT29/CH12320 ._CH',             # 10
        'ED6_DT29/CH12321 ._CH',             # 11
        'ED6_DT07/CH01640 ._CH',             # 12
        'ED6_DT07/CH01240 ._CH',             # 13
        'ED6_DT07/CH01260 ._CH',             # 14
        'ED6_DT26/CH20423 ._CH',             # 15
        'ED6_DT07/CH01360 ._CH',             # 16
        'ED6_DT29/CH12330 ._CH',             # 17
        'ED6_DT29/CH12331 ._CH',             # 18
        'ED6_DT29/CH12350 ._CH',             # 19
        'ED6_DT29/CH12351 ._CH',             # 1A
        'ED6_DT29/CH12570 ._CH',             # 1B
        'ED6_DT29/CH12571 ._CH',             # 1C
    )

    AddCharChipPat(
        'ED6_DT07/CH02390P._CP',             # 00
        'ED6_DT07/CH02550P._CP',             # 01
        'ED6_DT07/CH02320P._CP',             # 02
        'ED6_DT26/CH20238P._CP',             # 03
        'ED6_DT07/CH02323P._CP',             # 04
        'ED6_DT07/CH01080P._CP',             # 05
        'ED6_DT07/CH01090P._CP',             # 06
        'ED6_DT07/CH01370P._CP',             # 07
        'ED6_DT07/CH01580P._CP',             # 08
        'ED6_DT07/CH01093P._CP',             # 09
        'ED6_DT07/CH01460P._CP',             # 0A
        'ED6_DT07/CH01020P._CP',             # 0B
        'ED6_DT06/CH20045P._CP',             # 0C
        'ED6_DT26/CH20270P._CP',             # 0D
        'ED6_DT26/CH20422P._CP',             # 0E
        'ED6_DT26/CH20424P._CP',             # 0F
        'ED6_DT29/CH12320P._CP',             # 10
        'ED6_DT29/CH12321P._CP',             # 11
        'ED6_DT07/CH01640P._CP',             # 12
        'ED6_DT07/CH01240P._CP',             # 13
        'ED6_DT07/CH01260P._CP',             # 14
        'ED6_DT26/CH20423P._CP',             # 15
        'ED6_DT07/CH01360P._CP',             # 16
        'ED6_DT29/CH12330P._CP',             # 17
        'ED6_DT29/CH12331P._CP',             # 18
        'ED6_DT29/CH12350P._CP',             # 19
        'ED6_DT29/CH12351P._CP',             # 1A
        'ED6_DT29/CH12570P._CP',             # 1B
        'ED6_DT29/CH12571P._CP',             # 1C
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
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
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 58530,
        Z                   = 0,
        Y                   = 49540,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 32450,
        Z                   = 0,
        Y                   = 63980,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 32530,
        Z                   = 0,
        Y                   = 66280,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 29910,
        Z                   = -2000,
        Y                   = 47650,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 35640,
        Z                   = 0,
        Y                   = 77750,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 60000,
        Z                   = 0,
        Y                   = 50000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 39000,
        Z                   = -2000,
        Y                   = 46000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 38010,
        Z                   = 0,
        Y                   = 21120,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
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
        Unknown3            = 23,
        ChipIndex           = 0x17,
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
        Unknown3            = 23,
        ChipIndex           = 0x17,
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
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
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
        X                   = 12860,
        Z                   = 0,
        Y                   = 47520,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 12860,
        Z                   = 0,
        Y                   = 44370,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 29380,
        Z                   = -2000,
        Y                   = 35460,
        Direction           = 318,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 8,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 37390,
        Z                   = -2000,
        Y                   = 58930,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = 84080,
        Z                   = 0,
        Y                   = 28010,
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
        X                   = -3490,
        Z                   = 0,
        Y                   = 46180,
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
        X                   = 52160,
        Z                   = 0,
        Y                   = 12900,
        Unknown_0C          = 180,
        Unknown_0E          = 25,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xF3D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 31950,
        Z                   = 0,
        Y                   = 19680,
        Unknown_0C          = 180,
        Unknown_0E          = 23,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xF3C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 15470,
        Z                   = 0,
        Y                   = 14340,
        Unknown_0C          = 180,
        Unknown_0E          = 27,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xF3E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 21240,
        Z                   = 0,
        Y                   = 45950,
        Unknown_0C          = 180,
        Unknown_0E          = 23,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xF3C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 15510,
        Z                   = 0,
        Y                   = 81080,
        Unknown_0C          = 180,
        Unknown_0E          = 25,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xF3D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 34060,
        Z                   = -2000,
        Y                   = 46430,
        Unknown_0C          = 180,
        Unknown_0E          = 25,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xF3D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 33470,
        Z                   = 0,
        Y                   = 66230,
        Unknown_0C          = 180,
        Unknown_0E          = 16,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xF3F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 62710,
        Z                   = 0,
        Y                   = 50010,
        Unknown_0C          = 180,
        Unknown_0E          = 23,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xF3C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 63430,
        Z                   = 0,
        Y                   = 79810,
        Unknown_0C          = 180,
        Unknown_0E          = 27,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xF3E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 12290,
        Y                   = -1000,
        Z                   = 47300,
        Range               = 14900,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xAE38,
        Unknown_18          = 0x0,
        Unknown_1C          = 85,
    )

    DeclEvent(
        X                   = 12600,
        Y                   = -2000,
        Z                   = 44600,
        Range               = 14000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xB98C,
        Unknown_18          = 0x0,
        Unknown_1C          = 22,
    )

    DeclEvent(
        X                   = 13400,
        Y                   = -1000,
        Z                   = 24000,
        Range               = 18060,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x625C,
        Unknown_18          = 0x0,
        Unknown_1C          = 50,
    )

    DeclEvent(
        X                   = 26000,
        Y                   = -1000,
        Z                   = 11270,
        Range               = 26800,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x36F6,
        Unknown_18          = 0x0,
        Unknown_1C          = 51,
    )

    DeclEvent(
        X                   = 47400,
        Y                   = -1000,
        Z                   = 11070,
        Range               = 49000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x3A48,
        Unknown_18          = 0x0,
        Unknown_1C          = 52,
    )

    DeclEvent(
        X                   = 52060,
        Y                   = -1000,
        Z                   = 26000,
        Range               = 54200,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x7918,
        Unknown_18          = 0x0,
        Unknown_1C          = 55,
    )

    DeclEvent(
        X                   = 52060,
        Y                   = -1000,
        Z                   = 61000,
        Range               = 54200,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x101D0,
        Unknown_18          = 0x0,
        Unknown_1C          = 56,
    )

    DeclEvent(
        X                   = 43200,
        Y                   = -1000,
        Z                   = 82000,
        Range               = 41450,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x136F0,
        Unknown_18          = 0x0,
        Unknown_1C          = 69,
    )

    DeclEvent(
        X                   = 27430,
        Y                   = -1000,
        Z                   = 82000,
        Range               = 26100,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x13880,
        Unknown_18          = 0x0,
        Unknown_1C          = 70,
    )

    DeclEvent(
        X                   = 13400,
        Y                   = -1000,
        Z                   = 68000,
        Range               = 18060,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x10E3C,
        Unknown_18          = 0x0,
        Unknown_1C          = 75,
    )

    DeclEvent(
        X                   = 41180,
        Y                   = 0,
        Z                   = 74060,
        Range               = 1000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 86,
    )

    DeclEvent(
        X                   = 53030,
        Y                   = 0,
        Z                   = 67260,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 86,
    )

    DeclEvent(
        X                   = 53150,
        Y                   = 0,
        Z                   = 59630,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 87,
    )

    DeclEvent(
        X                   = 48380,
        Y                   = 0,
        Z                   = 45960,
        Range               = 1000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 87,
    )

    DeclEvent(
        X                   = 52870,
        Y                   = 0,
        Z                   = 32110,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 87,
    )

    DeclEvent(
        X                   = 53030,
        Y                   = 0,
        Z                   = 24850,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 88,
    )

    DeclEvent(
        X                   = 47120,
        Y                   = 0,
        Z                   = 19010,
        Range               = 1000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 88,
    )

    DeclEvent(
        X                   = 22030,
        Y                   = 0,
        Z                   = 25660,
        Range               = 1000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 89,
    )

    DeclEvent(
        X                   = 22010,
        Y                   = 0,
        Z                   = 67170,
        Range               = 1000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 90,
    )


    DeclActor(
        TriggerX            = 13480,
        TriggerZ            = 0,
        TriggerY            = 45900,
        TriggerRange        = 700,
        ActorX              = 13480,
        ActorZ              = 1500,
        ActorY              = 46000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 23,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 66600,
        TriggerZ            = 0,
        TriggerY            = 27910,
        TriggerRange        = 700,
        ActorX              = 66600,
        ActorZ              = 1500,
        ActorY              = 27910,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 24,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 17020,
        TriggerZ            = 0,
        TriggerY            = 22130,
        TriggerRange        = 700,
        ActorX              = 17000,
        ActorZ              = 1500,
        ActorY              = 22000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 46,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 16940,
        TriggerZ            = 0,
        TriggerY            = 16040,
        TriggerRange        = 700,
        ActorX              = 17000,
        ActorZ              = 1500,
        ActorY              = 16000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 48,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 57010,
        TriggerZ            = 0,
        TriggerY            = 14090,
        TriggerRange        = 700,
        ActorX              = 56980,
        ActorZ              = 1500,
        ActorY              = 14000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 53,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 57730,
        TriggerZ            = 0,
        TriggerY            = 36050,
        TriggerRange        = 700,
        ActorX              = 58000,
        ActorZ              = 1500,
        ActorY              = 36000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 57,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 58000,
        TriggerZ            = 0,
        TriggerY            = 39920,
        TriggerRange        = 700,
        ActorX              = 58000,
        ActorZ              = 1500,
        ActorY              = 40110,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 59,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 59010,
        TriggerZ            = 0,
        TriggerY            = 45880,
        TriggerRange        = 700,
        ActorX              = 59000,
        ActorZ              = 1500,
        ActorY              = 46040,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 61,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 57910,
        TriggerZ            = 0,
        TriggerY            = 51930,
        TriggerRange        = 700,
        ActorX              = 58000,
        ActorZ              = 1500,
        ActorY              = 51970,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 63,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 49150,
        TriggerZ            = 0,
        TriggerY            = 79920,
        TriggerRange        = 700,
        ActorX              = 48980,
        ActorZ              = 1500,
        ActorY              = 79890,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 67,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 17000,
        TriggerZ            = 0,
        TriggerY            = 77050,
        TriggerRange        = 700,
        ActorX              = 17000,
        ActorZ              = 1500,
        ActorY              = 76930,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 71,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 16960,
        TriggerZ            = 0,
        TriggerY            = 71100,
        TriggerRange        = 700,
        ActorX              = 17000,
        ActorZ              = 1500,
        ActorY              = 71000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 73,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_A1E",          # 00, 0
        "Function_1_E8F",          # 01, 1
        "Function_2_112A",         # 02, 2
        "Function_3_1140",         # 03, 3
        "Function_4_1377",         # 04, 4
        "Function_5_13D4",         # 05, 5
        "Function_6_16DE",         # 06, 6
        "Function_7_1702",         # 07, 7
        "Function_8_1726",         # 08, 8
        "Function_9_174A",         # 09, 9
        "Function_10_1803",        # 0A, 10
        "Function_11_1C10",        # 0B, 11
        "Function_12_1D48",        # 0C, 12
        "Function_13_1F47",        # 0D, 13
        "Function_14_21CD",        # 0E, 14
        "Function_15_23A8",        # 0F, 15
        "Function_16_2A46",        # 10, 16
        "Function_17_2BF8",        # 11, 17
        "Function_18_3152",        # 12, 18
        "Function_19_320C",        # 13, 19
        "Function_20_3240",        # 14, 20
        "Function_21_32BD",        # 15, 21
        "Function_22_338C",        # 16, 22
        "Function_23_4217",        # 17, 23
        "Function_24_4292",        # 18, 24
        "Function_25_44C0",        # 19, 25
        "Function_26_45F1",        # 1A, 26
        "Function_27_4722",        # 1B, 27
        "Function_28_4853",        # 1C, 28
        "Function_29_4984",        # 1D, 29
        "Function_30_4AB5",        # 1E, 30
        "Function_31_4BE6",        # 1F, 31
        "Function_32_4E3F",        # 20, 32
        "Function_33_4E55",        # 21, 33
        "Function_34_4F7F",        # 22, 34
        "Function_35_500D",        # 23, 35
        "Function_36_50A5",        # 24, 36
        "Function_37_5138",        # 25, 37
        "Function_38_51D0",        # 26, 38
        "Function_39_5305",        # 27, 39
        "Function_40_5446",        # 28, 40
        "Function_41_5564",        # 29, 41
        "Function_42_569B",        # 2A, 42
        "Function_43_5B3F",        # 2B, 43
        "Function_44_5B83",        # 2C, 44
        "Function_45_5BC7",        # 2D, 45
        "Function_46_5CAB",        # 2E, 46
        "Function_47_5E97",        # 2F, 47
        "Function_48_5F11",        # 30, 48
        "Function_49_6103",        # 31, 49
        "Function_50_6207",        # 32, 50
        "Function_51_6314",        # 33, 51
        "Function_52_6688",        # 34, 52
        "Function_53_68E9",        # 35, 53
        "Function_54_6ADB",        # 36, 54
        "Function_55_6BCB",        # 37, 55
        "Function_56_6DA0",        # 38, 56
        "Function_57_6F75",        # 39, 57
        "Function_58_703C",        # 3A, 58
        "Function_59_710A",        # 3B, 59
        "Function_60_726C",        # 3C, 60
        "Function_61_732D",        # 3D, 61
        "Function_62_751F",        # 3E, 62
        "Function_63_7602",        # 3F, 63
        "Function_64_76F0",        # 40, 64
        "Function_65_7848",        # 41, 65
        "Function_66_7A13",        # 42, 66
        "Function_67_7A79",        # 43, 67
        "Function_68_7C6B",        # 44, 68
        "Function_69_7D42",        # 45, 69
        "Function_70_7FA3",        # 46, 70
        "Function_71_8204",        # 47, 71
        "Function_72_83F6",        # 48, 72
        "Function_73_84C2",        # 49, 73
        "Function_74_86B4",        # 4A, 74
        "Function_75_8784",        # 4B, 75
        "Function_76_889B",        # 4C, 76
        "Function_77_8AC1",        # 4D, 77
        "Function_78_9039",        # 4E, 78
        "Function_79_9202",        # 4F, 79
        "Function_80_9257",        # 50, 80
        "Function_81_92FE",        # 51, 81
        "Function_82_9AB2",        # 52, 82
        "Function_83_A975",        # 53, 83
        "Function_84_AA0E",        # 54, 84
        "Function_85_AA67",        # 55, 85
        "Function_86_ACA1",        # 56, 86
        "Function_87_ACA5",        # 57, 87
        "Function_88_ACA9",        # 58, 88
        "Function_89_ACAD",        # 59, 89
        "Function_90_ACB1",        # 5A, 90
    )


    def Function_0_A1E(): pass

    label("Function_0_A1E")

    OP_51(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A3D")
    OP_B5(0x0)

    label("loc_A3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_AB9")
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrPos(0x10, 45800, 0, 46000, 0)
    OP_43(0x10, 0x0, 0x0, 0x4)
    ClearChrFlags(0x21, 0x80)
    SetChrPos(0xC, 36500, 0, 70920, 225)
    ClearChrFlags(0xC, 0x80)
    OP_43(0xC, 0x0, 0x6, 0x2)
    SetChrPos(0xD, 35500, 0, 69860, 45)
    ClearChrFlags(0xD, 0x80)
    OP_43(0xD, 0x0, 0x6, 0x2)
    OP_B5(0x0)
    Jump("loc_BC4")

    label("loc_AB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_END)), "loc_AD7")
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    Jump("loc_BC4")

    label("loc_AD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_AF7")
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    OP_B5(0x0)
    Jump("loc_BC4")

    label("loc_AF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_B37")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrPos(0x11, 46910, 0, 52960, 180)
    SetChrPos(0x10, 22070, 0, 28390, 0)
    Jump("loc_BC4")

    label("loc_B37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_B97")
    SetChrPos(0x10, 20410, 0, 28400, 53)
    OP_44(0x11, 0xFF)
    SetChrPos(0x11, 40830, -2000, 42670, 270)
    OP_43(0x11, 0x0, 0x6, 0x2)
    OP_44(0xF, 0xFF)
    SetChrFlags(0xF, 0x10)
    SetChrFlags(0xF, 0x4)
    SetChrChipByIndex(0xF, 9)
    SetChrPos(0xF, 33280, 200, 79020, 180)
    ClearChrFlags(0x20, 0x80)
    Jump("loc_BC4")

    label("loc_B97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_BB0")
    SoundLoad(190)
    ClearChrFlags(0x12, 0x80)
    OP_43(0x10, 0x0, 0x0, 0x3)
    Jump("loc_BC4")

    label("loc_BB0")

    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)

    label("loc_BC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 6)), scpexpr(EXPR_END)), "loc_CD7")
    OP_A3(0x10FE)
    SetMapFlags(0x10000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_BEF")
    OP_A3(0x10F0)
    OP_B5(0x0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 42)
    Jump("loc_CD4")

    label("loc_BEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_C0B")
    OP_A3(0x10F1)
    OP_B5(0x0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 45)
    Jump("loc_CD4")

    label("loc_C0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_C1C")
    OP_A3(0x10F2)
    Event(0, 47)
    Jump("loc_CD4")

    label("loc_C1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 3)), scpexpr(EXPR_END)), "loc_C2D")
    OP_A3(0x10F3)
    Event(0, 49)
    Jump("loc_CD4")

    label("loc_C2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 4)), scpexpr(EXPR_END)), "loc_C3E")
    OP_A3(0x10F4)
    Event(0, 54)
    Jump("loc_CD4")

    label("loc_C3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 5)), scpexpr(EXPR_END)), "loc_C4F")
    OP_A3(0x10F5)
    Event(0, 58)
    Jump("loc_CD4")

    label("loc_C4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 6)), scpexpr(EXPR_END)), "loc_C60")
    OP_A3(0x10F6)
    Event(0, 60)
    Jump("loc_CD4")

    label("loc_C60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 7)), scpexpr(EXPR_END)), "loc_C71")
    OP_A3(0x10F7)
    Event(0, 62)
    Jump("loc_CD4")

    label("loc_C71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 0)), scpexpr(EXPR_END)), "loc_C82")
    OP_A3(0x10F8)
    Event(0, 64)
    Jump("loc_CD4")

    label("loc_C82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 1)), scpexpr(EXPR_END)), "loc_C93")
    OP_A3(0x10F9)
    Event(0, 65)
    Jump("loc_CD4")

    label("loc_C93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 2)), scpexpr(EXPR_END)), "loc_CA4")
    OP_A3(0x10FA)
    Event(0, 66)
    Jump("loc_CD4")

    label("loc_CA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 3)), scpexpr(EXPR_END)), "loc_CB5")
    OP_A3(0x10FB)
    Event(0, 68)
    Jump("loc_CD4")

    label("loc_CB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 4)), scpexpr(EXPR_END)), "loc_CC6")
    OP_A3(0x10FC)
    Event(0, 72)
    Jump("loc_CD4")

    label("loc_CC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 5)), scpexpr(EXPR_END)), "loc_CD4")
    OP_A3(0x10FD)
    Event(0, 74)

    label("loc_CD4")

    Jump("loc_E8E")

    label("loc_CD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_CF6")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 31)
    Jump("loc_E8E")

    label("loc_CF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_D15")
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 33)
    Jump("loc_E8E")

    label("loc_D15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_D2B")
    OP_A3(0x10F2)
    SetMapFlags(0x10000000)
    Event(0, 77)
    Jump("loc_E8E")

    label("loc_D2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 3)), scpexpr(EXPR_END)), "loc_D4A")
    OP_A3(0x10F3)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x59), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 78)
    Jump("loc_E8E")

    label("loc_D4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 4)), scpexpr(EXPR_END)), "loc_D62")
    OP_A3(0x10F4)
    OP_B5(0x0)
    SetMapFlags(0x10000000)
    Event(0, 82)
    Jump("loc_E8E")

    label("loc_D62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x404, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x404, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x404, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x404, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DC3")
    SetMapFlags(0x10000000)
    Event(0, 81)
    Jump("loc_E8E")

    label("loc_DC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x246, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x246, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x246, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E8E")
    OP_44(0x10, 0xFF)
    SetChrPos(0x10, 20410, 0, 28400, 53)
    OP_43(0x10, 0x0, 0x6, 0x2)
    OP_44(0x11, 0xFF)
    SetChrPos(0x11, 40830, -2000, 42670, 270)
    OP_43(0x11, 0x0, 0x6, 0x2)
    OP_44(0xF, 0xFF)
    SetChrFlags(0xF, 0x10)
    SetChrFlags(0xF, 0x4)
    SetChrChipByIndex(0xF, 9)
    SetChrPos(0xF, 33280, 200, 79020, 180)
    SetChrFlags(0x12, 0x80)
    ClearChrFlags(0x20, 0x80)
    OP_A2(0x1221)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (101, "loc_E64"),
        (103, "loc_E6B"),
        (104, "loc_E72"),
        (105, "loc_E79"),
        (106, "loc_E80"),
        (107, "loc_E87"),
        (SWITCH_DEFAULT, "loc_E8E"),
    )


    label("loc_E64")

    Event(0, 25)
    Jump("loc_E8E")

    label("loc_E6B")

    Event(0, 26)
    Jump("loc_E8E")

    label("loc_E72")

    Event(0, 27)
    Jump("loc_E8E")

    label("loc_E79")

    Event(0, 29)
    Jump("loc_E8E")

    label("loc_E80")

    Event(0, 28)
    Jump("loc_E8E")

    label("loc_E87")

    Event(0, 30)
    Jump("loc_E8E")

    label("loc_E8E")

    Return()

    # Function_0_A1E end

    def Function_1_E8F(): pass

    label("Function_1_E8F")

    OP_16(0x2, 0xFA0, 0xFFFEA840, 0xFFFEBFB0, 0x23004C)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EB9")
    OP_B1("t2500_y")
    Jump("loc_EC2")

    label("loc_EB9")

    OP_B1("t2500_n")

    label("loc_EC2")

    OP_64(0x2, 0x1)
    OP_64(0x3, 0x1)
    OP_64(0x4, 0x1)
    OP_64(0x5, 0x1)
    OP_64(0x6, 0x1)
    OP_64(0x7, 0x1)
    OP_64(0x8, 0x1)
    OP_64(0x9, 0x1)
    OP_64(0xA, 0x1)
    OP_64(0xB, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1005")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_F22")
    OP_B5(0x0)
    OP_6F(0x21, 60)
    OP_72(0x21, 0x10)
    OP_64(0x0, 0x1)
    OP_6F(0x22, 60)
    OP_72(0x22, 0x10)
    OP_64(0x1, 0x1)
    Jump("loc_1002")

    label("loc_F22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_END)), "loc_F71")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x59), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)
    OP_6F(0x21, 60)
    OP_72(0x21, 0x10)
    OP_64(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x404, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F5E")
    OP_6F(0x22, 0)
    OP_72(0x22, 0x10)
    Jump("loc_F6E")

    label("loc_F5E")

    OP_6F(0x22, 60)
    OP_72(0x22, 0x10)
    OP_64(0x1, 0x1)

    label("loc_F6E")

    Jump("loc_1002")

    label("loc_F71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 3)), scpexpr(EXPR_END)), "loc_FF2")
    OP_B5(0x0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)
    OP_6F(0x21, 0)
    OP_72(0x21, 0x10)
    OP_64(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x404, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FAF")
    OP_6F(0x22, 0)
    OP_72(0x22, 0x10)
    Jump("loc_FBF")

    label("loc_FAF")

    OP_6F(0x22, 60)
    OP_72(0x22, 0x10)
    OP_64(0x1, 0x1)

    label("loc_FBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FEF")
    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    OP_65(0x5, 0x1)
    OP_65(0x6, 0x1)
    OP_65(0x7, 0x1)
    OP_65(0x8, 0x1)
    OP_65(0x9, 0x1)
    OP_65(0xA, 0x1)
    OP_65(0xB, 0x1)

    label("loc_FEF")

    Jump("loc_1002")

    label("loc_FF2")

    OP_6F(0x21, 0)
    OP_72(0x21, 0x10)
    OP_64(0x0, 0x1)

    label("loc_1002")

    Jump("loc_1053")

    label("loc_1005")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_101F")
    OP_64(0x0, 0x1)
    OP_72(0x21, 0x10)
    OP_6F(0x21, 60)
    Jump("loc_1037")

    label("loc_101F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_102D")
    OP_64(0x0, 0x1)
    Jump("loc_1037")

    label("loc_102D")

    OP_72(0x21, 0x10)
    OP_72(0x2D, 0x4)

    label("loc_1037")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 3)), scpexpr(EXPR_END)), "loc_104C")
    OP_64(0x1, 0x1)
    OP_6F(0x22, 60)
    Jump("loc_1053")

    label("loc_104C")

    OP_6F(0x22, 0)

    label("loc_1053")

    OP_71(0x9, 0x4)
    OP_71(0xA, 0x4)
    OP_71(0xB, 0x4)
    OP_71(0xC, 0x4)
    OP_71(0xD, 0x4)
    OP_71(0xE, 0x4)
    OP_71(0xF, 0x4)
    OP_71(0x10, 0x4)
    OP_71(0x11, 0x4)
    OP_71(0x12, 0x4)
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
    OP_71(0x1F, 0x4)
    OP_71(0x20, 0x4)
    OP_71(0x23, 0x4)
    OP_71(0x24, 0x4)
    OP_71(0x25, 0x4)
    OP_71(0x26, 0x4)
    OP_71(0x27, 0x4)
    OP_71(0x28, 0x4)
    OP_71(0x29, 0x4)
    OP_71(0x2A, 0x4)
    OP_71(0x2B, 0x4)
    OP_71(0x2C, 0x4)
    OP_51(0x25, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xC3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x27, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xC3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2A, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2B, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xC3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_E8F end

    def Function_2_112A(): pass

    label("Function_2_112A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_113F")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_112A")

    label("loc_113F")

    Return()

    # Function_2_112A end

    def Function_3_1140(): pass

    label("Function_3_1140")

    OP_8E(0xFE, 0xEA60, 0x0, 0xED80, 0x1388, 0x0)
    OP_8E(0xFE, 0xE86C, 0x0, 0xF0A0, 0x1388, 0x0)
    OP_8E(0xFE, 0xE678, 0x0, 0xF3C0, 0x1388, 0x0)
    OP_8E(0xFE, 0xE484, 0x0, 0xF550, 0x1388, 0x0)
    OP_8E(0xFE, 0xE290, 0x0, 0xF618, 0x1388, 0x0)

    label("loc_11A4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1376")
    OP_8E(0xFE, 0xBB80, 0x0, 0xF618, 0x1388, 0x0)
    OP_8E(0xFE, 0xB98C, 0x0, 0xF550, 0x1388, 0x0)
    OP_8E(0xFE, 0xB798, 0x0, 0xF3C0, 0x1388, 0x0)
    OP_8E(0xFE, 0xB5A4, 0x0, 0xF0A0, 0x1388, 0x0)
    OP_8E(0xFE, 0xB3B0, 0x0, 0xED80, 0x1388, 0x0)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0xFE, 0xB3B0, 0x0, 0x7918, 0x1388, 0x0)
    OP_8E(0xFE, 0xB5A4, 0x0, 0x75F8, 0x1388, 0x0)
    OP_8E(0xFE, 0xB798, 0x0, 0x72D8, 0x1388, 0x0)
    OP_8E(0xFE, 0xB98C, 0x0, 0x7148, 0x1388, 0x0)
    OP_8E(0xFE, 0xBB80, 0x0, 0x7080, 0x1388, 0x0)
    OP_8E(0xFE, 0xE290, 0x0, 0x7080, 0x1388, 0x0)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0xFE, 0xE484, 0x0, 0x7148, 0x1388, 0x0)
    OP_8E(0xFE, 0xE678, 0x0, 0x72D8, 0x1388, 0x0)
    OP_8E(0xFE, 0xE86C, 0x0, 0x75F8, 0x1388, 0x0)
    OP_8E(0xFE, 0xEA60, 0x0, 0x7918, 0x1388, 0x0)
    OP_8E(0xFE, 0xEA60, 0x0, 0xED80, 0x1388, 0x0)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0xFE, 0xE86C, 0x0, 0xF0A0, 0x1388, 0x0)
    OP_8E(0xFE, 0xE678, 0x0, 0xF3C0, 0x1388, 0x0)
    OP_8E(0xFE, 0xE484, 0x0, 0xF550, 0x1388, 0x0)
    OP_8E(0xFE, 0xE290, 0x0, 0xF618, 0x1388, 0x0)
    Jump("loc_11A4")

    label("loc_1376")

    Return()

    # Function_3_1140 end

    def Function_4_1377(): pass

    label("Function_4_1377")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13D3")
    OP_8E(0xFE, 0xB3B0, 0x0, 0xF9CE, 0x7D0, 0x0)
    OP_8E(0xFE, 0x567C, 0x0, 0xF9CE, 0x7D0, 0x0)
    OP_8E(0xFE, 0x567C, 0x0, 0x6D2E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xB3B0, 0x0, 0x6D2E, 0x7D0, 0x0)
    Jump("Function_4_1377")

    label("loc_13D3")

    Return()

    # Function_4_1377 end

    def Function_5_13D4(): pass

    label("Function_5_13D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_1401")

    label("loc_13DB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13FE")
    OP_8D(0xFE, 48790, 55520, 45390, 51020, 1000)
    Jump("loc_13DB")

    label("loc_13FE")

    Jump("loc_16DD")

    label("loc_1401")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_16DD")
    Sleep(1500)
    OP_8B(0xFE, 0x9858, 0xDAC0, 0x190)
    OP_8E(0xFE, 0x9858, 0xFFFFF830, 0xDAC0, 0x7D0, 0x0)
    OP_8E(0xFE, 0x9858, 0xFFFFF830, 0xDAC0, 0x7D0, 0x0)
    OP_8E(0xFE, 0x9470, 0xFFFFF830, 0xDEA8, 0x7D0, 0x0)
    OP_8E(0xFE, 0x88B8, 0xFFFFF830, 0xDEA8, 0x7D0, 0x0)
    OP_8E(0xFE, 0x84D0, 0xFFFFF830, 0xE290, 0x7D0, 0x0)
    OP_8E(0xFE, 0x84D0, 0x0, 0xF618, 0x7D0, 0x0)
    OP_8E(0xFE, 0x80E8, 0x0, 0xFA00, 0x7D0, 0x0)
    OP_8E(0xFE, 0x5DC0, 0x0, 0xFA00, 0x7D0, 0x0)
    OP_8E(0xFE, 0x59D8, 0x0, 0xF618, 0x7D0, 0x0)
    OP_8E(0xFE, 0x59D8, 0x0, 0xB3B0, 0x7D0, 0x0)
    OP_8B(0xFE, 0x4B64, 0xB3B0, 0x190)
    Sleep(500)
    OP_8B(0xFE, 0x7080, 0xA3AC, 0x190)
    Sleep(200)
    OP_8B(0xFE, 0x7080, 0xC3B4, 0x190)
    Sleep(1500)
    OP_8B(0xFE, 0x71AC, 0xB3B0, 0x190)
    OP_8E(0xFE, 0x6D60, 0xFFFFF830, 0xB3B0, 0x7D0, 0x0)
    OP_8E(0xFE, 0x7148, 0xFFFFF830, 0xAFC8, 0x7D0, 0x0)
    OP_8E(0xFE, 0x7148, 0xFFFFF830, 0x8CA0, 0x7D0, 0x0)
    OP_8E(0xFE, 0x7530, 0xFFFFF830, 0x88B8, 0x7D0, 0x0)
    OP_8E(0xFE, 0x80E8, 0xFFFFF830, 0x88B8, 0x7D0, 0x0)
    OP_8E(0xFE, 0x84D0, 0xFFFFF830, 0x84D0, 0x7D0, 0x0)
    OP_8E(0xFE, 0x84D0, 0x0, 0x7148, 0x7D0, 0x0)
    OP_8B(0xFE, 0x8CA0, 0x7148, 0x190)
    Sleep(500)
    OP_8B(0xFE, 0x7D00, 0x7148, 0x190)
    Sleep(800)
    OP_8B(0xFE, 0x9470, 0x61A8, 0x190)
    Sleep(1000)
    OP_8E(0xFE, 0x9470, 0x0, 0x61A8, 0x7D0, 0x0)
    Sleep(500)
    OP_8B(0xFE, 0x884A, 0x5096, 0x190)
    Sleep(500)
    OP_8B(0xFE, 0xA028, 0x55F0, 0x190)
    Sleep(1000)
    OP_8B(0xFE, 0xA028, 0x6D60, 0x190)
    OP_8E(0xFE, 0xA028, 0x0, 0x6D60, 0x7D0, 0x0)
    OP_8E(0xFE, 0xABE0, 0x0, 0x6D60, 0x7D0, 0x0)
    OP_8E(0xFE, 0xAFC8, 0x0, 0x7148, 0x7D0, 0x0)
    OP_8E(0xFE, 0xAFC8, 0x0, 0xB3B0, 0x7D0, 0x0)
    OP_8B(0xFE, 0x4B64, 0xB3B0, 0x190)
    Sleep(500)
    OP_8B(0xFE, 0x7080, 0xA3AC, 0x190)
    Sleep(200)
    OP_8B(0xFE, 0x7080, 0xC3B4, 0x190)
    Sleep(1500)
    OP_8B(0xFE, 0x71AC, 0xB3B0, 0x190)
    OP_8E(0xFE, 0x9858, 0xFFFFF830, 0xB3B0, 0x7D0, 0x0)
    Jump("loc_1401")

    label("loc_16DD")

    Return()

    # Function_5_13D4 end

    def Function_6_16DE(): pass

    label("Function_6_16DE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1701")
    OP_8D(0xFE, 27793, 65500, 35900, 62530, 2000)
    Jump("Function_6_16DE")

    label("loc_1701")

    Return()

    # Function_6_16DE end

    def Function_7_1702(): pass

    label("Function_7_1702")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1725")
    OP_8D(0xFE, 34220, 72290, 36840, 78320, 2000)
    Jump("Function_7_1702")

    label("loc_1725")

    Return()

    # Function_7_1702 end

    def Function_8_1726(): pass

    label("Function_8_1726")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1749")
    OP_8D(0xFE, 27610, 33720, 30640, 36510, 2000)
    Jump("Function_8_1726")

    label("loc_1749")

    Return()

    # Function_8_1726 end

    def Function_9_174A(): pass

    label("Function_9_174A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_17FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_17AD")

    ChrTalk(    #0
        0xFE,
        "哈，学院祭真开心啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "嗯，等到学院祭到来之前\x01",
            "就先享受一下社团活动吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17FF")

    label("loc_17AD")

    OP_A2(0x8)

    ChrTalk(    #2
        0xFE,
        "哈，学院祭真开心啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "能再那样和大家一起热闹\x01",
            "不知要等到什么时候了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17FF")

    TalkEnd(0xFE)
    Return()

    # Function_9_174A end

    def Function_10_1803(): pass

    label("Function_10_1803")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x24C, 2)), scpexpr(EXPR_END)), "loc_18B3")

    ChrTalk(    #4
        0xFE,
        (
            "#035F呵，王立学院的女子宿舍啊……\x02\x03",

            "可爱的花蕾们\x01",
            "一定等不及了吧。\x02\x03",

            "#035F呵呵……呵呵呵呵…………\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #5
        0x101,
        "#1019F（……绝对不带你去。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C0C")

    label("loc_18B3")

    OP_22(0xBE, 0x0, 0x64)
    OP_99(0xFE, 0x0, 0x4, 0x578)
    OP_99(0xFE, 0x4, 0x0, 0x1F4)
    Sleep(1000)
    OP_A2(0x1262)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1934")

    ChrTalk(    #6
        0xFE,
        "#035F呵，这不是艾丝蒂尔吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x101,
        (
            "#1018F怎样？奥利维尔。\x01",
            "打听有进展吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)
    Jump("loc_1977")

    label("loc_1934")


    ChrTalk(    #8
        0xFE,
        "#035F呼，这不是公主殿下吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x105,
        (
            "#040F辛苦了。\x01",
            "打听有进展吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1977")


    ChrTalk(    #10
        0xFE,
        (
            "#035F哈哈，这件事\x01",
            "委托给朵洛希了。\x02\x03",

            "话说回来，我碰巧听说\x01",
            "这里有女学生的宿舍呢。\x02\x03",

            "我正急着\x01",
            "找那个呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x105,
        "#044F啊，找女子宿舍……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x101,
        (
            "#1004F找那个干什么啊。\x02\x03",

            "#1015F不过，总觉～得\x01",
            "能猜到理由……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #13
        0xFE,
        (
            "#031F呵，这还用说吗。\x02\x03",

            "为了守护少女的卧室，\x01",
            "我要立即赶去才行啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        "#1007F唉，果然来这套。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x105,
        "#045F意、意料之中的行动啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "#035F若等危险至极的魔掌\x01",
            "伸长之后就为时已晚了……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #17
        0xFE,
        (
            "#031F对了。\x01",
            "我说，艾丝蒂尔……\x02\x03",

            "你以前，好像在这个学院\x01",
            "里待过吧。\x02\x03",

            "可以的话，能不能\x01",
            "带我去宿舍？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(    #18
        0x101,
        (
            "#1016F唔、唔～………\x02\x03",

            "#1016F现、现在有点忙，\x01",
            "稍后再说吧。\x02\x03",

            "#1019F（被、被这家伙知道\x01",
            "宿舍在哪就更危险了。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C0C")

    TalkEnd(0xFE)
    Return()

    # Function_10_1803 end

    def Function_11_1C10(): pass

    label("Function_11_1C10")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_1CA3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1C47")

    ChrTalk(    #19
        0xFE,
        (
            "这所学校真是\x01",
            "什么学生都有啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CA0")

    label("loc_1C47")

    OP_A2(0x6)

    ChrTalk(    #20
        0xFE,
        (
            "昨天夜晚，我在校舍巡逻\x01",
            "竟然发现有男生藏在教室。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "突然跑出来\x01",
            "真是把我吓死了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CA0")

    Jump("loc_1D44")

    label("loc_1CA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_1CF9")

    ChrTalk(    #22
        0xFE,
        (
            "呼，看来\x01",
            "操场好像没问题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "好了，待会儿还要\x01",
            "检查各社团的备用品呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D44")

    label("loc_1CF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_1D44")

    ChrTalk(    #24
        0xFE,
        (
            "明天起\x01",
            "就要开始社团活动了嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "正在检查\x01",
            "操场有没有异常呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D44")

    TalkEnd(0xFE)
    Return()

    # Function_11_1C10 end

    def Function_12_1D48(): pass

    label("Function_12_1D48")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_1E12")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DC8")

    ChrTalk(    #26
        0xFE,
        (
            "啊，游击士们。\x01",
            "真是辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "我们在这之后也要准备\x01",
            "重新开课，开始变忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        "唔，彼此加油啦。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_1E0F")

    label("loc_1DC8")


    ChrTalk(    #29
        0xFE,
        (
            "我们在这之后也要准备\x01",
            "重新开课，开始变忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        "唔，彼此加油啦。\x02",
    )

    CloseMessageWindow()

    label("loc_1E0F")

    Jump("loc_1F43")

    label("loc_1E12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_1E64")

    ChrTalk(    #31
        0xFE,
        (
            "好，今天起\x01",
            "终于要重开社团了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "变迟钝的身体\x01",
            "要努力重新锻炼啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F43")

    label("loc_1E64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 2)), scpexpr(EXPR_END)), "loc_1E7B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1E75")
    Jump("loc_1E78")

    label("loc_1E75")

    OP_A2(0x5)

    label("loc_1E78")

    Jump("loc_1F43")

    label("loc_1E7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_1ED0")

    ChrTalk(    #33
        0xFE,
        "呼，差不多要天黑了啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "为了明天开始的社团活动\x01",
            "今天就早点休息吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F43")

    label("loc_1ED0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_1F43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1EF5")

    ChrTalk(    #35
        0xFE,
        "哎嘿、哎嘿……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F43")

    label("loc_1EF5")

    OP_A2(0x5)
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #36
        0xFE,
        (
            "明天起是久违的\x01",
            "社团活动嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "要趁今天到处跑跑\x01",
            "活动筋骨才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F43")

    TalkEnd(0xFE)
    Return()

    # Function_12_1D48 end

    def Function_13_1F47(): pass

    label("Function_13_1F47")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_1FF0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1F96")

    ChrTalk(    #38
        0xFE,
        (
            "听说旧校舍\x01",
            "潜伏着可疑的人物？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        "像是小说成真一样。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1FED")

    label("loc_1F96")

    OP_A2(0x4)

    ChrTalk(    #40
        0xFE,
        (
            "刚才\x01",
            "碰巧听说了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "听说旧校舍\x01",
            "潜伏着可疑的人物？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        "像是小说成真一样。\x02",
    )

    CloseMessageWindow()

    label("loc_1FED")

    Jump("loc_21C9")

    label("loc_1FF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_20C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2051")

    ChrTalk(    #43
        0xFE,
        (
            "我想在休假中\x01",
            "试着写写长篇小说。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "打算以我们的学校\x01",
            "这样的学院做为舞台。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20C5")

    label("loc_2051")

    OP_A2(0x4)

    ChrTalk(    #45
        0xFE,
        (
            "我想在放假期间\x01",
            "试着写写长篇小说呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "打算以我们的学校\x01",
            "这样的学院做为舞台。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "现在正在考虑\x01",
            "这个设定。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20C5")

    Jump("loc_21C9")

    label("loc_20C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_21C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2137")

    ChrTalk(    #48
        0xFE,
        (
            "嗯～不过很有魅力呢。\x01",
            "袭击学院的怪现象……之类的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "现在构思中的小说里\x01",
            "说不定能用上。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21C9")

    label("loc_2137")

    OP_A2(0x4)

    ChrTalk(    #50
        0xFE,
        "考试中的怪事……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "不，没什么\x01",
            "特别的啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "不过，很有魅力呢。\x01",
            "袭击学院的怪现象……之类的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "现在构思中的小说里\x01",
            "说不定能用上。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21C9")

    TalkEnd(0xFE)
    Return()

    # Function_13_1F47 end

    def Function_14_21CD(): pass

    label("Function_14_21CD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_2269")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_220A")

    ChrTalk(    #54
        0xFE,
        (
            "今天美术部的各位\x01",
            "计划一起画素描哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2266")

    label("loc_220A")

    OP_A2(0x3)

    ChrTalk(    #55
        0xFE,
        (
            "今天美术部的各位\x01",
            "计划一起画素描。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        "……不过还没人来呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        "是不是来早了点呢。\x02",
    )

    CloseMessageWindow()

    label("loc_2266")

    Jump("loc_23A4")

    label("loc_2269")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_231C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_22B6")

    ChrTalk(    #58
        0xFE,
        (
            "好久没\x01",
            "坐在画布前了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "感觉现在能\x01",
            "画出漂亮的画呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2319")

    label("loc_22B6")

    OP_A2(0x3)

    ChrTalk(    #60
        0xFE,
        "哼哼哼～⊙\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "为了准备美术部的作品\x01",
            "正在寻找题材呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "哟，晚霞中的校舍\x01",
            "说不定很不错。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2319")

    Jump("loc_23A4")

    label("loc_231C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_23A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_235F")

    ChrTalk(    #63
        0xFE,
        "应该没什么特别的吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        "我去问问其他人吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_23A4")

    label("loc_235F")

    OP_A2(0x3)

    ChrTalk(    #65
        0xFE,
        (
            "考试期间中发生的\x01",
            "怪事……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "不，不知道。\x01",
            "问问其它人吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23A4")

    TalkEnd(0xFE)
    Return()

    # Function_14_21CD end

    def Function_15_23A8(): pass

    label("Function_15_23A8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_28D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x418, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23C4")
    Call(0, 17)
    OP_A2(0x20C5)
    Jump("loc_28D2")

    label("loc_23C4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2888")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x418, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2839")

    ChrTalk(    #67
        0xFE,
        (
            "小姐要有\x01",
            "广阔的视野才行……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "出身名门的人\x01",
            "就有背负这名声的命运。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x101,
        "#1015F…………………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #70
        0xFE,
        "哎呀，怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x101,
        (
            "#1008F嗯、嗯，基于职务上的理由\x01",
            "有些事情想打听一下……\x02\x03",

            "#1015F（那个，结果……\x01",
            "　相亲怎样了？）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #72
        0x102,
        (
            "#1048F（慢着……\x01",
            "　这哪算是职务上的话？)\x02\x03",

            "（单纯是艾丝蒂尔\x01",
            "　想知道吧。)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #73
        0x101,
        (
            "#1009F（有、有什么关系。\x01",
            "　多少也和工作有点关联嘛。)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        "（嗯，倒也无所谓……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        "（……当然是大成功啦。）\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x101, 0xFE, 400)
    Sleep(400)

    ChrTalk(    #76
        0x101,
        (
            "#1004F（咦咦！？成功了！？）\x02\x03",

            "#1013F（那个，这么说来……\x01",
            "　芙拉瑟，莫非……)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "（做事要循序渐进，\x01",
            "　不可能一下子就订婚啦。)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "（单纯只是相互\x01",
            "　都比较中意而已。)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x101,
        (
            "#1008F（这、这样啊……）\x02\x03",

            "#1007F（呼～虽说是别人的事\x01",
            "　还是禁不住着急起来了。)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_274E")
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #80
        0x103,
        (
            "#027F（哎呀，为什么艾丝蒂尔\x01",
            "　这么着急？)\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #81
        0x101,
        (
            "#1013F（没、没什么深刻涵义啦。\x01",
            "　只是因为我们同年……)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27E3")

    label("loc_274E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27E3")
    TurnDirection(0x106, 0x101, 400)

    ChrTalk(    #82
        0x106,
        (
            "#055F（啊？为什么你\x01",
            "　看起来这么着急？)\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(    #83
        0x101,
        (
            "#1013F（没、没什么深刻涵义，\x01",
            "　只是因为我们同年……)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27E3")


    ChrTalk(    #84
        0xFE,
        (
            "（暂时打算通过写信\x01",
            "　来加深交流。)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "（所以说，订婚的话\x01",
            "　还早得很吧。)\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x20C6)
    Jump("loc_2885")

    label("loc_2839")


    ChrTalk(    #86
        0xFE,
        (
            "大小姐要有\x01",
            "广阔的视野才行……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "出身名门的人\x01",
            "就有背负这名声的命运。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2885")

    Jump("loc_28D2")

    label("loc_2888")


    ChrTalk(    #88
        0xFE,
        (
            "小姐要有\x01",
            "广阔的视野才行……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "出身名门的人\x01",
            "就有背负这名声的命运。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28D2")

    Jump("loc_2A42")

    label("loc_28D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_294B")

    ChrTalk(    #90
        0xFE,
        (
            "（这次相亲的对象\x01",
            "　帝国某贵族子弟……)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "（对方听说是王国留学中的才女，\x01",
            "　马上就对小姐产生了兴趣。)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A42")

    label("loc_294B")

    OP_A2(0x2)

    ChrTalk(    #92
        0xFE,
        (
            "（芙拉瑟好像以为\x01",
            "　得到了我国的许可……)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "（其实这次归国，一开始\x01",
            "就预定到柏斯旅行的。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "（那边也有餐厅，\x01",
            "　还有从帝国出发的定期船……)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        (
            "（作为跟帝国贵族的相亲会场，\x01",
            "　确实是最理想的地方。)\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(    #96
        0xFE,
        "（…………不过这是秘密。）\x02",
    )

    CloseMessageWindow()

    label("loc_2A42")

    TalkEnd(0xFE)
    Return()

    # Function_15_23A8 end

    def Function_16_2A46(): pass

    label("Function_16_2A46")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_2B1F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x418, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A62")
    Call(0, 17)
    OP_A2(0x20C5)
    Jump("loc_2B1C")

    label("loc_2A62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2AC8")

    ChrTalk(    #97
        0xFE,
        (
            "不、不管怎样……\x01",
            "今天真是帮大忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "王国好像有危机，\x01",
            "不过大家都决心坚守学院生活。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B1C")

    label("loc_2AC8")


    ChrTalk(    #99
        0xC,
        (
            "自己的人生被人操纵，\x01",
            "没人会感到高兴的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xC,
        (
            "我不可能像蕾娜那样\x01",
            "想得那么乐观。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B1C")

    Jump("loc_2BF4")

    label("loc_2B1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2B69")

    ChrTalk(    #101
        0xFE,
        (
            "归国前会在柏斯城里\x01",
            "稍作停留。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "呵呵，蕾娜\x01",
            "也有优点嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BF4")

    label("loc_2B69")

    OP_A2(0x1)

    ChrTalk(    #103
        0xFE,
        "嘿嘿……太好了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        (
            "归省前会在柏斯城里\x01",
            "稍作停留。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "虽然没几天,\x01",
            "但足够享受市内旅游了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "这也多亏蕾娜\x01",
            "和国家进行了交涉呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BF4")

    TalkEnd(0xFE)
    Return()

    # Function_16_2A46 end

    def Function_17_2BF8(): pass

    label("Function_17_2BF8")

    OP_4A(0xC, 255)
    OP_4A(0xD, 255)
    OP_62(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xC, 0x101, 0)
    Sleep(400)

    ChrTalk(    #107
        0xC,
        (
            "啊，艾丝蒂尔\x01",
            "和约修亚……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x101, 400)

    ChrTalk(    #108
        0xD,
        "各位不是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xD,
        (
            "你们救了小姐，\x01",
            "实在是感激不尽。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xD,
        (
            "我代表本家\x01",
            "致以深切感谢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x101,
        "#1017F哪里，太客气了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x102,
        "#1040F嗯嗯，我们只是尽了义务。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x102, 400)

    ChrTalk(    #113
        0xC,
        (
            "呵呵，游击士\x01",
            "总是这么谦虚。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xC,
        (
            "不过，真的\x01",
            "非常感谢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xC,
        (
            "多亏事件的解决，\x01",
            "我们之间的鸿沟也被填埋了啊……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2F7A")

    ChrTalk(    #116
        0x101,
        (
            "#1004F啊……\x01",
            "这么说难道……\x02\x03",

            "……你们俩和好了？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 400)

    ChrTalk(    #117
        0xC,
        "嗯嗯，就算是吧。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x101, 400)

    ChrTalk(    #118
        0xD,
        (
            "只是我的立场\x01",
            "得到了理解。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xD,
        (
            "不过……\x01",
            "好像还没完全接受。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xD, 400)

    ChrTalk(    #120
        0xC,
        "哎呀，那是当然了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xC,
        (
            "随便给人家定什么相亲，\x01",
            "怎么可能接受嘛。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xC, 400)

    ChrTalk(    #122
        0xD,
        (
            "所以说，请别\x01",
            "拘泥那些小事了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xD,
        (
            "我是希望芙拉瑟\x01",
            "拥有广阔的视野。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #124
        0xC,
        (
            "这、这是我的亲事啊！？\x01",
            "哪里算是小事了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x101,
        (
            "#1016F好、好了好了……\x01",
            "两个人都冷静一下啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x102,
        "#1052F（这算是和好了吗……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x101,
        (
            "#1015F（嗯～很微妙……）\x02\x03",

            "#1016F（不过，算是恢复\x01",
            "以前的状态了吧？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3143")

    label("loc_2F7A")

    TurnDirection(0xD, 0xC, 400)

    ChrTalk(    #128
        0xD,
        (
            "嗯，确实我的立场\x01",
            "好像得到了理解……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xD,
        (
            "可是，小姐\x01",
            "还要具备不拘泥于\x01",
            "小事的态度才行……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xD, 400)

    ChrTalk(    #130
        0xC,
        "哎呀，拘泥也是当然的啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xC,
        (
            "自己的人生被人操纵，\x01",
            "没人会感到高兴的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xD,
        (
            "这种想法\x01",
            "太狭隘了，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xD,
        "呼，真没办法……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xD,
        (
            "看来，小姐的器量\x01",
            "也就是这种程度而已。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #135
        0xC,
        "你，你说什么！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x102,
        "#1052F（怎么吵起来了……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x101,
        (
            "#1016F（唔，嗯……\x01",
            "这两人真是老样子啊。）\x02\x03",

            "（不过，反正一直都是这样的\x01",
            "　这也算是关系好的证据吧。)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3143")

    OP_A2(0x1)
    OP_A2(0x2)
    OP_4B(0xC, 255)
    OP_4B(0xD, 255)
    Return()

    # Function_17_2BF8 end

    def Function_18_3152(): pass

    label("Function_18_3152")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_31A5")

    ChrTalk(    #138
        0xFE,
        (
            "结果，那个白影\x01",
            "到底是什么呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        (
            "反正就是带着\x01",
            "一副奇怪的面具。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3208")

    label("loc_31A5")

    OP_A2(0x0)

    ChrTalk(    #140
        0xFE,
        "哟，我听说啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        (
            "据说旧校舍\x01",
            "有可疑的家伙潜伏啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        (
            "我看到的白影\x01",
            "也是那家伙搞的鬼吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3208")

    TalkEnd(0xFE)
    Return()

    # Function_18_3152 end

    def Function_19_320C(): pass

    label("Function_19_320C")

    TalkBegin(0xFE)

    ChrTalk(    #143
        0xFE,
        "辛苦了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        (
            "以后的警备\x01",
            "请交给我们吧！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_320C end

    def Function_20_3240(): pass

    label("Function_20_3240")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3292")

    ChrTalk(    #145
        0xFE,
        "非常抱歉来迟了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        (
            "因为警备艇不能使用\x01",
            "行动起来很花时间。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_32B9")

    label("loc_3292")


    ChrTalk(    #147
        0xFE,
        (
            "非常抱歉来迟了。\x01",
            "警备由我们接手。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32B9")

    TalkEnd(0xFE)
    Return()

    # Function_20_3240 end

    def Function_21_32BD(): pass

    label("Function_21_32BD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_334D")

    ChrTalk(    #148
        0xFE,
        (
            "现在事件解决了\x01",
            "突然有点疑问……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        (
            "犯人们有使用\x01",
            "导力枪吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xFE,
        (
            "导力器都停了，\x01",
            "为何还能用枪呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        "唔～不可思议……\x02",
    )

    CloseMessageWindow()
    OP_A2(0xA)
    Jump("loc_3388")

    label("loc_334D")


    ChrTalk(    #152
        0xFE,
        (
            "导力器都停了，\x01",
            "为何还能用枪呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        "唔～不可思议……\x02",
    )

    CloseMessageWindow()

    label("loc_3388")

    TalkEnd(0xFE)
    Return()

    # Function_21_32BD end

    def Function_22_338C(): pass

    label("Function_22_338C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3399")
    Return()

    label("loc_3399")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_33AA")
    Call(0, 83)

    label("loc_33AA")

    EventBegin(0x0)
    OP_71(0x2, 0x10)
    OP_6F(0x21, 0)
    OP_70(0x21, 0x3C)
    Sleep(1000)
    Fade(1000)
    AddParty(0x4, 0xF9, 0xFF)
    OP_31(0x4, 0x0, 0x26)
    OP_31(0x4, 0xFE, 0x0)
    OP_41(0x4, 0x7F, 0xFF)
    OP_41(0x4, 0xFF, 0xFF)
    OP_41(0x4, 0x120, 0xFF)
    OP_41(0x4, 0x259, 0x0)
    OP_41(0x4, 0x2D4, 0x1)
    OP_41(0x4, 0x25B, 0x2)
    OP_35(0x4, 0x0)
    OP_35(0x4, 0x8C)
    OP_BB(0x4, 0x6, 0xFA)
    SetChrFlags(0xA, 0x40)
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0x105, 0x8)
    SetChrPos(0x101, 22270, 0, 46760, 91)
    SetChrPos(0xF7, 21650, 0, 45420, 84)
    SetChrPos(0x104, 20500, 0, 47120, 85)
    SetChrPos(0x127, 20100, 0, 46000, 85)
    SetChrPos(0x105, 22100, 0, 59170, 195)
    SetChrPos(0x8, 20980, 0, 58890, 171)
    SetChrPos(0x9, 22410, 0, 58760, 179)
    OP_6D(61060, 0, 55000, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(6110, 0)
    OP_6C(75000, 0)
    OP_6E(262, 0)
    StopSound(0x9470, 0x3D090, 0x0)
    OP_C8(0x200, 0x46, "C_PLAC06._CH", 0x1, 0x3E8)

    def lambda_34F4():
        OP_6D(21160, 0, 46450, 10000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_34F4)

    def lambda_350C():
        OP_6C(315000, 10000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_350C)
    Sleep(2000)
    StopSound(0x9470, 0x14C08, 0x1F40)

    def lambda_352E():
        OP_6B(3000, 8000)
        ExitThread()

    QueueWorkItem(0x1, 3, lambda_352E)

    def lambda_353E():
        OP_67(0, 8350, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_353E)
    Sleep(8000)

    ChrTalk(    #154
        0x104,
        (
            "#033F哦，这里就是王立学院吗。\x02\x03",

            "#035F即将绽放的花蕾们\x01",
            "洒下青春汗与泪的学舍……\x02\x03",

            "呵呵……\x01",
            "实在是太棒了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x127,
        (
            "#151F看来有很多\x01",
            "值得拍摄的对象呢～\x02\x03",

            "趁此机会要大拍特拍才行～\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF7, 0x104, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_365E")

    ChrTalk(    #156
        0x106,
        (
            "#551F#6P我说啊，我们只是\x01",
            "来调查幽灵骚动的啦。\x02\x03",

            "#552F明白吗，这件事？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36AA")

    label("loc_365E")


    ChrTalk(    #157
        0x103,
        (
            "#025F#6P唉……\x01",
            "完全忘记本来的目的了。\x02\x03",

            "#020F别忘了我们是来调查事件的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36AA")


    ChrTalk(    #158
        0x101,
        (
            "#1025F#5P不过，真是怀念啊……\x02\x03",

            "在这所学院\x01",
            "虽然只度过一周左右……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xF7, 0, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3757")

    ChrTalk(    #159
        0x106,
        (
            "#051F#6P不过，却是和朋友们\x01",
            "一起度过的难忘时光呢。\x02\x03",

            "不是还出演了\x01",
            "学院祭的戏剧吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37AD")

    label("loc_3757")


    ChrTalk(    #160
        0x103,
        (
            "#027F#6P呵呵，却是和朋友们\x01",
            "一起度过的难忘时光呢。\x02\x03",

            "不是还出演了\x01",
            "学院祭的戏剧吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37AD")


    ChrTalk(    #161
        0x127,
        (
            "#151F啊，我听奈尔前辈说了～\x02\x03",

            "小艾你们是骑士,\x01",
            "约修亚是公主对吧？\x02\x03",

            "#154F啊～啊，好想拍下照片啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #162
        0x104,
        (
            "#036F什么……那是真的吗！？\x02\x03",

            "#034F哦哦，竟然如此！\x01",
            "居然错过了约修亚的美态！\x02\x03",

            "无论如何也要找到他\x01",
            "让他再穿一次才行！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x104, 600)

    ChrTalk(    #163
        0x101,
        (
            "#1007F#4P唉，沉浸于感伤，\x01",
            "真是像傻瓜一样。\x02\x03",

            "#1015F这么说来，特蕾莎老师\x01",
            "说过现在是考试期间……\x02\x03",

            "还没结束吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x197, 0x0, 0x64)
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x127, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xF7, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_39AF():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_39AF)

    def lambda_39BD():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_39BD)

    def lambda_39CB():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_39CB)

    def lambda_39D9():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x127, 1, lambda_39D9)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #164
        0x101,
        "#1004F#5P基库！？\x02",
    )

    CloseMessageWindow()
    OP_6D(27230, 0, 48860, 1500)

    def lambda_3A14():
        OP_6D(21160, 0, 46450, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_3A14)
    OP_22(0x8C, 0x0, 0x64)
    SetChrPos(0xA, 36940, 6000, 46020, 90)
    ClearChrFlags(0xA, 0x80)
    OP_43(0xA, 0x1, 0x0, 0x2)
    OP_8E(0xA, 0x55F0, 0x7D0, 0xBCAC, 0x1770, 0x0)
    OP_22(0x197, 0x0, 0x64)
    OP_44(0xA, 0x1)
    OP_97(0xA, 0x56FE, 0xB6A8, 0xFFFA81C0, 0x1770, 0x1)
    OP_97(0xA, 0x56FE, 0xB6A8, 0xFFFE2B40, 0x1388, 0x1)
    OP_97(0xA, 0x56FE, 0xB6A8, 0xFFFF15A0, 0xBB8, 0x1)
    OP_8C(0x101, 135, 0)
    OP_43(0xA, 0x1, 0x0, 0x2)

    def lambda_3AB8():
        OP_8C(0xA, 90, 100)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_3AB8)
    OP_8F(0xA, 0x5708, 0x2BC, 0xB43C, 0x7D0, 0x0)
    Fade(500)
    OP_44(0xA, 0x1)
    SetChrFlags(0xA, 0x80)
    SetChrChipByIndex(0x101, 3)
    SetChrSubChip(0x101, 3)
    OP_0D()
    OP_8C(0xF7, 0, 400)
    SetChrSubChip(0x101, 5)
    OP_8C(0x104, 135, 400)

    ChrTalk(    #165
        0xA,
        "#311F#5P啾啾啾⊙\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x101,
        (
            "#1016F#2P啊哈哈……\x01",
            "虽然不明白你说什么，\x01",
            "不过好像在欢迎我们呢。\x02\x03",

            "#1006F好久不见，还好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xA,
        "#311F#5P啾～～㈱\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x105, 0x8)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)

    NpcTalk(    #168
        0x105,
        "女孩的声音",
        "#6P……艾丝蒂尔………\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrSubChip(0x101, 3)
    SetChrFlags(0x101, 0x20)
    TurnDirection(0x101, 0x105, 400)

    def lambda_3BF3():
        TurnDirection(0xF7, 0x105, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_3BF3)

    def lambda_3C01():
        TurnDirection(0x104, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3C01)

    def lambda_3C0F():
        TurnDirection(0x127, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x127, 1, lambda_3C0F)
    ClearChrFlags(0x101, 0x20)

    ChrTalk(    #169
        0x101,
        "#1025F#5P啊……\x02",
    )

    CloseMessageWindow()

    def lambda_3C37():
        OP_6D(21750, 0, 50070, 3000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_3C37)

    def lambda_3C4F():
        OP_67(0, 9280, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_3C4F)

    def lambda_3C67():
        OP_6C(328000, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_3C67)

    def lambda_3C77():
        OP_6B(2840, 3000)
        ExitThread()

    QueueWorkItem(0x1, 3, lambda_3C77)
    Fade(250)
    SetChrPos(0xA, 22710, 0, 46900, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    OP_22(0x8C, 0x0, 0x64)

    def lambda_3CB1():
        OP_8F(0xA, 0x6342, 0xD48, 0xC968, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_3CB1)
    OP_43(0xA, 0x1, 0x0, 0x2)

    def lambda_3CD3():
        OP_8E(0xFE, 0x5852, 0x0, 0xCC4C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3CD3)
    Sleep(1000)

    def lambda_3CF3():
        OP_8E(0xFE, 0x54B0, 0x0, 0xCFC6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3CF3)
    Sleep(300)

    def lambda_3D13():
        OP_8E(0xFE, 0x591A, 0x0, 0xD17E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3D13)
    WaitChrThread(0xA, 0x0)
    OP_8C(0xA, 270, 180)
    OP_8C(0xA, 180, 180)
    Sleep(250)
    OP_44(0xA, 0x1)
    SetChrChipByIndex(0xA, 4)
    SetChrSubChip(0xA, 0)
    WaitChrThread(0x9, 0x1)
    WaitChrThread(0x1, 0x0)
    WaitChrThread(0x1, 0x1)
    WaitChrThread(0x1, 0x2)
    WaitChrThread(0x1, 0x3)
    Sleep(500)

    ChrTalk(    #170
        0x101,
        (
            "#1025F#6P科洛丝……\x02\x03",

            "#1016F嘿嘿……诞辰庆典以来好久不见呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x105,
        (
            "#542F嗯……是啊。\x02\x03",

            "……那个……我……\x02\x03",

            "#049F…………我………………\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3DFB():

        label("loc_3DFB")

        TurnDirection(0xF7, 0x105, 0)
        OP_48()
        Jump("loc_3DFB")

    QueueWorkItem2(0xF7, 2, lambda_3DFB)

    def lambda_3E0C():

        label("loc_3E0C")

        TurnDirection(0x104, 0x105, 0)
        OP_48()
        Jump("loc_3E0C")

    QueueWorkItem2(0x104, 2, lambda_3E0C)

    def lambda_3E1D():

        label("loc_3E1D")

        TurnDirection(0x127, 0x105, 0)
        OP_48()
        Jump("loc_3E1D")

    QueueWorkItem2(0x127, 2, lambda_3E1D)

    def lambda_3E2E():
        OP_8E(0x105, 0x55F0, 0x0, 0xB810, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3E2E)
    Sleep(300)
    Fade(500)
    OP_6D(22200, 0, 48130, 0)
    OP_67(0, 9280, -10000, 0)
    OP_6B(2840, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)

    def lambda_3E90():
        OP_6D(22270, 0, 46760, 2000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_3E90)

    def lambda_3EA8():
        OP_67(0, 9280, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_3EA8)

    def lambda_3EC0():
        OP_8E(0xFE, 0x53A2, 0x0, 0xBEE6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3EC0)
    Sleep(300)

    def lambda_3EE0():
        OP_8E(0xFE, 0x5802, 0x0, 0xC01C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3EE0)
    WaitChrThread(0x105, 0x1)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 13)
    SetChrSubChip(0x101, 0)
    SetChrFlags(0x105, 0x80)
    OP_99(0x101, 0x0, 0x3, 0x7D0)
    OP_44(0xF7, 0x2)
    OP_44(0x104, 0x2)
    OP_44(0x127, 0x2)

    def lambda_3F29():

        label("loc_3F29")

        TurnDirection(0xF7, 0x101, 0)
        OP_48()
        Jump("loc_3F29")

    QueueWorkItem2(0xF7, 2, lambda_3F29)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #172
        0x101,
        (
            "#1025F哇哇……\x01",
            "怎么了科洛丝？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x105,
        (
            "#049F#6P对不起……\x01",
            "……真是对不起……\x02\x03",

            "艾丝蒂尔你们这么困难的时候，\x01",
            "我……什么也做不到……\x02\x03",

            "好讨厌自己力量不足……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x101,
        (
            "#1025F真是的……\x01",
            "别这么说嘛……\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x101, 0x4, 0x6, 0x5DC)
    Sleep(500)

    ChrTalk(    #175
        0x101,
        (
            "#1012F你这么为我们着想\x01",
            "我就很高兴了……\x02\x03",

            "约修亚\x01",
            "也一定是这样……\x02\x03",

            "#1017F总之……\x01",
            "能再见面就很开心了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x105,
        (
            "#047F#6P嗯……我也是……\x02\x03",

            "#048F能这样再会\x01",
            "就要感谢空之女神了。\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrFlags(0x101, 0x800)
    SetChrChipByIndex(0x101, 13)
    SetChrSubChip(0x101, 7)
    OP_0D()
    Sleep(500)

    ChrTalk(    #177
        0x8,
        (
            "#649F#2P真是的～\x01",
            "你们两个太夸张啦。\x02\x03",

            "#648F好久不见呢，艾丝蒂尔。\x01",
            "诞辰庆典见面以来都没见过了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x101,
        (
            "#1017F嗯，是啊。\x02\x03",

            "汉斯也是……好久不见。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x9,
        (
            "#730F#6P啊啊……是啊。\x02\x03",

            "虽然有很多话想说……\x01",
            "现在还是先推迟一下吧。\x02\x03",

            "你们是为游击士的工作来的吧？\x01",
            "我带你们去校长那里吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T2510   ._SN", 114, 0, 0)
    IdleLoop()
    Return()

    # Function_22_338C end

    def Function_23_4217(): pass

    label("Function_23_4217")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #180
        (
            "\x07\x05现在是期末考试中，\x01",
            "校外人员不允许进入。\x01",
            "　　　　　　　　　　杰尼丝王立学院\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_23_4217 end

    def Function_24_4292(): pass

    label("Function_24_4292")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4478")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x404, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_42B5")
    Call(0, 80)
    Jump("loc_4472")

    label("loc_42B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43FC")
    OP_A2(0x2017)
    EventBegin(0x0)
    Fade(500)
    OP_6D(65860, 0, 27990, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(122000, 0)
    OP_6E(262, 0)
    OP_6D(65860, 0, 27990, 0)
    SetChrPos(0x102, 65860, 0, 27990, 90)
    SetChrSubChip(0x102, 0)
    OP_0D()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #181
        "\x07\x05后门上了锁。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #182
        0x102,
        (
            "#1043F（这前面是旧校舍吗……）\x02\x03",

            "#1040F（……是啊，慎重起见……）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #183
        (
            "\x07\x05约修亚取出工具\x01",
            "快速插入钥匙孔。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x73, 0x0, 0x50)
    Sleep(1000)
    Call(0, 76)
    EventEnd(0x0)
    Jump("loc_4472")

    label("loc_43FC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #184
        "\x07\x05后门的锁被打开了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #185
        0x102,
        (
            "#1035F（现在没必要往前……）\x02\x03",

            "#1042F（回学院内探索吧。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4472")

    TalkEnd(0xFF)
    Jump("loc_44BF")

    label("loc_4478")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #186
        "\x07\x05后门上了锁。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)

    label("loc_44BF")

    Return()

    # Function_24_4292 end

    def Function_25_44C0(): pass

    label("Function_25_44C0")

    EventBegin(0x0)
    FadeToBright(1000, 0)
    SetChrPos(0x101, 22990, 250, 66860, 176)
    SetChrPos(0x105, 22040, 250, 66860, 175)
    OP_6D(22280, 480, 67450, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #187
        0x101,
        (
            "#1004F啊……\x01",
            "已经这么晚了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #188
        0x105,
        (
            "#542F已经向学生们打听过了，\x01",
            "暂时回学生会室吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #189
        0x101,
        (
            "#1006F嗯，是啊。\x02\x03",

            "核对大家的情报后\x01",
            "能发现什么就好了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1221)
    OP_28(0x83, 0x1, 0x40)
    EventEnd(0x0)
    Return()

    # Function_25_44C0 end

    def Function_26_45F1(): pass

    label("Function_26_45F1")

    EventBegin(0x0)
    FadeToBright(1000, 0)
    SetChrPos(0x101, 40810, 250, 73170, 271)
    SetChrPos(0x105, 40760, 250, 74250, 287)
    OP_6D(41600, 460, 73930, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #190
        0x101,
        (
            "#1004F啊……\x01",
            "已经这么晚了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #191
        0x105,
        (
            "#542F已经向学生们打听过了，\x01",
            "暂时回学生会室吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #192
        0x101,
        (
            "#1006F嗯，是啊。\x02\x03",

            "核对大家的情报后\x01",
            "能发现什么就好了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1221)
    OP_28(0x83, 0x1, 0x40)
    EventEnd(0x0)
    Return()

    # Function_26_45F1 end

    def Function_27_4722(): pass

    label("Function_27_4722")

    EventBegin(0x0)
    FadeToBright(1000, 0)
    SetChrPos(0x101, 52040, 0, 65500, 258)
    SetChrPos(0x105, 52280, 0, 64660, 252)
    OP_6D(52780, 0, 65680, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #193
        0x101,
        (
            "#1004F啊……\x01",
            "已经这么晚了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #194
        0x105,
        (
            "#542F已经向学生们打听过了，\x01",
            "暂时回学生会室吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #195
        0x101,
        (
            "#1006F嗯，是啊。\x02\x03",

            "核对大家的情报后\x01",
            "能发现什么就好了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1221)
    OP_28(0x83, 0x1, 0x40)
    EventEnd(0x0)
    Return()

    # Function_27_4722 end

    def Function_28_4853(): pass

    label("Function_28_4853")

    EventBegin(0x0)
    FadeToBright(1000, 0)
    SetChrPos(0x101, 51910, 0, 61530, 268)
    SetChrPos(0x105, 52160, 0, 62400, 253)
    OP_6D(52910, 0, 61210, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(111000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #196
        0x101,
        (
            "#1004F啊……\x01",
            "已经这么晚了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #197
        0x105,
        (
            "#542F已经向学生们打听过了，\x01",
            "暂时回学生会室吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #198
        0x101,
        (
            "#1006F嗯，是啊。\x02\x03",

            "核对大家的情报后\x01",
            "能发现什么就好了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1221)
    OP_28(0x83, 0x1, 0x40)
    EventEnd(0x0)
    Return()

    # Function_28_4853 end

    def Function_29_4984(): pass

    label("Function_29_4984")

    EventBegin(0x0)
    FadeToBright(1000, 0)
    SetChrPos(0x101, 46730, 0, 45410, 277)
    SetChrPos(0x105, 47060, 0, 46350, 262)
    OP_6D(47100, 0, 45890, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #199
        0x101,
        (
            "#1004F啊……\x01",
            "已经这么晚了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #200
        0x105,
        (
            "#542F已经向学生们打听过了，\x01",
            "暂时回学生会室吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #201
        0x101,
        (
            "#1006F嗯，是啊。\x02\x03",

            "核对大家的情报后\x01",
            "能发现什么就好了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1221)
    OP_28(0x83, 0x1, 0x40)
    EventEnd(0x0)
    Return()

    # Function_29_4984 end

    def Function_30_4AB5(): pass

    label("Function_30_4AB5")

    EventBegin(0x0)
    FadeToBright(1000, 0)
    SetChrPos(0x101, 51870, 0, 30080, 275)
    SetChrPos(0x105, 52310, 0, 29300, 257)
    OP_6D(52390, 0, 30630, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(53000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #202
        0x101,
        (
            "#1004F啊……\x01",
            "已经这么晚了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #203
        0x105,
        (
            "#542F已经向学生们打听过了，\x01",
            "暂时回学生会室吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #204
        0x101,
        (
            "#1006F嗯，是啊。\x02\x03",

            "核对大家的情报后\x01",
            "能发现什么就好了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1221)
    OP_28(0x83, 0x1, 0x40)
    EventEnd(0x0)
    Return()

    # Function_30_4AB5 end

    def Function_31_4BE6(): pass

    label("Function_31_4BE6")

    EventBegin(0x0)
    ClearMapFlags(0x10)
    OP_6D(72780, 0, 23250, 0)
    OP_67(0, 6540, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(40000, 0)
    OP_6E(439, 0)
    SetChrFlags(0x13, 0x20)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x13, 0x1)
    SetChrPos(0x13, 71000, 7000, 17030, 180)
    SetChrChipByIndex(0x13, 14)
    SetChrSubChip(0x13, 0)

    def lambda_4C5A():

        label("loc_4C5A")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_4C5A")

    QueueWorkItem2(0x13, 1, lambda_4C5A)
    OP_9F(0x13, 0xFF, 0xFF, 0xFF, 0xB4, 0x0)
    OP_A0(0x13, 0xB4, 0xB4, 0xB4, 0x0)
    FadeToBright(2000, 0)

    def lambda_4C8B():
        OP_6C(45000, 8000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_4C8B)
    OP_97(0x13, 0x10D88, 0x4286, 0xFFFA81C0, 0xBB8, 0x1)
    OP_97(0x13, 0x10D88, 0x4286, 0xFFFA81C0, 0xBB8, 0x1)
    OP_97(0x13, 0x10D88, 0x4286, 0xFFFEA070, 0x7D0, 0x1)
    Sleep(300)
    OP_8C(0x13, 90, 1000)
    OP_8C(0x13, 360, 1000)
    OP_8C(0x13, 270, 1000)
    Sleep(300)
    OP_44(0x0, 0x1)
    OP_44(0x0, 0x2)

    def lambda_4D01():
        OP_6D(71780, 0, 23250, 2000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4D01)

    def lambda_4D19():
        OP_6B(2700, 2000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_4D19)

    def lambda_4D29():
        OP_96(0x13, 0x101C6, 0x1388, 0x4286, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_4D29)
    WaitChrThread(0x13, 0x2)
    SetChrChipByIndex(0x13, 15)
    SetChrSubChip(0x13, 0)
    WaitChrThread(0x0, 0x1)
    Sleep(500)
    OP_44(0x13, 0x0)
    OP_44(0x13, 0x1)
    OP_44(0x13, 0x2)
    SetChrFlags(0x13, 0x2)
    SetChrChipByIndex(0x13, 21)
    SetChrSubChip(0x13, 0)
    Sleep(100)
    SetChrSubChip(0x13, 8)
    Sleep(100)
    SetChrSubChip(0x13, 16)
    Sleep(100)
    SetChrSubChip(0x13, 24)
    Sleep(100)
    SetChrSubChip(0x13, 32)
    Sleep(100)
    SetChrSubChip(0x13, 40)
    Sleep(100)
    SetChrSubChip(0x13, 48)
    Sleep(100)
    SetChrSubChip(0x13, 56)
    Sleep(100)
    SetChrSubChip(0x13, 64)
    Sleep(100)
    SetChrSubChip(0x13, 72)
    Sleep(1000)
    SetChrChipByIndex(0x13, 14)
    SetChrSubChip(0x13, 0)
    ClearChrFlags(0x13, 0x2)
    OP_8C(0x13, 90, 600)

    def lambda_4DF0():
        OP_6D(74780, 0, 23250, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4DF0)

    def lambda_4E08():
        OP_8E(0xFE, 0x124F8, 0x1B58, 0x4F4C, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_4E08)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x10F1)
    SetMapFlags(0x2000000)
    NewScene("ED6_DT21/T2511   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_31_4BE6 end

    def Function_32_4E3F(): pass

    label("Function_32_4E3F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4E54")
    OP_99(0xFE, 0x0, 0x7, 0x1F4)
    Jump("Function_32_4E3F")

    label("loc_4E54")

    Return()

    # Function_32_4E3F end

    def Function_33_4E55(): pass

    label("Function_33_4E55")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x29, 0x80)
    SetChrFlags(0x2A, 0x80)
    SetChrFlags(0x2B, 0x80)
    SetChrFlags(0x2C, 0x80)
    OP_D2(0x26000D, 0x260012, 0x20)
    SetChrChipByIndex(0x14, 32)
    SetChrChipByIndex(0x15, 32)
    SetChrChipByIndex(0x16, 32)
    SetChrChipByIndex(0x17, 32)
    OP_43(0x14, 0x1, 0x0, 0x22)
    OP_43(0x15, 0x1, 0x0, 0x23)
    OP_43(0x16, 0x1, 0x0, 0x24)
    OP_43(0x17, 0x1, 0x0, 0x25)
    OP_43(0x18, 0x1, 0x0, 0x26)
    OP_43(0x19, 0x1, 0x0, 0x27)
    OP_43(0x1A, 0x1, 0x0, 0x28)
    OP_43(0x1B, 0x1, 0x0, 0x29)
    OP_6D(45900, 0, 46020, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2960, 0)
    OP_6C(45000, 0)
    OP_6E(315, 0)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_4F3B():
        OP_6D(15710, 0, 46020, 10000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4F3B)

    def lambda_4F53():
        OP_6C(90000, 10000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_4F53)
    Sleep(9000)
    SetMapFlags(0x2000000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/R2301   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_33_4E55 end

    def Function_34_4F7F(): pass

    label("Function_34_4F7F")

    SetChrPos(0xFE, 46550, 0, 54620, 0)
    ClearChrFlags(0xFE, 0x80)

    label("loc_4F95")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_500C")
    OP_8C(0xFE, 315, 400)
    Sleep(600)
    OP_8C(0xFE, 45, 400)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0xB34C, 0x0, 0xC026, 0x7D0, 0x0)
    Sleep(500)
    OP_8C(0xFE, 270, 400)
    Sleep(600)
    OP_8C(0xFE, 180, 400)
    Sleep(500)
    OP_8C(0xFE, 0, 400)
    OP_8E(0xFE, 0xB5D6, 0x0, 0xD55C, 0x7D0, 0x0)
    Jump("loc_4F95")

    label("loc_500C")

    Return()

    # Function_34_4F7F end

    def Function_35_500D(): pass

    label("Function_35_500D")

    SetChrPos(0xFE, 45710, 0, 44810, 45)
    ClearChrFlags(0xFE, 0x80)
    Sleep(200)

    label("loc_5028")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_50A4")
    Sleep(600)
    OP_8C(0xFE, 315, 400)
    Sleep(500)
    OP_8C(0xFE, 45, 400)
    Sleep(600)
    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0xB608, 0x0, 0x7C2E, 0x7D0, 0x0)
    Sleep(500)
    OP_8C(0xFE, 135, 400)
    Sleep(600)
    OP_8C(0xFE, 225, 400)
    Sleep(500)
    OP_8C(0xFE, 0, 400)
    OP_8E(0xFE, 0xB28E, 0x0, 0xAF0A, 0x7D0, 0x0)
    Jump("loc_5028")

    label("loc_50A4")

    Return()

    # Function_35_500D end

    def Function_36_50A5(): pass

    label("Function_36_50A5")

    SetChrPos(0xFE, 21070, 0, 38420, 0)
    ClearChrFlags(0xFE, 0x80)

    label("loc_50BB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5137")
    OP_8E(0xFE, 0x524E, 0x0, 0xD28C, 0x7D0, 0x0)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    Sleep(500)
    OP_8C(0xFE, 0, 400)
    Sleep(600)
    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0x524E, 0x0, 0x9614, 0x7D0, 0x0)
    Sleep(500)
    OP_8C(0xFE, 270, 400)
    Sleep(600)
    OP_8C(0xFE, 90, 400)
    Sleep(500)
    OP_8C(0xFE, 0, 400)
    Jump("loc_50BB")

    label("loc_5137")

    Return()

    # Function_36_50A5 end

    def Function_37_5138(): pass

    label("Function_37_5138")

    SetChrPos(0xFE, 22990, 0, 54810, 180)
    ClearChrFlags(0xFE, 0x80)
    Sleep(200)

    label("loc_5153")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_51CF")
    OP_8E(0xFE, 0x59CE, 0x0, 0x9EE8, 0x7D0, 0x0)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    Sleep(600)
    OP_8C(0xFE, 180, 400)
    Sleep(600)
    OP_8C(0xFE, 0, 400)
    OP_8E(0xFE, 0x59CE, 0x0, 0xD61A, 0x7D0, 0x0)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    Sleep(500)
    OP_8C(0xFE, 270, 400)
    Sleep(600)
    OP_8C(0xFE, 180, 400)
    Jump("loc_5153")

    label("loc_51CF")

    Return()

    # Function_37_5138 end

    def Function_38_51D0(): pass

    label("Function_38_51D0")

    OP_43(0xFE, 0x0, 0x0, 0x2)
    Sleep(200)
    SetChrPos(0xFE, 31840, -1650, 57320, 0)
    ClearChrFlags(0xFE, 0x80)

    label("loc_51F2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5304")
    OP_8C(0xFE, 270, 400)
    SetChrChipByIndex(0xFE, 24)
    OP_8E(0xFE, 0x75BC, 0xFFFFF894, 0xDE80, 0x9C4, 0x0)
    SetChrPos(0xFE, 30140, -1650, 56960, 270)
    SetChrChipByIndex(0xFE, 23)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    SetChrChipByIndex(0xFE, 24)
    OP_8E(0xFE, 0x7602, 0xFFFFF894, 0xC5DA, 0x9C4, 0x0)
    SetChrPos(0xFE, 30210, -1550, 50650, 180)
    SetChrChipByIndex(0xFE, 23)
    OP_8C(0xFE, 225, 400)
    Sleep(800)
    OP_8C(0xFE, 135, 400)
    SetChrChipByIndex(0xFE, 24)
    OP_8E(0xFE, 0x80FC, 0xFFFFF894, 0xBE14, 0x9C4, 0x0)
    SetChrPos(0xFE, 33020, -1700, 48660, 135)
    SetChrChipByIndex(0xFE, 23)
    Sleep(500)
    OP_8C(0xFE, 0, 400)
    SetChrChipByIndex(0xFE, 24)
    OP_8E(0xFE, 0x7C60, 0xFFFFF894, 0xDFE8, 0x9C4, 0x0)
    SetChrPos(0xFE, 31840, -1650, 57320, 0)
    SetChrChipByIndex(0xFE, 23)
    Sleep(500)
    OP_8C(0xFE, 225, 400)
    Sleep(800)
    OP_8C(0xFE, 315, 400)
    Jump("loc_51F2")

    label("loc_5304")

    Return()

    # Function_38_51D0 end

    def Function_39_5305(): pass

    label("Function_39_5305")

    OP_43(0xFE, 0x0, 0x0, 0x2)
    SetChrPos(0xFE, 33990, -1650, 34800, 135)
    ClearChrFlags(0xFE, 0x80)

    label("loc_5322")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5445")
    Sleep(500)
    OP_8C(0xFE, 270, 400)
    SetChrChipByIndex(0xFE, 24)
    OP_8E(0xFE, 0x78D2, 0xFFFFF894, 0x8746, 0x9C4, 0x0)
    SetChrPos(0xFE, 30930, -1650, 34630, 270)
    SetChrChipByIndex(0xFE, 23)
    Sleep(800)
    OP_8C(0xFE, 0, 400)
    SetChrChipByIndex(0xFE, 24)
    OP_8E(0xFE, 0x747C, 0xFFFFF894, 0xABD6, 0x9C4, 0x0)
    SetChrPos(0xFE, 29820, -1650, 43990, 0)
    SetChrChipByIndex(0xFE, 23)
    OP_8C(0xFE, 315, 400)
    Sleep(500)
    OP_8C(0xFE, 270, 400)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    SetChrChipByIndex(0xFE, 24)
    OP_8E(0xFE, 0x8552, 0xFFFFF894, 0xA83E, 0x9C4, 0x0)
    SetChrPos(0xFE, 34130, -1650, 43070, 90)
    SetChrChipByIndex(0xFE, 23)
    Sleep(800)
    OP_8C(0xFE, 180, 400)
    SetChrChipByIndex(0xFE, 24)
    OP_8E(0xFE, 0x84C6, 0xFFFFF894, 0x87F0, 0x9C4, 0x0)
    SetChrPos(0xFE, 33990, -1650, 34800, 180)
    SetChrChipByIndex(0xFE, 23)
    Sleep(500)
    OP_8C(0xFE, 315, 400)
    Sleep(800)
    OP_8C(0xFE, 135, 400)
    Jump("loc_5322")

    label("loc_5445")

    Return()

    # Function_39_5305 end

    def Function_40_5446(): pass

    label("Function_40_5446")

    OP_43(0xFE, 0x0, 0x0, 0x2)
    SetChrPos(0xFE, 40320, -2000, 48550, 90)
    ClearChrFlags(0xFE, 0x80)
    Sleep(800)

    label("loc_5468")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5563")
    OP_8C(0xFE, 270, 400)
    SetChrChipByIndex(0xFE, 26)
    OP_8E(0xFE, 0x933A, 0xFFFFF830, 0xB860, 0xBB8, 0x0)
    SetChrChipByIndex(0xFE, 25)
    OP_8C(0xFE, 0, 400)
    Sleep(500)
    SetChrChipByIndex(0xFE, 26)
    OP_8E(0xFE, 0x9038, 0xFFFFF830, 0xCEC2, 0xBB8, 0x0)
    SetChrChipByIndex(0xFE, 25)
    OP_8C(0xFE, 45, 400)
    Sleep(800)
    OP_8C(0xFE, 0, 400)
    SetChrChipByIndex(0xFE, 26)
    OP_8E(0xFE, 0x8C78, 0xFFFFF830, 0xDC50, 0xBB8, 0x0)
    SetChrChipByIndex(0xFE, 25)
    SetChrFlags(0xFE, 0x2)
    Sleep(1000)
    ClearChrFlags(0xFE, 0x2)
    OP_8C(0xFE, 135, 400)
    SetChrChipByIndex(0xFE, 26)
    OP_8E(0xFE, 0x9A42, 0xFFFFF830, 0xD250, 0xBB8, 0x0)
    SetChrChipByIndex(0xFE, 25)
    Sleep(800)
    OP_8C(0xFE, 180, 400)
    SetChrChipByIndex(0xFE, 26)
    OP_8E(0xFE, 0x9D80, 0xFFFFF830, 0xBDA6, 0xBB8, 0x0)
    SetChrChipByIndex(0xFE, 25)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    Sleep(500)
    Jump("loc_5468")

    label("loc_5563")

    Return()

    # Function_40_5446 end

    def Function_41_5564(): pass

    label("Function_41_5564")

    OP_43(0xFE, 0x0, 0x0, 0x2)
    SetChrPos(0xFE, 36800, -2000, 41930, 315)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x2)
    Sleep(1000)
    ClearChrFlags(0xFE, 0x2)

    label("loc_5590")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_569A")
    OP_8C(0xFE, 90, 400)
    SetChrChipByIndex(0xFE, 26)
    OP_8E(0xFE, 0x9B3C, 0xFFFFF830, 0xA78A, 0xBB8, 0x0)
    SetChrChipByIndex(0xFE, 25)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    SetChrChipByIndex(0xFE, 26)
    SetChrFlags(0xFE, 0x2)
    Sleep(1000)
    ClearChrFlags(0xFE, 0x2)
    OP_8E(0xFE, 0x99A2, 0xFFFFF830, 0x8E3A, 0xBB8, 0x0)
    SetChrChipByIndex(0xFE, 25)
    OP_8C(0xFE, 270, 400)
    Sleep(800)
    OP_8C(0xFE, 215, 400)
    SetChrChipByIndex(0xFE, 26)
    OP_8E(0xFE, 0x8CA0, 0xFFFFF830, 0x875A, 0xBB8, 0x0)
    SetChrChipByIndex(0xFE, 25)
    SetChrFlags(0xFE, 0x2)
    Sleep(1000)
    ClearChrFlags(0xFE, 0x2)
    OP_8C(0xFE, 90, 400)
    SetChrChipByIndex(0xFE, 26)
    OP_8E(0xFE, 0x9560, 0xFFFFF830, 0x85B6, 0xBB8, 0x0)
    SetChrChipByIndex(0xFE, 25)
    Sleep(800)
    OP_8C(0xFE, 180, 400)
    SetChrChipByIndex(0xFE, 26)
    OP_8E(0xFE, 0x8FC0, 0xFFFFF830, 0xA3CA, 0xBB8, 0x0)
    SetChrChipByIndex(0xFE, 25)
    Sleep(500)
    OP_8C(0xFE, 315, 400)
    Sleep(500)
    Jump("loc_5590")

    label("loc_569A")

    Return()

    # Function_41_5564 end

    def Function_42_569B(): pass

    label("Function_42_569B")

    EventBegin(0x0)
    OP_6D(15700, 0, 45080, 0)
    OP_67(0, 11040, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(132000, 0)
    OP_6E(446, 0)
    SetChrPos(0x102, 10480, 0, 580, 0)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x29, 0x80)
    SetChrFlags(0x2A, 0x80)
    SetChrFlags(0x2B, 0x80)
    SetChrFlags(0x2C, 0x80)
    OP_D2(0x270019, 0x27001D, 0x1D)
    OP_D2(0x2600FC, 0x260101, 0x1E)
    OP_D2(0x26000D, 0x260012, 0x1F)
    SetChrChipByIndex(0x14, 31)
    SetChrChipByIndex(0x15, 31)
    SetChrChipByIndex(0x16, 31)
    SetChrChipByIndex(0x17, 31)
    OP_43(0x14, 0x1, 0x0, 0x22)
    OP_43(0x15, 0x1, 0x0, 0x23)
    OP_43(0x16, 0x1, 0x0, 0x24)
    OP_43(0x17, 0x1, 0x0, 0x25)
    OP_43(0x18, 0x1, 0x0, 0x26)
    OP_43(0x19, 0x1, 0x0, 0x27)
    OP_43(0x1A, 0x1, 0x0, 0x28)
    OP_43(0x1B, 0x1, 0x0, 0x29)
    OP_C8(0x200, 0x46, "C_PLAC06._CH", 0x1, 0x3E8)
    FadeToBright(1000, 0)

    def lambda_57A6():
        OP_6D(13720, 0, 10560, 6000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_57A6)

    def lambda_57BE():
        OP_67(0, 10100, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_57BE)

    def lambda_57D6():
        OP_6C(143000, 6000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_57D6)

    def lambda_57E6():
        OP_6E(296, 6000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_57E6)

    def lambda_57F6():
        OP_6B(2570, 6000)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_57F6)
    Sleep(4500)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    OP_8F(0x102, 0x2FF8, 0x0, 0x22A6, 0x1770, 0x0)
    OP_8C(0x102, 45, 400)
    SetChrChipByIndex(0x102, 30)
    SetChrSubChip(0x102, 1)
    WaitChrThread(0x102, 0x1)

    def lambda_585D():
        OP_6D(15230, 0, 13640, 2000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_585D)

    def lambda_5875():
        OP_6C(179000, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5875)
    SetChrSubChip(0x102, 1)
    Sleep(300)
    SetChrSubChip(0x102, 0)
    OP_22(0x23B, 0x0, 0x64)
    SetChrFlags(0x102, 0x4)
    OP_7D(0x0, 0x102, 0x28, 0x1F4)
    OP_96(0x102, 0x35DE, 0xD48, 0x2C56, 0x1194, 0x1770)
    OP_22(0xA4, 0x0, 0x64)
    SetChrSubChip(0x102, 1)
    Sleep(100)
    SetChrSubChip(0x102, 0)
    OP_22(0x23B, 0x0, 0x64)
    OP_96(0x102, 0x3C32, 0x0, 0x3610, 0x5DC, 0x1770)
    SetChrSubChip(0x102, 1)
    OP_22(0xA4, 0x0, 0x64)
    OP_7D(0x1, 0x102, 0x0, 0x0)
    ClearChrFlags(0x102, 0x4)
    WaitChrThread(0x102, 0x1)
    Sleep(500)

    ChrTalk(    #205
        0x102,
        "#1035F……………………………\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x102, 0)
    OP_0D()

    def lambda_5940():
        OP_6D(16090, 0, 24680, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5940)
    OP_8E(0x102, 0x3F48, 0x0, 0x5FC8, 0xBB8, 0x0)
    Fade(250)
    SetChrChipByIndex(0x102, 29)
    OP_8C(0x102, 45, 0)
    OP_0D()
    Sleep(1000)
    OP_D2(0x26000D, 0x260012, 0x20)
    SetChrChipByIndex(0x14, 32)
    SetChrChipByIndex(0x15, 32)
    OP_43(0x14, 0x1, 0x0, 0x2B)
    OP_43(0x15, 0x1, 0x0, 0x2C)

    def lambda_59A5():
        OP_6D(21840, 0, 27280, 4000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_59A5)

    def lambda_59BD():
        OP_6B(2910, 4000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_59BD)

    def lambda_59CD():
        OP_6C(153000, 4000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_59CD)
    OP_6E(301, 4000)
    Sleep(3000)
    Fade(500)
    OP_6D(16090, 0, 24680, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(166000, 0)
    OP_6E(288, 0)
    OP_44(0x14, 0x1)
    OP_44(0x15, 0x1)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    OP_0D()
    Sleep(300)

    ChrTalk(    #206
        0x102,
        (
            "#1043F（……看来移动到\x01",
            "  建筑物背后比较好。）\x02\x03",

            "#1042F（之后只要掌握建筑物里的人质\x01",
            "  和大体的敌方战力分布……）\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x102, 65535)
    OP_8C(0x102, 180, 0)
    OP_0D()

    def lambda_5ACB():
        OP_6D(16500, 0, 21880, 2000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5ACB)

    def lambda_5AE3():
        OP_6C(151000, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5AE3)
    OP_8E(0x102, 0x4060, 0x0, 0x5546, 0x7D0, 0x0)
    OP_8C(0x102, 90, 400)
    WaitChrThread(0x102, 0x1)

    def lambda_5B13():
        OP_6E(241, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5B13)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T2512   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_42_569B end

    def Function_43_5B3F(): pass

    label("Function_43_5B3F")

    SetChrPos(0xFE, 20980, 0, 38990, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x51F4, 0x0, 0x6E00, 0x7D0, 0x0)
    OP_8E(0xFE, 0x81F6, 0x0, 0x6E00, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_43_5B3F end

    def Function_44_5B83(): pass

    label("Function_44_5B83")

    SetChrPos(0xFE, 30910, 0, 29060, 270)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x59EC, 0x0, 0x7184, 0x7D0, 0x0)
    OP_8E(0xFE, 0x59EC, 0x0, 0x9F56, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_44_5B83 end

    def Function_45_5BC7(): pass

    label("Function_45_5BC7")

    EventBegin(0x0)
    OP_6D(16500, 0, 21880, 0)
    OP_6C(151000, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6E(288, 0)
    SetChrPos(0x102, 16480, 0, 21830, 90)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #207
        0x102,
        (
            "#1035F（男子宿舍内敌兵两名……）\x02\x03",

            "#1040F（就这样先检查一次\x01",
            "  全部建筑物吧……）\x02",
        )
    )

    CloseMessageWindow()
    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    OP_65(0x5, 0x1)
    OP_65(0x6, 0x1)
    OP_65(0x7, 0x1)
    OP_65(0x8, 0x1)
    OP_65(0x9, 0x1)
    OP_65(0xA, 0x1)
    OP_65(0xB, 0x1)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_45_5BC7 end

    def Function_46_5CAB(): pass

    label("Function_46_5CAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 3)), scpexpr(EXPR_END)), "loc_5DE9")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_57(0xC8, 0x14, 0xC, "#5C再看一次里面吗？")
    OP_CC(0x0, 0x0, 0xA, 0xA, 0x0)
    OP_CC(0x1, 0x0, "【是】")
    OP_CC(0x1, 0x0, "【否】")
    OP_CC(0x2, 0x0)
    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_DA()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5D33"),
        (1, "loc_5DD7"),
        (SWITCH_DEFAULT, "loc_5DE6"),
    )


    label("loc_5D33")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5D78")
    Fade(500)
    SetChrPos(0x102, 16480, 0, 21830, 90)
    OP_6D(16480, 0, 21830, 0)
    OP_6C(150000, 0)
    OP_A3(0x2030)
    OP_0D()
    Jump("loc_5DA3")

    label("loc_5D78")

    Fade(500)
    SetChrPos(0x102, 16480, 0, 21830, 90)
    OP_6D(16480, 0, 21830, 0)
    OP_A2(0x2030)
    OP_0D()

    label("loc_5DA3")


    def lambda_5DA9():
        OP_6E(241, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5DA9)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T2512   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_5DE6")

    label("loc_5DD7")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jump("loc_5DE6")

    label("loc_5DE6")

    Jump("loc_5E93")

    label("loc_5DE9")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5E2E")
    Fade(500)
    SetChrPos(0x102, 16480, 0, 21830, 90)
    OP_6D(16480, 0, 21830, 0)
    OP_6C(150000, 0)
    OP_A3(0x2030)
    OP_0D()
    Jump("loc_5E62")

    label("loc_5E2E")

    Fade(500)
    SetChrPos(0x102, 16480, 0, 21830, 90)
    OP_6D(16480, 0, 21830, 0)
    OP_6C(30000, 0)
    OP_A2(0x2030)
    OP_0D()

    label("loc_5E62")


    def lambda_5E68():
        OP_6E(241, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5E68)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T2512   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_5E93")

    TalkEnd(0xFF)
    Return()

    # Function_46_5CAB end

    def Function_47_5E97(): pass

    label("Function_47_5E97")

    EventBegin(0x0)
    OP_6D(16480, 0, 21830, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6E(262, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5EE1")
    OP_6C(150000, 0)
    Jump("loc_5EEA")

    label("loc_5EE1")

    OP_6C(30000, 0)

    label("loc_5EEA")

    SetChrPos(0x102, 16480, 0, 21830, 90)
    FadeToBright(1000, 0)
    OP_0D()
    Call(0, 76)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_47_5E97 end

    def Function_48_5F11(): pass

    label("Function_48_5F11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 4)), scpexpr(EXPR_END)), "loc_6055")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_57(0xC8, 0x14, 0xC, "#5C再看一次里面吗？")
    OP_CC(0x0, 0x0, 0xA, 0xA, 0x0)
    OP_CC(0x1, 0x0, "【是】")
    OP_CC(0x1, 0x0, "【否】")
    OP_CC(0x2, 0x0)
    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_DA()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5F99"),
        (1, "loc_6043"),
        (SWITCH_DEFAULT, "loc_6052"),
    )


    label("loc_5F99")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5FDE")
    Fade(500)
    SetChrPos(0x102, 16490, 0, 16250, 90)
    OP_6D(16490, 0, 16250, 0)
    OP_6C(150000, 0)
    OP_A3(0x2030)
    OP_0D()
    Jump("loc_6012")

    label("loc_5FDE")

    Fade(500)
    SetChrPos(0x102, 16490, 0, 16250, 90)
    OP_6D(16490, 0, 16250, 0)
    OP_6C(30000, 0)
    OP_A2(0x2030)
    OP_0D()

    label("loc_6012")


    def lambda_6018():
        OP_6E(241, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6018)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F2)
    NewScene("ED6_DT21/T2512   ._SN", 107, 0, 0)
    IdleLoop()

    label("loc_6043")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jump("loc_6052")

    label("loc_6052")

    Jump("loc_60FF")

    label("loc_6055")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_609A")
    Fade(500)
    SetChrPos(0x102, 16490, 0, 16250, 90)
    OP_6D(16490, 0, 16250, 0)
    OP_6C(150000, 0)
    OP_A3(0x2030)
    OP_0D()
    Jump("loc_60CE")

    label("loc_609A")

    Fade(500)
    SetChrPos(0x102, 16490, 0, 16250, 90)
    OP_6D(16490, 0, 16250, 0)
    OP_6C(30000, 0)
    OP_A2(0x2030)
    OP_0D()

    label("loc_60CE")


    def lambda_60D4():
        OP_6E(241, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_60D4)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F2)
    NewScene("ED6_DT21/T2512   ._SN", 107, 0, 0)
    IdleLoop()

    label("loc_60FF")

    TalkEnd(0xFF)
    Return()

    # Function_48_5F11 end

    def Function_49_6103(): pass

    label("Function_49_6103")

    EventBegin(0x0)
    OP_6D(16490, 0, 16250, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6E(262, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_614D")
    OP_6C(150000, 0)
    Jump("loc_6156")

    label("loc_614D")

    OP_6C(30000, 0)

    label("loc_6156")

    SetChrPos(0x102, 16490, 0, 16250, 90)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61FB")
    Sleep(500)

    ChrTalk(    #208
        0x102,
        (
            "#1043F（男学生两名\x01",
            "  和被击伤的勤务员吗……）\x02\x03",

            "#1040F（那个情况看来……\x01",
            "  似乎不是致命伤。）\x02\x03",

            "（总算放心一点吧……）\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2014)

    label("loc_61FB")

    Call(0, 76)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_49_6103 end

    def Function_50_6207(): pass

    label("Function_50_6207")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6214")
    Return()

    label("loc_6214")

    EventBegin(0x1)
    Fade(500)
    OP_6D(16410, 0, 23210, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    OP_8E(0x102, 0x4056, 0x0, 0x604A, 0x7D0, 0x0)
    OP_8C(0x102, 45, 400)
    OP_0D()
    Sleep(500)

    ChrTalk(    #209
        0x102,
        (
            "#1042F（……外面有巡逻。\x01",
            "  从里面通过比较好。）\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(500)
    OP_6D(15550, 0, 23560, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(180000, 0)
    OP_6E(262, 0)
    SetChrPos(0x102, 15550, 0, 23560, 180)
    OP_0D()
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)
    Return()

    # Function_50_6207 end

    def Function_51_6314(): pass

    label("Function_51_6314")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6321")
    Return()

    label("loc_6321")

    EventBegin(0x0)
    OP_D2(0x270019, 0x27001D, 0x1D)
    OP_D2(0x2600FC, 0x260101, 0x1E)
    OP_D2(0x270011, 0x270015, 0x1F)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6450")

    def lambda_634F():
        OP_6D(35520, 0, 12770, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_634F)

    def lambda_6367():
        OP_6B(2910, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6367)

    def lambda_6377():
        OP_6C(225000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_6377)
    OP_6E(310, 3000)
    Sleep(1000)
    Fade(500)
    OP_6D(26720, 0, 12520, 0)
    OP_67(0, 5470, -10000, 0)
    OP_6B(1580, 0)
    OP_6C(237000, 0)
    OP_6E(502, 0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    SetChrPos(0x102, 26720, 0, 12520, 45)
    OP_0D()
    Sleep(500)

    ChrTalk(    #210
        0x102,
        (
            "#1042F（……没办法了。\x01",
            "  一口气跑过去吧。）\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_8C(0x102, 90, 400)
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x102, 29)
    SetChrSubChip(0x102, 0)
    OP_0D()
    Sleep(500)
    Jump("loc_64B9")

    label("loc_6450")

    Fade(500)
    OP_6D(26720, 0, 12520, 0)
    OP_67(0, 5470, -10000, 0)
    OP_6B(1580, 0)
    OP_6C(237000, 0)
    OP_6E(502, 0)
    SetChrPos(0x102, 26720, 0, 12520, 90)
    OP_0D()
    Fade(250)
    SetChrChipByIndex(0x102, 29)
    SetChrSubChip(0x102, 0)
    OP_0D()
    Sleep(500)

    label("loc_64B9")

    LoadEffect(0x0, "craft\\\\cr162_02.eff")
    OP_7D(0x0, 0x102, 0x78, 0xFA0)
    OP_22(0x99, 0x0, 0x64)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x102, 0)

    def lambda_64EC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_64EC)

    def lambda_64FE():
        OP_8E(0xFE, 0xCE5E, 0x0, 0x3282, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_64FE)

    def lambda_6519():
        OP_6C(225000, 300)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_6519)

    def lambda_6529():
        OP_67(0, 6300, -10000, 300)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_6529)
    OP_6D(34000, 0, 12820, 300)
    OP_44(0x102, 0x1)
    WaitChrThread(0x102, 0x2)
    SetChrFlags(0x102, 0x80)
    Sleep(600)
    Fade(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10)
    OP_6D(50030, 0, 12990, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(90000, 0)
    OP_6E(262, 0)
    OP_7D(0x0, 0x102, 0x28, 0x3E8)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x102, 0x20)
    SetChrFlags(0x102, 0x1000)
    SetChrPos(0x102, 49830, 4000, 12930, 90)
    SetChrChipByIndex(0x102, 30)
    SetChrFlags(0x102, 0x20)
    SetChrSubChip(0x102, 1)

    def lambda_65EC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_65EC)
    SetChrFlags(0x102, 0x4)

    def lambda_6603():
        OP_8F(0xFE, 0xC36E, 0x0, 0x32BE, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6603)
    WaitChrThread(0x102, 0x1)
    PlayEffect(0x0, 0xFF, 0x102, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xA4, 0x0, 0x64)
    OP_7D(0x1, 0x102, 0x0, 0x0)
    WaitChrThread(0x102, 0x2)
    Sleep(500)
    ClearChrFlags(0x102, 0x20)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x102, 0)
    ClearChrFlags(0x102, 0x1000)
    OP_A2(0x2015)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_51_6314 end

    def Function_52_6688(): pass

    label("Function_52_6688")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6695")
    Return()

    label("loc_6695")

    EventBegin(0x0)
    OP_D2(0x270019, 0x27001D, 0x1D)
    OP_D2(0x2600FC, 0x260101, 0x1E)
    Fade(500)
    OP_6D(48840, 0, 12980, 0)
    OP_67(0, 5740, -10000, 0)
    OP_6B(1620, 0)
    OP_6C(135000, 0)
    OP_6E(502, 0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    SetChrPos(0x102, 48840, 0, 12980, 270)
    OP_0D()
    LoadEffect(0x0, "craft\\\\cr162_02.eff")
    Fade(250)
    SetChrChipByIndex(0x102, 29)
    SetChrSubChip(0x102, 0)
    OP_0D()
    Sleep(500)
    OP_7D(0x0, 0x102, 0x78, 0xFA0)
    OP_22(0x99, 0x0, 0x64)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x102, 0)

    def lambda_6755():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6755)

    def lambda_6767():
        OP_8E(0xFE, 0x619E, 0x0, 0x30E8, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6767)

    def lambda_6782():
        OP_6C(150000, 300)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_6782)

    def lambda_6792():
        OP_67(0, 6300, -10000, 300)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_6792)
    OP_6D(41000, 0, 12960, 300)
    OP_44(0x102, 0x1)
    WaitChrThread(0x102, 0x2)
    SetChrFlags(0x102, 0x80)
    Sleep(600)
    Fade(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10)
    OP_6D(24400, 0, 12550, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(270000, 0)
    OP_6E(262, 0)
    OP_7D(0x0, 0x102, 0x28, 0x3E8)
    ClearChrFlags(0x102, 0x80)
    SetChrFlags(0x102, 0x1000)
    SetChrPos(0x102, 24400, 4000, 12550, 270)
    SetChrChipByIndex(0x102, 30)
    SetChrFlags(0x102, 0x20)
    SetChrSubChip(0x102, 1)

    def lambda_6850():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6850)
    SetChrFlags(0x102, 0x4)

    def lambda_6867():
        OP_8F(0xFE, 0x5F50, 0x0, 0x3106, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6867)
    WaitChrThread(0x102, 0x1)
    PlayEffect(0x0, 0xFF, 0x102, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xA4, 0x0, 0x64)
    OP_7D(0x1, 0x102, 0x0, 0x0)
    WaitChrThread(0x102, 0x2)
    Sleep(500)
    ClearChrFlags(0x102, 0x20)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x102, 0)
    ClearChrFlags(0x102, 0x1000)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_52_6688 end

    def Function_53_68E9(): pass

    label("Function_53_68E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 6)), scpexpr(EXPR_END)), "loc_6A2D")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_57(0xC8, 0x14, 0xC, "#5C再看一次里面吗？")
    OP_CC(0x0, 0x0, 0xA, 0xA, 0x0)
    OP_CC(0x1, 0x0, "【是】")
    OP_CC(0x1, 0x0, "【否】")
    OP_CC(0x2, 0x0)
    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_DA()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6971"),
        (1, "loc_6A1B"),
        (SWITCH_DEFAULT, "loc_6A2A"),
    )


    label("loc_6971")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_69B6")
    Fade(500)
    SetChrPos(0x102, 56980, 0, 13500, 0)
    OP_6D(56980, 0, 13500, 0)
    OP_6C(285000, 0)
    OP_A3(0x2030)
    OP_0D()
    Jump("loc_69EA")

    label("loc_69B6")

    Fade(500)
    SetChrPos(0x102, 56980, 0, 13500, 0)
    OP_6D(56980, 0, 13500, 0)
    OP_6C(75000, 0)
    OP_A2(0x2030)
    OP_0D()

    label("loc_69EA")


    def lambda_69F0():
        OP_6E(241, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_69F0)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F2)
    NewScene("ED6_DT21/T2511   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_6A1B")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jump("loc_6A2A")

    label("loc_6A2A")

    Jump("loc_6AD7")

    label("loc_6A2D")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6A72")
    Fade(500)
    SetChrPos(0x102, 56980, 0, 13500, 0)
    OP_6D(56980, 0, 13500, 0)
    OP_6C(285000, 0)
    OP_A3(0x2030)
    OP_0D()
    Jump("loc_6AA6")

    label("loc_6A72")

    Fade(500)
    SetChrPos(0x102, 56980, 0, 13500, 0)
    OP_6D(56980, 0, 13500, 0)
    OP_6C(75000, 0)
    OP_A2(0x2030)
    OP_0D()

    label("loc_6AA6")


    def lambda_6AAC():
        OP_6E(241, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6AAC)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F2)
    NewScene("ED6_DT21/T2511   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_6AD7")

    TalkEnd(0xFF)
    Return()

    # Function_53_68E9 end

    def Function_54_6ADB(): pass

    label("Function_54_6ADB")

    EventBegin(0x0)
    OP_6D(56980, 0, 13500, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6E(262, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B25")
    OP_6C(285000, 0)
    Jump("loc_6B2E")

    label("loc_6B25")

    OP_6C(75000, 0)

    label("loc_6B2E")

    SetChrPos(0x102, 56980, 0, 13500, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6BBF")
    Sleep(500)

    ChrTalk(    #211
        0x102,
        (
            "#1043F（敌方士兵四名……）\x02\x03",

            "（以防万一的\x01",
            "  待命人员吗。）\x02\x03",

            "#1042F（或许人质\x01",
            "  在二楼也不一定。）\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2016)

    label("loc_6BBF")

    Call(0, 76)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_54_6ADB end

    def Function_55_6BCB(): pass

    label("Function_55_6BCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6BD8")
    Return()

    label("loc_6BD8")

    EventBegin(0x1)
    OP_D2(0x290142, 0x290146, 0x1F)
    Fade(500)
    SetChrPos(0x18, 38350, 350, 27790, 315)
    ClearChrFlags(0x18, 0x80)
    SetChrChipByIndex(0x18, 23)
    SetChrSubChip(0x18, 0)
    OP_43(0x18, 0x0, 0x0, 0x2)
    OP_6C(270000, 0)
    OP_8C(0x102, 270, 0)
    OP_69(0x102, 0x0)
    OP_0D()
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_6C4A():
        OP_6D(36580, 0, 27680, 3000)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_6C4A)

    def lambda_6C62():
        OP_67(0, 7500, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6C62)

    def lambda_6C7A():
        OP_6B(2300, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6C7A)

    def lambda_6C8A():
        OP_6C(270000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_6C8A)

    def lambda_6C9A():
        OP_6E(321, 3000)
        ExitThread()

    QueueWorkItem(0x18, 3, lambda_6C9A)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6F36), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6CDD")
    OP_90(0x102, 0x258, 0x0, 0x0, 0x1388, 0x0)
    OP_8E(0x102, 0xD67E, 0x0, 0x7ADA, 0x1388, 0x0)
    Jump("loc_6D05")

    label("loc_6CDD")

    OP_90(0x102, 0x258, 0x0, 0x0, 0x1388, 0x0)
    OP_8E(0x102, 0xD67E, 0x0, 0x6392, 0x1388, 0x0)

    label("loc_6D05")

    OP_8C(0x102, 90, 400)
    Sleep(700)
    WaitChrThread(0x101, 0x0)
    Sleep(500)
    Fade(500)
    OP_69(0x102, 0x0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(270000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x18, 0x80)
    OP_0D()
    Sleep(500)

    ChrTalk(    #212
        0x102,
        (
            "#1042F（……外面有巡逻。\x01",
            "  从里面通过比较好。）\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)
    Return()

    # Function_55_6BCB end

    def Function_56_6DA0(): pass

    label("Function_56_6DA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6DAD")
    Return()

    label("loc_6DAD")

    EventBegin(0x1)
    OP_D2(0x290142, 0x290146, 0x1F)
    Fade(500)
    SetChrPos(0x18, 36310, 350, 64080, 225)
    ClearChrFlags(0x18, 0x80)
    SetChrChipByIndex(0x18, 23)
    SetChrSubChip(0x18, 0)
    OP_43(0x18, 0x0, 0x0, 0x2)
    OP_6C(270000, 0)
    OP_8C(0x102, 270, 0)
    OP_69(0x102, 0x0)
    OP_0D()
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_6E1F():
        OP_6D(34720, 0, 63840, 3000)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_6E1F)

    def lambda_6E37():
        OP_67(0, 7500, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6E37)

    def lambda_6E4F():
        OP_6B(2300, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6E4F)

    def lambda_6E5F():
        OP_6C(270000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_6E5F)

    def lambda_6E6F():
        OP_6E(321, 3000)
        ExitThread()

    QueueWorkItem(0x18, 3, lambda_6E6F)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x3), scpexpr(EXPR_PUSH_LONG, 0xF816), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6EB2")
    OP_90(0x102, 0x258, 0x0, 0x0, 0x1388, 0x0)
    OP_8E(0x102, 0xD67E, 0x0, 0x1040A, 0x1388, 0x0)
    Jump("loc_6EDA")

    label("loc_6EB2")

    OP_90(0x102, 0x258, 0x0, 0x0, 0x1388, 0x0)
    OP_8E(0x102, 0xD67E, 0x0, 0xEC22, 0x1388, 0x0)

    label("loc_6EDA")

    OP_8C(0x102, 90, 400)
    Sleep(700)
    WaitChrThread(0x101, 0x0)
    Sleep(500)
    Fade(500)
    OP_69(0x102, 0x0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(270000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x18, 0x80)
    OP_0D()
    Sleep(500)

    ChrTalk(    #213
        0x102,
        (
            "#1042F（……外面有巡逻。\x01",
            "  从里面通过比较好。）\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)
    Return()

    # Function_56_6DA0 end

    def Function_57_6F75(): pass

    label("Function_57_6F75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6FED")
    EventBegin(0x0)
    OP_A2(0x2018)
    OP_28(0xC0, 0x1, 0x2)
    Fade(500)
    SetChrPos(0x102, 58500, 0, 36000, 270)
    OP_6D(58500, 0, 36000, 0)
    OP_6C(285000, 0)
    OP_0D()

    def lambda_6FBF():
        OP_6E(241, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6FBF)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T2510   ._SN", 114, 0, 0)
    IdleLoop()
    Jump("loc_703B")

    label("loc_6FED")


    ChrTalk(    #214
        0x102,
        (
            "#1043F（……好像还在\x01",
            "  继续说话。）\x02\x03",

            "#1042F（去其它地方调查看看吧。）\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_703B")

    Return()

    # Function_57_6F75 end

    def Function_58_703C(): pass

    label("Function_58_703C")

    EventBegin(0x0)
    SetChrPos(0x102, 58500, 0, 36000, 270)
    OP_6D(58500, 0, 36000, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(285000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #215
        0x102,
        (
            "#1035F（难道他就是这次的主谋吗……）\x02\x03",

            "#1043F（说起来的话，\x01",
            "  记得他好像是这学院的毕业生啊。）\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 76)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_58_703C end

    def Function_59_710A(): pass

    label("Function_59_710A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 1)), scpexpr(EXPR_END)), "loc_7206")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_57(0xC8, 0x14, 0xC, "#5C再看一次里面吗？")
    OP_CC(0x0, 0x0, 0xA, 0xA, 0x0)
    OP_CC(0x1, 0x0, "【是】")
    OP_CC(0x1, 0x0, "【否】")
    OP_CC(0x2, 0x0)
    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_DA()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7192"),
        (1, "loc_71F4"),
        (SWITCH_DEFAULT, "loc_7203"),
    )


    label("loc_7192")

    Fade(500)
    SetChrPos(0x102, 58510, 0, 40110, 270)
    OP_6D(58510, 0, 40110, 0)
    OP_6C(285000, 0)
    OP_0D()

    def lambda_71C9():
        OP_6E(241, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_71C9)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F2)
    NewScene("ED6_DT21/T2510   ._SN", 113, 0, 0)
    IdleLoop()

    label("loc_71F4")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jump("loc_7203")

    label("loc_7203")

    Jump("loc_7268")

    label("loc_7206")

    Fade(500)
    SetChrPos(0x102, 58510, 0, 40110, 270)
    OP_6D(58510, 0, 40110, 0)
    OP_6C(285000, 0)
    OP_0D()

    def lambda_723D():
        OP_6E(241, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_723D)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F2)
    NewScene("ED6_DT21/T2510   ._SN", 113, 0, 0)
    IdleLoop()

    label("loc_7268")

    TalkEnd(0xFF)
    Return()

    # Function_59_710A end

    def Function_60_726C(): pass

    label("Function_60_726C")

    EventBegin(0x0)
    SetChrPos(0x102, 58510, 0, 40110, 270)
    OP_6D(58510, 0, 40110, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(285000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7321")
    Sleep(500)

    ChrTalk(    #216
        0x102,
        (
            "#1043F（没有发现教师……）\x02\x03",

            "#1035F（大概是被监禁\x01",
            "  到其它地方了吧。）\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2019)

    label("loc_7321")

    Call(0, 76)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_60_726C end

    def Function_61_732D(): pass

    label("Function_61_732D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 2)), scpexpr(EXPR_END)), "loc_7471")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_57(0xC8, 0x14, 0xC, "#5C再看一次里面吗？")
    OP_CC(0x0, 0x0, 0xA, 0xA, 0x0)
    OP_CC(0x1, 0x0, "【是】")
    OP_CC(0x1, 0x0, "【否】")
    OP_CC(0x2, 0x0)
    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_DA()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_73B5"),
        (1, "loc_745F"),
        (SWITCH_DEFAULT, "loc_746E"),
    )


    label("loc_73B5")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x10E), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_73FA")
    Fade(500)
    SetChrPos(0x102, 59500, 0, 46040, 270)
    OP_6D(59500, 0, 46040, 0)
    OP_6C(315000, 0)
    OP_A3(0x2030)
    OP_0D()
    Jump("loc_742E")

    label("loc_73FA")

    Fade(500)
    SetChrPos(0x102, 59500, 0, 46040, 270)
    OP_6D(59500, 0, 46040, 0)
    OP_6C(225000, 0)
    OP_A2(0x2030)
    OP_0D()

    label("loc_742E")


    def lambda_7434():
        OP_6E(241, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7434)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F3)
    NewScene("ED6_DT21/T2510   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_745F")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jump("loc_746E")

    label("loc_746E")

    Jump("loc_751B")

    label("loc_7471")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x10E), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_74B6")
    Fade(500)
    SetChrPos(0x102, 59500, 0, 46040, 270)
    OP_6D(59500, 0, 46040, 0)
    OP_6C(315000, 0)
    OP_A3(0x2030)
    OP_0D()
    Jump("loc_74EA")

    label("loc_74B6")

    Fade(500)
    SetChrPos(0x102, 59500, 0, 46040, 270)
    OP_6D(59500, 0, 46040, 0)
    OP_6C(225000, 0)
    OP_A2(0x2030)
    OP_0D()

    label("loc_74EA")


    def lambda_74F0():
        OP_6E(241, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_74F0)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F3)
    NewScene("ED6_DT21/T2510   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_751B")

    TalkEnd(0xFF)
    Return()

    # Function_61_732D end

    def Function_62_751F(): pass

    label("Function_62_751F")

    EventBegin(0x0)
    OP_6D(59500, 0, 46040, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6E(262, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7569")
    OP_6C(315000, 0)
    Jump("loc_7572")

    label("loc_7569")

    OP_6C(225000, 0)

    label("loc_7572")

    SetChrPos(0x102, 59500, 0, 46040, 270)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_75F6")
    Sleep(500)

    ChrTalk(    #217
        0x102,
        (
            "#1042F（虽然有死角看不到，\x01",
            "  但可以感觉到走廊上有人……）\x02\x03",

            "（大概是看守的士兵吧。）\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x201A)

    label("loc_75F6")

    Call(0, 76)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_62_751F end

    def Function_63_7602(): pass

    label("Function_63_7602")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7691")
    EventBegin(0x0)
    OP_A2(0x201B)
    Fade(500)
    OP_6D(58500, 0, 51970, 0)
    SetChrPos(0x102, 58500, 0, 51970, 270)
    OP_6C(225000, 0)
    OP_0D()
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #218
        0x102,
        "#1044F（啊……）\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F4)
    NewScene("ED6_DT21/T2510   ._SN", 111, 0, 0)
    IdleLoop()
    Jump("loc_76EF")

    label("loc_7691")


    ChrTalk(    #219
        0x102,
        (
            "#1043F（……说太久的话\x01",
            "  也许会被看守的士兵发现。）\x02\x03",

            "#1042F（去其它地方调查看看吧。）\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_76EF")

    Return()

    # Function_63_7602 end

    def Function_64_76F0(): pass

    label("Function_64_76F0")

    EventBegin(0x0)
    SetChrPos(0x102, 58500, 0, 51970, 270)
    OP_6D(58500, 0, 51970, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    Sleep(500)

    ChrTalk(    #220
        0x102,
        (
            "#1040F#6P（……安静些，汉斯。）\x02\x03",

            "（声音太大的话\x01",
            "  会被看守的士兵发现啊。）\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(352, 0, -1, -1)
    SetChrName("汉斯")

    AnonymousTalk(    #221
        (
            "\x07\x00#732F（知、知道了……）\x02\x03",

            "#734F（……不过你啊，）\x02\x03",

            "（在这种情况下突然冒出来，\x01",
            "  让人怎么能不吃惊嘛。）\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #222
        0x102,
        "#1054F#6P（哈哈……抱歉。）\x02",
    )

    CloseMessageWindow()
    OP_A2(0x10F5)
    NewScene("ED6_DT21/T2510   ._SN", 111, 0, 0)
    IdleLoop()
    Return()

    # Function_64_76F0 end

    def Function_65_7848(): pass

    label("Function_65_7848")

    EventBegin(0x0)
    SetChrPos(0x102, 58500, 0, 51970, 270)
    OP_6D(58500, 0, 51970, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    Sleep(500)
    SetMessageWindowPos(360, 50, -1, -1)
    SetChrName("汉斯")

    AnonymousTalk(    #223
        (
            "\x07\x00#734F（总之一定切记\x01",
            "  声音不要太大啊……）\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(300, 0, -1, -1)
    SetChrName("乔儿")

    AnonymousTalk(    #224
        (
            "#645F（太、太吃惊了！）\x02\x03",

            "#644F（为什么约修亚\x01",
            "  会在这里呢！？）\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #225
        0x102,
        (
            "#1040F#6P（好久不见了啊，乔儿。）\x02\x03",

            "#1035F（现在时间紧迫，\x01",
            "  我只能长话短说……）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #226
        (
            "\x07\x05约修亚把至今为止发生的一切，以及从米克\x01",
            "那里听说学院发生了异变等事情做了个说明。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_A2(0x10F6)
    NewScene("ED6_DT21/T2510   ._SN", 111, 0, 0)
    IdleLoop()
    Return()

    # Function_65_7848 end

    def Function_66_7A13(): pass

    label("Function_66_7A13")

    EventBegin(0x0)
    SetChrPos(0x102, 58500, 0, 51970, 270)
    OP_6D(58500, 0, 51970, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Call(0, 76)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_66_7A13 end

    def Function_67_7A79(): pass

    label("Function_67_7A79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 4)), scpexpr(EXPR_END)), "loc_7BBD")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_57(0xC8, 0x14, 0xC, "#5C再看一次里面吗？")
    OP_CC(0x0, 0x0, 0xA, 0xA, 0x0)
    OP_CC(0x1, 0x0, "【是】")
    OP_CC(0x1, 0x0, "【否】")
    OP_CC(0x2, 0x0)
    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_DA()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7B01"),
        (1, "loc_7BAB"),
        (SWITCH_DEFAULT, "loc_7BBA"),
    )


    label("loc_7B01")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7B46")
    Fade(500)
    SetChrPos(0x102, 48830, 0, 80500, 180)
    OP_6D(48830, 0, 80500, 0)
    OP_6C(105000, 0)
    OP_A3(0x2030)
    OP_0D()
    Jump("loc_7B7A")

    label("loc_7B46")

    Fade(500)
    SetChrPos(0x102, 48830, 0, 80500, 180)
    OP_6D(48830, 0, 80500, 0)
    OP_6C(255000, 0)
    OP_A2(0x2030)
    OP_0D()

    label("loc_7B7A")


    def lambda_7B80():
        OP_6E(241, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7B80)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T2513   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_7BAB")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jump("loc_7BBA")

    label("loc_7BBA")

    Jump("loc_7C67")

    label("loc_7BBD")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7C02")
    Fade(500)
    SetChrPos(0x102, 48830, 0, 80500, 180)
    OP_6D(48830, 0, 80500, 0)
    OP_6C(105000, 0)
    OP_A3(0x2030)
    OP_0D()
    Jump("loc_7C36")

    label("loc_7C02")

    Fade(500)
    SetChrPos(0x102, 48830, 0, 80500, 180)
    OP_6D(48830, 0, 80500, 0)
    OP_6C(255000, 0)
    OP_A2(0x2030)
    OP_0D()

    label("loc_7C36")


    def lambda_7C3C():
        OP_6E(241, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7C3C)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T2513   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_7C67")

    TalkEnd(0xFF)
    Return()

    # Function_67_7A79 end

    def Function_68_7C6B(): pass

    label("Function_68_7C6B")

    EventBegin(0x0)
    OP_6D(48830, 0, 80500, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6E(262, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7CB5")
    OP_6C(105000, 0)
    Jump("loc_7CBE")

    label("loc_7CB5")

    OP_6C(255000, 0)

    label("loc_7CBE")

    SetChrPos(0x102, 48830, 0, 80500, 180)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D36")
    Sleep(500)

    ChrTalk(    #227
        0x102,
        (
            "#1040F（休息室这里很安静，\x01",
            "  不像有人的样子……）\x02\x03",

            "（这里应该没有人。）\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x201C)

    label("loc_7D36")

    Call(0, 76)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_68_7C6B end

    def Function_69_7D42(): pass

    label("Function_69_7D42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7D4F")
    Return()

    label("loc_7D4F")

    EventBegin(0x0)
    OP_D2(0x270019, 0x27001D, 0x1D)
    OP_D2(0x2600FC, 0x260101, 0x1E)
    Fade(500)
    OP_6D(43190, 0, 81780, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(1600, 0)
    OP_6C(45000, 0)
    OP_6E(499, 0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    SetChrPos(0x102, 43040, 0, 81120, 270)
    OP_0D()
    LoadEffect(0x0, "craft\\\\cr162_02.eff")
    Fade(250)
    SetChrChipByIndex(0x102, 29)
    SetChrSubChip(0x102, 0)
    OP_0D()
    Sleep(500)
    OP_7D(0x0, 0x102, 0x78, 0xFA0)
    OP_22(0x99, 0x0, 0x64)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x102, 0)

    def lambda_7E0F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7E0F)

    def lambda_7E21():
        OP_8E(0xFE, 0x6450, 0x0, 0x13C40, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7E21)

    def lambda_7E3C():
        OP_6C(30000, 300)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_7E3C)

    def lambda_7E4C():
        OP_67(0, 6300, -10000, 300)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_7E4C)
    OP_6D(36000, 0, 81030, 300)
    OP_44(0x102, 0x1)
    WaitChrThread(0x102, 0x2)
    SetChrFlags(0x102, 0x80)
    Sleep(600)
    Fade(500)
    OP_6D(25160, 0, 80940, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(270000, 0)
    OP_6E(262, 0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10)
    OP_7D(0x0, 0x102, 0x28, 0x3E8)
    ClearChrFlags(0x102, 0x80)
    SetChrFlags(0x102, 0x1000)
    SetChrPos(0x102, 25160, 4000, 80940, 270)
    SetChrChipByIndex(0x102, 30)
    SetChrFlags(0x102, 0x20)
    SetChrSubChip(0x102, 1)

    def lambda_7F0A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7F0A)
    SetChrFlags(0x102, 0x4)

    def lambda_7F21():
        OP_8F(0xFE, 0x6248, 0x0, 0x13C2C, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7F21)
    WaitChrThread(0x102, 0x1)
    PlayEffect(0x0, 0xFF, 0x102, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xA4, 0x0, 0x64)
    WaitChrThread(0x102, 0x2)
    OP_7D(0x1, 0x102, 0x0, 0x0)
    Sleep(500)
    ClearChrFlags(0x102, 0x20)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x102, 0)
    ClearChrFlags(0x102, 0x1000)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_69_7D42 end

    def Function_70_7FA3(): pass

    label("Function_70_7FA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7FB0")
    Return()

    label("loc_7FB0")

    EventBegin(0x0)
    OP_D2(0x270019, 0x27001D, 0x1D)
    OP_D2(0x2600FC, 0x260101, 0x1E)
    Fade(500)
    OP_6D(26220, 0, 80980, 0)
    OP_67(0, 5920, -10000, 0)
    OP_6B(1620, 0)
    OP_6C(312000, 0)
    OP_6E(499, 0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    SetChrPos(0x102, 26220, 0, 80980, 90)
    OP_0D()
    LoadEffect(0x0, "craft\\\\cr162_02.eff")
    Fade(250)
    SetChrChipByIndex(0x102, 29)
    SetChrSubChip(0x102, 0)
    OP_0D()
    Sleep(500)
    OP_22(0x99, 0x0, 0x64)
    OP_7D(0x0, 0x102, 0x78, 0xFA0)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x102, 0)

    def lambda_8070():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8070)

    def lambda_8082():
        OP_8E(0xFE, 0xA83E, 0x0, 0x13C4A, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8082)

    def lambda_809D():
        OP_6C(330000, 300)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_809D)

    def lambda_80AD():
        OP_67(0, 6300, -10000, 300)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_80AD)
    OP_6D(34000, 0, 80920, 300)
    OP_44(0x102, 0x1)
    WaitChrThread(0x102, 0x2)
    SetChrFlags(0x102, 0x80)
    Sleep(600)
    Fade(500)
    OP_6D(44120, 0, 80990, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(90000, 0)
    OP_6E(262, 0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10)
    OP_7D(0x0, 0x102, 0x28, 0x3E8)
    ClearChrFlags(0x102, 0x80)
    SetChrFlags(0x102, 0x1000)
    SetChrPos(0x102, 44120, 4000, 80990, 90)
    SetChrChipByIndex(0x102, 30)
    SetChrFlags(0x102, 0x20)
    SetChrSubChip(0x102, 1)

    def lambda_816B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_816B)
    SetChrFlags(0x102, 0x4)

    def lambda_8182():
        OP_8F(0xFE, 0xAC58, 0x0, 0x13C5E, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8182)
    WaitChrThread(0x102, 0x1)
    PlayEffect(0x0, 0xFF, 0x102, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xA4, 0x0, 0x64)
    WaitChrThread(0x102, 0x2)
    OP_7D(0x1, 0x102, 0x0, 0x0)
    Sleep(500)
    ClearChrFlags(0x102, 0x20)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x102, 0)
    ClearChrFlags(0x102, 0x1000)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_70_7FA3 end

    def Function_71_8204(): pass

    label("Function_71_8204")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 5)), scpexpr(EXPR_END)), "loc_8348")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_57(0xC8, 0x14, 0xC, "#5C再看一次里面吗？")
    OP_CC(0x0, 0x0, 0xA, 0xA, 0x0)
    OP_CC(0x1, 0x0, "【是】")
    OP_CC(0x1, 0x0, "【否】")
    OP_CC(0x2, 0x0)
    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_DA()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_828C"),
        (1, "loc_8336"),
        (SWITCH_DEFAULT, "loc_8345"),
    )


    label("loc_828C")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_82D1")
    Fade(500)
    SetChrPos(0x102, 16480, 0, 76930, 90)
    OP_6D(16480, 0, 76930, 0)
    OP_6C(150000, 0)
    OP_A3(0x2030)
    OP_0D()
    Jump("loc_8305")

    label("loc_82D1")

    Fade(500)
    SetChrPos(0x102, 16480, 0, 76930, 90)
    OP_6D(16480, 0, 76930, 0)
    OP_6C(30000, 0)
    OP_A2(0x2030)
    OP_0D()

    label("loc_8305")


    def lambda_830B():
        OP_6E(241, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_830B)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F3)
    NewScene("ED6_DT21/T2512   ._SN", 116, 0, 0)
    IdleLoop()

    label("loc_8336")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jump("loc_8345")

    label("loc_8345")

    Jump("loc_83F2")

    label("loc_8348")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_838D")
    Fade(500)
    SetChrPos(0x102, 16480, 0, 76930, 90)
    OP_6D(16480, 0, 76930, 0)
    OP_6C(150000, 0)
    OP_A3(0x2030)
    OP_0D()
    Jump("loc_83C1")

    label("loc_838D")

    Fade(500)
    SetChrPos(0x102, 16480, 0, 76930, 90)
    OP_6D(16480, 0, 76930, 0)
    OP_6C(30000, 0)
    OP_A2(0x2030)
    OP_0D()

    label("loc_83C1")


    def lambda_83C7():
        OP_6E(241, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_83C7)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F3)
    NewScene("ED6_DT21/T2512   ._SN", 116, 0, 0)
    IdleLoop()

    label("loc_83F2")

    TalkEnd(0xFF)
    Return()

    # Function_71_8204 end

    def Function_72_83F6(): pass

    label("Function_72_83F6")

    EventBegin(0x0)
    OP_6D(16480, 0, 76930, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6E(262, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8440")
    OP_6C(150000, 0)
    Jump("loc_8449")

    label("loc_8440")

    OP_6C(30000, 0)

    label("loc_8449")

    SetChrPos(0x102, 16480, 0, 76930, 90)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_84B6")
    Sleep(500)

    ChrTalk(    #228
        0x102,
        (
            "#1043F（三个女孩子吗……）\x02\x03",

            "#1042F（其它人大概在主校舍吧？）\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x201D)

    label("loc_84B6")

    Call(0, 76)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_72_83F6 end

    def Function_73_84C2(): pass

    label("Function_73_84C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 6)), scpexpr(EXPR_END)), "loc_8606")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_57(0xC8, 0x14, 0xC, "#5C再看一次里面吗？")
    OP_CC(0x0, 0x0, 0xA, 0xA, 0x0)
    OP_CC(0x1, 0x0, "【是】")
    OP_CC(0x1, 0x0, "【否】")
    OP_CC(0x2, 0x0)
    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_DA()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_854A"),
        (1, "loc_85F4"),
        (SWITCH_DEFAULT, "loc_8603"),
    )


    label("loc_854A")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_858F")
    Fade(500)
    SetChrPos(0x102, 16480, 0, 71110, 90)
    OP_6D(16480, 0, 71110, 0)
    OP_6C(150000, 0)
    OP_A3(0x2030)
    OP_0D()
    Jump("loc_85C3")

    label("loc_858F")

    Fade(500)
    SetChrPos(0x102, 16480, 0, 71110, 90)
    OP_6D(16480, 0, 71110, 0)
    OP_6C(30000, 0)
    OP_A2(0x2030)
    OP_0D()

    label("loc_85C3")


    def lambda_85C9():
        OP_6E(241, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_85C9)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F4)
    NewScene("ED6_DT21/T2512   ._SN", 109, 0, 0)
    IdleLoop()

    label("loc_85F4")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jump("loc_8603")

    label("loc_8603")

    Jump("loc_86B0")

    label("loc_8606")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_864B")
    Fade(500)
    SetChrPos(0x102, 16480, 0, 71110, 90)
    OP_6D(16480, 0, 71110, 0)
    OP_6C(150000, 0)
    OP_A3(0x2030)
    OP_0D()
    Jump("loc_867F")

    label("loc_864B")

    Fade(500)
    SetChrPos(0x102, 16480, 0, 71110, 90)
    OP_6D(16480, 0, 71110, 0)
    OP_6C(30000, 0)
    OP_A2(0x2030)
    OP_0D()

    label("loc_867F")


    def lambda_8685():
        OP_6E(241, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8685)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F4)
    NewScene("ED6_DT21/T2512   ._SN", 109, 0, 0)
    IdleLoop()

    label("loc_86B0")

    TalkEnd(0xFF)
    Return()

    # Function_73_84C2 end

    def Function_74_86B4(): pass

    label("Function_74_86B4")

    EventBegin(0x0)
    OP_6D(16480, 0, 71110, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6E(262, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_86FE")
    OP_6C(150000, 0)
    Jump("loc_8707")

    label("loc_86FE")

    OP_6C(30000, 0)

    label("loc_8707")

    SetChrPos(0x102, 16480, 0, 71110, 90)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8778")
    Sleep(500)

    ChrTalk(    #229
        0x102,
        (
            "#1042F（巡逻的士兵两名……）\x02\x03",

            "#1035F（其它的房间应该没有人了。）\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x201E)

    label("loc_8778")

    Call(0, 76)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_74_86B4 end

    def Function_75_8784(): pass

    label("Function_75_8784")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8791")
    Return()

    label("loc_8791")

    EventBegin(0x1)
    Fade(500)
    OP_6D(16260, 0, 70080, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(300)
    OP_8E(0x102, 0x406A, 0x0, 0x10B6C, 0x7D0, 0x0)
    OP_8C(0x102, 135, 400)
    WaitChrThread(0x102, 0x1)
    Sleep(500)

    ChrTalk(    #230
        0x102,
        (
            "#1042F（……外面有巡逻。\x01",
            "  从里面通过比较好。）\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(500)
    OP_6D(15560, 0, 69700, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrPos(0x102, 15560, 0, 69700, 0)
    OP_0D()
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)
    Return()

    # Function_75_8784 end

    def Function_76_889B(): pass

    label("Function_76_889B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8997")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇建筑物内部全部确认，后门的锁也已经打开】\x01",          # 0
            "【◇建筑物内部没有全部确认，后门的锁也没有打开】\x01",      # 1
            "【◇不变更】\x01",                                          # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8955"),
        (1, "loc_8976"),
        (SWITCH_DEFAULT, "loc_8997"),
    )


    label("loc_8955")

    OP_A2(0x2017)
    OP_A2(0x2014)
    OP_A2(0x2016)
    OP_A2(0x2018)
    OP_A2(0x2019)
    OP_A2(0x201A)
    OP_A2(0x201B)
    OP_A2(0x201C)
    OP_A2(0x201D)
    OP_A2(0x201E)
    Jump("loc_8997")

    label("loc_8976")

    OP_A3(0x2017)
    OP_A3(0x2014)
    OP_A3(0x2016)
    OP_A3(0x2018)
    OP_A3(0x2019)
    OP_A3(0x201A)
    OP_A3(0x201B)
    OP_A3(0x201C)
    OP_A3(0x201D)
    OP_A3(0x201E)
    Jump("loc_8997")

    label("loc_8997")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8AC0")
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x102)
    Sleep(500)

    ChrTalk(    #231
        0x102,
        (
            "#1035F（这样就算全部调查完毕了吧。）\x02\x03",

            "#1042F（这种程度的敌人……\x01",
            "  凭我一个人应该就可以……）\x02\x03",

            "（…………………………………）\x02\x03",

            "#1043F（不……\x01",
            "  现在不是最佳时机。）\x02\x03",

            "（还是赶快回到大家那里吧。）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/R2301   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_8AC0")

    Return()

    # Function_76_889B end

    def Function_77_8AC1(): pass

    label("Function_77_8AC1")

    EventBegin(0x0)
    OP_D2(0x26000D, 0x260012, 0x20)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrChipByIndex(0x14, 32)
    SetChrChipByIndex(0x15, 32)
    SetChrChipByIndex(0x16, 32)
    SetChrChipByIndex(0x17, 32)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x29, 0x80)
    SetChrFlags(0x2A, 0x80)
    SetChrFlags(0x2B, 0x80)
    SetChrFlags(0x2C, 0x80)
    OP_43(0x14, 0x1, 0x0, 0x22)
    OP_43(0x15, 0x1, 0x0, 0x23)
    OP_43(0x18, 0x1, 0x0, 0x26)
    OP_43(0x19, 0x1, 0x0, 0x27)
    OP_43(0x1A, 0x1, 0x0, 0x28)
    OP_43(0x1B, 0x1, 0x0, 0x29)
    SetChrPos(0x16, 21540, 0, 46950, 180)
    SetChrPos(0x17, 21540, 0, 45600, 0)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    OP_6D(53310, 0, 46050, 0)
    OP_67(0, 8390, -10000, 0)
    OP_6B(3210, 0)
    OP_6C(90000, 0)
    OP_6E(375, 0)

    def lambda_8BBB():
        OP_6D(23270, 0, 46150, 6000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_8BBB)

    def lambda_8BD3():
        OP_67(0, 7570, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_8BD3)

    def lambda_8BEB():
        OP_6B(3220, 6000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_8BEB)

    def lambda_8BFB():
        OP_6E(345, 6000)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_8BFB)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x0, 0x1)
    Fade(1000)
    OP_6D(22660, 0, 46750, 0)
    OP_67(0, 7180, -10000, 0)
    OP_6B(2990, 0)
    OP_6C(65000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #232
        0x16,
        (
            "#5P……基尔巴特那家伙的脑子里\x01",
            "到底在想些什么啊？\x02\x03",

            "费这么大力气占据了这里，\x01",
            "难道就是为了吓唬吓唬这群毛头小子吗？\x01",
            "真是无聊的行为啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0x17,
        (
            "#6P确实，想要在王国内制造混乱的话，\x01",
            "最好是在都市中下手……\x02\x03",

            "不过在这所学院中可是\x01",
            "聚集着很多名门家族的子女呢。\x02\x03",

            "听传闻说，就连利贝尔王家的公主\x01",
            "也都在这间学院中就读呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0x16,
        (
            "#5P王家的公主……\x01",
            "难道是科洛蒂娅公主吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0x17,
        (
            "#6P哈哈，那不可能吧。\x01",
            "听说她一直在王城中居住着。\x02\x03",

            "只不过，『怪盗绅士』所迷恋的\x01",
            "那个女孩就是这里的学生，\x01",
            "而且好像确实就是王族的人。\x02\x03",

            "基尔巴特大概就是为了确认\x01",
            "她的真实身份而攻占这里的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0x16,
        (
            "#5P原来如此……这么一说的话\x01",
            "我们辛苦这么久倒也不算是白费力气。\x02\x03",

            "只是那样的话，军队和游击士协会\x01",
            "肯定会来全力营救吧，\x02\x03",

            "我们可不能放松警戒。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0x17,
        (
            "#6P哈哈，我们才刚占据这里，\x01",
            "他们不可能马上发现的。\x02\x03",

            "而且那帮家伙和咱们不同，\x01",
            "现在连导力兵器都用不了，\x02\x03",

            "硬拼的话也不用怕他们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0x16,
        "#5P嗯，的确如此……\x02",
    )

    CloseMessageWindow()
    OP_22(0x235, 0x0, 0x3C)
    Sleep(600)
    OP_22(0x235, 0x0, 0x46)
    OP_20(0x7D0)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(600)
    OP_22(0x235, 0x0, 0x50)
    Sleep(400)

    def lambda_9006():
        OP_8C(0xFE, 270, 600)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_9006)
    Sleep(50)

    def lambda_9019():
        OP_8C(0xFE, 270, 600)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_9019)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F2)
    NewScene("ED6_DT21/R2301   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_77_8AC1 end

    def Function_78_9039(): pass

    label("Function_78_9039")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_D2(0x26000D, 0x260012, 0x20)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x29, 0x80)
    SetChrFlags(0x2A, 0x80)
    SetChrFlags(0x2B, 0x80)
    SetChrFlags(0x2C, 0x80)
    SetChrChipByIndex(0x14, 32)
    SetChrChipByIndex(0x15, 32)
    SetChrChipByIndex(0x16, 32)
    SetChrChipByIndex(0x17, 32)
    OP_43(0x14, 0x1, 0x0, 0x22)
    OP_43(0x15, 0x1, 0x0, 0x23)
    OP_43(0x18, 0x1, 0x0, 0x26)
    OP_43(0x19, 0x1, 0x0, 0x27)
    OP_43(0x1A, 0x1, 0x0, 0x28)
    OP_43(0x1B, 0x1, 0x0, 0x29)
    SetChrPos(0x16, 21540, 0, 46950, 270)
    SetChrPos(0x17, 21540, 0, 45600, 270)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    OP_6F(0x21, 0)
    OP_72(0x21, 0x10)
    OP_6D(22660, 0, 46750, 0)
    OP_67(0, 7180, -10000, 0)
    OP_6B(2990, 0)
    OP_6C(65000, 0)
    OP_6E(262, 0)
    OP_43(0x16, 0x2, 0x0, 0x4F)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #239
        0x16,
        (
            "#5P火、火药式的枪械！？\x01",
            "竟然连这种古董货都拿出来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0x17,
        (
            "#2P这样下去的话防线迟早要被他们攻破……\x01",
            "快把待命中的同伴们叫来！\x02",
        )
    )

    CloseMessageWindow()
    SetMapFlags(0x2000000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T2600   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_78_9039 end

    def Function_79_9202(): pass

    label("Function_79_9202")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9256")
    OP_22(0x235, 0x0, 0x50)
    Sleep(1500)
    OP_23(0x235)
    Sleep(500)
    OP_22(0x235, 0x0, 0x50)
    Sleep(1900)
    OP_23(0x235)
    Sleep(700)
    OP_22(0x235, 0x0, 0x50)
    Sleep(1700)
    OP_23(0x235)
    Sleep(600)
    OP_22(0x235, 0x0, 0x50)
    Sleep(2000)
    OP_23(0x235)
    Sleep(800)
    Jump("Function_79_9202")

    label("loc_9256")

    Return()

    # Function_79_9202 end

    def Function_80_9257(): pass

    label("Function_80_9257")

    EventBegin(0x0)
    Fade(500)
    SetChrPos(0x101, 67000, 0, 28000, 270)
    SetChrPos(0x102, 69060, 0, 28020, 270)
    SetChrPos(0x10A, 68950, 0, 27000, 315)
    SetChrPos(0x10E, 68850, 0, 29110, 225)
    OP_6D(65590, 0, 28000, 0)
    OP_67(0, 7570, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(270000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_70(0x22, 0x3C)
    OP_73(0x22)
    Sleep(1000)
    OP_A2(0x2020)
    OP_64(0x1, 0x1)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_80_9257 end

    def Function_81_92FE(): pass

    label("Function_81_92FE")

    EventBegin(0x0)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (101, "loc_9328"),
        (102, "loc_93EE"),
        (103, "loc_94B4"),
        (105, "loc_957A"),
        (106, "loc_9640"),
        (107, "loc_9706"),
        (108, "loc_97CC"),
        (109, "loc_9892"),
        (SWITCH_DEFAULT, "loc_9958"),
    )


    label("loc_9328")

    OP_6D(21430, 250, 67190, 0)
    OP_67(0, 7530, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(314000, 0)
    OP_6E(262, 0)
    SetChrPos(0x14, 35940, -2000, 50640, 0)
    SetChrPos(0x101, 21590, 250, 66630, 180)
    SetChrPos(0x102, 22830, 250, 66650, 180)
    SetChrPos(0x10A, 21570, 500, 67710, 180)
    SetChrPos(0x10E, 22630, 500, 67660, 180)
    FadeToBright(1000, 0)
    OP_0D()

    NpcTalk(    #241
        0x14,
        "女孩子的声音",
        "#2P呀～～不要啊～～！\x02",
    )

    Jump("loc_9958")

    label("loc_93EE")

    OP_6D(22360, 250, 25500, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(144000, 0)
    OP_6E(262, 0)
    SetChrPos(0x14, 40130, 250, 27260, 0)
    SetChrPos(0x101, 22590, 250, 26500, 0)
    SetChrPos(0x102, 21540, 250, 26340, 0)
    SetChrPos(0x10A, 22540, 500, 25460, 0)
    SetChrPos(0x10E, 21540, 500, 25390, 0)
    FadeToBright(1000, 0)
    OP_0D()

    NpcTalk(    #242
        0x14,
        "女孩子的声音",
        "#4P呀～～不要啊～～！\x02",
    )

    Jump("loc_9958")

    label("loc_94B4")

    OP_6D(41330, 440, 73990, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    SetChrPos(0x14, 48840, 0, 54680, 0)
    SetChrPos(0x101, 40760, 250, 73540, 270)
    SetChrPos(0x102, 40820, 250, 74500, 270)
    SetChrPos(0x10A, 41510, 500, 73600, 270)
    SetChrPos(0x10E, 41580, 500, 74500, 270)
    FadeToBright(1000, 0)
    OP_0D()

    NpcTalk(    #243
        0x14,
        "女孩子的声音",
        "#3P呀～～不要啊～～！\x02",
    )

    Jump("loc_9958")

    label("loc_957A")

    OP_6D(49030, 0, 45120, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(134000, 0)
    OP_6E(262, 0)
    SetChrPos(0x14, 65770, 0, 27850, 0)
    SetChrPos(0x101, 47790, 250, 46520, 270)
    SetChrPos(0x102, 47710, 250, 45530, 270)
    SetChrPos(0x10A, 48800, 500, 46520, 270)
    SetChrPos(0x10E, 48670, 500, 45520, 270)
    FadeToBright(1000, 0)
    OP_0D()

    NpcTalk(    #244
        0x14,
        "女孩子的声音",
        "#3P呀～～不要啊～～！\x02",
    )

    Jump("loc_9958")

    label("loc_9640")

    OP_6D(52890, 0, 62050, 0)
    OP_67(0, 8870, -10000, 0)
    OP_6B(2710, 0)
    OP_6C(99000, 0)
    OP_6E(262, 0)
    SetChrPos(0x14, 65770, 0, 27850, 0)
    SetChrPos(0x101, 51310, 0, 62270, 315)
    SetChrPos(0x102, 52320, 0, 62850, 315)
    SetChrPos(0x10A, 52190, 0, 61540, 315)
    SetChrPos(0x10E, 53310, 0, 61990, 315)
    FadeToBright(1000, 0)
    OP_0D()

    NpcTalk(    #245
        0x14,
        "女孩子的声音",
        "#3P呀～～不要啊～～！\x02",
    )

    Jump("loc_9958")

    label("loc_9706")

    OP_6D(52540, 0, 29710, 0)
    OP_67(0, 9140, -10000, 0)
    OP_6B(2650, 0)
    OP_6C(86000, 0)
    OP_6E(262, 0)
    SetChrPos(0x14, 65770, 0, 27850, 0)
    SetChrPos(0x101, 51230, 0, 29590, 225)
    SetChrPos(0x102, 52250, 0, 29160, 225)
    SetChrPos(0x10A, 51900, 0, 30380, 225)
    SetChrPos(0x10E, 52990, 0, 29970, 225)
    FadeToBright(1000, 0)
    OP_0D()

    NpcTalk(    #246
        0x14,
        "女孩子的声音",
        "#3P呀～～不要啊～～！\x02",
    )

    Jump("loc_9958")

    label("loc_97CC")

    OP_6D(47860, 0, 19530, 0)
    OP_67(0, 9580, -10000, 0)
    OP_6B(2580, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    SetChrPos(0x14, 65770, 0, 27850, 0)
    SetChrPos(0x101, 46810, 250, 19550, 270)
    SetChrPos(0x102, 46800, 250, 18440, 270)
    SetChrPos(0x10A, 47820, 500, 19500, 270)
    SetChrPos(0x10E, 47810, 500, 18470, 270)
    FadeToBright(1000, 0)
    OP_0D()

    NpcTalk(    #247
        0x14,
        "女孩子的声音",
        "#6P呀～～不要啊～～！\x02",
    )

    Jump("loc_9958")

    label("loc_9892")

    OP_6D(52820, 0, 26990, 0)
    OP_67(0, 7310, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(105000, 0)
    OP_6E(262, 0)
    SetChrPos(0x14, 65770, 0, 27850, 0)
    SetChrPos(0x101, 51270, 0, 27310, 315)
    SetChrPos(0x102, 52020, 0, 27920, 315)
    SetChrPos(0x10A, 52120, 0, 26600, 315)
    SetChrPos(0x10E, 53070, 0, 27160, 315)
    FadeToBright(1000, 0)
    OP_0D()

    NpcTalk(    #248
        0x14,
        "女孩子的声音",
        "#4P呀～～不要啊～～！\x02",
    )

    Jump("loc_9958")

    label("loc_9958")

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_99CF():
        TurnDirection(0xFE, 0x14, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_99CF)
    Sleep(50)

    def lambda_99E2():
        TurnDirection(0xFE, 0x14, 400)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_99E2)
    Sleep(50)

    def lambda_99F5():
        TurnDirection(0xFE, 0x14, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_99F5)
    Sleep(50)

    def lambda_9A08():
        TurnDirection(0xFE, 0x14, 400)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_9A08)
    Sleep(500)

    ChrTalk(    #249
        0x101,
        "#1020F刚刚的声音是……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0x102,
        (
            "#1042F那个方向……\x01",
            "是旧校舍那边！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0x10E,
        (
            "#842F手册上所差的最后１人……\x01",
            "就是她吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0x10A,
        "#815F赶快追过去！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x202E)
    OP_28(0xC0, 0x1, 0x4000)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_81_92FE end

    def Function_82_9AB2(): pass

    label("Function_82_9AB2")

    EventBegin(0x0)
    OP_20(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9B2B")
    Call(0, 83)
    Call(0, 84)
    OP_A3(0x2031)
    OP_A3(0x2032)
    OP_A3(0x2033)
    OP_A3(0x2034)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9AEA")
    OP_A2(0x2031)

    label("loc_9AEA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9AFA")
    OP_A2(0x2032)

    label("loc_9AFA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9B0A")
    OP_A2(0x2033)

    label("loc_9B0A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9B1A")
    OP_A2(0x2034)

    label("loc_9B1A")

    ClearParty()
    AddParty(0x0, 0xF6, 0xFF)
    AddParty(0x1, 0xF7, 0xFF)
    AddParty(0x9, 0xF8, 0xFF)
    AddParty(0xD, 0xF9, 0xFF)

    label("loc_9B2B")

    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x5, 0xFF, 0xFF)
    AddParty(0x7, 0xFF, 0xFF)
    AddParty(0x6, 0xFF, 0xFF)
    OP_D2(0x260049, 0x26004E, 0x1D)
    SetChrChipByIndex(0x101, 29)
    SetChrSubChip(0x101, 3)
    SetChrPos(0x101, 20370, 0, 45200, 270)
    SetChrPos(0x102, 20600, 0, 46260, 270)
    SetChrPos(0x107, 21330, 0, 45740, 270)
    SetChrPos(0x103, 21830, 0, 46650, 270)
    SetChrPos(0x106, 21700, 0, 44370, 270)
    SetChrPos(0x108, 22800, 0, 45100, 270)
    SetChrPos(0x10A, 18520, 0, 45400, 90)
    SetChrPos(0x1F, 17170, 0, 46730, 90)
    SetChrPos(0x1E, 17290, 0, 45450, 90)
    SetChrPos(0x10E, 18420, 0, 46630, 90)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    OP_6D(12000, 0, 46000, 0)
    OP_67(0, 7050, -10000, 0)
    OP_6B(1890, 0)
    OP_6C(90000, 0)
    OP_6E(469, 0)
    OP_1D(0xE)

    def lambda_9C52():
        OP_6D(21530, 0, 46000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9C52)

    def lambda_9C6A():
        OP_67(0, 8310, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9C6A)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x0)
    Fade(500)
    OP_6D(18910, 0, 46630, 0)
    OP_67(0, 6340, -10000, 0)
    OP_6B(2140, 0)
    OP_6C(315000, 0)
    OP_6E(397, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #253
        0x101,
        (
            "#1012F克鲁茨前辈、亚妮拉丝。\x01",
            "还有卡露娜前辈和库拉兹前辈。\x02\x03",

            "#1006F这次真是多谢\x01",
            "你们的帮助了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0x10A,
        (
            "#811F#5P啊哈哈哈……\x01",
            "干嘛要说这么见外的话啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0x10E,
        (
            "#841F#5P是啊，同样身为游击士，\x01",
            "这也是我们的义务。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0x1E,
        (
            "#835F#5P呵呵，在湖畔那里欠你们的人情\x01",
            "总算是稍微还上了一点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0x1F,
        (
            "#821F#5P大家以后要是遇到什么困难的话，\x01",
            "我们随时都可以帮忙的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0x103,
        "#021F呵呵，那就期待下次见面吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0x102,
        (
            "#1040F你们接下来\x01",
            "有什么打算呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0x10E,
        (
            "#840F#5P嗯，我们准备穿越古罗尼山道\x01",
            "到柏斯那边去。\x02\x03",

            "为了防止类似这次的事情再发生，\x01",
            "还要到各地进行一次巡视。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0x108,
        "#070F是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0x107,
        (
            "#560F#6P那个那个……\x01",
            "那你们可要一路小心了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0x1F,
        "#825F#5P哈哈，你们也是啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0x1E,
        (
            "#831F#5P这种状况结束之前\x01",
            "我们一刻都不能松懈。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0x106,
        (
            "#051F#6P嗯，说的没错，\x01",
            "我们彼此加油吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #266
        0x10A,
        (
            "#814F#5P对了……\x01",
            "喂，艾丝蒂尔。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0x101,
        "#1011F嗯？怎么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0x10A,
        (
            "#816F#5P这次和你并肩作战，\x01",
            "有些新的感觉……\x02\x03",

            "从艾丝蒂尔的动作中\x01",
            "已经感觉不到迷惑和迟疑了呢。\x02\x03",

            "#811F实在是成长了不少，\x01",
            "真让我佩服啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0x101,
        (
            "#1016F讨、讨厌啦～\x01",
            "就算夸奖我，也没有奖励可以拿哦。\x02\x03",

            "#1008F而且亚妮拉丝你也\x01",
            "进步了不少啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0x10A,
        (
            "#1314F#5P这就是在不断的实战中得到的财富吧。\x02\x03",

            "#817F不过我能感觉得到，\x01",
            "艾丝蒂尔不只是武术进步了，\x01",
            "连意志也比以前坚强了很多。\x02\x03",

            "大概是在寻找\x01",
            "约修亚的旅途中\x01",
            "悟出了自己的『道』吧。\x02\x03",

            "#816F真的……很了不起啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0x101,
        "#1017F亚妮拉丝……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0x10A,
        (
            "#819F#5P嘿嘿嘿，身为竞争对手，\x01",
            "我可是不能输给你的。\x02\x03",

            "#1310F以后有机会的话\x01",
            "再一起作战吧？\x02\x03",

            "#811F下一次就该轮到我\x01",
            "让艾丝蒂尔大吃一惊了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0x101,
        (
            "#1018F啊哈哈……嗯！\x01",
            "那我就期待着那一天的到来了！\x02",
        )
    )

    CloseMessageWindow()
    OP_B7(0x9)
    OP_B7(0xD)
    OP_20(0x7D0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A360")
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #274
        (
            "\x07\x05之后，阿加特和提妲\x01",
            "先一步返回了卢安支部，\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #275
        (
            "\x07\x05从王都飞来的基库\x01",
            "也回到了科洛丝的身边。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #276
        (
            "\x07\x05艾丝蒂尔一行人在和学院中的大家\x01",
            "道别后，也重新踏上了新的旅途。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_A708")

    label("loc_A360")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A422")
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #277
        (
            "\x07\x05之后，雪拉扎德和阿加特\x01",
            "先一步返回了卢安支部，\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #278
        (
            "\x07\x05从王都飞来的基库\x01",
            "也回到了科洛丝的身边。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #279
        (
            "\x07\x05艾丝蒂尔一行人在和学院中的大家\x01",
            "道别后，也重新踏上了新的旅途。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_A708")

    label("loc_A422")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A4DE")
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #280
        (
            "\x07\x05之后，阿加特和金\x01",
            "先一步返回了卢安支部，\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #281
        (
            "\x07\x05从王都飞来的基库\x01",
            "也回到了科洛丝的身边。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #282
        (
            "\x07\x05艾丝蒂尔一行人在和学院中的大家\x01",
            "道别后，也重新踏上了新的旅途。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_A708")

    label("loc_A4DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A59E")
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #283
        (
            "\x07\x05之后，雪拉扎德和提妲\x01",
            "先一步返回了卢安支部，\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #284
        (
            "\x07\x05从王都飞来的基库\x01",
            "也回到了科洛丝的身边。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #285
        (
            "\x07\x05艾丝蒂尔一行人在和学院中的大家\x01",
            "道别后，也重新踏上了新的旅途。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_A708")

    label("loc_A59E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A658")
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #286
        (
            "\x07\x05之后，提妲和金\x01",
            "先一步返回了卢安支部，\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #287
        (
            "\x07\x05从王都飞来的基库\x01",
            "也回到了科洛丝的身边。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #288
        (
            "\x07\x05艾丝蒂尔一行人在和学院中的大家\x01",
            "道别后，也重新踏上了新的旅途。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_A708")

    label("loc_A658")

    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #289
        (
            "\x07\x05之后，雪拉扎德和金\x01",
            "先一步返回了卢安支部，\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #290
        (
            "\x07\x05从王都飞来的基库\x01",
            "也回到了科洛丝的身边。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #291
        (
            "\x07\x05艾丝蒂尔一行人在和学院中的大家\x01",
            "道别后，也重新踏上了新的旅途。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_A708")

    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x17, 0x0, 0x64)

    AnonymousTalk(    #292
        "\x07\x02任务【王立学院受袭事件】\x07\x00完成了！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0xC0, 0x4, 0x10)
    OP_28(0xC0, 0x1, 0x8000)
    OP_28(0xC1, 0x3, 0x2)
    OP_28(0xC1, 0x3, 0x8)
    OP_28(0xC3, 0x4, 0x2)
    OP_28(0xC3, 0x4, 0x8)
    OP_28(0xC3, 0x4, 0x10)
    OP_28(0xC3, 0x1, 0x100)
    OP_28(0xC3, 0x1, 0x200)
    OP_28(0xC3, 0x1, 0x400)
    OP_28(0xC3, 0x1, 0x800)
    OP_28(0xC3, 0x1, 0x1000)
    OP_28(0xC3, 0x1, 0x2000)
    OP_28(0xC3, 0x1, 0x4000)
    OP_28(0xC3, 0x1, 0x8000)
    ClearParty()
    AddParty(0x0, 0xF6, 0xFF)
    AddParty(0x1, 0xF7, 0xFF)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A7CD")
    AddParty(0x5, 0xF8, 0xFF)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A7CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A7F7")
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A7F3")
    AddParty(0x2, 0xF8, 0xFF)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A7F7")

    label("loc_A7F3")

    AddParty(0x2, 0xF9, 0xFF)

    label("loc_A7F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A821")
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A81D")
    AddParty(0x6, 0xF8, 0xFF)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A821")

    label("loc_A81D")

    AddParty(0x6, 0xF9, 0xFF)

    label("loc_A821")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A84B")
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A847")
    AddParty(0x7, 0xF8, 0xFF)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A84B")

    label("loc_A847")

    AddParty(0x7, 0xF9, 0xFF)

    label("loc_A84B")

    OP_6D(21410, 0, 45890, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 21410, 0, 45890, 270)
    SetChrPos(0x1, 21410, 0, 45890, 270)
    SetChrPos(0x2, 21410, 0, 45890, 270)
    SetChrPos(0x3, 21410, 0, 45890, 270)
    OP_69(0x0, 0x0)
    SetChrChipByIndex(0x101, 65535)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    OP_A2(0x202F)
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x10, 45800, 0, 46000, 0)
    OP_43(0x10, 0x0, 0x0, 0x4)
    SetChrPos(0xC, 36500, 0, 70920, 225)
    OP_43(0xC, 0x0, 0x6, 0x2)
    SetChrPos(0xD, 35500, 0, 69860, 45)
    OP_43(0xD, 0x0, 0x6, 0x2)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x11, 0x80)
    Sleep(100)
    OP_1D(0x1A)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_82_9AB2 end

    def Function_83_A975(): pass

    label("Function_83_A975")

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
        (0, "loc_A9EF"),
        (1, "loc_A9F5"),
        (SWITCH_DEFAULT, "loc_A9FB"),
    )


    label("loc_A9EF")

    OP_A2(0x1200)
    Jump("loc_A9FB")

    label("loc_A9F5")

    OP_A2(0x1201)
    Jump("loc_A9FB")

    label("loc_A9FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_AA09")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_AA0D")

    label("loc_AA09")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_AA0D")

    Return()

    # Function_83_A975 end

    def Function_84_AA0E(): pass

    label("Function_84_AA0E")

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

    # Function_84_AA0E end

    def Function_85_AA67(): pass

    label("Function_85_AA67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ABD5")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AAC9")

    ChrTalk(    #293
        0x101,
        (
            "#1002F（现在是吸引敌人注意力的好时机。\x01",
            "　必须要尽快解救人质。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ABB2")

    label("loc_AAC9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AB19")

    ChrTalk(    #294
        0x102,
        (
            "#1042F（现在敌人的注意力已经转移了。\x01",
            "　赶快去解救人质吧。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ABB2")

    label("loc_AB19")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AB68")

    ChrTalk(    #295
        0x10A,
        (
            "#816F（看来已经成功把敌人引开了。\x01",
            "　我们快去解救人质吧。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ABB2")

    label("loc_AB68")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ABB2")

    ChrTalk(    #296
        0x10E,
        (
            "#842F（现在是吸引敌人的绝好时机。\x01",
            "　赶快去解救人质吧。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ABB2")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)
    Jump("loc_ACA0")

    label("loc_ABD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AC36")
    EventBegin(0x1)
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #297
        0x105,
        (
            "#040F天马上就要黑了啊。\x01",
            "先回学生会室吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_ACA0")

    label("loc_AC36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ACA0")
    EventBegin(0x1)
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #298
        0x105,
        (
            "#040F学生们应该在教室和宿舍中。\x01",
            "继续在学院内探听吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_ACA0")

    Return()

    # Function_85_AA67 end

    def Function_86_ACA1(): pass

    label("Function_86_ACA1")

    SetPlaceName(0x5F)
    Return()

    # Function_86_ACA1 end

    def Function_87_ACA5(): pass

    label("Function_87_ACA5")

    SetPlaceName(0x5C)
    Return()

    # Function_87_ACA5 end

    def Function_88_ACA9(): pass

    label("Function_88_ACA9")

    SetPlaceName(0x5D)
    Return()

    # Function_88_ACA9 end

    def Function_89_ACAD(): pass

    label("Function_89_ACAD")

    SetPlaceName(0x6C)
    Return()

    # Function_89_ACAD end

    def Function_90_ACB1(): pass

    label("Function_90_ACB1")

    SetPlaceName(0x6D)
    Return()

    # Function_90_ACB1 end

    SaveToFile()

Try(main)
