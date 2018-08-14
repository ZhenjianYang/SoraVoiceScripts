from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

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
        '小鬼',                                 # 9
        '小鬼',                                 # 10
        '小鬼',                                 # 11
        '小鬼',                                 # 12
        '',                                     # 13
        '',                                     # 14
        '',                                     # 15
        '',                                     # 16
        '',                                     # 17
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
        "Function_4_EB9",          # 04, 4
        "Function_5_166D",         # 05, 5
        "Function_6_16D5",         # 06, 6
        "Function_7_173D",         # 07, 7
        "Function_8_17A5",         # 08, 8
        "Function_9_180D",         # 09, 9
        "Function_10_1839",        # 0A, 10
        "Function_11_186A",        # 0B, 11
        "Function_12_189B",        # 0C, 12
        "Function_13_18CC",        # 0D, 13
        "Function_14_19AA",        # 0E, 14
        "Function_15_1A66",        # 0F, 15
        "Function_16_1B7C",        # 10, 16
        "Function_17_1BCA",        # 11, 17
        "Function_18_1C3E",        # 12, 18
        "Function_19_1DE1",        # 13, 19
        "Function_20_1E97",        # 14, 20
        "Function_21_1F42",        # 15, 21
        "Function_22_2068",        # 16, 22
        "Function_23_20E7",        # 17, 23
        "Function_24_2166",        # 18, 24
        "Function_25_21E5",        # 19, 25
        "Function_26_230B",        # 1A, 26
        "Function_27_2462",        # 1B, 27
        "Function_28_2502",        # 1C, 28
        "Function_29_2657",        # 1D, 29
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
        "#1063F#6P嘁……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BF5")

    ChrTalk(    #1
        0x107,
        "#065F#6P哇哇……\x02",
    )

    CloseMessageWindow()
    Jump("loc_CC5")

    label("loc_BF5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C2B")

    ChrTalk(    #2
        0x10B,
        "#216F#6P慢、慢着……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_CC5")

    label("loc_C2B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C5E")

    ChrTalk(    #3
        0x105,
        "#1162F#6P……哼………\x02",
    )

    CloseMessageWindow()
    Jump("loc_CC5")

    label("loc_C5E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C94")

    ChrTalk(    #4
        0x10D,
        "#270F#6P……来了吗……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_CC5")

    label("loc_C94")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CC5")

    ChrTalk(    #5
        0x10E,
        "#172F#6P这么突然……！\x02",
    )

    CloseMessageWindow()

    label("loc_CC5")

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

    def lambda_DD3():
        OP_6D(-7480, -6000, -83240, 300)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_DD3)

    def lambda_DEB():
        OP_67(0, 7850, -10000, 300)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_DEB)

    def lambda_E03():
        OP_6B(2000, 300)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_E03)
    SetChrChipByIndex(0x10, 1)

    def lambda_E18():
        OP_8F(0xFE, 0xFFFFD9B8, 0xFFFFE890, 0xFFFEB61E, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_E18)
    Sleep(20)
    SetChrChipByIndex(0x12, 1)

    def lambda_E3D():
        OP_8F(0xFE, 0xFFFFE462, 0xFFFFE890, 0xFFFEB9AC, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_E3D)
    Sleep(20)
    SetChrChipByIndex(0x11, 1)

    def lambda_E62():
        OP_8F(0xFE, 0xFFFFDDE6, 0xFFFFE890, 0xFFFEB984, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_E62)
    Sleep(20)
    SetChrChipByIndex(0x13, 1)

    def lambda_E87():
        OP_8F(0xFE, 0xFFFFE638, 0xFFFFE890, 0xFFFEB4CA, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_E87)
    WaitChrThread(0x109, 0x1)
    WaitChrThread(0x109, 0x2)
    WaitChrThread(0x109, 0x3)
    Battle(0x13E, 0x0, 0x0, 0x0, 0xFF)
    Return()

    # Function_3_5DD end

    def Function_4_EB9(): pass

    label("Function_4_EB9")

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

    def lambda_FBF():
        OP_6D(-7240, -6000, -84980, 2000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_FBF)

    def lambda_FD7():
        OP_67(0, 6730, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_FD7)
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
            "#1068F#5P唉……\x01",
            "总算是赶走那些家伙了。\x02\x03",

            "#1063F但是……\x01",
            "刚才那些奇怪的东西是什么啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1165")
    OP_A2(0x4)

    ChrTalk(    #7
        0x102,
        (
            "#1505F#6P……根据以往的经验来看，\x01",
            "应该不是普通的魔兽。\x02\x03",

            "#1502F像是童话故事里出现的\x01",
            "喜欢恶作剧的小鬼……\x02\x03",

            "可能就是这类型的魔兽吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1410")

    label("loc_1165")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1215")
    OP_A2(0x1)

    ChrTalk(    #8
        0x10E,
        (
            "#176F#6P……根据以往的经验来看，\x01",
            "应该不是普通的魔兽。\x02\x03",

            "#178F好像是童话故事里出现的\x01",
            "喜欢捉弄人的小鬼……\x02\x03",

            "可能就是这类型的东西吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1410")

    label("loc_1215")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12C7")
    OP_A2(0x2)

    ChrTalk(    #9
        0x10D,
        (
            "#272F#6P……根据以往的经验来看，\x01",
            "应该也不是普通的魔兽。\x02\x03",

            "#270F好像是童话故事里出现的\x01",
            "喜欢捉弄人的小鬼……\x02\x03",

            "可能就是这类型的东西吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1410")

    label("loc_12C7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1361")
    OP_A2(0x5)

    ChrTalk(    #10
        0x105,
        (
            "#1167F#6P果然……\x01",
            "不是普通的魔兽吧。\x02\x03",

            "#1162F像是童话故事里出现的\x01",
            "喜欢恶作剧的小鬼……\x02\x03",

            "应该就是这类东西吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1410")

    label("loc_1361")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1410")
    OP_A2(0x3)

    ChrTalk(    #11
        0x10B,
        (
            "#416F#6P虽然不是很清楚……\x01",
            "不过应该不是简单的魔兽吧。\x02\x03",

            "#212F好像是童话故事里出现的\x01",
            "恶作剧小鬼之类的家伙……\x02\x03",

            "我觉得大概就是那样吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1410")

    OP_8C(0x109, 180, 400)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1494")

    ChrTalk(    #12
        0x109,
        (
            "#1840F#5P原来如此……所言甚是。\x02\x03",

            "#1068F骸骨、鬼武士、亡灵，\x01",
            "还有童话故事里的小鬼吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14FE")

    label("loc_1494")


    ChrTalk(    #13
        0x109,
        (
            "#1840F#5P原来如此……所言甚是。\x02\x03",

            "#1068F骸骨、鬼武士、亡灵，\x01",
            "还有童话故事里的小鬼吗……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14FE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1559")

    ChrTalk(    #14
        0x105,
        (
            "#1162F#6P……照这样看来，\x01",
            "要继续前进可要花上不少功夫啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_164C")

    label("loc_1559")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15B3")

    ChrTalk(    #15
        0x10E,
        (
            "#178F#6P……照这样看来，\x01",
            "要继续前进可要花上不少功夫啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_164C")

    label("loc_15B3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1603")

    ChrTalk(    #16
        0x10D,
        (
            "#277F#6P哼……\x01",
            "敌人肯定不会让我们轻松过去的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_164C")

    label("loc_1603")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_164C")

    ChrTalk(    #17
        0x10B,
        (
            "#413F#6P唉……\x01",
            "看来不会让我们轻松过去的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_164C")

    OP_A2(0x2805)
    OP_28(0x30, 0x4, 0x4)
    OP_28(0x30, 0x4, 0x8)
    OP_28(0x30, 0x1, 0x1)
    OP_28(0x30, 0x1, 0x2)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_4_EB9 end

    def Function_5_166D(): pass

    label("Function_5_166D")

    PlayEffect(0x1, 0x4, 0xFF, -12500, -5900, -81310, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)

    def lambda_16A8():

        label("loc_16A8")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_16A8")

    QueueWorkItem2(0xFE, 1, lambda_16A8)
    OP_91(0xFE, 0x0, 0x7D0, 0x0, 0x4B0, 0x0)
    OP_82(0x0, 0x2)
    OP_82(0x4, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_5_166D end

    def Function_6_16D5(): pass

    label("Function_6_16D5")

    PlayEffect(0x1, 0x5, 0xFF, -9470, -5900, -79940, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)

    def lambda_1710():

        label("loc_1710")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1710")

    QueueWorkItem2(0xFE, 1, lambda_1710)
    OP_91(0xFE, 0x0, 0x7D0, 0x0, 0x4B0, 0x0)
    OP_82(0x1, 0x2)
    OP_82(0x5, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_6_16D5 end

    def Function_7_173D(): pass

    label("Function_7_173D")

    PlayEffect(0x1, 0x6, 0xFF, -6880, -5900, -80270, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)

    def lambda_1778():

        label("loc_1778")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1778")

    QueueWorkItem2(0xFE, 1, lambda_1778)
    OP_91(0xFE, 0x0, 0x7D0, 0x0, 0x4B0, 0x0)
    OP_82(0x2, 0x2)
    OP_82(0x6, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_7_173D end

    def Function_8_17A5(): pass

    label("Function_8_17A5")

    PlayEffect(0x1, 0x7, 0xFF, -4410, -5900, -82380, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)

    def lambda_17E0():

        label("loc_17E0")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_17E0")

    QueueWorkItem2(0xFE, 1, lambda_17E0)
    OP_91(0xFE, 0x0, 0x7D0, 0x0, 0x4B0, 0x0)
    OP_82(0x3, 0x2)
    OP_82(0x7, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_8_17A5 end

    def Function_9_180D(): pass

    label("Function_9_180D")


    def lambda_1813():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1813)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0xFFFFE084, 0xFFFFE890, 0xFFFEB4E8, 0x1388, 0x0)
    Return()

    # Function_9_180D end

    def Function_10_1839(): pass

    label("Function_10_1839")

    Sleep(350)

    def lambda_1844():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1844)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0xFFFFE43A, 0xFFFFE890, 0xFFFEB128, 0x1388, 0x0)
    Return()

    # Function_10_1839 end

    def Function_11_186A(): pass

    label("Function_11_186A")

    Sleep(600)

    def lambda_1875():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1875)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0xFFFFDBC0, 0xFFFFE890, 0xFFFEAFB6, 0x1388, 0x0)
    Return()

    # Function_11_186A end

    def Function_12_189B(): pass

    label("Function_12_189B")

    Sleep(1000)

    def lambda_18A6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_18A6)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0xFFFFE020, 0xFFFFE890, 0xFFFEAAC0, 0x1388, 0x0)
    Return()

    # Function_12_189B end

    def Function_13_18CC(): pass

    label("Function_13_18CC")

    OP_DE(0x0, 0x1, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    # Function_13_18CC end

    def Function_14_19AA(): pass

    label("Function_14_19AA")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    # Function_14_19AA end

    def Function_15_1A66(): pass

    label("Function_15_1A66")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A8F")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1A83():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1A83)

    label("loc_1A8F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1AB8")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1AAC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1AAC)

    label("loc_1AB8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1AE1")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1AD5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1AD5)

    label("loc_1AE1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B0A")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1AFE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1AFE)

    label("loc_1B0A")

    Sleep(800)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B36")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_1B36")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B4D")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_1B4D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B64")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_1B64")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B7B")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_1B7B")

    Return()

    # Function_15_1A66 end

    def Function_16_1B7C(): pass

    label("Function_16_1B7C")


    def lambda_1B82():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1B82)

    def lambda_1B94():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1B94)

    def lambda_1BA6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1BA6)

    def lambda_1BB8():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1BB8)
    Sleep(1000)
    Return()

    # Function_16_1B7C end

    def Function_17_1BCA(): pass

    label("Function_17_1BCA")

    SetMessageWindowPos(-1, 110, -1, -1)
    SetChrName("")

    AnonymousTalk(    #18
        "\x07\x05打开『门』吗？\x18\x02",
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    Jump("loc_1C27")

    label("loc_1C27")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Sleep(300)
    Return()

    # Function_17_1BCA end

    def Function_18_1C3E(): pass

    label("Function_18_1C3E")

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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D14")
    OP_28(0x9, 0x4, 0x2)
    OP_82(0x83, 0x2)
    PlayEffect(0x84, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_1D14")

    Sleep(1000)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #19
        (
            "\x07\x05#40W　  汝须将以拳述己心志者\x01",
            "　　   引领至吾面前。\x01",
            "#500W\x01",
            "#40W   如此，则『门』将开启……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DD5")
    Call(0, 17)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DD2")
    Call(0, 19)

    label("loc_1DD2")

    Jump("loc_1DD5")

    label("loc_1DD5")

    FadeToBright(300, 0)
    EventEnd(0x0)
    Return()

    # Function_18_1C3E end

    def Function_19_1DE1(): pass

    label("Function_19_1DE1")

    FadeToBright(300, 0)
    Sleep(500)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x78)
    Sleep(300)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x1)
    Sleep(500)

    def lambda_1E4A():
        OP_6B(4100, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_1E4A)
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

    # Function_19_1DE1 end

    def Function_20_1E97(): pass

    label("Function_20_1E97")

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

    # Function_20_1E97 end

    def Function_21_1F42(): pass

    label("Function_21_1F42")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x514, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2027")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x202, 1)"), scpexpr(EXPR_END)), "loc_1FB6")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #20
        "\x07\x00得到了\x1F\x02\x02\x07\x00。\x02",
    )

    Jump("loc_1F9B")

    label("loc_1F9B")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x28A0)
    Jump("loc_2024")

    label("loc_1FB6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #21
        (
            "宝箱里装有\x1F\x02\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x02\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_2005")

    label("loc_2005")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_2024")

    Jump("loc_205A")

    label("loc_2027")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #22
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_205A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_21_1F42 end

    def Function_22_2068(): pass

    label("Function_22_2068")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x514, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20B9")
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
    Jump("loc_20D5")

    label("loc_20B9")


    AnonymousTalk(    #23
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_20D5")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_22_2068 end

    def Function_23_20E7(): pass

    label("Function_23_20E7")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x514, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2138")
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
    Jump("loc_2154")

    label("loc_2138")


    AnonymousTalk(    #24
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_2154")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_23_20E7 end

    def Function_24_2166(): pass

    label("Function_24_2166")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x514, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21B7")
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
    Jump("loc_21D3")

    label("loc_21B7")


    AnonymousTalk(    #25
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_21D3")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_24_2166 end

    def Function_25_21E5(): pass

    label("Function_25_21E5")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x514, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22CA")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x19A, 1)"), scpexpr(EXPR_END)), "loc_2259")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #26
        "\x07\x00得到了\x1F\x9A\x01\x07\x00。\x02",
    )

    Jump("loc_223E")

    label("loc_223E")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x28A4)
    Jump("loc_22C7")

    label("loc_2259")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #27
        (
            "宝箱里装有\x1F\x9A\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x9A\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_22A8")

    label("loc_22A8")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)

    label("loc_22C7")

    Jump("loc_22FD")

    label("loc_22CA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #28
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_22FD")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_25_21E5 end

    def Function_26_230B(): pass

    label("Function_26_230B")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x514, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2434")
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
            "\x07\x00得到了：\x01",
            "\x07\x02#56I地之耀晶片×１００\x01",
            "\x07\x02#57I水之耀晶片×１００\x01",
            "\x07\x02#58I火之耀晶片×１００\x01",
            "\x07\x02#59I风之耀晶片×１００\x01",
            "\x07\x02#62I时之耀晶片×１００\x01",
            "\x07\x02#60I空之耀晶片×１００\x01",
            "\x07\x02#61I幻之耀晶片×１００\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x28A5)
    Jump("loc_2450")

    label("loc_2434")


    AnonymousTalk(    #30
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_2450")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_26_230B end

    def Function_27_2462(): pass

    label("Function_27_2462")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x514, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24D4")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x8, 0x1E)
    OP_73(0x8)
    OP_6F(0x8, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddMira(3000)

    AnonymousTalk(    #31
        "\x07\x00得到了\x07\x02１０００米拉\x07\x00。\x02",
    )

    Jump("loc_24C2")

    label("loc_24C2")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x28A6)
    Jump("loc_24F0")

    label("loc_24D4")


    AnonymousTalk(    #32
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_24F0")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_27_2462 end

    def Function_28_2502(): pass

    label("Function_28_2502")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x514, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_262B")
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
            "\x07\x00得到了：\x01",
            "\x07\x02#56I地之耀晶片×１００\x01",
            "\x07\x02#57I水之耀晶片×１００\x01",
            "\x07\x02#58I火之耀晶片×１００\x01",
            "\x07\x02#59I风之耀晶片×１００\x01",
            "\x07\x02#62I时之耀晶片×１００\x01",
            "\x07\x02#60I空之耀晶片×１００\x01",
            "\x07\x02#61I幻之耀晶片×１００\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x28A7)
    Jump("loc_2645")

    label("loc_262B")


    AnonymousTalk(    #34
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_2645")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_28_2502 end

    def Function_29_2657(): pass

    label("Function_29_2657")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x515, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2738")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xA, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x169, 1)"), scpexpr(EXPR_END)), "loc_26C9")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #35
        "\x07\x00得到了\x1F\x69\x01\x07\x00。\x02",
    )

    Jump("loc_26AE")

    label("loc_26AE")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x28AD)
    Jump("loc_2735")

    label("loc_26C9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #36
        (
            "宝箱里装有\x1F\x69\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x69\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_2716")

    label("loc_2716")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xA, 60)
    OP_70(0xA, 0x0)

    label("loc_2735")

    Jump("loc_2769")

    label("loc_2738")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #37
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_2769")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_29_2657 end

    SaveToFile()

Try(main)
