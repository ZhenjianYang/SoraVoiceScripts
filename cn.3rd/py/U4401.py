from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'U4401   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U4401.x',
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
        'ED6_DT29/CH14500 ._CH',             # 00
        'ED6_DT29/CH14501 ._CH',             # 01
        'ED6_DT29/CH14510 ._CH',             # 02
        'ED6_DT29/CH14511 ._CH',             # 03
        'ED6_DT29/CH14520 ._CH',             # 04
        'ED6_DT29/CH14521 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT29/CH14500P._CP',             # 00
        'ED6_DT29/CH14501P._CP',             # 01
        'ED6_DT29/CH14510P._CP',             # 02
        'ED6_DT29/CH14511P._CP',             # 03
        'ED6_DT29/CH14520P._CP',             # 04
        'ED6_DT29/CH14521P._CP',             # 05
    )

    DeclMonster(
        X                   = -1730,
        Z                   = 0,
        Y                   = 10930,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xD5,
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
        BattleIndex         = 0xD4,
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
        BattleIndex         = 0xD5,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 21250,
        Z                   = 0,
        Y                   = 112440,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xD4,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -960,
        Z                   = 0,
        Y                   = 56400,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xD5,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 18550,
        Z                   = 0,
        Y                   = 26840,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xD4,
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
        "Function_2_362",          # 02, 2
        "Function_3_482",          # 03, 3
        "Function_4_5A2",          # 04, 4
        "Function_5_6C2",          # 05, 5
        "Function_6_7E2",          # 06, 6
        "Function_7_902",          # 07, 7
        "Function_8_A22",          # 08, 8
    )


    def Function_0_27E(): pass

    label("Function_0_27E")

    Return()

    # Function_0_27E end

    def Function_1_27F(): pass

    label("Function_1_27F")

    OP_16(0x2, 0xFA0, 0xFFFE2370, 0xFFFEE2D8, 0x23006E)
    OP_22(0x1C5, 0x1, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E4, 1)), scpexpr(EXPR_END)), "loc_2A9")
    OP_B1("U4401_y")
    Jump("loc_2B2")

    label("loc_2A9")

    OP_B1("U4401_n")

    label("loc_2B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C4")
    OP_6F(0xC, 0)
    Jump("loc_2CB")

    label("loc_2C4")

    OP_6F(0xC, 60)

    label("loc_2CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DD")
    OP_6F(0xD, 0)
    Jump("loc_2E4")

    label("loc_2DD")

    OP_6F(0xD, 60)

    label("loc_2E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F6")
    OP_6F(0xE, 0)
    Jump("loc_2FD")

    label("loc_2F6")

    OP_6F(0xE, 60)

    label("loc_2FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F6, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30F")
    OP_6F(0xF, 0)
    Jump("loc_316")

    label("loc_30F")

    OP_6F(0xF, 60)

    label("loc_316")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_328")
    OP_6F(0x10, 0)
    Jump("loc_32F")

    label("loc_328")

    OP_6F(0x10, 60)

    label("loc_32F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_341")
    OP_6F(0x11, 0)
    Jump("loc_348")

    label("loc_341")

    OP_6F(0x11, 60)

    label("loc_348")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35A")
    OP_6F(0x12, 0)
    Jump("loc_361")

    label("loc_35A")

    OP_6F(0x12, 60)

    label("loc_361")

    Return()

    # Function_1_27F end

    def Function_2_362(): pass

    label("Function_2_362")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_443")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xC, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_3D4")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\xF6\x01\x07\x00。\x02",
    )

    Jump("loc_3B9")

    label("loc_3B9")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x27B0)
    Jump("loc_440")

    label("loc_3D4")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\xF6\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xF6\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_421")

    label("loc_421")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xC, 60)
    OP_70(0xC, 0x0)

    label("loc_440")

    Jump("loc_474")

    label("loc_443")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_474")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_362 end

    def Function_3_482(): pass

    label("Function_3_482")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_563")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xD, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F8, 1)"), scpexpr(EXPR_END)), "loc_4F4")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\xF8\x01\x07\x00。\x02",
    )

    Jump("loc_4D9")

    label("loc_4D9")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x27B1)
    Jump("loc_560")

    label("loc_4F4")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\xF8\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xF8\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_541")

    label("loc_541")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xD, 60)
    OP_70(0xD, 0x0)

    label("loc_560")

    Jump("loc_594")

    label("loc_563")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_594")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_482 end

    def Function_4_5A2(): pass

    label("Function_4_5A2")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_683")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xE, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F8, 1)"), scpexpr(EXPR_END)), "loc_614")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x00得到了\x1F\xF8\x01\x07\x00。\x02",
    )

    Jump("loc_5F9")

    label("loc_5F9")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x27B2)
    Jump("loc_680")

    label("loc_614")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "宝箱里装有\x1F\xF8\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xF8\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_661")

    label("loc_661")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xE, 60)
    OP_70(0xE, 0x0)

    label("loc_680")

    Jump("loc_6B4")

    label("loc_683")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
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

    # Function_4_5A2 end

    def Function_5_6C2(): pass

    label("Function_5_6C2")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F6, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A3")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xF, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x18A, 1)"), scpexpr(EXPR_END)), "loc_734")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x00得到了\x1F\x8A\x01\x07\x00。\x02",
    )

    Jump("loc_719")

    label("loc_719")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x27B3)
    Jump("loc_7A0")

    label("loc_734")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "宝箱里装有\x1F\x8A\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x8A\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_781")

    label("loc_781")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xF, 60)
    OP_70(0xF, 0x0)

    label("loc_7A0")

    Jump("loc_7D4")

    label("loc_7A3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_7D4")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_6C2 end

    def Function_6_7E2(): pass

    label("Function_6_7E2")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C3")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x10, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_854")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #12
        "\x07\x00得到了\x1F\xF6\x01\x07\x00。\x02",
    )

    Jump("loc_839")

    label("loc_839")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x27B4)
    Jump("loc_8C0")

    label("loc_854")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        (
            "宝箱里装有\x1F\xF6\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xF6\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_8A1")

    label("loc_8A1")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x10, 60)
    OP_70(0x10, 0x0)

    label("loc_8C0")

    Jump("loc_8F4")

    label("loc_8C3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_8F4")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_7E2 end

    def Function_7_902(): pass

    label("Function_7_902")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9E3")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x11, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2D0, 1)"), scpexpr(EXPR_END)), "loc_974")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #15
        "\x07\x00得到了\x1F\xD0\x02\x07\x00。\x02",
    )

    Jump("loc_959")

    label("loc_959")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x27B5)
    Jump("loc_9E0")

    label("loc_974")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #16
        (
            "宝箱里装有\x1F\xD0\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xD0\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_9C1")

    label("loc_9C1")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x11, 60)
    OP_70(0x11, 0x0)

    label("loc_9E0")

    Jump("loc_A14")

    label("loc_9E3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #17
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_A14")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_902 end

    def Function_8_A22(): pass

    label("Function_8_A22")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B03")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x12, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_A94")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #18
        "\x07\x00得到了\x1F\xFE\x01\x07\x00。\x02",
    )

    Jump("loc_A79")

    label("loc_A79")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x27B6)
    Jump("loc_B00")

    label("loc_A94")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #19
        (
            "宝箱里装有\x1F\xFE\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xFE\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_AE1")

    label("loc_AE1")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x12, 60)
    OP_70(0x12, 0x0)

    label("loc_B00")

    Jump("loc_B34")

    label("loc_B03")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #20
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_B34")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_A22 end

    SaveToFile()

Try(main)
