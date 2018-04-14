from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1200   ._SN',
        MapName             = 'Bose',
        Location            = 'T1200.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60015",
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
        '拉文努山道方向',                       # 9
        '拉文努废坑方向',                       # 10
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
        X                   = -2080,
        Z                   = 0,
        Y                   = -80,
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

    DeclNpc(
        X                   = 7170,
        Z                   = 8000,
        Y                   = 78890,
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


    DeclEvent(
        X                   = 5000,
        Y                   = 0,
        Z                   = 34240,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 4,
    )

    DeclEvent(
        X                   = 5150,
        Y                   = 4550,
        Z                   = 41780,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 4,
    )

    DeclEvent(
        X                   = 5310,
        Y                   = 0,
        Z                   = 23020,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 5,
    )

    DeclEvent(
        X                   = 6000,
        Y                   = 4400,
        Z                   = 54640,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 6,
    )


    DeclActor(
        TriggerX            = 34960,
        TriggerZ            = -3850,
        TriggerY            = 8220,
        TriggerRange        = 1000,
        ActorX              = 35010,
        ActorZ              = -4200,
        ActorY              = 5190,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_18E",          # 00, 0
        "Function_1_19F",          # 01, 1
        "Function_2_1B2",          # 02, 2
        "Function_3_1CB",          # 03, 3
        "Function_4_2D4",          # 04, 4
        "Function_5_2D8",          # 05, 5
        "Function_6_2DC",          # 06, 6
    )


    def Function_0_18E(): pass

    label("Function_0_18E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_19E")
    SetMapFlags(0x10000000)
    Event(0, 2)

    label("loc_19E")

    Return()

    # Function_0_18E end

    def Function_1_19F(): pass

    label("Function_1_19F")

    OP_16(0x2, 0xFA0, 0xFFFE5638, 0xFFFE98A0, 0x230043)
    Return()

    # Function_1_19F end

    def Function_2_1B2(): pass

    label("Function_2_1B2")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (109, "loc_1BE"),
        (SWITCH_DEFAULT, "loc_1CA"),
    )


    label("loc_1BE")

    NewScene("ED6_DT21/T1201   ._SN", 109, 0, 0)
    IdleLoop()
    Jump("loc_1CA")

    label("loc_1CA")

    Return()

    # Function_2_1B2 end

    def Function_3_1CB(): pass

    label("Function_3_1CB")

    EventBegin(0x1)

    ChrTalk(    #0
        0x101,
        "#1001F这里好像可以钓上什么来。\x02",
    )

    CloseMessageWindow()

    def lambda_1F7():
        OP_6D(35190, -3850, 5430, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1F7)

    def lambda_20F():
        OP_6B(2800, 1500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_20F)

    def lambda_21F():
        OP_6C(225000, 1500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_21F)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #1
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C4")
    RunExpression(0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x28), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x101, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NOT), scpexpr(EXPR_AND_SAVE), scpexpr(EXPR_END)))
    OP_C0(0xE, 0xA, 0x8976, 0xFFFFF0F6, 0x21D4, 0xB4, 0x88C2, 0xFFFFEF98, 0x1446)
    OP_51(0x101, 0x28, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    EventEnd(0x1)
    Jump("loc_2D3")

    label("loc_2C4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D3")
    EventEnd(0x1)

    label("loc_2D3")

    Return()

    # Function_3_1CB end

    def Function_4_2D4(): pass

    label("Function_4_2D4")

    SetPlaceName(0x2E)
    Return()

    # Function_4_2D4 end

    def Function_5_2D8(): pass

    label("Function_5_2D8")

    SetPlaceName(0x2D)
    Return()

    # Function_5_2D8 end

    def Function_6_2DC(): pass

    label("Function_6_2DC")

    SetPlaceName(0x2F)
    Return()

    # Function_6_2DC end

    SaveToFile()

Try(main)
