from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C2400   ._SN',
        MapName             = 'Ruan',
        Location            = 'C2400.x',
        MapIndex            = 97,
        MapDefaultBGM       = "ed60125",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/C2400   ._SN',
            'ED6_DT21/C2400_1 ._SN',
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
        '',                                     # 9
        '',                                     # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
        '霉菌雾',                               # 14
        '朵洛希',                               # 15
        '怪盗布卢布兰',                         # 16
        '布卢布兰幻影',                         # 17
        '魔兽',                                 # 18
        '曼·欧·诺斯',                         # 19
        '基库',                                 # 20
        '福音中型',                             # 21
        '缝影用的针①',                         # 22
        '缝影用的针②',                         # 23
        '缝影用的针③',                         # 24
        '缝影用的针④',                         # 25
        '缝影用的针⑤',                         # 26
        '目标用照相机',                         # 27
        '艾丝蒂尔幻影',                         # 28
        '约修亚幻影',                           # 29
        '雪拉幻影',                             # 30
        '奥利维尔幻影',                         # 31
        '科洛丝幻影',                           # 32
        '阿加特幻影',                           # 33
        '提妲幻影',                             # 34
        '金幻影',                               # 35
        '',                                     # 36
        '',                                     # 37
        '',                                     # 38
        '',                                     # 39
        '',                                     # 40
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
        'ED6_DT29/CH12120 ._CH',             # 00
        'ED6_DT29/CH12121 ._CH',             # 01
        'ED6_DT29/CH12260 ._CH',             # 02
        'ED6_DT29/CH12261 ._CH',             # 03
        'ED6_DT09/CH10530 ._CH',             # 04
        'ED6_DT09/CH10531 ._CH',             # 05
        'ED6_DT09/CH10540 ._CH',             # 06
        'ED6_DT09/CH10541 ._CH',             # 07
        'ED6_DT29/CH12480 ._CH',             # 08
        'ED6_DT29/CH12481 ._CH',             # 09
        'ED6_DT07/CH02070 ._CH',             # 0A
        'ED6_DT27/CH03530 ._CH',             # 0B
        'ED6_DT07/CH01560 ._CH',             # 0C
        'ED6_DT27/CH04000 ._CH',             # 0D
        'ED6_DT07/CH00120 ._CH',             # 0E
        'ED6_DT07/CH00150 ._CH',             # 0F
        'ED6_DT07/CH00130 ._CH',             # 10
        'ED6_DT07/CH00140 ._CH',             # 11
        'ED6_DT26/CH20289 ._CH',             # 12
        'ED6_DT07/CH02320 ._CH',             # 13
        'ED6_DT26/CH20254 ._CH',             # 14
        'ED6_DT06/CH20051 ._CH',             # 15
        'ED6_DT26/CH20273 ._CH',             # 16
        'ED6_DT26/CH20276 ._CH',             # 17
        'ED6_DT27/CH04538 ._CH',             # 18
        'ED6_DT06/CH20064 ._CH',             # 19
        'ED6_DT27/CH04532 ._CH',             # 1A
        'ED6_DT27/CH04530 ._CH',             # 1B
        'ED6_DT27/CH04531 ._CH',             # 1C
        'ED6_DT07/CH02323 ._CH',             # 1D
        'ED6_DT29/CH12122 ._CH',             # 1E
        'ED6_DT26/CH20278 ._CH',             # 1F
        'ED6_DT26/CH20275 ._CH',             # 20
        'ED6_DT27/CH03000 ._CH',             # 21
        'ED6_DT27/CH03010 ._CH',             # 22
        'ED6_DT07/CH00020 ._CH',             # 23
        'ED6_DT07/CH00030 ._CH',             # 24
        'ED6_DT07/CH00040 ._CH',             # 25
        'ED6_DT07/CH00050 ._CH',             # 26
        'ED6_DT07/CH00060 ._CH',             # 27
        'ED6_DT07/CH00070 ._CH',             # 28
    )

    AddCharChipPat(
        'ED6_DT29/CH12120P._CP',             # 00
        'ED6_DT29/CH12121P._CP',             # 01
        'ED6_DT29/CH12260P._CP',             # 02
        'ED6_DT29/CH12261P._CP',             # 03
        'ED6_DT09/CH10530P._CP',             # 04
        'ED6_DT09/CH10531P._CP',             # 05
        'ED6_DT09/CH10540P._CP',             # 06
        'ED6_DT09/CH10541P._CP',             # 07
        'ED6_DT29/CH12480P._CP',             # 08
        'ED6_DT29/CH12481P._CP',             # 09
        'ED6_DT07/CH02070P._CP',             # 0A
        'ED6_DT27/CH03530P._CP',             # 0B
        'ED6_DT07/CH01560P._CP',             # 0C
        'ED6_DT27/CH04000P._CP',             # 0D
        'ED6_DT07/CH00120P._CP',             # 0E
        'ED6_DT07/CH00150P._CP',             # 0F
        'ED6_DT07/CH00130P._CP',             # 10
        'ED6_DT07/CH00140P._CP',             # 11
        'ED6_DT26/CH20289P._CP',             # 12
        'ED6_DT07/CH02320P._CP',             # 13
        'ED6_DT26/CH20254P._CP',             # 14
        'ED6_DT06/CH20051P._CP',             # 15
        'ED6_DT26/CH20273P._CP',             # 16
        'ED6_DT26/CH20276P._CP',             # 17
        'ED6_DT27/CH04538P._CP',             # 18
        'ED6_DT06/CH20064P._CP',             # 19
        'ED6_DT27/CH04532P._CP',             # 1A
        'ED6_DT27/CH04530P._CP',             # 1B
        'ED6_DT27/CH04531P._CP',             # 1C
        'ED6_DT07/CH02323P._CP',             # 1D
        'ED6_DT29/CH12122P._CP',             # 1E
        'ED6_DT26/CH20278P._CP',             # 1F
        'ED6_DT26/CH20275P._CP',             # 20
        'ED6_DT27/CH03000P._CP',             # 21
        'ED6_DT27/CH03010P._CP',             # 22
        'ED6_DT07/CH00020P._CP',             # 23
        'ED6_DT07/CH00030P._CP',             # 24
        'ED6_DT07/CH00040P._CP',             # 25
        'ED6_DT07/CH00050P._CP',             # 26
        'ED6_DT07/CH00060P._CP',             # 27
        'ED6_DT07/CH00070P._CP',             # 28
    )

    DeclNpc(
        X                   = -77650,
        Z                   = 1000,
        Y                   = -45450,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 9260,
        Z                   = 1000,
        Y                   = -115060,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 87390,
        Z                   = 1000,
        Y                   = -64150,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -285710,
        Z                   = 1000,
        Y                   = -116450,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -225060,
        Z                   = 1000,
        Y                   = -68690,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -288070,
        Z                   = 0,
        Y                   = -70170,
        Direction           = 180,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
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
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
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
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
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
        NpcIndex            = 0x1E4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
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
        NpcIndex            = 0x1E4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
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
        NpcIndex            = 0x1E4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
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
        NpcIndex            = 0x1E4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
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
        NpcIndex            = 0x1E4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 33,
        ChipIndex           = 0x21,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 34,
        ChipIndex           = 0x22,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 35,
        ChipIndex           = 0x23,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 36,
        ChipIndex           = 0x24,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 37,
        ChipIndex           = 0x25,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 38,
        ChipIndex           = 0x26,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 39,
        ChipIndex           = 0x27,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 40,
        ChipIndex           = 0x28,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 140,
        Z                   = 0,
        Y                   = -26200,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x39A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -36720,
        Z                   = 0,
        Y                   = -32210,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x39B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -26310,
        Z                   = 0,
        Y                   = -61030,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x399,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -2870,
        Z                   = 0,
        Y                   = -84290,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x39A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 7900,
        Z                   = 0,
        Y                   = -51170,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x39B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 31140,
        Z                   = 0,
        Y                   = -44530,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x399,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 28370,
        Z                   = 0,
        Y                   = -63790,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x39B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -288370,
        Z                   = 0,
        Y                   = -48220,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x399,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -267560,
        Z                   = 0,
        Y                   = -24930,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x39A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -224930,
        Z                   = 0,
        Y                   = -62890,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x39B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -265230,
        Z                   = 0,
        Y                   = -1120,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x39C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -215420,
        Z                   = 0,
        Y                   = -1240,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x399,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -240970,
        Z                   = 0,
        Y                   = 21880,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x39B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -299360,
        Z                   = 0,
        Y                   = -20300,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x39C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -322950,
        Z                   = 0,
        Y                   = -22990,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x399,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -282400,
        Y                   = -1000,
        Z                   = -79250,
        Range               = -292410,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0xFFFEC08C,
        Unknown_18          = 0x0,
        Unknown_1C          = 4,
    )


    DeclActor(
        TriggerX            = -48450,
        TriggerZ            = 0,
        TriggerY            = -100,
        TriggerRange        = 1000,
        ActorX              = -47750,
        ActorZ              = 0,
        ActorY              = -110,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -26010,
        TriggerZ            = 0,
        TriggerY            = 580,
        TriggerRange        = 1000,
        ActorX              = -26070,
        ActorZ              = 0,
        ActorY              = 1270,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 30880,
        TriggerZ            = 0,
        TriggerY            = 6510,
        TriggerRange        = 1000,
        ActorX              = 30960,
        ActorZ              = 0,
        ActorY              = 7200,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -76860,
        TriggerZ            = 0,
        TriggerY            = -41820,
        TriggerRange        = 1000,
        ActorX              = -77670,
        ActorZ              = 0,
        ActorY              = -42070,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -76860,
        TriggerZ            = 0,
        TriggerY            = -38850,
        TriggerRange        = 1000,
        ActorX              = -77550,
        ActorZ              = 0,
        ActorY              = -39020,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -44430,
        TriggerZ            = 0,
        TriggerY            = -116030,
        TriggerRange        = 1000,
        ActorX              = -43740,
        ActorZ              = 0,
        ActorY              = -115970,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -24880,
        TriggerZ            = 0,
        TriggerY            = -115770,
        TriggerRange        = 1000,
        ActorX              = -25600,
        ActorZ              = 0,
        ActorY              = -115990,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 18,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 88610,
        TriggerZ            = 0,
        TriggerY            = -89500,
        TriggerRange        = 1000,
        ActorX              = 89330,
        ActorZ              = 0,
        ActorY              = -89530,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 21,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -353240,
        TriggerZ            = 0,
        TriggerY            = 25560,
        TriggerRange        = 1000,
        ActorX              = -353040,
        ActorZ              = 0,
        ActorY              = 26220,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 22,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -320150,
        TriggerZ            = 0,
        TriggerY            = 26540,
        TriggerRange        = 1000,
        ActorX              = -320010,
        ActorZ              = 0,
        ActorY              = 27300,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 23,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -354150,
        TriggerZ            = 0,
        TriggerY            = -5430,
        TriggerRange        = 1000,
        ActorX              = -353980,
        ActorZ              = 0,
        ActorY              = -4770,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 25,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -341110,
        TriggerZ            = 0,
        TriggerY            = -47480,
        TriggerRange        = 1000,
        ActorX              = -341080,
        ActorZ              = 0,
        ActorY              = -46820,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 26,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -313440,
        TriggerZ            = 0,
        TriggerY            = -83070,
        TriggerRange        = 1000,
        ActorX              = -312810,
        ActorZ              = 0,
        ActorY              = -83080,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 27,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -197390,
        TriggerZ            = 0,
        TriggerY            = -67050,
        TriggerRange        = 1000,
        ActorX              = -196720,
        ActorZ              = 0,
        ActorY              = -67090,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 29,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -76870,
        TriggerZ            = 0,
        TriggerY            = -45220,
        TriggerRange        = 1000,
        ActorX              = -77650,
        ActorZ              = 0,
        ActorY              = -45450,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 16,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 8640,
        TriggerZ            = 0,
        TriggerY            = -115060,
        TriggerRange        = 1000,
        ActorX              = 9260,
        ActorZ              = 0,
        ActorY              = -115060,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 19,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 86710,
        TriggerZ            = 0,
        TriggerY            = -64150,
        TriggerRange        = 1000,
        ActorX              = 87390,
        ActorZ              = 0,
        ActorY              = -64150,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 20,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -286330,
        TriggerZ            = 0,
        TriggerY            = -116450,
        TriggerRange        = 1000,
        ActorX              = -285710,
        ActorZ              = 0,
        ActorY              = -116450,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 24,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -224900,
        TriggerZ            = 0,
        TriggerY            = -67920,
        TriggerRange        = 1000,
        ActorX              = -225060,
        ActorZ              = 0,
        ActorY              = -68690,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 28,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -263020,
        TriggerZ            = 150,
        TriggerY            = 92180,
        TriggerRange        = 800,
        ActorX              = -263020,
        ActorZ              = 650,
        ActorY              = 92180,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 30,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -3200,
        TriggerZ            = 0,
        TriggerY            = 30680,
        TriggerRange        = 1200,
        ActorX              = -3200,
        ActorZ              = 1000,
        ActorY              = 30680,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 31,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -261769,
        TriggerZ            = 0,
        TriggerY            = 35590,
        TriggerRange        = 1200,
        ActorX              = -261769,
        ActorZ              = 1000,
        ActorY              = 35590,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 32,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_A2E",          # 00, 0
        "Function_1_A91",          # 01, 1
        "Function_2_D74",          # 02, 2
        "Function_3_D8A",          # 03, 3
        "Function_4_DD2",          # 04, 4
        "Function_5_1031",         # 05, 5
        "Function_6_1061",         # 06, 6
        "Function_7_10B9",         # 07, 7
        "Function_8_1137",         # 08, 8
        "Function_9_11B5",         # 09, 9
        "Function_10_128C",        # 0A, 10
        "Function_11_136C",        # 0B, 11
        "Function_12_1483",        # 0C, 12
        "Function_13_159A",        # 0D, 13
        "Function_14_16B1",        # 0E, 14
        "Function_15_17C8",        # 0F, 15
        "Function_16_18DF",        # 10, 16
        "Function_17_1AAF",        # 11, 17
        "Function_18_1BC6",        # 12, 18
        "Function_19_1CDD",        # 13, 19
        "Function_20_1DF4",        # 14, 20
        "Function_21_1F0B",        # 15, 21
        "Function_22_2022",        # 16, 22
        "Function_23_2139",        # 17, 23
        "Function_24_2250",        # 18, 24
        "Function_25_2420",        # 19, 25
        "Function_26_2537",        # 1A, 26
        "Function_27_264E",        # 1B, 27
        "Function_28_2765",        # 1C, 28
        "Function_29_287C",        # 1D, 29
        "Function_30_2993",        # 1E, 30
        "Function_31_2F31",        # 1F, 31
        "Function_32_3141",        # 20, 32
    )


    def Function_0_A2E(): pass

    label("Function_0_A2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25F, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A4C")
    SetChrPos(0xD, -288070, 0, -70170, 180)
    ClearChrFlags(0xD, 0x80)

    label("loc_A4C")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (103, "loc_A5C"),
        (143, "loc_A70"),
        (SWITCH_DEFAULT, "loc_A7F"),
    )


    label("loc_A5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x245, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A6D")
    SetMapFlags(0x10000000)
    Event(1, 0)

    label("loc_A6D")

    Jump("loc_A7F")

    label("loc_A70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A7C")
    Event(1, 1)

    label("loc_A7C")

    Jump("loc_A7F")

    label("loc_A7F")

    OP_51(0x13, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_A2E end

    def Function_1_A91(): pass

    label("Function_1_A91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_AA1")
    OP_10(0x30, 0x0)
    OP_10(0x0, 0x1)
    Jump("loc_AA7")

    label("loc_AA1")

    OP_10(0x30, 0x1)
    OP_10(0x0, 0x0)

    label("loc_AA7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ABC")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_ABC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x245, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ADE")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 4500, 0, 28050, 270)

    label("loc_ADE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x264, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AF0")
    OP_6F(0x0, 0)
    Jump("loc_AF7")

    label("loc_AF0")

    OP_6F(0x0, 60)

    label("loc_AF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x264, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B09")
    OP_6F(0x1, 0)
    Jump("loc_B10")

    label("loc_B09")

    OP_6F(0x1, 60)

    label("loc_B10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x264, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B22")
    OP_6F(0x2, 0)
    Jump("loc_B29")

    label("loc_B22")

    OP_6F(0x2, 60)

    label("loc_B29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x264, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B3B")
    OP_6F(0x3, 0)
    Jump("loc_B42")

    label("loc_B3B")

    OP_6F(0x3, 60)

    label("loc_B42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x264, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B54")
    OP_6F(0x4, 0)
    Jump("loc_B5B")

    label("loc_B54")

    OP_6F(0x4, 60)

    label("loc_B5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x264, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B6D")
    OP_6F(0x5, 0)
    Jump("loc_B74")

    label("loc_B6D")

    OP_6F(0x5, 60)

    label("loc_B74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x264, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B86")
    OP_6F(0x6, 0)
    Jump("loc_B8D")

    label("loc_B86")

    OP_6F(0x6, 60)

    label("loc_B8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x265, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B9F")
    OP_6F(0x7, 0)
    Jump("loc_BA6")

    label("loc_B9F")

    OP_6F(0x7, 60)

    label("loc_BA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x265, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BB8")
    OP_6F(0x8, 0)
    Jump("loc_BBF")

    label("loc_BB8")

    OP_6F(0x8, 60)

    label("loc_BBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x265, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BD1")
    OP_6F(0x9, 0)
    Jump("loc_BD8")

    label("loc_BD1")

    OP_6F(0x9, 60)

    label("loc_BD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x265, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BEA")
    OP_6F(0xA, 0)
    Jump("loc_BF1")

    label("loc_BEA")

    OP_6F(0xA, 60)

    label("loc_BF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x265, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C03")
    OP_6F(0xB, 0)
    Jump("loc_C0A")

    label("loc_C03")

    OP_6F(0xB, 60)

    label("loc_C0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x265, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C1C")
    OP_6F(0xC, 0)
    Jump("loc_C23")

    label("loc_C1C")

    OP_6F(0xC, 60)

    label("loc_C23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x267, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C35")
    OP_6F(0xD, 0)
    Jump("loc_C3C")

    label("loc_C35")

    OP_6F(0xD, 60)

    label("loc_C3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x266, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C4E")
    OP_6F(0xE, 0)
    Jump("loc_C55")

    label("loc_C4E")

    OP_6F(0xE, 60)

    label("loc_C55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x266, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C67")
    OP_6F(0xF, 0)
    Jump("loc_C6E")

    label("loc_C67")

    OP_6F(0xF, 60)

    label("loc_C6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x266, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C80")
    OP_6F(0x10, 0)
    Jump("loc_C87")

    label("loc_C80")

    OP_6F(0x10, 60)

    label("loc_C87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x266, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C99")
    OP_6F(0x11, 0)
    Jump("loc_CA0")

    label("loc_C99")

    OP_6F(0x11, 60)

    label("loc_CA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x266, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CB2")
    OP_6F(0x12, 0)
    Jump("loc_CB9")

    label("loc_CB2")

    OP_6F(0x12, 60)

    label("loc_CB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_CC5")
    OP_71(0x15, 0x4)

    label("loc_CC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_CD5")
    OP_64(0x13, 0x1)

    label("loc_CD5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D73")
    LoadEffect(0x2, "map\\\\mp027_00.eff")
    PlayEffect(0x2, 0x2, 0xFF, -3200, 1000, 30680, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    LoadEffect(0x4, "map\\\\mp027_00.eff")
    PlayEffect(0x4, 0x4, 0xFF, -261769, 1000, 35590, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)

    label("loc_D73")

    Return()

    # Function_1_A91 end

    def Function_2_D74(): pass

    label("Function_2_D74")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D89")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_D74")

    label("loc_D89")

    Return()

    # Function_2_D74 end

    def Function_3_D8A(): pass

    label("Function_3_D8A")

    TalkBegin(0xE)

    ChrTalk(    #0
        0xE,
        (
            "#150F如果找到什么\x01",
            "请告诉我哦～\x02\x03",

            "我无论如何\x01",
            "也想拍到幽灵哦～\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xE)
    Return()

    # Function_3_D8A end

    def Function_4_DD2(): pass

    label("Function_4_DD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25F, 6)), scpexpr(EXPR_END)), "loc_DDA")
    Return()

    label("loc_DDA")

    EventBegin(0x0)
    LoadEffect(0x0, "monster\\msc0500.eff")
    OP_D2(0x270111, 0x270121, 0x21)
    OP_D2(0x701D1, 0x701DD, 0x22)
    OP_D2(0x70219, 0x70225, 0x23)
    OP_D2(0x701E9, 0x701F5, 0x24)
    OP_D2(0x70201, 0x7020D, 0x25)
    Fade(500)
    OP_6D(-287220, 0, -79900, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2220, 0)
    OP_6C(40000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -288040, 0, -80880, 0)
    SetChrPos(0xF7, -287640, 0, -81990, 0)
    SetChrPos(0xF8, -289100, 0, -81800, 0)
    SetChrPos(0xF9, -288700, 0, -82730, 0)
    ClearChrFlags(0xD, 0x20)
    SetChrChipByIndex(0xD, 0)
    SetChrSubChip(0xD, 0)
    OP_0D()
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xD, 0, 500, 1500, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Sleep(2000)

    def lambda_F11():
        OP_6D(-287740, 0, -75300, 3000)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_F11)

    def lambda_F29():
        OP_6B(2500, 3000)
        ExitThread()

    QueueWorkItem(0xD, 3, lambda_F29)
    SetChrChipByIndex(0xD, 1)
    SetChrSubChip(0xD, 0)
    OP_43(0xD, 0x0, 0x0, 0x2)

    def lambda_F4A():
        OP_8F(0xFE, 0xFFFB9ABA, 0x0, 0xFFFEE22E, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_F4A)
    Sleep(1000)
    OP_43(0x101, 0x0, 0x0, 0x5)
    OP_43(0xF7, 0x0, 0x0, 0x6)
    OP_43(0xF8, 0x0, 0x0, 0x7)
    OP_43(0xF9, 0x0, 0x0, 0x8)
    WaitChrThread(0xD, 0x1)
    OP_44(0xD, 0x0)
    SetChrChipByIndex(0xD, 0)
    SetChrSubChip(0xD, 0)
    OP_43(0xD, 0x0, 0x0, 0x2)
    WaitChrThread(0xD, 0x2)
    Sleep(500)
    OP_44(0xD, 0x0)
    SetChrFlags(0xD, 0x20)
    SetChrChipByIndex(0xD, 30)
    SetChrSubChip(0xD, 0)

    def lambda_FBD():
        OP_99(0xFE, 0x0, 0x1, 0x7D0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_FBD)
    Sleep(500)

    def lambda_FD2():
        OP_99(0xFE, 0x1, 0x5, 0x1388)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_FD2)

    def lambda_FE2():
        OP_8F(0xFE, 0xFFFB9ABA, 0x0, 0xFFFED1C6, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_FE2)
    Sleep(250)
    Battle(0x39D, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_101D"),
        (0, "loc_1022"),
        (2, "loc_1029"),
        (SWITCH_DEFAULT, "loc_1030"),
    )


    label("loc_101D")

    OP_B4(0x0)
    Jump("loc_1030")

    label("loc_1022")

    Call(0, 9)
    Jump("loc_1030")

    label("loc_1029")

    Call(0, 10)
    Jump("loc_1030")

    label("loc_1030")

    Return()

    # Function_4_DD2 end

    def Function_5_1031(): pass

    label("Function_5_1031")

    SetChrChipByIndex(0x101, 33)
    SetChrSubChip(0x101, 0)
    OP_8E(0xFE, 0xFFFB9ABA, 0x0, 0xFFFED1C6, 0xFA0, 0x0)
    OP_8C(0xFE, 0, 400)
    SetChrChipByIndex(0x101, 13)
    SetChrSubChip(0x101, 0)
    Return()

    # Function_5_1031 end

    def Function_6_1061(): pass

    label("Function_6_1061")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1075")
    SetChrChipByIndex(0x106, 35)
    SetChrSubChip(0x106, 0)
    Jump("loc_107F")

    label("loc_1075")

    SetChrChipByIndex(0x103, 34)
    SetChrSubChip(0x103, 0)

    label("loc_107F")

    OP_8E(0xFE, 0xFFFB9DEE, 0x0, 0xFFFECE7E, 0xFA0, 0x0)
    OP_8C(0xFE, 0, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_10AE")
    SetChrChipByIndex(0x106, 15)
    SetChrSubChip(0x106, 0)
    Jump("loc_10B8")

    label("loc_10AE")

    SetChrChipByIndex(0x103, 14)
    SetChrSubChip(0x103, 0)

    label("loc_10B8")

    Return()

    # Function_6_1061 end

    def Function_7_10B9(): pass

    label("Function_7_10B9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10D3")
    SetChrChipByIndex(0x104, 36)
    SetChrSubChip(0x104, 0)
    Jump("loc_10EA")

    label("loc_10D3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10EA")
    SetChrChipByIndex(0x105, 37)
    SetChrSubChip(0x105, 0)

    label("loc_10EA")

    OP_8E(0xFE, 0xFFFB9722, 0x0, 0xFFFECDB6, 0xFA0, 0x0)
    OP_8C(0xFE, 0, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_111F")
    SetChrChipByIndex(0x104, 16)
    SetChrSubChip(0x104, 0)
    Jump("loc_1136")

    label("loc_111F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1136")
    SetChrChipByIndex(0x105, 17)
    SetChrSubChip(0x105, 0)

    label("loc_1136")

    Return()

    # Function_7_10B9 end

    def Function_8_1137(): pass

    label("Function_8_1137")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1151")
    SetChrChipByIndex(0x104, 36)
    SetChrSubChip(0x104, 0)
    Jump("loc_1168")

    label("loc_1151")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1168")
    SetChrChipByIndex(0x105, 37)
    SetChrSubChip(0x105, 0)

    label("loc_1168")

    OP_8E(0xFE, 0xFFFB99AC, 0x0, 0xFFFECA14, 0xFA0, 0x0)
    OP_8C(0xFE, 0, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_119D")
    SetChrChipByIndex(0x104, 16)
    SetChrSubChip(0x104, 0)
    Jump("loc_11B4")

    label("loc_119D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11B4")
    SetChrChipByIndex(0x105, 17)
    SetChrSubChip(0x105, 0)

    label("loc_11B4")

    Return()

    # Function_8_1137 end

    def Function_9_11B5(): pass

    label("Function_9_11B5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_44(0xD, 0x1)
    SetChrFlags(0xD, 0x80)
    OP_6D(-288040, 0, -76800, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -288040, 0, -76800, 0)
    SetChrPos(0x1, -288040, 0, -76800, 0)
    SetChrPos(0x2, -288040, 0, -76800, 0)
    SetChrPos(0x3, -288040, 0, -76800, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0xF7, 65535)
    SetChrSubChip(0xF7, 0)
    SetChrChipByIndex(0xF8, 65535)
    SetChrSubChip(0xF8, 0)
    SetChrChipByIndex(0xF9, 65535)
    SetChrSubChip(0xF9, 0)
    OP_A2(0x12FE)
    OP_B2(0x0, 0x0, 0x80)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_9_11B5 end

    def Function_10_128C(): pass

    label("Function_10_128C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_44(0xD, 0x1)
    SetChrPos(0xD, -288070, 0, -70170, 180)
    ClearChrFlags(0xD, 0x80)
    OP_6D(-288040, 0, -83520, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -288040, 0, -83520, 180)
    SetChrPos(0x1, -288040, 0, -83520, 180)
    SetChrPos(0x2, -288040, 0, -83520, 180)
    SetChrPos(0x3, -288040, 0, -83520, 180)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0xF7, 65535)
    SetChrSubChip(0xF7, 0)
    SetChrChipByIndex(0xF8, 65535)
    SetChrSubChip(0xF8, 0)
    SetChrChipByIndex(0xF9, 65535)
    SetChrSubChip(0xF9, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_10_128C end

    def Function_11_136C(): pass

    label("Function_11_136C")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x264, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1444")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_13DB")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #1
        "\x07\x00得到了\x1F\xF6\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1320)
    Jump("loc_1441")

    label("loc_13DB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "宝箱里装有\x1F\xF6\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xF6\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_1441")

    Jump("loc_1475")

    label("loc_1444")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1475")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_11_136C end

    def Function_12_1483(): pass

    label("Function_12_1483")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x264, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_155B")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_14F2")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #4
        "\x07\x00得到了\x1F\xFC\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1321)
    Jump("loc_1558")

    label("loc_14F2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "宝箱里装有\x1F\xFC\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFC\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_1558")

    Jump("loc_158C")

    label("loc_155B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_158C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_12_1483 end

    def Function_13_159A(): pass

    label("Function_13_159A")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x264, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1672")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x6C, 1)"), scpexpr(EXPR_END)), "loc_1609")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #7
        "\x07\x00得到了\x1F\x6C\x00\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1322)
    Jump("loc_166F")

    label("loc_1609")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        (
            "宝箱里装有\x1F\x6C\x00\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x6C\x00\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_166F")

    Jump("loc_16A3")

    label("loc_1672")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_16A3")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_13_159A end

    def Function_14_16B1(): pass

    label("Function_14_16B1")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x264, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1789")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_1720")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #10
        "\x07\x00得到了\x1F\xFE\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1323)
    Jump("loc_1786")

    label("loc_1720")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        (
            "宝箱里装有\x1F\xFE\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFE\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_1786")

    Jump("loc_17BA")

    label("loc_1789")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #12
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_17BA")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_14_16B1 end

    def Function_15_17C8(): pass

    label("Function_15_17C8")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x264, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18A0")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x267, 1)"), scpexpr(EXPR_END)), "loc_1837")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #13
        "\x07\x00得到了\x1F\x67\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1324)
    Jump("loc_189D")

    label("loc_1837")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        (
            "宝箱里装有\x1F\x67\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x67\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_189D")

    Jump("loc_18D1")

    label("loc_18A0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #15
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_18D1")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_15_17C8 end

    def Function_16_18DF(): pass

    label("Function_16_18DF")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x264, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A72")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x264, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19BE")
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_91(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_1931():
        OP_91(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1931)

    def lambda_194C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x258)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_194C)
    ClearChrFlags(0x8, 0x80)

    AnonymousTalk(    #16
        "\x07\x05魔兽出现了！\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x39E, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1999"),
        (2, "loc_19AB"),
        (1, "loc_19BB"),
        (SWITCH_DEFAULT, "loc_19BE"),
    )


    label("loc_1999")

    OP_A2(0x1326)
    OP_6F(0x5, 60)
    Sleep(500)
    Jump("loc_19BE")

    label("loc_19AB")

    OP_6F(0x5, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_19BB")

    OP_B4(0x0)
    Return()

    label("loc_19BE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x135, 1)"), scpexpr(EXPR_END)), "loc_1A0D")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #17
        "\x07\x00得到了\x1F\x35\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1325)
    Jump("loc_1A6F")

    label("loc_1A0D")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #18
        (
            "宝箱里装有\x1F\x35\x01\x07\x00。 \x01",
            "所持物品已经满了，\x1F\x35\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)

    label("loc_1A6F")

    Jump("loc_1AA1")

    label("loc_1A72")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #19
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1AA1")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_16_18DF end

    def Function_17_1AAF(): pass

    label("Function_17_1AAF")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x264, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B87")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FA, 1)"), scpexpr(EXPR_END)), "loc_1B1E")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #20
        "\x07\x00得到了\x1F\xFA\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1327)
    Jump("loc_1B84")

    label("loc_1B1E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #21
        (
            "宝箱里装有\x1F\xFA\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFA\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)

    label("loc_1B84")

    Jump("loc_1BB8")

    label("loc_1B87")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #22
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1BB8")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_17_1AAF end

    def Function_18_1BC6(): pass

    label("Function_18_1BC6")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x265, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C9E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x7, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_1C35")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #23
        "\x07\x00得到了\x1F\xFE\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1328)
    Jump("loc_1C9B")

    label("loc_1C35")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #24
        (
            "宝箱里装有\x1F\xFE\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFE\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x7, 60)
    OP_70(0x7, 0x0)

    label("loc_1C9B")

    Jump("loc_1CCF")

    label("loc_1C9E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #25
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1CCF")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_18_1BC6 end

    def Function_19_1CDD(): pass

    label("Function_19_1CDD")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x265, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DB5")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x8, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x25F, 1)"), scpexpr(EXPR_END)), "loc_1D4C")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #26
        "\x07\x00得到了\x1F\x5F\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1329)
    Jump("loc_1DB2")

    label("loc_1D4C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #27
        (
            "宝箱里装有\x1F\x5F\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x5F\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x8, 60)
    OP_70(0x8, 0x0)

    label("loc_1DB2")

    Jump("loc_1DE6")

    label("loc_1DB5")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #28
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1DE6")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_19_1CDD end

    def Function_20_1DF4(): pass

    label("Function_20_1DF4")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x265, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ECC")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x9, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x15E, 1)"), scpexpr(EXPR_END)), "loc_1E63")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #29
        "\x07\x00得到了\x1F\x5E\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x132A)
    Jump("loc_1EC9")

    label("loc_1E63")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #30
        (
            "宝箱里装有\x1F\x5E\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x5E\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x9, 60)
    OP_70(0x9, 0x0)

    label("loc_1EC9")

    Jump("loc_1EFD")

    label("loc_1ECC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #31
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1EFD")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_20_1DF4 end

    def Function_21_1F0B(): pass

    label("Function_21_1F0B")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x265, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FE3")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xA, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_1F7A")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #32
        "\x07\x00得到了\x1F\xF6\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x132B)
    Jump("loc_1FE0")

    label("loc_1F7A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #33
        (
            "宝箱里装有\x1F\xF6\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xF6\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xA, 60)
    OP_70(0xA, 0x0)

    label("loc_1FE0")

    Jump("loc_2014")

    label("loc_1FE3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #34
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_2014")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_21_1F0B end

    def Function_22_2022(): pass

    label("Function_22_2022")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x265, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20FA")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xB, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_2091")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #35
        "\x07\x00得到了\x1F\xFE\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x132C)
    Jump("loc_20F7")

    label("loc_2091")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #36
        (
            "宝箱里装有\x1F\xFE\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFE\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xB, 60)
    OP_70(0xB, 0x0)

    label("loc_20F7")

    Jump("loc_212B")

    label("loc_20FA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #37
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_212B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_22_2022 end

    def Function_23_2139(): pass

    label("Function_23_2139")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x265, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2211")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xC, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_21A8")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #38
        "\x07\x00得到了\x1F\xFC\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x132D)
    Jump("loc_220E")

    label("loc_21A8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #39
        (
            "宝箱里装有\x1F\xFC\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFC\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xC, 60)
    OP_70(0xC, 0x0)

    label("loc_220E")

    Jump("loc_2242")

    label("loc_2211")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #40
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_2242")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_23_2139 end

    def Function_24_2250(): pass

    label("Function_24_2250")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x267, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23E3")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xD, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x267, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_232F")
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xB, 0x0, 0)
    OP_91(0xB, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_22A2():
        OP_91(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_22A2)

    def lambda_22BD():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x258)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_22BD)
    ClearChrFlags(0xB, 0x80)

    AnonymousTalk(    #41
        "\x07\x05魔兽出现了！\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x39E, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xB, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_230A"),
        (2, "loc_231C"),
        (1, "loc_232C"),
        (SWITCH_DEFAULT, "loc_232F"),
    )


    label("loc_230A")

    OP_A2(0x133F)
    OP_6F(0xD, 60)
    Sleep(500)
    Jump("loc_232F")

    label("loc_231C")

    OP_6F(0xD, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_232C")

    OP_B4(0x0)
    Return()

    label("loc_232F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2C7, 1)"), scpexpr(EXPR_END)), "loc_237E")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #42
        "\x07\x00得到了\x1F\xC7\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x133E)
    Jump("loc_23E0")

    label("loc_237E")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #43
        (
            "宝箱里装有\x1F\xC7\x02\x07\x00。 \x01",
            "所持物品已经满了，\x1F\xC7\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xD, 60)
    OP_70(0xD, 0x0)

    label("loc_23E0")

    Jump("loc_2412")

    label("loc_23E3")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #44
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_2412")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_24_2250 end

    def Function_25_2420(): pass

    label("Function_25_2420")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x266, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24F8")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xE, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x205, 1)"), scpexpr(EXPR_END)), "loc_248F")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #45
        "\x07\x00得到了\x1F\x05\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1330)
    Jump("loc_24F5")

    label("loc_248F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #46
        (
            "宝箱里装有\x1F\x05\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x05\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xE, 60)
    OP_70(0xE, 0x0)

    label("loc_24F5")

    Jump("loc_2529")

    label("loc_24F8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #47
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_2529")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_25_2420 end

    def Function_26_2537(): pass

    label("Function_26_2537")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x266, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_260F")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xF, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_25A6")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #48
        "\x07\x00得到了\x1F\xF6\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1331)
    Jump("loc_260C")

    label("loc_25A6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #49
        (
            "宝箱里装有\x1F\xF6\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xF6\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xF, 60)
    OP_70(0xF, 0x0)

    label("loc_260C")

    Jump("loc_2640")

    label("loc_260F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #50
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_2640")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_26_2537 end

    def Function_27_264E(): pass

    label("Function_27_264E")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x266, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2726")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x10, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_26BD")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #51
        "\x07\x00得到了\x1F\xFE\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1332)
    Jump("loc_2723")

    label("loc_26BD")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #52
        (
            "宝箱里装有\x1F\xFE\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFE\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x10, 60)
    OP_70(0x10, 0x0)

    label("loc_2723")

    Jump("loc_2757")

    label("loc_2726")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #53
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_2757")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_27_264E end

    def Function_28_2765(): pass

    label("Function_28_2765")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x266, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_283D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x11, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x181, 1)"), scpexpr(EXPR_END)), "loc_27D4")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #54
        "\x07\x00得到了\x1F\x81\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1333)
    Jump("loc_283A")

    label("loc_27D4")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #55
        (
            "宝箱里装有\x1F\x81\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x81\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x11, 60)
    OP_70(0x11, 0x0)

    label("loc_283A")

    Jump("loc_286E")

    label("loc_283D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #56
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_286E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_28_2765 end

    def Function_29_287C(): pass

    label("Function_29_287C")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x266, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2954")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x12, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x206, 1)"), scpexpr(EXPR_END)), "loc_28EB")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #57
        "\x07\x00得到了\x1F\x06\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1334)
    Jump("loc_2951")

    label("loc_28EB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #58
        (
            "宝箱里装有\x1F\x06\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x06\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x12, 60)
    OP_70(0x12, 0x0)

    label("loc_2951")

    Jump("loc_2985")

    label("loc_2954")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #59
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_2985")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_29_287C end

    def Function_30_2993(): pass

    label("Function_30_2993")

    TalkBegin(0xFF)
    Sleep(500)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #60
        "\x07\x02有空间投影装置。\x02",
    )

    CloseMessageWindow()

    Menu(
        0,
        10,
        10,
        0,
        (
            "【按右边的按钮】\x01",      # 0
            "【按中央的按钮】\x01",      # 1
            "【按左边的按钮】\x01",      # 2
            "【什么也不做】\x01",        # 3
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DF6")
    Sleep(500)
    OP_22(0x9C, 0x0, 0x64)
    Sleep(500)
    Sleep(500)
    OP_22(0x9D, 0x0, 0x64)
    LoadEffect(0x1, "map\\\\mp088_00.eff")
    PlayEffect(0x1, 0x0, 0xFF, -263120, 80, 93290, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AED")
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x80)
    ClearChrFlags(0x1B, 0x1)
    OP_9F(0x1B, 0xFF, 0xFF, 0xFF, 0xAA, 0x0)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1B, -263000, 500, 89640, 180)
    OP_43(0x1B, 0x1, 0x1, 0xC)
    SetChrFlags(0x1B, 0x40)
    OP_0D()
    Jump("loc_2DF3")

    label("loc_2AED")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B5C")
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x80)
    ClearChrFlags(0x1C, 0x1)
    OP_9F(0x1C, 0xFF, 0xFF, 0xFF, 0xAA, 0x0)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x1C, -263000, 500, 89640, 180)
    OP_43(0x1C, 0x1, 0x1, 0xC)
    SetChrFlags(0x1C, 0x40)
    OP_0D()
    Jump("loc_2DF3")

    label("loc_2B5C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BCB")
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x80)
    ClearChrFlags(0x1D, 0x1)
    OP_9F(0x1D, 0xFF, 0xFF, 0xFF, 0xAA, 0x0)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, -263000, 500, 89640, 180)
    OP_43(0x1D, 0x1, 0x1, 0xC)
    SetChrFlags(0x1D, 0x40)
    OP_0D()
    Jump("loc_2DF3")

    label("loc_2BCB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C3A")
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x80)
    ClearChrFlags(0x1E, 0x1)
    OP_9F(0x1E, 0xFF, 0xFF, 0xFF, 0xAA, 0x0)
    ClearChrFlags(0x1E, 0x80)
    SetChrPos(0x1E, -263000, 500, 89640, 180)
    OP_43(0x1E, 0x1, 0x1, 0xC)
    SetChrFlags(0x1E, 0x40)
    OP_0D()
    Jump("loc_2DF3")

    label("loc_2C3A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CA9")
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x80)
    ClearChrFlags(0x1F, 0x1)
    OP_9F(0x1F, 0xFF, 0xFF, 0xFF, 0xAA, 0x0)
    ClearChrFlags(0x1F, 0x80)
    SetChrPos(0x1F, -263000, 500, 89640, 180)
    OP_43(0x1F, 0x1, 0x1, 0xC)
    SetChrFlags(0x1F, 0x40)
    OP_0D()
    Jump("loc_2DF3")

    label("loc_2CA9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D18")
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x80)
    ClearChrFlags(0x20, 0x1)
    OP_9F(0x20, 0xFF, 0xFF, 0xFF, 0xAA, 0x0)
    ClearChrFlags(0x20, 0x80)
    SetChrPos(0x20, -263000, 500, 89640, 180)
    OP_43(0x20, 0x1, 0x1, 0xC)
    SetChrFlags(0x20, 0x40)
    OP_0D()
    Jump("loc_2DF3")

    label("loc_2D18")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D87")
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x80)
    ClearChrFlags(0x21, 0x1)
    OP_9F(0x21, 0xFF, 0xFF, 0xFF, 0xAA, 0x0)
    ClearChrFlags(0x21, 0x80)
    SetChrPos(0x21, -263000, 500, 89640, 180)
    OP_43(0x21, 0x1, 0x1, 0xC)
    SetChrFlags(0x21, 0x40)
    OP_0D()
    Jump("loc_2DF3")

    label("loc_2D87")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DF3")
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x80)
    ClearChrFlags(0x22, 0x1)
    OP_9F(0x22, 0xFF, 0xFF, 0xFF, 0xAA, 0x0)
    ClearChrFlags(0x22, 0x80)
    SetChrPos(0x22, -263000, 500, 89640, 180)
    OP_43(0x22, 0x1, 0x1, 0xC)
    SetChrFlags(0x22, 0x40)
    OP_0D()

    label("loc_2DF3")

    Jump("loc_2F24")

    label("loc_2DF6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EC8")
    Sleep(500)
    OP_22(0x9C, 0x0, 0x64)
    Sleep(500)
    Sleep(500)
    OP_22(0x9D, 0x0, 0x64)
    LoadEffect(0x1, "map\\\\mp088_00.eff")
    PlayEffect(0x1, 0x0, 0xFF, -263120, 80, 93290, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x80)
    ClearChrFlags(0x10, 0x1)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0xAA, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -263000, 500, 89640, 180)
    OP_43(0x10, 0x1, 0x1, 0xC)
    SetChrFlags(0x10, 0x40)
    OP_0D()
    Jump("loc_2F24")

    label("loc_2EC8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F17")
    Sleep(500)
    OP_22(0x9C, 0x0, 0x64)
    Sleep(500)
    OP_82(0x0, 0x2)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x80)
    Jump("loc_2F24")

    label("loc_2F17")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F24")

    label("loc_2F24")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_30_2993 end

    def Function_31_2F31(): pass

    label("Function_31_2F31")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F82")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #61
        "\x07\x05导力好像停止了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Jump("loc_3140")

    label("loc_2F82")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #62
        "\x07\x05这是一台可供旅行者回复体力的导力器装置。\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "在这里休息\x01",      # 0
            "离开\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3125")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_82(0x2, 0x2)
    PlayEffect(0x2, 0x2, 0xFF, -3200, 1000, 30680, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    OP_6F(0x16, 0)
    OP_70(0x16, 0x32)
    OP_73(0x16)
    OP_20(0xBB8)
    OP_22(0xC, 0x0, 0x64)
    OP_82(0x2, 0x2)
    LoadEffect(0x3, "map\\\\mp027_01.eff")
    PlayEffect(0x3, 0x3, 0xFF, -3200, 1000, 30680, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0xFF, 0xFE, 0x0)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_82(0x3, 0x2)
    PlayEffect(0x2, 0x2, 0xFF, -3200, 1000, 30680, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    OP_6F(0x16, 0)
    OP_1E()
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_3125")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_313F")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_313F")

    Return()

    label("loc_3140")

    Return()

    # Function_31_2F31 end

    def Function_32_3141(): pass

    label("Function_32_3141")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3192")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #63
        "\x07\x05导力好像停止了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Jump("loc_3350")

    label("loc_3192")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #64
        "\x07\x05这是一台可供旅行者回复体力的导力器装置。\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "在这里休息\x01",      # 0
            "离开\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3335")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_82(0x4, 0x2)
    PlayEffect(0x4, 0x4, 0xFF, -261769, 1000, 35590, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    OP_6F(0x17, 0)
    OP_70(0x17, 0x32)
    OP_73(0x17)
    OP_20(0xBB8)
    OP_22(0xC, 0x0, 0x64)
    OP_82(0x4, 0x2)
    LoadEffect(0x5, "map\\\\mp027_01.eff")
    PlayEffect(0x5, 0x5, 0xFF, -261769, 1000, 35590, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0xFF, 0xFE, 0x0)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_82(0x5, 0x2)
    PlayEffect(0x4, 0x4, 0xFF, -261769, 1000, 35590, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    OP_6F(0x17, 0)
    OP_1E()
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_3335")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_334F")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_334F")

    Return()

    label("loc_3350")

    Return()

    # Function_32_3141 end

    SaveToFile()

Try(main)
