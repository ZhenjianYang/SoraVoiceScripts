from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'U4255   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U4255.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60230",
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
        TriggerX            = -65370,
        TriggerZ            = 0,
        TriggerY            = 76630,
        TriggerRange        = 1000,
        ActorX              = -65370,
        ActorZ              = 1000,
        ActorY              = 76630,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -63850,
        TriggerZ            = 0,
        TriggerY            = 76630,
        TriggerRange        = 1000,
        ActorX              = -63850,
        ActorZ              = 1000,
        ActorY              = 76630,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_F2",           # 00, 0
        "Function_1_F3",           # 01, 1
        "Function_2_126",          # 02, 2
        "Function_3_222",          # 03, 3
    )


    def Function_0_F2(): pass

    label("Function_0_F2")

    Return()

    # Function_0_F2 end

    def Function_1_F3(): pass

    label("Function_1_F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_105")
    OP_6F(0x5, 0)
    Jump("loc_10C")

    label("loc_105")

    OP_6F(0x5, 60)

    label("loc_10C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11E")
    OP_6F(0x6, 0)
    Jump("loc_125")

    label("loc_11E")

    OP_6F(0x6, 60)

    label("loc_125")

    Return()

    # Function_1_F3 end

    def Function_2_126(): pass

    label("Function_2_126")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F6")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x1E)
    OP_73(0x5)
    OP_6F(0x5, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_3E(0x1E0, 1)

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\xE0\x01\x07\x00。\x02",
    )

    Jump("loc_17D")

    label("loc_17D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x14)"), scpexpr(EXPR_END)), "loc_197")
    Jump("loc_1E4")

    label("loc_197")

    CloseMessageWindow()

    AnonymousTalk(    #1
        "\x07\x00得到了\x1F\xE0\x01\x07\x00的食谱。\x02",
    )

    Jump("loc_1BE")

    label("loc_1BE")

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #2
        "\x1F\xE0\x01\x07\x00的制作方法已经记下了。\x02",
    )


    label("loc_1E4")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x27A1)
    Jump("loc_210")

    label("loc_1F6")


    AnonymousTalk(    #3
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_210")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_126 end

    def Function_3_222(): pass

    label("Function_3_222")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_303")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1BC, 1)"), scpexpr(EXPR_END)), "loc_294")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #4
        "\x07\x00得到了\x1F\xBC\x01\x07\x00。\x02",
    )

    Jump("loc_279")

    label("loc_279")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x27A2)
    Jump("loc_300")

    label("loc_294")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "宝箱里装有\x1F\xBC\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xBC\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_2E1")

    label("loc_2E1")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)

    label("loc_300")

    Jump("loc_334")

    label("loc_303")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_334")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_222 end

    SaveToFile()

Try(main)
