from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'R0201   ._SN',
        MapName             = 'Rolent',
        Location            = 'R0201.x',
        MapIndex            = 22,
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
        '阿斯顿队长',                           # 9
        '士兵',                                 # 10
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
        '雾调整',                               # 22
        '洛连特方向',                           # 23
        '威尔特桥·关所方向',                   # 24
        '帕赛尔农场方向',                       # 25
        '窃魂兽',                               # 26
        '',                                     # 27
        '',                                     # 28
        '',                                     # 29
        '',                                     # 30
        '',                                     # 31
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
        'ED6_DT09/CH10020 ._CH',             # 00
        'ED6_DT09/CH10021 ._CH',             # 01
        'ED6_DT09/CH10180 ._CH',             # 02
        'ED6_DT09/CH10181 ._CH',             # 03
        'ED6_DT09/CH10260 ._CH',             # 04
        'ED6_DT09/CH10261 ._CH',             # 05
        'ED6_DT09/CH10210 ._CH',             # 06
        'ED6_DT09/CH10211 ._CH',             # 07
        'ED6_DT29/CH12090 ._CH',             # 08
        'ED6_DT29/CH12091 ._CH',             # 09
        'ED6_DT29/CH12130 ._CH',             # 0A
        'ED6_DT29/CH12131 ._CH',             # 0B
        'ED6_DT07/CH01310 ._CH',             # 0C
        'ED6_DT07/CH01640 ._CH',             # 0D
        'ED6_DT29/CH12400 ._CH',             # 0E
        'ED6_DT29/CH12401 ._CH',             # 0F
    )

    AddCharChipPat(
        'ED6_DT09/CH10020P._CP',             # 00
        'ED6_DT09/CH10021P._CP',             # 01
        'ED6_DT09/CH10180P._CP',             # 02
        'ED6_DT09/CH10181P._CP',             # 03
        'ED6_DT09/CH10260P._CP',             # 04
        'ED6_DT09/CH10261P._CP',             # 05
        'ED6_DT09/CH10210P._CP',             # 06
        'ED6_DT09/CH10211P._CP',             # 07
        'ED6_DT29/CH12090P._CP',             # 08
        'ED6_DT29/CH12091P._CP',             # 09
        'ED6_DT29/CH12130P._CP',             # 0A
        'ED6_DT29/CH12131P._CP',             # 0B
        'ED6_DT07/CH01310P._CP',             # 0C
        'ED6_DT07/CH01640P._CP',             # 0D
        'ED6_DT29/CH12400P._CP',             # 0E
        'ED6_DT29/CH12401P._CP',             # 0F
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -131580,
        Z                   = 0,
        Y                   = -18130,
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
        X                   = -224350,
        Z                   = 20,
        Y                   = -16180,
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
        X                   = -184980,
        Z                   = 0,
        Y                   = -81290,
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
        X                   = -186100,
        Z                   = 40,
        Y                   = -22120,
        Direction           = 213,
        Unknown2            = 14,
        Unknown3            = 917504,
        ChipIndex           = 0x0,
        NpcIndex            = 0x185,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -160000,
        Z                   = 200,
        Y                   = -2000,
        Unknown_0C          = 0,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x79,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -161000,
        Z                   = 0,
        Y                   = -21000,
        Unknown_0C          = 0,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x7A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -155000,
        Z                   = 0,
        Y                   = -44000,
        Unknown_0C          = 0,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x7B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -178000,
        Z                   = 500,
        Y                   = -29000,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x7D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -190000,
        Z                   = 0,
        Y                   = -39000,
        Unknown_0C          = 0,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x7C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -205000,
        Z                   = 200,
        Y                   = -55000,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x7E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -193000,
        Z                   = 200,
        Y                   = -2000,
        Unknown_0C          = 0,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x79,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -207000,
        Z                   = 200,
        Y                   = -6000,
        Unknown_0C          = 0,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x7B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -198000,
        Z                   = 300,
        Y                   = -47000,
        Unknown_0C          = 0,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x7A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -180000,
        Z                   = -500,
        Y                   = -58000,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x7D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -159000,
        Z                   = 200,
        Y                   = -59000,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x7E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -180000,
        Z                   = 0,
        Y                   = -5000,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x7C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -172000,
        Z                   = 200,
        Y                   = -43000,
        Unknown_0C          = 0,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x79,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -186100,
        Y                   = -1040,
        Z                   = -22120,
        Range               = 2000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 4,
    )


    DeclActor(
        TriggerX            = -176080,
        TriggerZ            = 50,
        TriggerY            = 11940,
        TriggerRange        = 1000,
        ActorX              = -176140,
        ActorZ              = 1050,
        ActorY              = 12680,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -211720,
        TriggerZ            = 20,
        TriggerY            = -56010,
        TriggerRange        = 1000,
        ActorX              = -211660,
        ActorZ              = 20,
        ActorY              = -56570,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -145080,
        TriggerZ            = 40,
        TriggerY            = -50920,
        TriggerRange        = 1000,
        ActorX              = -144640,
        ActorZ              = 40,
        ActorY              = -51360,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -179550,
        TriggerZ            = 0,
        TriggerY            = -15360,
        TriggerRange        = 1500,
        ActorX              = -179550,
        ActorZ              = 1500,
        ActorY              = -15360,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 41,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_586",          # 00, 0
        "Function_1_5CA",          # 01, 1
        "Function_2_7EB",          # 02, 2
        "Function_3_801",          # 03, 3
        "Function_4_899",          # 04, 4
        "Function_5_A54",          # 05, 5
        "Function_6_B6B",          # 06, 6
        "Function_7_C82",          # 07, 7
        "Function_8_D99",          # 08, 8
        "Function_9_1377",         # 09, 9
        "Function_10_1772",        # 0A, 10
        "Function_11_1C02",        # 0B, 11
        "Function_12_2705",        # 0C, 12
        "Function_13_2735",        # 0D, 13
        "Function_14_2765",        # 0E, 14
        "Function_15_2795",        # 0F, 15
        "Function_16_27C5",        # 10, 16
        "Function_17_27E1",        # 11, 17
        "Function_18_2811",        # 12, 18
        "Function_19_2841",        # 13, 19
        "Function_20_2871",        # 14, 20
        "Function_21_28A1",        # 15, 21
        "Function_22_28D1",        # 16, 22
        "Function_23_2901",        # 17, 23
        "Function_24_291D",        # 18, 24
        "Function_25_2939",        # 19, 25
        "Function_26_2A0D",        # 1A, 26
        "Function_27_2A27",        # 1B, 27
        "Function_28_2A41",        # 1C, 28
        "Function_29_2A5B",        # 1D, 29
        "Function_30_2A75",        # 1E, 30
        "Function_31_2A8F",        # 1F, 31
        "Function_32_2ABD",        # 20, 32
        "Function_33_2AEB",        # 21, 33
        "Function_34_2B19",        # 22, 34
        "Function_35_2B47",        # 23, 35
        "Function_36_2B75",        # 24, 36
        "Function_37_2BA3",        # 25, 37
        "Function_38_2BD1",        # 26, 38
        "Function_39_2BFF",        # 27, 39
        "Function_40_2C9B",        # 28, 40
        "Function_41_2CED",        # 29, 41
    )


    def Function_0_586(): pass

    label("Function_0_586")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5A0")
    Event(0, 10)
    Jump("loc_5B6")

    label("loc_5A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5B2")
    Event(0, 9)
    Jump("loc_5B6")

    label("loc_5B2")

    Event(0, 8)

    label("loc_5B6")

    Jump("loc_5C9")

    label("loc_5B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5C9")
    Event(0, 11)

    label("loc_5C9")

    Return()

    # Function_0_586 end

    def Function_1_5CA(): pass

    label("Function_1_5CA")

    OP_16(0x2, 0xFA0, 0xFFFB54B0, 0xFFFD8730, 0x23000C)
    OP_4F(0x3A, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x324, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F7")
    OP_6F(0x0, 0)
    Jump("loc_5FE")

    label("loc_5F7")

    OP_6F(0x0, 60)

    label("loc_5FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x324, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_610")
    OP_6F(0x1, 0)
    Jump("loc_617")

    label("loc_610")

    OP_6F(0x1, 60)

    label("loc_617")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x324, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_629")
    OP_6F(0x2, 0)
    Jump("loc_630")

    label("loc_629")

    OP_6F(0x2, 60)

    label("loc_630")

    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    OP_82(0x82, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_720")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_66A")
    SetMapFlags(0x10)
    OP_11(0xE6, 0xF0, 0xFF, 0x0, 0xEA60, 0x0)
    OP_C4(0x0, 0x4)
    Jump("loc_720")

    label("loc_66A")

    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_11(0xE6, 0xF0, 0xFF, 0x0, 0x13880, 0x0)
    OP_43(0x15, 0x0, 0x0, 0x3)

    label("loc_720")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_73E")
    SetChrFlags(0x19, 0x80)
    OP_B2(0x0, 0x0, 0x80)
    Jump("loc_750")

    label("loc_73E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31F, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_750")
    ClearChrFlags(0x19, 0x80)
    OP_B2(0x1, 0x0, 0x80)

    label("loc_750")

    OP_51(0x19, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1A, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1B, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1C, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1D, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1E, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1F, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x20, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x21, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x22, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x23, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x24, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x25, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x26, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_5CA end

    def Function_2_7EB(): pass

    label("Function_2_7EB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_800")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_7EB")

    label("loc_800")

    Return()

    # Function_2_7EB end

    def Function_3_801(): pass

    label("Function_3_801")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_898")
    OP_4F(0x37, (scpexpr(EXPR_PUSH_LONG, 0x22AB0), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x65), scpexpr(EXPR_SUB), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x37), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_835")
    OP_4F(0x37, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_84A")

    label("loc_835")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x37), scpexpr(EXPR_PUSH_LONG, 0x7D00), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_84A")
    OP_4F(0x37, (scpexpr(EXPR_PUSH_LONG, 0x7D00), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_84A")

    OP_4F(0x38, (scpexpr(EXPR_PUSH_LONG, 0x22AB0), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x65), scpexpr(EXPR_SUB), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMUL), scpexpr(EXPR_PUSH_LONG, 0x13880), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x38), scpexpr(EXPR_PUSH_LONG, 0x13880), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_87B")
    OP_4F(0x38, (scpexpr(EXPR_PUSH_LONG, 0x13880), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_890")

    label("loc_87B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x38), scpexpr(EXPR_PUSH_LONG, 0x222E0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_890")
    OP_4F(0x38, (scpexpr(EXPR_PUSH_LONG, 0x222E0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_890")

    Sleep(10)
    Jump("Function_3_801")

    label("loc_898")

    Return()

    # Function_3_801 end

    def Function_4_899(): pass

    label("Function_4_899")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31F, 5)), scpexpr(EXPR_END)), "loc_8A1")
    Return()

    label("loc_8A1")

    EventBegin(0x1)
    OP_51(0x0, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x3, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x4, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x5, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x6, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x7, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    SetChrSubChip(0x4, 0)
    SetChrSubChip(0x5, 0)
    SetChrSubChip(0x6, 0)
    SetChrSubChip(0x7, 0)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05大型魔兽正在四处游荡中。\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        0,
        (
            "【消灭它】\x01",      # 0
            "【放弃】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_986"),
        (SWITCH_DEFAULT, "loc_9A9"),
    )


    label("loc_986")

    Fade(500)
    OP_89(0x0, -191670, 190, -27970, 45)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    OP_0D()
    EventEnd(0x0)
    Return()

    label("loc_9A9")

    Battle(0xEEB, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x1)
    OP_89(0x0, -191670, 190, -27970, 45)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_9E2"),
        (1, "loc_9E5"),
        (SWITCH_DEFAULT, "loc_9E8"),
    )


    label("loc_9E2")

    EventEnd(0x0)
    Return()

    label("loc_9E5")

    OP_B4(0x0)
    Return()

    label("loc_9E8")

    EventBegin(0x1)
    SetChrFlags(0x19, 0x80)
    OP_B2(0x0, 0x0, 0x80)
    OP_0D()
    Sleep(400)
    OP_22(0x17, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        "\x07\x05消灭了通缉魔兽！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A2(0x18FD)
    OP_28(0xAF, 0x4, 0x10)
    OP_28(0xAF, 0x4, 0x2)
    OP_28(0xAF, 0x1, 0x1)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x0)
    Return()

    # Function_4_899 end

    def Function_5_A54(): pass

    label("Function_5_A54")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x324, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B2C")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0xA7, 1)"), scpexpr(EXPR_END)), "loc_AC3")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x00得到了\x1F\xA7\x00\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1922)
    Jump("loc_B29")

    label("loc_AC3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #3
        (
            "宝箱里装有\x1F\xA7\x00\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xA7\x00\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_B29")

    Jump("loc_B5D")

    label("loc_B2C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_B5D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_A54 end

    def Function_6_B6B(): pass

    label("Function_6_B6B")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x324, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C43")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x200, 1)"), scpexpr(EXPR_END)), "loc_BDA")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x00得到了\x1F\x00\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1923)
    Jump("loc_C40")

    label("loc_BDA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #6
        (
            "宝箱里装有\x1F\x00\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x00\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_C40")

    Jump("loc_C74")

    label("loc_C43")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_C74")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_B6B end

    def Function_7_C82(): pass

    label("Function_7_C82")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x324, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D5A")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_CF1")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x00得到了\x1F\xF6\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1924)
    Jump("loc_D57")

    label("loc_CF1")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #9
        (
            "宝箱里装有\x1F\xF6\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xF6\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_D57")

    Jump("loc_D8B")

    label("loc_D5A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_D8B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_C82 end

    def Function_8_D99(): pass

    label("Function_8_D99")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DC3")
    Call(0, 39)
    FadeToBright(0, 0)
    Call(0, 40)

    label("loc_DC3")

    OP_6D(-140320, 20, -17700, 0)
    OP_67(0, 6530, -10000, 0)
    OP_6B(3180, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -134560, 0, -17700, 270)
    SetChrPos(0x103, -134560, 0, -18700, 270)
    SetChrPos(0xF8, -133560, 0, -17450, 270)
    SetChrPos(0xF9, -133560, 0, -18950, 270)

    def lambda_E4A():
        OP_90(0xFE, 0xFFFFE4A8, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E4A)
    Sleep(100)

    def lambda_E6A():
        OP_90(0xFE, 0xFFFFE4A8, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_E6A)
    Sleep(200)

    def lambda_E8A():
        OP_90(0xFE, 0xFFFFE69C, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_E8A)
    Sleep(100)

    def lambda_EAA():
        OP_90(0xFE, 0xFFFFE69C, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_EAA)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0xF9, 0x1)

    ChrTalk(    #11
        0x101,
        "#1004F#6P啊……\x02",
    )

    CloseMessageWindow()

    def lambda_EE9():
        OP_8E(0xFE, 0xFFFDBF98, 0x0, 0xFFFFBADC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_EE9)
    Sleep(100)

    def lambda_F09():
        OP_8E(0xFE, 0xFFFDBF66, 0x0, 0xFFFFB65E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F09)
    Sleep(200)

    def lambda_F29():
        OP_8E(0xFE, 0xFFFDC6B4, 0x0, 0xFFFFBC44, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_F29)
    Sleep(100)

    def lambda_F49():
        OP_8E(0xFE, 0xFFFDC632, 0x0, 0xFFFFB744, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_F49)

    def lambda_F64():
        OP_6D(-146390, 0, -17590, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F64)

    def lambda_F7C():
        OP_6B(3500, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_F7C)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x103, 0x1)
    WaitChrThread(0xF8, 0x1)
    WaitChrThread(0xF9, 0x1)
    OP_8C(0x101, 295, 400)
    Sleep(50)
    OP_8C(0x103, 270, 400)
    Sleep(30)
    OP_8C(0xF8, 270, 400)
    Sleep(50)
    OP_8C(0xF9, 240, 400)
    Sleep(400)
    OP_8C(0x101, 270, 400)
    Sleep(50)
    OP_8C(0x103, 295, 400)
    Sleep(30)
    OP_8C(0xF8, 240, 400)
    Sleep(50)
    OP_8C(0xF9, 270, 400)
    Sleep(400)
    OP_8C(0x101, 240, 400)
    Sleep(50)
    OP_8C(0x103, 240, 400)
    Sleep(30)
    OP_8C(0xF8, 270, 400)
    Sleep(50)
    OP_8C(0xF9, 295, 400)
    Sleep(400)
    OP_8C(0x101, 270, 400)
    Sleep(50)
    OP_8C(0x103, 295, 400)
    Sleep(30)
    OP_8C(0xF8, 295, 400)
    Sleep(50)
    OP_8C(0xF9, 240, 400)
    Sleep(400)
    OP_8C(0x101, 90, 400)
    Sleep(50)
    OP_8C(0x103, 90, 400)
    Sleep(30)
    OP_8C(0xF8, 270, 400)
    Sleep(50)
    OP_8C(0xF9, 270, 400)
    Sleep(400)
    WaitChrThread(0x101, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10C3")

    ChrTalk(    #12
        0x107,
        (
            "#560F哇……\x01",
            "一下子就明朗了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_118C")

    label("loc_10C3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10F5")

    ChrTalk(    #13
        0x106,
        (
            "#051F嘿……\x01",
            "突然就明朗了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_118C")

    label("loc_10F5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1129")

    ChrTalk(    #14
        0x104,
        (
            "#030F嗯……\x01",
            "一下子就明朗了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_118C")

    label("loc_1129")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_115D")

    ChrTalk(    #15
        0x105,
        (
            "#048F呵呵……\x01",
            "忽然就明朗了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_118C")

    label("loc_115D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_118C")

    ChrTalk(    #16
        0x108,
        (
            "#070F呼……\x01",
            "突然就明朗了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_118C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11C8")

    ChrTalk(    #17
        0x107,
        (
            "#061F雾的覆盖范围\x01",
            "似乎就到这里为止呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12B5")

    label("loc_11C8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1204")

    ChrTalk(    #18
        0x106,
        (
            "#051F雾的覆盖范围\x01",
            "似乎就到这里为止啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12B5")

    label("loc_1204")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1240")

    ChrTalk(    #19
        0x104,
        (
            "#030F雾的覆盖范围\x01",
            "似乎就到这里为止啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12B5")

    label("loc_1240")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_127C")

    ChrTalk(    #20
        0x105,
        (
            "#048F雾的覆盖范围\x01",
            "似乎就到这里为止呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12B5")

    label("loc_127C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12B5")

    ChrTalk(    #21
        0x108,
        (
            "#070F雾的覆盖范围\x01",
            "似乎就到这里为止啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12B5")


    ChrTalk(    #22
        0x103,
        (
            "#026F米尔西街道，从洛连特出发\x01",
            "大约８０塞尔矩的地点……\x02\x03",

            "#022F浓雾中有魔兽在游荡，\x01",
            "情况相当危险呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        (
            "#1015F#6P嗯，是啊。\x02\x03",

            "调查完其它地方后，\x01",
            "必须赶快向爱娜姐报告才行。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x180F)
    OP_28(0x8F, 0x2, 0x10)
    OP_28(0x8F, 0x1, 0x20)
    EventEnd(0x0)
    Return()

    # Function_8_D99 end

    def Function_9_1377(): pass

    label("Function_9_1377")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13A1")
    Call(0, 39)
    FadeToBright(0, 0)
    Call(0, 40)

    label("loc_13A1")

    OP_6D(-140320, 20, -17700, 0)
    OP_67(0, 6530, -10000, 0)
    OP_6B(3180, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -137560, 0, -17700, 270)
    SetChrPos(0x103, -137560, 0, -18700, 270)
    SetChrPos(0xF8, -136560, 0, -17450, 270)
    SetChrPos(0xF9, -136560, 0, -18950, 270)

    def lambda_1428():
        OP_8E(0xFE, 0xFFFDBF98, 0x0, 0xFFFFBADC, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1428)
    Sleep(100)

    def lambda_1448():
        OP_8E(0xFE, 0xFFFDBF66, 0x0, 0xFFFFB65E, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1448)
    Sleep(200)

    def lambda_1468():
        OP_8E(0xFE, 0xFFFDC6B4, 0x0, 0xFFFFBC44, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_1468)
    Sleep(100)

    def lambda_1488():
        OP_8E(0xFE, 0xFFFDC632, 0x0, 0xFFFFB744, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_1488)

    def lambda_14A3():
        OP_6D(-146390, 0, -17590, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_14A3)

    def lambda_14BB():
        OP_6B(3500, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_14BB)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0xF9, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1504")

    ChrTalk(    #24
        0x107,
        "#061F嘿嘿，已经晴了⊙\x02",
    )

    CloseMessageWindow()
    Jump("loc_15BB")

    label("loc_1504")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_152F")

    ChrTalk(    #25
        0x106,
        "#051F嘿，已经晴了吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_15BB")

    label("loc_152F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_155E")

    ChrTalk(    #26
        0x104,
        "#030F嗯，好像已经晴了啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_15BB")

    label("loc_155E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_158D")

    ChrTalk(    #27
        0x105,
        "#048F……似乎已经晴了哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_15BB")

    label("loc_158D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15BB")

    ChrTalk(    #28
        0x108,
        "#070F嗯……已经没有雾了吗。\x02",
    )

    CloseMessageWindow()

    label("loc_15BB")


    ChrTalk(    #29
        0x103,
        (
            "#026F米尔西街道，距离洛连特\x01",
            "大约８０塞尔矩的地点……\x02\x03",

            "#022F浓雾中有魔兽在游荡，\x01",
            "情况相当危险呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16BD")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇调查过玛鲁加山道】\x01",      # 0
            "【◇调查过艾利兹街道】\x01",      # 1
            "【◇不变更】\x01",                # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_16AB"),
        (1, "loc_16B4"),
        (SWITCH_DEFAULT, "loc_16BD"),
    )


    label("loc_16AB")

    OP_A3(0x180E)
    OP_A2(0x1810)
    Jump("loc_16BD")

    label("loc_16B4")

    OP_A2(0x180E)
    OP_A3(0x1810)
    Jump("loc_16BD")

    label("loc_16BD")

    TurnDirection(0x101, 0x103, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 0)), scpexpr(EXPR_END)), "loc_1717")

    ChrTalk(    #30
        0x101,
        (
            "#1006F#5P嗯……\x01",
            "就向爱娜姐报告吧。\x02\x03",

            "接下来，只剩下\x01",
            "艾利兹街道了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1760")

    label("loc_1717")


    ChrTalk(    #31
        0x101,
        (
            "#1006F#5P嗯……\x01",
            "就向爱娜姐报告吧。\x02\x03",

            "接下来，只剩下\x01",
            "玛鲁加山道了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1760")

    OP_A2(0x180F)
    OP_28(0x8F, 0x2, 0x10)
    OP_28(0x8F, 0x1, 0x20)
    EventEnd(0x0)
    Return()

    # Function_9_1377 end

    def Function_10_1772(): pass

    label("Function_10_1772")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_179C")
    Call(0, 39)
    FadeToBright(0, 0)
    Call(0, 40)

    label("loc_179C")

    OP_6D(-140320, 20, -17700, 0)
    OP_67(0, 6530, -10000, 0)
    OP_6B(3180, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -137560, 0, -17700, 270)
    SetChrPos(0x103, -137560, 0, -18700, 270)
    SetChrPos(0xF8, -136560, 0, -17450, 270)
    SetChrPos(0xF9, -136560, 0, -18950, 270)

    def lambda_1823():
        OP_8E(0xFE, 0xFFFDBF98, 0x0, 0xFFFFBADC, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1823)
    Sleep(100)

    def lambda_1843():
        OP_8E(0xFE, 0xFFFDBF66, 0x0, 0xFFFFB65E, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1843)
    Sleep(200)

    def lambda_1863():
        OP_8E(0xFE, 0xFFFDC6B4, 0x0, 0xFFFFBC44, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_1863)
    Sleep(100)

    def lambda_1883():
        OP_8E(0xFE, 0xFFFDC632, 0x0, 0xFFFFB744, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_1883)

    def lambda_189E():
        OP_6D(-146390, 0, -17590, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_189E)

    def lambda_18B6():
        OP_6B(3500, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_18B6)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0xF9, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18FF")

    ChrTalk(    #32
        0x107,
        "#061F嘿嘿，已经晴了⊙\x02",
    )

    CloseMessageWindow()
    Jump("loc_19B6")

    label("loc_18FF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_192A")

    ChrTalk(    #33
        0x106,
        "#051F嘿，已经晴了吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_19B6")

    label("loc_192A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1959")

    ChrTalk(    #34
        0x104,
        "#030F嗯，好像已经晴了啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_19B6")

    label("loc_1959")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1988")

    ChrTalk(    #35
        0x105,
        "#048F……似乎已经晴了哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_19B6")

    label("loc_1988")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19B6")

    ChrTalk(    #36
        0x108,
        "#070F嗯……已经没有雾了吗。\x02",
    )

    CloseMessageWindow()

    label("loc_19B6")


    ChrTalk(    #37
        0x103,
        (
            "#026F米尔西街道，从洛连特出发\x01",
            "大约８０塞尔矩的地点……\x02\x03",

            "#022F浓雾中有魔兽在游荡，\x01",
            "情况相当危险呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x101,
        (
            "#1015F#5P是啊。\x02\x03",

            "这样的话，三个地方\x01",
            "都调查过了…\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #39
        0x101,
        (
            "#1006F#5P我们应该回协会\x01",
            "向爱娜姐报告了吧？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B1B")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇没去过布莱特家】\x01",      # 0
            "【◇去过布莱特家】\x01",        # 1
            "【◇不变更】\x01",              # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1B0F"),
        (1, "loc_1B15"),
        (SWITCH_DEFAULT, "loc_1B1B"),
    )


    label("loc_1B0F")

    OP_A3(0x180D)
    Jump("loc_1B1B")

    label("loc_1B15")

    OP_A2(0x180D)
    Jump("loc_1B1B")

    label("loc_1B1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BC1")
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #40
        0x103,
        (
            "#023F那样也好……\x02\x03",

            "不过，好像还没\x01",
            "回家看看呢吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x101,
        (
            "#1004F#5P啊……都给忘了。\x02\x03",

            "#1008F回协会报告之前\x01",
            "先回去看一下吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x8F, 0x2, 0x10)
    OP_28(0x8F, 0x1, 0x20)
    OP_28(0x8F, 0x1, 0x800)
    OP_28(0x8F, 0x1, 0x1000)
    Jump("loc_1BFC")

    label("loc_1BC1")

    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #42
        0x103,
        (
            "#021F哎哎。\x01",
            "那样也好。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x8F, 0x2, 0x10)
    OP_28(0x8F, 0x1, 0x20)
    OP_28(0x8F, 0x1, 0x200)
    OP_28(0x8F, 0x1, 0x400)

    label("loc_1BFC")

    OP_A2(0x180F)
    EventEnd(0x0)
    Return()

    # Function_10_1772 end

    def Function_11_1C02(): pass

    label("Function_11_1C02")

    EventBegin(0x0)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x26, 0x80)
    SetChrPos(0x101, -141380, 0, -19300, 270)
    SetChrPos(0x103, -141280, 0, -17970, 270)
    SetChrPos(0x107, -139730, 50, -17680, 270)
    SetChrPos(0x105, -139950, 20, -19100, 270)
    OP_6D(-142040, 0, -19080, 0)
    OP_67(0, 7030, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(224000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #43
        0x101,
        "#1004F#5P啊……！\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x8, -159130, 0, -15030, 135)
    SetChrPos(0x9, -161380, 10, -15080, 135)
    SetChrPos(0xA, -159660, 20, -13430, 135)
    SetChrPos(0xB, -162790, -10, -14750, 90)
    SetChrPos(0xC, -161600, -10, -12770, 90)
    SetChrPos(0xD, -164800, 10, -14940, 90)
    SetChrPos(0xE, -164010, -10, -12600, 90)
    SetChrPos(0xF, -166820, 0, -15120, 90)
    SetChrPos(0x10, -165800, 20, -12760, 90)
    SetChrPos(0x11, -168710, 0, -15170, 90)
    SetChrPos(0x12, -167690, 0, -12810, 90)
    SetChrPos(0x13, -171010, -20, -15140, 90)
    SetChrPos(0x14, -170070, 0, -12990, 90)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)

    def lambda_1E0B():
        OP_6D(-161370, 10, -15120, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1E0B)

    def lambda_1E23():
        OP_67(0, 9470, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1E23)
    Sleep(1200)
    OP_43(0x8, 0x0, 0x0, 0xC)
    Sleep(300)
    OP_43(0x9, 0x0, 0x0, 0xD)
    OP_43(0xA, 0x0, 0x0, 0xE)
    OP_43(0xB, 0x0, 0x0, 0xF)
    OP_43(0xC, 0x0, 0x0, 0x10)
    OP_43(0xD, 0x0, 0x0, 0x11)
    OP_43(0xE, 0x0, 0x0, 0x12)
    OP_43(0xF, 0x0, 0x0, 0x13)
    OP_43(0x10, 0x0, 0x0, 0x14)
    OP_43(0x11, 0x0, 0x0, 0x15)
    OP_43(0x12, 0x0, 0x0, 0x16)
    OP_43(0x13, 0x0, 0x0, 0x17)
    OP_43(0x14, 0x0, 0x0, 0x18)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    def lambda_1EAF():
        OP_6D(-153200, 0, -18030, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1EAF)
    WaitChrThread(0x8, 0x0)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #44
        0x8,
        "#5P呀呀……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 270, 400)
    Sleep(500)

    ChrTalk(    #45
        0x8,
        "#6P……各位，停止前进。\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x101, -143870, 0, -17360, 270)
    SetChrPos(0x103, -143760, 0, -16219, 270)
    SetChrPos(0x107, -142530, 0, -16120, 270)
    SetChrPos(0x105, -142450, 0, -17250, 270)

    def lambda_1F4F():
        OP_8E(0xFE, 0xFFFDAE4A, 0x0, 0xFFFFB988, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1F4F)
    Sleep(100)

    def lambda_1F6F():
        OP_8E(0xFE, 0xFFFDAE9A, 0x0, 0xFFFFBED8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1F6F)
    Sleep(100)

    def lambda_1F8F():
        OP_8E(0xFE, 0xFFFDB3AE, 0x0, 0xFFFFBA28, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1F8F)
    Sleep(100)

    def lambda_1FAF():
        OP_8E(0xFE, 0xFFFDB3E0, 0x0, 0xFFFFBF78, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1FAF)
    OP_8C(0x8, 90, 400)
    WaitChrThread(0x107, 0x1)
    WaitChrThread(0x101, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_206B")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇没有和阿斯顿再会过】\x01",      # 0
            "【◇和阿斯顿再会过】\x01",          # 1
            "【◇不变更】\x01",                  # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_205F"),
        (1, "loc_2065"),
        (SWITCH_DEFAULT, "loc_206B"),
    )


    label("loc_205F")

    OP_A3(0x1887)
    Jump("loc_206B")

    label("loc_2065")

    OP_A2(0x1887)
    Jump("loc_206B")

    label("loc_206B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x310, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20F8")

    ChrTalk(    #46
        0x101,
        "#1011F#6P阿斯顿先生，好久不见啦！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x8,
        (
            "#5P好久不见了，艾丝蒂尔。\x01",
            "连雪拉扎德也在一起啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x8,
        "#5P难道是正在处理协会的工作吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2166")

    label("loc_20F8")


    ChrTalk(    #49
        0x101,
        "#1011F#6P……阿斯顿先生！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x8,
        (
            "#5P艾丝蒂尔。\x01",
            "连雪拉扎德也在一起啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x8,
        "#5P难道是正在处理协会的工作吗？\x02",
    )

    CloseMessageWindow()

    label("loc_2166")


    ChrTalk(    #52
        0x101,
        (
            "#1025F#6P嗯，是啊……\x02\x03",

            "莫非要前往洛连特\x01",
            "进行警备的部队是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x8,
        "#5P嗯！就是我们！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x8,
        (
            "#5P我们和哈肯大门的增援\x01",
            "要一起前去守卫洛连特市。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x101,
        "#1017F#6P是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x103,
        "#021F那真是帮大忙了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x8,
        (
            "#5P哪里，保护市民\x01",
            "也是王国军的义务啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x8,
        "#5P洛连特的情况怎么样？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x101,
        (
            "#1015F#6P嗯，雾还是很浓，\x01",
            "不过昨天的昏睡事件……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #60
        0x101,
        "#1020F#6P啊，那个，阿斯顿先生！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x8,
        "#5P……啊，你是想说鲁克吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x8,
        (
            "#5P他只是睡着了而已，\x01",
            "并没有生命危险。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x8,
        "#5P不用那么担心！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        "#1026F#6P可、可是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x8,
        (
            "#5P我们现在的当务之急是\x01",
            "去执行自己的责任和义务，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x8,
        (
            "#5P也只有那样才能让\x01",
            "鲁克他们早日清醒吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x101,
        "#1025F#6P阿斯顿先生……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x103,
        (
            "#026F嗯，说的没错。\x02\x03",

            "#020F阿斯顿队长，\x01",
            "城镇那边就拜托您了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x8,
        "#5P没问题，交给我就好了。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 270, 400)
    Sleep(500)

    ChrTalk(    #70
        0x8,
        "#6P马上就到洛连特了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x8,
        (
            "#6P到达之后\x01",
            "马上进入警备状态！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrName("士兵们")
    SetMessageWindowPos(350, 80, -1, -1)

    AnonymousTalk(    #72
        "\x07\x00#4S是！长官！！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_8C(0x8, 90, 400)
    Sleep(200)
    OP_43(0x101, 0x3, 0x0, 0x19)
    WaitChrThread(0x101, 0x3)
    OP_43(0x8, 0x0, 0x0, 0x1A)

    def lambda_24FE():
        OP_6D(-147740, 0, -17850, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_24FE)
    OP_43(0x9, 0x0, 0x0, 0x1B)
    OP_43(0xA, 0x0, 0x0, 0x1C)
    OP_43(0xB, 0x0, 0x0, 0x1D)
    OP_43(0xC, 0x0, 0x0, 0x1E)
    OP_43(0xD, 0x0, 0x0, 0x1F)
    OP_43(0xE, 0x0, 0x0, 0x20)
    OP_43(0xF, 0x0, 0x0, 0x21)
    OP_43(0x10, 0x0, 0x0, 0x22)
    OP_43(0x11, 0x0, 0x0, 0x23)
    OP_43(0x12, 0x0, 0x0, 0x24)
    OP_43(0x13, 0x0, 0x0, 0x25)
    OP_43(0x14, 0x0, 0x0, 0x26)
    WaitChrThread(0x14, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0x103, 0x1)
    OP_44(0x107, 0x1)
    OP_44(0x105, 0x1)

    def lambda_257F():
        OP_6D(-150960, 10, -15560, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_257F)
    Sleep(1000)

    def lambda_259C():
        OP_8C(0x101, 45, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_259C)
    Sleep(50)

    def lambda_25AF():
        OP_8C(0x105, 270, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_25AF)
    Sleep(50)

    def lambda_25C2():
        OP_8C(0x103, 180, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_25C2)
    Sleep(50)
    OP_8C(0x107, 215, 400)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #73
        0x107,
        (
            "#063F刚才那位队长\x01",
            "难道就是那昏睡的男孩的…？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x101,
        (
            "#1007F嗯……他就是鲁克的父亲。\x02\x03",

            "#1003F他心里肯定\x01",
            "很担心的，可是…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x105,
        "#043F#6P真是个……坚强的人啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x103,
        (
            "#026F是啊……\x01",
            "所以我们也要加油才行。\x02\x03",

            "#020F马上去帕赛尔农场吧！\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    OP_A2(0x181F)
    OP_28(0x91, 0x1, 0x2)
    EventEnd(0x0)
    Return()

    # Function_11_1C02 end

    def Function_12_2705(): pass

    label("Function_12_2705")

    OP_8E(0xFE, 0xFFFD9F0E, 0x0, 0xFFFFBB90, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFDA86E, 0x0, 0xFFFFBA8C, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_12_2705 end

    def Function_13_2735(): pass

    label("Function_13_2735")

    OP_8E(0xFE, 0xFFFD9680, 0x0, 0xFFFFB87A, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFDA0C6, 0xFFFFFFF6, 0xFFFFB7D0, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_13_2735 end

    def Function_14_2765(): pass

    label("Function_14_2765")

    OP_8E(0xFE, 0xFFFD9C0C, 0x0, 0xFFFFBF6E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFDA1E8, 0x0, 0xFFFFBE92, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_14_2765 end

    def Function_15_2795(): pass

    label("Function_15_2795")

    OP_8E(0xFE, 0xFFFD94F0, 0x0, 0xFFFFB816, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFD9978, 0xFFFFFFF6, 0xFFFFB780, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_15_2795 end

    def Function_16_27C5(): pass

    label("Function_16_27C5")

    OP_8E(0xFE, 0xFFFD9B6C, 0x0, 0xFFFFBF28, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_16_27C5 end

    def Function_17_27E1(): pass

    label("Function_17_27E1")

    OP_8E(0xFE, 0xFFFD867C, 0xFFFFFFF6, 0xFFFFC6F8, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFD93A6, 0x0, 0xFFFFBA6E, 0x7D0, 0x0)
    OP_8C(0xFE, 135, 400)
    Return()

    # Function_17_27E1 end

    def Function_18_2811(): pass

    label("Function_18_2811")

    OP_8E(0xFE, 0xFFFD8A82, 0x14, 0xFFFFCD7E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFD963A, 0x0, 0xFFFFC220, 0x7D0, 0x0)
    OP_8C(0xFE, 135, 400)
    Return()

    # Function_18_2811 end

    def Function_19_2841(): pass

    label("Function_19_2841")

    OP_8E(0xFE, 0xFFFD867C, 0xFFFFFFF6, 0xFFFFC6F8, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFD8EE2, 0x0, 0xFFFFBE9C, 0x7D0, 0x0)
    OP_8C(0xFE, 135, 400)
    Return()

    # Function_19_2841 end

    def Function_20_2871(): pass

    label("Function_20_2871")

    OP_8E(0xFE, 0xFFFD8A82, 0x14, 0xFFFFCD7E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFD9248, 0x0, 0xFFFFC626, 0x7D0, 0x0)
    OP_8C(0xFE, 135, 400)
    Return()

    # Function_20_2871 end

    def Function_21_28A1(): pass

    label("Function_21_28A1")

    OP_8E(0xFE, 0xFFFD867C, 0xFFFFFFF6, 0xFFFFC6F8, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFD8B04, 0x0, 0xFFFFC248, 0x7D0, 0x0)
    OP_8C(0xFE, 135, 400)
    Return()

    # Function_21_28A1 end

    def Function_22_28D1(): pass

    label("Function_22_28D1")

    OP_8E(0xFE, 0xFFFD8A82, 0x14, 0xFFFFCD7E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFD8EB0, 0x14, 0xFFFFCA72, 0x7D0, 0x0)
    OP_8C(0xFE, 135, 400)
    Return()

    # Function_22_28D1 end

    def Function_23_2901(): pass

    label("Function_23_2901")

    OP_8E(0xFE, 0xFFFD864A, 0xFFFFFFF6, 0xFFFFC6DA, 0x7D0, 0x0)
    OP_8C(0xFE, 135, 400)
    Return()

    # Function_23_2901 end

    def Function_24_291D(): pass

    label("Function_24_291D")

    OP_8E(0xFE, 0xFFFD89B0, 0xA, 0xFFFFCE6E, 0x7D0, 0x0)
    OP_8C(0xFE, 135, 400)
    Return()

    # Function_24_291D end

    def Function_25_2939(): pass

    label("Function_25_2939")


    def lambda_293F():
        OP_8E(0xFE, 0xFFFDB138, 0x28, 0xFFFFC6E4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_293F)
    Sleep(50)

    def lambda_295F():
        OP_8E(0xFE, 0xFFFDB674, 0x14, 0xFFFFC75C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_295F)
    Sleep(200)

    def lambda_297F():
        OP_8E(0xFE, 0xFFFDB156, 0xA, 0xFFFFC2B6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_297F)
    Sleep(50)

    def lambda_299F():
        OP_8E(0xFE, 0xFFFDB674, 0xA, 0xFFFFC31A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_299F)
    WaitChrThread(0x103, 0x1)

    def lambda_29BF():

        label("loc_29BF")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_29BF")

    QueueWorkItem2(0x103, 1, lambda_29BF)
    WaitChrThread(0x107, 0x1)

    def lambda_29D5():

        label("loc_29D5")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_29D5")

    QueueWorkItem2(0x107, 1, lambda_29D5)
    WaitChrThread(0x101, 0x1)

    def lambda_29EB():

        label("loc_29EB")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_29EB")

    QueueWorkItem2(0x101, 1, lambda_29EB)
    WaitChrThread(0x105, 0x1)

    def lambda_2A01():

        label("loc_2A01")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_2A01")

    QueueWorkItem2(0x105, 1, lambda_2A01)
    Return()

    # Function_25_2939 end

    def Function_26_2A0D(): pass

    label("Function_26_2A0D")

    OP_8E(0xFE, 0xFFFE023C, 0x14, 0xFFFFB8E8, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_26_2A0D end

    def Function_27_2A27(): pass

    label("Function_27_2A27")

    OP_8E(0xFE, 0xFFFDFE04, 0x1E, 0xFFFFB6AE, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_27_2A27 end

    def Function_28_2A41(): pass

    label("Function_28_2A41")

    OP_8E(0xFE, 0xFFFDFF1C, 0x14, 0xFFFFBD2A, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_28_2A41 end

    def Function_29_2A5B(): pass

    label("Function_29_2A5B")

    OP_8E(0xFE, 0xFFFDF828, 0x28, 0xFFFFB730, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_29_2A5B end

    def Function_30_2A75(): pass

    label("Function_30_2A75")

    OP_8E(0xFE, 0xFFFDF90E, 0x14, 0xFFFFBD5C, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_30_2A75 end

    def Function_31_2A8F(): pass

    label("Function_31_2A8F")

    OP_8E(0xFE, 0xFFFD99AA, 0xFFFFFFF6, 0xFFFFB712, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFDF828, 0x28, 0xFFFFB730, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_31_2A8F end

    def Function_32_2ABD(): pass

    label("Function_32_2ABD")

    OP_8E(0xFE, 0xFFFD9A5E, 0x0, 0xFFFFBE6A, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFDF90E, 0x14, 0xFFFFBD5C, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_32_2ABD end

    def Function_33_2AEB(): pass

    label("Function_33_2AEB")

    OP_8E(0xFE, 0xFFFD99AA, 0xFFFFFFF6, 0xFFFFB712, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFDF828, 0x28, 0xFFFFB730, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_33_2AEB end

    def Function_34_2B19(): pass

    label("Function_34_2B19")

    OP_8E(0xFE, 0xFFFD9A5E, 0x0, 0xFFFFBE6A, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFDF90E, 0x14, 0xFFFFBD5C, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_34_2B19 end

    def Function_35_2B47(): pass

    label("Function_35_2B47")

    OP_8E(0xFE, 0xFFFD99AA, 0xFFFFFFF6, 0xFFFFB712, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFDF828, 0x28, 0xFFFFB730, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_35_2B47 end

    def Function_36_2B75(): pass

    label("Function_36_2B75")

    OP_8E(0xFE, 0xFFFD9A5E, 0x0, 0xFFFFBE6A, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFDF90E, 0x14, 0xFFFFBD5C, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_36_2B75 end

    def Function_37_2BA3(): pass

    label("Function_37_2BA3")

    OP_8E(0xFE, 0xFFFD99AA, 0xFFFFFFF6, 0xFFFFB712, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFDF828, 0x28, 0xFFFFB730, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_37_2BA3 end

    def Function_38_2BD1(): pass

    label("Function_38_2BD1")

    OP_8E(0xFE, 0xFFFD9A5E, 0x0, 0xFFFFBE6A, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFDF90E, 0x14, 0xFFFFBD5C, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_38_2BD1 end

    def Function_39_2BFF(): pass

    label("Function_39_2BFF")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    RemoveParty(0x9, 0xFF)
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
        (0, "loc_2C7C"),
        (1, "loc_2C82"),
        (SWITCH_DEFAULT, "loc_2C88"),
    )


    label("loc_2C7C")

    OP_A2(0x1200)
    Jump("loc_2C88")

    label("loc_2C82")

    OP_A2(0x1201)
    Jump("loc_2C88")

    label("loc_2C88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_2C96")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_2C9A")

    label("loc_2C96")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_2C9A")

    Return()

    # Function_39_2BFF end

    def Function_40_2C9B(): pass

    label("Function_40_2C9B")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x5, 0x3, 0x4, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_40_2C9B end

    def Function_41_2CED(): pass

    label("Function_41_2CED")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #77
        "\x07\x05南　帕赛尔农场\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_41_2CED end

    SaveToFile()

Try(main)
