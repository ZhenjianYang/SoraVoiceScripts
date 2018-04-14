from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'T5101   ._SN',
        MapName             = 'Other',
        Location            = 'T5101.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60084",
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
        '克鲁茨',                               # 9
        '目标用照相机',                         # 10
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


    AddCharChip(
        'ED6_DT07/CH01620 ._CH',             # 00
    )

    AddCharChipPat(
        'ED6_DT07/CH01620P._CP',             # 00
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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


    DeclEvent(
        X                   = -4320,
        Y                   = 0,
        Z                   = -36940,
        Range               = 3430,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFF7338,
        Unknown_18          = 0x0,
        Unknown_1C          = 3,
    )


    DeclActor(
        TriggerX            = -3550,
        TriggerZ            = 0,
        TriggerY            = -3000,
        TriggerRange        = 800,
        ActorX              = -4250,
        ActorZ              = 1000,
        ActorY              = -3000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_136",          # 00, 0
        "Function_1_143",          # 01, 1
        "Function_2_15B",          # 02, 2
        "Function_3_405",          # 03, 3
        "Function_4_483",          # 04, 4
    )


    def Function_0_136(): pass

    label("Function_0_136")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x201, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_142")
    Event(0, 2)

    label("loc_142")

    Return()

    # Function_0_136 end

    def Function_1_143(): pass

    label("Function_1_143")

    OP_16(0x2, 0xFA0, 0xFFFE13D0, 0xFFFDE4F0, 0x23006F)
    OP_22(0x1C3, 0x0, 0x64)
    Return()

    # Function_1_143 end

    def Function_2_15B(): pass

    label("Function_2_15B")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_6D(5450, 0, 52290, 0)
    OP_67(0, 12830, -10000, 0)
    OP_6B(4830, 0)
    OP_6C(325000, 0)
    OP_6E(262, 0)
    SetChrPos(0x8, -1740, 0, -20510, 356)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x101, -2300, 0, -22520, 70)
    SetChrPos(0x10A, -650, 0, -22430, 342)

    def lambda_1DD():
        OP_6D(-5130, 0, 1290, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1DD)

    def lambda_1F5():
        OP_67(0, 12830, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1F5)

    def lambda_20D():
        OP_6C(315000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_20D)
    Sleep(4000)

    def lambda_222():
        OP_8E(0x8, 0xFFFFF8EE, 0x0, 0xFFFFFFBA, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_222)
    Sleep(200)

    def lambda_242():
        OP_8E(0x101, 0xFFFFF7F4, 0x0, 0xFFFFF61E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_242)
    Sleep(100)

    def lambda_262():
        OP_8E(0x10A, 0xFFFFFC0E, 0x0, 0xFFFFF61E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_262)
    WaitChrThread(0x101, 0x1)
    Fade(500)
    OP_6D(-1960, 0, -1210, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2900, 0)
    OP_6E(262, 0)
    OP_6C(315000, 0)
    WaitChrThread(0x8, 0x1)
    OP_44(0x8, 0x2)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x0)
    OP_8C(0x8, 180, 500)
    Sleep(500)

    ChrTalk(    #0
        0x8,
        (
            "#841F好了，今天的训练结束了。\x02\x03",

            "你们两人都辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x101,
        "#1019F#6P好、好累～……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x10A,
        (
            "#813F确、确实……\x01",
            "到现在为止最严苛的训练啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "#843F哎呀哎呀。\x01",
            "你们体力还差得太远啊。\x02\x03",

            "#840F今晚早点休息，\x01",
            "准备明天的训练吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        "#1007F#6P是～……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x10A,
        "#1316F您辛苦了～……\x02",
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_23(0x1C3)
    NewScene("ED6_DT21/T5111   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_15B end

    def Function_3_405(): pass

    label("Function_3_405")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x201, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x203, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_482")
    EventBegin(0x1)

    ChrTalk(    #6
        0x101,
        (
            "#1007F……呼，今天的训练\x01",
            "真是够严苛的。\x02\x03",

            "#1011F收拾完毕以后\x01",
            "可得马上休息才行。\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_482")

    Return()

    # Function_3_405 end

    def Function_4_483(): pass

    label("Function_4_483")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #7
        (
            "\x07\x05　　 游击士协会\x01",
            "【卢·洛克尔训练场】\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_4_483 end

    SaveToFile()

Try(main)
