from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        'Mouki',                                # 14
        'Dorothy',                              # 15
        'Bleublanc',                            # 16
        'Bleublanc Shadow',                     # 17
        'Monster',                              # 18
        'Man-o-North',                          # 19
        'Sieg',                                 # 20
        'Gospel',                               # 21
        '影縫い用の針①',                       # 22
        '影縫い用の針②',                       # 23
        '影縫い用の針③',                       # 24
        '影縫い用の針④',                       # 25
        '影縫い用の針⑤',                       # 26
        'ターゲット用カメラ',                   # 27
        'エステル幻影',                         # 28
        'ヨシュア幻影',                         # 29
        'シェラ幻影',                           # 30
        'オリビエ幻影',                         # 31
        'クローゼ幻影',                         # 32
        'アガット幻影',                         # 33
        'ティータ幻影',                         # 34
        'ジン幻影',                             # 35
        '',                                     # 36
        '',                                     # 37
        '',                                     # 38
        '',                                     # 39
        '',                                     # 40
        '',                                     # 41
        '',                                     # 42
        '',                                     # 43
        '',                                     # 44
        '',                                     # 45
        '',                                     # 46
        '',                                     # 47
        '',                                     # 48
        '',                                     # 49
        '',                                     # 50
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
        "Function_4_DE8",          # 04, 4
        "Function_5_104F",         # 05, 5
        "Function_6_107F",         # 06, 6
        "Function_7_10D7",         # 07, 7
        "Function_8_1155",         # 08, 8
        "Function_9_11D3",         # 09, 9
        "Function_10_12AA",        # 0A, 10
        "Function_11_138A",        # 0B, 11
        "Function_12_14CF",        # 0C, 12
        "Function_13_15E4",        # 0D, 13
        "Function_14_1732",        # 0E, 14
        "Function_15_1872",        # 0F, 15
        "Function_16_1984",        # 10, 16
        "Function_17_1BA3",        # 11, 17
        "Function_18_1CD8",        # 12, 18
        "Function_19_1E64",        # 13, 19
        "Function_20_1FD2",        # 14, 20
        "Function_21_2131",        # 15, 21
        "Function_22_22C8",        # 16, 22
        "Function_23_240B",        # 17, 23
        "Function_24_2554",        # 18, 24
        "Function_25_2773",        # 19, 25
        "Function_26_28F8",        # 1A, 26
        "Function_27_2A50",        # 1B, 27
        "Function_28_2B8A",        # 1C, 28
        "Function_29_2CE1",        # 1D, 29
        "Function_30_2E52",        # 1E, 30
        "Function_31_340D",        # 1F, 31
        "Function_32_362F",        # 20, 32
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
            "#150FFind something fun for me,\x01",
            "please!\x02\x03",

            "I'd looove to take a picture\x01",
            "of a ghost!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xE)
    Return()

    # Function_3_D8A end

    def Function_4_DE8(): pass

    label("Function_4_DE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25F, 6)), scpexpr(EXPR_END)), "loc_DF0")
    Return()

    label("loc_DF0")

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
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xD, 0, 500, 1500, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Sleep(2000)

    def lambda_F27():
        OP_6D(-287740, 0, -75300, 3000)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_F27)

    def lambda_F3F():
        OP_6B(2500, 3000)
        ExitThread()

    QueueWorkItem(0xD, 3, lambda_F3F)
    SetChrChipByIndex(0xD, 1)
    SetChrSubChip(0xD, 0)
    OP_43(0xD, 0x0, 0x0, 0x2)

    def lambda_F60():
        OP_8F(0xFE, 0xFFFB9ABA, 0x0, 0xFFFEE22E, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_F60)
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

    def lambda_FD3():
        OP_99(0xFE, 0x0, 0x1, 0x7D0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_FD3)
    Sleep(500)

    def lambda_FE8():
        OP_99(0xFE, 0x1, 0x5, 0x1388)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_FE8)

    def lambda_FF8():
        OP_8F(0xFE, 0xFFFB9ABA, 0x0, 0xFFFED1C6, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_FF8)
    Sleep(250)
    OP_44(0xD, 0x1)
    OP_44(0xD, 0x2)
    Battle(0x39D, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_103B"),
        (0, "loc_1040"),
        (2, "loc_1047"),
        (SWITCH_DEFAULT, "loc_104E"),
    )


    label("loc_103B")

    OP_B4(0x0)
    Jump("loc_104E")

    label("loc_1040")

    Call(0, 9)
    Jump("loc_104E")

    label("loc_1047")

    Call(0, 10)
    Jump("loc_104E")

    label("loc_104E")

    Return()

    # Function_4_DE8 end

    def Function_5_104F(): pass

    label("Function_5_104F")

    SetChrChipByIndex(0x101, 33)
    SetChrSubChip(0x101, 0)
    OP_8E(0xFE, 0xFFFB9ABA, 0x0, 0xFFFED1C6, 0xFA0, 0x0)
    OP_8C(0xFE, 0, 400)
    SetChrChipByIndex(0x101, 13)
    SetChrSubChip(0x101, 0)
    Return()

    # Function_5_104F end

    def Function_6_107F(): pass

    label("Function_6_107F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1093")
    SetChrChipByIndex(0x106, 35)
    SetChrSubChip(0x106, 0)
    Jump("loc_109D")

    label("loc_1093")

    SetChrChipByIndex(0x103, 34)
    SetChrSubChip(0x103, 0)

    label("loc_109D")

    OP_8E(0xFE, 0xFFFB9DEE, 0x0, 0xFFFECE7E, 0xFA0, 0x0)
    OP_8C(0xFE, 0, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_10CC")
    SetChrChipByIndex(0x106, 15)
    SetChrSubChip(0x106, 0)
    Jump("loc_10D6")

    label("loc_10CC")

    SetChrChipByIndex(0x103, 14)
    SetChrSubChip(0x103, 0)

    label("loc_10D6")

    Return()

    # Function_6_107F end

    def Function_7_10D7(): pass

    label("Function_7_10D7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10F1")
    SetChrChipByIndex(0x104, 36)
    SetChrSubChip(0x104, 0)
    Jump("loc_1108")

    label("loc_10F1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1108")
    SetChrChipByIndex(0x105, 37)
    SetChrSubChip(0x105, 0)

    label("loc_1108")

    OP_8E(0xFE, 0xFFFB9722, 0x0, 0xFFFECDB6, 0xFA0, 0x0)
    OP_8C(0xFE, 0, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_113D")
    SetChrChipByIndex(0x104, 16)
    SetChrSubChip(0x104, 0)
    Jump("loc_1154")

    label("loc_113D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1154")
    SetChrChipByIndex(0x105, 17)
    SetChrSubChip(0x105, 0)

    label("loc_1154")

    Return()

    # Function_7_10D7 end

    def Function_8_1155(): pass

    label("Function_8_1155")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_116F")
    SetChrChipByIndex(0x104, 36)
    SetChrSubChip(0x104, 0)
    Jump("loc_1186")

    label("loc_116F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1186")
    SetChrChipByIndex(0x105, 37)
    SetChrSubChip(0x105, 0)

    label("loc_1186")

    OP_8E(0xFE, 0xFFFB99AC, 0x0, 0xFFFECA14, 0xFA0, 0x0)
    OP_8C(0xFE, 0, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11BB")
    SetChrChipByIndex(0x104, 16)
    SetChrSubChip(0x104, 0)
    Jump("loc_11D2")

    label("loc_11BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11D2")
    SetChrChipByIndex(0x105, 17)
    SetChrSubChip(0x105, 0)

    label("loc_11D2")

    Return()

    # Function_8_1155 end

    def Function_9_11D3(): pass

    label("Function_9_11D3")

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

    # Function_9_11D3 end

    def Function_10_12AA(): pass

    label("Function_10_12AA")

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

    # Function_10_12AA end

    def Function_11_138A(): pass

    label("Function_11_138A")

    OP_EA(0x2, 0xA4, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x264, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1462")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_13FB")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #1
        "Found \x1F\xF6\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1320)
    Jump("loc_145F")

    label("loc_13FB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "Found \x1F\xF6\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xF6\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_145F")

    Jump("loc_14C1")

    label("loc_1462")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #3
        (
            "\x07\x05A single tumbleweed rolls from one side of the\x01",
            "chest to another.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_14C1")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_11_138A end

    def Function_12_14CF(): pass

    label("Function_12_14CF")

    OP_EA(0x2, 0xA5, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x264, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15A7")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_1540")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #4
        "Found \x1F\xFC\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1321)
    Jump("loc_15A4")

    label("loc_1540")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "Found \x1F\xFC\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFC\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_15A4")

    Jump("loc_15D6")

    label("loc_15A7")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x05Yep, it's empty.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_15D6")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_12_14CF end

    def Function_13_15E4(): pass

    label("Function_13_15E4")

    OP_EA(0x2, 0xA6, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x264, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16BC")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x6C, 1)"), scpexpr(EXPR_END)), "loc_1655")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #7
        "Found \x1F\x6C\x00\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1322)
    Jump("loc_16B9")

    label("loc_1655")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        (
            "Found \x1F\x6C\x00\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x6C\x00\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_16B9")

    Jump("loc_1724")

    label("loc_16BC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #9
        (
            "\x07\x05Oh, boy! You came back to visit me! Does that\x01",
            "mean...you're my first fan?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1724")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_13_15E4 end

    def Function_14_1732(): pass

    label("Function_14_1732")

    OP_EA(0x2, 0xA7, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x264, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_180A")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_17A3")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #10
        "Found \x1F\xFE\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1323)
    Jump("loc_1807")

    label("loc_17A3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        (
            "Found \x1F\xFE\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFE\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_1807")

    Jump("loc_1864")

    label("loc_180A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #12
        (
            "\x07\x05What you have taken from this chest, you\x01",
            "can never restore.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1864")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_14_1732 end

    def Function_15_1872(): pass

    label("Function_15_1872")

    OP_EA(0x2, 0xA8, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x264, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_194A")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x267, 1)"), scpexpr(EXPR_END)), "loc_18E3")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #13
        "Found \x1F\x67\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1324)
    Jump("loc_1947")

    label("loc_18E3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        (
            "Found \x1F\x67\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x67\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_1947")

    Jump("loc_1976")

    label("loc_194A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #15
        "\x07\x05Well... Crap.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1976")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_15_1872 end

    def Function_16_1984(): pass

    label("Function_16_1984")

    OP_EA(0x2, 0xA9, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x264, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B1F")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x264, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A6E")
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_91(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_19DB():
        OP_91(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_19DB)

    def lambda_19F6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x258)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_19F6)
    ClearChrFlags(0x8, 0x80)

    AnonymousTalk(    #16
        "\x07\x05Monsters appeared!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x39E, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1A49"),
        (2, "loc_1A5B"),
        (1, "loc_1A6B"),
        (SWITCH_DEFAULT, "loc_1A6E"),
    )


    label("loc_1A49")

    OP_A2(0x1326)
    OP_6F(0x5, 60)
    Sleep(500)
    Jump("loc_1A6E")

    label("loc_1A5B")

    OP_6F(0x5, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_1A6B")

    OP_B4(0x0)
    Return()

    label("loc_1A6E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x135, 1)"), scpexpr(EXPR_END)), "loc_1ABA")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #17
        "Found \x1F\x35\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1325)
    Jump("loc_1B1C")

    label("loc_1ABA")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #18
        (
            "Found \x1F\x35\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x35\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)

    label("loc_1B1C")

    Jump("loc_1B95")

    label("loc_1B1F")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #19
        (
            "\x07\x05This is the 56th chest you've opened! Congrats!\x01",
            "Nah, just kidding. I'm not even COUNTING.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1B95")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_16_1984 end

    def Function_17_1BA3(): pass

    label("Function_17_1BA3")

    OP_EA(0x2, 0xAA, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x264, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C7B")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FA, 1)"), scpexpr(EXPR_END)), "loc_1C14")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #20
        "Found \x1F\xFA\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1327)
    Jump("loc_1C78")

    label("loc_1C14")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #21
        (
            "Found \x1F\xFA\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFA\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)

    label("loc_1C78")

    Jump("loc_1CCA")

    label("loc_1C7B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #22
        "\x07\x05It's a vase! It's a pot! No... It's Super Chest!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1CCA")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_17_1BA3 end

    def Function_18_1CD8(): pass

    label("Function_18_1CD8")

    OP_EA(0x2, 0xAB, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x265, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DB0")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x7, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_1D49")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #23
        "Found \x1F\xFE\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1328)
    Jump("loc_1DAD")

    label("loc_1D49")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #24
        (
            "Found \x1F\xFE\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFE\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x7, 60)
    OP_70(0x7, 0x0)

    label("loc_1DAD")

    Jump("loc_1E56")

    label("loc_1DB0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #25
        (
            "\x07\x05No matter how desperately you loot, you can't\x01",
            "find anything in the chest. The chest gives\x01",
            "you a smug look, prompting you to scowl back.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1E56")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_18_1CD8 end

    def Function_19_1E64(): pass

    label("Function_19_1E64")

    OP_EA(0x2, 0xAC, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x265, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F3C")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x8, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x25F, 1)"), scpexpr(EXPR_END)), "loc_1ED5")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #26
        "Found \x1F\x5F\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1329)
    Jump("loc_1F39")

    label("loc_1ED5")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #27
        (
            "Found \x1F\x5F\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x5F\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x8, 60)
    OP_70(0x8, 0x0)

    label("loc_1F39")

    Jump("loc_1FC4")

    label("loc_1F3C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #28
        (
            "\x07\x05As you open the chest, a number of trapped,\x01",
            "screaming souls come swirling out.\x01",
            "...That's probably normal.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1FC4")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_19_1E64 end

    def Function_20_1FD2(): pass

    label("Function_20_1FD2")

    OP_EA(0x2, 0xAD, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x265, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20AA")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x9, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x15E, 1)"), scpexpr(EXPR_END)), "loc_2043")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #29
        "Found \x1F\x5E\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x132A)
    Jump("loc_20A7")

    label("loc_2043")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #30
        (
            "Found \x1F\x5E\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x5E\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x9, 60)
    OP_70(0x9, 0x0)

    label("loc_20A7")

    Jump("loc_2123")

    label("loc_20AA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #31
        (
            "\x07\x05The chest is empty, but at least the interior is\x01",
            "really nice. Velvet-lined and everything!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_2123")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_20_1FD2 end

    def Function_21_2131(): pass

    label("Function_21_2131")

    OP_EA(0x2, 0xAE, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x265, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2209")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xA, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_21A2")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #32
        "Found \x1F\xF6\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x132B)
    Jump("loc_2206")

    label("loc_21A2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #33
        (
            "Found \x1F\xF6\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xF6\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xA, 60)
    OP_70(0xA, 0x0)

    label("loc_2206")

    Jump("loc_22BA")

    label("loc_2209")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #34
        (
            "\x07\x05You see a kitten curled up in the chest. Aww...\x01",
            "It's so cute... As a result of acute kittenitis, you\x01",
            "forgot to take whatever else was left inside.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_22BA")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_21_2131 end

    def Function_22_22C8(): pass

    label("Function_22_22C8")

    OP_EA(0x2, 0xAF, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x265, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23A0")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xB, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_2339")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #35
        "Found \x1F\xFE\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x132C)
    Jump("loc_239D")

    label("loc_2339")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #36
        (
            "Found \x1F\xFE\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFE\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xB, 60)
    OP_70(0xB, 0x0)

    label("loc_239D")

    Jump("loc_23FD")

    label("loc_23A0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #37
        (
            "\x07\x05You're... You're opening me again? Heeheehee...\x01",
            "How naughty...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_23FD")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_22_22C8 end

    def Function_23_240B(): pass

    label("Function_23_240B")

    OP_EA(0x2, 0xB0, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x265, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24E3")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xC, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_247C")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #38
        "Found \x1F\xFC\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x132D)
    Jump("loc_24E0")

    label("loc_247C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #39
        (
            "Found \x1F\xFC\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFC\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xC, 60)
    OP_70(0xC, 0x0)

    label("loc_24E0")

    Jump("loc_2546")

    label("loc_24E3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #40
        (
            "\x07\x05Check as many times as you want. Nothing will\x01",
            "ever be in here again.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_2546")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_23_240B end

    def Function_24_2554(): pass

    label("Function_24_2554")

    OP_EA(0x2, 0xB1, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x267, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26EF")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xD, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x267, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_263E")
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xB, 0x0, 0)
    OP_91(0xB, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_25AB():
        OP_91(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_25AB)

    def lambda_25C6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x258)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_25C6)
    ClearChrFlags(0xB, 0x80)

    AnonymousTalk(    #41
        "\x07\x05Monsters appeared!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x39E, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xB, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_2619"),
        (2, "loc_262B"),
        (1, "loc_263B"),
        (SWITCH_DEFAULT, "loc_263E"),
    )


    label("loc_2619")

    OP_A2(0x133F)
    OP_6F(0xD, 60)
    Sleep(500)
    Jump("loc_263E")

    label("loc_262B")

    OP_6F(0xD, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_263B")

    OP_B4(0x0)
    Return()

    label("loc_263E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2C7, 1)"), scpexpr(EXPR_END)), "loc_268A")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #42
        "Found \x1F\xC7\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x133E)
    Jump("loc_26EC")

    label("loc_268A")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #43
        (
            "Found \x1F\xC7\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xC7\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xD, 60)
    OP_70(0xD, 0x0)

    label("loc_26EC")

    Jump("loc_2765")

    label("loc_26EF")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #44
        (
            "\x07\x05Ever notice nobody else is running around\x01",
            "looting these things? Why do you think that is?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_2765")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_24_2554 end

    def Function_25_2773(): pass

    label("Function_25_2773")

    OP_EA(0x2, 0xB2, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x266, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_284B")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xE, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x205, 1)"), scpexpr(EXPR_END)), "loc_27E4")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #45
        "Found \x1F\x05\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1330)
    Jump("loc_2848")

    label("loc_27E4")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #46
        (
            "Found \x1F\x05\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x05\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xE, 60)
    OP_70(0xE, 0x0)

    label("loc_2848")

    Jump("loc_28EA")

    label("loc_284B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #47
        (
            "\x07\x05Look, I know you think it would be wonderful\x01",
            "if we could all just loot infinite amounts of\x01",
            "treasure from the same chest, but no.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_28EA")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_25_2773 end

    def Function_26_28F8(): pass

    label("Function_26_28F8")

    OP_EA(0x2, 0xB3, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x266, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29D0")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xF, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_2969")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #48
        "Found \x1F\xF6\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1331)
    Jump("loc_29CD")

    label("loc_2969")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #49
        (
            "Found \x1F\xF6\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xF6\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xF, 60)
    OP_70(0xF, 0x0)

    label("loc_29CD")

    Jump("loc_2A42")

    label("loc_29D0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #50
        (
            "\x07\x05There's nothing in this chest, but you imagine all\x01",
            "the things that COULD'VE been...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_2A42")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_26_28F8 end

    def Function_27_2A50(): pass

    label("Function_27_2A50")

    OP_EA(0x2, 0xB4, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x266, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B28")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x10, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_2AC1")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #51
        "Found \x1F\xFE\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1332)
    Jump("loc_2B25")

    label("loc_2AC1")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #52
        (
            "Found \x1F\xFE\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFE\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x10, 60)
    OP_70(0x10, 0x0)

    label("loc_2B25")

    Jump("loc_2B7C")

    label("loc_2B28")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #53
        (
            "\x07\x05Strange. This chest had something BEFORE,\x01",
            "at least...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_2B7C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_27_2A50 end

    def Function_28_2B8A(): pass

    label("Function_28_2B8A")

    OP_EA(0x2, 0xB5, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x266, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C62")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x11, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x181, 1)"), scpexpr(EXPR_END)), "loc_2BFB")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #54
        "Found \x1F\x81\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1333)
    Jump("loc_2C5F")

    label("loc_2BFB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #55
        (
            "Found \x1F\x81\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x81\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x11, 60)
    OP_70(0x11, 0x0)

    label("loc_2C5F")

    Jump("loc_2CD3")

    label("loc_2C62")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #56
        (
            "\x07\x05PROTIP: You can hide the body in an empty\x01",
            "chest. I won't tell anyone what you did.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_2CD3")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_28_2B8A end

    def Function_29_2CE1(): pass

    label("Function_29_2CE1")

    OP_EA(0x2, 0xB6, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x266, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DB9")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x12, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x206, 1)"), scpexpr(EXPR_END)), "loc_2D52")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #57
        "Found \x1F\x06\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1334)
    Jump("loc_2DB6")

    label("loc_2D52")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #58
        (
            "Found \x1F\x06\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x06\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x12, 60)
    OP_70(0x12, 0x0)

    label("loc_2DB6")

    Jump("loc_2E44")

    label("loc_2DB9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #59
        (
            "\x07\x05You look at the chest. The chest looks at you.\x01",
            "You both know that neither of you have anything\x01",
            "left to give.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_2E44")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_29_2CE1 end

    def Function_30_2E52(): pass

    label("Function_30_2E52")

    TalkBegin(0xFF)
    Sleep(500)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #60
        "\x07\x02There is a hologram projector here.\x02",
    )

    CloseMessageWindow()

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Press Right Button]\x01",       # 0
            "[Press Center Button]\x01",      # 1
            "[Press Left Button]\x01",        # 2
            "[Do Nothing]\x01",               # 3
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32D2")
    Sleep(500)
    OP_22(0x9C, 0x0, 0x64)
    Sleep(500)
    Sleep(500)
    OP_22(0x9D, 0x0, 0x64)
    LoadEffect(0x1, "map\\\\mp088_00.eff")
    PlayEffect(0x1, 0x0, 0xFF, -263120, 80, 93290, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FC9")
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
    Jump("loc_32CF")

    label("loc_2FC9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3038")
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
    Jump("loc_32CF")

    label("loc_3038")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30A7")
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
    Jump("loc_32CF")

    label("loc_30A7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3116")
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
    Jump("loc_32CF")

    label("loc_3116")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3185")
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
    Jump("loc_32CF")

    label("loc_3185")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31F4")
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
    Jump("loc_32CF")

    label("loc_31F4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3263")
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
    Jump("loc_32CF")

    label("loc_3263")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32CF")
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

    label("loc_32CF")

    Jump("loc_3400")

    label("loc_32D2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33A4")
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
    Jump("loc_3400")

    label("loc_33A4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33F3")
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
    Jump("loc_3400")

    label("loc_33F3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3400")

    label("loc_3400")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_30_2E52 end

    def Function_31_340D(): pass

    label("Function_31_340D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3473")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #61
        "\x07\x05Orbal energy appears to be shut down.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Jump("loc_362E")

    label("loc_3473")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #62
        "\x07\x05There is an orbment charging station here.\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "Rest\x01",       # 0
            "Leave\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3613")
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

    label("loc_3613")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_362D")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_362D")

    Return()

    label("loc_362E")

    Return()

    # Function_31_340D end

    def Function_32_362F(): pass

    label("Function_32_362F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3695")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #63
        "\x07\x05Orbal energy appears to be shut down.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Jump("loc_3850")

    label("loc_3695")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #64
        "\x07\x05There is an orbment charging station here.\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "Rest\x01",       # 0
            "Leave\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3835")
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

    label("loc_3835")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_384F")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_384F")

    Return()

    label("loc_3850")

    Return()

    # Function_32_362F end

    SaveToFile()

Try(main)
