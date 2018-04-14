from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C2209   ._SN',
        MapName             = 'Ruan',
        Location            = 'C2209.x',
        MapIndex            = 84,
        MapDefaultBGM       = "ed60015",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/C2209   ._SN',
            'ED6_DT21/C2209_1 ._SN',
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
        '玛诺利亚间道方向',                     # 9
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


    DeclNpc(
        X                   = 1330,
        Z                   = -430,
        Y                   = -46450,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = -960,
        TriggerZ            = 25000,
        TriggerY            = -770,
        TriggerRange        = 800,
        ActorX              = -960,
        ActorZ              = 26500,
        ActorY              = -770,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 15480,
        TriggerZ            = 20,
        TriggerY            = -7900,
        TriggerRange        = 1000,
        ActorX              = 23640,
        ActorZ              = -10010,
        ActorY              = -9260,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_112",          # 00, 0
        "Function_1_126",          # 01, 1
        "Function_2_150",          # 02, 2
        "Function_3_157",          # 03, 3
        "Function_4_15E",          # 04, 4
        "Function_5_1B8",          # 05, 5
    )


    def Function_0_112(): pass

    label("Function_0_112")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_125")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(1, 0)

    label("loc_125")

    Return()

    # Function_0_112 end

    def Function_1_126(): pass

    label("Function_1_126")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFDDD20, 0x230050)
    OP_B0(0x0, 0x78)
    OP_B0(0x1, 0x78)
    OP_1C(0x0, 0x0, 0x2)
    OP_1C(0x1, 0x0, 0x3)
    OP_22(0x1C5, 0x1, 0x64)
    Return()

    # Function_1_126 end

    def Function_2_150(): pass

    label("Function_2_150")

    TalkBegin(0xFF)
    TalkEnd(0xFF)
    Return()

    # Function_2_150 end

    def Function_3_157(): pass

    label("Function_3_157")

    TalkBegin(0xFF)
    TalkEnd(0xFF)
    Return()

    # Function_3_157 end

    def Function_4_15E(): pass

    label("Function_4_15E")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #0
        (
            "\x07\x05　　　危险！　　　\x01",
            "※非工作人员禁止进入\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_4_15E end

    def Function_5_1B8(): pass

    label("Function_5_1B8")

    EventBegin(0x1)

    ChrTalk(    #1
        0x101,
        "#1001F这里好像可以钓上什么来。\x02",
    )

    CloseMessageWindow()

    def lambda_1E4():
        OP_6D(20710, 20, -9100, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1E4)

    def lambda_1FC():
        OP_6D(17710, 20, -13100, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1FC)

    def lambda_214():
        OP_67(0, 9500, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_214)

    def lambda_22C():
        OP_6B(3250, 1500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_22C)

    def lambda_23C():
        OP_6C(45000, 1500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_23C)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05钓鱼吗？\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "钓鱼\x01",      # 0
            "离开\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    WaitChrThread(0x0, 0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C3")
    OP_C0(0xE, 0x14, 0x3C3C, 0xA, 0xFFFFE0B6, 0x5A, 0x5F78, 0xFFFFCE00, 0xFFFFE0C0)
    OP_0D()
    EventEnd(0x1)
    Jump("loc_2D2")

    label("loc_2C3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D2")
    EventEnd(0x1)

    label("loc_2D2")

    Return()

    # Function_5_1B8 end

    SaveToFile()

Try(main)
