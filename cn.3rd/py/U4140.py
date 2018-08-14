from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'U4140   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U4140.x',
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
        TriggerX            = 117490,
        TriggerZ            = 0,
        TriggerY            = 3960,
        TriggerRange        = 1000,
        ActorX              = 116610,
        ActorZ              = 1000,
        ActorY              = 4230,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -70,
        TriggerZ            = 0,
        TriggerY            = 129500,
        TriggerRange        = 1000,
        ActorX              = -780,
        ActorZ              = 1000,
        ActorY              = 129490,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_F2",           # 00, 0
        "Function_1_F3",           # 01, 1
        "Function_2_126",          # 02, 2
        "Function_3_246",          # 03, 3
    )


    def Function_0_F2(): pass

    label("Function_0_F2")

    Return()

    # Function_0_F2 end

    def Function_1_F3(): pass

    label("Function_1_F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_105")
    OP_6F(0xA, 0)
    Jump("loc_10C")

    label("loc_105")

    OP_6F(0xA, 60)

    label("loc_10C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11E")
    OP_6F(0xB, 0)
    Jump("loc_125")

    label("loc_11E")

    OP_6F(0xB, 60)

    label("loc_125")

    Return()

    # Function_1_F3 end

    def Function_2_126(): pass

    label("Function_2_126")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_207")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xA, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x259, 1)"), scpexpr(EXPR_END)), "loc_198")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x59\x02\x07\x00。\x02",
    )

    Jump("loc_17D")

    label("loc_17D")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2787)
    Jump("loc_204")

    label("loc_198")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\x59\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x59\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_1E5")

    label("loc_1E5")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xA, 60)
    OP_70(0xA, 0x0)

    label("loc_204")

    Jump("loc_238")

    label("loc_207")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_238")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_126 end

    def Function_3_246(): pass

    label("Function_3_246")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_327")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xB, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x4A0, 1)"), scpexpr(EXPR_END)), "loc_2B8")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\xA0\x04\x07\x00。\x02",
    )

    Jump("loc_29D")

    label("loc_29D")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2784)
    Jump("loc_324")

    label("loc_2B8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\xA0\x04\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xA0\x04\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_305")

    label("loc_305")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xB, 60)
    OP_70(0xB, 0x0)

    label("loc_324")

    Jump("loc_358")

    label("loc_327")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_358")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_246 end

    SaveToFile()

Try(main)
