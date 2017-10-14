from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        '',                                     # 14
        '',                                     # 15
        '',                                     # 16
        '',                                     # 17
        '',                                     # 18
        '',                                     # 19
        '',                                     # 20
        '',                                     # 21
        '',                                     # 22
        '',                                     # 23
        '',                                     # 24
        '',                                     # 25
        '',                                     # 26
        '',                                     # 27
        '',                                     # 28
        '',                                     # 29
        '',                                     # 30
        '',                                     # 31
        '',                                     # 32
        '',                                     # 33
        '',                                     # 34
        '',                                     # 35
        '',                                     # 36
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
        "Function_2_86E",          # 02, 2
        "Function_3_9F6",          # 03, 3
        "Function_4_B15",          # 04, 4
        "Function_5_C85",          # 05, 5
        "Function_6_DBA",          # 06, 6
        "Function_7_EF5",          # 07, 7
        "Function_8_101A",         # 08, 8
        "Function_9_1163",         # 09, 9
        "Function_10_12C8",        # 0A, 10
        "Function_11_143E",        # 0B, 11
        "Function_12_1584",        # 0C, 12
        "Function_13_1684",        # 0D, 13
        "Function_14_16FC",        # 0E, 14
        "Function_15_17FC",        # 0F, 15
        "Function_16_1874",        # 10, 16
        "Function_17_1974",        # 11, 17
        "Function_18_19EC",        # 12, 18
        "Function_19_1AFE",        # 13, 19
        "Function_20_1B7F",        # 14, 20
        "Function_21_1C91",        # 15, 21
        "Function_22_1D12",        # 16, 22
        "Function_23_1E24",        # 17, 23
        "Function_24_1EA5",        # 18, 24
        "Function_25_1F84",        # 19, 25
        "Function_26_2063",        # 1A, 26
        "Function_27_20B1",        # 1B, 27
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

    LoadEffect(0x0, "map\\\\mp049_21.eff")
    LoadEffect(0x1, "map\\\\mp049_22.eff")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FB, 7)), scpexpr(EXPR_END)), "loc_70B")
    SetChrFlags(0x8, 0x80)

    label("loc_70B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FC, 0)), scpexpr(EXPR_END)), "loc_717")
    SetChrFlags(0x9, 0x80)

    label("loc_717")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FC, 1)), scpexpr(EXPR_END)), "loc_723")
    SetChrFlags(0xA, 0x80)

    label("loc_723")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FC, 2)), scpexpr(EXPR_END)), "loc_72F")
    SetChrFlags(0xB, 0x80)

    label("loc_72F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FC, 3)), scpexpr(EXPR_END)), "loc_73B")
    SetChrFlags(0xC, 0x80)

    label("loc_73B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FC, 4)), scpexpr(EXPR_END)), "loc_747")
    SetChrFlags(0xD, 0x80)

    label("loc_747")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FC, 5)), scpexpr(EXPR_END)), "loc_753")
    SetChrFlags(0xE, 0x80)

    label("loc_753")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FC, 6)), scpexpr(EXPR_END)), "loc_75F")
    SetChrFlags(0xF, 0x80)

    label("loc_75F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FC, 7)), scpexpr(EXPR_END)), "loc_76B")
    SetChrFlags(0x10, 0x80)

    label("loc_76B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FD, 0)), scpexpr(EXPR_END)), "loc_777")
    SetChrFlags(0x11, 0x80)

    label("loc_777")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FD, 1)), scpexpr(EXPR_END)), "loc_783")
    SetChrFlags(0x12, 0x80)

    label("loc_783")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FD, 2)), scpexpr(EXPR_END)), "loc_78F")
    SetChrFlags(0x13, 0x80)

    label("loc_78F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FD, 3)), scpexpr(EXPR_END)), "loc_79B")
    SetChrFlags(0x14, 0x80)

    label("loc_79B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FD, 4)), scpexpr(EXPR_END)), "loc_7A7")
    SetChrFlags(0x15, 0x80)

    label("loc_7A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FD, 5)), scpexpr(EXPR_END)), "loc_7B3")
    SetChrFlags(0x16, 0x80)

    label("loc_7B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FD, 6)), scpexpr(EXPR_END)), "loc_7BF")
    SetChrFlags(0x17, 0x80)

    label("loc_7BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FD, 7)), scpexpr(EXPR_END)), "loc_7CB")
    SetChrFlags(0x18, 0x80)

    label("loc_7CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FE, 0)), scpexpr(EXPR_END)), "loc_7D7")
    SetChrFlags(0x19, 0x80)

    label("loc_7D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FE, 1)), scpexpr(EXPR_END)), "loc_7E3")
    SetChrFlags(0x1A, 0x80)

    label("loc_7E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FE, 2)), scpexpr(EXPR_END)), "loc_7EF")
    SetChrFlags(0x1B, 0x80)

    label("loc_7EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FE, 3)), scpexpr(EXPR_END)), "loc_7FB")
    SetChrFlags(0x1C, 0x80)

    label("loc_7FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FE, 4)), scpexpr(EXPR_END)), "loc_807")
    SetChrFlags(0x1D, 0x80)

    label("loc_807")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FE, 5)), scpexpr(EXPR_END)), "loc_813")
    SetChrFlags(0x1E, 0x80)

    label("loc_813")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FE, 6)), scpexpr(EXPR_END)), "loc_81F")
    SetChrFlags(0x1F, 0x80)

    label("loc_81F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FE, 7)), scpexpr(EXPR_END)), "loc_82B")
    SetChrFlags(0x20, 0x80)

    label("loc_82B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FF, 0)), scpexpr(EXPR_END)), "loc_837")
    SetChrFlags(0x21, 0x80)

    label("loc_837")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FF, 1)), scpexpr(EXPR_END)), "loc_843")
    SetChrFlags(0x22, 0x80)

    label("loc_843")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FF, 2)), scpexpr(EXPR_END)), "loc_84F")
    SetChrFlags(0x23, 0x80)

    label("loc_84F")

    OP_1B(0x0, 0x0, 0xD)
    OP_1B(0x1, 0x0, 0xF)
    OP_1B(0x2, 0x0, 0x11)
    OP_1B(0x3, 0x0, 0x13)
    OP_1B(0x4, 0x0, 0x15)
    OP_1B(0x5, 0x0, 0x17)
    Return()

    # Function_1_5DD end

    def Function_2_86E(): pass

    label("Function_2_86E")

    OP_EA(0x2, 0x69, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_946")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x164, 1)"), scpexpr(EXPR_END)), "loc_8DF")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\x64\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F92)
    Jump("loc_943")

    label("loc_8DF")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\x64\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x64\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_943")

    Jump("loc_9E8")

    label("loc_946")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05You ever wonder if the items in these chests\x01",
            "were meant for someone specific? And you have\x01",
            "the nerve to take them anyway. How rude.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_9E8")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_86E end

    def Function_3_9F6(): pass

    label("Function_3_9F6")

    OP_EA(0x2, 0x6A, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ACE")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x17D, 1)"), scpexpr(EXPR_END)), "loc_A67")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "Found \x1F\x7D\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F94)
    Jump("loc_ACB")

    label("loc_A67")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "Found \x1F\x7D\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x7D\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_ACB")

    Jump("loc_B07")

    label("loc_ACE")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05Wow! Look at all this air!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_B07")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_9F6 end

    def Function_4_B15(): pass

    label("Function_4_B15")

    OP_EA(0x2, 0x6B, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BED")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x202, 1)"), scpexpr(EXPR_END)), "loc_B86")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "Found \x1F\x02\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F96)
    Jump("loc_BEA")

    label("loc_B86")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "Found \x1F\x02\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x02\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_BEA")

    Jump("loc_C77")

    label("loc_BED")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        (
            "\x07\x05You open the chest, eyes wild with avarice.\x01",
            "Your face falls as you realize you've already\x01",
            "taken everything.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_C77")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_B15 end

    def Function_5_C85(): pass

    label("Function_5_C85")

    OP_EA(0x2, 0x6C, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D5D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FF, 1)"), scpexpr(EXPR_END)), "loc_CF6")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "Found \x1F\xFF\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F97)
    Jump("loc_D5A")

    label("loc_CF6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "Found \x1F\xFF\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFF\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_D5A")

    Jump("loc_DAC")

    label("loc_D5D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x05Well, I see you're not above asking for seconds.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_DAC")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_C85 end

    def Function_6_DBA(): pass

    label("Function_6_DBA")

    OP_EA(0x2, 0x6D, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E92")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x204, 1)"), scpexpr(EXPR_END)), "loc_E2B")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #12
        "Found \x1F\x04\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F98)
    Jump("loc_E8F")

    label("loc_E2B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        (
            "Found \x1F\x04\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x04\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_E8F")

    Jump("loc_EE7")

    label("loc_E92")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        (
            "\x07\x05This empty chest is a monument to your\x01",
            "reckless greed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_EE7")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_DBA end

    def Function_7_EF5(): pass

    label("Function_7_EF5")

    OP_EA(0x2, 0x6E, 0x0, 0x0)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FBE")
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
            "Found\x01",
            "#2C#56IEarth Sepith x300\x01",
            "#62ITime Sepith x100\x01",
            "#60ISpace Sepith x100\x01",
            "#61IMirage Sepith x100#0C.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x1F99)
    Jump("loc_1008")

    label("loc_FBE")


    AnonymousTalk(    #16
        (
            "\x07\x05Now that you've taken my contents,\x01",
            "this means we're dating, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_1008")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_EF5 end

    def Function_8_101A(): pass

    label("Function_8_101A")

    OP_EA(0x2, 0x6F, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10F2")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x206, 1)"), scpexpr(EXPR_END)), "loc_108B")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #17
        "Found \x1F\x06\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1FA0)
    Jump("loc_10EF")

    label("loc_108B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #18
        (
            "Found \x1F\x06\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x06\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)

    label("loc_10EF")

    Jump("loc_1155")

    label("loc_10F2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #19
        (
            "\x07\x05Someone's robbed this chest blind. Not to\x01",
            "worry. You're on the case.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1155")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_101A end

    def Function_9_1163(): pass

    label("Function_9_1163")

    OP_EA(0x2, 0x70, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_123B")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x7, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_11D4")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #20
        "Found \x1F\xFB\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1FA1)
    Jump("loc_1238")

    label("loc_11D4")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #21
        (
            "Found \x1F\xFB\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFB\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x7, 60)
    OP_70(0x7, 0x0)

    label("loc_1238")

    Jump("loc_12BA")

    label("loc_123B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #22
        (
            "\x07\x05The chest is empty, but you briefly consider\x01",
            "taking it along with you and selling it to\x01",
            "someone.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_12BA")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_1163 end

    def Function_10_12C8(): pass

    label("Function_10_12C8")

    OP_EA(0x2, 0x71, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13A0")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x8, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x12F, 1)"), scpexpr(EXPR_END)), "loc_1339")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #23
        "Found \x1F\x2F\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1FA2)
    Jump("loc_139D")

    label("loc_1339")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #24
        (
            "Found \x1F\x2F\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x2F\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x8, 60)
    OP_70(0x8, 0x0)

    label("loc_139D")

    Jump("loc_1430")

    label("loc_13A0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #25
        (
            "\x07\x05As you look into the woodgrain of the empty\x01",
            "chest, you wonder how many chests could be\x01",
            "made out of a single tree.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1430")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_12C8 end

    def Function_11_143E(): pass

    label("Function_11_143E")

    OP_EA(0x2, 0x72, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F4, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1516")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x9, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F7, 1)"), scpexpr(EXPR_END)), "loc_14AF")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #26
        "Found \x1F\xF7\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1FA3)
    Jump("loc_1513")

    label("loc_14AF")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #27
        (
            "Found \x1F\xF7\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xF7\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x9, 60)
    OP_70(0x9, 0x0)

    label("loc_1513")

    Jump("loc_1576")

    label("loc_1516")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #28
        (
            "\x07\x05This chest is empty...or is that just what it wants\x01",
            "you to think?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1576")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_11_143E end

    def Function_12_1584(): pass

    label("Function_12_1584")

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
    SetMapFlags(0x1)
    EventEnd(0x2)
    Return()

    # Function_12_1584 end

    def Function_13_1684(): pass

    label("Function_13_1684")

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

    # Function_13_1684 end

    def Function_14_16FC(): pass

    label("Function_14_16FC")

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
    SetMapFlags(0x1)
    EventEnd(0x2)
    Return()

    # Function_14_16FC end

    def Function_15_17FC(): pass

    label("Function_15_17FC")

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

    # Function_15_17FC end

    def Function_16_1874(): pass

    label("Function_16_1874")

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
    SetMapFlags(0x1)
    EventEnd(0x2)
    Return()

    # Function_16_1874 end

    def Function_17_1974(): pass

    label("Function_17_1974")

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

    # Function_17_1974 end

    def Function_18_19EC(): pass

    label("Function_18_19EC")

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
    SetMapFlags(0x1)
    EventEnd(0x2)
    Return()

    # Function_18_19EC end

    def Function_19_1AFE(): pass

    label("Function_19_1AFE")

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

    # Function_19_1AFE end

    def Function_20_1B7F(): pass

    label("Function_20_1B7F")

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
    SetMapFlags(0x1)
    EventEnd(0x2)
    Return()

    # Function_20_1B7F end

    def Function_21_1C91(): pass

    label("Function_21_1C91")

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

    # Function_21_1C91 end

    def Function_22_1D12(): pass

    label("Function_22_1D12")

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
    SetMapFlags(0x1)
    EventEnd(0x2)
    Return()

    # Function_22_1D12 end

    def Function_23_1E24(): pass

    label("Function_23_1E24")

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

    # Function_23_1E24 end

    def Function_24_1EA5(): pass

    label("Function_24_1EA5")

    PlayEffect(0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Return()

    # Function_24_1EA5 end

    def Function_25_1F84(): pass

    label("Function_25_1F84")

    PlayEffect(0x1, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Return()

    # Function_25_1F84 end

    def Function_26_2063(): pass

    label("Function_26_2063")


    def lambda_2069():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2069)

    def lambda_207B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_207B)

    def lambda_208D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_208D)

    def lambda_209F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_209F)
    Sleep(2500)
    Return()

    # Function_26_2063 end

    def Function_27_20B1(): pass

    label("Function_27_20B1")


    def lambda_20B7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_20B7)

    def lambda_20C9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_20C9)

    def lambda_20DB():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_20DB)

    def lambda_20ED():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_20ED)
    Sleep(2000)
    Return()

    # Function_27_20B1 end

    SaveToFile()

Try(main)
