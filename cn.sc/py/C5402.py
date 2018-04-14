from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C5402   ._SN',
        MapName             = 'Other',
        Location            = 'C5402.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60028",
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
        '目标探索者',                           # 9
        '目标探索者',                           # 10
        '哨兵570（蓝）',                        # 11
        '哨兵235（红）',                        # 12
        '哨兵570（蓝）',                        # 13
        '哨兵235（红）',                        # 14
        '据点武装者',                           # 15
        '据点武装者',                           # 16
        '据点武装者',                           # 17
        '目标探索者',                           # 18
        '目标探索者',                           # 19
        '哨兵570（蓝）',                        # 20
        '哨兵235（红）',                        # 21
        '哨兵570（蓝）',                        # 22
        '哨兵235（红）',                        # 23
        '据点武装者',                           # 24
        '据点武装者',                           # 25
        '据点武装者',                           # 26
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
        'ED6_DT27/CH04002 ._CH',             # 00
        'ED6_DT27/CH04004 ._CH',             # 01
        'ED6_DT29/CH12570 ._CH',             # 02
        'ED6_DT29/CH12571 ._CH',             # 03
        'ED6_DT29/CH12350 ._CH',             # 04
        'ED6_DT29/CH12351 ._CH',             # 05
        'ED6_DT29/CH12580 ._CH',             # 06
        'ED6_DT29/CH12581 ._CH',             # 07
        'ED6_DT29/CH12310 ._CH',             # 08
        'ED6_DT29/CH12310 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT27/CH04002P._CP',             # 00
        'ED6_DT27/CH04004P._CP',             # 01
        'ED6_DT29/CH12570P._CP',             # 02
        'ED6_DT29/CH12571P._CP',             # 03
        'ED6_DT29/CH12350P._CP',             # 04
        'ED6_DT29/CH12351P._CP',             # 05
        'ED6_DT29/CH12580P._CP',             # 06
        'ED6_DT29/CH12581P._CP',             # 07
        'ED6_DT29/CH12310P._CP',             # 08
        'ED6_DT29/CH12310P._CP',             # 09
    )

    DeclMonster(
        X                   = 92240,
        Z                   = 0,
        Y                   = 25900,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x428,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -90960,
        Z                   = 0,
        Y                   = -210,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x428,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 40060,
        Z                   = 1000,
        Y                   = -76560,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x424,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 38010,
        Z                   = 1000,
        Y                   = 80150,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x427,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -40030,
        Z                   = 1000,
        Y                   = 79100,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x424,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -40020,
        Z                   = 1000,
        Y                   = -76980,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x427,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -830,
        Z                   = 0,
        Y                   = -16890,
        Unknown_0C          = 0,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x426,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -940,
        Z                   = 0,
        Y                   = 8910,
        Unknown_0C          = 0,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x426,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -1050,
        Z                   = 0,
        Y                   = 23020,
        Unknown_0C          = 0,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x426,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 92240,
        Z                   = 0,
        Y                   = 25900,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x431,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -90960,
        Z                   = 0,
        Y                   = -210,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x431,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 40060,
        Z                   = 1000,
        Y                   = -76560,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x42D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 38010,
        Z                   = 1000,
        Y                   = 80150,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x430,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -40030,
        Z                   = 1000,
        Y                   = 79100,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x42D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -40020,
        Z                   = 1000,
        Y                   = -76980,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x430,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -830,
        Z                   = 0,
        Y                   = -16890,
        Unknown_0C          = 0,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x42F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -940,
        Z                   = 0,
        Y                   = 8910,
        Unknown_0C          = 0,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x42F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -1050,
        Z                   = 0,
        Y                   = 23020,
        Unknown_0C          = 0,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x42F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 110,
        Y                   = -1000,
        Z                   = 82080,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 21,
    )

    DeclEvent(
        X                   = -6460,
        Y                   = 0,
        Z                   = 25940,
        Range               = 5290,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x6E50,
        Unknown_18          = 0x0,
        Unknown_1C          = 13,
    )

    DeclEvent(
        X                   = -6460,
        Y                   = 0,
        Z                   = -28270,
        Range               = 5290,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFF9A2A,
        Unknown_18          = 0x0,
        Unknown_1C          = 14,
    )

    DeclEvent(
        X                   = 89640,
        Y                   = 0,
        Z                   = -6980,
        Range               = 95290,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFFE9D0,
        Unknown_18          = 0x0,
        Unknown_1C          = 15,
    )

    DeclEvent(
        X                   = 89640,
        Y                   = 0,
        Z                   = -8440,
        Range               = 95290,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFFE44E,
        Unknown_18          = 0x0,
        Unknown_1C          = 16,
    )

    DeclEvent(
        X                   = -93460,
        Y                   = 0,
        Z                   = 16000,
        Range               = -87810,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x4682,
        Unknown_18          = 0x0,
        Unknown_1C          = 17,
    )

    DeclEvent(
        X                   = -93460,
        Y                   = 0,
        Z                   = 13990,
        Range               = -87810,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x3DEA,
        Unknown_18          = 0x0,
        Unknown_1C          = 18,
    )

    DeclEvent(
        X                   = -93460,
        Y                   = 0,
        Z                   = -16200,
        Range               = -87810,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFFC75C,
        Unknown_18          = 0x0,
        Unknown_1C          = 19,
    )

    DeclEvent(
        X                   = -93460,
        Y                   = 0,
        Z                   = -16200,
        Range               = -87810,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFFB9B0,
        Unknown_18          = 0x0,
        Unknown_1C          = 20,
    )


    DeclActor(
        TriggerX            = -49300,
        TriggerZ            = 0,
        TriggerY            = 17980,
        TriggerRange        = 1000,
        ActorX              = -49910,
        ActorZ              = 0,
        ActorY              = 18010,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -49300,
        TriggerZ            = 0,
        TriggerY            = 14500,
        TriggerRange        = 1000,
        ActorX              = -49920,
        ActorZ              = 0,
        ActorY              = 14540,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -49300,
        TriggerZ            = 0,
        TriggerY            = 21480,
        TriggerRange        = 1000,
        ActorX              = -49960,
        ActorZ              = 0,
        ActorY              = 21520,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 41020,
        TriggerZ            = 0,
        TriggerY            = -23700,
        TriggerRange        = 1000,
        ActorX              = 41020,
        ActorZ              = 0,
        ActorY              = -23040,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 38540,
        TriggerZ            = 0,
        TriggerY            = -23700,
        TriggerRange        = 1000,
        ActorX              = 38540,
        ActorZ              = 0,
        ActorY              = -23040,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 43460,
        TriggerZ            = 0,
        TriggerY            = -23700,
        TriggerRange        = 1000,
        ActorX              = 43550,
        ActorZ              = 0,
        ActorY              = -23000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -48700,
        TriggerZ            = 0,
        TriggerY            = -27980,
        TriggerRange        = 1000,
        ActorX              = -48040,
        ActorZ              = 0,
        ActorY              = -27980,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 47800,
        TriggerZ            = 0,
        TriggerY            = 23490,
        TriggerRange        = 1000,
        ActorX              = 48450,
        ActorZ              = 0,
        ActorY              = 23510,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 47790,
        TriggerZ            = 0,
        TriggerY            = 19970,
        TriggerRange        = 1000,
        ActorX              = 48410,
        ActorZ              = 0,
        ActorY              = 19980,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 47800,
        TriggerZ            = 0,
        TriggerY            = 16490,
        TriggerRange        = 1000,
        ActorX              = 48460,
        ActorZ              = 0,
        ActorY              = 16460,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 5030,
        TriggerZ            = 0,
        TriggerY            = 76990,
        TriggerRange        = 1000,
        ActorX              = 5030,
        ActorZ              = 1000,
        ActorY              = 76990,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 22,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_59E",          # 00, 0
        "Function_1_59F",          # 01, 1
        "Function_2_782",          # 02, 2
        "Function_3_899",          # 03, 3
        "Function_4_9B0",          # 04, 4
        "Function_5_AC7",          # 05, 5
        "Function_6_BDE",          # 06, 6
        "Function_7_CF5",          # 07, 7
        "Function_8_E0C",          # 08, 8
        "Function_9_F23",          # 09, 9
        "Function_10_103A",        # 0A, 10
        "Function_11_1151",        # 0B, 11
        "Function_12_1268",        # 0C, 12
        "Function_13_14C1",        # 0D, 13
        "Function_14_1923",        # 0E, 14
        "Function_15_1D69",        # 0F, 15
        "Function_16_21B4",        # 10, 16
        "Function_17_25B7",        # 11, 17
        "Function_18_2A02",        # 12, 18
        "Function_19_2DFB",        # 13, 19
        "Function_20_3246",        # 14, 20
        "Function_21_3658",        # 15, 21
        "Function_22_3671",        # 16, 22
    )


    def Function_0_59E(): pass

    label("Function_0_59E")

    Return()

    # Function_0_59E end

    def Function_1_59F(): pass

    label("Function_1_59F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5BD")
    OP_4F(0x3B, (scpexpr(EXPR_PUSH_LONG, 0x227), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x3C, (scpexpr(EXPR_PUSH_LONG, 0x10A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A9, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CF")
    OP_6F(0x1A, 0)
    Jump("loc_5D6")

    label("loc_5CF")

    OP_6F(0x1A, 60)

    label("loc_5D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A9, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E8")
    OP_6F(0x1B, 0)
    Jump("loc_5EF")

    label("loc_5E8")

    OP_6F(0x1B, 60)

    label("loc_5EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A9, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_601")
    OP_6F(0x1C, 0)
    Jump("loc_608")

    label("loc_601")

    OP_6F(0x1C, 60)

    label("loc_608")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61A")
    OP_6F(0x1D, 0)
    Jump("loc_621")

    label("loc_61A")

    OP_6F(0x1D, 60)

    label("loc_621")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A6, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_633")
    OP_6F(0x1E, 0)
    Jump("loc_63A")

    label("loc_633")

    OP_6F(0x1E, 60)

    label("loc_63A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64C")
    OP_6F(0x1F, 0)
    Jump("loc_653")

    label("loc_64C")

    OP_6F(0x1F, 60)

    label("loc_653")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_665")
    OP_6F(0x20, 0)
    Jump("loc_66C")

    label("loc_665")

    OP_6F(0x20, 60)

    label("loc_66C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A9, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67E")
    OP_6F(0x27, 0)
    Jump("loc_685")

    label("loc_67E")

    OP_6F(0x27, 60)

    label("loc_685")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3AA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_697")
    OP_6F(0x28, 0)
    Jump("loc_69E")

    label("loc_697")

    OP_6F(0x28, 60)

    label("loc_69E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3AA, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B0")
    OP_6F(0x29, 0)
    Jump("loc_6B7")

    label("loc_6B0")

    OP_6F(0x29, 60)

    label("loc_6B7")

    OP_51(0xE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_735")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    Jump("loc_762")

    label("loc_735")

    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)

    label("loc_762")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_777")
    OP_10(0x2C, 0x1)
    OP_10(0x23, 0x0)
    Jump("loc_77D")

    label("loc_777")

    OP_10(0x2C, 0x0)
    OP_10(0x23, 0x1)

    label("loc_77D")

    Call(0, 12)
    Return()

    # Function_1_59F end

    def Function_2_782(): pass

    label("Function_2_782")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A9, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_85A")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1A, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x109, 1)"), scpexpr(EXPR_END)), "loc_7F1")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x09\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D4C)
    Jump("loc_857")

    label("loc_7F1")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\x09\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x09\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1A, 60)
    OP_70(0x1A, 0x0)

    label("loc_857")

    Jump("loc_88B")

    label("loc_85A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_88B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_782 end

    def Function_3_899(): pass

    label("Function_3_899")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A9, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_971")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1B, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_908")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\xF6\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D4D)
    Jump("loc_96E")

    label("loc_908")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\xF6\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xF6\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1B, 60)
    OP_70(0x1B, 0x0)

    label("loc_96E")

    Jump("loc_9A2")

    label("loc_971")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_9A2")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_899 end

    def Function_4_9B0(): pass

    label("Function_4_9B0")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A9, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A88")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1C, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F7, 1)"), scpexpr(EXPR_END)), "loc_A1F")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x00得到了\x1F\xF7\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D4E)
    Jump("loc_A85")

    label("loc_A1F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "宝箱里装有\x1F\xF7\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xF7\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1C, 60)
    OP_70(0x1C, 0x0)

    label("loc_A85")

    Jump("loc_AB9")

    label("loc_A88")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_AB9")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_9B0 end

    def Function_5_AC7(): pass

    label("Function_5_AC7")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B9F")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1D, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x159, 1)"), scpexpr(EXPR_END)), "loc_B36")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x00得到了\x1F\x59\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D32)
    Jump("loc_B9C")

    label("loc_B36")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "宝箱里装有\x1F\x59\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x59\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1D, 60)
    OP_70(0x1D, 0x0)

    label("loc_B9C")

    Jump("loc_BD0")

    label("loc_B9F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_BD0")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_AC7 end

    def Function_6_BDE(): pass

    label("Function_6_BDE")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A6, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CB6")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1E, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_C4D")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #12
        "\x07\x00得到了\x1F\xFE\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D33)
    Jump("loc_CB3")

    label("loc_C4D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        (
            "宝箱里装有\x1F\xFE\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFE\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1E, 60)
    OP_70(0x1E, 0x0)

    label("loc_CB3")

    Jump("loc_CE7")

    label("loc_CB6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_CE7")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_BDE end

    def Function_7_CF5(): pass

    label("Function_7_CF5")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DCD")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1F, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_D64")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #15
        "\x07\x00得到了\x1F\xFB\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D34)
    Jump("loc_DCA")

    label("loc_D64")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #16
        (
            "宝箱里装有\x1F\xFB\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFB\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1F, 60)
    OP_70(0x1F, 0x0)

    label("loc_DCA")

    Jump("loc_DFE")

    label("loc_DCD")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #17
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_DFE")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_CF5 end

    def Function_8_E0C(): pass

    label("Function_8_E0C")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EE4")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x20, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x16C, 1)"), scpexpr(EXPR_END)), "loc_E7B")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #18
        "\x07\x00得到了\x1F\x6C\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D35)
    Jump("loc_EE1")

    label("loc_E7B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #19
        (
            "宝箱里装有\x1F\x6C\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x6C\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x20, 60)
    OP_70(0x20, 0x0)

    label("loc_EE1")

    Jump("loc_F15")

    label("loc_EE4")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #20
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_F15")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_E0C end

    def Function_9_F23(): pass

    label("Function_9_F23")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A9, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FFB")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x27, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_F92")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #21
        "\x07\x00得到了\x1F\xFC\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D4F)
    Jump("loc_FF8")

    label("loc_F92")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #22
        (
            "宝箱里装有\x1F\xFC\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFC\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x27, 60)
    OP_70(0x27, 0x0)

    label("loc_FF8")

    Jump("loc_102C")

    label("loc_FFB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #23
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_102C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_F23 end

    def Function_10_103A(): pass

    label("Function_10_103A")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3AA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1112")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x28, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x4C, 1)"), scpexpr(EXPR_END)), "loc_10A9")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #24
        "\x07\x00得到了\x1F\x4C\x00\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D50)
    Jump("loc_110F")

    label("loc_10A9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #25
        (
            "宝箱里装有\x1F\x4C\x00\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x4C\x00\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x28, 60)
    OP_70(0x28, 0x0)

    label("loc_110F")

    Jump("loc_1143")

    label("loc_1112")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #26
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1143")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_103A end

    def Function_11_1151(): pass

    label("Function_11_1151")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3AA, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1229")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x29, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x202, 1)"), scpexpr(EXPR_END)), "loc_11C0")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #27
        "\x07\x00得到了\x1F\x02\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D51)
    Jump("loc_1226")

    label("loc_11C0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #28
        (
            "宝箱里装有\x1F\x02\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x02\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x29, 60)
    OP_70(0x29, 0x0)

    label("loc_1226")

    Jump("loc_125A")

    label("loc_1229")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #29
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_125A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_11_1151 end

    def Function_12_1268(): pass

    label("Function_12_1268")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 2)), scpexpr(EXPR_END)), "loc_1288")
    OP_72(0x0, 0x20)
    OP_72(0x0, 0x8)
    OP_6F(0x0, 0)
    OP_71(0x0, 0x2)
    Jump("loc_12E0")

    label("loc_1288")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 2)), scpexpr(EXPR_END)), "loc_12CA")
    OP_72(0x0, 0x20)
    OP_72(0x0, 0x8)
    OP_6F(0x0, 100)
    OP_72(0x0, 0x2)
    OP_BE(0x0, 0x1, 0x2, 0x64, 0x0, 0x2, -5600, -1000, 24500, 3600, 2000, 27500)
    Jump("loc_12E0")

    label("loc_12CA")

    OP_72(0x0, 0x20)
    OP_72(0x0, 0x8)
    OP_6F(0x0, 0)
    OP_71(0x0, 0x2)

    label("loc_12E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 2)), scpexpr(EXPR_END)), "loc_1300")
    OP_72(0x1, 0x20)
    OP_72(0x1, 0x8)
    OP_6F(0x1, 0)
    OP_71(0x1, 0x2)
    Jump("loc_1358")

    label("loc_1300")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 3)), scpexpr(EXPR_END)), "loc_1342")
    OP_72(0x1, 0x20)
    OP_72(0x1, 0x8)
    OP_6F(0x1, 100)
    OP_72(0x1, 0x2)
    OP_BE(0x1, 0x1, 0x2, 0x64, 0x0, 0x2, -5600, -1000, -27500, 3600, 2000, -24500)
    Jump("loc_1358")

    label("loc_1342")

    OP_72(0x1, 0x20)
    OP_72(0x1, 0x8)
    OP_6F(0x1, 0)
    OP_71(0x1, 0x2)

    label("loc_1358")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 2)), scpexpr(EXPR_END)), "loc_1378")
    OP_72(0x2, 0x20)
    OP_72(0x2, 0x8)
    OP_6F(0x2, 0)
    OP_71(0x2, 0x2)
    Jump("loc_13D0")

    label("loc_1378")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 4)), scpexpr(EXPR_END)), "loc_13BA")
    OP_72(0x2, 0x20)
    OP_72(0x2, 0x8)
    OP_6F(0x2, 100)
    OP_72(0x2, 0x2)
    OP_BE(0x2, 0x1, 0x2, 0x64, 0x0, 0x2, 90400, -1000, -8600, 93600, 2000, -5500)
    Jump("loc_13D0")

    label("loc_13BA")

    OP_72(0x2, 0x20)
    OP_72(0x2, 0x8)
    OP_6F(0x2, 0)
    OP_71(0x2, 0x2)

    label("loc_13D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 2)), scpexpr(EXPR_END)), "loc_13F0")
    OP_72(0x3, 0x20)
    OP_72(0x3, 0x8)
    OP_6F(0x3, 0)
    OP_71(0x3, 0x2)
    Jump("loc_1448")

    label("loc_13F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 5)), scpexpr(EXPR_END)), "loc_1432")
    OP_72(0x3, 0x20)
    OP_72(0x3, 0x8)
    OP_6F(0x3, 100)
    OP_72(0x3, 0x2)
    OP_BE(0x3, 0x1, 0x2, 0x64, 0x0, 0x2, -92500, -1000, 14600, -89600, 2000, 17450)
    Jump("loc_1448")

    label("loc_1432")

    OP_72(0x3, 0x20)
    OP_72(0x3, 0x8)
    OP_6F(0x3, 0)
    OP_71(0x3, 0x2)

    label("loc_1448")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 2)), scpexpr(EXPR_END)), "loc_1468")
    OP_72(0x4, 0x20)
    OP_72(0x4, 0x8)
    OP_6F(0x4, 0)
    OP_71(0x4, 0x2)
    Jump("loc_14C0")

    label("loc_1468")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x392, 2)), scpexpr(EXPR_END)), "loc_14AA")
    OP_72(0x4, 0x20)
    OP_72(0x4, 0x8)
    OP_6F(0x4, 100)
    OP_72(0x4, 0x2)
    OP_BE(0x4, 0x1, 0x2, 0x64, 0x0, 0x2, -92500, -1000, -17400, -89600, 2000, -14650)
    Jump("loc_14C0")

    label("loc_14AA")

    OP_72(0x4, 0x20)
    OP_72(0x4, 0x8)
    OP_6F(0x4, 0)
    OP_71(0x4, 0x2)

    label("loc_14C0")

    Return()

    # Function_12_1268 end

    def Function_13_14C1(): pass

    label("Function_13_14C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_14D0")
    Return()

    label("loc_14D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1550")
    EventBegin(0x0)
    OP_22(0x6B, 0x0, 0x64)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x64)
    OP_72(0x0, 0x2)
    OP_8C(0x0, 180, 400)
    Sleep(300)
    OP_95(0x0, 0x0, 0x0, 0x7D0, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)
    OP_A2(0x1C22)
    OP_BE(0x0, 0x1, 0x2, 0x64, 0x0, 0x2, -5600, -1000, 24500, 3600, 2000, 27500)
    OP_73(0x0)
    EventEnd(0x0)
    Jump("loc_1922")

    label("loc_1550")

    EventBegin(0x0)
    OP_22(0x6B, 0x0, 0x64)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x64)
    OP_72(0x0, 0x2)
    OP_A2(0x1C22)
    OP_BE(0x0, 0x1, 0x2, 0x64, 0x0, 0x2, -5600, -1000, 24500, 3600, 2000, 27500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15EE")
    OP_8C(0x101, 180, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0x7D0, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)

    ChrTalk(    #30
        0x101,
        "#1020F这、这是什么啊！？\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1C1E)
    OP_28(0x99, 0x1, 0x2)
    Jump("loc_191D")

    label("loc_15EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1649")
    OP_8C(0x101, 180, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0x7D0, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)

    ChrTalk(    #31
        0x101,
        "#1005F又、又来了！？\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1C1F)
    OP_28(0x99, 0x1, 0x4)
    Jump("loc_191D")

    label("loc_1649")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16A8")
    OP_8C(0x101, 180, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0x7D0, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)

    ChrTalk(    #32
        0x101,
        "#1019F适、适可而止吧……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1C20)
    OP_28(0x99, 0x1, 0x8)
    Jump("loc_191D")

    label("loc_16A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18F0")
    OP_8C(0x101, 180, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0x7D0, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)
    Fade(1000)
    SetChrPos(0x101, -940, 0, 30200, 180)
    OP_6D(-450, 0, 27630, 0)
    OP_67(0, 9280, -10000, 0)
    OP_6B(3530, 0)
    OP_6C(128000, 0)
    OP_6E(236, 0)
    OP_0D()

    ChrTalk(    #33
        0x101,
        (
            "#1019F………………\x02\x03",

            "#1022F#1022F很好很好。\x01",
            "就是不让我通过吧？\x02\x03",

            "#1005F既然这样的话……\x01",
            "就强行突破了！\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 0)
    Sleep(500)

    def lambda_17AB():
        OP_96(0x101, 0xFFFFFC54, 0x0, 0x6AF4, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_17AB)
    OP_99(0x101, 0x0, 0x7, 0x7D0)
    WaitChrThread(0x101, 0x1)
    OP_22(0xD6, 0x0, 0x64)

    def lambda_17DC():
        OP_69(0x101, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_17DC)

    def lambda_17EA():
        OP_95(0xFE, 0x0, 0x0, 0x7D0, 0x5DC, 0x1388)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_17EA)
    SetChrSubChip(0x101, 3)
    SetChrChipByIndex(0x101, 1)
    WaitChrThread(0x101, 0x2)
    Sleep(1000)
    SetChrSubChip(0x101, 2)
    Sleep(100)

    ChrTalk(    #34
        0x101,
        (
            "#1007F呜呜……\x01",
            "手麻掉了～……\x02\x03",

            "#1013F果然是太勉强了吗……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(500)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #35
        0x101,
        (
            "#1002F没办法……\x01",
            "绕道前进吧！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(1000)
    OP_6D(-940, 0, 29380, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_A2(0x1C21)
    OP_28(0x99, 0x1, 0x10)
    Jump("loc_191D")

    label("loc_18F0")

    OP_8C(0x101, 180, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0x7D0, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)

    label("loc_191D")

    OP_73(0x0)
    EventEnd(0x0)

    label("loc_1922")

    Return()

    # Function_13_14C1 end

    def Function_14_1923(): pass

    label("Function_14_1923")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1932")
    Return()

    label("loc_1932")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_19B2")
    EventBegin(0x0)
    OP_22(0x6B, 0x0, 0x64)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x64)
    OP_72(0x1, 0x2)
    OP_8C(0x0, 0, 400)
    Sleep(300)
    OP_95(0x0, 0x0, 0x0, 0xFFFFF830, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)
    OP_A2(0x1C23)
    OP_BE(0x1, 0x1, 0x2, 0x64, 0x0, 0x2, -5600, -1000, -27500, 3600, 2000, -24500)
    OP_73(0x1)
    EventEnd(0x0)
    Jump("loc_1D68")

    label("loc_19B2")

    EventBegin(0x0)
    OP_22(0x6B, 0x0, 0x64)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x64)
    OP_72(0x1, 0x2)
    OP_A2(0x1C23)
    OP_BE(0x1, 0x1, 0x2, 0x64, 0x0, 0x2, -5600, -1000, -27500, 3600, 2000, -24500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A4A")
    OP_8C(0x101, 0, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0xFFFFF830, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)

    ChrTalk(    #36
        0x101,
        "#1020F这、这是什么啊！？\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1C1E)
    Jump("loc_1D63")

    label("loc_1A4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A9F")
    OP_8C(0x101, 0, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0xFFFFF830, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)

    ChrTalk(    #37
        0x101,
        "#1005F又、又来了！？\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1C1F)
    Jump("loc_1D63")

    label("loc_1A9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AF8")
    OP_8C(0x101, 0, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0xFFFFF830, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)

    ChrTalk(    #38
        0x101,
        "#1019F适、适可而止吧……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1C20)
    Jump("loc_1D63")

    label("loc_1AF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D36")
    OP_8C(0x101, 0, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0xFFFFF830, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)
    Fade(1000)
    SetChrPos(0x101, -980, 0, -30230, 0)
    OP_6D(-980, 0, -30230, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(45000, 0)
    OP_6E(220, 0)
    OP_0D()

    ChrTalk(    #39
        0x101,
        (
            "#1019F………………\x02\x03",

            "#1022F很好很好。\x01",
            "就是不让我们通过吧？\x02\x03",

            "#1005F既然这样的话……\x01",
            "就强行突破了！\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 0)
    Sleep(500)

    def lambda_1BF7():
        OP_96(0x101, 0xFFFFFC2C, 0x0, 0xFFFF93EA, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1BF7)
    OP_99(0x101, 0x0, 0x7, 0x7D0)
    WaitChrThread(0x101, 0x1)
    OP_22(0xD6, 0x0, 0x64)

    def lambda_1C28():
        OP_69(0x101, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1C28)

    def lambda_1C36():
        OP_95(0xFE, 0x0, 0x0, 0xFFFFF830, 0x5DC, 0x1388)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1C36)
    SetChrSubChip(0x101, 3)
    SetChrChipByIndex(0x101, 1)
    WaitChrThread(0x101, 0x2)
    Sleep(1000)
    SetChrSubChip(0x101, 2)
    Sleep(100)

    ChrTalk(    #40
        0x101,
        (
            "#1007F呜呜……\x01",
            "手麻掉了～……\x02\x03",

            "#1013F果然是太勉强了吗……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(500)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #41
        0x101,
        (
            "#1002F没办法……\x01",
            "绕道前进吧！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(1000)
    OP_6D(-980, 0, -29670, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_A2(0x1C21)
    Jump("loc_1D63")

    label("loc_1D36")

    OP_8C(0x101, 0, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0xFFFFF830, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)

    label("loc_1D63")

    OP_73(0x1)
    EventEnd(0x0)

    label("loc_1D68")

    Return()

    # Function_14_1923 end

    def Function_15_1D69(): pass

    label("Function_15_1D69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1D78")
    Return()

    label("loc_1D78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1DF8")
    EventBegin(0x0)
    OP_22(0x6B, 0x0, 0x64)
    OP_6F(0x2, 0)
    OP_70(0x2, 0x64)
    OP_72(0x2, 0x2)
    OP_8C(0x0, 180, 400)
    Sleep(300)
    OP_95(0x0, 0x0, 0x0, 0x7D0, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)
    OP_A2(0x1C24)
    OP_BE(0x2, 0x1, 0x2, 0x64, 0x0, 0x2, 90400, -1000, -8600, 93600, 2000, -5500)
    OP_73(0x2)
    EventEnd(0x0)
    Jump("loc_21B3")

    label("loc_1DF8")

    EventBegin(0x0)
    OP_22(0x6B, 0x0, 0x64)
    OP_6F(0x2, 0)
    OP_70(0x2, 0x64)
    OP_72(0x2, 0x2)
    OP_A2(0x1C24)
    OP_BE(0x2, 0x1, 0x2, 0x64, 0x0, 0x2, 90400, -1000, -8600, 93600, 2000, -5500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E90")
    OP_8C(0x101, 180, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0x7D0, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)

    ChrTalk(    #42
        0x101,
        "#1020F这、这是什么啊！？\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1C1E)
    Jump("loc_21AE")

    label("loc_1E90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EE5")
    OP_8C(0x101, 180, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0x7D0, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)

    ChrTalk(    #43
        0x101,
        "#1005F又、又来了！？\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1C1F)
    Jump("loc_21AE")

    label("loc_1EE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F3E")
    OP_8C(0x101, 180, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0x7D0, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)

    ChrTalk(    #44
        0x101,
        "#1019F适、适可而止吧……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1C20)
    Jump("loc_21AE")

    label("loc_1F3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2181")
    OP_8C(0x101, 180, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0x7D0, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)
    Fade(1000)
    SetChrPos(0x101, 92040, 0, -3780, 180)
    OP_6D(91880, 0, -4860, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(51000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(    #45
        0x101,
        (
            "#1019F………………\x02\x03",

            "#1022F很好很好。\x01",
            "就是不让我们通过吧？\x02\x03",

            "#1005F既然这样的话……\x01",
            "就强行突破了！\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 0)
    Sleep(500)

    def lambda_2042():
        OP_96(0x101, 0x16788, 0x0, 0xFFFFE9A8, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2042)
    OP_99(0x101, 0x0, 0x7, 0x7D0)
    WaitChrThread(0x101, 0x1)
    OP_22(0xD6, 0x0, 0x64)

    def lambda_2073():
        OP_69(0x101, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2073)

    def lambda_2081():
        OP_95(0xFE, 0x0, 0x0, 0x7D0, 0x5DC, 0x1388)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2081)
    SetChrSubChip(0x101, 3)
    SetChrChipByIndex(0x101, 1)
    WaitChrThread(0x101, 0x2)
    Sleep(1000)
    SetChrSubChip(0x101, 2)
    Sleep(100)

    ChrTalk(    #46
        0x101,
        (
            "#1007F呜呜……\x01",
            "手麻掉了～……\x02\x03",

            "#1013F果是是太勉强了吗……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(500)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #47
        0x101,
        (
            "#1002F没办法……\x01",
            "绕道前进吧！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(1000)
    OP_6D(92040, 0, -3720, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_A2(0x1C21)
    Jump("loc_21AE")

    label("loc_2181")

    OP_8C(0x101, 180, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0x7D0, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)

    label("loc_21AE")

    OP_73(0x2)
    EventEnd(0x0)

    label("loc_21B3")

    Return()

    # Function_15_1D69 end

    def Function_16_21B4(): pass

    label("Function_16_21B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_21C3")
    Return()

    label("loc_21C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2243")
    EventBegin(0x0)
    OP_22(0x6B, 0x0, 0x64)
    OP_6F(0x2, 0)
    OP_70(0x2, 0x64)
    OP_72(0x2, 0x2)
    OP_8C(0x0, 0, 400)
    Sleep(300)
    OP_95(0x0, 0x0, 0x0, 0xFFFFF830, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)
    OP_A2(0x1C24)
    OP_BE(0x2, 0x1, 0x2, 0x64, 0x0, 0x2, 90400, -1000, -8600, 93600, 2000, -5500)
    OP_73(0x2)
    EventEnd(0x0)
    Jump("loc_25B6")

    label("loc_2243")

    EventBegin(0x0)
    OP_22(0x6B, 0x0, 0x64)
    OP_6F(0x2, 0)
    OP_70(0x2, 0x64)
    OP_72(0x2, 0x2)
    OP_A2(0x1C24)
    OP_BE(0x2, 0x1, 0x2, 0x64, 0x0, 0x2, 90400, -1000, -8600, 93600, 2000, -5500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22DB")
    OP_8C(0x101, 0, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0xFFFFF830, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)

    ChrTalk(    #48
        0x101,
        "#1020F这、这是什么啊！？\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1C1E)
    Jump("loc_25B1")

    label("loc_22DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2330")
    OP_8C(0x101, 0, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0xFFFFF830, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)

    ChrTalk(    #49
        0x101,
        "#1005F又、又来了！？\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1C1F)
    Jump("loc_25B1")

    label("loc_2330")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2389")
    OP_8C(0x101, 0, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0xFFFFF830, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)

    ChrTalk(    #50
        0x101,
        "#1019F适、适可而止吧……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1C20)
    Jump("loc_25B1")

    label("loc_2389")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2584")
    OP_8C(0x101, 0, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0xFFFFF830, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)
    Fade(1000)
    SetChrPos(0x101, 92040, 0, -10450, 0)
    OP_6D(92040, 0, -10450, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(    #51
        0x101,
        (
            "#1019F………………\x02\x03",

            "#1022F很好很好。\x01",
            "就是不让我们通过吧？\x02\x03",

            "#1005F既然这样的话……\x01",
            "就强行突破了！\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 0)
    Sleep(500)

    def lambda_248D():
        OP_96(0x101, 0x16788, 0x0, 0xFFFFDF58, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_248D)
    OP_99(0x101, 0x0, 0x7, 0x7D0)
    WaitChrThread(0x101, 0x1)
    OP_22(0xD6, 0x0, 0x64)

    def lambda_24BE():
        OP_69(0x101, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_24BE)

    def lambda_24CC():
        OP_95(0xFE, 0x0, 0x0, 0xFFFFF830, 0x5DC, 0x1388)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_24CC)
    SetChrSubChip(0x101, 3)
    SetChrChipByIndex(0x101, 1)
    WaitChrThread(0x101, 0x2)
    Sleep(1000)
    SetChrSubChip(0x101, 2)
    Sleep(100)

    ChrTalk(    #52
        0x101,
        (
            "#1007F呜呜……\x01",
            "手麻掉了～……\x02\x03",

            "#1013F果然是太勉强了吗……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(500)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #53
        0x101,
        (
            "#1002F没办法……\x01",
            "绕道前进吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1C21)
    Jump("loc_25B1")

    label("loc_2584")

    OP_8C(0x101, 0, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0xFFFFF830, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)

    label("loc_25B1")

    OP_73(0x2)
    EventEnd(0x0)

    label("loc_25B6")

    Return()

    # Function_16_21B4 end

    def Function_17_25B7(): pass

    label("Function_17_25B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_25C6")
    Return()

    label("loc_25C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2646")
    EventBegin(0x0)
    OP_22(0x6B, 0x0, 0x64)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x64)
    OP_72(0x3, 0x2)
    OP_8C(0x0, 180, 400)
    Sleep(300)
    OP_95(0x0, 0x0, 0x0, 0x7D0, 0x3E8, 0x1388)
    Sleep(9000)
    OP_22(0x9D, 0x0, 0x64)
    OP_A2(0x1C25)
    OP_BE(0x3, 0x1, 0x2, 0x64, 0x0, 0x2, -92500, -1000, 14600, -89600, 2000, 17450)
    OP_73(0x3)
    EventEnd(0x0)
    Jump("loc_2A01")

    label("loc_2646")

    EventBegin(0x0)
    OP_22(0x6B, 0x0, 0x64)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x64)
    OP_72(0x3, 0x2)
    OP_A2(0x1C25)
    OP_BE(0x3, 0x1, 0x2, 0x64, 0x0, 0x2, -92500, -1000, 14600, -89600, 2000, 17450)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26DE")
    OP_8C(0x101, 180, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0x7D0, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)

    ChrTalk(    #54
        0x101,
        "#1020F这、这是什么啊！？\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1C1E)
    Jump("loc_29FC")

    label("loc_26DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2733")
    OP_8C(0x101, 180, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0x7D0, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)

    ChrTalk(    #55
        0x101,
        "#1005F又、又来了！？\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1C1F)
    Jump("loc_29FC")

    label("loc_2733")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_278C")
    OP_8C(0x101, 180, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0x7D0, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)

    ChrTalk(    #56
        0x101,
        "#1019F适、适可而止吧……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1C20)
    Jump("loc_29FC")

    label("loc_278C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29CF")
    OP_8C(0x101, 180, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0x7D0, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)
    Fade(1000)
    SetChrPos(0x101, -90980, 0, 20100, 180)
    OP_6D(-90920, 0, 17750, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(    #57
        0x101,
        (
            "#1019F………………\x02\x03",

            "#1022F很好很好。\x01",
            "就是不让我们通过吧？\x02\x03",

            "#1005F既然这样的话……\x01",
            "就强行突破了！\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 0)
    Sleep(500)

    def lambda_2890():
        OP_96(0x101, 0xFFFE9C9C, 0x0, 0x442A, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2890)
    OP_99(0x101, 0x0, 0x7, 0x7D0)
    WaitChrThread(0x101, 0x1)
    OP_22(0xD6, 0x0, 0x64)

    def lambda_28C1():
        OP_69(0x101, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_28C1)

    def lambda_28CF():
        OP_95(0xFE, 0x0, 0x0, 0x7D0, 0x5DC, 0x1388)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_28CF)
    SetChrSubChip(0x101, 3)
    SetChrChipByIndex(0x101, 1)
    WaitChrThread(0x101, 0x2)
    Sleep(1000)
    SetChrSubChip(0x101, 2)
    Sleep(100)

    ChrTalk(    #58
        0x101,
        (
            "#1007F呜呜……\x01",
            "手麻掉了～……\x02\x03",

            "#1013F果然是太勉强了吗……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(500)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #59
        0x101,
        (
            "#1002F没办法……\x01",
            "绕道前进吧！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(1000)
    OP_6D(-90980, 0, 19450, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_A2(0x1C21)
    Jump("loc_29FC")

    label("loc_29CF")

    OP_8C(0x101, 180, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0x7D0, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)

    label("loc_29FC")

    OP_73(0x3)
    EventEnd(0x0)

    label("loc_2A01")

    Return()

    # Function_17_25B7 end

    def Function_18_2A02(): pass

    label("Function_18_2A02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2A11")
    Return()

    label("loc_2A11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2A91")
    EventBegin(0x0)
    OP_22(0x6B, 0x0, 0x64)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x64)
    OP_72(0x3, 0x2)
    OP_8C(0x0, 0, 400)
    Sleep(300)
    OP_95(0x0, 0x0, 0x0, 0xFFFFF830, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)
    OP_A2(0x1C25)
    OP_BE(0x3, 0x1, 0x2, 0x64, 0x0, 0x2, -92500, -1000, 14600, -89600, 2000, 17450)
    OP_73(0x3)
    EventEnd(0x0)
    Jump("loc_2DFA")

    label("loc_2A91")

    EventBegin(0x0)
    OP_22(0x6B, 0x0, 0x64)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x64)
    OP_72(0x3, 0x2)
    OP_A2(0x1C25)
    OP_BE(0x3, 0x1, 0x2, 0x64, 0x0, 0x2, -92500, -1000, 14600, -89600, 2000, 17450)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B29")
    OP_8C(0x101, 0, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0xFFFFF830, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)

    ChrTalk(    #60
        0x101,
        "#1020F这、这是什么啊！？\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1C1E)
    Jump("loc_2DF5")

    label("loc_2B29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B7E")
    OP_8C(0x101, 0, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0xFFFFF830, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)

    ChrTalk(    #61
        0x101,
        "#1005F又、又来了！？\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1C1F)
    Jump("loc_2DF5")

    label("loc_2B7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BD7")
    OP_8C(0x101, 0, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0xFFFFF830, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)

    ChrTalk(    #62
        0x101,
        "#1019F适、适可而止吧……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1C20)
    Jump("loc_2DF5")

    label("loc_2BD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DC8")
    OP_8C(0x101, 0, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0xFFFFF830, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)
    Fade(1000)
    SetChrPos(0x101, -91000, 0, 12100, 0)
    OP_6D(-91000, 0, 12100, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(    #63
        0x101,
        (
            "#1019F………………\x02\x03",

            "#1022F很好很好。\x01",
            "就是不让我们通过吧？\x02\x03",

            "#1005F既然这样的话……\x01",
            "就强行突破了！\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 0)
    Sleep(500)

    def lambda_2CDB():
        OP_96(0x101, 0xFFFE9C88, 0x0, 0x3818, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2CDB)
    OP_99(0x101, 0x0, 0x7, 0x7D0)
    WaitChrThread(0x101, 0x1)
    OP_22(0xD6, 0x0, 0x64)

    def lambda_2D0C():
        OP_69(0x101, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2D0C)

    def lambda_2D1A():
        OP_95(0xFE, 0x0, 0x0, 0xFFFFF830, 0x5DC, 0x1388)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2D1A)
    SetChrSubChip(0x101, 3)
    SetChrChipByIndex(0x101, 1)
    WaitChrThread(0x101, 0x2)
    Sleep(1000)

    ChrTalk(    #64
        0x101,
        (
            "#1007F呜呜……\x01",
            "手麻掉了～……\x02\x03",

            "#1013F果然是太勉强了吗……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(500)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #65
        0x101,
        (
            "#1002F没办法……\x01",
            "绕道前进吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1C21)
    Jump("loc_2DF5")

    label("loc_2DC8")

    OP_8C(0x101, 0, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0xFFFFF830, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)

    label("loc_2DF5")

    OP_73(0x3)
    EventEnd(0x0)

    label("loc_2DFA")

    Return()

    # Function_18_2A02 end

    def Function_19_2DFB(): pass

    label("Function_19_2DFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x392, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2E0A")
    Return()

    label("loc_2E0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x392, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E8A")
    EventBegin(0x0)
    OP_22(0x6B, 0x0, 0x64)
    OP_6F(0x4, 0)
    OP_70(0x4, 0x64)
    OP_72(0x4, 0x2)
    OP_8C(0x0, 180, 400)
    Sleep(300)
    OP_95(0x0, 0x0, 0x0, 0x7D0, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)
    OP_A2(0x1C92)
    OP_BE(0x4, 0x1, 0x2, 0x64, 0x0, 0x2, -92500, -1000, -17400, -89600, 2000, -14650)
    OP_73(0x4)
    EventEnd(0x0)
    Jump("loc_3245")

    label("loc_2E8A")

    EventBegin(0x0)
    OP_22(0x6B, 0x0, 0x64)
    OP_6F(0x4, 0)
    OP_70(0x4, 0x64)
    OP_72(0x4, 0x2)
    OP_A2(0x1C92)
    OP_BE(0x4, 0x1, 0x2, 0x64, 0x0, 0x2, -92500, -1000, -17400, -89600, 2000, -14650)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F22")
    OP_8C(0x101, 180, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0x7D0, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)

    ChrTalk(    #66
        0x101,
        "#1020F这、这是什么啊！？\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1C1E)
    Jump("loc_3240")

    label("loc_2F22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F77")
    OP_8C(0x101, 180, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0x7D0, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)

    ChrTalk(    #67
        0x101,
        "#1005F又、又来了！？\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1C1F)
    Jump("loc_3240")

    label("loc_2F77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FD0")
    OP_8C(0x101, 180, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0x7D0, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)

    ChrTalk(    #68
        0x101,
        "#1019F适、适可而止吧……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1C20)
    Jump("loc_3240")

    label("loc_2FD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3213")
    OP_8C(0x101, 180, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0x7D0, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)
    Fade(1000)
    SetChrPos(0x101, -91140, 0, -12020, 180)
    OP_6D(-90820, 0, -13710, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(    #69
        0x101,
        (
            "#1019F………………\x02\x03",

            "#1022F很好很好。\x01",
            "就是不让我们通过吧？\x02\x03",

            "#1005F既然这样的话……\x01",
            "就强行突破了！\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 0)
    Sleep(500)

    def lambda_30D4():
        OP_96(0x101, 0xFFFE9C88, 0x0, 0xFFFFC770, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_30D4)
    OP_99(0x101, 0x0, 0x7, 0x7D0)
    WaitChrThread(0x101, 0x1)
    OP_22(0xD6, 0x0, 0x64)

    def lambda_3105():
        OP_69(0x101, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3105)

    def lambda_3113():
        OP_95(0xFE, 0x0, 0x0, 0x7D0, 0x5DC, 0x1388)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3113)
    SetChrSubChip(0x101, 3)
    SetChrChipByIndex(0x101, 1)
    WaitChrThread(0x101, 0x2)
    Sleep(1000)
    SetChrSubChip(0x101, 2)
    Sleep(100)

    ChrTalk(    #70
        0x101,
        (
            "#1007F呜呜……\x01",
            "手麻掉了～……\x02\x03",

            "#1013F果然是太勉强了吗……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(500)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #71
        0x101,
        (
            "#1002F没办法……\x01",
            "绕道前进吧！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(1000)
    OP_6D(-91000, 0, -12480, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_A2(0x1C21)
    Jump("loc_3240")

    label("loc_3213")

    OP_8C(0x101, 180, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0x7D0, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)

    label("loc_3240")

    OP_73(0x4)
    EventEnd(0x0)

    label("loc_3245")

    Return()

    # Function_19_2DFB end

    def Function_20_3246(): pass

    label("Function_20_3246")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x392, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3255")
    Return()

    label("loc_3255")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x392, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_32D5")
    EventBegin(0x0)
    OP_22(0x6B, 0x0, 0x64)
    OP_6F(0x4, 0)
    OP_70(0x4, 0x64)
    OP_72(0x4, 0x2)
    OP_8C(0x0, 0, 400)
    Sleep(300)
    OP_95(0x0, 0x0, 0x0, 0xFFFFF830, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)
    OP_A2(0x1C92)
    OP_BE(0x4, 0x1, 0x2, 0x64, 0x0, 0x2, -92500, -1000, -17400, -89600, 2000, -14650)
    OP_73(0x4)
    EventEnd(0x0)
    Jump("loc_3657")

    label("loc_32D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x392, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_32E4")
    Return()

    label("loc_32E4")

    EventBegin(0x0)
    OP_22(0x6B, 0x0, 0x64)
    OP_6F(0x4, 0)
    OP_70(0x4, 0x64)
    OP_72(0x4, 0x2)
    OP_A2(0x1C92)
    OP_BE(0x4, 0x1, 0x2, 0x64, 0x0, 0x2, -92500, -1000, -17400, -89600, 2000, -14650)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_337C")
    OP_8C(0x101, 0, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0xFFFFF830, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)

    ChrTalk(    #72
        0x101,
        "#1020F这、这是什么啊！？\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1C1E)
    Jump("loc_3652")

    label("loc_337C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33D1")
    OP_8C(0x101, 0, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0xFFFFF830, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)

    ChrTalk(    #73
        0x101,
        "#1005F又、又来了！？\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1C1F)
    Jump("loc_3652")

    label("loc_33D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_342A")
    OP_8C(0x101, 0, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0xFFFFF830, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)

    ChrTalk(    #74
        0x101,
        "#1019F适、适可而止吧……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1C20)
    Jump("loc_3652")

    label("loc_342A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3625")
    OP_8C(0x101, 0, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0xFFFFF830, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)
    Fade(1000)
    SetChrPos(0x101, -91080, 0, -19830, 0)
    OP_6D(-91000, 0, -17270, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(    #75
        0x101,
        (
            "#1019F………………\x02\x03",

            "#1022F很好很好。\x01",
            "就是不让我们通过吧？\x02\x03",

            "#1005F既然这样的话……\x01",
            "就强行突破了！\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 0)
    Sleep(500)

    def lambda_352E():
        OP_96(0x101, 0xFFFE9BCA, 0x0, 0xFFFFBC30, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_352E)
    OP_99(0x101, 0x0, 0x7, 0x7D0)
    WaitChrThread(0x101, 0x1)
    OP_22(0xD6, 0x0, 0x64)

    def lambda_355F():
        OP_69(0x101, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_355F)

    def lambda_356D():
        OP_95(0xFE, 0x0, 0x0, 0xFFFFF830, 0x5DC, 0x1388)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_356D)
    SetChrSubChip(0x101, 3)
    SetChrChipByIndex(0x101, 1)
    WaitChrThread(0x101, 0x2)
    Sleep(1000)
    SetChrSubChip(0x101, 2)
    Sleep(100)

    ChrTalk(    #76
        0x101,
        (
            "#1007F呜呜……\x01",
            "手麻掉了～……\x02\x03",

            "#1013F果然是太勉强了吗……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(500)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #77
        0x101,
        (
            "#1002F没办法……\x01",
            "绕道前进吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1C21)
    Jump("loc_3652")

    label("loc_3625")

    OP_8C(0x101, 0, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0xFFFFF830, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)

    label("loc_3652")

    OP_73(0x4)
    EventEnd(0x0)

    label("loc_3657")

    Return()

    # Function_20_3246 end

    def Function_21_3658(): pass

    label("Function_21_3658")

    OP_A2(0x1C81)
    OP_A3(0x1C82)
    OP_A3(0x1C83)
    OP_A3(0x1C84)
    OP_A3(0x1C85)
    OP_A3(0x1C86)
    OP_A3(0x1C87)
    OP_A3(0x1C88)
    Return()

    # Function_21_3658 end

    def Function_22_3671(): pass

    label("Function_22_3671")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_AD(0x24012E, 0x0, 0x0, 0x1F4)
    Sleep(500)
    OP_56(0x3)
    OP_AE(0x1F4)
    TalkEnd(0xFF)
    Return()

    # Function_22_3671 end

    SaveToFile()

Try(main)
