from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 柏斯

    CreateScenaFile(
        FileName            = 'C1702   ._SN',
        MapName             = 'Bose',
        Location            = 'C1702.x',
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
        X                   = -6530,
        Z                   = 400,
        Y                   = -39740,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F6,
        Unknown_18          = 8187,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 5460,
        Z                   = 400,
        Y                   = -40310,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F4,
        Unknown_18          = 8188,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -60,
        Z                   = 400,
        Y                   = -1320,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F7,
        Unknown_18          = 8189,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -6310,
        Z                   = 400,
        Y                   = 40240,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F5,
        Unknown_18          = 8190,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 5540,
        Z                   = 400,
        Y                   = 39770,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F8,
        Unknown_18          = 8191,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -66580,
        Z                   = 400,
        Y                   = 75070,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F4,
        Unknown_18          = 7808,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -74870,
        Z                   = 400,
        Y                   = 66550,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F5,
        Unknown_18          = 7809,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -76050,
        Z                   = 400,
        Y                   = -67860,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F5,
        Unknown_18          = 7810,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -67900,
        Z                   = 400,
        Y                   = -75980,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F6,
        Unknown_18          = 7811,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 67970,
        Z                   = 400,
        Y                   = -75600,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F4,
        Unknown_18          = 7812,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 75900,
        Z                   = 400,
        Y                   = -67970,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F7,
        Unknown_18          = 7813,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 66360,
        Z                   = 400,
        Y                   = 74560,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F5,
        Unknown_18          = 7814,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 74650,
        Z                   = 400,
        Y                   = 66690,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F8,
        Unknown_18          = 7815,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 30,
        TriggerZ            = -50,
        TriggerY            = 39240,
        TriggerRange        = 1000,
        ActorX              = 30,
        ActorZ              = -50,
        ActorY              = 39940,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 80,
        TriggerZ            = -50,
        TriggerY            = -40760,
        TriggerRange        = 1000,
        ActorX              = 80,
        ActorZ              = -50,
        ActorY              = -40050,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -71270,
        TriggerZ            = 0,
        TriggerY            = 71150,
        TriggerRange        = 1000,
        ActorX              = -70740,
        ActorZ              = 0,
        ActorY              = 70800,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -71480,
        TriggerZ            = 0,
        TriggerY            = -71470,
        TriggerRange        = 1000,
        ActorX              = -71860,
        ActorZ              = 0,
        ActorY              = -72030,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 71530,
        TriggerZ            = 0,
        TriggerY            = -71540,
        TriggerRange        = 1000,
        ActorX              = 71990,
        ActorZ              = 0,
        ActorY              = -72000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 71140,
        TriggerZ            = 0,
        TriggerY            = 71150,
        TriggerRange        = 1000,
        ActorX              = 70730,
        ActorZ              = 0,
        ActorY              = 70630,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_35E",          # 00, 0
        "Function_1_3D5",          # 01, 1
        "Function_2_53A",          # 02, 2
        "Function_3_651",          # 03, 3
        "Function_4_768",          # 04, 4
        "Function_5_87F",          # 05, 5
        "Function_6_996",          # 06, 6
        "Function_7_A92",          # 07, 7
        "Function_8_BA9",          # 08, 8
        "Function_9_CB6",          # 09, 9
        "Function_10_D37",         # 0A, 10
        "Function_11_E44",         # 0B, 11
        "Function_12_EC5",         # 0C, 12
        "Function_13_FD2",         # 0D, 13
        "Function_14_1053",        # 0E, 14
        "Function_15_114E",        # 0F, 15
        "Function_16_11C6",        # 10, 16
        "Function_17_12C1",        # 11, 17
        "Function_18_1339",        # 12, 18
        "Function_19_1434",        # 13, 19
        "Function_20_14AC",        # 14, 20
        "Function_21_15A7",        # 15, 21
        "Function_22_161F",        # 16, 22
        "Function_23_171A",        # 17, 23
        "Function_24_1792",        # 18, 24
        "Function_25_189F",        # 19, 25
        "Function_26_1920",        # 1A, 26
        "Function_27_1A2D",        # 1B, 27
        "Function_28_1AAE",        # 1C, 28
        "Function_29_1BA1",        # 1D, 29
        "Function_30_1C94",        # 1E, 30
        "Function_31_1CE2",        # 1F, 31
    )


    def Function_0_35E(): pass

    label("Function_0_35E")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_38E"),
        (101, "loc_395"),
        (102, "loc_39C"),
        (103, "loc_3A3"),
        (104, "loc_3AA"),
        (105, "loc_3B1"),
        (106, "loc_3B8"),
        (107, "loc_3BF"),
        (108, "loc_3C6"),
        (109, "loc_3CD"),
        (SWITCH_DEFAULT, "loc_3D4"),
    )


    label("loc_38E")

    Event(0, 8)
    Jump("loc_3D4")

    label("loc_395")

    Event(0, 10)
    Jump("loc_3D4")

    label("loc_39C")

    Event(0, 12)
    Jump("loc_3D4")

    label("loc_3A3")

    Event(0, 14)
    Jump("loc_3D4")

    label("loc_3AA")

    Event(0, 16)
    Jump("loc_3D4")

    label("loc_3B1")

    Event(0, 18)
    Jump("loc_3D4")

    label("loc_3B8")

    Event(0, 20)
    Jump("loc_3D4")

    label("loc_3BF")

    Event(0, 22)
    Jump("loc_3D4")

    label("loc_3C6")

    Event(0, 24)
    Jump("loc_3D4")

    label("loc_3CD")

    Event(0, 26)
    Jump("loc_3D4")

    label("loc_3D4")

    Return()

    # Function_0_35E end

    def Function_1_3D5(): pass

    label("Function_1_3D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F4, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E7")
    OP_6F(0x0, 0)
    Jump("loc_3EE")

    label("loc_3E7")

    OP_6F(0x0, 60)

    label("loc_3EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_400")
    OP_6F(0x1, 0)
    Jump("loc_407")

    label("loc_400")

    OP_6F(0x1, 60)

    label("loc_407")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_419")
    OP_6F(0x2, 0)
    Jump("loc_420")

    label("loc_419")

    OP_6F(0x2, 60)

    label("loc_420")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F4, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_432")
    OP_6F(0x3, 0)
    Jump("loc_439")

    label("loc_432")

    OP_6F(0x3, 60)

    label("loc_439")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44B")
    OP_6F(0x4, 0)
    Jump("loc_452")

    label("loc_44B")

    OP_6F(0x4, 60)

    label("loc_452")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F5, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_464")
    OP_6F(0x5, 0)
    Jump("loc_46B")

    label("loc_464")

    OP_6F(0x5, 60)

    label("loc_46B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FF, 3)), scpexpr(EXPR_END)), "loc_477")
    SetChrFlags(0x8, 0x80)

    label("loc_477")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FF, 4)), scpexpr(EXPR_END)), "loc_483")
    SetChrFlags(0x9, 0x80)

    label("loc_483")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FF, 5)), scpexpr(EXPR_END)), "loc_48F")
    SetChrFlags(0xA, 0x80)

    label("loc_48F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FF, 6)), scpexpr(EXPR_END)), "loc_49B")
    SetChrFlags(0xB, 0x80)

    label("loc_49B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FF, 7)), scpexpr(EXPR_END)), "loc_4A7")
    SetChrFlags(0xC, 0x80)

    label("loc_4A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D0, 0)), scpexpr(EXPR_END)), "loc_4B3")
    SetChrFlags(0xD, 0x80)

    label("loc_4B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D0, 1)), scpexpr(EXPR_END)), "loc_4BF")
    SetChrFlags(0xE, 0x80)

    label("loc_4BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D0, 2)), scpexpr(EXPR_END)), "loc_4CB")
    SetChrFlags(0xF, 0x80)

    label("loc_4CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D0, 3)), scpexpr(EXPR_END)), "loc_4D7")
    SetChrFlags(0x10, 0x80)

    label("loc_4D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D0, 4)), scpexpr(EXPR_END)), "loc_4E3")
    SetChrFlags(0x11, 0x80)

    label("loc_4E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D0, 5)), scpexpr(EXPR_END)), "loc_4EF")
    SetChrFlags(0x12, 0x80)

    label("loc_4EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D0, 6)), scpexpr(EXPR_END)), "loc_4FB")
    SetChrFlags(0x13, 0x80)

    label("loc_4FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D0, 7)), scpexpr(EXPR_END)), "loc_507")
    SetChrFlags(0x14, 0x80)

    label("loc_507")

    OP_1B(0x0, 0x0, 0x9)
    OP_1B(0x1, 0x0, 0xB)
    OP_1B(0x2, 0x0, 0xD)
    OP_1B(0x3, 0x0, 0xF)
    OP_1B(0x4, 0x0, 0x11)
    OP_1B(0x5, 0x0, 0x13)
    OP_1B(0x6, 0x0, 0x15)
    OP_1B(0x7, 0x0, 0x17)
    OP_1B(0x8, 0x0, 0x19)
    OP_1B(0x9, 0x0, 0x1B)
    Return()

    # Function_1_3D5 end

    def Function_2_53A(): pass

    label("Function_2_53A")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F4, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_612")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x202, 1)"), scpexpr(EXPR_END)), "loc_5A9")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x02\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1FA4)
    Jump("loc_60F")

    label("loc_5A9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\x02\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x02\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_60F")

    Jump("loc_643")

    label("loc_612")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_643")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_53A end

    def Function_3_651(): pass

    label("Function_3_651")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_729")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x136, 1)"), scpexpr(EXPR_END)), "loc_6C0")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\x36\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1FA5)
    Jump("loc_726")

    label("loc_6C0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\x36\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x36\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_726")

    Jump("loc_75A")

    label("loc_729")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_75A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_651 end

    def Function_4_768(): pass

    label("Function_4_768")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_840")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_7D7")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x00得到了\x1F\xFD\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1FA6)
    Jump("loc_83D")

    label("loc_7D7")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
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

    label("loc_83D")

    Jump("loc_871")

    label("loc_840")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_871")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_768 end

    def Function_5_87F(): pass

    label("Function_5_87F")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F4, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_957")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2D3, 1)"), scpexpr(EXPR_END)), "loc_8EE")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x00得到了\x1F\xD3\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1FA7)
    Jump("loc_954")

    label("loc_8EE")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "宝箱里装有\x1F\xD3\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xD3\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_954")

    Jump("loc_988")

    label("loc_957")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_988")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_87F end

    def Function_6_996(): pass

    label("Function_6_996")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A66")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x1E)
    OP_73(0x4)
    OP_6F(0x4, 30)
    AddSepith(0x0, 0x12C)
    AddSepith(0x4, 0x64)
    AddSepith(0x5, 0x64)
    AddSepith(0x6, 0x64)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #12
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
    OP_A2(0x1FA8)
    Jump("loc_A80")

    label("loc_A66")


    AnonymousTalk(    #13
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_A80")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_996 end

    def Function_7_A92(): pass

    label("Function_7_A92")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F5, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B6A")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_B01")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #14
        "\x07\x00得到了\x1F\xFB\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1FA9)
    Jump("loc_B67")

    label("loc_B01")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #15
        (
            "宝箱里装有\x1F\xFB\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFB\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)

    label("loc_B67")

    Jump("loc_B9B")

    label("loc_B6A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #16
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_B9B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_A92 end

    def Function_8_BA9(): pass

    label("Function_8_BA9")

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
    Call(0, 28)
    Call(0, 30)
    Fade(500)
    OP_6D(-60, 200, -64400, 0)
    OP_6C(45000, 0)
    SetChrPos(0x0, -60, 200, -64400, 0)
    SetChrPos(0x1, -60, 200, -64400, 0)
    SetChrPos(0x2, -60, 200, -64400, 0)
    SetChrPos(0x3, -60, 200, -64400, 0)
    EventEnd(0x0)
    Return()

    # Function_8_BA9 end

    def Function_9_CB6(): pass

    label("Function_9_CB6")

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
    Call(0, 28)
    Call(0, 31)
    NewScene("ED6_DT21/C1701   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_9_CB6 end

    def Function_10_D37(): pass

    label("Function_10_D37")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-46700, 200, 46200, 0)
    OP_6C(135000, 0)
    SetChrPos(0x101, -47200, 200, 46700, 0)
    SetChrPos(0x102, -46200, 200, 46700, 0)
    SetChrPos(0xF8, -47200, 200, 45700, 0)
    SetChrPos(0xF9, -46200, 200, 45700, 0)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 29)
    Call(0, 30)
    Fade(500)
    OP_6D(-46770, 200, 48120, 0)
    OP_6C(45000, 0)
    SetChrPos(0x0, -46770, 200, 48120, 0)
    SetChrPos(0x1, -46770, 200, 48120, 0)
    SetChrPos(0x2, -46770, 200, 48120, 0)
    SetChrPos(0x3, -46770, 200, 48120, 0)
    EventEnd(0x0)
    Return()

    # Function_10_D37 end

    def Function_11_E44(): pass

    label("Function_11_E44")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(-46700, 200, 46200, 0)
    OP_6C(135000, 0)
    SetChrPos(0x101, -46200, 200, 45700, 180)
    SetChrPos(0x102, -47200, 200, 45700, 180)
    SetChrPos(0xF8, -46200, 200, 46700, 180)
    SetChrPos(0xF9, -47200, 200, 46700, 180)
    OP_0D()
    Call(0, 29)
    Call(0, 31)
    NewScene("ED6_DT21/C1701   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_11_E44 end

    def Function_12_EC5(): pass

    label("Function_12_EC5")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(46600, 200, 46200, 0)
    OP_6C(135000, 0)
    SetChrPos(0x101, 46100, 200, 46700, 0)
    SetChrPos(0x102, 47100, 200, 46700, 0)
    SetChrPos(0xF8, 46100, 200, 45700, 0)
    SetChrPos(0xF9, 47100, 200, 45700, 0)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 29)
    Call(0, 30)
    Fade(500)
    OP_6D(46620, 200, 48180, 0)
    OP_6C(45000, 0)
    SetChrPos(0x0, 46620, 200, 48180, 0)
    SetChrPos(0x1, 46620, 200, 48180, 0)
    SetChrPos(0x2, 46620, 200, 48180, 0)
    SetChrPos(0x3, 46620, 200, 48180, 0)
    EventEnd(0x0)
    Return()

    # Function_12_EC5 end

    def Function_13_FD2(): pass

    label("Function_13_FD2")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(46600, 200, 46200, 0)
    OP_6C(135000, 0)
    SetChrPos(0x101, 47100, 200, 45700, 180)
    SetChrPos(0x102, 46100, 200, 45700, 180)
    SetChrPos(0xF8, 47100, 200, 46700, 180)
    SetChrPos(0xF9, 46100, 200, 46700, 180)
    OP_0D()
    Call(0, 29)
    Call(0, 31)
    NewScene("ED6_DT21/C1701   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_13_FD2 end

    def Function_14_1053(): pass

    label("Function_14_1053")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(46500, 200, -46100, 0)
    SetChrPos(0x101, 47000, 200, -46600, 180)
    SetChrPos(0x102, 46000, 200, -46600, 180)
    SetChrPos(0xF8, 47000, 200, -45600, 180)
    SetChrPos(0xF9, 46000, 200, -45600, 180)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 28)
    Call(0, 30)
    Fade(500)
    OP_6D(46630, 200, -48040, 0)
    SetChrPos(0x0, 46630, 200, -48040, 180)
    SetChrPos(0x1, 46630, 200, -48040, 180)
    SetChrPos(0x2, 46630, 200, -48040, 180)
    SetChrPos(0x3, 46630, 200, -48040, 180)
    EventEnd(0x0)
    Return()

    # Function_14_1053 end

    def Function_15_114E(): pass

    label("Function_15_114E")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(46500, 200, -46100, 0)
    SetChrPos(0x101, 46000, 200, -45600, 0)
    SetChrPos(0x102, 47000, 200, -45600, 0)
    SetChrPos(0xF8, 46000, 200, -46600, 0)
    SetChrPos(0xF9, 47000, 200, -46600, 0)
    OP_0D()
    Call(0, 28)
    Call(0, 31)
    NewScene("ED6_DT21/C1701   ._SN", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_15_114E end

    def Function_16_11C6(): pass

    label("Function_16_11C6")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-46500, 200, -46000, 0)
    SetChrPos(0x101, -46000, 200, -46500, 180)
    SetChrPos(0x102, -47000, 200, -46500, 180)
    SetChrPos(0xF8, -46000, 200, -45500, 180)
    SetChrPos(0xF9, -47000, 200, -45500, 180)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 28)
    Call(0, 30)
    Fade(500)
    OP_6D(-46470, 200, -47980, 0)
    SetChrPos(0x0, -46470, 200, -47980, 180)
    SetChrPos(0x1, -46470, 200, -47980, 180)
    SetChrPos(0x2, -46470, 200, -47980, 180)
    SetChrPos(0x3, -46470, 200, -47980, 180)
    EventEnd(0x0)
    Return()

    # Function_16_11C6 end

    def Function_17_12C1(): pass

    label("Function_17_12C1")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(-46500, 200, -46000, 0)
    SetChrPos(0x101, -47000, 200, -45500, 0)
    SetChrPos(0x102, -46000, 200, -45500, 0)
    SetChrPos(0xF8, -47000, 200, -46500, 0)
    SetChrPos(0xF9, -46000, 200, -46500, 0)
    OP_0D()
    Call(0, 28)
    Call(0, 31)
    NewScene("ED6_DT21/C1701   ._SN", 105, 0, 0)
    IdleLoop()
    Return()

    # Function_17_12C1 end

    def Function_18_1339(): pass

    label("Function_18_1339")

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
    Call(0, 29)
    Call(0, 30)
    Fade(500)
    OP_6D(130, 200, 64560, 0)
    SetChrPos(0x0, 130, 200, 64560, 180)
    SetChrPos(0x1, 130, 200, 64560, 180)
    SetChrPos(0x2, 130, 200, 64560, 180)
    SetChrPos(0x3, 130, 200, 64560, 180)
    EventEnd(0x0)
    Return()

    # Function_18_1339 end

    def Function_19_1434(): pass

    label("Function_19_1434")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(0, 200, 66500, 0)
    SetChrPos(0x101, -500, 200, 67000, 0)
    SetChrPos(0x102, 500, 200, 67000, 0)
    SetChrPos(0xF8, -500, 200, 66000, 0)
    SetChrPos(0xF9, 500, 200, 66000, 0)
    OP_0D()
    Call(0, 29)
    Call(0, 31)
    NewScene("ED6_DT21/C1703   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_19_1434 end

    def Function_20_14AC(): pass

    label("Function_20_14AC")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-96100, 200, 96700, 0)
    SetChrPos(0x101, -95600, 200, 96200, 180)
    SetChrPos(0x102, -96600, 200, 96200, 180)
    SetChrPos(0xF8, -95600, 200, 97200, 180)
    SetChrPos(0xF9, -96600, 200, 97200, 180)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 28)
    Call(0, 30)
    Fade(500)
    OP_6D(-96090, 200, 94660, 0)
    SetChrPos(0x0, -96090, 200, 94660, 180)
    SetChrPos(0x1, -96090, 200, 94660, 180)
    SetChrPos(0x2, -96090, 200, 94660, 180)
    SetChrPos(0x3, -96090, 200, 94660, 180)
    EventEnd(0x0)
    Return()

    # Function_20_14AC end

    def Function_21_15A7(): pass

    label("Function_21_15A7")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(-96100, 200, 96700, 0)
    SetChrPos(0x101, -96600, 200, 97200, 0)
    SetChrPos(0x102, -95600, 200, 97200, 0)
    SetChrPos(0xF8, -96600, 200, 96200, 0)
    SetChrPos(0xF9, -95600, 200, 96200, 0)
    OP_0D()
    Call(0, 28)
    Call(0, 31)
    NewScene("ED6_DT21/C1703   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_21_15A7 end

    def Function_22_161F(): pass

    label("Function_22_161F")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(96200, 200, 96700, 0)
    SetChrPos(0x101, 96700, 200, 96200, 180)
    SetChrPos(0x102, 95700, 200, 96200, 180)
    SetChrPos(0xF8, 96700, 200, 97200, 180)
    SetChrPos(0xF9, 95700, 200, 97200, 180)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 28)
    Call(0, 30)
    Fade(500)
    OP_6D(96270, 200, 94740, 0)
    SetChrPos(0x0, 96270, 200, 94740, 180)
    SetChrPos(0x1, 96270, 200, 94740, 180)
    SetChrPos(0x2, 96270, 200, 94740, 180)
    SetChrPos(0x3, 96270, 200, 94740, 180)
    EventEnd(0x0)
    Return()

    # Function_22_161F end

    def Function_23_171A(): pass

    label("Function_23_171A")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(96200, 200, 96700, 0)
    SetChrPos(0x101, 95700, 200, 97200, 0)
    SetChrPos(0x102, 96700, 200, 97200, 0)
    SetChrPos(0xF8, 95700, 200, 96200, 0)
    SetChrPos(0xF9, 96700, 200, 96200, 0)
    OP_0D()
    Call(0, 28)
    Call(0, 31)
    NewScene("ED6_DT21/C1703   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_23_171A end

    def Function_24_1792(): pass

    label("Function_24_1792")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(96000, 200, -96500, 0)
    OP_6C(135000, 0)
    SetChrPos(0x101, 95500, 200, -96000, 0)
    SetChrPos(0x102, 96500, 200, -96000, 0)
    SetChrPos(0xF8, 95500, 200, -97000, 0)
    SetChrPos(0xF9, 96500, 200, -97000, 0)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 29)
    Call(0, 30)
    Fade(500)
    OP_6D(95950, 200, -94510, 0)
    OP_6C(45000, 0)
    SetChrPos(0x0, 95950, 200, -94510, 0)
    SetChrPos(0x1, 95950, 200, -94510, 0)
    SetChrPos(0x2, 95950, 200, -94510, 0)
    SetChrPos(0x3, 95950, 200, -94510, 0)
    EventEnd(0x0)
    Return()

    # Function_24_1792 end

    def Function_25_189F(): pass

    label("Function_25_189F")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(96000, 200, -96500, 0)
    OP_6C(135000, 0)
    SetChrPos(0x101, 96500, 200, -97000, 180)
    SetChrPos(0x102, 95500, 200, -97000, 180)
    SetChrPos(0xF8, 96500, 200, -96000, 180)
    SetChrPos(0xF9, 95500, 200, -96000, 180)
    OP_0D()
    Call(0, 29)
    Call(0, 31)
    NewScene("ED6_DT21/C1703   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_25_189F end

    def Function_26_1920(): pass

    label("Function_26_1920")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-96000, 200, -96500, 0)
    OP_6C(135000, 0)
    SetChrPos(0x101, -96500, 200, -96000, 0)
    SetChrPos(0x102, -95500, 200, -96000, 0)
    SetChrPos(0xF8, -96500, 200, -97000, 0)
    SetChrPos(0xF9, -95500, 200, -97000, 0)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 29)
    Call(0, 30)
    Fade(500)
    OP_6D(-96080, 200, -94480, 0)
    OP_6C(45000, 0)
    SetChrPos(0x0, -96080, 200, -94480, 0)
    SetChrPos(0x1, -96080, 200, -94480, 0)
    SetChrPos(0x2, -96080, 200, -94480, 0)
    SetChrPos(0x3, -96080, 200, -94480, 0)
    EventEnd(0x0)
    Return()

    # Function_26_1920 end

    def Function_27_1A2D(): pass

    label("Function_27_1A2D")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(-96000, 200, -96500, 0)
    OP_6C(135000, 0)
    SetChrPos(0x101, -95500, 200, -97000, 180)
    SetChrPos(0x102, -96500, 200, -97000, 180)
    SetChrPos(0xF8, -95500, 200, -96000, 180)
    SetChrPos(0xF9, -96500, 200, -96000, 180)
    OP_0D()
    Call(0, 29)
    Call(0, 31)
    NewScene("ED6_DT21/C1703   ._SN", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_27_1A2D end

    def Function_28_1AAE(): pass

    label("Function_28_1AAE")

    LoadEffect(0x0, "map\\\\mp049_21.eff")
    PlayEffect(0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Return()

    # Function_28_1AAE end

    def Function_29_1BA1(): pass

    label("Function_29_1BA1")

    LoadEffect(0x0, "map\\\\mp049_22.eff")
    PlayEffect(0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Return()

    # Function_29_1BA1 end

    def Function_30_1C94(): pass

    label("Function_30_1C94")


    def lambda_1C9A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1C9A)

    def lambda_1CAC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1CAC)

    def lambda_1CBE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1CBE)

    def lambda_1CD0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1CD0)
    Sleep(2500)
    Return()

    # Function_30_1C94 end

    def Function_31_1CE2(): pass

    label("Function_31_1CE2")


    def lambda_1CE8():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1CE8)

    def lambda_1CFA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1CFA)

    def lambda_1D0C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1D0C)

    def lambda_1D1E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1D1E)
    Sleep(2000)
    Return()

    # Function_31_1CE2 end

    SaveToFile()

Try(main)
