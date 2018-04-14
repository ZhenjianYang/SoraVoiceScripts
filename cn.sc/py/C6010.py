from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C6010   ._SN',
        MapName             = 'Other',
        Location            = 'C6010.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60062",
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
        "Function_1_B9",           # 01, 1
        "Function_2_1CE",          # 02, 2
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_B8")
    OP_A3(0x10F0)
    Event(0, 2)

    label("loc_B8")

    Return()

    # Function_0_AA end

    def Function_1_B9(): pass

    label("Function_1_B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x442, 0)), scpexpr(EXPR_END)), "loc_F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x442, 5)), scpexpr(EXPR_END)), "loc_D3")
    OP_B1("C6010_1")
    Jump("loc_F6")

    label("loc_D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x442, 6)), scpexpr(EXPR_END)), "loc_E6")
    OP_B1("C6010_1")
    Jump("loc_F6")

    label("loc_E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x442, 7)), scpexpr(EXPR_END)), "loc_F6")
    OP_B1("C6010_4")

    label("loc_F6")

    Jump("loc_1B6")

    label("loc_F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x442, 1)), scpexpr(EXPR_END)), "loc_139")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x442, 4)), scpexpr(EXPR_END)), "loc_113")
    OP_B1("C6010_1")
    Jump("loc_136")

    label("loc_113")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x442, 6)), scpexpr(EXPR_END)), "loc_126")
    OP_B1("C6010_2")
    Jump("loc_136")

    label("loc_126")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x442, 7)), scpexpr(EXPR_END)), "loc_136")
    OP_B1("C6010_2")

    label("loc_136")

    Jump("loc_1B6")

    label("loc_139")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x442, 2)), scpexpr(EXPR_END)), "loc_179")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x442, 4)), scpexpr(EXPR_END)), "loc_153")
    OP_B1("C6010_3")
    Jump("loc_176")

    label("loc_153")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x442, 5)), scpexpr(EXPR_END)), "loc_166")
    OP_B1("C6010_2")
    Jump("loc_176")

    label("loc_166")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x442, 7)), scpexpr(EXPR_END)), "loc_176")
    OP_B1("C6010_3")

    label("loc_176")

    Jump("loc_1B6")

    label("loc_179")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x442, 3)), scpexpr(EXPR_END)), "loc_1B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x442, 4)), scpexpr(EXPR_END)), "loc_193")
    OP_B1("C6010_4")
    Jump("loc_1B6")

    label("loc_193")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x442, 5)), scpexpr(EXPR_END)), "loc_1A6")
    OP_B1("C6010_4")
    Jump("loc_1B6")

    label("loc_1A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x442, 6)), scpexpr(EXPR_END)), "loc_1B6")
    OP_B1("C6010_3")

    label("loc_1B6")

    OP_22(0x13E, 0x0, 0x64)
    OP_22(0x1C3, 0x1, 0x64)
    StopSound(0x124F8, 0x493E0, 0x0)
    Return()

    # Function_1_B9 end

    def Function_2_1CE(): pass

    label("Function_2_1CE")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x442, 0)), scpexpr(EXPR_END)), "loc_31B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x442, 5)), scpexpr(EXPR_END)), "loc_243")
    OP_6D(1000, 0, -360, 0)
    OP_67(0, 2300, -10000, 0)
    OP_6B(6250, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_76(0x1, 0x0, 0x1, 0x19, 0x0, 0x0, 0x0, 0x0)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x12C)
    Jump("loc_318")

    label("loc_243")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x442, 6)), scpexpr(EXPR_END)), "loc_2AF")
    OP_6D(1000, 0, -360, 0)
    OP_67(0, 2300, -10000, 0)
    OP_6B(6250, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_76(0x1, 0x0, 0x1, 0x19, 0x0, 0x0, 0x0, 0x0)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x12C)
    Jump("loc_318")

    label("loc_2AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x442, 7)), scpexpr(EXPR_END)), "loc_318")
    OP_6D(1000, 0, -360, 0)
    OP_67(0, 2300, -10000, 0)
    OP_6B(6250, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_76(0x1, 0x0, 0x1, 0x19, 0x0, 0x0, 0x0, 0x0)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x12C)

    label("loc_318")

    Jump("loc_6F9")

    label("loc_31B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x442, 1)), scpexpr(EXPR_END)), "loc_466")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x442, 4)), scpexpr(EXPR_END)), "loc_38E")
    OP_6D(1000, 0, -360, 0)
    OP_67(0, 2300, -10000, 0)
    OP_6B(6250, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_76(0x1, 0x0, 0x1, 0xFFFFFFE7, 0x0, 0x0, 0x0, 0x0)
    OP_6F(0x0, 300)
    OP_70(0x0, 0x0)
    Jump("loc_463")

    label("loc_38E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x442, 6)), scpexpr(EXPR_END)), "loc_3FA")
    OP_6D(1000, 0, -360, 0)
    OP_67(0, 2300, -10000, 0)
    OP_6B(6250, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_76(0x1, 0x0, 0x1, 0x19, 0x0, 0x0, 0x0, 0x0)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x12C)
    Jump("loc_463")

    label("loc_3FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x442, 7)), scpexpr(EXPR_END)), "loc_463")
    OP_6D(1000, 0, -360, 0)
    OP_67(0, 2300, -10000, 0)
    OP_6B(6250, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_76(0x1, 0x0, 0x1, 0x19, 0x0, 0x0, 0x0, 0x0)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x12C)

    label("loc_463")

    Jump("loc_6F9")

    label("loc_466")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x442, 2)), scpexpr(EXPR_END)), "loc_5B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x442, 4)), scpexpr(EXPR_END)), "loc_4D9")
    OP_6D(1000, 0, -360, 0)
    OP_67(0, 2300, -10000, 0)
    OP_6B(6250, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_76(0x1, 0x0, 0x1, 0xFFFFFFE7, 0x0, 0x0, 0x0, 0x0)
    OP_6F(0x0, 300)
    OP_70(0x0, 0x0)
    Jump("loc_5AE")

    label("loc_4D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x442, 5)), scpexpr(EXPR_END)), "loc_545")
    OP_6D(1000, 0, -360, 0)
    OP_67(0, 2300, -10000, 0)
    OP_6B(6250, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_76(0x1, 0x0, 0x1, 0xFFFFFFE7, 0x0, 0x0, 0x0, 0x0)
    OP_6F(0x0, 300)
    OP_70(0x0, 0x0)
    Jump("loc_5AE")

    label("loc_545")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x442, 7)), scpexpr(EXPR_END)), "loc_5AE")
    OP_6D(1000, 0, -360, 0)
    OP_67(0, 2300, -10000, 0)
    OP_6B(6250, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_76(0x1, 0x0, 0x1, 0xFFFFFFE7, 0x0, 0x0, 0x0, 0x0)
    OP_6F(0x0, 300)
    OP_70(0x0, 0x0)

    label("loc_5AE")

    Jump("loc_6F9")

    label("loc_5B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x442, 3)), scpexpr(EXPR_END)), "loc_6F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x442, 4)), scpexpr(EXPR_END)), "loc_624")
    OP_6D(1000, 0, -360, 0)
    OP_67(0, 2300, -10000, 0)
    OP_6B(6250, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_76(0x1, 0x0, 0x1, 0xFFFFFFE7, 0x0, 0x0, 0x0, 0x0)
    OP_6F(0x0, 300)
    OP_70(0x0, 0x0)
    Jump("loc_6F9")

    label("loc_624")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x442, 5)), scpexpr(EXPR_END)), "loc_690")
    OP_6D(1000, 0, -360, 0)
    OP_67(0, 2300, -10000, 0)
    OP_6B(6250, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_76(0x1, 0x0, 0x1, 0xFFFFFFE7, 0x0, 0x0, 0x0, 0x0)
    OP_6F(0x0, 300)
    OP_70(0x0, 0x0)
    Jump("loc_6F9")

    label("loc_690")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x442, 6)), scpexpr(EXPR_END)), "loc_6F9")
    OP_6D(1000, 0, -360, 0)
    OP_67(0, 2300, -10000, 0)
    OP_6B(6250, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_76(0x1, 0x0, 0x1, 0x19, 0x0, 0x0, 0x0, 0x0)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x12C)

    label("loc_6F9")


    def lambda_6FF():
        OP_6B(8570, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6FF)

    def lambda_70F():
        OP_67(0, 3300, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_70F)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x100000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x442, 4)), scpexpr(EXPR_END)), "loc_759")
    OP_A3(0x2214)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/C6000   ._SN", 101, 0, 0)
    IdleLoop()
    Jump("loc_7A1")

    label("loc_759")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x442, 5)), scpexpr(EXPR_END)), "loc_772")
    OP_A3(0x2215)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C6001   ._SN", 101, 0, 0)
    IdleLoop()
    Jump("loc_7A1")

    label("loc_772")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x442, 6)), scpexpr(EXPR_END)), "loc_78B")
    OP_A3(0x2216)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C6002   ._SN", 101, 0, 0)
    IdleLoop()
    Jump("loc_7A1")

    label("loc_78B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x442, 7)), scpexpr(EXPR_END)), "loc_7A1")
    OP_A3(0x2217)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C6003   ._SN", 101, 0, 0)
    IdleLoop()

    label("loc_7A1")

    Return()

    # Function_2_1CE end

    SaveToFile()

Try(main)
