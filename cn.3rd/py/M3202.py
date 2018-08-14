from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M3202   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M3202.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60232",
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
        'ED6_DT07/CH00330 ._CH',             # 00
        'ED6_DT07/CH00331 ._CH',             # 01
        'ED6_DT07/CH00430 ._CH',             # 02
        'ED6_DT07/CH00431 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT07/CH00330P._CP',             # 00
        'ED6_DT07/CH00331P._CP',             # 01
        'ED6_DT07/CH00430P._CP',             # 02
        'ED6_DT07/CH00431P._CP',             # 03
    )

    DeclMonster(
        X                   = 42990,
        Z                   = 0,
        Y                   = -21130,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 67370,
        Z                   = 0,
        Y                   = 67070,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -16860,
        Z                   = 0,
        Y                   = 97670,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -77550,
        Z                   = 0,
        Y                   = 32030,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 43020,
        TriggerZ            = 0,
        TriggerY            = 5760,
        TriggerRange        = 1000,
        ActorX              = 43020,
        ActorZ              = 800,
        ActorY              = 5760,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -21920,
        TriggerZ            = 0,
        TriggerY            = -9940,
        TriggerRange        = 1000,
        ActorX              = -21420,
        ActorZ              = 1000,
        ActorY              = -9740,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 67960,
        TriggerZ            = 120,
        TriggerY            = -45240,
        TriggerRange        = 1000,
        ActorX              = 67960,
        ActorZ              = 1120,
        ActorY              = -45240,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 69830,
        TriggerZ            = 120,
        TriggerY            = -23440,
        TriggerRange        = 1000,
        ActorX              = 69830,
        ActorZ              = 1120,
        ActorY              = -23440,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 68450,
        TriggerZ            = 120,
        TriggerY            = 2920,
        TriggerRange        = 1000,
        ActorX              = 68450,
        ActorZ              = 1120,
        ActorY              = 2920,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -21530,
        TriggerZ            = 120,
        TriggerY            = -4990,
        TriggerRange        = 1000,
        ActorX              = -21530,
        ActorZ              = 1120,
        ActorY              = -4990,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 16990,
        TriggerZ            = 120,
        TriggerY            = 100470,
        TriggerRange        = 1000,
        ActorX              = 16990,
        ActorZ              = 1120,
        ActorY              = 100470,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 23000,
        TriggerZ            = 120,
        TriggerY            = 100360,
        TriggerRange        = 1000,
        ActorX              = 23000,
        ActorZ              = 1120,
        ActorY              = 100360,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_25A",          # 00, 0
        "Function_1_25B",          # 01, 1
        "Function_2_320",          # 02, 2
        "Function_3_446",          # 03, 3
        "Function_4_56C",          # 04, 4
        "Function_5_692",          # 05, 5
        "Function_6_7B8",          # 06, 6
        "Function_7_8DE",          # 07, 7
        "Function_8_A04",          # 08, 8
        "Function_9_B2A",          # 09, 9
    )


    def Function_0_25A(): pass

    label("Function_0_25A")

    Return()

    # Function_0_25A end

    def Function_1_25B(): pass

    label("Function_1_25B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x570, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26C")
    OP_72(0x1000, 0x0)
    ExitThread()
    Jump("loc_270")

    label("loc_26C")

    OP_64(0x0, 0x1)

    label("loc_270")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x571, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_282")
    OP_6F(0x24, 0)
    Jump("loc_289")

    label("loc_282")

    OP_6F(0x24, 60)

    label("loc_289")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x571, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29B")
    OP_6F(0x25, 0)
    Jump("loc_2A2")

    label("loc_29B")

    OP_6F(0x25, 60)

    label("loc_2A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x571, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B4")
    OP_6F(0x26, 0)
    Jump("loc_2BB")

    label("loc_2B4")

    OP_6F(0x26, 60)

    label("loc_2BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x571, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CD")
    OP_6F(0x27, 0)
    Jump("loc_2D4")

    label("loc_2CD")

    OP_6F(0x27, 60)

    label("loc_2D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x571, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E6")
    OP_6F(0x28, 0)
    Jump("loc_2ED")

    label("loc_2E6")

    OP_6F(0x28, 60)

    label("loc_2ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x571, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FF")
    OP_6F(0x29, 0)
    Jump("loc_306")

    label("loc_2FF")

    OP_6F(0x29, 60)

    label("loc_306")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x571, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_318")
    OP_6F(0x2A, 0)
    Jump("loc_31F")

    label("loc_318")

    OP_6F(0x2A, 60)

    label("loc_31F")

    Return()

    # Function_1_25B end

    def Function_2_320(): pass

    label("Function_2_320")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x571, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_405")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x24, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x14E, 1)"), scpexpr(EXPR_END)), "loc_394")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x4E\x01\x07\x00。\x02",
    )

    Jump("loc_379")

    label("loc_379")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2B88)
    Jump("loc_402")

    label("loc_394")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\x4E\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x4E\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_3E3")

    label("loc_3E3")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x24, 60)
    OP_70(0x24, 0x0)

    label("loc_402")

    Jump("loc_438")

    label("loc_405")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_438")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_320 end

    def Function_3_446(): pass

    label("Function_3_446")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x571, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52B")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x25, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1C4, 1)"), scpexpr(EXPR_END)), "loc_4BA")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\xC4\x01\x07\x00。\x02",
    )

    Jump("loc_49F")

    label("loc_49F")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2B89)
    Jump("loc_528")

    label("loc_4BA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\xC4\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xC4\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_509")

    label("loc_509")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x25, 60)
    OP_70(0x25, 0x0)

    label("loc_528")

    Jump("loc_55E")

    label("loc_52B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_55E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_446 end

    def Function_4_56C(): pass

    label("Function_4_56C")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x571, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_651")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x26, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_5E0")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x00得到了\x1F\xFB\x01\x07\x00。\x02",
    )

    Jump("loc_5C5")

    label("loc_5C5")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2B8A)
    Jump("loc_64E")

    label("loc_5E0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "宝箱里装有\x1F\xFB\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xFB\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_62F")

    label("loc_62F")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x26, 60)
    OP_70(0x26, 0x0)

    label("loc_64E")

    Jump("loc_684")

    label("loc_651")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_684")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_56C end

    def Function_5_692(): pass

    label("Function_5_692")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x571, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_777")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x27, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2E0, 1)"), scpexpr(EXPR_END)), "loc_706")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x00得到了\x1F\xE0\x02\x07\x00。\x02",
    )

    Jump("loc_6EB")

    label("loc_6EB")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2B8B)
    Jump("loc_774")

    label("loc_706")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "宝箱里装有\x1F\xE0\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xE0\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_755")

    label("loc_755")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x27, 60)
    OP_70(0x27, 0x0)

    label("loc_774")

    Jump("loc_7AA")

    label("loc_777")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_7AA")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_692 end

    def Function_6_7B8(): pass

    label("Function_6_7B8")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x571, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_89D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x28, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2A3, 1)"), scpexpr(EXPR_END)), "loc_82C")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #12
        "\x07\x00得到了\x1F\xA3\x02\x07\x00。\x02",
    )

    Jump("loc_811")

    label("loc_811")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2B8C)
    Jump("loc_89A")

    label("loc_82C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        (
            "宝箱里装有\x1F\xA3\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xA3\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_87B")

    label("loc_87B")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x28, 60)
    OP_70(0x28, 0x0)

    label("loc_89A")

    Jump("loc_8D0")

    label("loc_89D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_8D0")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_7B8 end

    def Function_7_8DE(): pass

    label("Function_7_8DE")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x571, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9C3")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x29, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x205, 1)"), scpexpr(EXPR_END)), "loc_952")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #15
        "\x07\x00得到了\x1F\x05\x02\x07\x00。\x02",
    )

    Jump("loc_937")

    label("loc_937")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2B8D)
    Jump("loc_9C0")

    label("loc_952")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #16
        (
            "宝箱里装有\x1F\x05\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x05\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_9A1")

    label("loc_9A1")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x29, 60)
    OP_70(0x29, 0x0)

    label("loc_9C0")

    Jump("loc_9F6")

    label("loc_9C3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #17
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_9F6")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_8DE end

    def Function_8_A04(): pass

    label("Function_8_A04")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x571, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AE9")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2A, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x202, 1)"), scpexpr(EXPR_END)), "loc_A78")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #18
        "\x07\x00得到了\x1F\x02\x02\x07\x00。\x02",
    )

    Jump("loc_A5D")

    label("loc_A5D")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2B8E)
    Jump("loc_AE6")

    label("loc_A78")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #19
        (
            "宝箱里装有\x1F\x02\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x02\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_AC7")

    label("loc_AC7")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2A, 60)
    OP_70(0x2A, 0x0)

    label("loc_AE6")

    Jump("loc_B1C")

    label("loc_AE9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #20
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_B1C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_A04 end

    def Function_9_B2A(): pass

    label("Function_9_B2A")

    TalkBegin(0xFF)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #21
        "\x07\x05门上了锁。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x570, 4)), scpexpr(EXPR_END)), "loc_C32")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BA1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C32")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "使用Ｃ－０１钥匙\x01",      # 0
            "不使用\x01",                # 1
        )
    )

    Jump("loc_BD8")

    label("loc_BD8")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_BFE"),
        (SWITCH_DEFAULT, "loc_C22"),
    )


    label("loc_BFE")

    OP_22(0x73, 0x0, 0x64)
    Sleep(500)
    OP_A2(0x2B81)
    OP_71(0x1000, 0x0)
    ExitThread()
    OP_64(0x0, 0x1)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C2F")

    label("loc_C22")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C2F")

    label("loc_C2F")

    Jump("loc_BA1")

    label("loc_C32")

    TalkEnd(0xFF)
    Return()

    # Function_9_B2A end

    SaveToFile()

Try(main)
