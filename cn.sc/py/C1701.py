from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 柏斯

    CreateScenaFile(
        FileName            = 'C1701   ._SN',
        MapName             = 'Bose',
        Location            = 'C1701.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60060",
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
        '',                                     # 9
        '',                                     # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
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
        'ED6_DT29/CH12800 ._CH',             # 00
        'ED6_DT29/CH12801 ._CH',             # 01
        'ED6_DT29/CH12810 ._CH',             # 02
        'ED6_DT29/CH12811 ._CH',             # 03
        'ED6_DT29/CH12820 ._CH',             # 04
        'ED6_DT29/CH12821 ._CH',             # 05
        'ED6_DT29/CH12830 ._CH',             # 06
        'ED6_DT29/CH12831 ._CH',             # 07
        'ED6_DT29/CH12840 ._CH',             # 08
        'ED6_DT29/CH12841 ._CH',             # 09
        'ED6_DT29/CH12850 ._CH',             # 0A
        'ED6_DT29/CH12851 ._CH',             # 0B
        'ED6_DT29/CH12860 ._CH',             # 0C
        'ED6_DT29/CH12861 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT29/CH12800P._CP',             # 00
        'ED6_DT29/CH12801P._CP',             # 01
        'ED6_DT29/CH12810P._CP',             # 02
        'ED6_DT29/CH12811P._CP',             # 03
        'ED6_DT29/CH12820P._CP',             # 04
        'ED6_DT29/CH12821P._CP',             # 05
        'ED6_DT29/CH12830P._CP',             # 06
        'ED6_DT29/CH12831P._CP',             # 07
        'ED6_DT29/CH12840P._CP',             # 08
        'ED6_DT29/CH12841P._CP',             # 09
        'ED6_DT29/CH12850P._CP',             # 0A
        'ED6_DT29/CH12851P._CP',             # 0B
        'ED6_DT29/CH12860P._CP',             # 0C
        'ED6_DT29/CH12861P._CP',             # 0D
    )

    DeclMonster(
        X                   = -5970,
        Z                   = 400,
        Y                   = 45720,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F4,
        Unknown_18          = 8159,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 5390,
        Z                   = 400,
        Y                   = 45270,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F6,
        Unknown_18          = 8160,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 5120,
        Z                   = 400,
        Y                   = 34620,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F4,
        Unknown_18          = 8161,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -5060,
        Z                   = 400,
        Y                   = 34970,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F7,
        Unknown_18          = 8162,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -5260,
        Z                   = 400,
        Y                   = -35050,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F5,
        Unknown_18          = 8163,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 4970,
        Z                   = 400,
        Y                   = -35230,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F8,
        Unknown_18          = 8164,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 4920,
        Z                   = 400,
        Y                   = -45050,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F4,
        Unknown_18          = 8165,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -5210,
        Z                   = 400,
        Y                   = -44800,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F6,
        Unknown_18          = 8166,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -35820,
        Z                   = 400,
        Y                   = -28320,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F8,
        Unknown_18          = 8167,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -22620,
        Z                   = 400,
        Y                   = -28510,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F4,
        Unknown_18          = 8168,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -48840,
        Z                   = 400,
        Y                   = 2080,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F6,
        Unknown_18          = 8169,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -41530,
        Z                   = 400,
        Y                   = 9460,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F5,
        Unknown_18          = 8170,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -58380,
        Z                   = 400,
        Y                   = 18910,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F4,
        Unknown_18          = 8171,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -68160,
        Z                   = 400,
        Y                   = 28510,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F7,
        Unknown_18          = 8172,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 24510,
        Z                   = 400,
        Y                   = 32220,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F8,
        Unknown_18          = 8173,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 32299,
        Z                   = 400,
        Y                   = 24240,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F5,
        Unknown_18          = 8174,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 28240,
        Z                   = 400,
        Y                   = -34620,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F4,
        Unknown_18          = 8175,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 28550,
        Z                   = 400,
        Y                   = -22270,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F6,
        Unknown_18          = 8176,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -35620,
        Z                   = 400,
        Y                   = 28020,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F5,
        Unknown_18          = 8177,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -21380,
        Z                   = 400,
        Y                   = 27940,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F4,
        Unknown_18          = 8178,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 49370,
        Z                   = 400,
        Y                   = 1840,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F7,
        Unknown_18          = 8179,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 41470,
        Z                   = 400,
        Y                   = 9410,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F6,
        Unknown_18          = 8180,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 56480,
        Z                   = 400,
        Y                   = 22770,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F4,
        Unknown_18          = 8181,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 58240,
        Z                   = 400,
        Y                   = 29080,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F5,
        Unknown_18          = 8182,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 64269,
        Z                   = 400,
        Y                   = 30680,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F6,
        Unknown_18          = 8183,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 69700,
        Z                   = 400,
        Y                   = 25930,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F4,
        Unknown_18          = 8184,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 68230,
        Z                   = 400,
        Y                   = 19540,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F8,
        Unknown_18          = 8185,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 63650,
        Z                   = 400,
        Y                   = 17440,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F5,
        Unknown_18          = 8186,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -63050,
        TriggerZ            = -50,
        TriggerY            = 23470,
        TriggerRange        = 1000,
        ActorX              = -63580,
        ActorZ              = -50,
        ActorY              = 24000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 63180,
        TriggerZ            = -50,
        TriggerY            = 23570,
        TriggerRange        = 1000,
        ActorX              = 63680,
        ActorZ              = -50,
        ActorY              = 24060,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 40,
        TriggerZ            = 0,
        TriggerY            = 40700,
        TriggerRange        = 1000,
        ActorX              = 40,
        ActorZ              = 0,
        ActorY              = 39950,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 40,
        TriggerZ            = 0,
        TriggerY            = -39300,
        TriggerRange        = 1000,
        ActorX              = 40,
        ActorZ              = 0,
        ActorY              = -40050,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -44740,
        TriggerZ            = 0,
        TriggerY            = 5210,
        TriggerRange        = 1000,
        ActorX              = -45200,
        ActorZ              = 0,
        ActorY              = 5680,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -28740,
        TriggerZ            = 0,
        TriggerY            = -28820,
        TriggerRange        = 1000,
        ActorX              = -28270,
        ActorZ              = 0,
        ActorY              = -28350,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 27840,
        TriggerZ            = 0,
        TriggerY            = 27760,
        TriggerRange        = 1000,
        ActorX              = 28280,
        ActorZ              = 0,
        ActorY              = 28190,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -27740,
        TriggerZ            = 0,
        TriggerY            = 27880,
        TriggerRange        = 1000,
        ActorX              = -28270,
        ActorZ              = 0,
        ActorY              = 28280,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 28880,
        TriggerZ            = 0,
        TriggerY            = -28720,
        TriggerRange        = 1000,
        ActorX              = 28380,
        ActorZ              = 0,
        ActorY              = -28280,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 44780,
        TriggerZ            = -50,
        TriggerY            = 5110,
        TriggerRange        = 1000,
        ActorX              = 45180,
        ActorZ              = -50,
        ActorY              = 5630,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_592",          # 00, 0
        "Function_1_5DD",          # 01, 1
        "Function_2_846",          # 02, 2
        "Function_3_95D",          # 03, 3
        "Function_4_A74",          # 04, 4
        "Function_5_B8B",          # 05, 5
        "Function_6_CA2",          # 06, 6
        "Function_7_DB9",          # 07, 7
        "Function_8_EB5",          # 08, 8
        "Function_9_FCC",          # 09, 9
        "Function_10_10E3",        # 0A, 10
        "Function_11_11FA",        # 0B, 11
        "Function_12_1311",        # 0C, 12
        "Function_13_140C",        # 0D, 13
        "Function_14_1484",        # 0E, 14
        "Function_15_157F",        # 0F, 15
        "Function_16_15F7",        # 10, 16
        "Function_17_16F2",        # 11, 17
        "Function_18_176A",        # 12, 18
        "Function_19_1877",        # 13, 19
        "Function_20_18F8",        # 14, 20
        "Function_21_1A05",        # 15, 21
        "Function_22_1A86",        # 16, 22
        "Function_23_1B93",        # 17, 23
        "Function_24_1C14",        # 18, 24
        "Function_25_1D07",        # 19, 25
        "Function_26_1DFA",        # 1A, 26
        "Function_27_1E48",        # 1B, 27
    )


    def Function_0_592(): pass

    label("Function_0_592")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_5B2"),
        (101, "loc_5B9"),
        (102, "loc_5C0"),
        (103, "loc_5C7"),
        (104, "loc_5CE"),
        (105, "loc_5D5"),
        (SWITCH_DEFAULT, "loc_5DC"),
    )


    label("loc_5B2")

    Event(0, 12)
    Jump("loc_5DC")

    label("loc_5B9")

    Event(0, 14)
    Jump("loc_5DC")

    label("loc_5C0")

    Event(0, 16)
    Jump("loc_5DC")

    label("loc_5C7")

    Event(0, 18)
    Jump("loc_5DC")

    label("loc_5CE")

    Event(0, 20)
    Jump("loc_5DC")

    label("loc_5D5")

    Event(0, 22)
    Jump("loc_5DC")

    label("loc_5DC")

    Return()

    # Function_0_592 end

    def Function_1_5DD(): pass

    label("Function_1_5DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5EF")
    OP_6F(0x0, 0)
    Jump("loc_5F6")

    label("loc_5EF")

    OP_6F(0x0, 60)

    label("loc_5F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_608")
    OP_6F(0x1, 0)
    Jump("loc_60F")

    label("loc_608")

    OP_6F(0x1, 60)

    label("loc_60F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_621")
    OP_6F(0x2, 0)
    Jump("loc_628")

    label("loc_621")

    OP_6F(0x2, 60)

    label("loc_628")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63A")
    OP_6F(0x3, 0)
    Jump("loc_641")

    label("loc_63A")

    OP_6F(0x3, 60)

    label("loc_641")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_653")
    OP_6F(0x4, 0)
    Jump("loc_65A")

    label("loc_653")

    OP_6F(0x4, 60)

    label("loc_65A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66C")
    OP_6F(0x5, 0)
    Jump("loc_673")

    label("loc_66C")

    OP_6F(0x5, 60)

    label("loc_673")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_685")
    OP_6F(0x6, 0)
    Jump("loc_68C")

    label("loc_685")

    OP_6F(0x6, 60)

    label("loc_68C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_69E")
    OP_6F(0x7, 0)
    Jump("loc_6A5")

    label("loc_69E")

    OP_6F(0x7, 60)

    label("loc_6A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B7")
    OP_6F(0x8, 0)
    Jump("loc_6BE")

    label("loc_6B7")

    OP_6F(0x8, 60)

    label("loc_6BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F4, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D0")
    OP_6F(0x9, 0)
    Jump("loc_6D7")

    label("loc_6D0")

    OP_6F(0x9, 60)

    label("loc_6D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FB, 7)), scpexpr(EXPR_END)), "loc_6E3")
    SetChrFlags(0x8, 0x80)

    label("loc_6E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FC, 0)), scpexpr(EXPR_END)), "loc_6EF")
    SetChrFlags(0x9, 0x80)

    label("loc_6EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FC, 1)), scpexpr(EXPR_END)), "loc_6FB")
    SetChrFlags(0xA, 0x80)

    label("loc_6FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FC, 2)), scpexpr(EXPR_END)), "loc_707")
    SetChrFlags(0xB, 0x80)

    label("loc_707")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FC, 3)), scpexpr(EXPR_END)), "loc_713")
    SetChrFlags(0xC, 0x80)

    label("loc_713")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FC, 4)), scpexpr(EXPR_END)), "loc_71F")
    SetChrFlags(0xD, 0x80)

    label("loc_71F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FC, 5)), scpexpr(EXPR_END)), "loc_72B")
    SetChrFlags(0xE, 0x80)

    label("loc_72B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FC, 6)), scpexpr(EXPR_END)), "loc_737")
    SetChrFlags(0xF, 0x80)

    label("loc_737")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FC, 7)), scpexpr(EXPR_END)), "loc_743")
    SetChrFlags(0x10, 0x80)

    label("loc_743")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FD, 0)), scpexpr(EXPR_END)), "loc_74F")
    SetChrFlags(0x11, 0x80)

    label("loc_74F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FD, 1)), scpexpr(EXPR_END)), "loc_75B")
    SetChrFlags(0x12, 0x80)

    label("loc_75B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FD, 2)), scpexpr(EXPR_END)), "loc_767")
    SetChrFlags(0x13, 0x80)

    label("loc_767")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FD, 3)), scpexpr(EXPR_END)), "loc_773")
    SetChrFlags(0x14, 0x80)

    label("loc_773")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FD, 4)), scpexpr(EXPR_END)), "loc_77F")
    SetChrFlags(0x15, 0x80)

    label("loc_77F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FD, 5)), scpexpr(EXPR_END)), "loc_78B")
    SetChrFlags(0x16, 0x80)

    label("loc_78B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FD, 6)), scpexpr(EXPR_END)), "loc_797")
    SetChrFlags(0x17, 0x80)

    label("loc_797")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FD, 7)), scpexpr(EXPR_END)), "loc_7A3")
    SetChrFlags(0x18, 0x80)

    label("loc_7A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FE, 0)), scpexpr(EXPR_END)), "loc_7AF")
    SetChrFlags(0x19, 0x80)

    label("loc_7AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FE, 1)), scpexpr(EXPR_END)), "loc_7BB")
    SetChrFlags(0x1A, 0x80)

    label("loc_7BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FE, 2)), scpexpr(EXPR_END)), "loc_7C7")
    SetChrFlags(0x1B, 0x80)

    label("loc_7C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FE, 3)), scpexpr(EXPR_END)), "loc_7D3")
    SetChrFlags(0x1C, 0x80)

    label("loc_7D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FE, 4)), scpexpr(EXPR_END)), "loc_7DF")
    SetChrFlags(0x1D, 0x80)

    label("loc_7DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FE, 5)), scpexpr(EXPR_END)), "loc_7EB")
    SetChrFlags(0x1E, 0x80)

    label("loc_7EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FE, 6)), scpexpr(EXPR_END)), "loc_7F7")
    SetChrFlags(0x1F, 0x80)

    label("loc_7F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FE, 7)), scpexpr(EXPR_END)), "loc_803")
    SetChrFlags(0x20, 0x80)

    label("loc_803")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FF, 0)), scpexpr(EXPR_END)), "loc_80F")
    SetChrFlags(0x21, 0x80)

    label("loc_80F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FF, 1)), scpexpr(EXPR_END)), "loc_81B")
    SetChrFlags(0x22, 0x80)

    label("loc_81B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FF, 2)), scpexpr(EXPR_END)), "loc_827")
    SetChrFlags(0x23, 0x80)

    label("loc_827")

    OP_1B(0x0, 0x0, 0xD)
    OP_1B(0x1, 0x0, 0xF)
    OP_1B(0x2, 0x0, 0x11)
    OP_1B(0x3, 0x0, 0x13)
    OP_1B(0x4, 0x0, 0x15)
    OP_1B(0x5, 0x0, 0x17)
    Return()

    # Function_1_5DD end

    def Function_2_846(): pass

    label("Function_2_846")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_91E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x164, 1)"), scpexpr(EXPR_END)), "loc_8B5")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x64\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F92)
    Jump("loc_91B")

    label("loc_8B5")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\x64\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x64\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_91B")

    Jump("loc_94F")

    label("loc_91E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_94F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_846 end

    def Function_3_95D(): pass

    label("Function_3_95D")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A35")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x17D, 1)"), scpexpr(EXPR_END)), "loc_9CC")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\x7D\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F94)
    Jump("loc_A32")

    label("loc_9CC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\x7D\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x7D\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_A32")

    Jump("loc_A66")

    label("loc_A35")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_A66")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_95D end

    def Function_4_A74(): pass

    label("Function_4_A74")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B4C")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x202, 1)"), scpexpr(EXPR_END)), "loc_AE3")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x00得到了\x1F\x02\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F96)
    Jump("loc_B49")

    label("loc_AE3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "宝箱里装有\x1F\x02\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x02\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_B49")

    Jump("loc_B7D")

    label("loc_B4C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_B7D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_A74 end

    def Function_5_B8B(): pass

    label("Function_5_B8B")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C63")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FF, 1)"), scpexpr(EXPR_END)), "loc_BFA")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x00得到了\x1F\xFF\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F97)
    Jump("loc_C60")

    label("loc_BFA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "宝箱里装有\x1F\xFF\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFF\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_C60")

    Jump("loc_C94")

    label("loc_C63")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_C94")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_B8B end

    def Function_6_CA2(): pass

    label("Function_6_CA2")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D7A")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x204, 1)"), scpexpr(EXPR_END)), "loc_D11")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #12
        "\x07\x00得到了\x1F\x04\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F98)
    Jump("loc_D77")

    label("loc_D11")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        (
            "宝箱里装有\x1F\x04\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x04\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_D77")

    Jump("loc_DAB")

    label("loc_D7A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_DAB")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_CA2 end

    def Function_7_DB9(): pass

    label("Function_7_DB9")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E89")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x1E)
    OP_73(0x5)
    OP_6F(0x5, 30)
    AddSepith(0x0, 0x12C)
    AddSepith(0x4, 0x64)
    AddSepith(0x5, 0x64)
    AddSepith(0x6, 0x64)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #15
        (
            "\x07\x00得到了\x07\x02#56I地之耀晶片×３００\x01",
            "\x07\x02#62I时之耀晶片×１００\x01",
            "\x07\x02#60I空之耀晶片×１００\x01",
            "\x07\x02#61I幻之耀晶片×１００\x01",
            "\x07\x00。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x1F99)
    Jump("loc_EA3")

    label("loc_E89")


    AnonymousTalk(    #16
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_EA3")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_DB9 end

    def Function_8_EB5(): pass

    label("Function_8_EB5")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F8D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x206, 1)"), scpexpr(EXPR_END)), "loc_F24")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #17
        "\x07\x00得到了\x1F\x06\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1FA0)
    Jump("loc_F8A")

    label("loc_F24")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #18
        (
            "宝箱里装有\x1F\x06\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x06\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)

    label("loc_F8A")

    Jump("loc_FBE")

    label("loc_F8D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #19
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_FBE")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_EB5 end

    def Function_9_FCC(): pass

    label("Function_9_FCC")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10A4")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x7, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_103B")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #20
        "\x07\x00得到了\x1F\xFB\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1FA1)
    Jump("loc_10A1")

    label("loc_103B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #21
        (
            "宝箱里装有\x1F\xFB\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFB\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x7, 60)
    OP_70(0x7, 0x0)

    label("loc_10A1")

    Jump("loc_10D5")

    label("loc_10A4")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #22
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_10D5")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_FCC end

    def Function_10_10E3(): pass

    label("Function_10_10E3")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11BB")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x8, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x12F, 1)"), scpexpr(EXPR_END)), "loc_1152")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #23
        "\x07\x00得到了\x1F\x2F\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1FA2)
    Jump("loc_11B8")

    label("loc_1152")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #24
        (
            "宝箱里装有\x1F\x2F\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x2F\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x8, 60)
    OP_70(0x8, 0x0)

    label("loc_11B8")

    Jump("loc_11EC")

    label("loc_11BB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #25
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_11EC")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_10E3 end

    def Function_11_11FA(): pass

    label("Function_11_11FA")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F4, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12D2")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x9, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F7, 1)"), scpexpr(EXPR_END)), "loc_1269")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #26
        "\x07\x00得到了\x1F\xF7\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1FA3)
    Jump("loc_12CF")

    label("loc_1269")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #27
        (
            "宝箱里装有\x1F\xF7\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xF7\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x9, 60)
    OP_70(0x9, 0x0)

    label("loc_12CF")

    Jump("loc_1303")

    label("loc_12D2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #28
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1303")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_11_11FA end

    def Function_12_1311(): pass

    label("Function_12_1311")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(0, 200, 66500, 0)
    SetChrPos(0x101, 500, 200, 66000, 180)
    SetChrPos(0x102, -500, 200, 66000, 180)
    SetChrPos(0xF8, 500, 200, 67000, 180)
    SetChrPos(0xF9, -500, 200, 67000, 180)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 24)
    Call(0, 26)
    Fade(500)
    OP_6D(70, 200, 64620, 0)
    SetChrPos(0x0, 70, 200, 64620, 180)
    SetChrPos(0x1, 70, 200, 64620, 180)
    SetChrPos(0x2, 70, 200, 64620, 180)
    SetChrPos(0x3, 70, 200, 64620, 180)
    EventEnd(0x0)
    Return()

    # Function_12_1311 end

    def Function_13_140C(): pass

    label("Function_13_140C")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(0, 200, 66500, 0)
    SetChrPos(0x101, -500, 200, 67000, 0)
    SetChrPos(0x102, 500, 200, 67000, 0)
    SetChrPos(0xF8, -500, 200, 66000, 0)
    SetChrPos(0xF9, 500, 200, 66000, 0)
    OP_0D()
    Call(0, 24)
    Call(0, 27)
    NewScene("ED6_DT21/C1700   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_13_140C end

    def Function_14_1484(): pass

    label("Function_14_1484")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-46600, 200, 47300, 0)
    SetChrPos(0x101, -46100, 200, 46800, 180)
    SetChrPos(0x102, -47100, 200, 46800, 180)
    SetChrPos(0xF8, -46100, 200, 47800, 180)
    SetChrPos(0xF9, -47100, 200, 47800, 180)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 24)
    Call(0, 26)
    Fade(500)
    OP_6D(-46580, 200, 45210, 0)
    SetChrPos(0x0, -46580, 200, 45210, 180)
    SetChrPos(0x1, -46580, 200, 45210, 180)
    SetChrPos(0x2, -46580, 200, 45210, 180)
    SetChrPos(0x3, -46580, 200, 45210, 180)
    EventEnd(0x0)
    Return()

    # Function_14_1484 end

    def Function_15_157F(): pass

    label("Function_15_157F")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(-46600, 200, 47300, 0)
    SetChrPos(0x101, -47100, 200, 47800, 0)
    SetChrPos(0x102, -46100, 200, 47800, 0)
    SetChrPos(0xF8, -47100, 200, 46800, 0)
    SetChrPos(0xF9, -46100, 200, 46800, 0)
    OP_0D()
    Call(0, 24)
    Call(0, 27)
    NewScene("ED6_DT21/C1702   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_15_157F end

    def Function_16_15F7(): pass

    label("Function_16_15F7")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(46700, 200, 47200, 0)
    SetChrPos(0x101, 47200, 200, 46700, 180)
    SetChrPos(0x102, 46200, 200, 46700, 180)
    SetChrPos(0xF8, 47200, 200, 47700, 180)
    SetChrPos(0xF9, 46200, 200, 47700, 180)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 24)
    Call(0, 26)
    Fade(500)
    OP_6D(46730, 200, 45190, 0)
    SetChrPos(0x0, 46730, 200, 45190, 180)
    SetChrPos(0x1, 46730, 200, 45190, 180)
    SetChrPos(0x2, 46730, 200, 45190, 180)
    SetChrPos(0x3, 46730, 200, 45190, 180)
    EventEnd(0x0)
    Return()

    # Function_16_15F7 end

    def Function_17_16F2(): pass

    label("Function_17_16F2")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(46700, 200, 47200, 0)
    SetChrPos(0x101, 46200, 200, 47700, 0)
    SetChrPos(0x102, 47200, 200, 47700, 0)
    SetChrPos(0xF8, 46200, 200, 46700, 0)
    SetChrPos(0xF9, 47200, 200, 46700, 0)
    OP_0D()
    Call(0, 24)
    Call(0, 27)
    NewScene("ED6_DT21/C1702   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_17_16F2 end

    def Function_18_176A(): pass

    label("Function_18_176A")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(0, 200, -66500, 0)
    OP_6C(135000, 0)
    SetChrPos(0x101, -500, 200, -66000, 0)
    SetChrPos(0x102, 500, 200, -66000, 0)
    SetChrPos(0xF8, -500, 200, -67000, 0)
    SetChrPos(0xF9, 500, 200, -67000, 0)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 25)
    Call(0, 26)
    Fade(500)
    OP_6D(-90, 200, -64500, 0)
    OP_6C(45000, 0)
    SetChrPos(0x0, -90, 200, -64500, 0)
    SetChrPos(0x1, -90, 200, -64500, 0)
    SetChrPos(0x2, -90, 200, -64500, 0)
    SetChrPos(0x3, -90, 200, -64500, 0)
    EventEnd(0x0)
    Return()

    # Function_18_176A end

    def Function_19_1877(): pass

    label("Function_19_1877")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(0, 200, -66500, 0)
    OP_6C(135000, 0)
    SetChrPos(0x101, 500, 200, -67000, 180)
    SetChrPos(0x102, -500, 200, -67000, 180)
    SetChrPos(0xF8, 500, 200, -66000, 180)
    SetChrPos(0xF9, -500, 200, -66000, 180)
    OP_0D()
    Call(0, 25)
    Call(0, 27)
    NewScene("ED6_DT21/C1702   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_19_1877 end

    def Function_20_18F8(): pass

    label("Function_20_18F8")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(46600, 200, -47000, 0)
    OP_6C(135000, 0)
    SetChrPos(0x101, 46100, 200, -46500, 0)
    SetChrPos(0x102, 47100, 200, -46500, 0)
    SetChrPos(0xF8, 46100, 200, -47500, 0)
    SetChrPos(0xF9, 47100, 200, -47500, 0)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 25)
    Call(0, 26)
    Fade(500)
    OP_6D(46590, 200, -45090, 0)
    OP_6C(45000, 0)
    SetChrPos(0x0, 46590, 200, -45090, 0)
    SetChrPos(0x1, 46590, 200, -45090, 0)
    SetChrPos(0x2, 46590, 200, -45090, 0)
    SetChrPos(0x3, 46590, 200, -45090, 0)
    EventEnd(0x0)
    Return()

    # Function_20_18F8 end

    def Function_21_1A05(): pass

    label("Function_21_1A05")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(46600, 200, -47000, 0)
    OP_6C(135000, 0)
    SetChrPos(0x101, 47100, 200, -47500, 180)
    SetChrPos(0x102, 46100, 200, -47500, 180)
    SetChrPos(0xF8, 47100, 200, -46500, 180)
    SetChrPos(0xF9, 46100, 200, -46500, 180)
    OP_0D()
    Call(0, 25)
    Call(0, 27)
    NewScene("ED6_DT21/C1702   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_21_1A05 end

    def Function_22_1A86(): pass

    label("Function_22_1A86")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-46600, 200, -47000, 0)
    OP_6C(135000, 0)
    SetChrPos(0x101, -47100, 200, -46500, 0)
    SetChrPos(0x102, -46100, 200, -46500, 0)
    SetChrPos(0xF8, -47100, 200, -47500, 0)
    SetChrPos(0xF9, -46100, 200, -47500, 0)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 25)
    Call(0, 26)
    Fade(500)
    OP_6D(-46720, 200, -45050, 0)
    OP_6C(45000, 0)
    SetChrPos(0x0, -46720, 200, -45050, 0)
    SetChrPos(0x1, -46720, 200, -45050, 0)
    SetChrPos(0x2, -46720, 200, -45050, 0)
    SetChrPos(0x3, -46720, 200, -45050, 0)
    EventEnd(0x0)
    Return()

    # Function_22_1A86 end

    def Function_23_1B93(): pass

    label("Function_23_1B93")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(-46600, 200, -47000, 0)
    OP_6C(135000, 0)
    SetChrPos(0x101, -46100, 200, -47500, 180)
    SetChrPos(0x102, -47100, 200, -47500, 180)
    SetChrPos(0xF8, -46100, 200, -46500, 180)
    SetChrPos(0xF9, -47100, 200, -46500, 180)
    OP_0D()
    Call(0, 25)
    Call(0, 27)
    NewScene("ED6_DT21/C1702   ._SN", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_23_1B93 end

    def Function_24_1C14(): pass

    label("Function_24_1C14")

    LoadEffect(0x0, "map\\\\mp049_21.eff")
    PlayEffect(0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Return()

    # Function_24_1C14 end

    def Function_25_1D07(): pass

    label("Function_25_1D07")

    LoadEffect(0x0, "map\\\\mp049_22.eff")
    PlayEffect(0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Return()

    # Function_25_1D07 end

    def Function_26_1DFA(): pass

    label("Function_26_1DFA")


    def lambda_1E00():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1E00)

    def lambda_1E12():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1E12)

    def lambda_1E24():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1E24)

    def lambda_1E36():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1E36)
    Sleep(2500)
    Return()

    # Function_26_1DFA end

    def Function_27_1E48(): pass

    label("Function_27_1E48")


    def lambda_1E4E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1E4E)

    def lambda_1E60():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1E60)

    def lambda_1E72():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1E72)

    def lambda_1E84():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1E84)
    Sleep(2000)
    Return()

    # Function_27_1E48 end

    SaveToFile()

Try(main)
