from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C1602   ._SN',
        MapName             = 'Bose',
        Location            = 'C1602.x',
        MapIndex            = 250,
        MapDefaultBGM       = "ed60125",
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
        'ED6_DT29/CH12450 ._CH',             # 00
        'ED6_DT29/CH12451 ._CH',             # 01
        'ED6_DT09/CH10840 ._CH',             # 02
        'ED6_DT09/CH10841 ._CH',             # 03
        'ED6_DT29/CH12460 ._CH',             # 04
        'ED6_DT29/CH12461 ._CH',             # 05
        'ED6_DT09/CH10550 ._CH',             # 06
        'ED6_DT09/CH10551 ._CH',             # 07
        'ED6_DT29/CH12500 ._CH',             # 08
        'ED6_DT29/CH12501 ._CH',             # 09
        'ED6_DT29/CH12560 ._CH',             # 0A
        'ED6_DT29/CH12561 ._CH',             # 0B
    )

    AddCharChipPat(
        'ED6_DT29/CH12450P._CP',             # 00
        'ED6_DT29/CH12451P._CP',             # 01
        'ED6_DT09/CH10840P._CP',             # 02
        'ED6_DT09/CH10841P._CP',             # 03
        'ED6_DT29/CH12460P._CP',             # 04
        'ED6_DT29/CH12461P._CP',             # 05
        'ED6_DT09/CH10550P._CP',             # 06
        'ED6_DT09/CH10551P._CP',             # 07
        'ED6_DT29/CH12500P._CP',             # 08
        'ED6_DT29/CH12501P._CP',             # 09
        'ED6_DT29/CH12560P._CP',             # 0A
        'ED6_DT29/CH12561P._CP',             # 0B
    )

    DeclMonster(
        X                   = 33560,
        Z                   = 0,
        Y                   = -17800,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3C6,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 9220,
        Z                   = -1000,
        Y                   = -5220,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3C8,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 10130,
        Z                   = 0,
        Y                   = 41950,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3C7,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -31690,
        Z                   = 0,
        Y                   = 17530,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3C6,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -22920,
        Z                   = -1000,
        Y                   = 3720,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3C7,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -17070,
        Z                   = -500,
        Y                   = -6360,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3C8,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 159370,
        Z                   = 0,
        Y                   = -1020,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3C7,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 184150,
        Z                   = -500,
        Y                   = -2380,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3C3,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 186100,
        Z                   = 0,
        Y                   = 12660,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3C3,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 209310,
        Z                   = 0,
        Y                   = -1090,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3C6,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 230690,
        Z                   = -500,
        Y                   = -3880,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3C3,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 16510,
        TriggerZ            = 0,
        TriggerY            = 40840,
        TriggerRange        = 1000,
        ActorX              = 17170,
        ActorZ              = 0,
        ActorY              = 40840,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 245230,
        TriggerZ            = 0,
        TriggerY            = 25460,
        TriggerRange        = 1000,
        ActorX              = 245680,
        ActorZ              = 0,
        ActorY              = 25970,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 9970,
        TriggerZ            = 0,
        TriggerY            = 48740,
        TriggerRange        = 1000,
        ActorX              = 10010,
        ActorZ              = 0,
        ActorY              = 49440,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -16170,
        TriggerZ            = 0,
        TriggerY            = 17900,
        TriggerRange        = 1000,
        ActorX              = -15800,
        ActorZ              = 0,
        ActorY              = 18460,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2CE",          # 00, 0
        "Function_1_2CF",          # 01, 1
        "Function_2_3BD",          # 02, 2
        "Function_3_4D4",          # 03, 3
        "Function_4_596",          # 04, 4
        "Function_5_6AD",          # 05, 5
    )


    def Function_0_2CE(): pass

    label("Function_0_2CE")

    Return()

    # Function_0_2CE end

    def Function_1_2CF(): pass

    label("Function_1_2CF")

    OP_22(0x1C7, 0x0, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x372, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E6")
    OP_6F(0x0, 0)
    Jump("loc_2ED")

    label("loc_2E6")

    OP_6F(0x0, 60)

    label("loc_2ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x372, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FF")
    OP_6F(0x1, 0)
    Jump("loc_306")

    label("loc_2FF")

    OP_6F(0x1, 60)

    label("loc_306")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x372, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_318")
    OP_6F(0x2, 0)
    Jump("loc_31F")

    label("loc_318")

    OP_6F(0x2, 60)

    label("loc_31F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x372, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_331")
    OP_6F(0x3, 0)
    Jump("loc_338")

    label("loc_331")

    OP_6F(0x3, 60)

    label("loc_338")

    OP_51(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3B2")
    OP_4F(0x2A, (scpexpr(EXPR_PUSH_LONG, 0x578), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3BC")

    label("loc_3B2")

    OP_4F(0x2A, (scpexpr(EXPR_PUSH_LONG, 0x12C), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3BC")

    Return()

    # Function_1_2CF end

    def Function_2_3BD(): pass

    label("Function_2_3BD")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x372, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_495")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x8B, 1)"), scpexpr(EXPR_END)), "loc_42C")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x8B\x00\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B90)
    Jump("loc_492")

    label("loc_42C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\x8B\x00\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x8B\x00\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_492")

    Jump("loc_4C6")

    label("loc_495")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_4C6")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_3BD end

    def Function_3_4D4(): pass

    label("Function_3_4D4")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x372, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56A")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x1E)
    OP_73(0x1)
    OP_6F(0x1, 30)
    AddSepith(0x0, 0x64)
    AddSepith(0x6, 0x64)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #3
        (
            "\x07\x00得到了\x07\x02#56I地之耀晶片×１００\x01",
            "\x07\x02#61I幻之耀晶片×１００\x01",
            "\x07\x00。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x1B92)
    Jump("loc_584")

    label("loc_56A")


    AnonymousTalk(    #4
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_584")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_4D4 end

    def Function_4_596(): pass

    label("Function_4_596")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x372, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_605")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x00得到了\x1F\xFE\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B94)
    Jump("loc_66B")

    label("loc_605")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #6
        (
            "宝箱里装有\x1F\xFE\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFE\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_66B")

    Jump("loc_69F")

    label("loc_66E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_69F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_596 end

    def Function_5_6AD(): pass

    label("Function_5_6AD")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x372, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_785")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1E3, 1)"), scpexpr(EXPR_END)), "loc_71C")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x00得到了\x1F\xE3\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B95)
    Jump("loc_782")

    label("loc_71C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #9
        (
            "宝箱里装有\x1F\xE3\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xE3\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_782")

    Jump("loc_7B6")

    label("loc_785")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_7B6")

    Sleep(30)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_80E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x30)"), scpexpr(EXPR_END)), "loc_7D5")
    Jump("loc_80E")

    label("loc_7D5")


    AnonymousTalk(    #11
        "\x07\x00得到了\x1F\xE3\x01\x07\x00的食谱。\x02",
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #12
        "\x1F\xE3\x01\x07\x00的做法已经学会了。\x02",
    )

    CloseMessageWindow()

    label("loc_80E")

    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_6AD end

    SaveToFile()

Try(main)
