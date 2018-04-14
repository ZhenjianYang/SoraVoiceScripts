from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 洛连特

    CreateScenaFile(
        FileName            = 'C0704   ._SN',
        MapName             = 'Rolent',
        Location            = 'C0704.x',
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
        'ED6_DT29/CH12590 ._CH',             # 00
        'ED6_DT29/CH12591 ._CH',             # 01
        'ED6_DT29/CH12600 ._CH',             # 02
        'ED6_DT29/CH12601 ._CH',             # 03
        'ED6_DT29/CH12610 ._CH',             # 04
        'ED6_DT29/CH12611 ._CH',             # 05
        'ED6_DT29/CH12620 ._CH',             # 06
        'ED6_DT29/CH12621 ._CH',             # 07
        'ED6_DT29/CH12630 ._CH',             # 08
        'ED6_DT29/CH12631 ._CH',             # 09
        'ED6_DT29/CH12640 ._CH',             # 0A
        'ED6_DT29/CH12641 ._CH',             # 0B
    )

    AddCharChipPat(
        'ED6_DT29/CH12590P._CP',             # 00
        'ED6_DT29/CH12591P._CP',             # 01
        'ED6_DT29/CH12600P._CP',             # 02
        'ED6_DT29/CH12601P._CP',             # 03
        'ED6_DT29/CH12610P._CP',             # 04
        'ED6_DT29/CH12611P._CP',             # 05
        'ED6_DT29/CH12620P._CP',             # 06
        'ED6_DT29/CH12621P._CP',             # 07
        'ED6_DT29/CH12630P._CP',             # 08
        'ED6_DT29/CH12631P._CP',             # 09
        'ED6_DT29/CH12640P._CP',             # 0A
        'ED6_DT29/CH12641P._CP',             # 0B
    )

    DeclMonster(
        X                   = -4220,
        Z                   = 400,
        Y                   = -6080,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3EC,
        Unknown_18          = 8148,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 6080,
        Z                   = 400,
        Y                   = -4800,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3E8,
        Unknown_18          = 8149,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 5440,
        Z                   = 400,
        Y                   = 4640,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3EC,
        Unknown_18          = 8150,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -4850,
        Z                   = 400,
        Y                   = 4550,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3E9,
        Unknown_18          = 8151,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -190,
        Z                   = -4000,
        Y                   = 42600,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3EC,
        Unknown_18          = 8152,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -4670,
        Z                   = -3600,
        Y                   = 37330,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3EA,
        Unknown_18          = 8153,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -4680,
        Z                   = -3600,
        Y                   = 47440,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3EA,
        Unknown_18          = 8154,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 5340,
        Z                   = -3600,
        Y                   = 47490,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3EA,
        Unknown_18          = 8155,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 5120,
        Z                   = -3600,
        Y                   = 37300,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3EA,
        Unknown_18          = 8156,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 21700,
        Z                   = -4050,
        Y                   = 20880,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3EC,
        Unknown_18          = 8157,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -20580,
        TriggerZ            = -15200,
        TriggerY            = 41200,
        TriggerRange        = 1000,
        ActorX              = -19850,
        ActorZ              = -15200,
        ActorY              = 40980,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 48480,
        TriggerZ            = -7600,
        TriggerY            = 5760,
        TriggerRange        = 1000,
        ActorX              = 48450,
        ActorZ              = -7600,
        ActorY              = 6350,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -25120,
        TriggerZ            = -14800,
        TriggerY            = 46340,
        TriggerRange        = 1000,
        ActorX              = -25520,
        ActorZ              = -14800,
        ActorY              = 46750,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -14570,
        TriggerZ            = -14800,
        TriggerY            = 46130,
        TriggerRange        = 1000,
        ActorX              = -14130,
        ActorZ              = -14800,
        ActorY              = 46610,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -14670,
        TriggerZ            = -14800,
        TriggerY            = 35810,
        TriggerRange        = 1000,
        ActorX              = -14270,
        ActorZ              = -14800,
        ActorY              = 35400,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -24890,
        TriggerZ            = -14800,
        TriggerY            = 35860,
        TriggerRange        = 1000,
        ActorX              = -25360,
        ActorZ              = -14800,
        ActorY              = 35390,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 43290,
        TriggerZ            = -7200,
        TriggerY            = 1360,
        TriggerRange        = 1000,
        ActorX              = 42850,
        ActorZ              = -7200,
        ActorY              = 920,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 43470,
        TriggerZ            = -7200,
        TriggerY            = 11820,
        TriggerRange        = 1000,
        ActorX              = 43000,
        ActorZ              = -7200,
        ActorY              = 12160,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 53990,
        TriggerZ            = -7200,
        TriggerY            = 11500,
        TriggerRange        = 1000,
        ActorX              = 54490,
        ActorZ              = -7200,
        ActorY              = 12000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 53690,
        TriggerZ            = -7200,
        TriggerY            = 1320,
        TriggerRange        = 1000,
        ActorX              = 54280,
        ActorZ              = -7200,
        ActorY              = 730,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 26950,
        TriggerZ            = -3600,
        TriggerY            = 26260,
        TriggerRange        = 1000,
        ActorX              = 27410,
        ActorZ              = -3600,
        ActorY              = 26680,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 26820,
        TriggerZ            = -3600,
        TriggerY            = 15820,
        TriggerRange        = 1000,
        ActorX              = 27280,
        ActorZ              = -3600,
        ActorY              = 15350,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 16460,
        TriggerZ            = -3600,
        TriggerY            = 15780,
        TriggerRange        = 1000,
        ActorX              = 16030,
        ActorZ              = -3600,
        ActorY              = 15340,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 16610,
        TriggerZ            = -3600,
        TriggerY            = 26290,
        TriggerRange        = 1000,
        ActorX              = 16140,
        ActorZ              = -3600,
        ActorY              = 26630,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -3930,
        TriggerZ            = 4000,
        TriggerY            = 98030,
        TriggerRange        = 1200,
        ActorX              = -3930,
        ActorZ              = 5200,
        ActorY              = 98030,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 28,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_43E",          # 00, 0
        "Function_1_473",          # 01, 1
        "Function_2_701",          # 02, 2
        "Function_3_818",          # 03, 3
        "Function_4_92F",          # 04, 4
        "Function_5_A46",          # 05, 5
        "Function_6_B42",          # 06, 6
        "Function_7_C59",          # 07, 7
        "Function_8_D70",          # 08, 8
        "Function_9_E87",          # 09, 9
        "Function_10_F83",         # 0A, 10
        "Function_11_109A",        # 0B, 11
        "Function_12_11B1",        # 0C, 12
        "Function_13_12C8",        # 0D, 13
        "Function_14_13DF",        # 0E, 14
        "Function_15_14DB",        # 0F, 15
        "Function_16_15F2",        # 10, 16
        "Function_17_16FF",        # 11, 17
        "Function_18_1780",        # 12, 18
        "Function_19_187B",        # 13, 19
        "Function_20_18F3",        # 14, 20
        "Function_21_19EE",        # 15, 21
        "Function_22_1A66",        # 16, 22
        "Function_23_1B73",        # 17, 23
        "Function_24_1BF4",        # 18, 24
        "Function_25_1CE7",        # 19, 25
        "Function_26_1DDA",        # 1A, 26
        "Function_27_1E28",        # 1B, 27
        "Function_28_1E76",        # 1C, 28
    )


    def Function_0_43E(): pass

    label("Function_0_43E")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_456"),
        (101, "loc_45D"),
        (102, "loc_464"),
        (103, "loc_46B"),
        (SWITCH_DEFAULT, "loc_472"),
    )


    label("loc_456")

    Event(0, 16)
    Jump("loc_472")

    label("loc_45D")

    Event(0, 18)
    Jump("loc_472")

    label("loc_464")

    Event(0, 20)
    Jump("loc_472")

    label("loc_46B")

    Event(0, 22)
    Jump("loc_472")

    label("loc_472")

    Return()

    # Function_0_43E end

    def Function_1_473(): pass

    label("Function_1_473")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_485")
    OP_6F(0x0, 0)
    Jump("loc_48C")

    label("loc_485")

    OP_6F(0x0, 60)

    label("loc_48C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49E")
    OP_6F(0x1, 0)
    Jump("loc_4A5")

    label("loc_49E")

    OP_6F(0x1, 60)

    label("loc_4A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B7")
    OP_6F(0x2, 0)
    Jump("loc_4BE")

    label("loc_4B7")

    OP_6F(0x2, 60)

    label("loc_4BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D0")
    OP_6F(0x3, 0)
    Jump("loc_4D7")

    label("loc_4D0")

    OP_6F(0x3, 60)

    label("loc_4D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E9")
    OP_6F(0x4, 0)
    Jump("loc_4F0")

    label("loc_4E9")

    OP_6F(0x4, 60)

    label("loc_4F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_502")
    OP_6F(0x5, 0)
    Jump("loc_509")

    label("loc_502")

    OP_6F(0x5, 60)

    label("loc_509")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51B")
    OP_6F(0x6, 0)
    Jump("loc_522")

    label("loc_51B")

    OP_6F(0x6, 60)

    label("loc_522")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_534")
    OP_6F(0x7, 0)
    Jump("loc_53B")

    label("loc_534")

    OP_6F(0x7, 60)

    label("loc_53B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54D")
    OP_6F(0x8, 0)
    Jump("loc_554")

    label("loc_54D")

    OP_6F(0x8, 60)

    label("loc_554")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_566")
    OP_6F(0x9, 0)
    Jump("loc_56D")

    label("loc_566")

    OP_6F(0x9, 60)

    label("loc_56D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57F")
    OP_6F(0xA, 0)
    Jump("loc_586")

    label("loc_57F")

    OP_6F(0xA, 60)

    label("loc_586")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_598")
    OP_6F(0xB, 0)
    Jump("loc_59F")

    label("loc_598")

    OP_6F(0xB, 60)

    label("loc_59F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B1")
    OP_6F(0xC, 0)
    Jump("loc_5B8")

    label("loc_5B1")

    OP_6F(0xC, 60)

    label("loc_5B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E3, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CA")
    OP_6F(0xD, 0)
    Jump("loc_5D1")

    label("loc_5CA")

    OP_6F(0xD, 60)

    label("loc_5D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FA, 4)), scpexpr(EXPR_END)), "loc_5DD")
    SetChrFlags(0x8, 0x80)

    label("loc_5DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FA, 5)), scpexpr(EXPR_END)), "loc_5E9")
    SetChrFlags(0x9, 0x80)

    label("loc_5E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FA, 6)), scpexpr(EXPR_END)), "loc_5F5")
    SetChrFlags(0xA, 0x80)

    label("loc_5F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FA, 7)), scpexpr(EXPR_END)), "loc_601")
    SetChrFlags(0xB, 0x80)

    label("loc_601")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FB, 0)), scpexpr(EXPR_END)), "loc_60D")
    SetChrFlags(0xC, 0x80)

    label("loc_60D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FB, 1)), scpexpr(EXPR_END)), "loc_619")
    SetChrFlags(0xD, 0x80)

    label("loc_619")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FB, 2)), scpexpr(EXPR_END)), "loc_625")
    SetChrFlags(0xE, 0x80)

    label("loc_625")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FB, 3)), scpexpr(EXPR_END)), "loc_631")
    SetChrFlags(0xF, 0x80)

    label("loc_631")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FB, 4)), scpexpr(EXPR_END)), "loc_63D")
    SetChrFlags(0x10, 0x80)

    label("loc_63D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FB, 5)), scpexpr(EXPR_END)), "loc_649")
    SetChrFlags(0x11, 0x80)

    label("loc_649")

    OP_51(0xD, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xCF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xCF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xCF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xCF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1B(0x0, 0x0, 0x11)
    OP_1B(0x1, 0x0, 0x13)
    OP_1B(0x2, 0x0, 0x15)
    OP_1B(0x3, 0x0, 0x17)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6F4")
    LoadEffect(0x2, "map\\\\mp027_00.eff")
    PlayEffect(0x2, 0x2, 0xFF, -3930, 5200, 98030, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    OP_71(0x10, 0x20)
    OP_6F(0x10, 0)
    OP_70(0x10, 0xFA)
    Jump("loc_700")

    label("loc_6F4")

    OP_72(0x10, 0x20)
    OP_6F(0x10, 250)

    label("loc_700")

    Return()

    # Function_1_473 end

    def Function_2_701(): pass

    label("Function_2_701")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D9")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x187, 1)"), scpexpr(EXPR_END)), "loc_770")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x87\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F10)
    Jump("loc_7D6")

    label("loc_770")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\x87\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x87\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_7D6")

    Jump("loc_80A")

    label("loc_7D9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_80A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_701 end

    def Function_3_818(): pass

    label("Function_3_818")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8F0")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x17D, 1)"), scpexpr(EXPR_END)), "loc_887")
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
    OP_A2(0x1F12)
    Jump("loc_8ED")

    label("loc_887")

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

    label("loc_8ED")

    Jump("loc_921")

    label("loc_8F0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_921")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_818 end

    def Function_4_92F(): pass

    label("Function_4_92F")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A07")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_99E")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x00得到了\x1F\xFC\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F14)
    Jump("loc_A04")

    label("loc_99E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "宝箱里装有\x1F\xFC\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFC\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_A04")

    Jump("loc_A38")

    label("loc_A07")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_A38")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_92F end

    def Function_5_A46(): pass

    label("Function_5_A46")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B16")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x1E)
    OP_73(0x3)
    OP_6F(0x3, 30)
    AddSepith(0x3, 0x12C)
    AddSepith(0x4, 0x64)
    AddSepith(0x5, 0x64)
    AddSepith(0x6, 0x64)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #9
        (
            "\x07\x00得到了\x07\x02#59I风之耀晶片×３００\x01",
            "\x07\x02#62I时之耀晶片×１００\x01",
            "\x07\x02#60I空之耀晶片×１００\x01",
            "\x07\x02#61I幻之耀晶片×１００\x01",
            "\x07\x00。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x1F15)
    Jump("loc_B30")

    label("loc_B16")


    AnonymousTalk(    #10
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_B30")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_A46 end

    def Function_6_B42(): pass

    label("Function_6_B42")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C1A")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_BB1")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x00得到了\x1F\xFB\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F16)
    Jump("loc_C17")

    label("loc_BB1")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #12
        (
            "宝箱里装有\x1F\xFB\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFB\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_C17")

    Jump("loc_C4B")

    label("loc_C1A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_C4B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_B42 end

    def Function_7_C59(): pass

    label("Function_7_C59")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D31")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_CC8")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #14
        "\x07\x00得到了\x1F\xFE\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F17)
    Jump("loc_D2E")

    label("loc_CC8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #15
        (
            "宝箱里装有\x1F\xFE\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFE\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)

    label("loc_D2E")

    Jump("loc_D62")

    label("loc_D31")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #16
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_D62")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_C59 end

    def Function_8_D70(): pass

    label("Function_8_D70")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E48")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F7, 1)"), scpexpr(EXPR_END)), "loc_DDF")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #17
        "\x07\x00得到了\x1F\xF7\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F18)
    Jump("loc_E45")

    label("loc_DDF")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #18
        (
            "宝箱里装有\x1F\xF7\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xF7\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)

    label("loc_E45")

    Jump("loc_E79")

    label("loc_E48")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #19
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_E79")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_D70 end

    def Function_9_E87(): pass

    label("Function_9_E87")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F57")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x7, 0x1E)
    OP_73(0x7)
    OP_6F(0x7, 30)
    AddSepith(0x3, 0x12C)
    AddSepith(0x4, 0x64)
    AddSepith(0x5, 0x64)
    AddSepith(0x6, 0x64)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #20
        (
            "\x07\x00得到了\x07\x02#59I风之耀晶片×３００\x01",
            "\x07\x02#62I时之耀晶片×１００\x01",
            "\x07\x02#60I空之耀晶片×１００\x01",
            "\x07\x02#61I幻之耀晶片×１００\x01",
            "\x07\x00。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x1F19)
    Jump("loc_F71")

    label("loc_F57")


    AnonymousTalk(    #21
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_F71")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_E87 end

    def Function_10_F83(): pass

    label("Function_10_F83")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_105B")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x8, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_FF2")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #22
        "\x07\x00得到了\x1F\xFD\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F1A)
    Jump("loc_1058")

    label("loc_FF2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #23
        (
            "宝箱里装有\x1F\xFD\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFD\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x8, 60)
    OP_70(0x8, 0x0)

    label("loc_1058")

    Jump("loc_108C")

    label("loc_105B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #24
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_108C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_F83 end

    def Function_11_109A(): pass

    label("Function_11_109A")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1172")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x9, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x202, 1)"), scpexpr(EXPR_END)), "loc_1109")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #25
        "\x07\x00得到了\x1F\x02\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F1B)
    Jump("loc_116F")

    label("loc_1109")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #26
        (
            "宝箱里装有\x1F\x02\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x02\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x9, 60)
    OP_70(0x9, 0x0)

    label("loc_116F")

    Jump("loc_11A3")

    label("loc_1172")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #27
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_11A3")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_11_109A end

    def Function_12_11B1(): pass

    label("Function_12_11B1")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1289")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xA, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0xA8, 1)"), scpexpr(EXPR_END)), "loc_1220")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #28
        "\x07\x00得到了\x1F\xA8\x00\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F1C)
    Jump("loc_1286")

    label("loc_1220")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #29
        (
            "宝箱里装有\x1F\xA8\x00\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xA8\x00\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xA, 60)
    OP_70(0xA, 0x0)

    label("loc_1286")

    Jump("loc_12BA")

    label("loc_1289")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #30
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_12BA")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_12_11B1 end

    def Function_13_12C8(): pass

    label("Function_13_12C8")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13A0")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xB, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FA, 1)"), scpexpr(EXPR_END)), "loc_1337")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #31
        "\x07\x00得到了\x1F\xFA\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F1D)
    Jump("loc_139D")

    label("loc_1337")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #32
        (
            "宝箱里装有\x1F\xFA\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFA\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xB, 60)
    OP_70(0xB, 0x0)

    label("loc_139D")

    Jump("loc_13D1")

    label("loc_13A0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #33
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_13D1")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_13_12C8 end

    def Function_14_13DF(): pass

    label("Function_14_13DF")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14AF")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xC, 0x1E)
    OP_73(0xC)
    OP_6F(0xC, 30)
    AddSepith(0x3, 0x12C)
    AddSepith(0x4, 0x64)
    AddSepith(0x5, 0x64)
    AddSepith(0x6, 0x64)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #34
        (
            "\x07\x00得到了\x07\x02#59I风之耀晶片×３００\x01",
            "\x07\x02#62I时之耀晶片×１００\x01",
            "\x07\x02#60I空之耀晶片×１００\x01",
            "\x07\x02#61I幻之耀晶片×１００\x01",
            "\x07\x00。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x1F1E)
    Jump("loc_14C9")

    label("loc_14AF")


    AnonymousTalk(    #35
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_14C9")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_14_13DF end

    def Function_15_14DB(): pass

    label("Function_15_14DB")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E3, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15B3")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xD, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FF, 1)"), scpexpr(EXPR_END)), "loc_154A")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #36
        "\x07\x00得到了\x1F\xFF\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F1F)
    Jump("loc_15B0")

    label("loc_154A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #37
        (
            "宝箱里装有\x1F\xFF\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFF\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xD, 60)
    OP_70(0xD, 0x0)

    label("loc_15B0")

    Jump("loc_15E4")

    label("loc_15B3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #38
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_15E4")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_15_14DB end

    def Function_16_15F2(): pass

    label("Function_16_15F2")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(0, 250, -82450, 0)
    OP_6C(225000, 0)
    SetChrPos(0x101, -500, 250, -82000, 0)
    SetChrPos(0x102, 500, 250, -82000, 0)
    SetChrPos(0xF8, -500, 250, -83000, 0)
    SetChrPos(0xF9, 500, 250, -83000, 0)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Call(0, 24)
    Call(0, 26)
    Fade(500)
    OP_6D(-20, -50, -78290, 0)
    OP_6C(315000, 0)
    SetChrPos(0x0, -20, -50, -78290, 0)
    SetChrPos(0x1, -20, -50, -78290, 0)
    SetChrPos(0x2, -20, -50, -78290, 0)
    SetChrPos(0x3, -20, -50, -78290, 0)
    EventEnd(0x0)
    Return()

    # Function_16_15F2 end

    def Function_17_16FF(): pass

    label("Function_17_16FF")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(0, 250, -82450, 0)
    OP_6C(225000, 0)
    SetChrPos(0x101, 500, 250, -83000, 180)
    SetChrPos(0x102, -500, 250, -83000, 180)
    SetChrPos(0xF8, 500, 250, -82000, 180)
    SetChrPos(0xF9, -500, 250, -82000, 180)
    OP_0D()
    Call(0, 24)
    Call(0, 27)
    NewScene("ED6_DT21/C0703   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_17_16FF end

    def Function_18_1780(): pass

    label("Function_18_1780")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(0, 3850, 105000, 0)
    SetChrPos(0x101, 500, 3850, 104500, 180)
    SetChrPos(0x102, -500, 3850, 104500, 180)
    SetChrPos(0xF8, 500, 3850, 105500, 180)
    SetChrPos(0xF9, -500, 3850, 105500, 180)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Call(0, 25)
    Call(0, 26)
    Fade(500)
    OP_6D(70, 3890, 102320, 0)
    SetChrPos(0x0, 70, 3890, 102320, 180)
    SetChrPos(0x1, 70, 3890, 102320, 180)
    SetChrPos(0x2, 70, 3890, 102320, 180)
    SetChrPos(0x3, 70, 3890, 102320, 180)
    EventEnd(0x0)
    Return()

    # Function_18_1780 end

    def Function_19_187B(): pass

    label("Function_19_187B")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(0, 3850, 105000, 0)
    SetChrPos(0x101, -500, 3850, 105500, 0)
    SetChrPos(0x102, 500, 3850, 105500, 0)
    SetChrPos(0xF8, -500, 3850, 104500, 0)
    SetChrPos(0xF9, 500, 3850, 104500, 0)
    OP_0D()
    Call(0, 24)
    Call(0, 27)
    NewScene("ED6_DT21/C0705   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_19_187B end

    def Function_20_18F3(): pass

    label("Function_20_18F3")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(16000, -3750, -15500, 0)
    SetChrPos(0x101, 16500, -3750, -15000, 90)
    SetChrPos(0x102, 16500, -3750, -16000, 90)
    SetChrPos(0xF8, 15500, -3750, -15000, 90)
    SetChrPos(0xF9, 15500, -3750, -16000, 90)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Call(0, 24)
    Call(0, 26)
    Fade(500)
    OP_6D(18870, -3700, -15430, 0)
    SetChrPos(0x0, 18870, -3700, -15430, 90)
    SetChrPos(0x1, 18870, -3700, -15430, 90)
    SetChrPos(0x2, 18870, -3700, -15430, 90)
    SetChrPos(0x3, 18870, -3700, -15430, 90)
    EventEnd(0x0)
    Return()

    # Function_20_18F3 end

    def Function_21_19EE(): pass

    label("Function_21_19EE")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(16000, -3750, -15500, 0)
    SetChrPos(0x101, 15500, -3750, -16000, 270)
    SetChrPos(0x102, 15500, -3750, -15000, 270)
    SetChrPos(0xF8, 16500, -3750, -16000, 270)
    SetChrPos(0xF9, 16500, -3750, -15000, 270)
    OP_0D()
    Call(0, 24)
    Call(0, 27)
    NewScene("ED6_DT21/C0703   ._SN", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_21_19EE end

    def Function_22_1A66(): pass

    label("Function_22_1A66")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-17300, -3750, 14900, 0)
    OP_6C(45000, 0)
    SetChrPos(0x101, -17800, -3750, 14400, 270)
    SetChrPos(0x102, -17800, -3750, 15400, 270)
    SetChrPos(0xF8, -16800, -3750, 14400, 270)
    SetChrPos(0xF9, -16800, -3750, 15400, 270)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Call(0, 24)
    Call(0, 26)
    Fade(500)
    OP_6D(-21080, -3890, 14900, 0)
    OP_6C(315000, 0)
    SetChrPos(0x0, -21080, -3890, 14900, 270)
    SetChrPos(0x1, -21080, -3890, 14900, 270)
    SetChrPos(0x2, -21080, -3890, 14900, 270)
    SetChrPos(0x3, -21080, -3890, 14900, 270)
    EventEnd(0x0)
    Return()

    # Function_22_1A66 end

    def Function_23_1B73(): pass

    label("Function_23_1B73")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(-17300, -3750, 14900, 0)
    OP_6C(45000, 0)
    SetChrPos(0x101, -16800, -3750, 15400, 90)
    SetChrPos(0x102, -16800, -3750, 14400, 90)
    SetChrPos(0xF8, -17800, -3750, 15400, 90)
    SetChrPos(0xF9, -17800, -3750, 14400, 90)
    OP_0D()
    Call(0, 24)
    Call(0, 27)
    NewScene("ED6_DT21/C0703   ._SN", 105, 0, 0)
    IdleLoop()
    Return()

    # Function_23_1B73 end

    def Function_24_1BF4(): pass

    label("Function_24_1BF4")

    LoadEffect(0x0, "map\\\\mp049_21.eff")
    PlayEffect(0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Return()

    # Function_24_1BF4 end

    def Function_25_1CE7(): pass

    label("Function_25_1CE7")

    LoadEffect(0x0, "map\\\\mp049_22.eff")
    PlayEffect(0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Return()

    # Function_25_1CE7 end

    def Function_26_1DDA(): pass

    label("Function_26_1DDA")


    def lambda_1DE0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1DE0)

    def lambda_1DF2():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1DF2)

    def lambda_1E04():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1E04)

    def lambda_1E16():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1E16)
    Sleep(2500)
    Return()

    # Function_26_1DDA end

    def Function_27_1E28(): pass

    label("Function_27_1E28")


    def lambda_1E2E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1E2E)

    def lambda_1E40():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1E40)

    def lambda_1E52():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1E52)

    def lambda_1E64():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1E64)
    Sleep(2000)
    Return()

    # Function_27_1E28 end

    def Function_28_1E76(): pass

    label("Function_28_1E76")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EC9")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #39
        "\x07\x05好像是导力停止了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Jump("loc_206E")

    label("loc_1EC9")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #40
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2053")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_72(0x10, 0x20)
    OP_6F(0x10, 300)
    OP_70(0x10, 0x1F4)
    OP_73(0x10)
    OP_6F(0x10, 500)
    OP_70(0x10, 0x2BC)
    OP_71(0x10, 0x20)
    OP_20(0xBB8)
    OP_22(0xC, 0x0, 0x64)
    OP_82(0x2, 0x2)
    LoadEffect(0x3, "map\\\\mp027_01.eff")
    PlayEffect(0x3, 0x3, 0xFF, -3930, 5200, 98030, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    FadeToDark(1500, 0, -1)
    Sleep(1500)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0xFF, 0xFE, 0x0)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_82(0x3, 0x2)
    PlayEffect(0x2, 0x2, 0xFF, -3930, 5200, 98030, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    OP_6F(0x10, 0)
    OP_70(0x10, 0xFA)
    OP_1E()
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_2053")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_206D")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_206D")

    Return()

    label("loc_206E")

    Return()

    # Function_28_1E76 end

    SaveToFile()

Try(main)
