from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'U4404   ._SN',
        MapName             = 'gaiden2',
        Location            = 'U4404.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60221",
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
        'ED6_DT29/CH14450 ._CH',             # 00
        'ED6_DT29/CH14451 ._CH',             # 01
        'ED6_DT29/CH14730 ._CH',             # 02
        'ED6_DT29/CH14730 ._CH',             # 03
        'ED6_DT29/CH14790 ._CH',             # 04
        'ED6_DT29/CH14791 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT29/CH14450P._CP',             # 00
        'ED6_DT29/CH14451P._CP',             # 01
        'ED6_DT29/CH14730P._CP',             # 02
        'ED6_DT29/CH14730P._CP',             # 03
        'ED6_DT29/CH14790P._CP',             # 04
        'ED6_DT29/CH14791P._CP',             # 05
    )

    DeclMonster(
        X                   = -1730,
        Z                   = 0,
        Y                   = 10930,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xDF,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -12250,
        Z                   = 0,
        Y                   = 51840,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xDD,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -8330,
        Z                   = 0,
        Y                   = 72990,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xDE,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 21250,
        Z                   = 0,
        Y                   = 112440,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xDF,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -960,
        Z                   = 0,
        Y                   = 56400,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xDD,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 18550,
        Z                   = 0,
        Y                   = 26840,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xDE,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 10760,
        TriggerZ            = 0,
        TriggerY            = 120990,
        TriggerRange        = 1000,
        ActorX              = 10760,
        ActorZ              = 1000,
        ActorY              = 120990,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 45390,
        TriggerZ            = 0,
        TriggerY            = 49070,
        TriggerRange        = 1000,
        ActorX              = 45390,
        ActorZ              = 1000,
        ActorY              = 49070,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -18600,
        TriggerZ            = 0,
        TriggerY            = 107760,
        TriggerRange        = 1000,
        ActorX              = -18600,
        ActorZ              = 1000,
        ActorY              = 107760,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 28990,
        TriggerZ            = 0,
        TriggerY            = 30440,
        TriggerRange        = 1000,
        ActorX              = 28990,
        ActorZ              = 1000,
        ActorY              = 30440,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 28440,
        TriggerZ            = 0,
        TriggerY            = 22530,
        TriggerRange        = 1000,
        ActorX              = 28440,
        ActorZ              = 1000,
        ActorY              = 22530,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -34390,
        TriggerZ            = 0,
        TriggerY            = 75950,
        TriggerRange        = 1000,
        ActorX              = -34390,
        ActorZ              = 1000,
        ActorY              = 75950,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 27030,
        TriggerZ            = 0,
        TriggerY            = 76890,
        TriggerRange        = 1000,
        ActorX              = 27030,
        ActorZ              = 1000,
        ActorY              = 76890,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_27E",          # 00, 0
        "Function_1_27F",          # 01, 1
        "Function_2_35C",          # 02, 2
        "Function_3_47C",          # 03, 3
        "Function_4_59C",          # 04, 4
        "Function_5_6BC",          # 05, 5
        "Function_6_7DC",          # 06, 6
        "Function_7_8FC",          # 07, 7
        "Function_8_A1C",          # 08, 8
    )


    def Function_0_27E(): pass

    label("Function_0_27E")

    Return()

    # Function_0_27E end

    def Function_1_27F(): pass

    label("Function_1_27F")

    OP_16(0x2, 0xFA0, 0xFFFE2370, 0xFFFEE2D8, 0x23006E)
    OP_22(0x1C5, 0x1, 0x64)
    OP_51(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BE")
    OP_6F(0xD, 0)
    Jump("loc_2C5")

    label("loc_2BE")

    OP_6F(0xD, 60)

    label("loc_2C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D7")
    OP_6F(0xE, 0)
    Jump("loc_2DE")

    label("loc_2D7")

    OP_6F(0xE, 60)

    label("loc_2DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F0")
    OP_6F(0xF, 0)
    Jump("loc_2F7")

    label("loc_2F0")

    OP_6F(0xF, 60)

    label("loc_2F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F6, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_309")
    OP_6F(0x10, 0)
    Jump("loc_310")

    label("loc_309")

    OP_6F(0x10, 60)

    label("loc_310")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_322")
    OP_6F(0x11, 0)
    Jump("loc_329")

    label("loc_322")

    OP_6F(0x11, 60)

    label("loc_329")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33B")
    OP_6F(0x12, 0)
    Jump("loc_342")

    label("loc_33B")

    OP_6F(0x12, 60)

    label("loc_342")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_354")
    OP_6F(0x13, 0)
    Jump("loc_35B")

    label("loc_354")

    OP_6F(0x13, 60)

    label("loc_35B")

    Return()

    # Function_1_27F end

    def Function_2_35C(): pass

    label("Function_2_35C")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xD, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_3CE")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\xF6\x01\x07\x00。\x02",
    )

    Jump("loc_3B3")

    label("loc_3B3")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x27B0)
    Jump("loc_43A")

    label("loc_3CE")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\xF6\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xF6\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_41B")

    label("loc_41B")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xD, 60)
    OP_70(0xD, 0x0)

    label("loc_43A")

    Jump("loc_46E")

    label("loc_43D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_46E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_35C end

    def Function_3_47C(): pass

    label("Function_3_47C")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xE, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F8, 1)"), scpexpr(EXPR_END)), "loc_4EE")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\xF8\x01\x07\x00。\x02",
    )

    Jump("loc_4D3")

    label("loc_4D3")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x27B1)
    Jump("loc_55A")

    label("loc_4EE")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\xF8\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xF8\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_53B")

    label("loc_53B")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xE, 60)
    OP_70(0xE, 0x0)

    label("loc_55A")

    Jump("loc_58E")

    label("loc_55D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_58E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_47C end

    def Function_4_59C(): pass

    label("Function_4_59C")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xF, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F8, 1)"), scpexpr(EXPR_END)), "loc_60E")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x00得到了\x1F\xF8\x01\x07\x00。\x02",
    )

    Jump("loc_5F3")

    label("loc_5F3")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x27B2)
    Jump("loc_67A")

    label("loc_60E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "宝箱里装有\x1F\xF8\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xF8\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_65B")

    label("loc_65B")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xF, 60)
    OP_70(0xF, 0x0)

    label("loc_67A")

    Jump("loc_6AE")

    label("loc_67D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_6AE")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_59C end

    def Function_5_6BC(): pass

    label("Function_5_6BC")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F6, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_79D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x10, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x18A, 1)"), scpexpr(EXPR_END)), "loc_72E")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x00得到了\x1F\x8A\x01\x07\x00。\x02",
    )

    Jump("loc_713")

    label("loc_713")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x27B3)
    Jump("loc_79A")

    label("loc_72E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "宝箱里装有\x1F\x8A\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x8A\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_77B")

    label("loc_77B")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x10, 60)
    OP_70(0x10, 0x0)

    label("loc_79A")

    Jump("loc_7CE")

    label("loc_79D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_7CE")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_6BC end

    def Function_6_7DC(): pass

    label("Function_6_7DC")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8BD")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x11, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_84E")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #12
        "\x07\x00得到了\x1F\xF6\x01\x07\x00。\x02",
    )

    Jump("loc_833")

    label("loc_833")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x27B4)
    Jump("loc_8BA")

    label("loc_84E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        (
            "宝箱里装有\x1F\xF6\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xF6\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_89B")

    label("loc_89B")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x11, 60)
    OP_70(0x11, 0x0)

    label("loc_8BA")

    Jump("loc_8EE")

    label("loc_8BD")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_8EE")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_7DC end

    def Function_7_8FC(): pass

    label("Function_7_8FC")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9DD")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x12, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2D0, 1)"), scpexpr(EXPR_END)), "loc_96E")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #15
        "\x07\x00得到了\x1F\xD0\x02\x07\x00。\x02",
    )

    Jump("loc_953")

    label("loc_953")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x27B5)
    Jump("loc_9DA")

    label("loc_96E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #16
        (
            "宝箱里装有\x1F\xD0\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xD0\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_9BB")

    label("loc_9BB")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x12, 60)
    OP_70(0x12, 0x0)

    label("loc_9DA")

    Jump("loc_A0E")

    label("loc_9DD")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #17
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_A0E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_8FC end

    def Function_8_A1C(): pass

    label("Function_8_A1C")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AFD")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x13, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_A8E")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #18
        "\x07\x00得到了\x1F\xFE\x01\x07\x00。\x02",
    )

    Jump("loc_A73")

    label("loc_A73")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x27B6)
    Jump("loc_AFA")

    label("loc_A8E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #19
        (
            "宝箱里装有\x1F\xFE\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xFE\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_ADB")

    label("loc_ADB")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x13, 60)
    OP_70(0x13, 0x0)

    label("loc_AFA")

    Jump("loc_B2E")

    label("loc_AFD")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #20
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_B2E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_A1C end

    SaveToFile()

Try(main)
