from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M5512   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M5512.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60231",
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
        'ED6_DT29/CH14740 ._CH',             # 00
        'ED6_DT29/CH14741 ._CH',             # 01
        'ED6_DT29/CH14540 ._CH',             # 02
        'ED6_DT29/CH14541 ._CH',             # 03
        'ED6_DT29/CH15110 ._CH',             # 04
        'ED6_DT29/CH15111 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT29/CH14740P._CP',             # 00
        'ED6_DT29/CH14741P._CP',             # 01
        'ED6_DT29/CH14540P._CP',             # 02
        'ED6_DT29/CH14541P._CP',             # 03
        'ED6_DT29/CH15110P._CP',             # 04
        'ED6_DT29/CH15111P._CP',             # 05
    )

    DeclMonster(
        X                   = -48930,
        Z                   = 550,
        Y                   = 3110,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x196,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -29090,
        Z                   = 0,
        Y                   = 17490,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x199,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -17600,
        Z                   = -4000,
        Y                   = 24160,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x199,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -20720,
        Z                   = -4000,
        Y                   = -11360,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x199,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -7680,
        Z                   = 0,
        Y                   = 25650,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x198,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -57550,
        TriggerZ            = 0,
        TriggerY            = -8700,
        TriggerRange        = 1000,
        ActorX              = -57550,
        ActorZ              = 1000,
        ActorY              = -8700,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -19420,
        TriggerZ            = -4000,
        TriggerY            = 38680,
        TriggerRange        = 1000,
        ActorX              = -19420,
        ActorZ              = -3000,
        ActorY              = 38680,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -23100,
        TriggerZ            = -4000,
        TriggerY            = -27760,
        TriggerRange        = 1000,
        ActorX              = -23100,
        ActorZ              = -3000,
        ActorY              = -27760,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -3430,
        TriggerZ            = 0,
        TriggerY            = 33040,
        TriggerRange        = 1000,
        ActorX              = -3430,
        ActorZ              = 1000,
        ActorY              = 33040,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -51110,
        TriggerZ            = 0,
        TriggerY            = 21930,
        TriggerRange        = 800,
        ActorX              = -51640,
        ActorZ              = 1000,
        ActorY              = 22460,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_21A",          # 00, 0
        "Function_1_21B",          # 01, 1
        "Function_2_297",          # 02, 2
        "Function_3_3BD",          # 03, 3
        "Function_4_4E3",          # 04, 4
        "Function_5_609",          # 05, 5
        "Function_6_72F",          # 06, 6
    )


    def Function_0_21A(): pass

    label("Function_0_21A")

    Return()

    # Function_0_21A end

    def Function_1_21B(): pass

    label("Function_1_21B")

    OP_16(0x2, 0xFA0, 0xFFFDA670, 0xFFFDFC60, 0x2300A5)
    OP_22(0x1CD, 0x0, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x534, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_244")
    OP_6F(0x0, 0)
    Jump("loc_24B")

    label("loc_244")

    OP_6F(0x0, 60)

    label("loc_24B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x534, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25D")
    OP_6F(0x1, 0)
    Jump("loc_264")

    label("loc_25D")

    OP_6F(0x1, 60)

    label("loc_264")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x534, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_276")
    OP_6F(0x2, 0)
    Jump("loc_27D")

    label("loc_276")

    OP_6F(0x2, 60)

    label("loc_27D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x534, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28F")
    OP_6F(0x3, 0)
    Jump("loc_296")

    label("loc_28F")

    OP_6F(0x3, 60)

    label("loc_296")

    Return()

    # Function_1_21B end

    def Function_2_297(): pass

    label("Function_2_297")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x534, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37C")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x16C, 1)"), scpexpr(EXPR_END)), "loc_30B")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x6C\x01\x07\x00。\x02",
    )

    Jump("loc_2F0")

    label("loc_2F0")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x29A0)
    Jump("loc_379")

    label("loc_30B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\x6C\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x6C\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_35A")

    label("loc_35A")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_379")

    Jump("loc_3AF")

    label("loc_37C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_3AF")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_297 end

    def Function_3_3BD(): pass

    label("Function_3_3BD")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x534, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A2")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_431")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\xFD\x01\x07\x00。\x02",
    )

    Jump("loc_416")

    label("loc_416")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x29A1)
    Jump("loc_49F")

    label("loc_431")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\xFD\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xFD\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_480")

    label("loc_480")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_49F")

    Jump("loc_4D5")

    label("loc_4A2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_4D5")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_3BD end

    def Function_4_4E3(): pass

    label("Function_4_4E3")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x534, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C8")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1BE, 1)"), scpexpr(EXPR_END)), "loc_557")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x00得到了\x1F\xBE\x01\x07\x00。\x02",
    )

    Jump("loc_53C")

    label("loc_53C")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x29A2)
    Jump("loc_5C5")

    label("loc_557")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "宝箱里装有\x1F\xBE\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xBE\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_5A6")

    label("loc_5A6")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_5C5")

    Jump("loc_5FB")

    label("loc_5C8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_5FB")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_4E3 end

    def Function_5_609(): pass

    label("Function_5_609")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x534, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6EE")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x294, 1)"), scpexpr(EXPR_END)), "loc_67D")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x00得到了\x1F\x94\x02\x07\x00。\x02",
    )

    Jump("loc_662")

    label("loc_662")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x29A3)
    Jump("loc_6EB")

    label("loc_67D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "宝箱里装有\x1F\x94\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x94\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_6CC")

    label("loc_6CC")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_6EB")

    Jump("loc_721")

    label("loc_6EE")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_721")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_609 end

    def Function_6_72F(): pass

    label("Function_6_72F")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #12
        "\x07\x05【圣科洛瓦森林】\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #13
        (
            "\x07\x05除了游击队员训练以外，\x01",
            "这里也适合进行生存训练。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_6_72F end

    SaveToFile()

Try(main)
