from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3112   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3112.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
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
        '目标用照相机',                         # 9
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_CA",           # 00, 0
        "Function_1_101",          # 01, 1
        "Function_2_102",          # 02, 2
        "Function_3_40D",          # 03, 3
        "Function_4_44A",          # 04, 4
    )


    def Function_0_CA(): pass

    label("Function_0_CA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_F5")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)
    Jump("loc_F9")

    label("loc_F5")

    Event(0, 4)

    label("loc_F9")

    Jump("loc_100")

    label("loc_FC")

    Event(0, 4)

    label("loc_100")

    Return()

    # Function_0_CA end

    def Function_1_101(): pass

    label("Function_1_101")

    Return()

    # Function_1_101 end

    def Function_2_102(): pass

    label("Function_2_102")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_1D(0x53)
    OP_6D(1780, 0, 2220, 0)
    OP_67(0, 4520, -10000, 0)
    OP_6B(3030, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x107, -40, 0, -1160, 0)
    OP_9F(0x107, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x107, 0x4)
    Sleep(2000)
    FadeToBright(2000, 0)
    Sleep(1000)
    OP_22(0x6D, 0x0, 0x64)
    Sleep(500)

    def lambda_191():
        OP_6D(1600, 0, 2860, 1500)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_191)
    OP_43(0x107, 0x0, 0x0, 0x3)
    WaitChrThread(0x107, 0x0)
    WaitChrThread(0x10, 0x0)
    OP_8C(0x107, 270, 400)
    Sleep(300)
    OP_62(0x107, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x107)
    Sleep(500)

    ChrTalk(    #0
        0x107,
        (
            "#561F#40W……这种事，我知道的啊。\x02\x03",

            "就算妈妈不说，\x01",
            "这点事我也知道……\x02\x03",

            "#069F但是……但是………！\x02\x03",

            "这样的话，我到底算是什么啊！？\x02\x03",

            "#068F什么也做不到……！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x107)
    Sleep(500)

    ChrTalk(    #1
        0x107,
        (
            "#561F#40W………………对了。\x01",
            "去和爸爸商量看看吧。\x02\x03",

            "如果是爸爸的话\x01",
            "说不定会理解我……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)
    OP_8C(0x107, 90, 400)

    def lambda_338():
        OP_6D(2500, 0, 2870, 1500)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_338)

    def lambda_350():
        OP_8E(0xFE, 0x690, 0x0, 0x578, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_350)
    WaitChrThread(0x107, 0x1)
    WaitChrThread(0x10, 0x0)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05提妲在槽中插入认证卡片。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Sleep(500)
    OP_22(0x9C, 0x0, 0x64)
    OP_77(0xFF, 0x64, 0x64, 0x0, 0x0)
    Sleep(1500)
    FadeToDark(2000, 0, -1)
    OP_22(0x67, 0x0, 0x64)
    OP_6D(2500, 11900, 2870, 2000)
    OP_0D()
    Sleep(800)
    OP_23(0x67)
    Sleep(500)
    SetMapFlags(0x2000000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T3121   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_102 end

    def Function_3_40D(): pass

    label("Function_3_40D")


    def lambda_413():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x258)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_413)

    def lambda_425():
        OP_8F(0xFE, 0x5A, 0x0, 0x622, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_425)
    WaitChrThread(0xFE, 0x1)
    WaitChrThread(0xFE, 0x2)
    OP_22(0x6D, 0x0, 0x64)
    Return()

    # Function_3_40D end

    def Function_4_44A(): pass

    label("Function_4_44A")

    ClearMapFlags(0x1)
    EventBegin(0x1)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6D(1400, 0, 4500, 0)
    SetChrPos(0x0, 1750, 0, 1370, 90)
    SetChrPos(0x1, 1280, 0, 2600, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C4")
    SetChrPos(0x2, 70, 0, 1470, 180)

    label("loc_4C4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4E1")
    SetChrPos(0x3, -50, 0, 2600, 180)

    label("loc_4E1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4FE")
    SetChrPos(0x4, -1380, 0, 1470, 180)

    label("loc_4FE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_51B")
    SetChrPos(0x5, -1380, 0, 2600, 180)

    label("loc_51B")

    Sleep(200)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5BD")

    Menu(
        0,
        10,
        10,
        0,
        (
            "　【 顶楼 】\x01",      # 0
            "　【 ５层 】\x01",      # 1
            "　【 ４层 】\x01",      # 2
            "　【 ３层 】\x01",      # 3
            "　【 ２层 】\x01",      # 4
            "　【 １层 】\x01",      # 5
            "★【 Ｂ１ 】\x01",      # 6
            "　【 离开 】\x01",      # 7
        )
    )

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8F6")

    label("loc_5BD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_647")

    Menu(
        0,
        10,
        10,
        0,
        (
            "　【 顶楼 】\x01",      # 0
            "　【 ５层 】\x01",      # 1
            "　【 ４层 】\x01",      # 2
            "　【 ３层 】\x01",      # 3
            "　【 ２层 】\x01",      # 4
            "★【 １层 】\x01",      # 5
            "　【 Ｂ１ 】\x01",      # 6
            "　【 离开 】\x01",      # 7
        )
    )

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8F6")

    label("loc_647")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D1")

    Menu(
        0,
        10,
        10,
        0,
        (
            "　【 顶楼 】\x01",      # 0
            "　【 ５层 】\x01",      # 1
            "　【 ４层 】\x01",      # 2
            "　【 ３层 】\x01",      # 3
            "★【 ２层 】\x01",      # 4
            "　【 １层 】\x01",      # 5
            "　【 Ｂ１ 】\x01",      # 6
            "　【 离开 】\x01",      # 7
        )
    )

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8F6")

    label("loc_6D1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_75B")

    Menu(
        0,
        10,
        10,
        0,
        (
            "　【 顶楼 】\x01",      # 0
            "　【 ５层 】\x01",      # 1
            "　【 ４层 】\x01",      # 2
            "★【 ３层 】\x01",      # 3
            "　【 ２层 】\x01",      # 4
            "　【 １层 】\x01",      # 5
            "　【 Ｂ１ 】\x01",      # 6
            "　【 离开 】\x01",      # 7
        )
    )

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8F6")

    label("loc_75B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E5")

    Menu(
        0,
        10,
        10,
        0,
        (
            "　【 顶楼 】\x01",      # 0
            "　【 ５层 】\x01",      # 1
            "★【 ４层 】\x01",      # 2
            "　【 ３层 】\x01",      # 3
            "　【 ２层 】\x01",      # 4
            "　【 １层 】\x01",      # 5
            "　【 Ｂ１ 】\x01",      # 6
            "　【 离开 】\x01",      # 7
        )
    )

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8F6")

    label("loc_7E5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_86F")

    Menu(
        0,
        10,
        10,
        0,
        (
            "　【 顶楼 】\x01",      # 0
            "★【 ５层 】\x01",      # 1
            "　【 ４层 】\x01",      # 2
            "　【 ３层 】\x01",      # 3
            "　【 ２层 】\x01",      # 4
            "　【 １层 】\x01",      # 5
            "　【 Ｂ１ 】\x01",      # 6
            "　【 离开 】\x01",      # 7
        )
    )

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8F6")

    label("loc_86F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8F6")

    Menu(
        0,
        10,
        10,
        0,
        (
            "★【 顶楼 】\x01",      # 0
            "　【 ５层 】\x01",      # 1
            "　【 ４层 】\x01",      # 2
            "　【 ３层 】\x01",      # 3
            "　【 ２层 】\x01",      # 4
            "　【 １层 】\x01",      # 5
            "　【 Ｂ１ 】\x01",      # 6
            "　【 离开 】\x01",      # 7
        )
    )

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8F6")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_92C")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_92C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_93C")
    Jump("loc_9A7")

    label("loc_93C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_973")
    FadeToDark(2000, 0, -1)
    OP_22(0x67, 0x0, 0x64)
    OP_6D(1400, -11900, 4500, 2000)
    OP_0D()
    Sleep(800)
    OP_23(0x67)
    Jump("loc_9A7")

    label("loc_973")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9A7")
    FadeToDark(2000, 0, -1)
    OP_22(0x67, 0x0, 0x64)
    OP_6D(1400, 11900, 4500, 2000)
    OP_0D()
    Sleep(800)
    OP_23(0x67)

    label("loc_9A7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A30")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_9D9"),
        (1, "loc_9E5"),
        (2, "loc_9F1"),
        (3, "loc_9FD"),
        (4, "loc_A09"),
        (5, "loc_A15"),
        (6, "loc_A21"),
        (SWITCH_DEFAULT, "loc_A2D"),
    )


    label("loc_9D9")

    NewScene("ED6_DT21/T3111   ._SN", 106, 0, 0)
    IdleLoop()
    Jump("loc_A2D")

    label("loc_9E5")

    NewScene("ED6_DT21/T3111   ._SN", 101, 0, 0)
    IdleLoop()
    Jump("loc_A2D")

    label("loc_9F1")

    NewScene("ED6_DT21/T3114   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_A2D")

    label("loc_9FD")

    NewScene("ED6_DT21/T3114   ._SN", 106, 0, 0)
    IdleLoop()
    Jump("loc_A2D")

    label("loc_A09")

    NewScene("ED6_DT21/T3114   ._SN", 112, 0, 0)
    IdleLoop()
    Jump("loc_A2D")

    label("loc_A15")

    NewScene("ED6_DT21/T3119   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_A2D")

    label("loc_A21")

    NewScene("ED6_DT21/T3101   ._SN", 104, 0, 0)
    IdleLoop()
    Jump("loc_A2D")

    label("loc_A2D")

    Jump("loc_AEF")

    label("loc_A30")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_A55"),
        (1, "loc_A6B"),
        (2, "loc_A81"),
        (3, "loc_A97"),
        (4, "loc_AAD"),
        (5, "loc_AC3"),
        (6, "loc_AD9"),
        (SWITCH_DEFAULT, "loc_AEF"),
    )


    label("loc_A55")

    OP_22(0xE, 0x0, 0x64)
    Sleep(500)
    NewScene("ED6_DT21/T3111   ._SN", 106, 0, 0)
    IdleLoop()
    Jump("loc_AEF")

    label("loc_A6B")

    OP_22(0xE, 0x0, 0x64)
    Sleep(500)
    NewScene("ED6_DT21/T3111   ._SN", 101, 0, 0)
    IdleLoop()
    Jump("loc_AEF")

    label("loc_A81")

    OP_22(0xE, 0x0, 0x64)
    Sleep(500)
    NewScene("ED6_DT21/T3114   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_AEF")

    label("loc_A97")

    OP_22(0xE, 0x0, 0x64)
    Sleep(500)
    NewScene("ED6_DT21/T3114   ._SN", 106, 0, 0)
    IdleLoop()
    Jump("loc_AEF")

    label("loc_AAD")

    OP_22(0xE, 0x0, 0x64)
    Sleep(500)
    NewScene("ED6_DT21/T3114   ._SN", 112, 0, 0)
    IdleLoop()
    Jump("loc_AEF")

    label("loc_AC3")

    OP_22(0xE, 0x0, 0x64)
    Sleep(500)
    NewScene("ED6_DT21/T3119   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_AEF")

    label("loc_AD9")

    OP_22(0xE, 0x0, 0x64)
    Sleep(500)
    NewScene("ED6_DT21/T3101   ._SN", 104, 0, 0)
    IdleLoop()
    Jump("loc_AEF")

    label("loc_AEF")

    Return()

    # Function_4_44A end

    SaveToFile()

Try(main)
