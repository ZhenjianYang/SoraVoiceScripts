from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 洛连特

    CreateScenaFile(
        FileName            = 'C0701   ._SN',
        MapName             = 'Rolent',
        Location            = 'C0701.x',
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
        'ED6_DT29/CH12652 ._CH',             # 0C
        'ED6_DT29/CH12652 ._CH',             # 0D
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
        'ED6_DT29/CH12652P._CP',             # 0C
        'ED6_DT29/CH12652P._CP',             # 0D
    )

    DeclMonster(
        X                   = 680,
        Z                   = 400,
        Y                   = 47850,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3E9,
        Unknown_18          = 8130,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 0,
        Z                   = -50,
        Y                   = 0,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3EA,
        Unknown_18          = 8131,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 25540,
        Z                   = 0,
        Y                   = 47760,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3E8,
        Unknown_18          = 8132,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 45190,
        Z                   = 7600,
        Y                   = 7900,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3EA,
        Unknown_18          = 8133,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -46750,
        Z                   = 400,
        Y                   = 4450,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3E9,
        Unknown_18          = 8134,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -47010,
        Z                   = 400,
        Y                   = -7800,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3EA,
        Unknown_18          = 8135,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 29120,
        Z                   = 400,
        Y                   = -29450,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3E8,
        Unknown_18          = 8136,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 37280,
        Z                   = 400,
        Y                   = -37230,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3E9,
        Unknown_18          = 8137,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 330,
        Z                   = 0,
        Y                   = -70120,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3EA,
        Unknown_18          = 8138,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -5350,
        Z                   = 400,
        Y                   = -76120,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3E8,
        Unknown_18          = 8139,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 5780,
        Z                   = 400,
        Y                   = -75920,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3E8,
        Unknown_18          = 8140,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 15810,
        TriggerZ            = 0,
        TriggerY            = -14950,
        TriggerRange        = 1000,
        ActorX              = 15310,
        ActorZ              = 0,
        ActorY              = -15440,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 32640,
        TriggerZ            = 0,
        TriggerY            = -33770,
        TriggerRange        = 1000,
        ActorX              = 33140,
        ActorZ              = 0,
        ActorY              = -33270,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 0,
        TriggerZ            = 400,
        TriggerY            = -16600,
        TriggerRange        = 1000,
        ActorX              = 0,
        ActorZ              = 400,
        ActorY              = -15980,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -16300,
        TriggerZ            = 7600,
        TriggerY            = -50,
        TriggerRange        = 1000,
        ActorX              = -16980,
        ActorZ              = 7600,
        ActorY              = -50,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2DE",          # 00, 0
        "Function_1_2FD",          # 01, 1
        "Function_2_41C",          # 02, 2
        "Function_3_533",          # 03, 3
        "Function_4_64A",          # 04, 4
        "Function_5_761",          # 05, 5
        "Function_6_878",          # 06, 6
        "Function_7_973",          # 07, 7
        "Function_8_9F6",          # 08, 8
        "Function_9_B03",          # 09, 9
        "Function_10_B84",         # 0A, 10
        "Function_11_C77",         # 0B, 11
        "Function_12_D6A",         # 0C, 12
        "Function_13_DB8",         # 0D, 13
    )


    def Function_0_2DE(): pass

    label("Function_0_2DE")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_2EE"),
        (101, "loc_2F5"),
        (SWITCH_DEFAULT, "loc_2FC"),
    )


    label("loc_2EE")

    Event(0, 6)
    Jump("loc_2FC")

    label("loc_2F5")

    Event(0, 8)
    Jump("loc_2FC")

    label("loc_2FC")

    Return()

    # Function_0_2DE end

    def Function_1_2FD(): pass

    label("Function_1_2FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30F")
    OP_6F(0x0, 0)
    Jump("loc_316")

    label("loc_30F")

    OP_6F(0x0, 60)

    label("loc_316")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_328")
    OP_6F(0x1, 0)
    Jump("loc_32F")

    label("loc_328")

    OP_6F(0x1, 60)

    label("loc_32F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_341")
    OP_6F(0x2, 0)
    Jump("loc_348")

    label("loc_341")

    OP_6F(0x2, 60)

    label("loc_348")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35A")
    OP_6F(0x3, 0)
    Jump("loc_361")

    label("loc_35A")

    OP_6F(0x3, 60)

    label("loc_361")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F8, 2)), scpexpr(EXPR_END)), "loc_36D")
    SetChrFlags(0x8, 0x80)

    label("loc_36D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F8, 3)), scpexpr(EXPR_END)), "loc_379")
    SetChrFlags(0x9, 0x80)

    label("loc_379")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F8, 4)), scpexpr(EXPR_END)), "loc_385")
    SetChrFlags(0xA, 0x80)

    label("loc_385")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F8, 5)), scpexpr(EXPR_END)), "loc_391")
    SetChrFlags(0xB, 0x80)

    label("loc_391")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F8, 6)), scpexpr(EXPR_END)), "loc_39D")
    SetChrFlags(0xC, 0x80)

    label("loc_39D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F8, 7)), scpexpr(EXPR_END)), "loc_3A9")
    SetChrFlags(0xD, 0x80)

    label("loc_3A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F9, 0)), scpexpr(EXPR_END)), "loc_3B5")
    SetChrFlags(0xE, 0x80)

    label("loc_3B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F9, 1)), scpexpr(EXPR_END)), "loc_3C1")
    SetChrFlags(0xF, 0x80)

    label("loc_3C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F9, 2)), scpexpr(EXPR_END)), "loc_3CD")
    SetChrFlags(0x10, 0x80)

    label("loc_3CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F9, 3)), scpexpr(EXPR_END)), "loc_3D9")
    SetChrFlags(0x11, 0x80)

    label("loc_3D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F9, 4)), scpexpr(EXPR_END)), "loc_3E5")
    SetChrFlags(0x12, 0x80)

    label("loc_3E5")

    OP_51(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xCF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xCF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xCF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xCF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1B(0x0, 0x0, 0x7)
    OP_1B(0x1, 0x0, 0x9)
    Return()

    # Function_1_2FD end

    def Function_2_41C(): pass

    label("Function_2_41C")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F4")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x200, 1)"), scpexpr(EXPR_END)), "loc_48B")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x00\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F01)
    Jump("loc_4F1")

    label("loc_48B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\x00\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x00\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_4F1")

    Jump("loc_525")

    label("loc_4F4")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_525")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_41C end

    def Function_3_533(): pass

    label("Function_3_533")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60B")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_5A2")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\xFC\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F02)
    Jump("loc_608")

    label("loc_5A2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\xFC\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFC\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_608")

    Jump("loc_63C")

    label("loc_60B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_63C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_533 end

    def Function_4_64A(): pass

    label("Function_4_64A")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_722")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x8C, 1)"), scpexpr(EXPR_END)), "loc_6B9")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x00得到了\x1F\x8C\x00\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F03)
    Jump("loc_71F")

    label("loc_6B9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "宝箱里装有\x1F\x8C\x00\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x8C\x00\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_71F")

    Jump("loc_753")

    label("loc_722")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_753")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_64A end

    def Function_5_761(): pass

    label("Function_5_761")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_839")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x131, 1)"), scpexpr(EXPR_END)), "loc_7D0")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x00得到了\x1F\x31\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F05)
    Jump("loc_836")

    label("loc_7D0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "宝箱里装有\x1F\x31\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x31\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_836")

    Jump("loc_86A")

    label("loc_839")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_86A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_761 end

    def Function_6_878(): pass

    label("Function_6_878")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(0, 200, 84750, 0)
    SetChrPos(0x101, 500, -50, 84250, 180)
    SetChrPos(0x102, -500, -50, 84250, 180)
    SetChrPos(0xF8, 500, -50, 85250, 180)
    SetChrPos(0xF9, -500, -50, 85250, 180)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Call(0, 10)
    Call(0, 12)
    Fade(500)
    OP_6D(80, 200, 82700, 0)
    SetChrPos(0x0, 80, 200, 82700, 180)
    SetChrPos(0x1, 80, 200, 82700, 180)
    SetChrPos(0x2, 80, 200, 82700, 180)
    SetChrPos(0x3, 80, 200, 82700, 180)
    EventEnd(0x0)
    Return()

    # Function_6_878 end

    def Function_7_973(): pass

    label("Function_7_973")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(0, 200, 84750, 0)
    SetChrPos(0x101, -500, -50, 85250, 0)
    SetChrPos(0x102, 500, -50, 85250, 0)
    SetChrPos(0xF8, -500, -50, 84250, 0)
    SetChrPos(0xF9, 500, -50, 84250, 0)
    OP_0D()
    Call(0, 10)
    Call(0, 13)
    FadeToDark(1000, 0, -1)
    OP_0D()
    NewScene("ED6_DT21/C0700   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_7_973 end

    def Function_8_9F6(): pass

    label("Function_8_9F6")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(0, 3800, -124480, 0)
    OP_6C(225000, 0)
    SetChrPos(0x101, -500, 3800, -123980, 0)
    SetChrPos(0x102, 500, 3800, -123980, 0)
    SetChrPos(0xF8, -500, 3800, -124980, 0)
    SetChrPos(0xF9, 500, 3800, -124980, 0)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Call(0, 11)
    Call(0, 12)
    Fade(500)
    OP_6D(80, 3550, -120330, 0)
    OP_6C(315000, 0)
    SetChrPos(0x0, 80, 3550, -120330, 0)
    SetChrPos(0x1, 80, 3550, -120330, 0)
    SetChrPos(0x2, 80, 3550, -120330, 0)
    SetChrPos(0x3, 80, 3550, -120330, 0)
    EventEnd(0x0)
    Return()

    # Function_8_9F6 end

    def Function_9_B03(): pass

    label("Function_9_B03")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(0, 3800, -124480, 0)
    OP_6C(225000, 0)
    SetChrPos(0x101, 500, 3800, -124980, 180)
    SetChrPos(0x102, -500, 3800, -124980, 180)
    SetChrPos(0xF8, 500, 3800, -123980, 180)
    SetChrPos(0xF9, -500, 3800, -123980, 180)
    OP_0D()
    Call(0, 11)
    Call(0, 13)
    NewScene("ED6_DT21/C0702   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_9_B03 end

    def Function_10_B84(): pass

    label("Function_10_B84")

    LoadEffect(0x0, "map\\\\mp049_21.eff")
    PlayEffect(0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Return()

    # Function_10_B84 end

    def Function_11_C77(): pass

    label("Function_11_C77")

    LoadEffect(0x0, "map\\\\mp049_22.eff")
    PlayEffect(0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Return()

    # Function_11_C77 end

    def Function_12_D6A(): pass

    label("Function_12_D6A")


    def lambda_D70():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_D70)

    def lambda_D82():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_D82)

    def lambda_D94():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_D94)

    def lambda_DA6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_DA6)
    Sleep(2500)
    Return()

    # Function_12_D6A end

    def Function_13_DB8(): pass

    label("Function_13_DB8")


    def lambda_DBE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_DBE)

    def lambda_DD0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_DD0)

    def lambda_DE2():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_DE2)

    def lambda_DF4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_DF4)
    Sleep(2000)
    Return()

    # Function_13_DB8 end

    SaveToFile()

Try(main)
