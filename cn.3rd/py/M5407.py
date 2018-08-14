from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M5407   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M5407.x',
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


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_AF",           # 01, 1
        "Function_2_B0",           # 02, 2
        "Function_3_210",          # 03, 3
        "Function_4_236",          # 04, 4
        "Function_5_266",          # 05, 5
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
    OP_6D(990, 0, 1420, 0)
    OP_67(0, 8620, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 1590, 0, -160, 90)
    SetChrPos(0x1, 830, 0, 1050, 90)
    SetChrPos(0x2, -790, 0, 1400, 90)
    SetChrPos(0x3, -580, 0, -150, 90)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56D, 2)), scpexpr(EXPR_END)), "loc_154")
    Call(0, 5)
    NewScene("ED6_DT21/M5400   ._SN", 127, 0, 0)
    IdleLoop()
    Jump("loc_20F")

    label("loc_154")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56D, 3)), scpexpr(EXPR_END)), "loc_16B")
    Call(0, 3)
    NewScene("ED6_DT21/M5402   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_20F")

    label("loc_16B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56D, 4)), scpexpr(EXPR_END)), "loc_19F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 1)), scpexpr(EXPR_END)), "loc_180")
    Call(0, 3)
    Jump("loc_193")

    label("loc_180")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18F")
    Call(0, 3)
    Jump("loc_193")

    label("loc_18F")

    Call(0, 4)

    label("loc_193")

    NewScene("ED6_DT21/M5400   ._SN", 125, 0, 0)
    IdleLoop()
    Jump("loc_20F")

    label("loc_19F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56D, 5)), scpexpr(EXPR_END)), "loc_1B6")
    Call(0, 5)
    NewScene("ED6_DT21/M5400   ._SN", 124, 0, 0)
    IdleLoop()
    Jump("loc_20F")

    label("loc_1B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56D, 6)), scpexpr(EXPR_END)), "loc_1CD")
    Call(0, 5)
    NewScene("ED6_DT21/M5404   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_20F")

    label("loc_1CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56D, 7)), scpexpr(EXPR_END)), "loc_1E4")
    Call(0, 3)
    NewScene("ED6_DT21/M5403   ._SN", 147, 0, 0)
    IdleLoop()
    Jump("loc_20F")

    label("loc_1E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56E, 0)), scpexpr(EXPR_END)), "loc_1FB")
    Call(0, 5)
    NewScene("ED6_DT21/M5411   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_20F")

    label("loc_1FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56E, 1)), scpexpr(EXPR_END)), "loc_20F")
    Call(0, 3)
    NewScene("ED6_DT21/M5404   ._SN", 153, 0, 0)
    IdleLoop()

    label("loc_20F")

    Return()

    # Function_2_B0 end

    def Function_3_210(): pass

    label("Function_3_210")

    FadeToDark(2000, 0, -1)
    OP_22(0x67, 0x0, 0x64)
    OP_6D(990, -12000, 1420, 2000)
    Sleep(2000)
    Return()

    # Function_3_210 end

    def Function_4_236(): pass

    label("Function_4_236")

    FadeToDark(2000, 0, -1)
    OP_22(0x67, 0x0, 0x64)
    OP_6D(990, -12000, 1420, 2000)
    Sleep(1000)
    OP_20(0x3E8)
    Sleep(1000)
    Return()

    # Function_4_236 end

    def Function_5_266(): pass

    label("Function_5_266")

    FadeToDark(2000, 0, -1)
    OP_22(0x67, 0x0, 0x64)
    OP_6D(990, 12000, 1420, 2000)
    Sleep(2000)
    Return()

    # Function_5_266 end

    SaveToFile()

Try(main)
