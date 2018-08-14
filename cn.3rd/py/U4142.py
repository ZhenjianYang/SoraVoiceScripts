from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'U4142   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U4142.x',
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
        TriggerX            = -59340,
        TriggerZ            = 0,
        TriggerY            = 121250,
        TriggerRange        = 1000,
        ActorX              = -59340,
        ActorZ              = 1000,
        ActorY              = 121250,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
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
        TalkFunctionIndex   = 4,
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
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_13A",          # 00, 0
        "Function_1_13B",          # 01, 1
        "Function_2_16E",          # 02, 2
        "Function_3_294",          # 03, 3
        "Function_4_3B6",          # 04, 4
        "Function_5_459",          # 05, 5
    )


    def Function_0_13A(): pass

    label("Function_0_13A")

    Return()

    # Function_0_13A end

    def Function_1_13B(): pass

    label("Function_1_13B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14D")
    OP_6F(0x9, 0)
    Jump("loc_154")

    label("loc_14D")

    OP_6F(0x9, 60)

    label("loc_154")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_166")
    OP_6F(0xA, 0)
    Jump("loc_16D")

    label("loc_166")

    OP_6F(0xA, 60)

    label("loc_16D")

    Return()

    # Function_1_13B end

    def Function_2_16E(): pass

    label("Function_2_16E")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_253")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x9, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1AC, 1)"), scpexpr(EXPR_END)), "loc_1E2")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\xAC\x01\x07\x00。\x02",
    )

    Jump("loc_1C7")

    label("loc_1C7")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2788)
    Jump("loc_250")

    label("loc_1E2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\xAC\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xAC\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_231")

    label("loc_231")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x9, 60)
    OP_70(0x9, 0x0)

    label("loc_250")

    Jump("loc_286")

    label("loc_253")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_286")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_16E end

    def Function_3_294(): pass

    label("Function_3_294")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_377")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xA, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x165, 1)"), scpexpr(EXPR_END)), "loc_308")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\x65\x01\x07\x00。\x02",
    )

    Jump("loc_2ED")

    label("loc_2ED")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2795)
    Jump("loc_374")

    label("loc_308")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\x65\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x65\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_355")

    label("loc_355")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xA, 60)
    OP_70(0xA, 0x0)

    label("loc_374")

    Jump("loc_3A8")

    label("loc_377")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_3A8")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_294 end

    def Function_4_3B6(): pass

    label("Function_4_3B6")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #6
        (
            "\x07\x05巴拉尔咖啡厅的名菜！\x01",
            "『完熟咖喱饭』　９００米拉\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #7
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

    # Function_4_3B6 end

    def Function_5_459(): pass

    label("Function_5_459")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #8
        (
            "\x07\x05～　菜单　～\x01",
            "　仿手工制派　　　４００米拉\x01",
            "　苦西红柿三明治　１４００米拉\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #9
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

    # Function_5_459 end

    SaveToFile()

Try(main)
