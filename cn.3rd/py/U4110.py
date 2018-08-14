from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'U4110   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U4110.x',
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


    DeclActor(
        TriggerX            = 31070,
        TriggerZ            = 4000,
        TriggerY            = 5840,
        TriggerRange        = 1000,
        ActorX              = 31770,
        ActorZ              = 5000,
        ActorY              = 5980,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -29710,
        TriggerZ            = 4000,
        TriggerY            = 760,
        TriggerRange        = 1000,
        ActorX              = -29000,
        ActorZ              = 5000,
        ActorY              = 1000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 90730,
        TriggerZ            = 4000,
        TriggerY            = 2830,
        TriggerRange        = 1000,
        ActorX              = 91440,
        ActorZ              = 5000,
        ActorY              = 2930,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 51770,
        TriggerZ            = 0,
        TriggerY            = 57180,
        TriggerRange        = 1000,
        ActorX              = 51070,
        ActorZ              = 1000,
        ActorY              = 57200,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_13A",          # 00, 0
        "Function_1_13B",          # 01, 1
        "Function_2_1BC",          # 02, 2
        "Function_3_2DC",          # 03, 3
        "Function_4_3FC",          # 04, 4
        "Function_5_51C",          # 05, 5
    )


    def Function_0_13A(): pass

    label("Function_0_13A")

    Return()

    # Function_0_13A end

    def Function_1_13B(): pass

    label("Function_1_13B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E4, 1)), scpexpr(EXPR_END)), "loc_14E")
    OP_B1("U4110_y")
    Jump("loc_157")

    label("loc_14E")

    OP_B1("U4110_n")

    label("loc_157")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_169")
    OP_6F(0x0, 0)
    Jump("loc_170")

    label("loc_169")

    OP_6F(0x0, 60)

    label("loc_170")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_182")
    OP_6F(0x1, 0)
    Jump("loc_189")

    label("loc_182")

    OP_6F(0x1, 60)

    label("loc_189")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19B")
    OP_6F(0x2, 0)
    Jump("loc_1A2")

    label("loc_19B")

    OP_6F(0x2, 60)

    label("loc_1A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B4")
    OP_6F(0x3, 0)
    Jump("loc_1BB")

    label("loc_1B4")

    OP_6F(0x3, 60)

    label("loc_1BB")

    Return()

    # Function_1_13B end

    def Function_2_1BC(): pass

    label("Function_2_1BC")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FA, 1)"), scpexpr(EXPR_END)), "loc_22E")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\xFA\x01\x07\x00。\x02",
    )

    Jump("loc_213")

    label("loc_213")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2780)
    Jump("loc_29A")

    label("loc_22E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\xFA\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xFA\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_27B")

    label("loc_27B")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_29A")

    Jump("loc_2CE")

    label("loc_29D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_2CE")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_1BC end

    def Function_3_2DC(): pass

    label("Function_3_2DC")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BD")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x200, 1)"), scpexpr(EXPR_END)), "loc_34E")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\x00\x02\x07\x00。\x02",
    )

    Jump("loc_333")

    label("loc_333")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2781)
    Jump("loc_3BA")

    label("loc_34E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\x00\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x00\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_39B")

    label("loc_39B")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_3BA")

    Jump("loc_3EE")

    label("loc_3BD")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_3EE")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_2DC end

    def Function_4_3FC(): pass

    label("Function_4_3FC")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DD")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x206, 1)"), scpexpr(EXPR_END)), "loc_46E")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x00得到了\x1F\x06\x02\x07\x00。\x02",
    )

    Jump("loc_453")

    label("loc_453")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2782)
    Jump("loc_4DA")

    label("loc_46E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "宝箱里装有\x1F\x06\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x06\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_4BB")

    label("loc_4BB")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_4DA")

    Jump("loc_50E")

    label("loc_4DD")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_50E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_3FC end

    def Function_5_51C(): pass

    label("Function_5_51C")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5FD")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_58E")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x00得到了\x1F\xF6\x01\x07\x00。\x02",
    )

    Jump("loc_573")

    label("loc_573")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2783)
    Jump("loc_5FA")

    label("loc_58E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "宝箱里装有\x1F\xF6\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xF6\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_5DB")

    label("loc_5DB")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_5FA")

    Jump("loc_62E")

    label("loc_5FD")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_62E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_51C end

    SaveToFile()

Try(main)
