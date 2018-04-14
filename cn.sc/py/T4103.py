from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4103   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4103.x',
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
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '诺雅尔',                               # 9
        '维基奥',                               # 10
        '巴鲁托',                               # 11
        '王国军士兵',                           # 12
        '王国军士兵',                           # 13
        '巡逻兵',                               # 14
        '吉赛尔',                               # 15
        '杜南公爵',                             # 16
        '凯诺娜',                               # 17
        '特务兵',                               # 18
        '特务兵',                               # 19
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
        '士兵',                                 # 31
        '士兵',                                 # 32
        '士兵',                                 # 33
        '士兵',                                 # 34
        '士兵',                                 # 35
        '王都格兰赛尔·西街区',                 # 36
        '格兰赛尔城',                           # 37
        '王都格兰赛尔·东街区',                 # 38
        '王都格兰赛尔·南街区',                 # 39
        '',                                     # 40
        '',                                     # 41
        '',                                     # 42
        '',                                     # 43
        '',                                     # 44
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
        'ED6_DT07/CH02140 ._CH',             # 01
        'ED6_DT27/CH03120 ._CH',             # 02
        'ED6_DT07/CH01610 ._CH',             # 03
        'ED6_DT06/CH20043 ._CH',             # 04
        'ED6_DT07/CH01130 ._CH',             # 05
        'ED6_DT07/CH01290 ._CH',             # 06
        'ED6_DT07/CH01200 ._CH',             # 07
        'ED6_DT27/CH04610 ._CH',             # 08
        'ED6_DT27/CH04611 ._CH',             # 09
        'ED6_DT27/CH04620 ._CH',             # 0A
        'ED6_DT27/CH04621 ._CH',             # 0B
        'ED6_DT29/CH12570 ._CH',             # 0C
        'ED6_DT29/CH12571 ._CH',             # 0D
        'ED6_DT29/CH12350 ._CH',             # 0E
        'ED6_DT29/CH12351 ._CH',             # 0F
        'ED6_DT29/CH12320 ._CH',             # 10
        'ED6_DT29/CH12321 ._CH',             # 11
        'ED6_DT07/CH01230 ._CH',             # 12
    )

    AddCharChipPat(
        'ED6_DT07/CH01640P._CP',             # 00
        'ED6_DT07/CH02140P._CP',             # 01
        'ED6_DT27/CH03120P._CP',             # 02
        'ED6_DT07/CH01610P._CP',             # 03
        'ED6_DT06/CH20043P._CP',             # 04
        'ED6_DT07/CH01130P._CP',             # 05
        'ED6_DT07/CH01290P._CP',             # 06
        'ED6_DT07/CH01200P._CP',             # 07
        'ED6_DT27/CH04610P._CP',             # 08
        'ED6_DT27/CH04611P._CP',             # 09
        'ED6_DT27/CH04620P._CP',             # 0A
        'ED6_DT27/CH04621P._CP',             # 0B
        'ED6_DT29/CH12570P._CP',             # 0C
        'ED6_DT29/CH12571P._CP',             # 0D
        'ED6_DT29/CH12350P._CP',             # 0E
        'ED6_DT29/CH12351P._CP',             # 0F
        'ED6_DT29/CH12320P._CP',             # 10
        'ED6_DT29/CH12321P._CP',             # 11
        'ED6_DT07/CH01230P._CP',             # 12
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -2950,
        Z                   = 0,
        Y                   = 63820,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -7440,
        Z                   = 0,
        Y                   = 49400,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
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
        X                   = 7690,
        Z                   = 0,
        Y                   = 41560,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 8,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x1A0,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -40080,
        Z                   = 0,
        Y                   = 17660,
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
        X                   = 100,
        Z                   = 0,
        Y                   = 104130,
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
        X                   = 40430,
        Z                   = 0,
        Y                   = 64060,
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
        X                   = 20,
        Z                   = 0,
        Y                   = -3500,
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
        X                   = 170,
        Z                   = 0,
        Y                   = 39490,
        Unknown_0C          = 180,
        Unknown_0E          = 16,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x54A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 16030,
        Z                   = 0,
        Y                   = 63610,
        Unknown_0C          = 180,
        Unknown_0E          = 12,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x548,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -40070,
        Z                   = 0,
        Y                   = 49910,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x547,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -14730,
        Z                   = 0,
        Y                   = 50220,
        Unknown_0C          = 180,
        Unknown_0E          = 14,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x549,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 9080,
        Z                   = 250,
        Y                   = 58390,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x546,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 18520,
        Y                   = 0,
        Z                   = 44050,
        Range               = 1500,
        Unknown_10          = 0x9C4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 26,
    )


    DeclActor(
        TriggerX            = 19260,
        TriggerZ            = 750,
        TriggerY            = 44000,
        TriggerRange        = 800,
        ActorX              = 19260,
        ActorZ              = 1750,
        ActorY              = 44000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 21,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -23040,
        TriggerZ            = 500,
        TriggerY            = 63200,
        TriggerRange        = 800,
        ActorX              = -23040,
        ActorZ              = 1500,
        ActorY              = 63200,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 21,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -22160,
        TriggerZ            = 500,
        TriggerY            = 29050,
        TriggerRange        = 800,
        ActorX              = -22160,
        ActorZ              = 1500,
        ActorY              = 29050,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 21,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_63A",          # 00, 0
        "Function_1_6EB",          # 01, 1
        "Function_2_7AB",          # 02, 2
        "Function_3_7C1",          # 03, 3
        "Function_4_807",          # 04, 4
        "Function_5_A18",          # 05, 5
        "Function_6_A72",          # 06, 6
        "Function_7_B09",          # 07, 7
        "Function_8_C10",          # 08, 8
        "Function_9_C34",          # 09, 9
        "Function_10_FED",         # 0A, 10
        "Function_11_11FF",        # 0B, 11
        "Function_12_1571",        # 0C, 12
        "Function_13_16B4",        # 0D, 13
        "Function_14_17A6",        # 0E, 14
        "Function_15_18DA",        # 0F, 15
        "Function_16_1D0C",        # 10, 16
        "Function_17_1D51",        # 11, 17
        "Function_18_1DD3",        # 12, 18
        "Function_19_23DA",        # 13, 19
        "Function_20_2876",        # 14, 20
        "Function_21_2A4F",        # 15, 21
        "Function_22_2A88",        # 16, 22
        "Function_23_2D07",        # 17, 23
        "Function_24_2F86",        # 18, 24
        "Function_25_300D",        # 19, 25
        "Function_26_3066",        # 1A, 26
    )


    def Function_0_63A(): pass

    label("Function_0_63A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 2)), scpexpr(EXPR_END)), "loc_645")
    Call(0, 20)

    label("loc_645")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_663")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xE, 0x80)
    Jump("loc_6C3")

    label("loc_663")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_67C")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xE, 0x80)
    Jump("loc_6C3")

    label("loc_67C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_690")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_6C3")

    label("loc_690")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_6A4")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_6C3")

    label("loc_6A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6B2")
    Jump("loc_6C3")

    label("loc_6B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_6BC")
    Jump("loc_6C3")

    label("loc_6BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_6C3")

    label("loc_6C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_6D9")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 18)
    Jump("loc_6EA")

    label("loc_6D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6EA")
    SetMapFlags(0x10000000)
    Event(0, 15)

    label("loc_6EA")

    Return()

    # Function_0_63A end

    def Function_1_6EB(): pass

    label("Function_1_6EB")

    OP_16(0x2, 0xFA0, 0xFFFDE4F0, 0xFFFECF50, 0x23005E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_712")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_712")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_732")
    OP_B1("t4103_y")
    Jump("loc_753")

    label("loc_732")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_74A")
    OP_B1("t4103_y")
    Jump("loc_753")

    label("loc_74A")

    OP_B1("t4103_n")

    label("loc_753")

    OP_51(0x27, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 2)), scpexpr(EXPR_END)), "loc_79C")
    OP_72(0x2, 0x10)
    OP_72(0x3, 0x10)
    OP_72(0x4, 0x10)
    OP_1B(0x4, 0x0, 0x17)
    OP_1B(0x5, 0x0, 0x16)
    OP_77(0xFF, 0xBD, 0xA7, 0x0, 0x0)
    Call(0, 19)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)
    Jump("loc_7AA")

    label("loc_79C")

    OP_64(0x0, 0x1)
    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)
    OP_B5(0x0)

    label("loc_7AA")

    Return()

    # Function_1_6EB end

    def Function_2_7AB(): pass

    label("Function_2_7AB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7C0")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_7AB")

    label("loc_7C0")

    Return()

    # Function_2_7AB end

    def Function_3_7C1(): pass

    label("Function_3_7C1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_806")
    SetChrPos(0xFE, 31870, 0, 62980, 270)
    OP_8E(0xFE, 0xC6C, 0x0, 0xF604, 0x7D0, 0x0)
    OP_8E(0xFE, 0xC6C, 0x0, 0x40CE, 0x7D0, 0x0)
    Jump("Function_3_7C1")

    label("loc_806")

    Return()

    # Function_3_7C1 end

    def Function_4_807(): pass

    label("Function_4_807")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A17")
    SetChrPos(0xFE, -40860, 0, 28340, 0)
    OP_8E(0xFE, 0xFFFF6064, 0x0, 0xBAE0, 0x2328, 0x0)
    OP_8E(0xFE, 0xFFFF624E, 0x0, 0xC422, 0x2328, 0x0)
    OP_8E(0xFE, 0xFFFFA33A, 0x0, 0xC5F8, 0x2328, 0x0)
    OP_8C(0xFE, 0, 800)
    Sleep(300)
    OP_8E(0xFE, 0xFFFFA33A, 0xFA, 0xE9DE, 0x2328, 0x0)
    OP_8E(0xFE, 0xFFFF9F48, 0xFA, 0xF1F4, 0x2328, 0x0)
    OP_8C(0xFE, 0, 800)
    Sleep(400)
    OP_8E(0xFE, 0xFFFFA33A, 0xFA, 0xE9DE, 0x2328, 0x0)
    OP_8E(0xFE, 0xFFFFA33A, 0x0, 0xC5F8, 0x2328, 0x0)
    OP_8E(0xFE, 0xFFFFE674, 0x0, 0xC5F8, 0x2328, 0x0)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)
    OP_8E(0xFE, 0xFFFFECDC, 0x0, 0xCED6, 0x2328, 0x0)
    OP_8E(0xFE, 0xFFFFECDC, 0x0, 0xF276, 0x2328, 0x0)
    OP_8E(0xFE, 0xFFFFF16E, 0x0, 0xFD84, 0x2328, 0x0)
    OP_8E(0xFE, 0x9B8C, 0x0, 0xFD84, 0x2328, 0x0)
    Sleep(2000)
    SetChrPos(0xFE, 39650, 0, 62210, 90)
    OP_8E(0xFE, 0x67A2, 0x0, 0xF302, 0x2328, 0x0)
    OP_8E(0xFE, 0x56B8, 0xFA, 0xE60A, 0x2328, 0x0)
    OP_8E(0xFE, 0x2A9E, 0xFA, 0xE60A, 0x2328, 0x0)
    OP_8E(0xFE, 0x2288, 0xFA, 0xDC00, 0x2328, 0x0)
    OP_8E(0xFE, 0x2288, 0xFA, 0xC030, 0x2328, 0x0)
    OP_8E(0xFE, 0x2BE8, 0xFA, 0xB6D0, 0x2328, 0x0)
    OP_8E(0xFE, 0x402E, 0xFA, 0xB6D0, 0x2328, 0x0)
    Sleep(400)
    OP_8E(0xFE, 0x1EF0, 0xFA, 0x8E12, 0x2328, 0x0)
    OP_8E(0xFE, 0x1EF0, 0xFA, 0x1F04, 0x2328, 0x0)
    Sleep(2000)
    Jump("Function_4_807")

    label("loc_A17")

    Return()

    # Function_4_807 end

    def Function_5_A18(): pass

    label("Function_5_A18")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A71")
    SetChrPos(0xFE, -4340, 0, 16160, 0)
    OP_8E(0xFE, 0xFFFFEF0C, 0x0, 0xBD74, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFF6866, 0x0, 0xBD74, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFF6866, 0x0, 0x6B58, 0x9C4, 0x0)
    Jump("Function_5_A18")

    label("loc_A71")

    Return()

    # Function_5_A18 end

    def Function_6_A72(): pass

    label("Function_6_A72")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B08")
    OP_8E(0xFE, 0xFFFFF47A, 0x0, 0xC300, 0x9C4, 0x0)
    OP_8C(0xFE, 270, 400)
    Sleep(2000)
    OP_8E(0xFE, 0xFFFFF47A, 0x0, 0x5528, 0x9C4, 0x0)
    Sleep(2000)
    OP_8C(0xFE, 270, 400)
    Sleep(2000)
    OP_8E(0xFE, 0xFFFFF47A, 0x0, 0xC300, 0x9C4, 0x0)
    OP_8C(0xFE, 270, 400)
    Sleep(2000)
    OP_8E(0xFE, 0xFFFFF47A, 0x0, 0xF94C, 0x9C4, 0x0)
    Sleep(2000)
    OP_8C(0xFE, 90, 400)
    Sleep(2000)
    Jump("Function_6_A72")

    label("loc_B08")

    Return()

    # Function_6_A72 end

    def Function_7_B09(): pass

    label("Function_7_B09")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C0F")
    OP_8E(0xFE, 0xFFFFA68C, 0x0, 0xC0F8, 0x9C4, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(2000)
    OP_8E(0xFE, 0xFFFFA68C, 0x0, 0xC0F8, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFF65E6, 0x0, 0xBBE4, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFF64BA, 0x0, 0xB644, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFF64BA, 0x0, 0x9592, 0x9C4, 0x0)
    Sleep(2000)
    OP_8E(0xFE, 0xFFFF64BA, 0x0, 0xB644, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFF676C, 0x0, 0xC1E8, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFFA68C, 0x0, 0xC0F8, 0x9C4, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(2000)
    OP_8E(0xFE, 0xFFFFE2F0, 0x0, 0xC0F8, 0x9C4, 0x0)
    Sleep(2000)
    OP_8C(0xFE, 0, 400)
    Sleep(2000)
    OP_8C(0xFE, 180, 400)
    Sleep(2000)
    OP_8C(0xFE, 90, 400)
    Sleep(2000)
    Jump("Function_7_B09")

    label("loc_C0F")

    Return()

    # Function_7_B09 end

    def Function_8_C10(): pass

    label("Function_8_C10")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C33")
    OP_8D(0xFE, 8130, 41700, 5710, 43100, 2000)
    Jump("Function_8_C10")

    label("loc_C33")

    Return()

    # Function_8_C10 end

    def Function_9_C34(): pass

    label("Function_9_C34")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_C9F")

    ChrTalk(    #0
        0xFE,
        (
            "大家都认为女王陛下\x01",
            "会想办法的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "导力停止的原因\x01",
            "还不明吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        "我非常非常不安……\x02",
    )

    CloseMessageWindow()
    Jump("loc_FE9")

    label("loc_C9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_D14")

    ChrTalk(    #3
        0xFE,
        (
            "西街区的事你们听说了吗？\x01",
            "真是了不得。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "不过情报部的余党\x01",
            "也因此不复存在了，\x01",
            "生活得能稍微安心点了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FE9")

    label("loc_D14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_D8E")

    ChrTalk(    #5
        0xFE,
        (
            "我和以前在附近看到的\x01",
            "旅行者的孩子擦肩而过了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "虽然那孩子平时\x01",
            "都和父母在一起。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        "不知道要不要紧……\x02",
    )

    CloseMessageWindow()
    Jump("loc_FE9")

    label("loc_D8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DEA")

    ChrTalk(    #8
        0xFE,
        (
            "哎呀，讨厌。\x01",
            "已经这么晚了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "在百货商店关门之前\x01",
            "要买好晚饭的原料。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FE9")

    label("loc_DEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_E9A")

    ChrTalk(    #10
        0xFE,
        "可能是签字仪式近了的缘故……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "最近，帝国和共和国的大使馆的人\x01",
            "好像频繁出入着到城堡。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "互不侵犯条约虽然像梦一样，不过现在\x01",
            "我开始感受到它的真实存在感了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FE9")

    label("loc_E9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_FE9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F6A")

    ChrTalk(    #13
        0xFE,
        (
            "向普通人开放的\x01",
            "城堡游览项目因政变被中止,但是现在恢复了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        "我自然要推荐空中庭园。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "从瓦雷利亚湖吹来的清爽的风\x01",
            "和庭园的草木的香味儿真的很舒服。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        "#1003F…………………………\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_FE9")

    label("loc_F6A")


    ChrTalk(    #17
        0xFE,
        (
            "向普通人开放的\x01",
            "城堡游览项目因政变被中止,但是现在恢复了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "从瓦雷利亚湖吹来的清爽的风\x01",
            "和庭园的草木的香味儿真的很舒服。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FE9")

    TalkEnd(0xFE)
    Return()

    # Function_9_C34 end

    def Function_10_FED(): pass

    label("Function_10_FED")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1052")

    ChrTalk(    #19
        0xFE,
        (
            "在港口能看见那个\x01",
            "形状古怪的物体。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "从王城的女王宫应该\x01",
            "能看清那个方向的东西……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11FB")

    label("loc_1052")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_10DA")

    ChrTalk(    #21
        0xFE,
        (
            "港湾区出现了巨大的\x01",
            "人形兵器吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "传闻说拉赛尔博士\x01",
            "制造的新兵器失控了，\x01",
            "真的假的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "没有官方消息，\x01",
            "所以传闻很多。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11FB")

    label("loc_10DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_112A")

    ChrTalk(    #24
        0xFE,
        (
            "说起来，我刚才\x01",
            "在飞船坪听说……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "卢安的新市长\x01",
            "终于产生了哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11FB")

    label("loc_112A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1198")

    ChrTalk(    #26
        0xFE,
        (
            "说起来，卢安现在\x01",
            "正在选举市长呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        "那个戴尔蒙的后任啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "真希望他能\x01",
            "重振卢安啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11FB")

    label("loc_1198")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_11D6")

    ChrTalk(    #29
        0xFE,
        "啊，忙死了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        "下一个投送地点在东街区……\x02",
    )

    CloseMessageWindow()
    Jump("loc_11FB")

    label("loc_11D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_11FB")

    ChrTalk(    #31
        0xFE,
        "让开让开，快递公司来了！\x02",
    )

    CloseMessageWindow()

    label("loc_11FB")

    TalkEnd(0xFE)
    Return()

    # Function_10_FED end

    def Function_11_11FF(): pass

    label("Function_11_11FF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_12A7")

    ChrTalk(    #32
        0xFE,
        (
            "我正在遵照女王陛下的\x01",
            "指示挨家挨户地说明情况。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "大家似乎还没能完全接受，\x01",
            "虽然这也是理所当然的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "这样下去的话稍有风吹草动\x01",
            "就有可能引发恐慌……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_156D")

    label("loc_12A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1356")

    ChrTalk(    #35
        0xFE,
        (
            "情报部的预算有很多\x01",
            "被操纵过的痕迹……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "仅据我所了解的情况，\x01",
            "就有不少去向不明的资金。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "恐怕就是这次的\x01",
            "坦克的开发费用吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        "通过这次的事件都连成线了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_156D")

    label("loc_1356")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1424")

    ChrTalk(    #39
        0xFE,
        (
            "以准将身份回归军队的\x01",
            "卡西乌斯先生真了不起。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "不仅军事策略，连财政方面也\x01",
            "能做出正确的指示。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "不愧是击退了帝国军、\x01",
            "曾被誉为智将的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "在城里和他碰见的话\x01",
            "连我也会不自觉地紧张起来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_156D")

    label("loc_1424")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1459")

    ChrTalk(    #43
        0xFE,
        (
            "呼，该回城一次向\x01",
            "女王陛下报告……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_156D")

    label("loc_1459")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1504")

    ChrTalk(    #44
        0xFE,
        (
            "传言生病了的女王陛下\x01",
            "其实很健康哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "不过她还要收拾政变之后的局势，\x01",
            "还有签字仪式的准备工作一定很忙吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "我倒是觉得签字仪式\x01",
            "稍微推迟一点也没关系……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_156D")

    label("loc_1504")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_156D")

    ChrTalk(    #47
        0xFE,
        (
            "我是在王城工作的，\x01",
            "正在调查政变事件。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "虽然恢复了和平，不过\x01",
            "那件事的不良影响还是很深的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_156D")

    TalkEnd(0xFE)
    Return()

    # Function_11_11FF end

    def Function_12_1571(): pass

    label("Function_12_1571")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_15B3")

    ChrTalk(    #49
        0xFE,
        (
            "为了不让市民们动摇，\x01",
            "我们得保持泰然自若的姿态。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16B0")

    label("loc_15B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_166A")

    ChrTalk(    #50
        0xFE,
        (
            "从某种意义上说凯诺娜上尉\x01",
            "是个很厉害的女人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "正因为她有能力，\x01",
            "才能实行那个作战方案。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "要是那些无能的士官\x01",
            "怎么可能有这种计划。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        "和她为敌真是吃不了兜着走。\x02",
    )

    CloseMessageWindow()
    Jump("loc_16B0")

    label("loc_166A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_16B0")

    ChrTalk(    #54
        0xFE,
        (
            "签字仪式虽然在离宫进行，\x01",
            "不过上面吩咐也要加强王都的警戒。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16B0")

    TalkEnd(0xFE)
    Return()

    # Function_12_1571 end

    def Function_13_16B4(): pass

    label("Function_13_16B4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_16FA")

    ChrTalk(    #55
        0xFE,
        (
            "没事儿，就算不能使用导力，\x01",
            "我也会用刺刀保护大家的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17A2")

    label("loc_16FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1780")

    ChrTalk(    #56
        0xFE,
        (
            "如果坦克侵入市区的话\x01",
            "受害情况就绝不止这样了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "如果做错一步的话\x01",
            "王都就有可能陷入火海了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        "……想想都觉得可怕。\x02",
    )

    CloseMessageWindow()
    Jump("loc_17A2")

    label("loc_1780")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_17A2")

    ChrTalk(    #59
        0xFE,
        (
            "好，现在没\x01",
            "任何异常。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17A2")

    TalkEnd(0xFE)
    Return()

    # Function_13_16B4 end

    def Function_14_17A6(): pass

    label("Function_14_17A6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_17CB")

    ChrTalk(    #60
        0xFE,
        "吉赛尔　临时消息。\x02",
    )

    CloseMessageWindow()
    Jump("loc_18D6")

    label("loc_17CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_17FA")

    ChrTalk(    #61
        0xFE,
        (
            "坦克竟然出现在城里，\x01",
            "真可怕……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18D6")

    label("loc_17FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1849")

    ChrTalk(    #62
        0xFE,
        (
            "……穿白衣服的女孩子？\x01",
            "那孩子迷路了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        "没看见她出现在附近。\x02",
    )

    CloseMessageWindow()
    Jump("loc_18D6")

    label("loc_1849")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1880")

    ChrTalk(    #64
        0xFE,
        (
            "那么，差不多该\x01",
            "要不要回宾馆房间呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18D6")

    label("loc_1880")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_18A4")

    ChrTalk(    #65
        0xFE,
        "好，去城堡参观参观。\x02",
    )

    CloseMessageWindow()
    Jump("loc_18D6")

    label("loc_18A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_18D6")

    ChrTalk(    #66
        0xFE,
        (
            "我一直憧憬有一天能\x01",
            "住在这家酒店里啊～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18D6")

    TalkEnd(0xFE)
    Return()

    # Function_14_17A6 end

    def Function_15_18DA(): pass

    label("Function_15_18DA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x2000000)
    OP_77(0xC8, 0xC8, 0xC8, 0x0, 0x0)
    OP_11(0x0, 0x0, 0x0, 0x9470, 0x1FBD0, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xE, 0x80)
    OP_4A(0x9, 255)
    OP_4A(0xA, 255)
    OP_4A(0x8, 255)
    OP_4A(0xB, 255)
    OP_4A(0xC, 255)
    OP_4A(0xE, 255)
    LoadEffect(0x0, "map\\\\mp014_00.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -2650, 0, 50890, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6D(-3300, 0, 71820, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -2540, 0, 73310, 180)
    SetChrPos(0xD, -2180, 0, 41910, 0)
    ClearChrFlags(0xD, 0x80)
    OP_43(0xD, 0x3, 0x0, 0x10)
    Sleep(600)
    FadeToBright(1000, 0)

    def lambda_1A02():
        OP_6D(-2650, 0, 50890, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1A02)
    OP_8E(0x101, 0xFFFFF5E2, 0x0, 0xC788, 0x1B58, 0x0)

    ChrTalk(    #67
        0x101,
        (
            "#584F#5P呼、呼……\x02\x03",

            "……………………………\x02\x03",

            "#588F不可能……\x02\x03",

            "约修亚怎么可能走掉……\x01",
            "这……不可能……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xD,
        (
            "#1P哎呀，小姐。\x01",
            "你在这里干什么？\x02",
        )
    )

    CloseMessageWindow()
    OP_92(0xD, 0x101, 0x7D0, 0xBB8, 0x0)

    ChrTalk(    #69
        0xD,
        (
            "在被淋湿之前\x01",
            "赶紧回家吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x101,
        (
            "#004F#5P啊……\x02\x03",

            "………………………………\x02\x03",

            "#586F……对，是的。\x02\x03",

            "约修亚不可能走掉……\x02\x03",

            "他一定是……先回家了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xD,
        "咦？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x101,
        (
            "#006F#5P谢谢你，士兵先生！\x02\x03",

            "我马上回家！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1B96():
        OP_6D(-1170, 0, 52220, 1000)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_1B96)

    def lambda_1BAE():
        OP_67(0, 9500, -10000, 1000)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1BAE)
    OP_8C(0x101, 45, 800)

    def lambda_1BCD():
        OP_8E(0x101, 0x758, 0x0, 0xD548, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1BCD)
    WaitChrThread(0x101, 0x1)

    def lambda_1BED():
        OP_8E(0x101, 0x938, 0x0, 0xEB3C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1BED)
    Sleep(1500)

    def lambda_1C0D():
        OP_6D(-2550, 0, 49300, 1500)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_1C0D)

    def lambda_1C25():
        OP_67(0, 9500, -10000, 1500)
        ExitThread()

    QueueWorkItem(0xD, 3, lambda_1C25)
    Sleep(1500)

    ChrTalk(    #73
        0xD,
        "怎、怎么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xD,
        (
            "说起来刚才那女孩子……\x01",
            "我好像在哪儿见过。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #75
        0xD,
        (
            "对了！\x01",
            "她是帮忙阻止政变的……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(3000, 0, -1)
    OP_24(0x1C9, 0x5A)
    OP_0D()
    OP_AD(0x2400B6, 0x0, 0x0, 0x96)
    Sleep(1000)
    OP_56(0x2)
    OP_20(0xFA0)
    OP_43(0xD, 0x3, 0x0, 0x11)
    OP_AE(0xC8)
    OP_21()
    WaitChrThread(0xD, 0x3)
    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearMapFlags(0x10000000)
    NewScene("ED6_DT21/E0001   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_15_18DA end

    def Function_16_1D0C(): pass

    label("Function_16_1D0C")

    OP_22(0x1C9, 0x1, 0x1E)
    Sleep(300)
    OP_24(0x1C9, 0x28)
    Sleep(300)
    OP_24(0x1C9, 0x32)
    Sleep(300)
    OP_24(0x1C9, 0x3C)
    Sleep(300)
    OP_24(0x1C9, 0x46)
    Sleep(300)
    OP_24(0x1C9, 0x50)
    Sleep(300)
    OP_24(0x1C9, 0x5A)
    Sleep(300)
    OP_24(0x1C9, 0x64)
    Return()

    # Function_16_1D0C end

    def Function_17_1D51(): pass

    label("Function_17_1D51")

    OP_24(0x1C9, 0x5F)
    Sleep(200)
    OP_24(0x1C9, 0x5A)
    Sleep(200)
    OP_24(0x1C9, 0x55)
    Sleep(200)
    OP_24(0x1C9, 0x50)
    Sleep(200)
    OP_24(0x1C9, 0x4B)
    Sleep(200)
    OP_24(0x1C9, 0x46)
    Sleep(200)
    OP_24(0x1C9, 0x41)
    Sleep(200)
    OP_24(0x1C9, 0x3C)
    Sleep(200)
    OP_24(0x1C9, 0x37)
    Sleep(200)
    OP_24(0x1C9, 0x32)
    Sleep(200)
    OP_24(0x1C9, 0x2D)
    Sleep(200)
    OP_24(0x1C9, 0x28)
    Sleep(200)
    OP_24(0x1C9, 0x23)
    Sleep(200)
    OP_24(0x1C9, 0x1E)
    Sleep(200)
    OP_23(0x1C9)
    Return()

    # Function_17_1D51 end

    def Function_18_1DD3(): pass

    label("Function_18_1DD3")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xE, 0x80)
    OP_4A(0x9, 255)
    OP_4A(0xA, 255)
    OP_4A(0x8, 255)
    OP_4A(0xB, 255)
    OP_4A(0xC, 255)
    OP_4A(0xE, 255)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -40420, 0, 33150, 360)
    OP_6D(-40710, 0, 35630, 0)
    OP_67(0, 6910, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(120000, 0)
    OP_6E(262, 0)
    OP_69(0xF, 0x0)
    OP_C4(0x0, 0x40)
    OP_6A(0xF)
    FadeToBright(2000, 0)
    OP_8F(0xF, 0xFFFF62E4, 0x0, 0x83D6, 0x258, 0x0)
    Sleep(100)
    OP_8F(0xF, 0xFFFF621C, 0x0, 0x86F6, 0x3E8, 0x0)
    Sleep(50)
    OP_8F(0xF, 0xFFFF6154, 0x0, 0x8B2E, 0x258, 0x0)
    Sleep(50)

    ChrTalk(    #76
        0xF,
        (
            "#480F嗝……\x02\x03",

            "菲利普那家伙\x01",
            "总是对我说三道四……\x02\x03",

            "他以为\x01",
            "我是谁啊……\x02\x03",

            "我可是有着第一顺位王位继承权的……\x01",
            "杜南·冯·奥赛雷丝……\x02",
        )
    )

    CloseMessageWindow()
    OP_8F(0xF, 0xFFFF6280, 0x0, 0x8E62, 0x3E8, 0x0)
    Sleep(100)
    OP_8F(0xF, 0xFFFF6348, 0x0, 0x920E, 0x258, 0x0)
    Sleep(50)

    ChrTalk(    #77
        0xF,
        (
            "#483F唔……\x01",
            "好像有点喝多了……\x02\x03",

            "可是那个咖喱饭\x01",
            "味道相当不错……\x02\x03",

            "偶尔尝尝平民的味道也不坏……\x02",
        )
    )

    CloseMessageWindow()
    OP_8F(0xF, 0xFFFF63AC, 0x0, 0x9402, 0x3E8, 0x0)
    Sleep(100)
    OP_8F(0xF, 0xFFFF64CE, 0x0, 0x9786, 0x320, 0x0)
    Sleep(50)
    OP_6A(0xFF)
    OP_C4(0x1, 0x40)

    ChrTalk(    #78
        0xF,
        (
            "#480F……可恶……\x02\x03",

            "科洛蒂娅……\x01",
            "还有那个游击士小丫头……\x02\x03",

            "为什么我……\x01",
            "……会因为那些小丫头们……\x02\x03",

            "因为那些小丫头们的话……\x01",
            "而心烦意乱……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -39770, 0, 46180, 180)

    NpcTalk(    #79
        0x10,
        "女人的声音",
        (
            "#2P我了解公爵阁下的\x01",
            "痛苦。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_20(0x7D0)
    OP_6D(-39770, 0, 42350, 2000)

    ChrTalk(    #80
        0xF,
        (
            "#481F#4P什……\x02\x03",

            "你是理查德的……\x02",
        )
    )

    CloseMessageWindow()
    OP_1D(0x51)
    Sleep(500)

    ChrTalk(    #81
        0x10,
        (
            "#1180F#5P嗯，我是他的副官凯诺娜。\x02\x03",

            "公爵阁下你这么\x01",
            "精神真是太好了。\x02\x03",

            "#1183F呵呵，不过您的\x01",
            "情绪看来不佳……\x02",
        )
    )

    CloseMessageWindow()
    OP_91(0xF, 0x0, 0x0, 0xFFFFFE0C, 0x3E8, 0x0)

    ChrTalk(    #82
        0xF,
        (
            "#484F#4P你、你有什么事……\x02\x03",

            "我记得你们\x01",
            "正受到通缉吧……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2211():
        OP_6D(-39600, 0, 41260, 1200)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_2211)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x11, -39000, 0, 33000, 0)
    SetChrPos(0x12, -40500, 0, 33000, 0)

    def lambda_2255():
        OP_8E(0xFE, 0xFFFF67A8, 0x0, 0x8E94, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2255)
    Sleep(50)

    def lambda_2275():
        OP_8E(0xFE, 0xFFFF61CC, 0x0, 0x8E94, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2275)
    WaitChrThread(0x11, 0x1)
    WaitChrThread(0x12, 0x1)
    OP_62(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0xF, 180, 600)
    OP_62(0xF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_91(0xF, 0x0, 0x0, 0x1F4, 0x7D0, 0x0)

    ChrTalk(    #83
        0xF,
        "#484F#6P呀……！？\x02",
    )

    CloseMessageWindow()

    def lambda_22FB():
        OP_6D(-39600, 0, 38790, 2500)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_22FB)

    def lambda_2313():
        OP_92(0xFE, 0xF, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2313)
    Sleep(2000)
    OP_8C(0xF, 360, 400)
    OP_62(0xF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    WaitChrThread(0x10, 0x2)
    WaitChrThread(0x10, 0x1)
    Sleep(500)

    ChrTalk(    #84
        0x10,
        (
            "#1180F呵呵，您这么警惕的话\x01",
            "可要受伤的哦。\x02\x03",

            "我们只是……\x01",
            "想要帮助公爵阁下而已。\x02\x03",

            "#1181F好了，请跟我们来。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T0601   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_18_1DD3 end

    def Function_19_23DA(): pass

    label("Function_19_23DA")

    LoadEffect(0x0, "map\\\\mpsmk0.eff")
    LoadEffect(0x1, "map\\\\mpfire2.eff")
    LoadEffect(0x2, "map\\\\mpkaji0.eff")
    OP_22(0x87, 0x1, 0x50)
    OP_22(0xAE, 0x1, 0x50)
    PlayEffect(0x2, 0xFF, 0xFF, -150, 250, 42190, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 6610, 1800, -55210, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 18680, 5000, 41990, 0, 0, 0, 1500, 1800, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, -410, 3500, 33390, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, -16160, 4400, 33500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, -610, 3600, 25270, 0, 0, 0, 1300, 1500, 1300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 10660, 5000, 27200, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, -21520, 5000, 26000, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, -22010, 5000, 62980, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 760, 4200, 58600, 0, 0, 0, 1500, 1700, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, -46780, 3000, 52260, 0, 0, 0, 1600, 1800, 1600, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, -610, 3300, 25270, 0, 0, 0, 2200, 2200, 2200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, -22010, 4800, 62980, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 760, 3800, 58600, 0, 0, 0, 1700, 1700, 1700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 10660, 4800, 27200, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, -21520, 4700, 26000, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, -46780, 2480, 52260, 0, 0, 0, 2500, 2500, 2500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 16740, 4200, 51970, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, -410, 3400, 33390, 0, 0, 0, 1100, 1300, 1100, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, -16160, 3900, 33500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 18680, 4800, 41990, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_19_23DA end

    def Function_20_2876(): pass

    label("Function_20_2876")

    SetChrPos(0x13, -37620, 0, 37330, 45)
    SetChrPos(0x14, -41800, 0, 37210, 135)
    SetChrPos(0x15, 9070, 0, 30110, 315)
    SetChrPos(0x16, 8300, 0, 66830, 225)
    SetChrPos(0x17, -6670, 0, 58620, 135)
    SetChrPos(0x18, -2340, 0, 34710, 180)
    SetChrPos(0x19, -9060, 250, 28940, 90)
    SetChrPos(0x1A, 13690, 250, 44060, 270)
    SetChrPos(0x1B, 4640, 0, 44330, 225)
    SetChrPos(0x1C, -11050, 0, 50470, 90)
    SetChrPos(0x1D, -30670, 0, 47940, 180)
    SetChrPos(0x1E, 8950, 250, 58550, 225)
    SetChrPos(0x1F, 3900, 0, 60990, 315)
    SetChrPos(0x20, -7260, 0, 48580, 270)
    SetChrPos(0x21, -6530, 250, 36470, 315)
    SetChrPos(0x22, 5150, 10, 30490, 135)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
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
    ClearChrFlags(0x1E, 0x1)
    ClearChrFlags(0x1F, 0x1)
    ClearChrFlags(0x20, 0x1)
    ClearChrFlags(0x21, 0x1)
    ClearChrFlags(0x22, 0x1)
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
    SetChrFlags(0x1E, 0x20)
    SetChrFlags(0x1F, 0x20)
    SetChrFlags(0x20, 0x20)
    SetChrFlags(0x21, 0x20)
    SetChrFlags(0x22, 0x20)
    Return()

    # Function_20_2876 end

    def Function_21_2A4F(): pass

    label("Function_21_2A4F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #85
        "\x07\x05门上着锁。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    SetMapFlags(0x2000000)
    Return()

    # Function_21_2A4F end

    def Function_22_2A88(): pass

    label("Function_22_2A88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A91")
    Return()

    label("loc_2A91")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2AB1")
    Call(0, 24)
    Call(0, 25)
    FadeToBright(0, 0)

    label("loc_2AB1")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #86
        (
            "\x07\x05东街区断断续续地\x01",
            "传来枪声和剑戟的声音。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B59")

    ChrTalk(    #87
        0x101,
        (
            "#1002F（看来是军队在\x01",
            "和猎兵作战……)\x02\x03",

            "(我们得赶快\x01",
            "赶往城堡！)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CE6")

    label("loc_2B59")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BA8")

    ChrTalk(    #88
        0x102,
        (
            "#1042F（这边布置了\x01",
            "军队……)\x02\x03",

            "(就交给他们吧，我们去城堡。)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CE6")

    label("loc_2BA8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BF4")

    ChrTalk(    #89
        0x103,
        (
            "#022F（这边应该\x01",
            "有军队在作战……)\x02\x03",

            "(我们还是去城堡吧。)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CE6")

    label("loc_2BF4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C53")

    ChrTalk(    #90
        0x107,
        (
            "#062F（军队的失败们看来\x01",
            "正在结社的人作战……)\x02\x03",

            "(我们得赶快\x01",
            "赶往城堡……！)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CE6")

    label("loc_2C53")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CA3")

    ChrTalk(    #91
        0x106,
        (
            "#057F（看来军队住在\x01",
            "和猎兵们作战……)\x02\x03",

            "(我们还是去城堡吧。)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CE6")

    label("loc_2CA3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CE6")

    ChrTalk(    #92
        0x108,
        (
            "#072F（这边有军队\x01",
            "在守护……)\x02\x03",

            "(我们赶紧去王城吧)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CE6")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)
    Return()

    # Function_22_2A88 end

    def Function_23_2D07(): pass

    label("Function_23_2D07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D10")
    Return()

    label("loc_2D10")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D30")
    Call(0, 24)
    Call(0, 25)
    FadeToBright(0, 0)

    label("loc_2D30")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #93
        (
            "\x07\x05西街区断断续续地\x01",
            "传来枪声和剑戟的声音。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DD8")

    ChrTalk(    #94
        0x101,
        (
            "#1002F（看来是军队在\x01",
            "和猎兵作战……)\x02\x03",

            "(我们得赶快\x01",
            "赶往城堡！)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F65")

    label("loc_2DD8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E27")

    ChrTalk(    #95
        0x102,
        (
            "#1042F（这边布置了\x01",
            "军队……)\x02\x03",

            "(就交给他们吧，我们去城堡。)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F65")

    label("loc_2E27")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E73")

    ChrTalk(    #96
        0x103,
        (
            "#022F（这边应该\x01",
            "有军队在作战……)\x02\x03",

            "(我们还是去城堡吧。)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F65")

    label("loc_2E73")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2ED2")

    ChrTalk(    #97
        0x107,
        (
            "#062F（军队的失败们看来\x01",
            "正在结社的人作战……)\x02\x03",

            "(我们得赶快\x01",
            "赶往城堡……！)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F65")

    label("loc_2ED2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F22")

    ChrTalk(    #98
        0x106,
        (
            "#057F（看来军队住在\x01",
            "和猎兵们作战……)\x02\x03",

            "(我们还是去城堡吧。)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F65")

    label("loc_2F22")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F65")

    ChrTalk(    #99
        0x108,
        (
            "#072F（这边有军队\x01",
            "在守护……)\x02\x03",

            "(我们赶紧去王城吧)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F65")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)
    Return()

    # Function_23_2D07 end

    def Function_24_2F86(): pass

    label("Function_24_2F86")

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
        (0, "loc_3000"),
        (1, "loc_3006"),
        (SWITCH_DEFAULT, "loc_300C"),
    )


    label("loc_3000")

    OP_A2(0x1200)
    Jump("loc_300C")

    label("loc_3006")

    OP_A2(0x1201)
    Jump("loc_300C")

    label("loc_300C")

    Return()

    # Function_24_2F86 end

    def Function_25_300D(): pass

    label("Function_25_300D")

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

    # Function_25_300D end

    def Function_26_3066(): pass

    label("Function_26_3066")

    SetPlaceName(0xB4)
    Return()

    # Function_26_3066 end

    SaveToFile()

Try(main)
