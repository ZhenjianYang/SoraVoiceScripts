from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'U4130   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U4130.x',
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
        TriggerX            = 5830,
        TriggerZ            = 4000,
        TriggerY            = 5250,
        TriggerRange        = 1000,
        ActorX              = 6530,
        ActorZ              = 5000,
        ActorY              = 5220,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 59930,
        TriggerZ            = 0,
        TriggerY            = -550,
        TriggerRange        = 1000,
        ActorX              = 60000,
        ActorZ              = 1000,
        ActorY              = 150,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 61900,
        TriggerZ            = 0,
        TriggerY            = -550,
        TriggerRange        = 1000,
        ActorX              = 62000,
        ActorZ              = 1000,
        ActorY              = 150,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -59340,
        TriggerZ            = 0,
        TriggerY            = 121250,
        TriggerRange        = 1000,
        ActorX              = -59340,
        ActorZ              = 1000,
        ActorY              = 121250,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 57530,
        TriggerZ            = 0,
        TriggerY            = 400,
        TriggerRange        = 800,
        ActorX              = 57290,
        ActorZ              = 900,
        ActorY              = 340,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 2480,
        TriggerZ            = -250,
        TriggerY            = -3810,
        TriggerRange        = 800,
        ActorX              = 2480,
        ActorZ              = 1100,
        ActorY              = -3810,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_182",          # 00, 0
        "Function_1_183",          # 01, 1
        "Function_2_204",          # 02, 2
        "Function_3_32A",          # 03, 3
        "Function_4_44C",          # 04, 4
        "Function_5_56C",          # 05, 5
        "Function_6_68C",          # 06, 6
        "Function_7_72F",          # 07, 7
    )


    def Function_0_182(): pass

    label("Function_0_182")

    Return()

    # Function_0_182 end

    def Function_1_183(): pass

    label("Function_1_183")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E4, 1)), scpexpr(EXPR_END)), "loc_196")
    OP_B1("U4130_y")
    Jump("loc_19F")

    label("loc_196")

    OP_B1("U4130_n")

    label("loc_19F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B1")
    OP_6F(0x6, 0)
    Jump("loc_1B8")

    label("loc_1B1")

    OP_6F(0x6, 60)

    label("loc_1B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CA")
    OP_6F(0x7, 0)
    Jump("loc_1D1")

    label("loc_1CA")

    OP_6F(0x7, 60)

    label("loc_1D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E3")
    OP_6F(0x8, 0)
    Jump("loc_1EA")

    label("loc_1E3")

    OP_6F(0x8, 60)

    label("loc_1EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FC")
    OP_6F(0x9, 0)
    Jump("loc_203")

    label("loc_1FC")

    OP_6F(0x9, 60)

    label("loc_203")

    Return()

    # Function_1_183 end

    def Function_2_204(): pass

    label("Function_2_204")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E9")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1AC, 1)"), scpexpr(EXPR_END)), "loc_278")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\xAC\x01\x07\x00。\x02",
    )

    Jump("loc_25D")

    label("loc_25D")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2788)
    Jump("loc_2E6")

    label("loc_278")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\xAC\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xAC\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_2C7")

    label("loc_2C7")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)

    label("loc_2E6")

    Jump("loc_31C")

    label("loc_2E9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_31C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_204 end

    def Function_3_32A(): pass

    label("Function_3_32A")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x7, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x19C, 1)"), scpexpr(EXPR_END)), "loc_39E")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\x9C\x01\x07\x00。\x02",
    )

    Jump("loc_383")

    label("loc_383")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2789)
    Jump("loc_40A")

    label("loc_39E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\x9C\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x9C\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_3EB")

    label("loc_3EB")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x7, 60)
    OP_70(0x7, 0x0)

    label("loc_40A")

    Jump("loc_43E")

    label("loc_40D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_43E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_32A end

    def Function_4_44C(): pass

    label("Function_4_44C")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x8, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x199, 1)"), scpexpr(EXPR_END)), "loc_4BE")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x00得到了\x1F\x99\x01\x07\x00。\x02",
    )

    Jump("loc_4A3")

    label("loc_4A3")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x278A)
    Jump("loc_52A")

    label("loc_4BE")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "宝箱里装有\x1F\x99\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x99\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_50B")

    label("loc_50B")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x8, 60)
    OP_70(0x8, 0x0)

    label("loc_52A")

    Jump("loc_55E")

    label("loc_52D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
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

    # Function_4_44C end

    def Function_5_56C(): pass

    label("Function_5_56C")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x9, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x165, 1)"), scpexpr(EXPR_END)), "loc_5DE")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x00得到了\x1F\x65\x01\x07\x00。\x02",
    )

    Jump("loc_5C3")

    label("loc_5C3")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2795)
    Jump("loc_64A")

    label("loc_5DE")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "宝箱里装有\x1F\x65\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x65\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_62B")

    label("loc_62B")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x9, 60)
    OP_70(0x9, 0x0)

    label("loc_64A")

    Jump("loc_67E")

    label("loc_64D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_67E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_56C end

    def Function_6_68C(): pass

    label("Function_6_68C")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #12
        (
            "\x07\x05巴拉尔咖啡厅的名菜！\x01",
            "『完熟咖喱饭』　９００米拉\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #13
        (
            "\x07\x05使用秘传的香辛料精心烹制的辣味咖喱，\x01",
            "请您走过路过不要错过。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_6_68C end

    def Function_7_72F(): pass

    label("Function_7_72F")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #14
        (
            "\x07\x05～　菜单　～\x01",
            "　仿手工制派　　　４００米拉\x01",
            "　苦西红柿三明治　１４００米拉\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #15
        (
            "\x07\x05～　本店推荐　～\x01",
            "　热海汁　　　　　１２００米拉\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_7_72F end

    SaveToFile()

Try(main)
