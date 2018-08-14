from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'U4122   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U4122.x',
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
        TriggerX            = 12730,
        TriggerZ            = 0,
        TriggerY            = -7330,
        TriggerRange        = 1000,
        ActorX              = 12730,
        ActorZ              = 1000,
        ActorY              = -7330,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 13510,
        TriggerZ            = 0,
        TriggerY            = 11190,
        TriggerRange        = 1000,
        ActorX              = 13510,
        ActorZ              = 1000,
        ActorY              = 11190,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -14510,
        TriggerZ            = 0,
        TriggerY            = 3850,
        TriggerRange        = 1000,
        ActorX              = -14510,
        ActorZ              = 1000,
        ActorY              = 3850,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_116",          # 00, 0
        "Function_1_117",          # 01, 1
        "Function_2_17F",          # 02, 2
        "Function_3_2A5",          # 03, 3
        "Function_4_3C5",          # 04, 4
    )


    def Function_0_116(): pass

    label("Function_0_116")

    Return()

    # Function_0_116 end

    def Function_1_117(): pass

    label("Function_1_117")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E4, 1)), scpexpr(EXPR_END)), "loc_12A")
    OP_B1("U4122_y")
    Jump("loc_133")

    label("loc_12A")

    OP_B1("U4122_n")

    label("loc_133")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_145")
    OP_6F(0x2, 0)
    Jump("loc_14C")

    label("loc_145")

    OP_6F(0x2, 60)

    label("loc_14C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F8, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15E")
    OP_6F(0x3, 0)
    Jump("loc_165")

    label("loc_15E")

    OP_6F(0x3, 60)

    label("loc_165")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_177")
    OP_6F(0x4, 0)
    Jump("loc_17E")

    label("loc_177")

    OP_6F(0x4, 60)

    label("loc_17E")

    Return()

    # Function_1_117 end

    def Function_2_17F(): pass

    label("Function_2_17F")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_264")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x145, 1)"), scpexpr(EXPR_END)), "loc_1F3")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x45\x01\x07\x00。\x02",
    )

    Jump("loc_1D8")

    label("loc_1D8")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x27C0)
    Jump("loc_261")

    label("loc_1F3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\x45\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x45\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_242")

    label("loc_242")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_261")

    Jump("loc_297")

    label("loc_264")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_297")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_17F end

    def Function_3_2A5(): pass

    label("Function_3_2A5")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F8, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_386")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F9, 1)"), scpexpr(EXPR_END)), "loc_317")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\xF9\x01\x07\x00。\x02",
    )

    Jump("loc_2FC")

    label("loc_2FC")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x27C1)
    Jump("loc_383")

    label("loc_317")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\xF9\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xF9\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_364")

    label("loc_364")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_383")

    Jump("loc_3B7")

    label("loc_386")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_3B7")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_2A5 end

    def Function_4_3C5(): pass

    label("Function_4_3C5")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48F")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x1E)
    OP_73(0x4)
    OP_6F(0x4, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_3E(0x1E3, 1)

    AnonymousTalk(    #6
        "\x07\x00得到了\x1F\xE3\x01\x07\x00。\x02",
    )

    Jump("loc_41A")

    label("loc_41A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_47D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x30)"), scpexpr(EXPR_END)), "loc_434")
    Jump("loc_47D")

    label("loc_434")

    CloseMessageWindow()

    AnonymousTalk(    #7
        "\x07\x00得到了\x1F\xE3\x01\x07\x00的食谱。\x02",
    )

    Jump("loc_459")

    label("loc_459")

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #8
        "\x1F\xE3\x01\x07\x00的制作方法已经记下了。\x02",
    )


    label("loc_47D")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x27C2)
    Jump("loc_4A9")

    label("loc_48F")


    AnonymousTalk(    #9
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_4A9")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_3C5 end

    SaveToFile()

Try(main)
