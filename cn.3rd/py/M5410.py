from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M5410   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M5410.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60234",
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
        TriggerX            = -81710,
        TriggerZ            = 0,
        TriggerY            = -17950,
        TriggerRange        = 1000,
        ActorX              = -81000,
        ActorZ              = 0,
        ActorY              = -18020,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_CE",           # 00, 0
        "Function_1_CF",           # 01, 1
        "Function_2_14A",          # 02, 2
    )


    def Function_0_CE(): pass

    label("Function_0_CE")

    Return()

    # Function_0_CE end

    def Function_1_CF(): pass

    label("Function_1_CF")

    OP_6F(0x1, 100)
    OP_72(0x201, 0x0)
    ExitThread()
    OP_BE(0x1, 0x1, 0x2, 0x3E8, 0x0, 0x2, -127750, -1000, -57600, -122480, 2000, -60300)
    OP_72(0x2000, 0x0)
    ExitThread()
    OP_72(0x800, 0x0)
    ExitThread()
    OP_6F(0x0, 0)
    OP_71(0x200, 0x0)
    ExitThread()
    OP_72(0x2002, 0x0)
    ExitThread()
    OP_72(0x802, 0x0)
    ExitThread()
    OP_6F(0x2, 0)
    OP_71(0x202, 0x0)
    ExitThread()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_142")
    OP_6F(0x13, 0)
    Jump("loc_149")

    label("loc_142")

    OP_6F(0x13, 60)

    label("loc_149")

    Return()

    # Function_1_CF end

    def Function_2_14A(): pass

    label("Function_2_14A")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22B")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x13, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x17C, 1)"), scpexpr(EXPR_END)), "loc_1BC")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x7C\x01\x07\x00。\x02",
    )

    Jump("loc_1A1")

    label("loc_1A1")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BFA)
    Jump("loc_228")

    label("loc_1BC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\x7C\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x7C\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_209")

    label("loc_209")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x13, 60)
    OP_70(0x13, 0x0)

    label("loc_228")

    Jump("loc_25C")

    label("loc_22B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_25C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_14A end

    SaveToFile()

Try(main)
