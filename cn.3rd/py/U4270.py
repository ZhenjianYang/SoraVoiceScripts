from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'U4270   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U4270.x',
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
        TriggerX            = -55290,
        TriggerZ            = 0,
        TriggerY            = 14190,
        TriggerRange        = 1000,
        ActorX              = -55290,
        ActorZ              = 1000,
        ActorY              = 14190,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_CE",           # 00, 0
        "Function_1_CF",           # 01, 1
        "Function_2_E9",           # 02, 2
    )


    def Function_0_CE(): pass

    label("Function_0_CE")

    Return()

    # Function_0_CE end

    def Function_1_CF(): pass

    label("Function_1_CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E1")
    OP_6F(0x2B, 0)
    Jump("loc_E8")

    label("loc_E1")

    OP_6F(0x2B, 60)

    label("loc_E8")

    Return()

    # Function_1_CF end

    def Function_2_E9(): pass

    label("Function_2_E9")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CA")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2B, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2D2, 1)"), scpexpr(EXPR_END)), "loc_15B")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\xD2\x02\x07\x00。\x02",
    )

    Jump("loc_140")

    label("loc_140")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x27A8)
    Jump("loc_1C7")

    label("loc_15B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\xD2\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xD2\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_1A8")

    label("loc_1A8")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2B, 60)
    OP_70(0x2B, 0x0)

    label("loc_1C7")

    Jump("loc_1FB")

    label("loc_1CA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1FB")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_E9 end

    SaveToFile()

Try(main)
