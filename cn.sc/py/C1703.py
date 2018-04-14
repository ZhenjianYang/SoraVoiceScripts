from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 柏斯

    CreateScenaFile(
        FileName            = 'C1703   ._SN',
        MapName             = 'Bose',
        Location            = 'C1703.x',
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

    DeclNpc(
        X                   = 32009,
        Z                   = 2400,
        Y                   = 30,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -16079,
        Z                   = 400,
        Y                   = 31920,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F6,
        Unknown_18          = 7816,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -16020,
        Z                   = 400,
        Y                   = 16040,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F4,
        Unknown_18          = 7817,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -16010,
        Z                   = 400,
        Y                   = -40,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F7,
        Unknown_18          = 7818,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -16270,
        Z                   = 400,
        Y                   = -16340,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F5,
        Unknown_18          = 7819,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 16040,
        Z                   = 400,
        Y                   = -15950,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F8,
        Unknown_18          = 7820,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 15850,
        Z                   = 400,
        Y                   = -200,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F4,
        Unknown_18          = 7821,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 15800,
        Z                   = 400,
        Y                   = 15870,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F6,
        Unknown_18          = 7822,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 16129,
        Z                   = 400,
        Y                   = 32250,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F5,
        Unknown_18          = 7823,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -31950,
        TriggerZ            = 400,
        TriggerY            = 31360,
        TriggerRange        = 1000,
        ActorX              = -31950,
        ActorZ              = 400,
        ActorY              = 31980,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 32009,
        TriggerZ            = 400,
        TriggerY            = 820,
        TriggerRange        = 1000,
        ActorX              = 32009,
        ActorZ              = 400,
        ActorY              = 30,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 60,
        TriggerZ            = 400,
        TriggerY            = 37280,
        TriggerRange        = 1000,
        ActorX              = 20,
        ActorZ              = 400,
        ActorY              = 37940,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -20,
        TriggerZ            = 400,
        TriggerY            = 11720,
        TriggerRange        = 1000,
        ActorX              = -20,
        ActorZ              = 400,
        ActorY              = 10980,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 20,
        TriggerZ            = 400,
        TriggerY            = 4280,
        TriggerRange        = 1000,
        ActorX              = 20,
        ActorZ              = 400,
        ActorY              = 4900,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -10,
        TriggerZ            = 400,
        TriggerY            = -21280,
        TriggerRange        = 1000,
        ActorX              = -10,
        ActorZ              = 400,
        ActorY              = -22070,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2F2",          # 00, 0
        "Function_1_369",          # 01, 1
        "Function_2_492",          # 02, 2
        "Function_3_4A8",          # 03, 3
        "Function_4_5BF",          # 04, 4
        "Function_5_78F",          # 05, 5
        "Function_6_8A6",          # 06, 6
        "Function_7_9BD",          # 07, 7
        "Function_8_AD4",          # 08, 8
        "Function_9_BEB",          # 09, 9
        "Function_10_CE6",         # 0A, 10
        "Function_11_D5E",         # 0B, 11
        "Function_12_E6B",         # 0C, 12
        "Function_13_EEC",         # 0D, 13
        "Function_14_FE7",         # 0E, 14
        "Function_15_105F",        # 0F, 15
        "Function_16_116C",        # 10, 16
        "Function_17_11ED",        # 11, 17
        "Function_18_12FA",        # 12, 18
        "Function_19_137B",        # 13, 19
        "Function_20_1488",        # 14, 20
        "Function_21_1509",        # 15, 21
        "Function_22_1604",        # 16, 22
        "Function_23_167C",        # 17, 23
        "Function_24_1777",        # 18, 24
        "Function_25_17EF",        # 19, 25
        "Function_26_18FC",        # 1A, 26
        "Function_27_197D",        # 1B, 27
        "Function_28_1A78",        # 1C, 28
        "Function_29_1AF0",        # 1D, 29
        "Function_30_1BE3",        # 1E, 30
        "Function_31_1CD6",        # 1F, 31
        "Function_32_1D24",        # 20, 32
    )


    def Function_0_2F2(): pass

    label("Function_0_2F2")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_322"),
        (101, "loc_329"),
        (102, "loc_330"),
        (103, "loc_337"),
        (104, "loc_33E"),
        (105, "loc_345"),
        (106, "loc_34C"),
        (107, "loc_353"),
        (108, "loc_35A"),
        (109, "loc_361"),
        (SWITCH_DEFAULT, "loc_368"),
    )


    label("loc_322")

    Event(0, 9)
    Jump("loc_368")

    label("loc_329")

    Event(0, 11)
    Jump("loc_368")

    label("loc_330")

    Event(0, 13)
    Jump("loc_368")

    label("loc_337")

    Event(0, 15)
    Jump("loc_368")

    label("loc_33E")

    Event(0, 17)
    Jump("loc_368")

    label("loc_345")

    Event(0, 19)
    Jump("loc_368")

    label("loc_34C")

    Event(0, 21)
    Jump("loc_368")

    label("loc_353")

    Event(0, 23)
    Jump("loc_368")

    label("loc_35A")

    Event(0, 25)
    Jump("loc_368")

    label("loc_361")

    Event(0, 27)
    Jump("loc_368")

    label("loc_368")

    Return()

    # Function_0_2F2 end

    def Function_1_369(): pass

    label("Function_1_369")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37B")
    OP_6F(0x0, 0)
    Jump("loc_382")

    label("loc_37B")

    OP_6F(0x0, 60)

    label("loc_382")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F5, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_394")
    OP_6F(0x1, 0)
    Jump("loc_39B")

    label("loc_394")

    OP_6F(0x1, 60)

    label("loc_39B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F5, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AD")
    OP_6F(0x2, 0)
    Jump("loc_3B4")

    label("loc_3AD")

    OP_6F(0x2, 60)

    label("loc_3B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C6")
    OP_6F(0x3, 0)
    Jump("loc_3CD")

    label("loc_3C6")

    OP_6F(0x3, 60)

    label("loc_3CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DF")
    OP_6F(0x4, 0)
    Jump("loc_3E6")

    label("loc_3DF")

    OP_6F(0x4, 60)

    label("loc_3E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F8")
    OP_6F(0x5, 0)
    Jump("loc_3FF")

    label("loc_3F8")

    OP_6F(0x5, 60)

    label("loc_3FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D1, 0)), scpexpr(EXPR_END)), "loc_40B")
    SetChrFlags(0x9, 0x80)

    label("loc_40B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D1, 1)), scpexpr(EXPR_END)), "loc_417")
    SetChrFlags(0xA, 0x80)

    label("loc_417")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D1, 2)), scpexpr(EXPR_END)), "loc_423")
    SetChrFlags(0xB, 0x80)

    label("loc_423")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D1, 3)), scpexpr(EXPR_END)), "loc_42F")
    SetChrFlags(0xC, 0x80)

    label("loc_42F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D1, 4)), scpexpr(EXPR_END)), "loc_43B")
    SetChrFlags(0xD, 0x80)

    label("loc_43B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D1, 5)), scpexpr(EXPR_END)), "loc_447")
    SetChrFlags(0xE, 0x80)

    label("loc_447")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D1, 6)), scpexpr(EXPR_END)), "loc_453")
    SetChrFlags(0xF, 0x80)

    label("loc_453")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D1, 7)), scpexpr(EXPR_END)), "loc_45F")
    SetChrFlags(0x10, 0x80)

    label("loc_45F")

    OP_1B(0x0, 0x0, 0xA)
    OP_1B(0x1, 0x0, 0xC)
    OP_1B(0x2, 0x0, 0xE)
    OP_1B(0x3, 0x0, 0x10)
    OP_1B(0x4, 0x0, 0x12)
    OP_1B(0x5, 0x0, 0x14)
    OP_1B(0x6, 0x0, 0x16)
    OP_1B(0x7, 0x0, 0x18)
    OP_1B(0x8, 0x0, 0x1A)
    OP_1B(0x9, 0x0, 0x1C)
    Return()

    # Function_1_369 end

    def Function_2_492(): pass

    label("Function_2_492")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4A7")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_492")

    label("loc_4A7")

    Return()

    # Function_2_492 end

    def Function_3_4A8(): pass

    label("Function_3_4A8")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_580")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0xC6, 1)"), scpexpr(EXPR_END)), "loc_517")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\xC6\x00\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1FAA)
    Jump("loc_57D")

    label("loc_517")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\xC6\x00\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xC6\x00\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_57D")

    Jump("loc_5B1")

    label("loc_580")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_5B1")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_4A8 end

    def Function_4_5BF(): pass

    label("Function_4_5BF")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F5, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_752")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F5, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_69E")
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_91(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_611():
        OP_91(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_611)

    def lambda_62C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x258)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_62C)
    ClearChrFlags(0x8, 0x80)

    AnonymousTalk(    #3
        "\x07\x05魔兽出现了！\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x3FC, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_679"),
        (2, "loc_68B"),
        (1, "loc_69B"),
        (SWITCH_DEFAULT, "loc_69E"),
    )


    label("loc_679")

    OP_A2(0x1FAD)
    OP_6F(0x1, 60)
    Sleep(500)
    Jump("loc_69E")

    label("loc_68B")

    OP_6F(0x1, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_69B")

    OP_B4(0x0)
    Return()

    label("loc_69E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x15A, 1)"), scpexpr(EXPR_END)), "loc_6ED")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #4
        "\x07\x00得到了\x1F\x5A\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1FAC)
    Jump("loc_74F")

    label("loc_6ED")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #5
        (
            "宝箱里装有\x1F\x5A\x01\x07\x00。 \x01",
            "所持物品已经满了，\x1F\x5A\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_74F")

    Jump("loc_781")

    label("loc_752")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #6
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_781")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_5BF end

    def Function_5_78F(): pass

    label("Function_5_78F")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F5, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_867")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_7FE")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #7
        "\x07\x00得到了\x1F\xFD\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1FAE)
    Jump("loc_864")

    label("loc_7FE")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        (
            "宝箱里装有\x1F\xFD\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFD\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_864")

    Jump("loc_898")

    label("loc_867")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_898")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_78F end

    def Function_6_8A6(): pass

    label("Function_6_8A6")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_97E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FF, 1)"), scpexpr(EXPR_END)), "loc_915")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #10
        "\x07\x00得到了\x1F\xFF\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1FAF)
    Jump("loc_97B")

    label("loc_915")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
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

    label("loc_97B")

    Jump("loc_9AF")

    label("loc_97E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #12
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_9AF")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_8A6 end

    def Function_7_9BD(): pass

    label("Function_7_9BD")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A95")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F7, 1)"), scpexpr(EXPR_END)), "loc_A2C")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #13
        "\x07\x00得到了\x1F\xF7\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1FB0)
    Jump("loc_A92")

    label("loc_A2C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        (
            "宝箱里装有\x1F\xF7\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xF7\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_A92")

    Jump("loc_AC6")

    label("loc_A95")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #15
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_AC6")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_9BD end

    def Function_8_AD4(): pass

    label("Function_8_AD4")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BAC")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x141, 1)"), scpexpr(EXPR_END)), "loc_B43")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #16
        "\x07\x00得到了\x1F\x41\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1FB1)
    Jump("loc_BA9")

    label("loc_B43")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #17
        (
            "宝箱里装有\x1F\x41\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x41\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)

    label("loc_BA9")

    Jump("loc_BDD")

    label("loc_BAC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #18
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_BDD")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_AD4 end

    def Function_9_BEB(): pass

    label("Function_9_BEB")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(0, 200, 84600, 0)
    SetChrPos(0x101, 500, 200, 84100, 180)
    SetChrPos(0x102, -500, 200, 84100, 180)
    SetChrPos(0xF8, 500, 200, 85100, 180)
    SetChrPos(0xF9, -500, 200, 85100, 180)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 29)
    Call(0, 31)
    Fade(500)
    OP_6D(120, 200, 82670, 0)
    SetChrPos(0x0, 120, 200, 82670, 180)
    SetChrPos(0x1, 120, 200, 82670, 180)
    SetChrPos(0x2, 120, 200, 82670, 180)
    SetChrPos(0x3, 120, 200, 82670, 180)
    EventEnd(0x0)
    Return()

    # Function_9_BEB end

    def Function_10_CE6(): pass

    label("Function_10_CE6")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(0, 200, 84600, 0)
    SetChrPos(0x101, -500, 200, 85100, 0)
    SetChrPos(0x102, 500, 200, 85100, 0)
    SetChrPos(0xF8, -500, 200, 84100, 0)
    SetChrPos(0xF9, 500, 200, 84100, 0)
    OP_0D()
    Call(0, 29)
    Call(0, 32)
    NewScene("ED6_DT21/C1702   ._SN", 105, 0, 0)
    IdleLoop()
    Return()

    # Function_10_CE6 end

    def Function_11_D5E(): pass

    label("Function_11_D5E")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-43200, 8200, 98000, 0)
    OP_6C(315000, 0)
    SetChrPos(0x101, -42700, 8200, 98500, 90)
    SetChrPos(0x102, -42700, 8200, 97500, 90)
    SetChrPos(0xF8, -43700, 8200, 98500, 90)
    SetChrPos(0xF9, -43700, 8200, 97500, 90)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 29)
    Call(0, 31)
    Fade(500)
    OP_6D(-41260, 8200, 98030, 0)
    OP_6C(45000, 0)
    SetChrPos(0x0, -41260, 8200, 98030, 90)
    SetChrPos(0x1, -41260, 8200, 98030, 90)
    SetChrPos(0x2, -41260, 8200, 98030, 90)
    SetChrPos(0x3, -41260, 8200, 98030, 90)
    EventEnd(0x0)
    Return()

    # Function_11_D5E end

    def Function_12_E6B(): pass

    label("Function_12_E6B")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(-43200, 8200, 98000, 0)
    OP_6C(315000, 0)
    SetChrPos(0x101, -43700, 8200, 97500, 270)
    SetChrPos(0x102, -43700, 8200, 98500, 270)
    SetChrPos(0xF8, -42700, 8200, 97500, 270)
    SetChrPos(0xF9, -42700, 8200, 98500, 270)
    OP_0D()
    Call(0, 29)
    Call(0, 32)
    NewScene("ED6_DT21/C1702   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_12_E6B end

    def Function_13_EEC(): pass

    label("Function_13_EEC")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(43400, 8200, 98000, 0)
    SetChrPos(0x101, 42900, 8200, 97500, 270)
    SetChrPos(0x102, 42900, 8200, 98500, 270)
    SetChrPos(0xF8, 43900, 8200, 97500, 270)
    SetChrPos(0xF9, 43900, 8200, 98500, 270)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 29)
    Call(0, 31)
    Fade(500)
    OP_6D(41380, 8200, 97960, 0)
    SetChrPos(0x0, 41380, 8200, 97960, 270)
    SetChrPos(0x1, 41380, 8200, 97960, 270)
    SetChrPos(0x2, 41380, 8200, 97960, 270)
    SetChrPos(0x3, 41380, 8200, 97960, 270)
    EventEnd(0x0)
    Return()

    # Function_13_EEC end

    def Function_14_FE7(): pass

    label("Function_14_FE7")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(43400, 8200, 98000, 0)
    SetChrPos(0x101, 43900, 8200, 98500, 90)
    SetChrPos(0x102, 43900, 8200, 97500, 90)
    SetChrPos(0xF8, 42900, 8200, 98500, 90)
    SetChrPos(0xF9, 42900, 8200, 97500, 90)
    OP_0D()
    Call(0, 29)
    Call(0, 32)
    NewScene("ED6_DT21/C1702   ._SN", 107, 0, 0)
    IdleLoop()
    Return()

    # Function_14_FE7 end

    def Function_15_105F(): pass

    label("Function_15_105F")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(32000, 200, -34400, 0)
    OP_6C(135000, 0)
    SetChrPos(0x101, 31500, 200, -33900, 0)
    SetChrPos(0x102, 32500, 200, -33900, 0)
    SetChrPos(0xF8, 31500, 200, -34900, 0)
    SetChrPos(0xF9, 32500, 200, -34900, 0)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 29)
    Call(0, 31)
    Fade(500)
    OP_6D(31900, 200, -32360, 0)
    OP_6C(45000, 0)
    SetChrPos(0x0, 31900, 200, -32360, 0)
    SetChrPos(0x1, 31900, 200, -32360, 0)
    SetChrPos(0x2, 31900, 200, -32360, 0)
    SetChrPos(0x3, 31900, 200, -32360, 0)
    EventEnd(0x0)
    Return()

    # Function_15_105F end

    def Function_16_116C(): pass

    label("Function_16_116C")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(32000, 200, -34400, 0)
    OP_6C(135000, 0)
    SetChrPos(0x101, 32500, 200, -34900, 180)
    SetChrPos(0x102, 31500, 200, -34900, 180)
    SetChrPos(0xF8, 32500, 200, -33900, 180)
    SetChrPos(0xF9, 31500, 200, -33900, 180)
    OP_0D()
    Call(0, 29)
    Call(0, 32)
    NewScene("ED6_DT21/C1702   ._SN", 108, 0, 0)
    IdleLoop()
    Return()

    # Function_16_116C end

    def Function_17_11ED(): pass

    label("Function_17_11ED")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-32000, 200, -34400, 0)
    OP_6C(135000, 0)
    SetChrPos(0x101, -32500, 200, -33900, 0)
    SetChrPos(0x102, -31500, 200, -33900, 0)
    SetChrPos(0xF8, -32500, 200, -34900, 0)
    SetChrPos(0xF9, -31500, 200, -34900, 0)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 29)
    Call(0, 31)
    Fade(500)
    OP_6D(-32100, 200, -32530, 0)
    OP_6C(45000, 0)
    SetChrPos(0x0, -32100, 200, -32530, 0)
    SetChrPos(0x1, -32100, 200, -32530, 0)
    SetChrPos(0x2, -32100, 200, -32530, 0)
    SetChrPos(0x3, -32100, 200, -32530, 0)
    EventEnd(0x0)
    Return()

    # Function_17_11ED end

    def Function_18_12FA(): pass

    label("Function_18_12FA")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(-32000, 200, -34400, 0)
    OP_6C(135000, 0)
    SetChrPos(0x101, -31500, 200, -34900, 180)
    SetChrPos(0x102, -32500, 200, -34900, 180)
    SetChrPos(0xF8, -31500, 200, -33900, 180)
    SetChrPos(0xF9, -32500, 200, -33900, 180)
    OP_0D()
    Call(0, 29)
    Call(0, 32)
    NewScene("ED6_DT21/C1702   ._SN", 109, 0, 0)
    IdleLoop()
    Return()

    # Function_18_12FA end

    def Function_19_137B(): pass

    label("Function_19_137B")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(0, 200, 51500, 0)
    OP_6C(135000, 0)
    SetChrPos(0x101, -500, 200, 52000, 0)
    SetChrPos(0x102, 500, 200, 52000, 0)
    SetChrPos(0xF8, -500, 200, 51000, 0)
    SetChrPos(0xF9, 500, 200, 51000, 0)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 30)
    Call(0, 31)
    Fade(500)
    OP_6D(-100, 200, 53480, 0)
    OP_6C(45000, 0)
    SetChrPos(0x0, -100, 200, 53480, 0)
    SetChrPos(0x1, -100, 200, 53480, 0)
    SetChrPos(0x2, -100, 200, 53480, 0)
    SetChrPos(0x3, -100, 200, 53480, 0)
    EventEnd(0x0)
    Return()

    # Function_19_137B end

    def Function_20_1488(): pass

    label("Function_20_1488")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(0, 200, 51500, 0)
    OP_6C(135000, 0)
    SetChrPos(0x101, 500, 200, 51000, 180)
    SetChrPos(0x102, -500, 200, 51000, 180)
    SetChrPos(0xF8, 500, 200, 52000, 180)
    SetChrPos(0xF9, -500, 200, 52000, 180)
    OP_0D()
    Call(0, 30)
    Call(0, 32)
    NewScene("ED6_DT21/C1704   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_20_1488 end

    def Function_21_1509(): pass

    label("Function_21_1509")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-16000, 200, 68400, 0)
    SetChrPos(0x101, -15500, 200, 67900, 180)
    SetChrPos(0x102, -16500, 200, 67900, 180)
    SetChrPos(0xF8, -15500, 200, 68900, 180)
    SetChrPos(0xF9, -16500, 200, 68900, 180)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 30)
    Call(0, 31)
    Fade(500)
    OP_6D(-15940, 200, 66450, 0)
    SetChrPos(0x0, -15940, 200, 66450, 180)
    SetChrPos(0x1, -15940, 200, 66450, 180)
    SetChrPos(0x2, -15940, 200, 66450, 180)
    SetChrPos(0x3, -15940, 200, 66450, 180)
    EventEnd(0x0)
    Return()

    # Function_21_1509 end

    def Function_22_1604(): pass

    label("Function_22_1604")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(-16000, 200, 68400, 0)
    SetChrPos(0x101, -16500, 200, 68900, 0)
    SetChrPos(0x102, -15500, 200, 68900, 0)
    SetChrPos(0xF8, -16500, 200, 67900, 0)
    SetChrPos(0xF9, -15500, 200, 67900, 0)
    OP_0D()
    Call(0, 30)
    Call(0, 32)
    NewScene("ED6_DT21/C1704   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_22_1604 end

    def Function_23_167C(): pass

    label("Function_23_167C")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(16000, 200, 68400, 0)
    SetChrPos(0x101, 16500, 200, 67900, 180)
    SetChrPos(0x102, 15500, 200, 67900, 180)
    SetChrPos(0xF8, 16500, 200, 68900, 180)
    SetChrPos(0xF9, 15500, 200, 68900, 180)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 30)
    Call(0, 31)
    Fade(500)
    OP_6D(16100, 200, 66510, 0)
    SetChrPos(0x0, 16100, 200, 66510, 180)
    SetChrPos(0x1, 16100, 200, 66510, 180)
    SetChrPos(0x2, 16100, 200, 66510, 180)
    SetChrPos(0x3, 16100, 200, 66510, 180)
    EventEnd(0x0)
    Return()

    # Function_23_167C end

    def Function_24_1777(): pass

    label("Function_24_1777")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(16000, 200, 68400, 0)
    SetChrPos(0x101, 15500, 200, 68900, 0)
    SetChrPos(0x102, 16500, 200, 68900, 0)
    SetChrPos(0xF8, 15500, 200, 67900, 0)
    SetChrPos(0xF9, 16500, 200, 67900, 0)
    OP_0D()
    Call(0, 30)
    Call(0, 32)
    NewScene("ED6_DT21/C1704   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_24_1777 end

    def Function_25_17EF(): pass

    label("Function_25_17EF")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(21600, 8200, 86100, 0)
    OP_6C(315000, 0)
    SetChrPos(0x101, 22100, 8200, 86600, 90)
    SetChrPos(0x102, 22100, 8200, 85600, 90)
    SetChrPos(0xF8, 21100, 8200, 86600, 90)
    SetChrPos(0xF9, 21100, 8200, 85600, 90)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 30)
    Call(0, 31)
    Fade(500)
    OP_6D(23480, 8200, 86130, 0)
    OP_6C(45000, 0)
    SetChrPos(0x0, 23480, 8200, 86130, 90)
    SetChrPos(0x1, 23480, 8200, 86130, 90)
    SetChrPos(0x2, 23480, 8200, 86130, 90)
    SetChrPos(0x3, 23480, 8200, 86130, 90)
    EventEnd(0x0)
    Return()

    # Function_25_17EF end

    def Function_26_18FC(): pass

    label("Function_26_18FC")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(21600, 8200, 86100, 0)
    OP_6C(315000, 0)
    SetChrPos(0x101, 21100, 8200, 85600, 270)
    SetChrPos(0x102, 21100, 8200, 86600, 270)
    SetChrPos(0xF8, 22100, 8200, 85600, 270)
    SetChrPos(0xF9, 22100, 8200, 86600, 270)
    OP_0D()
    Call(0, 30)
    Call(0, 32)
    NewScene("ED6_DT21/C1704   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_26_18FC end

    def Function_27_197D(): pass

    label("Function_27_197D")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-21400, 8200, 86000, 0)
    SetChrPos(0x101, -21900, 8200, 85500, 270)
    SetChrPos(0x102, -21900, 8200, 86500, 270)
    SetChrPos(0xF8, -20900, 8200, 85500, 270)
    SetChrPos(0xF9, -20900, 8200, 86500, 270)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 30)
    Call(0, 31)
    Fade(500)
    OP_6D(-23380, 8200, 85960, 0)
    SetChrPos(0x0, -23380, 8200, 85960, 270)
    SetChrPos(0x1, -23380, 8200, 85960, 270)
    SetChrPos(0x2, -23380, 8200, 85960, 270)
    SetChrPos(0x3, -23380, 8200, 85960, 270)
    EventEnd(0x0)
    Return()

    # Function_27_197D end

    def Function_28_1A78(): pass

    label("Function_28_1A78")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(-21400, 8200, 86000, 0)
    SetChrPos(0x101, -20900, 8200, 86500, 90)
    SetChrPos(0x102, -20900, 8200, 85500, 90)
    SetChrPos(0xF8, -21900, 8200, 86500, 90)
    SetChrPos(0xF9, -21900, 8200, 85500, 90)
    OP_0D()
    Call(0, 30)
    Call(0, 32)
    NewScene("ED6_DT21/C1704   ._SN", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_28_1A78 end

    def Function_29_1AF0(): pass

    label("Function_29_1AF0")

    LoadEffect(0x0, "map\\\\mp049_21.eff")
    PlayEffect(0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Return()

    # Function_29_1AF0 end

    def Function_30_1BE3(): pass

    label("Function_30_1BE3")

    LoadEffect(0x0, "map\\\\mp049_22.eff")
    PlayEffect(0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Return()

    # Function_30_1BE3 end

    def Function_31_1CD6(): pass

    label("Function_31_1CD6")


    def lambda_1CDC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1CDC)

    def lambda_1CEE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1CEE)

    def lambda_1D00():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1D00)

    def lambda_1D12():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1D12)
    Sleep(2500)
    Return()

    # Function_31_1CD6 end

    def Function_32_1D24(): pass

    label("Function_32_1D24")


    def lambda_1D2A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1D2A)

    def lambda_1D3C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1D3C)

    def lambda_1D4E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1D4E)

    def lambda_1D60():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1D60)
    Sleep(2000)
    Return()

    # Function_32_1D24 end

    SaveToFile()

Try(main)
