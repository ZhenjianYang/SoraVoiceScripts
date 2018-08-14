from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M7410   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7410.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60225",
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
        '',                                     # 9
        '',                                     # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
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
        'ED6_DT29/CH14040 ._CH',             # 00
        'ED6_DT29/CH14040 ._CH',             # 01
        'ED6_DT29/CH14880 ._CH',             # 02
        'ED6_DT29/CH14880 ._CH',             # 03
        'ED6_DT29/CH14890 ._CH',             # 04
        'ED6_DT29/CH14890 ._CH',             # 05
        'ED6_DT29/CH14870 ._CH',             # 06
        'ED6_DT29/CH14870 ._CH',             # 07
        'ED6_DT29/CH14820 ._CH',             # 08
        'ED6_DT29/CH14820 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT29/CH14040P._CP',             # 00
        'ED6_DT29/CH14040P._CP',             # 01
        'ED6_DT29/CH14880P._CP',             # 02
        'ED6_DT29/CH14880P._CP',             # 03
        'ED6_DT29/CH14890P._CP',             # 04
        'ED6_DT29/CH14890P._CP',             # 05
        'ED6_DT29/CH14870P._CP',             # 06
        'ED6_DT29/CH14870P._CP',             # 07
        'ED6_DT29/CH14820P._CP',             # 08
        'ED6_DT29/CH14820P._CP',             # 09
    )

    DeclMonster(
        X                   = 17160,
        Z                   = 0,
        Y                   = -108660,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x322,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 16990,
        Z                   = 0,
        Y                   = -193200,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x324,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 20720,
        Z                   = 0,
        Y                   = -196940,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x324,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 17050,
        Z                   = 0,
        Y                   = -200750,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x324,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 13260,
        Z                   = 0,
        Y                   = -197040,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x324,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 19650,
        Z                   = 0,
        Y                   = 171100,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x320,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 69000,
        TriggerZ            = 0,
        TriggerY            = 63000,
        TriggerRange        = 1000,
        ActorX              = 69000,
        ActorZ              = 1000,
        ActorY              = 63000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 69000,
        TriggerZ            = 0,
        TriggerY            = 113000,
        TriggerRange        = 1000,
        ActorX              = 69000,
        ActorZ              = 1000,
        ActorY              = 113000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 18500,
        TriggerZ            = 0,
        TriggerY            = -197000,
        TriggerRange        = 1000,
        ActorX              = 18500,
        ActorZ              = 1000,
        ActorY              = -197000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 15500,
        TriggerZ            = 0,
        TriggerY            = -197000,
        TriggerRange        = 1000,
        ActorX              = 15500,
        ActorZ              = 1000,
        ActorY              = -197000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_232",          # 00, 0
        "Function_1_233",          # 01, 1
        "Function_2_2E5",          # 02, 2
        "Function_3_405",          # 03, 3
        "Function_4_525",          # 04, 4
        "Function_5_5A2",          # 05, 5
    )


    def Function_0_232(): pass

    label("Function_0_232")

    Return()

    # Function_0_232 end

    def Function_1_233(): pass

    label("Function_1_233")

    OP_51(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x15, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x15, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x590, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_292")
    OP_6F(0x0, 0)
    Jump("loc_299")

    label("loc_292")

    OP_6F(0x0, 60)

    label("loc_299")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x590, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AB")
    OP_6F(0x1, 0)
    Jump("loc_2B2")

    label("loc_2AB")

    OP_6F(0x1, 60)

    label("loc_2B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x590, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C4")
    OP_6F(0x2, 0)
    Jump("loc_2CB")

    label("loc_2C4")

    OP_6F(0x2, 60)

    label("loc_2CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x590, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DD")
    OP_6F(0x1F, 0)
    Jump("loc_2E4")

    label("loc_2DD")

    OP_6F(0x1F, 60)

    label("loc_2E4")

    Return()

    # Function_1_233 end

    def Function_2_2E5(): pass

    label("Function_2_2E5")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x590, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C6")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x206, 1)"), scpexpr(EXPR_END)), "loc_357")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x06\x02\x07\x00。\x02",
    )

    Jump("loc_33C")

    label("loc_33C")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2C84)
    Jump("loc_3C3")

    label("loc_357")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\x06\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x06\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_3A4")

    label("loc_3A4")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_3C3")

    Jump("loc_3F7")

    label("loc_3C6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_3F7")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_2E5 end

    def Function_3_405(): pass

    label("Function_3_405")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x590, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E6")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x177, 1)"), scpexpr(EXPR_END)), "loc_477")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\x77\x01\x07\x00。\x02",
    )

    Jump("loc_45C")

    label("loc_45C")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2C85)
    Jump("loc_4E3")

    label("loc_477")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\x77\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x77\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_4C4")

    label("loc_4C4")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_4E3")

    Jump("loc_517")

    label("loc_4E6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_517")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_405 end

    def Function_4_525(): pass

    label("Function_4_525")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x590, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_576")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x1E)
    OP_73(0x2)
    OP_6F(0x2, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    Call(6, 24)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2C86)
    Jump("loc_590")

    label("loc_576")


    AnonymousTalk(    #6
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_590")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_525 end

    def Function_5_5A2(): pass

    label("Function_5_5A2")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x590, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_683")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1F, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x182, 1)"), scpexpr(EXPR_END)), "loc_614")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #7
        "\x07\x00得到了\x1F\x82\x01\x07\x00。\x02",
    )

    Jump("loc_5F9")

    label("loc_5F9")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2C87)
    Jump("loc_680")

    label("loc_614")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        (
            "宝箱里装有\x1F\x82\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x82\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_661")

    label("loc_661")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1F, 60)
    OP_70(0x1F, 0x0)

    label("loc_680")

    Jump("loc_6B4")

    label("loc_683")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_6B4")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_5A2 end

    SaveToFile()

Try(main)
