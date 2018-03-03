from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M7102   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7102.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60222",
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Gremlin',                              # 9
        'Gremlin',                              # 10
        'Gremlin',                              # 11
        'Gremlin',                              # 12
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
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT29/CH14460 ._CH',             # 00
        'ED6_DT29/CH14461 ._CH',             # 01
        'ED6_DT29/CH14910 ._CH',             # 02
        'ED6_DT29/CH14911 ._CH',             # 03
        'ED6_DT29/CH14920 ._CH',             # 04
        'ED6_DT29/CH14921 ._CH',             # 05
        'ED6_DT29/CH14930 ._CH',             # 06
        'ED6_DT29/CH14931 ._CH',             # 07
        'ED6_DT29/CH15040 ._CH',             # 08
        'ED6_DT29/CH15040 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT29/CH14460P._CP',             # 00
        'ED6_DT29/CH14461P._CP',             # 01
        'ED6_DT29/CH14910P._CP',             # 02
        'ED6_DT29/CH14911P._CP',             # 03
        'ED6_DT29/CH14920P._CP',             # 04
        'ED6_DT29/CH14921P._CP',             # 05
        'ED6_DT29/CH14930P._CP',             # 06
        'ED6_DT29/CH14931P._CP',             # 07
        'ED6_DT29/CH15040P._CP',             # 08
        'ED6_DT29/CH15040P._CP',             # 09
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 25890,
        Z                   = -2000,
        Y                   = -81580,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x12C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 50170,
        Z                   = -2000,
        Y                   = -81490,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x12D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -42110,
        Z                   = -2000,
        Y                   = -81730,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x12E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -59850,
        Z                   = 2000,
        Y                   = -47910,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x12F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -41860,
        Z                   = 6000,
        Y                   = -13920,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x130,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -7930,
        Z                   = 10000,
        Y                   = -13990,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x12C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 36280,
        Z                   = 18000,
        Y                   = -41800,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x12D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 65910,
        Z                   = 18000,
        Y                   = -42040,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x12E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 58100,
        Z                   = 26000,
        Y                   = 8150,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x12F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 24050,
        Z                   = 30000,
        Y                   = 15580,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x130,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -9710,
        Z                   = 26000,
        Y                   = 43910,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x12C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -43850,
        Z                   = 30000,
        Y                   = 15930,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x12D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 23800,
        TriggerZ            = 30000,
        TriggerY            = 46230,
        TriggerRange        = 1000,
        ActorX              = 24000,
        ActorZ              = 33000,
        ActorY              = 48000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 18,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 60000,
        TriggerZ            = -2000,
        TriggerY            = -81500,
        TriggerRange        = 1000,
        ActorX              = 60000,
        ActorZ              = -1000,
        ActorY              = -81500,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 21,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -19000,
        TriggerZ            = 18000,
        TriggerY            = -42000,
        TriggerRange        = 1000,
        ActorX              = -19000,
        ActorZ              = 19000,
        ActorY              = -42000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 22,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 10000,
        TriggerZ            = 10000,
        TriggerY            = 7500,
        TriggerRange        = 1000,
        ActorX              = 10000,
        ActorZ              = 11000,
        ActorY              = 7500,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 23,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -83500,
        TriggerZ            = 30000,
        TriggerY            = 15800,
        TriggerRange        = 1000,
        ActorX              = -83500,
        ActorZ              = 31000,
        ActorY              = 15800,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 24,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -19000,
        TriggerZ            = 18000,
        TriggerY            = -40000,
        TriggerRange        = 1000,
        ActorX              = -19000,
        ActorZ              = 19000,
        ActorY              = -40000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 25,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -19000,
        TriggerZ            = 18000,
        TriggerY            = -44000,
        TriggerRange        = 1000,
        ActorX              = -19000,
        ActorZ              = 19000,
        ActorY              = -44000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 26,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -83500,
        TriggerZ            = 30000,
        TriggerY            = 13800,
        TriggerRange        = 1000,
        ActorX              = -83500,
        ActorZ              = 31000,
        ActorY              = 13800,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 27,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -83500,
        TriggerZ            = 30000,
        TriggerY            = 17800,
        TriggerRange        = 1000,
        ActorX              = -83500,
        ActorZ              = 31000,
        ActorY              = 17800,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 28,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -43800,
        TriggerZ            = 34000,
        TriggerY            = 72000,
        TriggerRange        = 1000,
        ActorX              = -43800,
        ActorZ              = 35000,
        ActorY              = 72000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 29,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_432",          # 00, 0
        "Function_1_484",          # 01, 1
        "Function_2_5D4",          # 02, 2
        "Function_3_5DD",          # 03, 3
        "Function_4_E8C",          # 04, 4
        "Function_5_16C4",         # 05, 5
        "Function_6_172C",         # 06, 6
        "Function_7_1794",         # 07, 7
        "Function_8_17FC",         # 08, 8
        "Function_9_1864",         # 09, 9
        "Function_10_1890",        # 0A, 10
        "Function_11_18C1",        # 0B, 11
        "Function_12_18F2",        # 0C, 12
        "Function_13_1923",        # 0D, 13
        "Function_14_1A01",        # 0E, 14
        "Function_15_1ABD",        # 0F, 15
        "Function_16_1BD3",        # 10, 16
        "Function_17_1C21",        # 11, 17
        "Function_18_1C7A",        # 12, 18
        "Function_19_1E1B",        # 13, 19
        "Function_20_1ED1",        # 14, 20
        "Function_21_1F7C",        # 15, 21
        "Function_22_20C0",        # 16, 22
        "Function_23_2161",        # 17, 23
        "Function_24_22A9",        # 18, 24
        "Function_25_2352",        # 19, 25
        "Function_26_252A",        # 1A, 26
        "Function_27_272B",        # 1B, 27
        "Function_28_27D1",        # 1C, 28
        "Function_29_295E",        # 1D, 29
    )


    def Function_0_432(): pass

    label("Function_0_432")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_448")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    Event(0, 20)
    Jump("loc_464")

    label("loc_448")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_464")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)

    label("loc_464")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_483")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (101, "loc_47C"),
        (SWITCH_DEFAULT, "loc_483"),
    )


    label("loc_47C")

    Event(0, 13)
    Jump("loc_483")

    label("loc_483")

    Return()

    # Function_0_432 end

    def Function_1_484(): pass

    label("Function_1_484")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFDAA58, 0x230085)
    OP_1B(0x1, 0x0, 0xE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B3")
    OP_72(0x1000, 0x0)
    ExitThread()
    OP_10(0x0, 0x0)
    Jump("loc_4C6")

    label("loc_4B3")

    OP_72(0x1000, 0x0)
    ExitThread()
    OP_6F(0x0, 120)
    OP_72(0x800, 0x0)
    ExitThread()

    label("loc_4C6")

    OP_51(0x17, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1C, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_82(0x82, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_4EF")
    OP_82(0x83, 0x0)
    Jump("loc_4F2")

    label("loc_4EF")

    OP_82(0x84, 0x0)

    label("loc_4F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x514, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_504")
    OP_6F(0x2, 0)
    Jump("loc_50B")

    label("loc_504")

    OP_6F(0x2, 60)

    label("loc_50B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x514, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51D")
    OP_6F(0x3, 0)
    Jump("loc_524")

    label("loc_51D")

    OP_6F(0x3, 60)

    label("loc_524")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x514, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_536")
    OP_6F(0x4, 0)
    Jump("loc_53D")

    label("loc_536")

    OP_6F(0x4, 60)

    label("loc_53D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x514, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54F")
    OP_6F(0x5, 0)
    Jump("loc_556")

    label("loc_54F")

    OP_6F(0x5, 60)

    label("loc_556")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x514, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_568")
    OP_6F(0x6, 0)
    Jump("loc_56F")

    label("loc_568")

    OP_6F(0x6, 60)

    label("loc_56F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x514, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_581")
    OP_6F(0x7, 0)
    Jump("loc_588")

    label("loc_581")

    OP_6F(0x7, 60)

    label("loc_588")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x514, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59A")
    OP_6F(0x8, 0)
    Jump("loc_5A1")

    label("loc_59A")

    OP_6F(0x8, 60)

    label("loc_5A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x514, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B3")
    OP_6F(0x9, 0)
    Jump("loc_5BA")

    label("loc_5B3")

    OP_6F(0x9, 60)

    label("loc_5BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x515, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CC")
    OP_6F(0xA, 0)
    Jump("loc_5D3")

    label("loc_5CC")

    OP_6F(0xA, 60)

    label("loc_5D3")

    Return()

    # Function_1_484 end

    def Function_2_5D4(): pass

    label("Function_2_5D4")

    Call(0, 3)
    Call(0, 4)
    Return()

    # Function_2_5D4 end

    def Function_3_5DD(): pass

    label("Function_3_5DD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_AA(65282)
    LoadEffect(0x0, "map\\mp250_00.eff")
    LoadEffect(0x1, "map\\mp250_01.eff")
    OP_E0(238, 0x4A, 0x2)
    OP_E0(239, 0x4B, 0x2)
    OP_E0(240, 0x4C, 0x2)
    OP_E0(241, 0x4D, 0x2)
    SetChrPos(0xEE, -7700, -6000, -105370, 0)
    SetChrPos(0xEF, -7450, -6000, -105440, 0)
    SetChrPos(0xF0, -8430, -6000, -105530, 0)
    SetChrPos(0xF1, -8430, -6000, -105530, 0)
    OP_9F(0xEE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xEF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xF0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xF1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6F(0x0, 120)
    OP_6D(-6190, -4700, -105310, 0)
    OP_67(0, 6440, -10000, 0)
    OP_6B(3800, 0)
    OP_6C(140000, 0)
    OP_6E(243, 0)

    def lambda_6E2():
        OP_6B(4500, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_6E2)
    FadeToBright(2000, 0)
    OP_0D()
    OP_43(0xEE, 0x0, 0x0, 0x9)
    OP_43(0xEF, 0x0, 0x0, 0xA)
    OP_43(0xF0, 0x0, 0x0, 0xB)
    OP_43(0xF1, 0x0, 0x0, 0xC)
    Sleep(2000)
    OP_22(0x6C, 0x0, 0x64)
    OP_B0(0x0, 0x1E)
    OP_6F(0x0, 120)
    OP_70(0x0, 0x0)
    Sleep(300)
    Fade(1000)
    OP_6D(-4660, -8050, -86460, 0)
    OP_67(0, 3490, -10000, 0)
    OP_6B(5150, 0)
    OP_6C(42000, 0)
    OP_6E(543, 0)

    def lambda_77B():
        OP_6D(-7460, 1650, -85660, 7000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_77B)

    def lambda_793():
        OP_67(0, 1340, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_793)

    def lambda_7AB():
        OP_6B(6150, 7000)
        ExitThread()

    QueueWorkItem(0xEF, 2, lambda_7AB)

    def lambda_7BB():
        OP_6C(42000, 7000)
        ExitThread()

    QueueWorkItem(0xEF, 3, lambda_7BB)

    def lambda_7CB():
        OP_6E(569, 7000)
        ExitThread()

    QueueWorkItem(0xF0, 2, lambda_7CB)
    StopSound(0x20B70, 0x5BCC0, 0x0)
    OP_C8(0x200, 0x46, "C_PLAC32._CH", 0x1, 0x3E8)
    OP_73(0x0)
    OP_22(0x9A, 0x0, 0x64)
    OP_23(0x6C)
    WaitChrThread(0x109, 0x2)
    Fade(500)
    OP_6D(-7720, -6000, -82450, 0)
    OP_67(0, 7910, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(44000, 0)
    OP_6E(298, 0)
    StopSound(0xEE48, 0x30D40, 0x0)
    OP_0D()
    Sleep(300)
    OP_20(0x3E8)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x0, 0xFF, -12500, -5900, -81310, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x1, 0xFF, -9470, -5900, -79940, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x2, 0xFF, -6880, -5900, -80270, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x3, 0xFF, -4410, -5900, -82380, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_981")
    OP_62(0xEE, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_9E8")

    label("loc_981")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9A9")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_9E8")

    label("loc_9A9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9D1")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_9E8")

    label("loc_9D1")

    OP_62(0xEE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_9E8")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A15")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_A7C")

    label("loc_A15")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A3D")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_A7C")

    label("loc_A3D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A65")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_A7C")

    label("loc_A65")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_A7C")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AA9")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B10")

    label("loc_AA9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AD1")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B10")

    label("loc_AD1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AF9")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B10")

    label("loc_AF9")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_B10")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B3D")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_BA4")

    label("loc_B3D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B65")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_BA4")

    label("loc_B65")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B8D")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_BA4")

    label("loc_B8D")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_BA4")

    Sleep(1000)
    OP_1D(0x97)

    ChrTalk(    #0
        0x109,
        "#1063F#6PHere we go again...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BF0")

    ChrTalk(    #1
        0x107,
        "#065F#6PAck!\x02",
    )

    CloseMessageWindow()
    Jump("loc_C98")

    label("loc_BF0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C1F")

    ChrTalk(    #2
        0x10B,
        "#216F#6PWh-What the...?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_C98")

    label("loc_C1F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C45")

    ChrTalk(    #3
        0x105,
        "#1162F#6PUgh...\x02",
    )

    CloseMessageWindow()
    Jump("loc_C98")

    label("loc_C45")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C6C")

    ChrTalk(    #4
        0x10D,
        "#270F#6PTo arms!\x02",
    )

    CloseMessageWindow()
    Jump("loc_C98")

    label("loc_C6C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C98")

    ChrTalk(    #5
        0x10E,
        "#172F#6PNo time to rest!\x02",
    )

    CloseMessageWindow()

    label("loc_C98")

    Fade(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 10)
    SetChrSubChip(0x109, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xEF, 11)
    SetChrSubChip(0xEF, 0)
    Sleep(80)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xF0, 12)
    SetChrSubChip(0xF0, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xF1, 13)
    SetChrSubChip(0xF1, 0)
    OP_0D()
    Sleep(300)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x10, -12500, -8000, -81310, 135)
    SetChrPos(0x11, -9470, -8000, -79940, 180)
    SetChrPos(0x12, -6880, -8000, -80270, 180)
    SetChrPos(0x13, -4410, -8000, -82380, 225)
    OP_22(0x85, 0x1, 0x64)
    OP_43(0x10, 0x0, 0x0, 0x5)
    Sleep(100)
    OP_43(0x13, 0x0, 0x0, 0x8)
    Sleep(100)
    OP_43(0x12, 0x0, 0x0, 0x7)
    Sleep(100)
    OP_43(0x11, 0x0, 0x0, 0x6)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x12, 0x0)
    WaitChrThread(0x13, 0x0)
    OP_23(0x85)
    Sleep(1000)

    def lambda_DA6():
        OP_6D(-7480, -6000, -83240, 300)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_DA6)

    def lambda_DBE():
        OP_67(0, 7850, -10000, 300)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_DBE)

    def lambda_DD6():
        OP_6B(2000, 300)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_DD6)
    SetChrChipByIndex(0x10, 1)

    def lambda_DEB():
        OP_8F(0xFE, 0xFFFFD9B8, 0xFFFFE890, 0xFFFEB61E, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_DEB)
    Sleep(20)
    SetChrChipByIndex(0x12, 1)

    def lambda_E10():
        OP_8F(0xFE, 0xFFFFE462, 0xFFFFE890, 0xFFFEB9AC, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_E10)
    Sleep(20)
    SetChrChipByIndex(0x11, 1)

    def lambda_E35():
        OP_8F(0xFE, 0xFFFFDDE6, 0xFFFFE890, 0xFFFEB984, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_E35)
    Sleep(20)
    SetChrChipByIndex(0x13, 1)

    def lambda_E5A():
        OP_8F(0xFE, 0xFFFFE638, 0xFFFFE890, 0xFFFEB4CA, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_E5A)
    WaitChrThread(0x109, 0x1)
    WaitChrThread(0x109, 0x2)
    WaitChrThread(0x109, 0x3)
    Battle(0x13E, 0x0, 0x0, 0x0, 0xFF)
    Return()

    # Function_3_5DD end

    def Function_4_E8C(): pass

    label("Function_4_E8C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10)
    OP_44(0x10, 0x0)
    OP_44(0x11, 0x0)
    OP_44(0x12, 0x0)
    OP_44(0x13, 0x0)
    OP_E0(238, 0x4A, 0x2)
    OP_E0(239, 0x4B, 0x2)
    OP_E0(240, 0x4C, 0x2)
    OP_E0(241, 0x4D, 0x2)
    SetChrPos(0xEE, -8060, -6000, -84760, 0)
    SetChrPos(0xEF, -7300, -6000, -85820, 0)
    SetChrPos(0xF0, -9280, -6000, -86090, 0)
    SetChrPos(0xF1, -8160, -6000, -87360, 0)
    SetChrChipByIndex(0x109, 10)
    SetChrSubChip(0x109, 0)
    SetChrChipByIndex(0xEF, 11)
    SetChrSubChip(0xEF, 0)
    SetChrChipByIndex(0xF0, 12)
    SetChrSubChip(0xF0, 0)
    SetChrChipByIndex(0xF1, 13)
    SetChrSubChip(0xF1, 0)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    Sleep(1000)
    OP_6D(-7420, -6000, -81560, 0)
    OP_67(0, 7430, -10000, 0)
    OP_6B(2660, 0)
    OP_6C(44000, 0)
    OP_6E(306, 0)

    def lambda_F92():
        OP_6D(-7240, -6000, -84980, 2000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_F92)

    def lambda_FAA():
        OP_67(0, 6730, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_FAA)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    Fade(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x0, 65535)
    SetChrSubChip(0x0, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x1, 65535)
    SetChrSubChip(0x1, 0)
    Sleep(50)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x2, 65535)
    SetChrSubChip(0x2, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x3, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #6
        0x109,
        (
            "#1068F#5PWhew... That takes care of them.\x02\x03",

            "#1063FJust what WERE they?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_112D")
    OP_A2(0x4)

    ChrTalk(    #7
        0x102,
        (
            "#1505F#6PThey weren't ordinary monsters, anyway.\x02\x03",

            "#1502FThey reminded me of the prank-loving\x01",
            "gremlins that appear in folklore.\x02\x03",

            "Perhaps that's what they actually were?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_142C")

    label("loc_112D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11EE")
    OP_A2(0x1)

    ChrTalk(    #8
        0x10E,
        (
            "#176F#6PThey weren't ordinary monsters, at least.\x02\x03",

            "#178FThey reminded me of the prank-loving\x01",
            "gremlins that appear in folklore.\x02\x03",

            "Perhaps that's what they actually were?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_142C")

    label("loc_11EE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12AF")
    OP_A2(0x2)

    ChrTalk(    #9
        0x10D,
        (
            "#272F#6PThey weren't ordinary monsters, at least.\x02\x03",

            "#270FThey reminded me of the prank-loving\x01",
            "gremlins that appear in folklore.\x02\x03",

            "Perhaps that's what they actually were?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_142C")

    label("loc_12AF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1372")
    OP_A2(0x5)

    ChrTalk(    #10
        0x105,
        (
            "#1167F#6PThey weren't ordinary monsters, at least.\x02\x03",

            "#1162FThey reminded me of the prank-loving\x01",
            "gremlins that appear in folklore.\x02\x03",

            "Perhaps that's what they actually were?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_142C")

    label("loc_1372")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_142C")
    OP_A2(0x3)

    ChrTalk(    #11
        0x10B,
        (
            "#416F#6PThey weren't ordinary monsters, anyway.\x02\x03",

            "#212FThey reminded me of the prank-loving\x01",
            "gremlins that appear in folklore.\x02\x03",

            "Maybe that's what they actually were?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_142C")

    OP_8C(0x109, 180, 400)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_14DF")

    ChrTalk(    #12
        0x109,
        (
            "#1840F#5PIt's possible...\x02\x03",

            "#1068FFirst skeletons, then armored knights,\x01",
            "then ghosts, and now gremlins...\x01",
            "This place sure is all about that folkore.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1578")

    label("loc_14DF")


    ChrTalk(    #13
        0x109,
        (
            "#1840F#5PIt's possible...\x02\x03",

            "#1068FFirst skeletons, then armored knights,\x01",
            "then ghosts, and now gremlins...\x01",
            "This place sure is all about that folkore.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1578")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15C0")

    ChrTalk(    #14
        0x105,
        "#1162F#6PAnd not the pleasant kind, at that.\x02",
    )

    CloseMessageWindow()
    Jump("loc_16A3")

    label("loc_15C0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1607")

    ChrTalk(    #15
        0x10E,
        "#178F#6PAnd not the pleasant kind, at that.\x02",
    )

    CloseMessageWindow()
    Jump("loc_16A3")

    label("loc_1607")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1653")

    ChrTalk(    #16
        0x10D,
        "#277F#6PHeh. And not the pleasant kind, at that.\x02",
    )

    CloseMessageWindow()
    Jump("loc_16A3")

    label("loc_1653")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16A3")

    ChrTalk(    #17
        0x10B,
        (
            "#413F#6P*sigh* Well, I sure wish it was the fun\x01",
            "kind...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16A3")

    OP_A2(0x2805)
    OP_28(0x30, 0x4, 0x4)
    OP_28(0x30, 0x4, 0x8)
    OP_28(0x30, 0x1, 0x1)
    OP_28(0x30, 0x1, 0x2)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_4_E8C end

    def Function_5_16C4(): pass

    label("Function_5_16C4")

    PlayEffect(0x1, 0x4, 0xFF, -12500, -5900, -81310, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)

    def lambda_16FF():

        label("loc_16FF")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_16FF")

    QueueWorkItem2(0xFE, 1, lambda_16FF)
    OP_91(0xFE, 0x0, 0x7D0, 0x0, 0x4B0, 0x0)
    OP_82(0x0, 0x2)
    OP_82(0x4, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_5_16C4 end

    def Function_6_172C(): pass

    label("Function_6_172C")

    PlayEffect(0x1, 0x5, 0xFF, -9470, -5900, -79940, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)

    def lambda_1767():

        label("loc_1767")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1767")

    QueueWorkItem2(0xFE, 1, lambda_1767)
    OP_91(0xFE, 0x0, 0x7D0, 0x0, 0x4B0, 0x0)
    OP_82(0x1, 0x2)
    OP_82(0x5, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_6_172C end

    def Function_7_1794(): pass

    label("Function_7_1794")

    PlayEffect(0x1, 0x6, 0xFF, -6880, -5900, -80270, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)

    def lambda_17CF():

        label("loc_17CF")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_17CF")

    QueueWorkItem2(0xFE, 1, lambda_17CF)
    OP_91(0xFE, 0x0, 0x7D0, 0x0, 0x4B0, 0x0)
    OP_82(0x2, 0x2)
    OP_82(0x6, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_7_1794 end

    def Function_8_17FC(): pass

    label("Function_8_17FC")

    PlayEffect(0x1, 0x7, 0xFF, -4410, -5900, -82380, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)

    def lambda_1837():

        label("loc_1837")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1837")

    QueueWorkItem2(0xFE, 1, lambda_1837)
    OP_91(0xFE, 0x0, 0x7D0, 0x0, 0x4B0, 0x0)
    OP_82(0x3, 0x2)
    OP_82(0x7, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_8_17FC end

    def Function_9_1864(): pass

    label("Function_9_1864")


    def lambda_186A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_186A)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0xFFFFE084, 0xFFFFE890, 0xFFFEB4E8, 0x1388, 0x0)
    Return()

    # Function_9_1864 end

    def Function_10_1890(): pass

    label("Function_10_1890")

    Sleep(350)

    def lambda_189B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_189B)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0xFFFFE43A, 0xFFFFE890, 0xFFFEB128, 0x1388, 0x0)
    Return()

    # Function_10_1890 end

    def Function_11_18C1(): pass

    label("Function_11_18C1")

    Sleep(600)

    def lambda_18CC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_18CC)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0xFFFFDBC0, 0xFFFFE890, 0xFFFEAFB6, 0x1388, 0x0)
    Return()

    # Function_11_18C1 end

    def Function_12_18F2(): pass

    label("Function_12_18F2")

    Sleep(1000)

    def lambda_18FD():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_18FD)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0xFFFFE020, 0xFFFFE890, 0xFFFEAAC0, 0x1388, 0x0)
    Return()

    # Function_12_18F2 end

    def Function_13_1923(): pass

    label("Function_13_1923")

    OP_DE(0x0, 0x1, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, -44020, 34290, 63630, 180)
    SetChrPos(0x1, -44020, 34290, 63630, 180)
    SetChrPos(0x2, -44020, 34290, 63630, 180)
    SetChrPos(0x3, -44020, 34290, 63630, 180)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -44020, 34290, 63630, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 15)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x14C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_13_1923 end

    def Function_14_1A01(): pass

    label("Function_14_1A01")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x0, -44020, 34290, 63630, 0)
    SetChrPos(0x1, -44020, 34290, 63630, 0)
    SetChrPos(0x2, -44020, 34290, 63630, 0)
    SetChrPos(0x3, -44020, 34290, 63630, 0)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -44020, 34290, 63630, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 16)
    NewScene("ED6_DT21/M7104   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_14_1A01 end

    def Function_15_1ABD(): pass

    label("Function_15_1ABD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1AE6")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1ADA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1ADA)

    label("loc_1AE6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B0F")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1B03():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1B03)

    label("loc_1B0F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B38")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1B2C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1B2C)

    label("loc_1B38")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B61")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1B55():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1B55)

    label("loc_1B61")

    Sleep(800)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B8D")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_1B8D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BA4")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_1BA4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BBB")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_1BBB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BD2")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_1BD2")

    Return()

    # Function_15_1ABD end

    def Function_16_1BD3(): pass

    label("Function_16_1BD3")


    def lambda_1BD9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1BD9)

    def lambda_1BEB():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1BEB)

    def lambda_1BFD():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1BFD)

    def lambda_1C0F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1C0F)
    Sleep(1000)
    Return()

    # Function_16_1BD3 end

    def Function_17_1C21(): pass

    label("Function_17_1C21")

    SetMessageWindowPos(-1, 110, -1, -1)
    SetChrName("")

    AnonymousTalk(    #18
        "\x07\x05Open the Door?\x18\x02",
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Sleep(300)
    Return()

    # Function_17_1C21 end

    def Function_18_1C7A(): pass

    label("Function_18_1C7A")

    EventBegin(0x0)
    OP_22(0x222, 0x0, 0x64)
    Fade(500)
    SetChrPos(0x0, 24660, 30000, 45450, 0)
    SetChrPos(0x1, 22980, 30000, 45400, 0)
    SetChrPos(0x2, 24380, 30000, 43840, 0)
    SetChrPos(0x3, 22440, 30000, 43610, 0)
    OP_6D(23670, 30000, 46430, 0)
    OP_67(0, 6230, -10000, 0)
    OP_6B(4600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D50")
    OP_28(0x9, 0x4, 0x2)
    OP_82(0x83, 0x2)
    PlayEffect(0x84, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_1D50")

    Sleep(1000)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #19
        (
            "\x07\x05#40WBring to me the man who talks\x01",
            "with his fists.\x01",
            "#500W \x01",
            "#40WOnly then shall the door open...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E0F")
    Call(0, 17)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E0C")
    Call(0, 19)

    label("loc_1E0C")

    Jump("loc_1E0F")

    label("loc_1E0F")

    FadeToBright(300, 0)
    EventEnd(0x0)
    Return()

    # Function_18_1C7A end

    def Function_19_1E1B(): pass

    label("Function_19_1E1B")

    FadeToBright(300, 0)
    Sleep(500)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x78)
    Sleep(300)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x1)
    Sleep(500)

    def lambda_1E84():
        OP_6B(4100, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_1E84)
    OP_22(0x138, 0x0, 0x64)
    FadeToDark(2000, 16777215, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    FadeToBright(2000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    OP_E3(0x0, 0x2, 0, 0x0)
    NewScene("ED6_DT21/P9001   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_19_1E1B end

    def Function_20_1ED1(): pass

    label("Function_20_1ED1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    Sleep(500)
    SetChrPos(0x0, 24660, 30000, 45450, 0)
    SetChrPos(0x1, 22980, 30000, 45400, 0)
    SetChrPos(0x2, 24380, 30000, 43840, 0)
    SetChrPos(0x3, 22440, 30000, 43610, 0)
    OP_6D(23670, 30000, 46430, 0)
    OP_67(0, 6230, -10000, 0)
    OP_6B(4600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    EventEnd(0x0)
    Return()

    # Function_20_1ED1 end

    def Function_21_1F7C(): pass

    label("Function_21_1F7C")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x514, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2055")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x202, 1)"), scpexpr(EXPR_END)), "loc_1FEA")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #20
        "\x07\x05Found \x1F\x02\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x28A0)
    Jump("loc_2052")

    label("loc_1FEA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #21
        (
            "\x07\x05Found \x1F\x02\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x02\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_2052")

    Jump("loc_20B2")

    label("loc_2055")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #22
        "\x07\x05This chest appreciates your concern, but it's doing okay.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0xB7, 0x0)

    label("loc_20B2")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_21_1F7C end

    def Function_22_20C0(): pass

    label("Function_22_20C0")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x514, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2111")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x1E)
    OP_73(0x3)
    OP_6F(0x3, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    Call(6, 26)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x28A1)
    Jump("loc_214A")

    label("loc_2111")


    AnonymousTalk(    #23
        "\x07\x05Please do not take without permission. Thank you.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_214A")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    OP_F7(0x19, 0xB8, 0x0)
    Return()

    # Function_22_20C0 end

    def Function_23_2161(): pass

    label("Function_23_2161")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x514, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21B2")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x1E)
    OP_73(0x4)
    OP_6F(0x4, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    Call(6, 26)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x28A2)
    Jump("loc_2292")

    label("loc_21B2")


    AnonymousTalk(    #24
        (
            "\x07\x05[24/36] 'No, we aren't. That place is mine, and I can do whatever I want\x01",
            "with it. And what I want to do is wash my hands of the thing for good!'\x01",
            "He swallowed another healthy chunk of lamb, then clack! went his knife.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_2292")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    OP_F7(0x19, 0xB9, 0x0)
    Return()

    # Function_23_2161 end

    def Function_24_22A9(): pass

    label("Function_24_22A9")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x514, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22FA")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x1E)
    OP_73(0x5)
    OP_6F(0x5, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    Call(6, 26)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x28A3)
    Jump("loc_233B")

    label("loc_22FA")


    AnonymousTalk(    #25
        "\x07\x05Could ya spare a Tear Balm or two for these rusty hinges?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_233B")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    OP_F7(0x19, 0xBA, 0x0)
    Return()

    # Function_24_22A9 end

    def Function_25_2352(): pass

    label("Function_25_2352")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x514, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_242B")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x19A, 1)"), scpexpr(EXPR_END)), "loc_23C0")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #26
        "\x07\x05Found \x1F\x9A\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x28A4)
    Jump("loc_2428")

    label("loc_23C0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #27
        (
            "\x07\x05Found \x1F\x9A\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x9A\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)

    label("loc_2428")

    Jump("loc_251C")

    label("loc_242B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #28
        (
            "\x07\x05[21/36] 'And I say we keep it,' she said, her stiff tone implying that any\x01",
            "other plans he dared to present would be, to put it delicately, stupid.\x01",
            "'Think of all the history you're abandoning. Fifty years!'\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0xBB, 0x0)

    label("loc_251C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_25_2352 end

    def Function_26_252A(): pass

    label("Function_26_252A")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x514, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_263A")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x7, 0x1E)
    OP_73(0x7)
    OP_6F(0x7, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 0x64)
    AddSepith(0x1, 0x64)
    AddSepith(0x2, 0x64)
    AddSepith(0x3, 0x64)
    AddSepith(0x4, 0x64)
    AddSepith(0x5, 0x64)
    AddSepith(0x6, 0x64)

    AnonymousTalk(    #29
        (
            "\x07\x02Obtained:\x01",
            "#56IEarth Sepith x100\x01",
            "#57IWater Sepith x100\x01",
            "#58IFire Sepith x100\x01",
            "#59IWind Sepith x100\x01",
            "#62ITime Sepith x100\x01",
            "#60ISpace Sepith x100\x01",
            "#61IMirage Sepith x100.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x28A5)
    Jump("loc_2714")

    label("loc_263A")


    AnonymousTalk(    #30
        (
            "\x07\x05Did you know? Halle from Gambler Jack's name was originally translated\x01",
            "accurately as 'Haru,' but it turns out the official Japanese spelling wasn't\x01",
            "that, but 'Halle.' This was revealed in Gambler Jack's sequel.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_2714")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    OP_F7(0x19, 0xBC, 0x0)
    Return()

    # Function_26_252A end

    def Function_27_272B(): pass

    label("Function_27_272B")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x514, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2795")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x8, 0x1E)
    OP_73(0x8)
    OP_6F(0x8, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddMira(3000)

    AnonymousTalk(    #31
        "\x07\x05Found \x07\x021,000 mira\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x28A6)
    Jump("loc_27BA")

    label("loc_2795")


    AnonymousTalk(    #32
        "\x07\x05Congratulations! It's a girl!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_27BA")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    OP_F7(0x19, 0xBD, 0x0)
    Return()

    # Function_27_272B end

    def Function_28_27D1(): pass

    label("Function_28_27D1")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x514, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28E1")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x9, 0x1E)
    OP_73(0x9)
    OP_6F(0x9, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 0x64)
    AddSepith(0x1, 0x64)
    AddSepith(0x2, 0x64)
    AddSepith(0x3, 0x64)
    AddSepith(0x4, 0x64)
    AddSepith(0x5, 0x64)
    AddSepith(0x6, 0x64)

    AnonymousTalk(    #33
        (
            "\x07\x02Obtained:\x01",
            "#56IEarth Sepith x100\x01",
            "#57IWater Sepith x100\x01",
            "#58IFire Sepith x100\x01",
            "#59IWind Sepith x100\x01",
            "#62ITime Sepith x100\x01",
            "#60ISpace Sepith x100\x01",
            "#61IMirage Sepith x100.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x28A7)
    Jump("loc_2947")

    label("loc_28E1")


    AnonymousTalk(    #34
        (
            "\x07\x05Looking into the void inside the empty chest, you start questioning the\x01",
            "nature of life itself.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_2947")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    OP_F7(0x19, 0xBE, 0x0)
    Return()

    # Function_28_27D1 end

    def Function_29_295E(): pass

    label("Function_29_295E")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x515, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A37")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xA, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x169, 1)"), scpexpr(EXPR_END)), "loc_29CC")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #35
        "\x07\x05Found \x1F\x69\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x28AD)
    Jump("loc_2A34")

    label("loc_29CC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #36
        (
            "\x07\x05Found \x1F\x69\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x69\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xA, 60)
    OP_70(0xA, 0x0)

    label("loc_2A34")

    Jump("loc_2AB5")

    label("loc_2A37")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #37
        (
            "\x07\x05You open the lid. A piercing scream fills the air.\x01",
            "You quickly shut the lid and walk away.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0xBF, 0x0)

    label("loc_2AB5")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_29_295E end

    SaveToFile()

Try(main)
