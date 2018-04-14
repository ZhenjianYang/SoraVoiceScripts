from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'R2200   ._SN',
        MapName             = 'Ruan',
        Location            = 'R2200.x',
        MapIndex            = 101,
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
        '特蕾莎院长',                           # 9
        '克拉姆',                               # 10
        '波利',                                 # 11
        '玛丽',                                 # 12
        '达尼艾尔',                             # 13
        '克鲁茨',                               # 14
        '亚妮拉丝',                             # 15
        '库拉茨',                               # 16
        '卡露娜',                               # 17
        '王国军士兵',                           # 18
        '王国军士兵',                           # 19
        '王国军士兵',                           # 20
        '装甲猎豹',                             # 21
        '装甲猎豹',                             # 22
        '装甲猎豹',                             # 23
        '装甲猎豹',                             # 24
        '装甲猎豹',                             # 25
        '装甲猎豹',                             # 26
        '装甲猎豹',                             # 27
        '装甲猎豹',                             # 28
        '装甲猎豹',                             # 29
        '装甲猎豹',                             # 30
        '目标用照相机',                         # 31
        '目标',                                 # 32
        '目标',                                 # 33
        '目标',                                 # 34
        '目标',                                 # 35
        '玛诺利亚村方向',                       # 36
        '玛西亚孤儿院方向',                     # 37
        '卢安方向',                             # 38
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
        'ED6_DT29/CH12100 ._CH',             # 00
        'ED6_DT29/CH12101 ._CH',             # 01
        'ED6_DT29/CH12150 ._CH',             # 02
        'ED6_DT29/CH12151 ._CH',             # 03
        'ED6_DT07/CH02570 ._CH',             # 04
        'ED6_DT07/CH02590 ._CH',             # 05
        'ED6_DT07/CH02500 ._CH',             # 06
        'ED6_DT07/CH02630 ._CH',             # 07
        'ED6_DT07/CH02640 ._CH',             # 08
        'ED6_DT07/CH00412 ._CH',             # 09
        'ED6_DT07/CH00420 ._CH',             # 0A
        'ED6_DT07/CH00390 ._CH',             # 0B
        'ED6_DT07/CH00400 ._CH',             # 0C
        'ED6_DT07/CH00320 ._CH',             # 0D
        'ED6_DT29/CH12330 ._CH',             # 0E
        'ED6_DT07/CH00411 ._CH',             # 0F
        'ED6_DT07/CH00412 ._CH',             # 10
        'ED6_DT07/CH00415 ._CH',             # 11
        'ED6_DT07/CH00416 ._CH',             # 12
        'ED6_DT07/CH00421 ._CH',             # 13
        'ED6_DT07/CH00422 ._CH',             # 14
        'ED6_DT07/CH00391 ._CH',             # 15
        'ED6_DT07/CH00392 ._CH',             # 16
        'ED6_DT07/CH00401 ._CH',             # 17
        'ED6_DT07/CH00321 ._CH',             # 18
        'ED6_DT07/CH00326 ._CH',             # 19
        'ED6_DT29/CH12331 ._CH',             # 1A
        'ED6_DT29/CH12333 ._CH',             # 1B
        'ED6_DT07/CH00321 ._CH',             # 1C
        'ED6_DT07/CH01640 ._CH',             # 1D
        'ED6_DT07/CH01620 ._CH',             # 1E
        'ED6_DT07/CH01630 ._CH',             # 1F
        'ED6_DT07/CH01260 ._CH',             # 20
        'ED6_DT07/CH01240 ._CH',             # 21
    )

    AddCharChipPat(
        'ED6_DT29/CH12100P._CP',             # 00
        'ED6_DT29/CH12101P._CP',             # 01
        'ED6_DT29/CH12150P._CP',             # 02
        'ED6_DT29/CH12151P._CP',             # 03
        'ED6_DT07/CH02570P._CP',             # 04
        'ED6_DT07/CH02590P._CP',             # 05
        'ED6_DT07/CH02500P._CP',             # 06
        'ED6_DT07/CH02630P._CP',             # 07
        'ED6_DT07/CH02640P._CP',             # 08
        'ED6_DT07/CH00412P._CP',             # 09
        'ED6_DT07/CH00420P._CP',             # 0A
        'ED6_DT07/CH00390P._CP',             # 0B
        'ED6_DT07/CH00400P._CP',             # 0C
        'ED6_DT07/CH00320P._CP',             # 0D
        'ED6_DT29/CH12330P._CP',             # 0E
        'ED6_DT07/CH00411P._CP',             # 0F
        'ED6_DT07/CH00412P._CP',             # 10
        'ED6_DT07/CH00415P._CP',             # 11
        'ED6_DT07/CH00416P._CP',             # 12
        'ED6_DT07/CH00421P._CP',             # 13
        'ED6_DT07/CH00422P._CP',             # 14
        'ED6_DT07/CH00391P._CP',             # 15
        'ED6_DT07/CH00392P._CP',             # 16
        'ED6_DT07/CH00401P._CP',             # 17
        'ED6_DT07/CH00321P._CP',             # 18
        'ED6_DT07/CH00326P._CP',             # 19
        'ED6_DT29/CH12331P._CP',             # 1A
        'ED6_DT29/CH12333P._CP',             # 1B
        'ED6_DT07/CH00321P._CP',             # 1C
        'ED6_DT07/CH01640P._CP',             # 1D
        'ED6_DT07/CH01620P._CP',             # 1E
        'ED6_DT07/CH01630P._CP',             # 1F
        'ED6_DT07/CH01260P._CP',             # 20
        'ED6_DT07/CH01240P._CP',             # 21
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
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
        Unknown3            = 14,
        ChipIndex           = 0xE,
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
        Unknown3            = 14,
        ChipIndex           = 0xE,
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
        Unknown3            = 14,
        ChipIndex           = 0xE,
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
        Unknown3            = 14,
        ChipIndex           = 0xE,
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
        Unknown3            = 14,
        ChipIndex           = 0xE,
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
        Unknown3            = 14,
        ChipIndex           = 0xE,
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
        Unknown3            = 14,
        ChipIndex           = 0xE,
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
        Unknown3            = 14,
        ChipIndex           = 0xE,
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
        Unknown3            = 14,
        ChipIndex           = 0xE,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -139370,
        Z                   = -2020,
        Y                   = 15120,
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
        X                   = -28630,
        Z                   = -1990,
        Y                   = 79340,
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
        X                   = 7410,
        Z                   = -2000,
        Y                   = 29980,
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
        X                   = -96260,
        Z                   = -1950,
        Y                   = 27960,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x184,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -104740,
        Z                   = -5970,
        Y                   = 11000,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x18F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -81100,
        Z                   = -5870,
        Y                   = 13330,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x18E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -88220,
        Z                   = -5960,
        Y                   = 9810,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x18F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -114230,
        TriggerZ            = -6050,
        TriggerY            = 11770,
        TriggerRange        = 1000,
        ActorX              = -114730,
        ActorZ              = -6040,
        ActorY              = 12270,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -77980,
        TriggerZ            = -6870,
        TriggerY            = -11780,
        TriggerRange        = 1000,
        ActorX              = -77540,
        ActorZ              = -6730,
        ActorY              = -11140,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -21830,
        TriggerZ            = -2000,
        TriggerY            = 37790,
        TriggerRange        = 1500,
        ActorX              = -21830,
        ActorZ              = -800,
        ActorY              = 37790,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 48,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -18840,
        TriggerZ            = -2000,
        TriggerY            = 33860,
        TriggerRange        = 1500,
        ActorX              = -18840,
        ActorZ              = -500,
        ActorY              = 33860,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 49,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_67A",          # 00, 0
        "Function_1_6D9",          # 01, 1
        "Function_2_72D",          # 02, 2
        "Function_3_8AA",          # 03, 3
        "Function_4_9C1",          # 04, 4
        "Function_5_AD8",          # 05, 5
        "Function_6_FCD",          # 06, 6
        "Function_7_1327",         # 07, 7
        "Function_8_2CC9",         # 08, 8
        "Function_9_2D12",         # 09, 9
        "Function_10_2D2C",        # 0A, 10
        "Function_11_2D46",        # 0B, 11
        "Function_12_2D60",        # 0C, 12
        "Function_13_2D7A",        # 0D, 13
        "Function_14_2D94",        # 0E, 14
        "Function_15_2DAE",        # 0F, 15
        "Function_16_2E21",        # 10, 16
        "Function_17_2E94",        # 11, 17
        "Function_18_2F07",        # 12, 18
        "Function_19_2F7A",        # 13, 19
        "Function_20_2FE2",        # 14, 20
        "Function_21_304A",        # 15, 21
        "Function_22_3069",        # 16, 22
        "Function_23_3088",        # 17, 23
        "Function_24_30A7",        # 18, 24
        "Function_25_30C0",        # 19, 25
        "Function_26_318D",        # 1A, 26
        "Function_27_3253",        # 1B, 27
        "Function_28_3319",        # 1C, 28
        "Function_29_33DF",        # 1D, 29
        "Function_30_3440",        # 1E, 30
        "Function_31_34A8",        # 1F, 31
        "Function_32_3504",        # 20, 32
        "Function_33_3545",        # 21, 33
        "Function_34_35AD",        # 22, 34
        "Function_35_3615",        # 23, 35
        "Function_36_367D",        # 24, 36
        "Function_37_3856",        # 25, 37
        "Function_38_3A38",        # 26, 38
        "Function_39_3AC5",        # 27, 39
        "Function_40_3CFB",        # 28, 40
        "Function_41_3D7F",        # 29, 41
        "Function_42_3DA5",        # 2A, 42
        "Function_43_3DCB",        # 2B, 43
        "Function_44_3DF1",        # 2C, 44
        "Function_45_3E49",        # 2D, 45
        "Function_46_3E8D",        # 2E, 46
        "Function_47_3ED1",        # 2F, 47
        "Function_48_3F6A",        # 30, 48
        "Function_49_3FAD",        # 31, 49
    )


    def Function_0_67A(): pass

    label("Function_0_67A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_690")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 6)
    Jump("loc_6D8")

    label("loc_690")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_6AF")
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x29), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 7)
    Jump("loc_6D8")

    label("loc_6AF")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (101, "loc_6BB"),
        (SWITCH_DEFAULT, "loc_6D8"),
    )


    label("loc_6BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6D5")
    ClearMapFlags(0x10)
    SetMapFlags(0x10000000)
    Event(0, 5)

    label("loc_6D5")

    Jump("loc_6D8")

    label("loc_6D8")

    Return()

    # Function_0_67A end

    def Function_1_6D9(): pass

    label("Function_1_6D9")

    OP_16(0x2, 0xFA0, 0xFFFD21A0, 0xFFFE5638, 0x230026)
    OP_4F(0x2A, (scpexpr(EXPR_PUSH_LONG, 0x186A), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x1C8, 0x1, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x260, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_70C")
    OP_6F(0x0, 0)
    Jump("loc_713")

    label("loc_70C")

    OP_6F(0x0, 60)

    label("loc_713")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x260, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_725")
    OP_6F(0x1, 0)
    Jump("loc_72C")

    label("loc_725")

    OP_6F(0x1, 60)

    label("loc_72C")

    Return()

    # Function_1_6D9 end

    def Function_2_72D(): pass

    label("Function_2_72D")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_752")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_894")

    label("loc_752")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_76B")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_894")

    label("loc_76B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_784")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_894")

    label("loc_784")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_79D")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_894")

    label("loc_79D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B6")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_894")

    label("loc_7B6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7CF")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_894")

    label("loc_7CF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E8")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_894")

    label("loc_7E8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_801")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_894")

    label("loc_801")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81A")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_894")

    label("loc_81A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_833")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_894")

    label("loc_833")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_84C")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_894")

    label("loc_84C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_865")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_894")

    label("loc_865")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_87E")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_894")

    label("loc_87E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_894")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_894")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8A9")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_894")

    label("loc_8A9")

    Return()

    # Function_2_72D end

    def Function_3_8AA(): pass

    label("Function_3_8AA")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x260, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_982")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F8, 1)"), scpexpr(EXPR_END)), "loc_919")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\xF8\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1302)
    Jump("loc_97F")

    label("loc_919")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\xF8\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xF8\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_97F")

    Jump("loc_9B3")

    label("loc_982")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_9B3")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_8AA end

    def Function_4_9C1(): pass

    label("Function_4_9C1")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x260, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A99")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_A30")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\xFC\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1303)
    Jump("loc_A96")

    label("loc_A30")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
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

    label("loc_A96")

    Jump("loc_ACA")

    label("loc_A99")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_ACA")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_9C1 end

    def Function_5_AD8(): pass

    label("Function_5_AD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AE9")
    Call(0, 47)

    label("loc_AE9")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, -28930, -1990, 68170, 180)
    SetChrPos(0xF7, -27890, -2009, 67540, 180)
    ClearMapFlags(0x1)
    OP_6D(-28090, -2060, 66510, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    def lambda_B64():
        OP_6D(-28100, -2000, 63110, 2800)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_B64)

    def lambda_B7C():
        OP_67(0, 9500, -10000, 2800)
        ExitThread()

    QueueWorkItem(0xF7, 2, lambda_B7C)

    def lambda_B94():
        OP_8E(0xFE, 0xFFFF930E, 0x0, 0xF708, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_B94)

    def lambda_BAF():
        OP_8E(0xFE, 0xFFFF8EFE, 0x0, 0xF7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_BAF)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0xF7, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_DEE")
    OP_8C(0x106, 270, 400)

    ChrTalk(    #6
        0x106,
        (
            "#051F#2P不过，那位院长老师\x01",
            "给人的感觉还是像母亲一样呢。\x02\x03",

            "女王也是那样……\x01",
            "在那种人面前自然没法不低头啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(    #7
        0x101,
        (
            "#1016F#6P啊哈哈，阿加特\x01",
            "原来也会这么想啊。\x02\x03",

            "#1017F嗯，和我妈妈\x01",
            "感觉很像呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x106,
        (
            "#052F#2P是吗，大叔的……\x02\x03",

            "#552F听说是在１０年前的战争中\x01",
            "去世了……\x02\x03",

            "……………………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        "#1004F#6P怎么了，阿加特？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x106,
        (
            "#552F#2P不……怎么说呢。\x02\x03",

            "我觉得女人真是坚强啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #11
        0x101,
        "#1015F#6P你想说什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x106,
        (
            "#053F#2P……别再问下去了。\x02\x03",

            "#050F好啦，赶快去玛诺利亚村\x01",
            "把小鬼们都接回来吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FC7")

    label("loc_DEE")

    OP_8C(0x103, 270, 400)

    ChrTalk(    #13
        0x103,
        (
            "#021F#2P嗯……\x01",
            "很了不起的女性呢。\x02\x03",

            "虽然类型完全不同，\x01",
            "不过感觉上跟莱娜阿姨很像。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #14
        0x101,
        (
            "#1017F#6P啊，雪拉姐也这么想？\x02\x03",

            "我觉得妈妈也是那个样子，\x01",
            "而且跟女王陛下也很相似呢。\x02\x03",

            "怎么说呢……\x01",
            "会让人心中温暖起来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x103,
        (
            "#020F#2P说到底，这可能\x01",
            "就是女性的包容力呢。\x02\x03",

            "#026F呼……我还差的远呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        (
            "#1006F#6P嗯～我认为雪拉姐\x01",
            "还算有一定的包容力哦？\x02\x03",

            "不过要更上一层楼的话，\x01",
            "首先嗜酒就是个问题了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x103,
        (
            "#025F#2P唔……\x01",
            "一针见血啊。\x02\x03",

            "#020F好了，赶快去村子\x01",
            "接孩子们去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FC7")

    OP_A2(0x1217)
    EventEnd(0x0)
    Return()

    # Function_5_AD8 end

    def Function_6_FCD(): pass

    label("Function_6_FCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FDE")
    Call(0, 47)

    label("loc_FDE")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, -27520, -1970, 67560, 197)
    SetChrPos(0xF7, -28770, -2040, 67850, 173)
    SetChrPos(0x109, -28090, -2000, 66790, 186)
    OP_6D(-27790, -1950, 68340, 0)
    OP_67(0, 10060, -10000, 0)
    OP_6B(2830, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    def lambda_1065():
        OP_6D(-28370, -1950, 60060, 5000)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_1065)

    def lambda_107D():
        OP_67(0, 10060, -10000, 5000)
        ExitThread()

    QueueWorkItem(0xF7, 2, lambda_107D)

    def lambda_1095():
        OP_8E(0xFE, 0xFFFF90F2, 0xFFFFF844, 0xE5C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1095)
    Sleep(500)

    def lambda_10B5():
        OP_8E(0xFE, 0xFFFF934A, 0xFFFFF84E, 0xEC0E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_10B5)
    Sleep(200)

    def lambda_10D5():
        OP_8E(0xFE, 0xFFFF8DA0, 0xFFFFF844, 0xED3A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_10D5)
    FadeToBright(2000, 0)
    WaitChrThread(0x109, 0x0)
    OP_8C(0x109, 0, 400)
    WaitChrThread(0xF7, 0x1)
    WaitChrThread(0xF7, 0x2)

    ChrTalk(    #18
        0x109,
        (
            "#1061F呀～真是一群\x01",
            "有精神的小鬼啊。\x02\x03",

            "#1062F不过，这就是院长老师的魅力吗？\x02\x03",

            "每个人都是那么率直，\x01",
            "实在令人感到十分舒畅。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x101,
        (
            "#1006F因为是特蕾莎老师嘛。\x02\x03",

            "不过本来还有\x01",
            "另一个人在照顾孩子们的。\x02\x03",

            "由于正值学校的考试期间，\x01",
            "今天好像没来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x109,
        (
            "#1062F嗯～这样啊。\x02\x03",

            "#1060F话说回来我\x01",
            "现在就回卢安了。\x02\x03",

            "你们怎么办？\x01",
            "一起去城里吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_129A")

    ChrTalk(    #21
        0x106,
        (
            "#051F#5P是啊，这边的\x01",
            "探听也结束了……\x02\x03",

            "一路上结伴同行也不错。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12DD")

    label("loc_129A")


    ChrTalk(    #22
        0x103,
        (
            "#021F#5P是啊，这边的\x01",
            "探听也结束了……\x02\x03",

            "一路上结伴同行也不错。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12DD")


    ChrTalk(    #23
        0x101,
        (
            "#1006F那就决定了。\x02\x03",

            "目标卢安——Ｌｅｔ＇ｓ　ｇｏ！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x121A)
    OP_28(0x82, 0x2, 0x100)
    OP_28(0x82, 0x1, 0x200)
    EventEnd(0x0)
    Return()

    # Function_6_FCD end

    def Function_7_1327(): pass

    label("Function_7_1327")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-45040, -2090, 25310, 0)
    OP_67(0, 7900, -10000, 0)
    OP_6B(4610, 0)
    OP_6C(48000, 0)
    OP_6E(339, 0)
    SetChrPos(0x8, -35650, -2000, 30000, 90)
    SetChrPos(0x9, -36610, -2000, 30450, 90)
    SetChrPos(0xB, -36680, -2000, 29000, 90)
    SetChrPos(0xC, -37600, -2000, 30100, 90)
    SetChrPos(0xA, -37620, -2000, 29000, 90)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0xA, 0x40)
    SetChrFlags(0xB, 0x40)
    SetChrFlags(0xC, 0x40)
    SetChrPos(0x11, -32070, -1990, 32290, 135)
    SetChrPos(0x12, -31520, -2000, 31180, 135)
    SetChrPos(0x13, -32080, -2000, 29670, 135)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x11, 0x40)
    SetChrFlags(0x12, 0x40)
    SetChrFlags(0x13, 0x40)
    LoadEffect(0x0, "map\\\\mp008_00.eff")
    LoadEffect(0x1, "Craft\\\\cr000_00.eff")
    LoadEffect(0x2, "monster\\\\msc0290.eff")
    LoadEffect(0x3, "monster\\\\msc0100.eff")
    LoadEffect(0x4, "battle\\\\btgun00.eff")
    LoadEffect(0x5, "map\\\\mp003_00.eff")
    LoadEffect(0x6, "scraft\\\\sc000_11.eff")

    def lambda_14F1():
        OP_6D(-24600, -2000, 30160, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_14F1)
    OP_C8(0x200, 0x46, "C_PLAC18._CH", 0x1, 0x3E8)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x0)
    Fade(1000)
    OP_6D(-10080, -2000, 30010, 0)
    OP_67(0, 7490, -10000, 0)
    OP_6B(1540, 0)
    OP_6C(72000, 0)
    OP_6E(562, 0)
    OP_43(0x14, 0x0, 0x0, 0x18)
    Sleep(150)
    OP_43(0xB, 0x3, 0x0, 0x28)
    OP_0D()

    def lambda_1583():
        OP_6D(-16810, -2000, 29970, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1583)

    def lambda_159B():
        OP_67(0, 6040, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_159B)

    def lambda_15B3():
        OP_6B(1400, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_15B3)

    def lambda_15C3():
        OP_6C(59000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_15C3)
    WaitChrThread(0x14, 0x0)
    OP_44(0xB, 0x3)
    OP_23(0x13F)
    WaitChrThread(0x101, 0x0)
    Sleep(1000)
    Fade(500)
    OP_6D(-34180, -2000, 31670, 0)
    OP_67(0, 5050, -10000, 0)
    OP_6B(2290, 0)
    OP_6C(33000, 0)
    OP_6E(378, 0)
    OP_0D()
    OP_43(0x11, 0x0, 0x0, 0x15)
    Sleep(100)
    OP_43(0x12, 0x0, 0x0, 0x16)
    Sleep(100)
    OP_43(0x13, 0x0, 0x0, 0x17)
    WaitChrThread(0x12, 0x0)

    def lambda_1650():
        OP_8F(0xFE, 0xFFFF7ED2, 0xFFFFF83A, 0x7E22, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_1650)
    Sleep(100)

    def lambda_1670():
        OP_8F(0xFE, 0xFFFF7EC8, 0xFFFFF830, 0x73E6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_1670)
    Sleep(100)

    def lambda_1690():
        OP_8F(0xFE, 0xFFFF80F8, 0xFFFFF830, 0x79CC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_1690)

    ChrTalk(    #24
        0x12,
        (
            "#6P唔……\x01",
            "还在追吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x11,
        (
            "#6P很快就能和玛诺利亚的\x01",
            "守备队会合了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x13,
        (
            "#6P别退缩！\x01",
            "必定能平安送到的！\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x11, 0x1, 0x0, 0x21)
    Sleep(100)
    OP_43(0x12, 0x1, 0x0, 0x22)
    Sleep(100)
    OP_43(0x13, 0x1, 0x0, 0x23)
    Sleep(1000)

    ChrTalk(    #27
        0xB,
        "#6P老、老师……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 270, 400)

    ChrTalk(    #28
        0x8,
        (
            "#754F#2P没问题……不要担心。\x02\x03",

            "#750F我不会让它们\x01",
            "伤害你们任何一个人的。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0xA, 270, 400)

    ChrTalk(    #29
        0xA,
        "#5P这下真的麻烦大了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x8,
        "#752F#2P#3S！！！\x02",
    )

    CloseMessageWindow()
    OP_43(0x16, 0x3, 0x0, 0x2)
    OP_43(0x17, 0x3, 0x0, 0x2)
    SetChrPos(0x14, -58610, -1700, 17850, 90)
    SetChrPos(0x15, -61080, -1700, 19330, 90)
    SetChrPos(0x16, -59760, -1700, 15360, 90)
    SetChrPos(0x17, -62900, -1700, 16980, 90)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x14, 0x40)
    SetChrFlags(0x15, 0x40)
    SetChrFlags(0x16, 0x40)
    SetChrFlags(0x17, 0x40)
    SetChrFlags(0x14, 0x800)
    SetChrFlags(0x15, 0x800)
    SetChrFlags(0x16, 0x800)
    SetChrFlags(0x17, 0x800)

    def lambda_1886():
        OP_6D(-60930, -2000, 17930, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1886)

    def lambda_189E():
        OP_67(0, 4890, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_189E)

    def lambda_18B6():
        OP_6B(2250, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_18B6)

    def lambda_18C6():
        OP_6C(299000, 4000)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_18C6)

    def lambda_18D6():
        OP_6E(362, 4000)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_18D6)

    def lambda_18E6():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_18E6)
    Sleep(80)

    def lambda_18F9():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_18F9)
    Sleep(50)

    def lambda_190C():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_190C)
    OP_8E(0x8, 0xFFFF7414, 0xFFFFF830, 0x6EF0, 0xBB8, 0x0)
    OP_8E(0x8, 0xFFFF6B22, 0xFFFFF830, 0x6C3E, 0xBB8, 0x0)
    OP_8E(0x8, 0xFFFF68D4, 0xFFFFF830, 0x7030, 0xBB8, 0x0)
    OP_8C(0x8, 270, 400)
    WaitChrThread(0x101, 0x3)
    Sleep(1000)
    Fade(500)
    OP_6D(-36180, -2000, 31670, 0)
    OP_67(0, 5050, -10000, 0)
    OP_6B(2290, 0)
    OP_6C(33000, 0)
    OP_6E(378, 0)
    OP_44(0x11, 0x1)
    OP_44(0x13, 0x1)
    SetChrSubChip(0x11, 0)
    SetChrSubChip(0x13, 0)
    SetChrChipByIndex(0x11, 13)
    SetChrChipByIndex(0x13, 13)
    OP_8C(0x11, 270, 0)
    OP_8C(0x13, 270, 0)
    OP_8C(0x14, 90, 0)
    OP_8C(0x15, 90, 0)
    OP_8C(0x16, 90, 0)
    OP_8C(0x17, 90, 0)
    ClearChrFlags(0x14, 0x800)
    ClearChrFlags(0x15, 0x800)
    ClearChrFlags(0x16, 0x800)
    ClearChrFlags(0x17, 0x800)
    OP_0D()

    ChrTalk(    #31
        0x13,
        "#2P什…什么…！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x11,
        "#2P从另一边过来！？\x02",
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #33
        0xC,
        "#2P呜哎哎哎哎哎！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x9,
        (
            "#776F#2P这、这样的话\x01",
            "连我们也……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x8,
        (
            "#755F#5P不行！\x01",
            "退下！\x02\x03",

            "#757F（女神啊……\x01",
            "　请拯救我们这些无助的人吧。)\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(500)
    OP_44(0x12, 0x1)
    OP_6D(-58200, -2000, 18040, 0)
    OP_67(0, 4530, -10000, 0)
    OP_6B(2700, 0)
    OP_6C(255000, 0)
    OP_6E(371, 0)

    def lambda_1B1B():
        OP_6D(-51550, -2000, 22170, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B1B)
    OP_43(0xB, 0x3, 0x0, 0x28)
    OP_43(0x14, 0x0, 0x0, 0x19)
    Sleep(200)
    OP_43(0x15, 0x0, 0x0, 0x1A)
    Sleep(250)
    OP_43(0x16, 0x0, 0x0, 0x1B)
    Sleep(200)
    OP_43(0x17, 0x0, 0x0, 0x1C)
    Sleep(1000)
    OP_20(0x3E8)
    WaitChrThread(0x17, 0x0)
    WaitChrThread(0x101, 0x1)
    Sleep(500)
    OP_1D(0x2C)
    Sleep(500)
    Fade(500)
    OP_6D(-49530, -2000, 23670, 0)
    OP_67(0, 6880, -10000, 0)
    OP_6B(2310, 0)
    OP_6C(20000, 0)
    OP_6E(355, 0)
    ClearMapFlags(0x10)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xE, -50890, 300, 35800, 225)
    SetChrPos(0xD, -50890, 300, 35800, 225)
    SetChrPos(0xF, -50890, 300, 35800, 225)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xE, 0x40)
    SetChrFlags(0xD, 0x40)
    SetChrFlags(0xF, 0x40)
    OP_43(0xF, 0x1, 0x0, 0x24)
    Sleep(100)
    OP_43(0xE, 0x1, 0x0, 0x25)
    Sleep(100)
    OP_43(0xD, 0x1, 0x0, 0x27)
    WaitChrThread(0xE, 0x1)
    WaitChrThread(0xD, 0x1)
    WaitChrThread(0xF, 0x1)
    SetChrFlags(0xE, 0x20)
    SetChrFlags(0xF, 0x20)

    def lambda_1C5E():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1C5E)

    def lambda_1C6C():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1C6C)
    Sleep(1000)

    def lambda_1C7F():
        OP_6D(-57190, -2000, 18670, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1C7F)
    OP_7D(0x0, 0xE, 0x32, 0x1F4)
    OP_7D(0x0, 0xD, 0x32, 0x1F4)
    OP_7D(0x0, 0xF, 0x32, 0x1F4)
    SetChrSubChip(0xE, 0)
    SetChrChipByIndex(0xE, 20)

    def lambda_1CB9():
        OP_99(0xFE, 0x1, 0x4, 0xFA0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1CB9)

    def lambda_1CC9():
        OP_99(0xFE, 0x1, 0x4, 0xFA0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1CC9)

    def lambda_1CD9():
        OP_99(0xFE, 0x1, 0x4, 0xFA0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1CD9)

    def lambda_1CE9():
        OP_8F(0xFE, 0xFFFF1EE2, 0xFFFFF830, 0x47EA, 0x6590, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_1CE9)

    def lambda_1D04():
        OP_8F(0xFE, 0xFFFF225C, 0xFFFFF830, 0x45A6, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_1D04)

    def lambda_1D1F():
        OP_8F(0xFE, 0xFFFF1EF6, 0xFFFFF830, 0x4CCC, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_1D1F)
    OP_22(0x9B, 0x0, 0x64)
    Sleep(100)
    OP_44(0x17, 0x3)
    SetChrChipByIndex(0x17, 27)
    SetChrSubChip(0x17, 0)
    WaitChrThread(0xE, 0x2)
    WaitChrThread(0xD, 0x2)
    WaitChrThread(0xF, 0x2)
    OP_7D(0x1, 0xE, 0x0, 0x0)
    OP_7D(0x1, 0xD, 0x0, 0x0)
    OP_7D(0x1, 0xF, 0x0, 0x0)
    PlayEffect(0x3, 0x0, 0x17, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_83(0x0, 0x2)
    SetChrFlags(0x17, 0x80)
    Sleep(1000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(-37000, -2000, 30060, 0)
    OP_67(0, 4780, -10000, 0)
    OP_6B(3240, 0)
    OP_6C(24000, 0)
    OP_6E(282, 0)
    SetChrPos(0x11, -35550, -2000, 30860, 270)
    SetChrPos(0x12, -34880, -2000, 29770, 270)
    SetChrPos(0x13, -34710, -2000, 28220, 270)
    SetChrSubChip(0x11, 0)
    SetChrSubChip(0x12, 0)
    SetChrSubChip(0x13, 0)
    SetChrChipByIndex(0x11, 29)
    SetChrChipByIndex(0x12, 29)
    SetChrChipByIndex(0x13, 29)
    OP_8C(0x12, 270, 0)
    ClearChrFlags(0xD, 0x20)
    ClearChrFlags(0xE, 0x20)
    ClearChrFlags(0xF, 0x20)
    SetChrSubChip(0xD, 0)
    SetChrChipByIndex(0xD, 30)
    SetChrSubChip(0xE, 0)
    SetChrChipByIndex(0xE, 31)
    SetChrSubChip(0xF, 0)
    SetChrChipByIndex(0xF, 32)

    def lambda_1E8B():
        OP_8E(0xFE, 0xFFFF5E84, 0xFFFFF830, 0x6B6C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1E8B)
    OP_0D()
    SetMapFlags(0x10)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)

    def lambda_1EC8():
        OP_8E(0xFE, 0xFFFF5ACE, 0xFFFFF830, 0x6E0A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1EC8)
    OP_62(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xB, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xA, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_1F8E():
        OP_8E(0xFE, 0xFFFF5E02, 0xFFFFF830, 0x65A4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1F8E)
    WaitChrThread(0xD, 0x1)
    SetChrSubChip(0xD, 0)
    SetChrSubChip(0xE, 0)
    SetChrSubChip(0xF, 0)

    ChrTalk(    #36
        0x11,
        "#2P你、你们是！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x9,
        "#774F#2P难、难道是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xB,
        "#2P游击士先生……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xF,
        "#821F#6P嘿嘿，久等了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xE,
        (
            "#811F#6P没事吧？\x01",
            "没受伤吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xC,
        "#2P嗯、嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xA,
        "#2P没事～\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x10, -44820, 0, 51380, 135)

    NpcTalk(    #43
        0x10,
        "女性的声音",
        (
            "呵呵……\x01",
            "幸好赶上了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    SetChrPos(0x10, -48280, 0, 36210, 135)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x40)
    SetChrSubChip(0x10, 0)
    SetChrChipByIndex(0x10, 33)

    def lambda_20CB():
        OP_6D(-40770, -2000, 33410, 2500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_20CB)

    def lambda_20E3():
        OP_67(0, 3940, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_20E3)

    def lambda_20FB():
        OP_6B(2880, 2500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_20FB)

    def lambda_210B():
        OP_6C(327000, 2500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_210B)

    def lambda_211B():
        OP_6E(367, 2500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_211B)

    def lambda_212B():
        OP_8E(0xFE, 0xFFFF59E8, 0x0, 0x8016, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_212B)

    def lambda_2146():

        label("loc_2146")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_2146")

    QueueWorkItem2(0x8, 1, lambda_2146)

    def lambda_2157():

        label("loc_2157")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_2157")

    QueueWorkItem2(0x9, 1, lambda_2157)

    def lambda_2168():

        label("loc_2168")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_2168")

    QueueWorkItem2(0xC, 1, lambda_2168)

    def lambda_2179():

        label("loc_2179")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_2179")

    QueueWorkItem2(0x11, 1, lambda_2179)

    def lambda_218A():

        label("loc_218A")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_218A")

    QueueWorkItem2(0xF, 1, lambda_218A)
    Sleep(100)

    def lambda_21A0():

        label("loc_21A0")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_21A0")

    QueueWorkItem2(0xB, 1, lambda_21A0)

    def lambda_21B1():

        label("loc_21B1")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_21B1")

    QueueWorkItem2(0xA, 1, lambda_21B1)

    def lambda_21C2():

        label("loc_21C2")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_21C2")

    QueueWorkItem2(0x12, 1, lambda_21C2)

    def lambda_21D3():

        label("loc_21D3")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_21D3")

    QueueWorkItem2(0xE, 1, lambda_21D3)
    Sleep(100)

    def lambda_21E9():

        label("loc_21E9")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_21E9")

    QueueWorkItem2(0x13, 1, lambda_21E9)

    def lambda_21FA():

        label("loc_21FA")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_21FA")

    QueueWorkItem2(0xD, 1, lambda_21FA)
    WaitChrThread(0x10, 0x1)
    SetChrSubChip(0x10, 0)
    OP_44(0x8, 0x1)
    OP_44(0x9, 0x1)
    OP_44(0xC, 0x1)
    OP_44(0x11, 0x1)
    OP_44(0xF, 0x1)
    OP_44(0xB, 0x1)
    OP_44(0xA, 0x1)
    OP_44(0x12, 0x1)
    OP_44(0xE, 0x1)
    OP_44(0x13, 0x1)
    OP_44(0xD, 0x1)
    Sleep(500)

    ChrTalk(    #44
        0x8,
        "#753F#6P啊，卡露娜小姐……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x10,
        (
            "#831F#6P好久不见呢，院长老师。\x02\x03",

            "你们在前往玛诺利亚避难的途中吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x8,
        (
            "#750F#6P嗯嗯，承蒙\x01",
            "军队的各位相送……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_22D9():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_22D9)
    Sleep(100)

    def lambda_22EC():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_22EC)
    Sleep(100)

    def lambda_22FF():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_22FF)
    Sleep(400)

    ChrTalk(    #47
        0xD,
        (
            "#842F#5P军队的各位！\x01",
            "这里交给我们了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xE,
        (
            "#816F#5P请赶快带孩子们\x01",
            "去玛诺利亚！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x12,
        "#2P不、不胜感激！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x13,
        (
            "#2P各位！\x01",
            "跟我们来！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2397():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2397)
    Sleep(80)

    def lambda_23AA():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_23AA)

    def lambda_23B8():

        label("loc_23B8")

        OP_8C(0xFE, 90, 400)
        OP_48()
        Jump("loc_23B8")

    QueueWorkItem2(0xB, 1, lambda_23B8)
    Sleep(80)

    def lambda_23CE():

        label("loc_23CE")

        OP_8C(0xFE, 90, 400)
        OP_48()
        Jump("loc_23CE")

    QueueWorkItem2(0xA, 1, lambda_23CE)
    Sleep(50)

    def lambda_23E4():

        label("loc_23E4")

        OP_8C(0xFE, 90, 400)
        OP_48()
        Jump("loc_23E4")

    QueueWorkItem2(0xC, 1, lambda_23E4)
    Sleep(400)

    ChrTalk(    #51
        0x9,
        "#770F#5P嗯！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xA,
        "#5P知道了～\x02",
    )

    CloseMessageWindow()
    OP_43(0x13, 0x1, 0x0, 0x2E)
    OP_43(0x12, 0x1, 0x0, 0x2D)
    Sleep(100)
    OP_43(0xD, 0x1, 0x0, 0x2B)

    def lambda_2437():

        label("loc_2437")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_2437")

    QueueWorkItem2(0x10, 3, lambda_2437)
    Sleep(200)
    OP_43(0xF, 0x1, 0x0, 0x29)
    Sleep(200)
    OP_43(0xE, 0x1, 0x0, 0x2A)

    def lambda_2460():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2460)

    def lambda_246E():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_246E)

    def lambda_247C():

        label("loc_247C")

        OP_8C(0xFE, 270, 400)
        OP_48()
        Jump("loc_247C")

    QueueWorkItem2(0x8, 1, lambda_247C)

    def lambda_248D():

        label("loc_248D")

        OP_8C(0xFE, 270, 400)
        OP_48()
        Jump("loc_248D")

    QueueWorkItem2(0x9, 1, lambda_248D)

    def lambda_249E():

        label("loc_249E")

        OP_8C(0xFE, 270, 400)
        OP_48()
        Jump("loc_249E")

    QueueWorkItem2(0xC, 1, lambda_249E)

    def lambda_24AF():

        label("loc_24AF")

        OP_8C(0xFE, 270, 400)
        OP_48()
        Jump("loc_24AF")

    QueueWorkItem2(0xB, 1, lambda_24AF)

    def lambda_24C0():

        label("loc_24C0")

        OP_8C(0xFE, 270, 400)
        OP_48()
        Jump("loc_24C0")

    QueueWorkItem2(0xA, 1, lambda_24C0)
    WaitChrThread(0x11, 0x1)
    WaitChrThread(0x12, 0x1)
    WaitChrThread(0x13, 0x1)
    OP_44(0x8, 0x1)
    OP_44(0x9, 0x1)
    OP_44(0xC, 0x1)
    OP_44(0xB, 0x1)
    OP_44(0xA, 0x1)
    SetChrSubChip(0x12, 0)
    SetChrChipByIndex(0x12, 24)

    def lambda_24FE():
        OP_8E(0xFE, 0xFFFF33A0, 0xFFFFF830, 0x5442, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_24FE)
    Sleep(50)
    SetChrSubChip(0x13, 0)
    SetChrChipByIndex(0x13, 24)

    def lambda_2528():
        OP_8E(0xFE, 0xFFFF2D56, 0xFFFFF84E, 0x5ADC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2528)
    Sleep(100)

    def lambda_2548():
        OP_8E(0xFE, 0xFFFF3684, 0xFFFFF830, 0x5906, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2548)

    def lambda_2563():
        OP_6D(-39740, -1500, 29550, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2563)

    def lambda_257B():
        OP_67(0, 5590, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_257B)

    def lambda_2593():
        OP_6B(2600, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2593)

    def lambda_25A3():
        OP_6C(306000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_25A3)

    def lambda_25B3():
        OP_6E(367, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_25B3)
    Sleep(100)

    def lambda_25C8():
        OP_8E(0xFE, 0xFFFF3C6A, 0xFFFFF830, 0x56EA, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_25C8)
    Sleep(50)

    def lambda_25E8():
        OP_8E(0xFE, 0xFFFF3738, 0xFFFFF830, 0x5FC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_25E8)
    Sleep(100)

    def lambda_2608():
        OP_8E(0xFE, 0xFFFF3C6A, 0xFFFFF830, 0x56EA, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2608)

    def lambda_2623():
        OP_8E(0xFE, 0xFFFF3738, 0xFFFFF830, 0x5FC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2623)
    Sleep(100)
    SetChrSubChip(0x11, 0)
    SetChrChipByIndex(0x11, 24)

    def lambda_264D():
        OP_8E(0xFE, 0xFFFF3B8E, 0xFFFFF830, 0x5C26, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_264D)
    WaitChrThread(0x11, 0x1)
    WaitChrThread(0x101, 0x1)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    OP_44(0xF, 0x3)
    OP_44(0x10, 0x3)
    OP_44(0xE, 0x3)
    OP_44(0xD, 0x3)
    OP_8C(0xD, 45, 400)

    def lambda_26B1():
        OP_8E(0xFE, 0xFFFF696A, 0xFFFFF830, 0x6D6A, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_26B1)
    Sleep(100)
    OP_8C(0x10, 135, 400)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_26DD():
        OP_96(0xFE, 0xFFFF6794, 0xFFFFF830, 0x73BE, 0x3E8, 0x1770)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_26DD)
    Sleep(100)
    WaitChrThread(0xD, 0x0)
    OP_8C(0xD, 90, 400)
    WaitChrThread(0x10, 0x0)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_2716():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2716)
    Sleep(100)

    def lambda_2729():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2729)
    Sleep(100)
    OP_8C(0xE, 90, 400)
    Fade(1000)
    OP_6D(-16780, -2000, 30390, 0)
    OP_67(0, 5500, -10000, 0)
    OP_6B(2330, 0)
    OP_6C(89000, 0)
    OP_6E(349, 0)

    def lambda_2785():
        OP_6C(53000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2785)
    OP_43(0x14, 0x0, 0x0, 0xF)
    Sleep(200)
    OP_43(0xB, 0x3, 0x0, 0x28)
    Sleep(200)
    OP_43(0x15, 0x0, 0x0, 0x10)
    Sleep(400)
    OP_43(0x16, 0x0, 0x0, 0x11)
    Sleep(400)
    OP_43(0x17, 0x0, 0x0, 0x12)
    Sleep(400)
    OP_43(0x18, 0x0, 0x0, 0x13)
    Sleep(400)
    OP_43(0x19, 0x0, 0x0, 0x14)
    WaitChrThread(0x19, 0x0)
    OP_44(0xB, 0x3)
    WaitChrThread(0x101, 0x3)
    Sleep(1000)
    SetChrPos(0xD, -37670, -2000, 29370, 90)
    SetChrPos(0xF, -39320, -2000, 30070, 90)
    SetChrPos(0xE, -39100, -2000, 27880, 90)
    SetChrPos(0x10, -41230, -2000, 28610, 90)
    SetChrChipByIndex(0xD, 9)
    SetChrSubChip(0xD, 0)
    SetChrChipByIndex(0xF, 11)
    SetChrSubChip(0xF, 0)
    SetChrChipByIndex(0xE, 10)
    SetChrSubChip(0xE, 0)
    SetChrChipByIndex(0x10, 12)
    SetChrSubChip(0x10, 0)

    def lambda_2863():
        OP_6D(-37540, -2000, 29550, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2863)
    WaitChrThread(0x101, 0x0)
    Sleep(300)

    ChrTalk(    #53
        0xF,
        (
            "#825F#6P好了～\x01",
            "看来会相当吃力呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x10,
        (
            "#835F#6P不过……\x01",
            "也只能全力以赴了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xE,
        (
            "#816F#6P没问题，总有办法的！\x02\x03",

            "和前往塔内的\x01",
            "艾丝蒂尔他们相比\x01",
            "这实在算不了什么！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xD,
        (
            "#840F#6P呵呵，是啊。\x02\x03",

            "为了让他们放心战斗，\x01",
            "就让我们尽最大努力吧。\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0xD, 0)
    SetChrChipByIndex(0xD, 17)
    OP_0D()
    Sleep(500)

    ChrTalk(    #57
        0xD,
        "#843F#6P方术──满碛寒光生铁衣。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xD, 0)
    SetChrChipByIndex(0xD, 18)
    OP_51(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(240)
    PlayEffect(0x1, 0x0, 0xD, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_83(0x0, 0x2)
    PlayEffect(0x2, 0x1, 0xD, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    PlayEffect(0x2, 0x2, 0xE, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    PlayEffect(0x2, 0x3, 0xF, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    PlayEffect(0x2, 0x4, 0x10, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_83(0x4, 0x2)
    Sleep(500)
    Fade(500)
    OP_22(0xD8, 0x0, 0x64)
    SetChrSubChip(0xD, 0)
    SetChrChipByIndex(0xD, 9)
    OP_0D()
    Sleep(500)

    ChrTalk(    #58
        0xD,
        "#846F#6P要上啰，各位！\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #59
        0xE,
        "#815F#1K好！\x02",
    )


    ChrTalk(    #60
        0xF,
        "#822F#1K#1P啊啊！\x02",
    )


    ChrTalk(    #61
        0x10,
        "#832F#1K明白！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_56(0x1)
    OP_59()

    def lambda_2B86():
        OP_6D(-26760, -2000, 31240, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2B86)

    def lambda_2B9E():
        OP_6B(2390, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2B9E)
    FadeToDark(2000, 0, -1)
    SetChrSubChip(0xD, 0)
    SetChrChipByIndex(0xD, 15)

    def lambda_2BC2():
        OP_8F(0xFE, 0xFFFF8DFA, 0xFFFFF830, 0x7A08, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2BC2)
    Sleep(100)
    SetChrSubChip(0xE, 0)
    SetChrChipByIndex(0xE, 19)

    def lambda_2BEC():
        OP_8F(0xFE, 0xFFFF897C, 0xFFFFF830, 0x7454, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2BEC)
    Sleep(50)
    SetChrSubChip(0xF, 0)
    SetChrChipByIndex(0xF, 21)

    def lambda_2C16():
        OP_8F(0xFE, 0xFFFF87D8, 0xFFFFF830, 0x7CA6, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2C16)
    Sleep(100)
    SetChrSubChip(0x10, 0)
    SetChrChipByIndex(0x10, 23)

    def lambda_2C40():
        OP_8F(0xFE, 0xFFFF8404, 0xFFFFF830, 0x771A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2C40)
    OP_43(0x14, 0x1, 0x0, 0x8)
    OP_43(0xB, 0x3, 0x0, 0x28)
    OP_A2(0x0)
    Sleep(100)
    OP_0D()
    OP_20(0x7D0)
    Sleep(200)
    OP_24(0x1C8, 0x5A)
    Sleep(200)
    OP_24(0x1C8, 0x50)
    Sleep(200)
    OP_24(0x1C8, 0x46)
    Sleep(200)
    OP_24(0x1C8, 0x3C)
    Sleep(200)
    OP_24(0x1C8, 0x32)
    Sleep(200)
    OP_24(0x1C8, 0x28)
    Sleep(200)
    OP_24(0x1C8, 0x1E)
    Sleep(200)
    OP_23(0x1C8)
    OP_21()
    OP_A2(0x1E2F)
    OP_A2(0x10F6)
    NewScene("ED6_DT21/E0800   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_1327 end

    def Function_8_2CC9(): pass

    label("Function_8_2CC9")

    Sleep(500)
    OP_43(0x14, 0x0, 0x0, 0x9)
    Sleep(200)
    OP_43(0x15, 0x0, 0x0, 0xA)
    Sleep(200)
    OP_43(0x16, 0x0, 0x0, 0xB)
    Sleep(200)
    OP_43(0x17, 0x0, 0x0, 0xC)
    Sleep(200)
    OP_43(0x18, 0x0, 0x0, 0xD)
    Sleep(200)
    OP_43(0x19, 0x0, 0x0, 0xE)
    Return()

    # Function_8_2CC9 end

    def Function_9_2D12(): pass

    label("Function_9_2D12")

    SetChrChipByIndex(0xFE, 26)
    OP_90(0xFE, 0xFFFFEC78, 0xFFFFFF38, 0x1F4, 0x1388, 0x0)
    Return()

    # Function_9_2D12 end

    def Function_10_2D2C(): pass

    label("Function_10_2D2C")

    SetChrChipByIndex(0xFE, 26)
    OP_90(0xFE, 0xFFFFEC78, 0xFFFFFF38, 0x1F4, 0x1388, 0x0)
    Return()

    # Function_10_2D2C end

    def Function_11_2D46(): pass

    label("Function_11_2D46")

    SetChrChipByIndex(0xFE, 26)
    OP_90(0xFE, 0xFFFFEC78, 0xFFFFFF38, 0x1F4, 0x1388, 0x0)
    Return()

    # Function_11_2D46 end

    def Function_12_2D60(): pass

    label("Function_12_2D60")

    SetChrChipByIndex(0xFE, 26)
    OP_90(0xFE, 0xFFFFEC78, 0xFFFFFF38, 0x1F4, 0x1388, 0x0)
    Return()

    # Function_12_2D60 end

    def Function_13_2D7A(): pass

    label("Function_13_2D7A")

    SetChrChipByIndex(0xFE, 26)
    OP_90(0xFE, 0xFFFFEC78, 0xFFFFFF38, 0x1F4, 0x1388, 0x0)
    Return()

    # Function_13_2D7A end

    def Function_14_2D94(): pass

    label("Function_14_2D94")

    SetChrChipByIndex(0xFE, 26)
    OP_90(0xFE, 0xFFFFEC78, 0xFFFFFF38, 0x1F4, 0x1388, 0x0)
    Return()

    # Function_14_2D94 end

    def Function_15_2DAE(): pass

    label("Function_15_2DAE")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0xFE, -2790, -1750, 30120, 270)
    ClearChrFlags(0xFE, 0x80)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    SetChrChipByIndex(0xFE, 26)
    OP_8E(0xFE, 0xFFFFD760, 0xFFFFF92A, 0x7404, 0x1770, 0x0)
    OP_8E(0xFE, 0xFFFFB302, 0xFFFFF92A, 0x79F4, 0x1770, 0x0)
    SetChrPos(0xFE, -19710, -1600, 31220, 270)
    SetChrChipByIndex(0xFE, 14)
    OP_8C(0xFE, 270, 0)
    Return()

    # Function_15_2DAE end

    def Function_16_2E21(): pass

    label("Function_16_2E21")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0xFE, -2790, -1750, 30120, 270)
    ClearChrFlags(0xFE, 0x80)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    SetChrChipByIndex(0xFE, 26)
    OP_8E(0xFE, 0xFFFFD760, 0xFFFFF92A, 0x7404, 0x1770, 0x0)
    OP_8E(0xFE, 0xFFFFAF6A, 0xFFFFF92A, 0x7094, 0x1770, 0x0)
    SetChrPos(0xFE, -20630, -1600, 28820, 270)
    SetChrChipByIndex(0xFE, 14)
    OP_8C(0xFE, 270, 0)
    Return()

    # Function_16_2E21 end

    def Function_17_2E94(): pass

    label("Function_17_2E94")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0xFE, -2790, -1750, 30120, 270)
    ClearChrFlags(0xFE, 0x80)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    SetChrChipByIndex(0xFE, 26)
    OP_8E(0xFE, 0xFFFFD760, 0xFFFFF92A, 0x7404, 0x1770, 0x0)
    OP_8E(0xFE, 0xFFFFBBFE, 0xFFFFF92A, 0x6E46, 0x1770, 0x0)
    SetChrPos(0xFE, -17410, -1600, 28230, 270)
    SetChrChipByIndex(0xFE, 14)
    OP_8C(0xFE, 270, 0)
    Return()

    # Function_17_2E94 end

    def Function_18_2F07(): pass

    label("Function_18_2F07")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0xFE, -2790, -1750, 30120, 270)
    ClearChrFlags(0xFE, 0x80)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    SetChrChipByIndex(0xFE, 26)
    OP_8E(0xFE, 0xFFFFD760, 0xFFFFF92A, 0x7404, 0x1770, 0x0)
    OP_8E(0xFE, 0xFFFFC07C, 0xFFFFF92A, 0x7738, 0x1770, 0x0)
    SetChrPos(0xFE, -16260, -1600, 30520, 270)
    SetChrChipByIndex(0xFE, 14)
    OP_8C(0xFE, 270, 0)
    Return()

    # Function_18_2F07 end

    def Function_19_2F7A(): pass

    label("Function_19_2F7A")

    SetChrPos(0xFE, -2790, -1750, 30120, 270)
    ClearChrFlags(0xFE, 0x80)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    SetChrChipByIndex(0xFE, 26)
    OP_8E(0xFE, 0xFFFFD760, 0xFFFFF92A, 0x7404, 0x1770, 0x0)
    OP_8E(0xFE, 0xFFFFC9E6, 0xFFFFF92A, 0x72F6, 0x1770, 0x0)
    SetChrPos(0xFE, -13850, -1600, 29430, 270)
    SetChrChipByIndex(0xFE, 14)
    OP_8C(0xFE, 270, 0)
    Return()

    # Function_19_2F7A end

    def Function_20_2FE2(): pass

    label("Function_20_2FE2")

    SetChrPos(0xFE, -2790, -1750, 30120, 270)
    ClearChrFlags(0xFE, 0x80)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    SetChrChipByIndex(0xFE, 26)
    OP_8E(0xFE, 0xFFFFD760, 0xFFFFF92A, 0x7404, 0x1770, 0x0)
    OP_8E(0xFE, 0xFFFFD31E, 0xFFFFF92A, 0x713E, 0x1770, 0x0)
    SetChrPos(0xFE, -11490, -1600, 28990, 270)
    SetChrChipByIndex(0xFE, 14)
    OP_8C(0xFE, 270, 0)
    Return()

    # Function_20_2FE2 end

    def Function_21_304A(): pass

    label("Function_21_304A")

    SetChrChipByIndex(0xFE, 28)
    OP_8F(0xFE, 0xFFFF7ED2, 0xFFFFF830, 0x7E22, 0x7D0, 0x0)
    SetChrChipByIndex(0xFE, 13)
    Return()

    # Function_21_304A end

    def Function_22_3069(): pass

    label("Function_22_3069")

    SetChrChipByIndex(0xFE, 28)
    OP_8F(0xFE, 0xFFFF80F8, 0xFFFFF830, 0x79CC, 0x7D0, 0x0)
    SetChrChipByIndex(0xFE, 13)
    Return()

    # Function_22_3069 end

    def Function_23_3088(): pass

    label("Function_23_3088")

    SetChrChipByIndex(0xFE, 28)
    OP_8F(0xFE, 0xFFFF7EC8, 0xFFFFF830, 0x73E6, 0x7D0, 0x0)
    SetChrChipByIndex(0xFE, 13)
    Return()

    # Function_23_3088 end

    def Function_24_30A7(): pass

    label("Function_24_30A7")

    OP_43(0x14, 0x1, 0x0, 0x1D)
    Sleep(600)
    OP_43(0x15, 0x1, 0x0, 0x1E)
    WaitChrThread(0x15, 0x1)
    Return()

    # Function_24_30A7 end

    def Function_25_30C0(): pass

    label("Function_25_30C0")

    SetChrChipByIndex(0xFE, 26)
    OP_8E(0xFE, 0xFFFF2BF8, 0xFFFFF95C, 0x4E3E, 0x1770, 0x0)
    OP_8E(0xFE, 0xFFFF3EEA, 0xFFFFF95C, 0x5C62, 0x1770, 0x0)
    SetChrPos(0xFE, -49430, -1500, 23650, 45)
    OP_44(0xFE, 0x3)
    OP_44(0xB, 0x3)
    OP_23(0x13F)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x5, 0xFF, 0x14, 3000, 2500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 27)
    SetChrSubChip(0xFE, 0)
    OP_22(0x209, 0x0, 0x64)
    OP_9E(0xFE, 0x14, 0x0, 0x12C, 0xBB8)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 14)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    Return()

    # Function_25_30C0 end

    def Function_26_318D(): pass

    label("Function_26_318D")

    SetChrChipByIndex(0xFE, 26)
    OP_8E(0xFE, 0xFFFF2324, 0xFFFFF95C, 0x4E48, 0x1770, 0x0)
    OP_8E(0xFE, 0xFFFF336E, 0xFFFFF95C, 0x5D3E, 0x1770, 0x0)
    SetChrPos(0xFE, -52370, -1500, 23870, 45)
    OP_44(0xFE, 0x3)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x5, 0xFF, 0x15, 3000, 2500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 27)
    SetChrSubChip(0xFE, 0)
    OP_22(0x209, 0x0, 0x64)
    OP_9E(0xFE, 0x14, 0x0, 0x12C, 0xBB8)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 14)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    Return()

    # Function_26_318D end

    def Function_27_3253(): pass

    label("Function_27_3253")

    SetChrChipByIndex(0xFE, 26)
    OP_8E(0xFE, 0xFFFF2CC0, 0xFFFFF95C, 0x454C, 0x1770, 0x0)
    OP_8E(0xFE, 0xFFFF39F4, 0xFFFFF95C, 0x4F38, 0x1770, 0x0)
    SetChrPos(0xFE, -50700, -1500, 20280, 45)
    OP_44(0xFE, 0x3)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x5, 0xFF, 0x16, 3000, 2500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 27)
    SetChrSubChip(0xFE, 0)
    OP_22(0x209, 0x0, 0x64)
    OP_9E(0xFE, 0x14, 0x0, 0x12C, 0xBB8)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 14)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    Return()

    # Function_27_3253 end

    def Function_28_3319(): pass

    label("Function_28_3319")

    SetChrChipByIndex(0xFE, 26)
    OP_8E(0xFE, 0xFFFF1E56, 0xFFFFF95C, 0x4632, 0x1770, 0x0)
    OP_8E(0xFE, 0xFFFF2B76, 0xFFFFF95C, 0x4F4C, 0x1770, 0x0)
    SetChrPos(0xFE, -54410, -1500, 20300, 45)
    OP_44(0xFE, 0x3)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x5, 0xFF, 0x17, 3000, 2500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 27)
    SetChrSubChip(0xFE, 0)
    OP_22(0x209, 0x0, 0x64)
    OP_9E(0xFE, 0x14, 0x0, 0x12C, 0xBB8)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 14)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    Return()

    # Function_28_3319 end

    def Function_29_33DF(): pass

    label("Function_29_33DF")

    OP_43(0xFE, 0x3, 0x0, 0x2)
    SetChrPos(0xFE, 6670, -1750, 29940, 270)
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 26)
    OP_8F(0xFE, 0xFFFFD396, 0xFFFFF92A, 0x74F4, 0x1770, 0x0)
    OP_8F(0xFE, 0xFFFFBCEE, 0xFFFFF92A, 0x771A, 0x1770, 0x0)
    SetChrPos(0xFE, -17170, -1600, 30490, 270)
    SetChrChipByIndex(0xFE, 14)
    Return()

    # Function_29_33DF end

    def Function_30_3440(): pass

    label("Function_30_3440")

    OP_43(0xFE, 0x3, 0x0, 0x2)
    SetChrPos(0xFE, 6670, -1750, 29940, 270)
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 26)
    OP_8F(0xFE, 0xFFFFD396, 0xFFFFF92A, 0x74F4, 0x1770, 0x0)
    OP_8E(0xFE, 0xFFFFBB86, 0xFFFFF92A, 0x6B6C, 0x1770, 0x0)
    SetChrPos(0xFE, -17530, -1600, 27500, 270)
    OP_8C(0xFE, 270, 0)
    SetChrChipByIndex(0xFE, 14)
    Return()

    # Function_30_3440 end

    def Function_31_34A8(): pass

    label("Function_31_34A8")

    SetChrPos(0xFE, 6670, -1750, 29940, 270)
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 26)
    OP_8F(0xFE, 0xFFFFD396, 0xFFFFF92A, 0x74F4, 0x1770, 0x0)
    OP_8E(0xFE, 0xFFFFC50E, 0xFFFFF92A, 0x6EC8, 0x1770, 0x0)
    SetChrPos(0xFE, -15090, -1600, 28360, 270)
    OP_8C(0xFE, 270, 0)
    Return()

    # Function_31_34A8 end

    def Function_32_3504(): pass

    label("Function_32_3504")

    SetChrPos(0xFE, 6670, -1750, 29940, 270)
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 26)
    OP_8F(0xFE, 0xFFFFCA40, 0xFFFFF92A, 0x759E, 0x1388, 0x0)
    SetChrPos(0xFE, -13760, -1600, 30110, 270)
    Return()

    # Function_32_3504 end

    def Function_33_3545(): pass

    label("Function_33_3545")

    SetChrChipByIndex(0xFE, 25)

    label("loc_354A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_35AC")
    OP_99(0xFE, 0x0, 0x4, 0xA28)
    OP_22(0x1F7, 0x0, 0x50)
    PlayEffect(0x4, 0xFF, 0xFE, 0, 900, 1100, -45, 0, 0, 1000, 1000, 1000, 0x1F, 0, 0, 0, 0)
    Sleep(500)
    OP_99(0xFE, 0x4, 0x0, 0xA28)
    Sleep(550)
    Jump("loc_354A")

    label("loc_35AC")

    Return()

    # Function_33_3545 end

    def Function_34_35AD(): pass

    label("Function_34_35AD")

    SetChrChipByIndex(0xFE, 25)

    label("loc_35B2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3614")
    OP_99(0xFE, 0x0, 0x4, 0xA28)
    OP_22(0x1F7, 0x0, 0x50)
    PlayEffect(0x4, 0xFF, 0xFE, 0, 900, 1100, -45, 0, 0, 1000, 1000, 1000, 0x1F, 0, 0, 0, 0)
    Sleep(500)
    OP_99(0xFE, 0x4, 0x0, 0xA28)
    Sleep(600)
    Jump("loc_35B2")

    label("loc_3614")

    Return()

    # Function_34_35AD end

    def Function_35_3615(): pass

    label("Function_35_3615")

    SetChrChipByIndex(0xFE, 25)

    label("loc_361A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_367C")
    OP_99(0xFE, 0x0, 0x4, 0xA28)
    OP_22(0x1F7, 0x0, 0x50)
    PlayEffect(0x4, 0xFF, 0xFE, 0, 900, 1100, -45, 0, 0, 1000, 1000, 1000, 0x1F, 0, 0, 0, 0)
    Sleep(500)
    OP_99(0xFE, 0x4, 0x0, 0xA28)
    Sleep(500)
    Jump("loc_361A")

    label("loc_367C")

    Return()

    # Function_35_3615 end

    def Function_36_367D(): pass

    label("Function_36_367D")

    OP_22(0xA3, 0x0, 0x64)
    OP_96(0xFE, 0xFFFF4F20, 0xFFFFF830, 0x5D8E, 0x4B0, 0x1388)
    OP_22(0xA4, 0x0, 0x64)
    OP_8C(0xFE, 225, 400)
    SetChrFlags(0x16, 0x20)
    SetChrFlags(0x16, 0x4)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 21)
    OP_8E(0xFE, 0xFFFF4052, 0xFFFFF830, 0x51E0, 0x1770, 0x0)
    SetChrSubChip(0xF, 0)
    SetChrChipByIndex(0xF, 22)

    def lambda_36DD():
        OP_99(0xFE, 0x0, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_36DD)
    Sleep(300)
    PlayEffect(0x6, 0xFF, 0x16, 0, 800, 300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_44(0x16, 0x3)
    SetChrChipByIndex(0x16, 27)
    SetChrSubChip(0x16, 0)

    def lambda_3746():
        OP_9E(0xFE, 0x1E, 0x0, 0x7D0, 0xFA0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_3746)
    Sleep(300)

    def lambda_3765():
        OP_96(0xFE, 0xFFFF4052, 0xFFFFF830, 0x51E0, 0xBB8, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3765)

    def lambda_3783():
        OP_99(0xFE, 0x7, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3783)
    OP_44(0x16, 0x1)
    WaitChrThread(0xFE, 0x2)
    SetChrFlags(0xFE, 0x800)
    OP_99(0xFE, 0x0, 0x4, 0xDAC)
    WaitChrThread(0xFE, 0x3)
    PlayEffect(0x6, 0xFF, 0x16, 0, 1000, 300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)

    def lambda_37F5():
        OP_9E(0xFE, 0x1E, 0x0, 0x7D0, 0xFA0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_37F5)

    def lambda_380F():
        OP_9F(0x16, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_380F)
    OP_94(0x1, 0x16, 0x0, 0xFFFFE0C0, 0x5DC0, 0x0)
    OP_44(0x16, 0x1)
    OP_22(0x20B, 0x0, 0x64)
    SetChrFlags(0x16, 0x80)
    ClearChrFlags(0x16, 0x20)
    ClearChrFlags(0x16, 0x4)
    ClearChrFlags(0xFE, 0x800)
    OP_99(0xFE, 0x4, 0x7, 0x9C4)
    SetChrSubChip(0xFE, 1)
    Return()

    # Function_36_367D end

    def Function_37_3856(): pass

    label("Function_37_3856")

    OP_22(0xA3, 0x0, 0x64)
    OP_96(0xFE, 0xFFFF506A, 0xFFFFF830, 0x64FA, 0x44C, 0x1388)
    OP_22(0xA4, 0x0, 0x64)
    OP_8C(0xFE, 225, 400)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 19)
    OP_8E(0xFE, 0xFFFF43A4, 0xFFFFF830, 0x5D5C, 0x1770, 0x0)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 20)

    def lambda_38AC():
        OP_99(0xFE, 0x0, 0x7, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_38AC)
    Sleep(200)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    PlayEffect(0x6, 0xFF, 0x14, 0, 500, 300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_44(0x14, 0x3)
    SetChrChipByIndex(0x14, 27)
    SetChrSubChip(0x14, 0)

    def lambda_3915():
        OP_9E(0xFE, 0x1E, 0x0, 0x7D0, 0xFA0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3915)
    WaitChrThread(0xFE, 0x2)

    def lambda_3934():
        OP_99(0xFE, 0x0, 0x7, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3934)
    Sleep(200)
    PlayEffect(0x6, 0xFF, 0x14, 0, 500, 300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_44(0x14, 0x1)
    WaitChrThread(0xFE, 0x2)
    SetChrChipByIndex(0x14, 14)
    SetChrSubChip(0x14, 0)
    SetChrSubChip(0xFE, 1)

    def lambda_39A7():
        OP_96(0xFE, 0xFFFF43A4, 0xFFFFF830, 0x5D5C, 0xFA0, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_39A7)
    WaitChrThread(0xFE, 0x3)

    def lambda_39CA():
        OP_99(0xE, 0x1, 0x4, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_39CA)
    OP_43(0x14, 0x3, 0x0, 0x26)
    WaitChrThread(0xFE, 0x2)
    SetChrFlags(0xFE, 0x2)

    def lambda_39EB():
        OP_96(0xFE, 0xFFFF4548, 0xFFFFF830, 0x5E88, 0x7D0, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_39EB)
    SetChrSubChip(0xFE, 1)
    OP_99(0xFE, 0x0, 0x7, 0xFA0)
    OP_99(0xFE, 0x0, 0x7, 0xFA0)
    ClearChrFlags(0xFE, 0x2)
    WaitChrThread(0xFE, 0x3)
    SetChrSubChip(0xFE, 0)

    def lambda_3A2F():
        TurnDirection(0xFE, 0x17, 0)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_3A2F)
    Return()

    # Function_37_3856 end

    def Function_38_3A38(): pass

    label("Function_38_3A38")

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    PlayEffect(0x6, 0xFF, 0x14, 0, 1000, 300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0x14, 0x20)
    SetChrChipByIndex(0x14, 27)
    SetChrSubChip(0x14, 0)

    def lambda_3A93():
        OP_94(0x1, 0x14, 0x0, 0xFFFFEC78, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_3A93)

    def lambda_3AA9():
        OP_9F(0x14, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_3AA9)
    WaitChrThread(0x14, 0x0)
    OP_22(0x20B, 0x0, 0x64)
    SetChrFlags(0x14, 0x80)
    Return()

    # Function_38_3A38 end

    def Function_39_3AC5(): pass

    label("Function_39_3AC5")

    OP_22(0xA3, 0x0, 0x64)
    OP_96(0xFE, 0xFFFF455C, 0xFFFFF830, 0x6824, 0x3E8, 0x1388)
    OP_22(0xA4, 0x0, 0x64)
    OP_8C(0xFE, 225, 400)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 15)
    OP_8E(0xFE, 0xFFFF3882, 0xFFFFF830, 0x5FAA, 0x1770, 0x0)
    SetChrFlags(0x15, 0x20)
    SetChrFlags(0xFE, 0x20)
    SetChrSubChip(0xD, 0)
    SetChrChipByIndex(0xD, 16)

    def lambda_3B25():
        OP_99(0xFE, 0x0, 0x5, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3B25)
    Sleep(200)
    PlayEffect(0x6, 0xFF, 0x15, 0, 500, 300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_44(0x15, 0x3)
    SetChrChipByIndex(0x15, 27)
    SetChrSubChip(0x15, 0)

    def lambda_3B8E():
        OP_9E(0xFE, 0x1E, 0x0, 0x7D0, 0xFA0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_3B8E)

    def lambda_3BA8():
        OP_99(0xFE, 0x0, 0x5, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3BA8)
    Sleep(200)
    PlayEffect(0x6, 0xFF, 0x15, 0, 500, 300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    WaitChrThread(0xFE, 0x2)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_3C0D():
        OP_96(0xFE, 0xFFFF4098, 0xFFFFF830, 0x66BC, 0x1F4, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3C0D)
    SetChrChipByIndex(0xD, 18)
    SetChrSubChip(0xFE, 1)
    WaitChrThread(0xFE, 0x3)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(300)

    def lambda_3C44():
        OP_8F(0xFE, 0xFFFF3832, 0xFFFFF830, 0x5FAA, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3C44)
    SetChrChipByIndex(0xD, 16)
    SetChrSubChip(0xFE, 0)
    OP_99(0xFE, 0x0, 0x3, 0xBB8)
    WaitChrThread(0xFE, 0x3)
    PlayEffect(0x6, 0xFF, 0x15, 0, 500, 300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)

    def lambda_3CBD():
        OP_9F(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_3CBD)
    OP_94(0x1, 0x15, 0x0, 0xFFFFE890, 0x5DC0, 0x0)
    SetChrFlags(0x15, 0x80)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 9)
    OP_22(0x20B, 0x0, 0x64)
    ClearChrFlags(0x15, 0x20)
    OP_99(0xFE, 0x4, 0x7, 0x9C4)
    Return()

    # Function_39_3AC5 end

    def Function_40_3CFB(): pass

    label("Function_40_3CFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D1A")
    OP_22(0x13F, 0x0, 0x4B)
    Sleep(150)
    OP_22(0x13F, 0x0, 0x4B)
    Sleep(300)
    Jump("Function_40_3CFB")

    label("loc_3D1A")

    OP_22(0x13F, 0x0, 0x41)
    Sleep(150)
    OP_22(0x13F, 0x0, 0x41)
    Sleep(300)
    OP_22(0x13F, 0x0, 0x37)
    Sleep(150)
    OP_22(0x13F, 0x0, 0x37)
    Sleep(300)
    OP_22(0x13F, 0x0, 0x2D)
    Sleep(150)
    OP_22(0x13F, 0x0, 0x2D)
    Sleep(300)
    OP_22(0x13F, 0x0, 0x23)
    Sleep(150)
    OP_22(0x13F, 0x0, 0x23)
    Sleep(300)
    OP_22(0x13F, 0x0, 0x19)
    Sleep(150)
    OP_22(0x13F, 0x0, 0x19)
    Sleep(300)
    Return()

    # Function_40_3CFB end

    def Function_41_3D7F(): pass

    label("Function_41_3D7F")

    OP_8E(0xFE, 0xFFFF5FA6, 0xFFFFF830, 0x792C, 0xBB8, 0x0)

    def lambda_3D99():

        label("loc_3D99")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_3D99")

    QueueWorkItem2(0xFE, 3, lambda_3D99)
    Return()

    # Function_41_3D7F end

    def Function_42_3DA5(): pass

    label("Function_42_3DA5")

    OP_8E(0xFE, 0xFFFF5D08, 0xFFFFF830, 0x75EE, 0xBB8, 0x0)

    def lambda_3DBF():

        label("loc_3DBF")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_3DBF")

    QueueWorkItem2(0xFE, 3, lambda_3DBF)
    Return()

    # Function_42_3DA5 end

    def Function_43_3DCB(): pass

    label("Function_43_3DCB")

    OP_8E(0xFE, 0xFFFF680C, 0xFFFFF827, 0x60C2, 0xBB8, 0x0)

    def lambda_3DE5():

        label("loc_3DE5")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_3DE5")

    QueueWorkItem2(0xFE, 3, lambda_3DE5)
    Return()

    # Function_43_3DCB end

    def Function_44_3DF1(): pass

    label("Function_44_3DF1")

    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 24)
    OP_8E(0xFE, 0xFFFF6C1C, 0xFFFFF880, 0x7A9E, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFF678A, 0xFFFFF830, 0x7602, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFF644C, 0xFFFFF830, 0x7008, 0x1388, 0x0)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 13)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_44_3DF1 end

    def Function_45_3E49(): pass

    label("Function_45_3E49")

    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 24)
    OP_8E(0xFE, 0xFFFF7568, 0xFFFFF830, 0x6AF4, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFF67B2, 0xFFFFF830, 0x68C4, 0x1388, 0x0)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 13)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_45_3E49 end

    def Function_46_3E8D(): pass

    label("Function_46_3E8D")

    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 24)
    OP_8E(0xFE, 0xFFFF67B2, 0xFFFFF830, 0x68C4, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFF61D6, 0xFFFFF830, 0x6FEA, 0x1388, 0x0)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 13)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_46_3E8D end

    def Function_47_3ED1(): pass

    label("Function_47_3ED1")

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
        (0, "loc_3F4B"),
        (1, "loc_3F51"),
        (SWITCH_DEFAULT, "loc_3F57"),
    )


    label("loc_3F4B")

    OP_A2(0x1200)
    Jump("loc_3F57")

    label("loc_3F51")

    OP_A2(0x1201)
    Jump("loc_3F57")

    label("loc_3F57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_3F65")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_3F69")

    label("loc_3F65")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_3F69")

    Return()

    # Function_47_3ED1 end

    def Function_48_3F6A(): pass

    label("Function_48_3F6A")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #62
        "\x07\x05北　玛西亚孤儿院\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_48_3F6A end

    def Function_49_3FAD(): pass

    label("Function_49_3FAD")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #63
        (
            "\x07\x05东　卢安市　　２３８塞尔矩\x01",
            "西　玛诺利亚村　７４塞尔矩\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_49_3FAD end

    SaveToFile()

Try(main)
