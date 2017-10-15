from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C5614   ._SN',
        MapName             = 'Other',
        Location            = 'C5614.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60061",
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
        Unknown_08              = 6000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 0,
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
    OP_6D(1120, 0, 4019, 0)
    OP_67(0, 8620, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 650, 0, 2620, 90)
    SetChrPos(0x1, 650, 0, 3800, 90)
    SetChrPos(0x2, -930, 0, 2620, 90)
    SetChrPos(0x3, -930, 0, 3800, 90)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x393, 2)), scpexpr(EXPR_END)), "loc_154")
    Call(0, 3)
    NewScene("ED6_DT21/C5611   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1C4")

    label("loc_154")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x393, 3)), scpexpr(EXPR_END)), "loc_16B")
    Call(0, 4)
    NewScene("ED6_DT21/C5610   ._SN", 132, 0, 0)
    IdleLoop()
    Jump("loc_1C4")

    label("loc_16B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x393, 4)), scpexpr(EXPR_END)), "loc_182")
    Call(0, 3)
    NewScene("ED6_DT21/C5612   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1C4")

    label("loc_182")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x393, 5)), scpexpr(EXPR_END)), "loc_199")
    Call(0, 4)
    NewScene("ED6_DT21/C5611   ._SN", 101, 0, 0)
    IdleLoop()
    Jump("loc_1C4")

    label("loc_199")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x393, 6)), scpexpr(EXPR_END)), "loc_1B0")
    Call(0, 3)
    NewScene("ED6_DT21/C5613   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1C4")

    label("loc_1B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x393, 7)), scpexpr(EXPR_END)), "loc_1C4")
    Call(0, 4)
    NewScene("ED6_DT21/C5612   ._SN", 101, 0, 0)
    IdleLoop()

    label("loc_1C4")

    Return()

    # Function_2_B0 end

    def Function_3_1C5(): pass

    label("Function_3_1C5")

    FadeToDark(2000, 0, -1)
    OP_22(0x67, 0x0, 0x64)
    OP_6D(1120, -12000, 4019, 2000)
    Sleep(2000)
    Return()

    # Function_3_1C5 end

    def Function_4_1EB(): pass

    label("Function_4_1EB")

    FadeToDark(2000, 0, -1)
    OP_22(0x67, 0x0, 0x64)
    OP_6D(1120, 12000, 4019, 2000)
    Sleep(2000)
    Return()

    # Function_4_1EB end

    SaveToFile()

Try(main)
