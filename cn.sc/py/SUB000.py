from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'SUB000  ._SN',
        MapName             = 'a',
        Location            = 'a.x',
        MapIndex            = 0,
        MapDefaultBGM       = "ed60000",
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
        "Function_1_AB",           # 01, 1
        "Function_2_AC",           # 02, 2
        "Function_3_153",          # 03, 3
        "Function_4_1AB",          # 04, 4
        "Function_5_1FF",          # 05, 5
        "Function_6_243",          # 06, 6
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Return()

    # Function_0_AA end

    def Function_1_AB(): pass

    label("Function_1_AB")

    Return()

    # Function_1_AB end

    def Function_2_AC(): pass

    label("Function_2_AC")

    RunExpression(0x65, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x65), scpexpr(EXPR_END)),
        (0, "loc_DD"),
        (1, "loc_E9"),
        (2, "loc_F5"),
        (3, "loc_101"),
        (4, "loc_10D"),
        (5, "loc_119"),
        (6, "loc_125"),
        (SWITCH_DEFAULT, "loc_131"),
    )


    label("loc_DD")

    OP_99(0xFE, 0x0, 0x7, 0x5AA)
    Jump("loc_13D")

    label("loc_E9")

    OP_99(0xFE, 0x0, 0x7, 0x60E)
    Jump("loc_13D")

    label("loc_F5")

    OP_99(0xFE, 0x0, 0x7, 0x640)
    Jump("loc_13D")

    label("loc_101")

    OP_99(0xFE, 0x0, 0x7, 0x578)
    Jump("loc_13D")

    label("loc_10D")

    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_13D")

    label("loc_119")

    OP_99(0xFE, 0x0, 0x7, 0x546)
    Jump("loc_13D")

    label("loc_125")

    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_13D")

    label("loc_131")

    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_13D")

    label("loc_13D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_152")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_13D")

    label("loc_152")

    Return()

    # Function_2_AC end

    def Function_3_153(): pass

    label("Function_3_153")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",            # 0
            "改造·换钱\x01",      # 1
            "离开\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AA")
    OP_0D()

    label("loc_1AA")

    Return()

    # Function_3_153 end

    def Function_4_1AB(): pass

    label("Function_4_1AB")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",        # 0
            "买东西\x01",      # 1
            "离开\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FE")
    OP_0D()

    label("loc_1FE")

    Return()

    # Function_4_1AB end

    def Function_5_1FF(): pass

    label("Function_5_1FF")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",      # 0
            "报告\x01",      # 1
            "离开\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Return()

    # Function_5_1FF end

    def Function_6_243(): pass

    label("Function_6_243")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",      # 0
            "休息\x01",      # 1
            "离开\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_294")
    OP_0D()

    label("loc_294")

    Return()

    # Function_6_243 end

    SaveToFile()

Try(main)
