from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M4308   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M4308.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60221",
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


    DeclEvent(
        X                   = -3000,
        Y                   = -1000,
        Z                   = 156000,
        Range               = 3000,
        Unknown_10          = 0x5DC,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 7,
    )


    ScpFunction(
        "Function_0_CA",           # 00, 0
        "Function_1_EE",           # 01, 1
        "Function_2_F5",           # 02, 2
        "Function_3_8E1",          # 03, 3
        "Function_4_91C",          # 04, 4
        "Function_5_95C",          # 05, 5
        "Function_6_99C",          # 06, 6
        "Function_7_9C8",          # 07, 7
        "Function_8_A57",          # 08, 8
    )


    def Function_0_CA(): pass

    label("Function_0_CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_D8")
    OP_A3(0x2504)
    Event(0, 8)

    label("loc_D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E3, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ED")
    SetMapFlags(0x10000000)
    Event(0, 2)

    label("loc_ED")

    Return()

    # Function_0_CA end

    def Function_1_EE(): pass

    label("Function_1_EE")

    OP_10(0x12, 0x0)
    OP_10(0x15, 0x0)
    Return()

    # Function_1_EE end

    def Function_2_F5(): pass

    label("Function_2_F5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, -3150, 0, 144900, 0)
    SetChrPos(0x10F, -3150, 0, 144900, 0)
    SetChrPos(0xF0, -3150, 0, 144900, 0)
    SetChrPos(0xF1, -3150, 0, 144900, 0)
    OP_9F(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x10F, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xF0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xF1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(-2270, 0, 146900, 0)
    OP_67(0, 7460, -10000, 0)
    OP_6B(3120, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_43(0x109, 0x0, 0x0, 0x3)
    OP_43(0x10F, 0x0, 0x0, 0x4)
    OP_43(0xF0, 0x0, 0x0, 0x5)
    OP_43(0xF1, 0x0, 0x0, 0x6)

    def lambda_1D0():
        OP_6D(-2670, 0, 148880, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1D0)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    WaitChrThread(0x109, 0x2)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_265")
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_28F")

    label("loc_265")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28F")
    Sleep(50)
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_28F")

    Sleep(1000)

    ChrTalk(    #0
        0x109,
        "#1064F#5P哎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x10E,
        "#173F#6P什……！？\x02",
    )

    CloseMessageWindow()

    def lambda_2D5():
        OP_6D(-3110, 300, 155720, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2D5)

    def lambda_2ED():
        OP_67(0, 10740, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2ED)

    def lambda_305():
        OP_6B(3560, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_305)

    def lambda_315():
        OP_6C(45000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_315)

    def lambda_325():
        OP_6E(305, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_325)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x109, 0x2)
    Sleep(1000)
    Fade(500)
    OP_6D(-2340, 0, 149550, 0)
    OP_67(0, 6600, -10000, 0)
    OP_6B(3150, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_62(0x10F, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x10F, 0x109, 400)
    Sleep(300)

    ChrTalk(    #2
        0x10F,
        "#1444F#5P……有什么问题？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4A2")

    ChrTalk(    #3
        0x109,
        "#1841F#5P这已经不只是问题了…… \x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_457")

    ChrTalk(    #4
        0x102,
        (
            "#1503F#6P这是……\x01",
            "遗迹的结构改变了？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49F")

    label("loc_457")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_49F")

    ChrTalk(    #5
        0x107,
        (
            "#065F#6P那、那个……\x01",
            "遗迹的构造好像改变了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49F")

    Jump("loc_500")

    label("loc_4A2")


    ChrTalk(    #6
        0x109,
        (
            "#1841F#5P这已经不只是问题了……\x02\x03",

            "#1063F这是，\x01",
            "遗迹的结构完全改变了不是吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_500")


    ChrTalk(    #7
        0x10E,
        (
            "#176F#6P啊啊……不会错。\x02\x03",

            "#178F这个地方\x01",
            "应该有路通往\x01",
            "开始的三岔路……\x02\x03",

            "可为什么……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5A9")

    ChrTalk(    #8
        0x10B,
        (
            "#215F#6P好像……\x01",
            "不是错觉呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_60F")

    label("loc_5A9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5E4")

    ChrTalk(    #9
        0x10D,
        (
            "#270F#6P好像……\x01",
            "不是错觉啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_60F")

    label("loc_5E4")


    ChrTalk(    #10
        0x10F,
        (
            "#1802F#5P好像……\x01",
            "不是错觉呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_60F")


    ChrTalk(    #11
        0x109,
        (
            "#1067F#5P………………………………\x02\x03",

            "#1075F……原来如此。\x01",
            "是这么回事啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_730")

    ChrTalk(    #12
        0x102,
        (
            "#1502F#6P嗯嗯……\x01",
            "很有这种可能。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 90, 400)
    OP_8C(0x109, 180, 400)
    Sleep(300)

    ChrTalk(    #13
        0x109,
        (
            "#1840F#5P哦……\x01",
            "约修亚也发觉了吗。\x02\x03",

            "那或许就能确定了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10E,
        (
            "#173F#6P你们俩……\x01",
            "发现了什么？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_81D")

    label("loc_730")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_764")

    ChrTalk(    #15
        0x107,
        "#064F#6P凯、凯文哥哥？\x02",
    )

    CloseMessageWindow()
    Jump("loc_7DA")

    label("loc_764")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7AF")

    ChrTalk(    #16
        0x10B,
        (
            "#212F#6P怎、怎么啦。\x01",
            "一个人想明白了什么似的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7DA")

    label("loc_7AF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7DA")

    ChrTalk(    #17
        0x10D,
        "#273F#6P唔……？\x02",
    )

    CloseMessageWindow()

    label("loc_7DA")


    ChrTalk(    #18
        0x10E,
        (
            "#173F#6P凯文神父……\x01",
            "你发现了什么？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 90, 400)
    OP_8C(0x109, 180, 400)
    Sleep(300)

    label("loc_81D")


    ChrTalk(    #19
        0x109,
        (
            "#1060F#5P不……\x01",
            "总之先用这个下去吧。\x02\x03",

            "前面应该就有\x01",
            "答案等着我们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x10E,
        "#178F#6P是吗……我知道了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x10F,
        (
            "#1446F#5P……看来有必要\x01",
            "做好心理准备呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x271E)
    OP_28(0x2E, 0x1, 0x4)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_2_F5 end

    def Function_3_8E1(): pass

    label("Function_3_8E1")


    def lambda_8E7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8E7)
    OP_8E(0xFE, 0xFFFFF2E0, 0x0, 0x23A50, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF074, 0x0, 0x24810, 0x7D0, 0x0)
    Return()

    # Function_3_8E1 end

    def Function_4_91C(): pass

    label("Function_4_91C")

    Sleep(600)

    def lambda_927():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_927)
    OP_8E(0xFE, 0xFFFFF3D0, 0x0, 0x23BF4, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF628, 0x0, 0x24720, 0x7D0, 0x0)
    Return()

    # Function_4_91C end

    def Function_5_95C(): pass

    label("Function_5_95C")

    Sleep(1100)

    def lambda_967():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_967)
    OP_8E(0xFE, 0xFFFFF0EC, 0x0, 0x23ECE, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFEFF2, 0x0, 0x241EE, 0x7D0, 0x0)
    Return()

    # Function_5_95C end

    def Function_6_99C(): pass

    label("Function_6_99C")

    Sleep(1700)

    def lambda_9A7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9A7)
    OP_8E(0xFE, 0xFFFFF542, 0x0, 0x240F4, 0x7D0, 0x0)
    Return()

    # Function_6_99C end

    def Function_7_9C8(): pass

    label("Function_7_9C8")

    EventBegin(0x0)
    Fade(1000)
    OP_89(0x0, -2200, 20000, 156800, 0)
    OP_89(0x1, -3800, 20000, 156800, 0)
    OP_89(0x2, -3800, 20000, 155200, 0)
    OP_89(0x3, -2200, 20000, 155200, 0)
    OP_6D(-3000, 0, 156000, 1500)
    Sleep(100)
    OP_B0(0x0, 0x5A)
    SetMapFlags(0x100000)
    OP_22(0xEB, 0x0, 0x64)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x1F4)
    Sleep(2000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/M4302   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_9C8 end

    def Function_8_A57(): pass

    label("Function_8_A57")

    EventBegin(0x0)
    SetPlaceName(0xE0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0xE0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6F(0x0, 300)
    OP_70(0x0, 0x0)
    OP_48()
    OP_89(0x0, -3800, 0, 155200, 180)
    OP_89(0x1, -2200, 0, 155200, 180)
    OP_89(0x2, -2200, 0, 156800, 180)
    OP_89(0x3, -3800, 0, 156800, 180)
    OP_6D(-3000, 0, 156000, 0)
    OP_73(0x0)
    Sleep(100)
    Fade(1000)
    OP_89(0x0, -3030, 0, 152600, 180)
    OP_89(0x1, -3030, 0, 152600, 180)
    OP_89(0x2, -3030, 0, 152600, 180)
    OP_89(0x3, -3030, 0, 152600, 180)
    EventEnd(0x0)
    Return()

    # Function_8_A57 end

    SaveToFile()

Try(main)
