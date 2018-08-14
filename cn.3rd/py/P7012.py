from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'P7012   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'P7012.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60174",
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


    AddCharChip(
        'ED6_DT26/CH20373 ._CH',             # 00
    )

    AddCharChipPat(
        'ED6_DT26/CH20373P._CP',             # 00
    )

    ScpFunction(
        "Function_0_B2",           # 00, 0
        "Function_1_DC",           # 01, 1
        "Function_2_DD",           # 02, 2
        "Function_3_699",          # 03, 3
        "Function_4_1E9D",         # 04, 4
    )


    def Function_0_B2(): pass

    label("Function_0_B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_C8")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    Event(0, 3)
    Jump("loc_DB")

    label("loc_C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_DB")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 2)

    label("loc_DB")

    Return()

    # Function_0_B2 end

    def Function_1_DC(): pass

    label("Function_1_DC")

    Return()

    # Function_1_DC end

    def Function_2_DD(): pass

    label("Function_2_DD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, 480, -140, -4930, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13E")
    SetChrPos(0xEF, -470, 280, -5370, 90)
    SetChrPos(0xF0, -1820, 900, -5500, 90)
    SetChrPos(0xF1, -1960, 840, -4500, 90)
    Jump("loc_1C3")

    label("loc_13E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_182")
    SetChrPos(0xF0, -470, 280, -5370, 90)
    SetChrPos(0xEF, -1820, 900, -5500, 90)
    SetChrPos(0xF1, -1960, 840, -4500, 90)
    Jump("loc_1C3")

    label("loc_182")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C3")
    SetChrPos(0xF1, -470, 280, -5370, 90)
    SetChrPos(0xEF, -1820, 900, -5500, 90)
    SetChrPos(0xF0, -1960, 840, -4500, 90)

    label("loc_1C3")

    OP_43(0xEE, 0x0, 0x0, 0x4)
    OP_43(0xEF, 0x0, 0x0, 0x4)
    OP_43(0xF0, 0x0, 0x0, 0x4)
    OP_43(0xF1, 0x0, 0x0, 0x4)
    OP_6D(-300, 830, -4800, 0)
    OP_67(0, 7940, -10000, 0)
    OP_6B(2560, 0)
    OP_6C(327000, 0)
    OP_6E(448, 0)
    StopSound(0x2710, 0xF618, 0x1F40)

    def lambda_22F():
        OP_6B(1970, 8000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_22F)

    def lambda_23F():
        OP_67(0, 3180, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_23F)
    FadeToBright(3000, 0)
    OP_0D()
    WaitChrThread(0x109, 0x3)
    WaitChrThread(0x10F, 0x3)

    ChrTalk(    #0
        0x109,
        (
            "#1067F#100P#6P……那一天。\x02\x03",

            "我想你应该记得，\x01",
            "那是我和露菲娜姐姐\x01",
            "预定要回乡的日子。\x02\x03",

            "因为我们都有各自的任务，\x01",
            "就打算先在城里汇合\x01",
            "然后一起回来。\x02\x03",

            "#1065F……但是姐姐\x01",
            "乘坐的列车晚点了……\x02\x03",

            "我先到了之后，\x01",
            "消息传了过来……\x02",
        )
    )

    CloseMessageWindow()
    OP_AD(0x24016B, 0x0, 0x0, 0x12C)
    Sleep(2000)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("凯文")

    AnonymousTalk(    #1
        (
            "\x07\x0C#40W你和孩子们有危险……\x01",
            "我一想到这里，\x01",
            "就决定单独行动清除占领的猎兵。\x02\x03",

            "说实话，他们的水平没什么了不起的。\x02\x03",

            "就算我只是随从骑士，\x01",
            "也轻松打倒了一连串的猎兵，\x01",
            "解放了孩子们和老师……\x02\x03",

            "但是，我没找到你。\x07\x00\x02",
        )
    )

    Jump("loc_476")

    label("loc_476")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_AE(0x12C)
    Sleep(2000)

    ChrTalk(    #2
        0x109,
        (
            "#1065F#100P#6P听孩子们说，\x01",
            "猎兵中的一个人\x01",
            "带着昏迷的你不知道去了哪里……\x02\x03",

            "我处理好伤势后就开始寻找，\x01",
            "总算找到了这个地方……\x02\x03",

            "#1840F……我说，莉丝……\x02\x03",

            "你醒来的时候，\x01",
            "没戴着丝带对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x10F,
        (
            "#1802F#100P#5P嗯、嗯……\x02\x03",

            "但是，为什么……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x109,
        (
            "#1075F#100P#6P你的丝带，\x01",
            "掉落在那扇暗门前了。\x02\x03",

            "而且还有很新的足迹，\x01",
            "所以被我发现了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x10F,
        "#1444F#100P#5P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x109,
        (
            "#1067F#100P#6P然后……\x02\x03",

            "我追着带走你的猎兵\x01",
            "下到这个地方……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1500)
    OP_A2(0x2505)
    NewScene("ED6_DT21/P7012   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_DD end

    def Function_3_699(): pass

    label("Function_3_699")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    StopSound(0x80E8, 0xF618, 0x0)
    OP_72(0x402, 0x0)
    ExitThread()
    OP_72(0x1003, 0x0)
    ExitThread()
    OP_72(0x803, 0x0)
    ExitThread()
    OP_72(0x2003, 0x0)
    ExitThread()
    OP_6F(0x3, 0)
    OP_71(0x404, 0x0)
    ExitThread()
    SetChrPos(0x109, 79760, 0, -8450, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_72C")
    SetChrPos(0xEF, 79840, 0, -10580, 0)
    SetChrPos(0xF0, 80570, 0, -12380, 0)
    SetChrPos(0xF1, 79500, 0, -12590, 0)
    Jump("loc_7B1")

    label("loc_72C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_770")
    SetChrPos(0xF0, 79840, 0, -10580, 0)
    SetChrPos(0xEF, 80570, 0, -12380, 0)
    SetChrPos(0xF1, 79500, 0, -12590, 0)
    Jump("loc_7B1")

    label("loc_770")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B1")
    SetChrPos(0xF1, 79840, 0, -10580, 0)
    SetChrPos(0xEF, 80570, 0, -12380, 0)
    SetChrPos(0xF0, 79500, 0, -12590, 0)

    label("loc_7B1")

    OP_6D(78260, 1050, -16040, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(325, 0)

    def lambda_7F4():
        OP_8F(0xFE, 0x13920, 0x0, 0x4B1E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7F4)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_87A")

    def lambda_822():
        OP_8F(0xFE, 0x1397A, 0x0, 0x43A8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_822)
    Sleep(50)

    def lambda_842():
        OP_8F(0xFE, 0x13CFE, 0x0, 0x3C82, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_842)
    Sleep(50)

    def lambda_862():
        OP_8F(0xFE, 0x13740, 0x0, 0x3CB4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_862)
    Jump("loc_94F")

    label("loc_87A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E6")

    def lambda_88E():
        OP_8F(0xFE, 0x1397A, 0x0, 0x43A8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_88E)
    Sleep(50)

    def lambda_8AE():
        OP_8F(0xFE, 0x13CFE, 0x0, 0x3D4A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_8AE)
    Sleep(50)

    def lambda_8CE():
        OP_8F(0xFE, 0x13740, 0x0, 0x3D7C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_8CE)
    Jump("loc_94F")

    label("loc_8E6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_94F")

    def lambda_8FA():
        OP_8F(0xFE, 0x1397A, 0x0, 0x43A8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_8FA)
    Sleep(50)

    def lambda_91A():
        OP_8F(0xFE, 0x13CFE, 0x0, 0x3D4A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_91A)
    Sleep(50)

    def lambda_93A():
        OP_8F(0xFE, 0x13740, 0x0, 0x3D7C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_93A)

    label("loc_94F")

    Sleep(1500)

    def lambda_95A():
        OP_6D(78260, 1050, 20160, 11000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_95A)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    WaitChrThread(0xEE, 0x1)
    Fade(500)
    OP_6D(78430, 0, 19800, 0)
    OP_67(0, 4800, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(297, 0)
    OP_0D()
    Sleep(300)
    OP_8C(0x109, 180, 400)
    Sleep(300)

    ChrTalk(    #7
        0x109,
        (
            "#1065F#11P对了，莉丝。\x02\x03",

            "#1063F你还记得……\x01",
            "第一次见面时\x01",
            "我是什么样子吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x10F,
        (
            "#1445F#6P……嗯。\x02\x03",

            "#1446F虽然我那时还小……\x01",
            "不过很不可思议，当时的事情我还记得。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_AD(0x24016A, 0x0, 0x0, 0x12C)
    Sleep(2000)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("莉丝")

    AnonymousTalk(    #9
        (
            "\x07\x0C#40W那时的凯文……\x01",
            "眼神里充满了完全的绝望……\x02\x03",

            "说实话……\x01",
            "我觉得有点害怕。\x02\x03",

            "我在想，这个孩子\x01",
            "究竟看到了什么…… \x02",
        )
    )

    Jump("loc_B59")

    label("loc_B59")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_AE(0x12C)
    Sleep(1500)

    ChrTalk(    #10
        0x109,
        "#1840F#11P哈哈……看到了什么吗。\x02",
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x109)
    Sleep(500)

    ChrTalk(    #11
        0x109,
        (
            "#1067F#11P当初姐姐似乎\x01",
            "是知道的……\x02\x03",

            "#1840F当时，\x01",
            "我杀了自己的亲生母亲。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C3F")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_CA6")

    label("loc_C3F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C67")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_CA6")

    label("loc_C67")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C8F")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_CA6")

    label("loc_C8F")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_CA6")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CD3")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_D3A")

    label("loc_CD3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CFB")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_D3A")

    label("loc_CFB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D23")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_D3A")

    label("loc_D23")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_D3A")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D67")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_DCE")

    label("loc_D67")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D8F")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_DCE")

    label("loc_D8F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DB7")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_DCE")

    label("loc_DB7")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_DCE")

    Sleep(1000)

    ChrTalk(    #12
        0x10F,
        "#1444F#6P……啊……！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E2C")

    ChrTalk(    #13
        0x104,
        "#1543F#6P……什么………\x02",
    )

    CloseMessageWindow()
    Jump("loc_1070")

    label("loc_E2C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E61")

    ChrTalk(    #14
        0x102,
        "#1504F#6P……什么………\x02",
    )

    CloseMessageWindow()
    Jump("loc_1070")

    label("loc_E61")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E95")

    ChrTalk(    #15
        0x10B,
        "#216F#6P……什么………\x02",
    )

    CloseMessageWindow()
    Jump("loc_1070")

    label("loc_E95")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EC3")

    ChrTalk(    #16
        0x106,
        "#055F#6P什么！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1070")

    label("loc_EC3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EF5")

    ChrTalk(    #17
        0x10E,
        "#178F#6P什么……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1070")

    label("loc_EF5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F26")

    ChrTalk(    #18
        0x103,
        "#1523F#6P啊……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1070")

    label("loc_F26")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F57")

    ChrTalk(    #19
        0x101,
        "#1004F#6P啊……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1070")

    label("loc_F57")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F88")

    ChrTalk(    #20
        0x105,
        "#1163F#6P啊……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1070")

    label("loc_F88")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FBA")

    ChrTalk(    #21
        0x110,
        "#264F#6P……啊………\x02",
    )

    CloseMessageWindow()
    Jump("loc_1070")

    label("loc_FBA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FED")

    ChrTalk(    #22
        0x10A,
        "#1317F#6P……啊………\x02",
    )

    CloseMessageWindow()
    Jump("loc_1070")

    label("loc_FED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1017")

    ChrTalk(    #23
        0x10D,
        "#270F#6P！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1070")

    label("loc_1017")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1041")

    ChrTalk(    #24
        0x108,
        "#072F#6P！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1070")

    label("loc_1041")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1070")

    ChrTalk(    #25
        0x107,
        "#065F#6P…………哎。\x02",
    )

    CloseMessageWindow()

    label("loc_1070")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_109A")

    ChrTalk(    #26
        0x10C,
        "#113F#6P！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1294")

    label("loc_109A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10C4")

    ChrTalk(    #27
        0x107,
        "#065F#6P！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1294")

    label("loc_10C4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10EE")

    ChrTalk(    #28
        0x108,
        "#072F#6P！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1294")

    label("loc_10EE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1118")

    ChrTalk(    #29
        0x10D,
        "#270F#6P！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1294")

    label("loc_1118")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1143")

    ChrTalk(    #30
        0x10A,
        "#1317F#6P！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1294")

    label("loc_1143")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_116D")

    ChrTalk(    #31
        0x110,
        "#264F#6P！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1294")

    label("loc_116D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1198")

    ChrTalk(    #32
        0x105,
        "#1163F#6P！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1294")

    label("loc_1198")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11C3")

    ChrTalk(    #33
        0x101,
        "#1004F#6P！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1294")

    label("loc_11C3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11EE")

    ChrTalk(    #34
        0x103,
        "#1523F#6P！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1294")

    label("loc_11EE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1218")

    ChrTalk(    #35
        0x10E,
        "#178F#6P！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1294")

    label("loc_1218")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1242")

    ChrTalk(    #36
        0x106,
        "#055F#6P！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1294")

    label("loc_1242")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_126C")

    ChrTalk(    #37
        0x10B,
        "#216F#6P！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1294")

    label("loc_126C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1294")

    ChrTalk(    #38
        0x102,
        "#1504F#6P！？\x02",
    )

    CloseMessageWindow()

    label("loc_1294")


    ChrTalk(    #39
        0x109,
        (
            "#1840F#11P啊啊，\x01",
            "说是杀了可能有点夸张吧。\x02\x03",

            "#1075F见死不救……\x01",
            "这么说可能比较正确吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    Sleep(500)
    OP_AD(0x24015D, 0x0, 0x0, 0x64)
    Sleep(3000)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("凯文")

    AnonymousTalk(    #40
        (
            "\x07\x0C#40W我们家\x01",
            "是单亲独子家庭。\x02\x03",

            "爸爸虽然偶尔也会露面，\x01",
            "不过似乎另组了家庭，\x01",
            "成了一个有钱人家。\x02\x03",

            "但是这没有关系，\x01",
            "我还是喜欢妈妈。\x02\x03",

            "虽说这样，我有时也会因此\x01",
            "被附近的小孩欺负，\x01",
            "不过基本上都被我打得落花流水。\x02\x03",

            "喜欢料理，人又温柔……\x01",
            "是令我感到自豪的妈妈。\x02",
        )
    )

    Jump("loc_1454")

    label("loc_1454")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_6D(123020, 0, 12050, 0)
    OP_67(0, 4960, -10000, 0)
    OP_6B(2510, 0)
    OP_6C(315000, 0)
    OP_6E(325, 0)
    OP_AE(0xC8)
    Sleep(2000)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("凯文")

    AnonymousTalk(    #41
        (
            "\x07\x0C#40W但是七岁时……\x01",
            "妈妈被爸爸抛弃了。\x02\x03",

            "她原本心理就脆弱……\x01",
            "渐渐地越来越没精神，\x01",
            "身体也越来越差……\x02\x03",

            "虽然我做了很多努力，\x01",
            "但是都无法让她恢复精神。\x02\x03",

            "然后……在某一个冬日。\x02\x03",

            "妈妈……\x01",
            "勒紧了熟睡中的我的脖子。\x02",
        )
    )

    Jump("loc_15BD")

    label("loc_15BD")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("莉丝")

    AnonymousTalk(    #42
        "\x07\x0C#3S！！！\x02",
    )

    Jump("loc_15F3")

    label("loc_15F3")

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(300)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS461._CH")
    OP_C6(0x0, 0x3, -1, 2000, 0)
    Sleep(2500)
    OP_C6(0x0, 0x3, -5592406, 500, 0)
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 200, -1, -1)
    SetChrName("")

    AnonymousTalk(    #43 op#A
        "\x07\x00#50W#20A………对不起…………\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #44 op#A
        "\x07\x00#50W#25A……对不起……凯文………\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #45 op#A
        (
            "\x07\x00#50W#50A……但是妈妈………\x01",
            "已经……很累了………\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #46 op#A
        (
            "\x07\x00#50W#55A……所以……\x01",
            "…………所以啊……凯文…………\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #47 op#A
        (
            "\x07\x00#50W#60A……就这样………\x01",
            "………和妈妈一起………\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(150)
    OP_C6(0x0, 0x3, 16777215, 1500, 0)
    Sleep(2000)
    OP_C7(0x1, 0xFF, 0x0)
    FadeToBright(0, 0)
    OP_C4(0x1, 0x800)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("凯文")

    AnonymousTalk(    #48
        (
            "\x07\x0C#40W反正就是说，\x01",
            "既然这么痛苦干脆一起解脱算了。\x02\x03",

            "但是我……\x01",
            "没有陪她一起去。\x02\x03",

            "我疯狂地踢开妈妈……\x01",
            "光着脚冲到了下着雪的外面。\x02\x03",

            "我完全不明白妈妈所做事情的意义，\x01",
            "只是在一片混乱中徘徊了差不多一个小时。\x02\x03",

            "然后我肚子饿了……\x01",
            "想起了妈妈……\x02\x03",

            "……心惊胆战地回到家里……\x07\x00\x02",
        )
    )

    Jump("loc_18E7")

    label("loc_18E7")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_AD(0x24015F, 0x0, 0x0, 0x64)
    Sleep(3000)
    Sleep(500)
    FadeToDark(0, 16777215, -1)
    OP_0D()
    OP_AE(0x64)
    Sleep(3000)
    OP_6D(78090, -200, 19770, 0)
    OP_67(0, 4800, -10000, 0)
    OP_6B(2760, 0)
    OP_6C(315000, 0)
    OP_6E(297, 0)
    Sleep(1000)
    FadeToBright(2000, 16777215)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #49
        0x10F,
        "#1960F#6P#60W……凯……文…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x109,
        (
            "#1844F#11P#40W哈哈，抱歉。\x01",
            "说了这些无济于事的话。\x02\x03",

            "#1843F话虽如此……\x01",
            "大概就是那个时候吧。\x02\x03",

            "#1845F……我心中就被\x01",
            "刻入了『圣痕』。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #51
        0x10F,
        "#1809F#6P咦……！？\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_1A81():
        OP_6D(78520, 0, 21620, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_1A81)

    def lambda_1A99():
        OP_67(0, 4840, -10000, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_1A99)

    def lambda_1AB1():
        OP_6B(2600, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_1AB1)

    def lambda_1AC1():
        OP_6E(330, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_1AC1)
    OP_8C(0x109, 0, 400)
    WaitChrThread(0xEE, 0x0)
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x109, 0)
    SetChrSubChip(0x109, 0)
    Sleep(500)
    OP_22(0xD8, 0x0, 0x64)
    SetChrSubChip(0x109, 1)
    Sleep(600)
    LoadEffect(0x0, "map\\mp058_00.eff")
    LoadEffect(0x1, "scraft\\sc008_02.eff")
    LoadEffect(0x2, "map\\mpP90_00.eff")
    LoadEffect(0x3, "map\\mpP90_01.eff")
    LoadEffect(0x4, "map\\mpP90_04.eff")
    PlayEffect(0x1, 0xFF, 0xFF, 80170, 1000, 19900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_23(0xC9)
    OP_82(0x0, 0x2)
    Sleep(2000)
    Fade(1000)
    OP_22(0xD7, 0x0, 0x64)
    OP_22(0x146, 0x64, 0x1)
    PlayEffect(0x2, 0x0, 0xFF, 80130, 0, 21750, 0, 0, 0, 1800, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x1, 0xFF, 80130, 0, 21750, 0, 0, 0, 1800, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x2, 0xFF, 80130, 0, 21750, 0, 0, 0, 1800, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(1000)
    Fade(1000)
    OP_22(0x117, 0x0, 0x64)
    OP_71(0x402, 0x0)
    ExitThread()
    OP_72(0x404, 0x0)
    ExitThread()
    OP_23(0x146)
    OP_82(0x0, 0x0)
    OP_82(0x1, 0x0)
    OP_82(0x2, 0x0)
    OP_0D()
    SetChrSubChip(0x109, 0)
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(500)

    def lambda_1C9D():
        OP_6D(77520, 0, 23520, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_1C9D)

    def lambda_1CB5():
        OP_8F(0xFE, 0x138BC, 0x0, 0x535C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1CB5)
    WaitChrThread(0x109, 0x0)
    Sleep(500)
    OP_22(0x70, 0x0, 0x64)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x10E)
    OP_73(0x3)
    SetChrFlags(0x0, 0x4)
    SetChrFlags(0x1, 0x4)
    SetChrFlags(0x2, 0x4)
    SetChrFlags(0x3, 0x4)

    def lambda_1D04():
        OP_8F(0xFE, 0x13902, 0x0, 0x6770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1D04)
    Sleep(500)

    def lambda_1D24():
        OP_6D(77520, 0, 25000, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_1D24)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DA2")

    def lambda_1D4A():
        OP_8F(0xFE, 0x13902, 0x0, 0x6770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_1D4A)
    Sleep(300)

    def lambda_1D6A():
        OP_8F(0xFE, 0x13B00, 0x0, 0x6766, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_1D6A)
    Sleep(600)

    def lambda_1D8A():
        OP_8F(0xFE, 0x13740, 0x0, 0x6748, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_1D8A)
    Jump("loc_1E77")

    label("loc_1DA2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E0E")

    def lambda_1DB6():
        OP_8F(0xFE, 0x13902, 0x0, 0x6770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_1DB6)
    Sleep(300)

    def lambda_1DD6():
        OP_8F(0xFE, 0x13B00, 0x0, 0x6766, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_1DD6)
    Sleep(600)

    def lambda_1DF6():
        OP_8F(0xFE, 0x13740, 0x0, 0x6748, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_1DF6)
    Jump("loc_1E77")

    label("loc_1E0E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E77")

    def lambda_1E22():
        OP_8F(0xFE, 0x13902, 0x0, 0x6770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_1E22)
    Sleep(300)

    def lambda_1E42():
        OP_8F(0xFE, 0x13B00, 0x0, 0x6766, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_1E42)
    Sleep(600)

    def lambda_1E62():
        OP_8F(0xFE, 0x13740, 0x0, 0x6748, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_1E62)

    label("loc_1E77")

    Sleep(3000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0xEE, 0x1)
    SetMapFlags(0x2000000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/P7013   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_699 end

    def Function_4_1E9D(): pass

    label("Function_4_1E9D")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EC2")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_2004")

    label("loc_1EC2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EDB")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_2004")

    label("loc_1EDB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EF4")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_2004")

    label("loc_1EF4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F0D")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_2004")

    label("loc_1F0D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F26")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_2004")

    label("loc_1F26")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F3F")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_2004")

    label("loc_1F3F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F58")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_2004")

    label("loc_1F58")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F71")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_2004")

    label("loc_1F71")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F8A")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_2004")

    label("loc_1F8A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FA3")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_2004")

    label("loc_1FA3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FBC")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_2004")

    label("loc_1FBC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FD5")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_2004")

    label("loc_1FD5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FEE")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_2004")

    label("loc_1FEE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2004")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_2004")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2019")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_2004")

    label("loc_2019")

    Return()

    # Function_4_1E9D end

    SaveToFile()

Try(main)
