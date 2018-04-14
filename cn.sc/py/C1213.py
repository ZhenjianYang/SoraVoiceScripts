from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 柏斯

    CreateScenaFile(
        FileName            = 'C1213   ._SN',
        MapName             = 'Bose',
        Location            = 'C1213.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60033",
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
        'ED6_DT09/CH10410 ._CH',             # 00
        'ED6_DT09/CH10411 ._CH',             # 01
        'ED6_DT09/CH10420 ._CH',             # 02
        'ED6_DT09/CH10421 ._CH',             # 03
        'ED6_DT09/CH10430 ._CH',             # 04
        'ED6_DT09/CH10431 ._CH',             # 05
        'ED6_DT09/CH10440 ._CH',             # 06
        'ED6_DT09/CH10441 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT09/CH10410P._CP',             # 00
        'ED6_DT09/CH10411P._CP',             # 01
        'ED6_DT09/CH10420P._CP',             # 02
        'ED6_DT09/CH10421P._CP',             # 03
        'ED6_DT09/CH10430P._CP',             # 04
        'ED6_DT09/CH10431P._CP',             # 05
        'ED6_DT09/CH10440P._CP',             # 06
        'ED6_DT09/CH10441P._CP',             # 07
    )

    DeclMonster(
        X                   = -12480,
        Z                   = 0,
        Y                   = -20,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x90,
        Unknown_18          = 7076,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 12540,
        Z                   = 0,
        Y                   = 80,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x90,
        Unknown_18          = 7077,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -70,
        Z                   = 0,
        Y                   = 4810,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x90,
        Unknown_18          = 7078,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 5870,
        Z                   = 0,
        Y                   = -210,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x90,
        Unknown_18          = 7079,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -5700,
        Z                   = 0,
        Y                   = -130,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x90,
        Unknown_18          = 7080,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 4430,
        TriggerZ            = 0,
        TriggerY            = -22590,
        TriggerRange        = 1000,
        ActorX              = 4430,
        ActorZ              = 0,
        ActorY              = -23210,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -4600,
        TriggerZ            = 0,
        TriggerY            = -22590,
        TriggerRange        = 1000,
        ActorX              = -4690,
        ActorZ              = 0,
        ActorY              = -23250,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -19260,
        TriggerZ            = 0,
        TriggerY            = 12750,
        TriggerRange        = 1000,
        ActorX              = -19730,
        ActorZ              = 0,
        ActorY              = 13160,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -12760,
        TriggerZ            = 0,
        TriggerY            = 19190,
        TriggerRange        = 1000,
        ActorX              = -13160,
        ActorZ              = 0,
        ActorY              = 19720,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -4500,
        TriggerZ            = 0,
        TriggerY            = 22580,
        TriggerRange        = 1000,
        ActorX              = -4590,
        ActorZ              = 0,
        ActorY              = 23200,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 4570,
        TriggerZ            = 0,
        TriggerY            = 22620,
        TriggerRange        = 1000,
        ActorX              = 4570,
        ActorZ              = 0,
        ActorY              = 23280,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 12790,
        TriggerZ            = 0,
        TriggerY            = 19090,
        TriggerRange        = 1000,
        ActorX              = 13170,
        ActorZ              = 0,
        ActorY              = 19650,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 19110,
        TriggerZ            = 0,
        TriggerY            = 12780,
        TriggerRange        = 1000,
        ActorX              = 19700,
        ActorZ              = 0,
        ActorY              = 13250,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 60,
        TriggerZ            = 0,
        TriggerY            = -700,
        TriggerRange        = 1000,
        ActorX              = 0,
        ActorZ              = 0,
        ActorY              = 0,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2BA",          # 00, 0
        "Function_1_2BB",          # 01, 1
        "Function_2_3D9",          # 02, 2
        "Function_3_4F0",          # 03, 3
        "Function_4_607",          # 04, 4
        "Function_5_71E",          # 05, 5
        "Function_6_835",          # 06, 6
        "Function_7_94C",          # 07, 7
        "Function_8_A63",          # 08, 8
        "Function_9_BCD",          # 09, 9
        "Function_10_CE4",         # 0A, 10
    )


    def Function_0_2BA(): pass

    label("Function_0_2BA")

    Return()

    # Function_0_2BA end

    def Function_1_2BB(): pass

    label("Function_1_2BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CD")
    OP_6F(0x0, 0)
    Jump("loc_2D4")

    label("loc_2CD")

    OP_6F(0x0, 60)

    label("loc_2D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E6")
    OP_6F(0x1, 0)
    Jump("loc_2ED")

    label("loc_2E6")

    OP_6F(0x1, 60)

    label("loc_2ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FF")
    OP_6F(0x2, 0)
    Jump("loc_306")

    label("loc_2FF")

    OP_6F(0x2, 60)

    label("loc_306")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_318")
    OP_6F(0x3, 0)
    Jump("loc_31F")

    label("loc_318")

    OP_6F(0x3, 60)

    label("loc_31F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_331")
    OP_6F(0x4, 0)
    Jump("loc_338")

    label("loc_331")

    OP_6F(0x4, 60)

    label("loc_338")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34A")
    OP_6F(0x5, 0)
    Jump("loc_351")

    label("loc_34A")

    OP_6F(0x5, 60)

    label("loc_351")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_363")
    OP_6F(0x6, 0)
    Jump("loc_36A")

    label("loc_363")

    OP_6F(0x6, 60)

    label("loc_36A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37C")
    OP_6F(0x7, 0)
    Jump("loc_383")

    label("loc_37C")

    OP_6F(0x7, 60)

    label("loc_383")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36B, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_395")
    OP_6F(0x8, 0)
    Jump("loc_39C")

    label("loc_395")

    OP_6F(0x8, 60)

    label("loc_39C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x374, 4)), scpexpr(EXPR_END)), "loc_3A8")
    SetChrFlags(0x8, 0x80)

    label("loc_3A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x374, 5)), scpexpr(EXPR_END)), "loc_3B4")
    SetChrFlags(0x9, 0x80)

    label("loc_3B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x374, 6)), scpexpr(EXPR_END)), "loc_3C0")
    SetChrFlags(0xA, 0x80)

    label("loc_3C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x374, 7)), scpexpr(EXPR_END)), "loc_3CC")
    SetChrFlags(0xB, 0x80)

    label("loc_3CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x375, 0)), scpexpr(EXPR_END)), "loc_3D8")
    SetChrFlags(0xC, 0x80)

    label("loc_3D8")

    Return()

    # Function_1_2BB end

    def Function_2_3D9(): pass

    label("Function_2_3D9")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B1")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_448")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\xFB\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B55)
    Jump("loc_4AE")

    label("loc_448")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\xFB\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFB\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_4AE")

    Jump("loc_4E2")

    label("loc_4B1")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_4E2")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_3D9 end

    def Function_3_4F0(): pass

    label("Function_3_4F0")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C8")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_55F")
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
    OP_A2(0x1B56)
    Jump("loc_5C5")

    label("loc_55F")

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

    label("loc_5C5")

    Jump("loc_5F9")

    label("loc_5C8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_5F9")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_4F0 end

    def Function_4_607(): pass

    label("Function_4_607")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6DF")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x202, 1)"), scpexpr(EXPR_END)), "loc_676")
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
    OP_A2(0x1B57)
    Jump("loc_6DC")

    label("loc_676")

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

    label("loc_6DC")

    Jump("loc_710")

    label("loc_6DF")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_710")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_607 end

    def Function_5_71E(): pass

    label("Function_5_71E")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F6")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x294, 1)"), scpexpr(EXPR_END)), "loc_78D")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x00得到了\x1F\x94\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B58)
    Jump("loc_7F3")

    label("loc_78D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "宝箱里装有\x1F\x94\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x94\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_7F3")

    Jump("loc_827")

    label("loc_7F6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_827")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_71E end

    def Function_6_835(): pass

    label("Function_6_835")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_90D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x206, 1)"), scpexpr(EXPR_END)), "loc_8A4")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #12
        "\x07\x00得到了\x1F\x06\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B59)
    Jump("loc_90A")

    label("loc_8A4")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        (
            "宝箱里装有\x1F\x06\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x06\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_90A")

    Jump("loc_93E")

    label("loc_90D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_93E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_835 end

    def Function_7_94C(): pass

    label("Function_7_94C")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A24")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_9BB")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #15
        "\x07\x00得到了\x1F\xF6\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B5A)
    Jump("loc_A21")

    label("loc_9BB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #16
        (
            "宝箱里装有\x1F\xF6\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xF6\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)

    label("loc_A21")

    Jump("loc_A55")

    label("loc_A24")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #17
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_A55")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_94C end

    def Function_8_A63(): pass

    label("Function_8_A63")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B3B")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1E0, 1)"), scpexpr(EXPR_END)), "loc_AD2")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #18
        "\x07\x00得到了\x1F\xE0\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B5B)
    Jump("loc_B38")

    label("loc_AD2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #19
        (
            "宝箱里装有\x1F\xE0\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xE0\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)

    label("loc_B38")

    Jump("loc_B6C")

    label("loc_B3B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #20
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_B6C")

    Sleep(30)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BC4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x14)"), scpexpr(EXPR_END)), "loc_B8B")
    Jump("loc_BC4")

    label("loc_B8B")


    AnonymousTalk(    #21
        "\x07\x00得到了\x1F\xE0\x01\x07\x00的食谱。\x02",
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #22
        "\x1F\xE0\x01\x07\x00的做法已经学会了。\x02",
    )

    CloseMessageWindow()

    label("loc_BC4")

    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_A63 end

    def Function_9_BCD(): pass

    label("Function_9_BCD")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CA5")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x7, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_C3C")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #23
        "\x07\x00得到了\x1F\xFE\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B5C)
    Jump("loc_CA2")

    label("loc_C3C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #24
        (
            "宝箱里装有\x1F\xFE\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFE\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x7, 60)
    OP_70(0x7, 0x0)

    label("loc_CA2")

    Jump("loc_CD6")

    label("loc_CA5")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #25
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_CD6")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_BCD end

    def Function_10_CE4(): pass

    label("Function_10_CE4")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36B, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DBC")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x8, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x141, 1)"), scpexpr(EXPR_END)), "loc_D53")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #26
        "\x07\x00得到了\x1F\x41\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B5D)
    Jump("loc_DB9")

    label("loc_D53")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #27
        (
            "宝箱里装有\x1F\x41\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x41\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x8, 60)
    OP_70(0x8, 0x0)

    label("loc_DB9")

    Jump("loc_DED")

    label("loc_DBC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #28
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_DED")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_CE4 end

    SaveToFile()

Try(main)
