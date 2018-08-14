from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M5614   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M5614.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60233",
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


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_AF",           # 01, 1
        "Function_2_B0",           # 02, 2
        "Function_3_1C5",          # 03, 3
        "Function_4_1EB",          # 04, 4
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Event(0, 2)
    Return()

    # Function_0_AA end

    def Function_1_AF(): pass

    label("Function_1_AF")

    Return()

    # Function_1_AF end

    def Function_2_B0(): pass

    label("Function_2_B0")

    EventBegin(0x0)
    OP_6D(-1250, -50, 4440, 0)
    OP_67(0, 6720, -10000, 0)
    OP_6B(2870, 0)
    OP_6C(314000, 0)
    OP_6E(274, 0)
    SetChrPos(0x0, -680, 0, 2390, 270)
    SetChrPos(0x1, -480, 0, 3650, 270)
    SetChrPos(0x2, 1020, 0, 2150, 270)
    SetChrPos(0x3, 1090, 0, 3570, 270)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56C, 4)), scpexpr(EXPR_END)), "loc_154")
    Call(0, 3)
    NewScene("ED6_DT21/M5611   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1C4")

    label("loc_154")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56C, 5)), scpexpr(EXPR_END)), "loc_16B")
    Call(0, 4)
    NewScene("ED6_DT21/M5610   ._SN", 132, 0, 0)
    IdleLoop()
    Jump("loc_1C4")

    label("loc_16B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56C, 6)), scpexpr(EXPR_END)), "loc_182")
    Call(0, 3)
    NewScene("ED6_DT21/M5612   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1C4")

    label("loc_182")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56C, 7)), scpexpr(EXPR_END)), "loc_199")
    Call(0, 4)
    NewScene("ED6_DT21/M5611   ._SN", 101, 0, 0)
    IdleLoop()
    Jump("loc_1C4")

    label("loc_199")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56D, 0)), scpexpr(EXPR_END)), "loc_1B0")
    Call(0, 3)
    NewScene("ED6_DT21/M5613   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1C4")

    label("loc_1B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56D, 1)), scpexpr(EXPR_END)), "loc_1C4")
    Call(0, 4)
    NewScene("ED6_DT21/M5612   ._SN", 101, 0, 0)
    IdleLoop()

    label("loc_1C4")

    Return()

    # Function_2_B0 end

    def Function_3_1C5(): pass

    label("Function_3_1C5")

    FadeToDark(2000, 0, -1)
    OP_22(0x67, 0x0, 0x64)
    OP_6D(-1250, -12050, 4440, 2000)
    Sleep(2000)
    Return()

    # Function_3_1C5 end

    def Function_4_1EB(): pass

    label("Function_4_1EB")

    FadeToDark(2000, 0, -1)
    OP_22(0x67, 0x0, 0x64)
    OP_6D(-1250, 12050, 4440, 2000)
    Sleep(2000)
    Return()

    # Function_4_1EB end

    SaveToFile()

Try(main)
