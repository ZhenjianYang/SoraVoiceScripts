from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 调试地图

    CreateScenaFile(
        FileName            = 'A0019   ._SN',
        MapName             = 'map1',
        Location            = 'A0006.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 3,
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


    DeclActor(
        TriggerX            = 1800,
        TriggerZ            = 1000,
        TriggerY            = 120,
        TriggerRange        = 2000,
        ActorX              = 1800,
        ActorZ              = 1000,
        ActorY              = 120,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 4000,
        TriggerZ            = 1000,
        TriggerY            = 120,
        TriggerRange        = 2000,
        ActorX              = 4000,
        ActorZ              = 1000,
        ActorY              = 120,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_F2",           # 00, 0
        "Function_1_FD",           # 01, 1
        "Function_2_18D",          # 02, 2
        "Function_3_23B",          # 03, 3
        "Function_4_2D1",          # 04, 4
    )


    def Function_0_F2(): pass

    label("Function_0_F2")

    OP_3E(0x383, 1)
    OP_3E(0x150, 1)
    Return()

    # Function_0_F2 end

    def Function_1_FD(): pass

    label("Function_1_FD")

    OP_BE(0x0, 0x1, 0x2, 0x28, 0x0, 0x2, 1000, 0, 5000, 5000, 1000, 10000)
    OP_BE(0x1, 0x4, 0x2, 0x14, 0x0, 0x1, 10000, -500, 2000, 6000, 1000, 0)
    OP_BE(0x2, 0x2, 0x0, 0x3C, 0x3, 0x0, 0, 0, 0, 0, 0, 0)
    OP_BF(0x2, 0x2, 2, 2000)
    OP_BF(0x2, 0x2, 3, 4000)
    OP_C1(0x80, 0x1, 0x3C)
    OP_C1(0x81, 0x1, 0x3C)
    OP_C1(0x82, 0x1, 0x3C)
    OP_C4(0x0, 0x1)
    Return()

    # Function_1_FD end

    def Function_2_18D(): pass

    label("Function_2_18D")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B7")
    OP_6F(0x0, 0)
    OP_70(0x0, 0x3C)
    Sleep(500)
    OP_82(0x80, 0x2)
    OP_82(0x81, 0x2)
    OP_A2(0x0)
    Jump("loc_237")

    label("loc_1B7")

    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)
    Sleep(500)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A3(0x0)

    label("loc_237")

    TalkEnd(0xFF)
    Return()

    # Function_2_18D end

    def Function_3_23B(): pass

    label("Function_3_23B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x13), scpexpr(EXPR_PUSH_LONG, 0x383), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D0")
    EventBegin(0x0)
    OP_C0(0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_62(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x3C)
    Sleep(500)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)
    Sleep(500)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x3C)
    Sleep(500)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)
    Sleep(500)
    EventEnd(0x0)

    label("loc_2D0")

    Return()

    # Function_3_23B end

    def Function_4_2D1(): pass

    label("Function_4_2D1")

    TalkBegin(0xFF)
    OP_18()
    ExitThread()
    ExitThread()
    ExitThread()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x383), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FC")
    OP_62(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_2FC")

    TalkEnd(0xFF)
    Return()

    # Function_4_2D1 end

    SaveToFile()

Try(main)
