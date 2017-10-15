from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        'ポートシーカー',                       # 9
        'ポートシーカー',                       # 10
        'ヴォーグル570（青）',                  # 11
        'ヴォーグル235（赤）',                  # 12
        'ヴォーグル570（青）',                  # 13
        'ヴォーグル235（赤）',                  # 14
        'レオールガンイージ',                   # 15
        'レオールガンイージ',                   # 16
        'レオールガンイージ',                   # 17
        'ポートシーカー',                       # 18
        'ポートシーカー',                       # 19
        'ヴォーグル570（青）',                  # 20
        'ヴォーグル235（赤）',                  # 21
        'ヴォーグル570（青）',                  # 22
        'ヴォーグル235（赤）',                  # 23
        'レオールガンイージ',                   # 24
        'レオールガンイージ',                   # 25
        'レオールガンイージ',                   # 26
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
        "Function_3_8A9",          # 03, 3
        "Function_4_A0B",          # 04, 4
        "Function_5_B3C",          # 05, 5
        "Function_6_C92",          # 06, 6
        "Function_7_DC7",          # 07, 7
        "Function_8_F34",          # 08, 8
        "Function_9_10AE",         # 09, 9
        "Function_10_11C3",        # 0A, 10
        "Function_11_12F8",        # 0B, 11
        "Function_12_144F",        # 0C, 12
        "Function_13_16A8",        # 0D, 13
        "Function_14_1B7C",        # 0E, 14
        "Function_15_203B",        # 0F, 15
        "Function_16_24F6",        # 10, 16
        "Function_17_2972",        # 11, 17
        "Function_18_2E33",        # 12, 18
        "Function_19_32A5",        # 13, 19
        "Function_20_3769",        # 14, 20
        "Function_21_3BF4",        # 15, 21
        "Function_22_3C0D",        # 16, 22
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

    OP_EA(0x2, 0x59, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A9, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_85A")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1A, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x109, 1)"), scpexpr(EXPR_END)), "loc_7F3")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\x09\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D4C)
    Jump("loc_857")

    label("loc_7F3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\x09\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x09\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1A, 60)
    OP_70(0x1A, 0x0)

    label("loc_857")

    Jump("loc_89B")

    label("loc_85A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05The empty chest's stomach gurgles.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_89B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_782 end

    def Function_3_8A9(): pass

    label("Function_3_8A9")

    OP_EA(0x2, 0x5A, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A9, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_981")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1B, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_91A")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "Found \x1F\xF6\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D4D)
    Jump("loc_97E")

    label("loc_91A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "Found \x1F\xF6\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xF6\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1B, 60)
    OP_70(0x1B, 0x0)

    label("loc_97E")

    Jump("loc_9FD")

    label("loc_981")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x05Every empty chest we open takes a little bit of my\x01",
            "soul with it. Soon, I, too, will be empty.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_9FD")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_8A9 end

    def Function_4_A0B(): pass

    label("Function_4_A0B")

    OP_EA(0x2, 0x5B, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A9, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AE3")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1C, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F7, 1)"), scpexpr(EXPR_END)), "loc_A7C")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "Found \x1F\xF7\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D4E)
    Jump("loc_AE0")

    label("loc_A7C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "Found \x1F\xF7\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xF7\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1C, 60)
    OP_70(0x1C, 0x0)

    label("loc_AE0")

    Jump("loc_B2E")

    label("loc_AE3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05Is this your way of asking me out on a date?\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_B2E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_A0B end

    def Function_5_B3C(): pass

    label("Function_5_B3C")

    OP_EA(0x2, 0x5C, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C14")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1D, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x159, 1)"), scpexpr(EXPR_END)), "loc_BAD")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "Found \x1F\x59\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D32)
    Jump("loc_C11")

    label("loc_BAD")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "Found \x1F\x59\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x59\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1D, 60)
    OP_70(0x1D, 0x0)

    label("loc_C11")

    Jump("loc_C84")

    label("loc_C14")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        (
            "\x07\x05This chest remembers your previous visit and is\x01",
            "none too happy to see you return.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_C84")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_B3C end

    def Function_6_C92(): pass

    label("Function_6_C92")

    OP_EA(0x2, 0x5D, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A6, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D6A")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1E, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_D03")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #12
        "Found \x1F\xFE\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D33)
    Jump("loc_D67")

    label("loc_D03")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        (
            "Found \x1F\xFE\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFE\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1E, 60)
    OP_70(0x1E, 0x0)

    label("loc_D67")

    Jump("loc_DB9")

    label("loc_D6A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        "\x07\x05It's a vase! It's a pot! No... It's Super Chest!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_DB9")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_C92 end

    def Function_7_DC7(): pass

    label("Function_7_DC7")

    OP_EA(0x2, 0x5E, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E9F")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1F, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_E38")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #15
        "Found \x1F\xFB\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D34)
    Jump("loc_E9C")

    label("loc_E38")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #16
        (
            "Found \x1F\xFB\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFB\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1F, 60)
    OP_70(0x1F, 0x0)

    label("loc_E9C")

    Jump("loc_F26")

    label("loc_E9F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #17
        (
            "\x07\x05 As you look into the darkness of the empty\x01",
            "chest, it reminds you of the darkness that fills\x01",
            "your heart.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_F26")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_DC7 end

    def Function_8_F34(): pass

    label("Function_8_F34")

    OP_EA(0x2, 0x5F, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_100C")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x20, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x16C, 1)"), scpexpr(EXPR_END)), "loc_FA5")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #18
        "Found \x1F\x6C\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D35)
    Jump("loc_1009")

    label("loc_FA5")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #19
        (
            "Found \x1F\x6C\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x6C\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x20, 60)
    OP_70(0x20, 0x0)

    label("loc_1009")

    Jump("loc_10A0")

    label("loc_100C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #20
        (
            "\x07\x05There's nothing in this chest, but you looked so\x01",
            "excited to open it that I didn't have the heart to\x01",
            "tell you earlier.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_10A0")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_F34 end

    def Function_9_10AE(): pass

    label("Function_9_10AE")

    OP_EA(0x2, 0x60, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A9, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1186")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x27, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_111F")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #21
        "Found \x1F\xFC\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D4F)
    Jump("loc_1183")

    label("loc_111F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #22
        (
            "Found \x1F\xFC\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFC\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x27, 60)
    OP_70(0x27, 0x0)

    label("loc_1183")

    Jump("loc_11B5")

    label("loc_1186")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #23
        "\x07\x05TO BE CONTINUED.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_11B5")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_10AE end

    def Function_10_11C3(): pass

    label("Function_10_11C3")

    OP_EA(0x2, 0x61, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3AA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_129B")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x28, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x4C, 1)"), scpexpr(EXPR_END)), "loc_1234")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #24
        "Found \x1F\x4C\x00\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D50)
    Jump("loc_1298")

    label("loc_1234")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #25
        (
            "Found \x1F\x4C\x00\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x4C\x00\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x28, 60)
    OP_70(0x28, 0x0)

    label("loc_1298")

    Jump("loc_12EA")

    label("loc_129B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #26
        "\x07\x05Well, I see you're not above asking for seconds.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_12EA")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_11C3 end

    def Function_11_12F8(): pass

    label("Function_11_12F8")

    OP_EA(0x2, 0x62, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3AA, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13D0")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x29, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x202, 1)"), scpexpr(EXPR_END)), "loc_1369")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #27
        "Found \x1F\x02\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D51)
    Jump("loc_13CD")

    label("loc_1369")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #28
        (
            "Found \x1F\x02\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x02\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x29, 60)
    OP_70(0x29, 0x0)

    label("loc_13CD")

    Jump("loc_1441")

    label("loc_13D0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #29
        (
            "\x07\x05This treasure chest graduated at the top of its\x01",
            "class at the Riches Royal Academy.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1441")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_11_12F8 end

    def Function_12_144F(): pass

    label("Function_12_144F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 2)), scpexpr(EXPR_END)), "loc_146F")
    OP_72(0x0, 0x20)
    OP_72(0x0, 0x8)
    OP_6F(0x0, 0)
    OP_71(0x0, 0x2)
    Jump("loc_14C7")

    label("loc_146F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 2)), scpexpr(EXPR_END)), "loc_14B1")
    OP_72(0x0, 0x20)
    OP_72(0x0, 0x8)
    OP_6F(0x0, 100)
    OP_72(0x0, 0x2)
    OP_BE(0x0, 0x1, 0x2, 0x64, 0x0, 0x2, -5600, -1000, 24500, 3600, 2000, 27500)
    Jump("loc_14C7")

    label("loc_14B1")

    OP_72(0x0, 0x20)
    OP_72(0x0, 0x8)
    OP_6F(0x0, 0)
    OP_71(0x0, 0x2)

    label("loc_14C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 2)), scpexpr(EXPR_END)), "loc_14E7")
    OP_72(0x1, 0x20)
    OP_72(0x1, 0x8)
    OP_6F(0x1, 0)
    OP_71(0x1, 0x2)
    Jump("loc_153F")

    label("loc_14E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 3)), scpexpr(EXPR_END)), "loc_1529")
    OP_72(0x1, 0x20)
    OP_72(0x1, 0x8)
    OP_6F(0x1, 100)
    OP_72(0x1, 0x2)
    OP_BE(0x1, 0x1, 0x2, 0x64, 0x0, 0x2, -5600, -1000, -27500, 3600, 2000, -24500)
    Jump("loc_153F")

    label("loc_1529")

    OP_72(0x1, 0x20)
    OP_72(0x1, 0x8)
    OP_6F(0x1, 0)
    OP_71(0x1, 0x2)

    label("loc_153F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 2)), scpexpr(EXPR_END)), "loc_155F")
    OP_72(0x2, 0x20)
    OP_72(0x2, 0x8)
    OP_6F(0x2, 0)
    OP_71(0x2, 0x2)
    Jump("loc_15B7")

    label("loc_155F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 4)), scpexpr(EXPR_END)), "loc_15A1")
    OP_72(0x2, 0x20)
    OP_72(0x2, 0x8)
    OP_6F(0x2, 100)
    OP_72(0x2, 0x2)
    OP_BE(0x2, 0x1, 0x2, 0x64, 0x0, 0x2, 90400, -1000, -8600, 93600, 2000, -5500)
    Jump("loc_15B7")

    label("loc_15A1")

    OP_72(0x2, 0x20)
    OP_72(0x2, 0x8)
    OP_6F(0x2, 0)
    OP_71(0x2, 0x2)

    label("loc_15B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 2)), scpexpr(EXPR_END)), "loc_15D7")
    OP_72(0x3, 0x20)
    OP_72(0x3, 0x8)
    OP_6F(0x3, 0)
    OP_71(0x3, 0x2)
    Jump("loc_162F")

    label("loc_15D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 5)), scpexpr(EXPR_END)), "loc_1619")
    OP_72(0x3, 0x20)
    OP_72(0x3, 0x8)
    OP_6F(0x3, 100)
    OP_72(0x3, 0x2)
    OP_BE(0x3, 0x1, 0x2, 0x64, 0x0, 0x2, -92500, -1000, 14600, -89600, 2000, 17450)
    Jump("loc_162F")

    label("loc_1619")

    OP_72(0x3, 0x20)
    OP_72(0x3, 0x8)
    OP_6F(0x3, 0)
    OP_71(0x3, 0x2)

    label("loc_162F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 2)), scpexpr(EXPR_END)), "loc_164F")
    OP_72(0x4, 0x20)
    OP_72(0x4, 0x8)
    OP_6F(0x4, 0)
    OP_71(0x4, 0x2)
    Jump("loc_16A7")

    label("loc_164F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x392, 2)), scpexpr(EXPR_END)), "loc_1691")
    OP_72(0x4, 0x20)
    OP_72(0x4, 0x8)
    OP_6F(0x4, 100)
    OP_72(0x4, 0x2)
    OP_BE(0x4, 0x1, 0x2, 0x64, 0x0, 0x2, -92500, -1000, -17400, -89600, 2000, -14650)
    Jump("loc_16A7")

    label("loc_1691")

    OP_72(0x4, 0x20)
    OP_72(0x4, 0x8)
    OP_6F(0x4, 0)
    OP_71(0x4, 0x2)

    label("loc_16A7")

    Return()

    # Function_12_144F end

    def Function_13_16A8(): pass

    label("Function_13_16A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_16B7")
    Return()

    label("loc_16B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1737")
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
    Jump("loc_1B7B")

    label("loc_1737")

    EventBegin(0x0)
    OP_22(0x6B, 0x0, 0x64)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x64)
    OP_72(0x0, 0x2)
    OP_A2(0x1C22)
    OP_BE(0x0, 0x1, 0x2, 0x64, 0x0, 0x2, -5600, -1000, 24500, 3600, 2000, 27500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17D4")
    OP_8C(0x101, 180, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0x7D0, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)

    ChrTalk(    #30
        0x101,
        "#1020FWh-What is THIS?!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1C1E)
    OP_28(0x99, 0x1, 0x2)
    Jump("loc_1B76")

    label("loc_17D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1835")
    OP_8C(0x101, 180, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0x7D0, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)

    ChrTalk(    #31
        0x101,
        "#1005FOh, come on! Again?!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1C1F)
    OP_28(0x99, 0x1, 0x4)
    Jump("loc_1B76")

    label("loc_1835")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_189C")
    OP_8C(0x101, 180, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0x7D0, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)

    ChrTalk(    #32
        0x101,
        "#1019FOkay, this is getting old.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1C20)
    OP_28(0x99, 0x1, 0x8)
    Jump("loc_1B76")

    label("loc_189C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B49")
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
            "#1019FWhat?\x02\x03",

            "#1022F...Fine, then.\x01",
            "You don't wanna let me by?\x02\x03",

            "#1005FIn that case, I'll just have to\x01",
            "MAKE MY OWN DOOR!\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 0)
    Sleep(500)

    def lambda_19B0():
        OP_96(0x101, 0xFFFFFC54, 0x0, 0x6AF4, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_19B0)
    OP_99(0x101, 0x0, 0x7, 0x7D0)
    WaitChrThread(0x101, 0x1)
    OP_22(0xD6, 0x0, 0x64)

    def lambda_19E1():
        OP_69(0x101, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_19E1)

    def lambda_19EF():
        OP_95(0xFE, 0x0, 0x0, 0x7D0, 0x5DC, 0x1388)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_19EF)
    SetChrSubChip(0x101, 3)
    SetChrChipByIndex(0x101, 1)
    WaitChrThread(0x101, 0x2)
    Sleep(1000)
    SetChrSubChip(0x101, 2)
    Sleep(100)

    ChrTalk(    #34
        0x101,
        (
            "#5P#1007FWaaaaa...\x01",
            "My arm's all numb...\x02\x03",

            "#1013FSo much for my career as\x01",
            "Estelle the Wall-Crusher, I guess...\x02",
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
            "#5P#1002FGuess I'll just have to try\x01",
            "and find some way around.\x02",
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
    Jump("loc_1B76")

    label("loc_1B49")

    OP_8C(0x101, 180, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0x7D0, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)

    label("loc_1B76")

    OP_73(0x0)
    EventEnd(0x0)

    label("loc_1B7B")

    Return()

    # Function_13_16A8 end

    def Function_14_1B7C(): pass

    label("Function_14_1B7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1B8B")
    Return()

    label("loc_1B8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C0B")
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
    Jump("loc_203A")

    label("loc_1C0B")

    EventBegin(0x0)
    OP_22(0x6B, 0x0, 0x64)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x64)
    OP_72(0x1, 0x2)
    OP_A2(0x1C23)
    OP_BE(0x1, 0x1, 0x2, 0x64, 0x0, 0x2, -5600, -1000, -27500, 3600, 2000, -24500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CA2")
    OP_8C(0x101, 0, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0xFFFFF830, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)

    ChrTalk(    #36
        0x101,
        "#1020FWh-What is THIS?!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1C1E)
    Jump("loc_2035")

    label("loc_1CA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CFD")
    OP_8C(0x101, 0, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0xFFFFF830, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)

    ChrTalk(    #37
        0x101,
        "#1005FOh, come on! Again?!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1C1F)
    Jump("loc_2035")

    label("loc_1CFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D5E")
    OP_8C(0x101, 0, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0xFFFFF830, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)

    ChrTalk(    #38
        0x101,
        "#1019FOkay, this is getting old.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1C20)
    Jump("loc_2035")

    label("loc_1D5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2008")
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
            "#4P#1019FWhat?\x02\x03",

            "#1022F...Fine, then.\x01",
            "You don't wanna let me by?\x02\x03",

            "#1005FIn that case, I'll just have to\x01",
            "MAKE MY OWN DOOR!\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 0)
    Sleep(500)

    def lambda_1E75():
        OP_96(0x101, 0xFFFFFC2C, 0x0, 0xFFFF93EA, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1E75)
    OP_99(0x101, 0x0, 0x7, 0x7D0)
    WaitChrThread(0x101, 0x1)
    OP_22(0xD6, 0x0, 0x64)

    def lambda_1EA6():
        OP_69(0x101, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1EA6)

    def lambda_1EB4():
        OP_95(0xFE, 0x0, 0x0, 0xFFFFF830, 0x5DC, 0x1388)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1EB4)
    SetChrSubChip(0x101, 3)
    SetChrChipByIndex(0x101, 1)
    WaitChrThread(0x101, 0x2)
    Sleep(1000)
    SetChrSubChip(0x101, 2)
    Sleep(100)

    ChrTalk(    #40
        0x101,
        (
            "#2P#1007FWaaaaa...\x01",
            "My arm's all numb...\x02\x03",

            "#1013FSo much for my career as\x01",
            "Estelle the Wall-Crusher, I guess...\x02",
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
            "#2P#1002FGuess I'll just have to try\x01",
            "and find some way around.\x02",
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
    Jump("loc_2035")

    label("loc_2008")

    OP_8C(0x101, 0, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0xFFFFF830, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)

    label("loc_2035")

    OP_73(0x1)
    EventEnd(0x0)

    label("loc_203A")

    Return()

    # Function_14_1B7C end

    def Function_15_203B(): pass

    label("Function_15_203B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_204A")
    Return()

    label("loc_204A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_20CA")
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
    Jump("loc_24F5")

    label("loc_20CA")

    EventBegin(0x0)
    OP_22(0x6B, 0x0, 0x64)
    OP_6F(0x2, 0)
    OP_70(0x2, 0x64)
    OP_72(0x2, 0x2)
    OP_A2(0x1C24)
    OP_BE(0x2, 0x1, 0x2, 0x64, 0x0, 0x2, 90400, -1000, -8600, 93600, 2000, -5500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2161")
    OP_8C(0x101, 180, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0x7D0, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)

    ChrTalk(    #42
        0x101,
        "#1020FWh-What is THIS?!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1C1E)
    Jump("loc_24F0")

    label("loc_2161")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21BC")
    OP_8C(0x101, 180, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0x7D0, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)

    ChrTalk(    #43
        0x101,
        "#1005FOh, come on! Again?!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1C1F)
    Jump("loc_24F0")

    label("loc_21BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_221D")
    OP_8C(0x101, 180, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0x7D0, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)

    ChrTalk(    #44
        0x101,
        "#1019FOkay, this is getting old.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1C20)
    Jump("loc_24F0")

    label("loc_221D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24C3")
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
            "#1019FWhat?\x02\x03",

            "#1022F...Fine, then.\x01",
            "You don't wanna let me by?\x02\x03",

            "#1005FIn that case, I'll just have to\x01",
            "MAKE MY OWN DOOR!\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 0)
    Sleep(500)

    def lambda_2336():
        OP_96(0x101, 0x16788, 0x0, 0xFFFFE9A8, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2336)
    OP_99(0x101, 0x0, 0x7, 0x7D0)
    WaitChrThread(0x101, 0x1)
    OP_22(0xD6, 0x0, 0x64)

    def lambda_2367():
        OP_69(0x101, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2367)

    def lambda_2375():
        OP_95(0xFE, 0x0, 0x0, 0x7D0, 0x5DC, 0x1388)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2375)
    SetChrSubChip(0x101, 3)
    SetChrChipByIndex(0x101, 1)
    WaitChrThread(0x101, 0x2)
    Sleep(1000)
    SetChrSubChip(0x101, 2)
    Sleep(100)

    ChrTalk(    #46
        0x101,
        (
            "#1007FWaaaaa...\x01",
            "My arm's all numb...\x02\x03",

            "#1013FSo much for my career as\x01",
            "Estelle the Wall-Crusher, I guess...\x02",
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
            "#1002FGuess I'll just have to try\x01",
            "and find some way around.\x02",
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
    Jump("loc_24F0")

    label("loc_24C3")

    OP_8C(0x101, 180, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0x7D0, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)

    label("loc_24F0")

    OP_73(0x2)
    EventEnd(0x0)

    label("loc_24F5")

    Return()

    # Function_15_203B end

    def Function_16_24F6(): pass

    label("Function_16_24F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2505")
    Return()

    label("loc_2505")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2585")
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
    Jump("loc_2971")

    label("loc_2585")

    EventBegin(0x0)
    OP_22(0x6B, 0x0, 0x64)
    OP_6F(0x2, 0)
    OP_70(0x2, 0x64)
    OP_72(0x2, 0x2)
    OP_A2(0x1C24)
    OP_BE(0x2, 0x1, 0x2, 0x64, 0x0, 0x2, 90400, -1000, -8600, 93600, 2000, -5500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_261C")
    OP_8C(0x101, 0, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0xFFFFF830, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)

    ChrTalk(    #48
        0x101,
        "#1020FWh-What is THIS?!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1C1E)
    Jump("loc_296C")

    label("loc_261C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2677")
    OP_8C(0x101, 0, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0xFFFFF830, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)

    ChrTalk(    #49
        0x101,
        "#1005FOh, come on! Again?!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1C1F)
    Jump("loc_296C")

    label("loc_2677")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26D8")
    OP_8C(0x101, 0, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0xFFFFF830, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)

    ChrTalk(    #50
        0x101,
        "#1019FOkay, this is getting old.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1C20)
    Jump("loc_296C")

    label("loc_26D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_293F")
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
            "#4P#1019FWhat?\x02\x03",

            "#1022F...Fine, then.\x01",
            "You don't wanna let me by?\x02\x03",

            "#1005FIn that case, I'll just have to\x01",
            "MAKE MY OWN DOOR!\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 0)
    Sleep(500)

    def lambda_27F4():
        OP_96(0x101, 0x16788, 0x0, 0xFFFFDF58, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_27F4)
    OP_99(0x101, 0x0, 0x7, 0x7D0)
    WaitChrThread(0x101, 0x1)
    OP_22(0xD6, 0x0, 0x64)

    def lambda_2825():
        OP_69(0x101, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2825)

    def lambda_2833():
        OP_95(0xFE, 0x0, 0x0, 0xFFFFF830, 0x5DC, 0x1388)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2833)
    SetChrSubChip(0x101, 3)
    SetChrChipByIndex(0x101, 1)
    WaitChrThread(0x101, 0x2)
    Sleep(1000)
    SetChrSubChip(0x101, 2)
    Sleep(100)

    ChrTalk(    #52
        0x101,
        (
            "#2P#1007FWaaaaa...\x01",
            "My arm's all numb...\x02\x03",

            "#1013FSo much for my career as\x01",
            "Estelle the Wall-Crusher, I guess...\x02",
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
            "#2P#1002FGuess I'll just have to try\x01",
            "and find some way around.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1C21)
    Jump("loc_296C")

    label("loc_293F")

    OP_8C(0x101, 0, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0xFFFFF830, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)

    label("loc_296C")

    OP_73(0x2)
    EventEnd(0x0)

    label("loc_2971")

    Return()

    # Function_16_24F6 end

    def Function_17_2972(): pass

    label("Function_17_2972")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2981")
    Return()

    label("loc_2981")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2A01")
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
    Jump("loc_2E32")

    label("loc_2A01")

    EventBegin(0x0)
    OP_22(0x6B, 0x0, 0x64)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x64)
    OP_72(0x3, 0x2)
    OP_A2(0x1C25)
    OP_BE(0x3, 0x1, 0x2, 0x64, 0x0, 0x2, -92500, -1000, 14600, -89600, 2000, 17450)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A98")
    OP_8C(0x101, 180, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0x7D0, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)

    ChrTalk(    #54
        0x101,
        "#1020FWh-What is THIS?!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1C1E)
    Jump("loc_2E2D")

    label("loc_2A98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AF3")
    OP_8C(0x101, 180, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0x7D0, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)

    ChrTalk(    #55
        0x101,
        "#1005FOh, come on! Again?!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1C1F)
    Jump("loc_2E2D")

    label("loc_2AF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B54")
    OP_8C(0x101, 180, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0x7D0, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)

    ChrTalk(    #56
        0x101,
        "#1019FOkay, this is getting old.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1C20)
    Jump("loc_2E2D")

    label("loc_2B54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E00")
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
            "#1019FWhat?\x02\x03",

            "#1022F...Fine, then.\x01",
            "You don't wanna let me by?\x02\x03",

            "#1005FIn that case, I'll just have to\x01",
            "MAKE MY OWN DOOR!\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 0)
    Sleep(500)

    def lambda_2C6D():
        OP_96(0x101, 0xFFFE9C9C, 0x0, 0x442A, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2C6D)
    OP_99(0x101, 0x0, 0x7, 0x7D0)
    WaitChrThread(0x101, 0x1)
    OP_22(0xD6, 0x0, 0x64)

    def lambda_2C9E():
        OP_69(0x101, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2C9E)

    def lambda_2CAC():
        OP_95(0xFE, 0x0, 0x0, 0x7D0, 0x5DC, 0x1388)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2CAC)
    SetChrSubChip(0x101, 3)
    SetChrChipByIndex(0x101, 1)
    WaitChrThread(0x101, 0x2)
    Sleep(1000)
    SetChrSubChip(0x101, 2)
    Sleep(100)

    ChrTalk(    #58
        0x101,
        (
            "#5P#1007FWaaaaa...\x01",
            "My arm's all numb...\x02\x03",

            "#1013FSo much for my career as\x01",
            "Estelle the Wall-Crusher, I guess...\x02",
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
            "#5P#1002FGuess I'll just have to try\x01",
            "and find some way around.\x02",
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
    Jump("loc_2E2D")

    label("loc_2E00")

    OP_8C(0x101, 180, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0x7D0, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)

    label("loc_2E2D")

    OP_73(0x3)
    EventEnd(0x0)

    label("loc_2E32")

    Return()

    # Function_17_2972 end

    def Function_18_2E33(): pass

    label("Function_18_2E33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2E42")
    Return()

    label("loc_2E42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2EC2")
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
    Jump("loc_32A4")

    label("loc_2EC2")

    EventBegin(0x0)
    OP_22(0x6B, 0x0, 0x64)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x64)
    OP_72(0x3, 0x2)
    OP_A2(0x1C25)
    OP_BE(0x3, 0x1, 0x2, 0x64, 0x0, 0x2, -92500, -1000, 14600, -89600, 2000, 17450)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F59")
    OP_8C(0x101, 0, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0xFFFFF830, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)

    ChrTalk(    #60
        0x101,
        "#1020FWh-What is THIS?!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1C1E)
    Jump("loc_329F")

    label("loc_2F59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FB4")
    OP_8C(0x101, 0, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0xFFFFF830, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)

    ChrTalk(    #61
        0x101,
        "#1005FOh, come on! Again?!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1C1F)
    Jump("loc_329F")

    label("loc_2FB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3015")
    OP_8C(0x101, 0, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0xFFFFF830, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)

    ChrTalk(    #62
        0x101,
        "#1019FOkay, this is getting old.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1C20)
    Jump("loc_329F")

    label("loc_3015")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3272")
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
            "#4P#1019FWhat?\x02\x03",

            "#1022F...Fine, then.\x01",
            "You don't wanna let me by?\x02\x03",

            "#1005FIn that case, I'll just have to\x01",
            "MAKE MY OWN DOOR!\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 0)
    Sleep(500)

    def lambda_3131():
        OP_96(0x101, 0xFFFE9C88, 0x0, 0x3818, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3131)
    OP_99(0x101, 0x0, 0x7, 0x7D0)
    WaitChrThread(0x101, 0x1)
    OP_22(0xD6, 0x0, 0x64)

    def lambda_3162():
        OP_69(0x101, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3162)

    def lambda_3170():
        OP_95(0xFE, 0x0, 0x0, 0xFFFFF830, 0x5DC, 0x1388)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3170)
    SetChrSubChip(0x101, 3)
    SetChrChipByIndex(0x101, 1)
    WaitChrThread(0x101, 0x2)
    Sleep(1000)

    ChrTalk(    #64
        0x101,
        (
            "#2P#1007FWaaaaa...\x01",
            "My arm's all numb...\x02\x03",

            "#1013FSo much for my career as\x01",
            "Estelle the Wall-Crusher, I guess...\x02",
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
            "#2P#1002FGuess I'll just have to try\x01",
            "and find some way around.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1C21)
    Jump("loc_329F")

    label("loc_3272")

    OP_8C(0x101, 0, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0xFFFFF830, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)

    label("loc_329F")

    OP_73(0x3)
    EventEnd(0x0)

    label("loc_32A4")

    Return()

    # Function_18_2E33 end

    def Function_19_32A5(): pass

    label("Function_19_32A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x392, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_32B4")
    Return()

    label("loc_32B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x392, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3334")
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
    Jump("loc_3768")

    label("loc_3334")

    EventBegin(0x0)
    OP_22(0x6B, 0x0, 0x64)
    OP_6F(0x4, 0)
    OP_70(0x4, 0x64)
    OP_72(0x4, 0x2)
    OP_A2(0x1C92)
    OP_BE(0x4, 0x1, 0x2, 0x64, 0x0, 0x2, -92500, -1000, -17400, -89600, 2000, -14650)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33CB")
    OP_8C(0x101, 180, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0x7D0, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)

    ChrTalk(    #66
        0x101,
        "#1020FWh-What is THIS?!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1C1E)
    Jump("loc_3763")

    label("loc_33CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3426")
    OP_8C(0x101, 180, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0x7D0, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)

    ChrTalk(    #67
        0x101,
        "#1005FOh, come on! Again?!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1C1F)
    Jump("loc_3763")

    label("loc_3426")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3487")
    OP_8C(0x101, 180, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0x7D0, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)

    ChrTalk(    #68
        0x101,
        "#1019FOkay, this is getting old.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1C20)
    Jump("loc_3763")

    label("loc_3487")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3736")
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
            "#1P#1019FWhat?\x02\x03",

            "#1022F...Fine, then.\x01",
            "You don't wanna let me by?\x02\x03",

            "#1005FIn that case, I'll just have to\x01",
            "MAKE MY OWN DOOR!\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 0)
    Sleep(500)

    def lambda_35A3():
        OP_96(0x101, 0xFFFE9C88, 0x0, 0xFFFFC770, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_35A3)
    OP_99(0x101, 0x0, 0x7, 0x7D0)
    WaitChrThread(0x101, 0x1)
    OP_22(0xD6, 0x0, 0x64)

    def lambda_35D4():
        OP_69(0x101, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_35D4)

    def lambda_35E2():
        OP_95(0xFE, 0x0, 0x0, 0x7D0, 0x5DC, 0x1388)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_35E2)
    SetChrSubChip(0x101, 3)
    SetChrChipByIndex(0x101, 1)
    WaitChrThread(0x101, 0x2)
    Sleep(1000)
    SetChrSubChip(0x101, 2)
    Sleep(100)

    ChrTalk(    #70
        0x101,
        (
            "#1P#1007FWaaaaa...\x01",
            "My arm's all numb...\x02\x03",

            "#1013FSo much for my career as\x01",
            "Estelle the Wall-Crusher, I guess...\x02",
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
            "#1P#1002FGuess I'll just have to try\x01",
            "and find some way around.\x02",
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
    Jump("loc_3763")

    label("loc_3736")

    OP_8C(0x101, 180, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0x7D0, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)

    label("loc_3763")

    OP_73(0x4)
    EventEnd(0x0)

    label("loc_3768")

    Return()

    # Function_19_32A5 end

    def Function_20_3769(): pass

    label("Function_20_3769")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x392, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3778")
    Return()

    label("loc_3778")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x392, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_37F8")
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
    Jump("loc_3BF3")

    label("loc_37F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x392, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3807")
    Return()

    label("loc_3807")

    EventBegin(0x0)
    OP_22(0x6B, 0x0, 0x64)
    OP_6F(0x4, 0)
    OP_70(0x4, 0x64)
    OP_72(0x4, 0x2)
    OP_A2(0x1C92)
    OP_BE(0x4, 0x1, 0x2, 0x64, 0x0, 0x2, -92500, -1000, -17400, -89600, 2000, -14650)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_389E")
    OP_8C(0x101, 0, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0xFFFFF830, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)

    ChrTalk(    #72
        0x101,
        "#1020FWh-What is THIS?!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1C1E)
    Jump("loc_3BEE")

    label("loc_389E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38F9")
    OP_8C(0x101, 0, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0xFFFFF830, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)

    ChrTalk(    #73
        0x101,
        "#1005FOh, come on! Again?!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1C1F)
    Jump("loc_3BEE")

    label("loc_38F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_395A")
    OP_8C(0x101, 0, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0xFFFFF830, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)

    ChrTalk(    #74
        0x101,
        "#1019FOkay, this is getting old.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1C20)
    Jump("loc_3BEE")

    label("loc_395A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BC1")
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
            "#2P#1019FWhat?\x02\x03",

            "#1022F...Fine, then.\x01",
            "You don't wanna let me by?\x02\x03",

            "#1005FIn that case, I'll just have to\x01",
            "MAKE MY OWN DOOR!\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 0)
    Sleep(500)

    def lambda_3A76():
        OP_96(0x101, 0xFFFE9BCA, 0x0, 0xFFFFBC30, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3A76)
    OP_99(0x101, 0x0, 0x7, 0x7D0)
    WaitChrThread(0x101, 0x1)
    OP_22(0xD6, 0x0, 0x64)

    def lambda_3AA7():
        OP_69(0x101, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3AA7)

    def lambda_3AB5():
        OP_95(0xFE, 0x0, 0x0, 0xFFFFF830, 0x5DC, 0x1388)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3AB5)
    SetChrSubChip(0x101, 3)
    SetChrChipByIndex(0x101, 1)
    WaitChrThread(0x101, 0x2)
    Sleep(1000)
    SetChrSubChip(0x101, 2)
    Sleep(100)

    ChrTalk(    #76
        0x101,
        (
            "#2P#1007FWaaaaa...\x01",
            "My arm's all numb...\x02\x03",

            "#1013FSo much for my career as\x01",
            "Estelle the Wall-Crusher, I guess...\x02",
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
            "#2P#1002FGuess I'll just have to try\x01",
            "and find some way around.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1C21)
    Jump("loc_3BEE")

    label("loc_3BC1")

    OP_8C(0x101, 0, 400)
    Sleep(300)
    OP_95(0x101, 0x0, 0x0, 0xFFFFF830, 0x3E8, 0x1388)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)

    label("loc_3BEE")

    OP_73(0x4)
    EventEnd(0x0)

    label("loc_3BF3")

    Return()

    # Function_20_3769 end

    def Function_21_3BF4(): pass

    label("Function_21_3BF4")

    OP_A2(0x1C81)
    OP_A3(0x1C82)
    OP_A3(0x1C83)
    OP_A3(0x1C84)
    OP_A3(0x1C85)
    OP_A3(0x1C86)
    OP_A3(0x1C87)
    OP_A3(0x1C88)
    Return()

    # Function_21_3BF4 end

    def Function_22_3C0D(): pass

    label("Function_22_3C0D")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_AD(0x24012E, 0x0, 0x0, 0x1F4)
    Sleep(500)
    OP_56(0x3)
    OP_AE(0x1F4)
    TalkEnd(0xFF)
    Return()

    # Function_22_3C0D end

    SaveToFile()

Try(main)
