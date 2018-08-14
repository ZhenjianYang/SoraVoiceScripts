from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'P7010   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'P7010.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60211",
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


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_C7",           # 01, 1
        "Function_2_CE",           # 02, 2
        "Function_3_120F",         # 03, 3
        "Function_4_1272",         # 04, 4
        "Function_5_12D2",         # 05, 5
        "Function_6_1332",         # 06, 6
        "Function_7_1392",         # 07, 7
        "Function_8_13B1",         # 08, 8
        "Function_9_13FC",         # 09, 9
        "Function_10_1447",        # 0A, 10
        "Function_11_148B",        # 0B, 11
        "Function_12_14CF",        # 0C, 12
        "Function_13_14F6",        # 0D, 13
        "Function_14_151D",        # 0E, 14
        "Function_15_1544",        # 0F, 15
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_C6")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xAE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)

    label("loc_C6")

    Return()

    # Function_0_AA end

    def Function_1_C7(): pass

    label("Function_1_C7")

    OP_72(0x1001, 0x0)
    ExitThread()
    Return()

    # Function_1_C7 end

    def Function_2_CE(): pass

    label("Function_2_CE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, 1010, -300, -2200, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12F")
    SetChrPos(0xEF, -240, -300, -2200, 0)
    SetChrPos(0xF0, 1010, -300, -2200, 0)
    SetChrPos(0xF1, -240, -300, -2200, 0)
    Jump("loc_1B4")

    label("loc_12F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_173")
    SetChrPos(0xF0, -240, -300, -2200, 0)
    SetChrPos(0xEF, 1010, -300, -2200, 0)
    SetChrPos(0xF1, -240, -300, -2200, 0)
    Jump("loc_1B4")

    label("loc_173")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B4")
    SetChrPos(0xF1, -240, -300, -2200, 0)
    SetChrPos(0xEF, 1010, -300, -2200, 0)
    SetChrPos(0xF0, -240, -300, -2200, 0)

    label("loc_1B4")

    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(-790, 4300, 20090, 0)
    OP_67(0, 3640, -10000, 0)
    OP_6B(2520, 0)
    OP_6C(338000, 0)
    OP_6E(346, 0)
    FadeToBright(2000, 0)
    OP_0D()

    def lambda_22D():
        OP_6D(1360, 4300, 1740, 7500)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_22D)

    def lambda_245():
        OP_67(0, 5800, -10000, 7500)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_245)

    def lambda_25D():
        OP_6B(2520, 7500)
        ExitThread()

    QueueWorkItem(0xEF, 2, lambda_25D)

    def lambda_26D():
        OP_6C(326000, 7500)
        ExitThread()

    QueueWorkItem(0xF0, 2, lambda_26D)

    def lambda_27D():
        OP_6E(346, 7500)
        ExitThread()

    QueueWorkItem(0xF1, 2, lambda_27D)
    Sleep(4500)
    OP_22(0x177, 0x0, 0x64)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D2")
    OP_43(0xEF, 0x0, 0x0, 0xD)
    Sleep(600)
    OP_43(0x109, 0x0, 0x0, 0xC)
    Sleep(700)
    OP_43(0xF0, 0x0, 0x0, 0xE)
    Sleep(200)
    OP_43(0xF1, 0x0, 0x0, 0xF)
    Jump("loc_347")

    label("loc_2D2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30E")
    OP_43(0xF0, 0x0, 0x0, 0xD)
    Sleep(600)
    OP_43(0x109, 0x0, 0x0, 0xC)
    Sleep(700)
    OP_43(0xEF, 0x0, 0x0, 0xE)
    Sleep(200)
    OP_43(0xF1, 0x0, 0x0, 0xF)
    Jump("loc_347")

    label("loc_30E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_347")
    OP_43(0xF1, 0x0, 0x0, 0xD)
    Sleep(600)
    OP_43(0x109, 0x0, 0x0, 0xC)
    Sleep(700)
    OP_43(0xEF, 0x0, 0x0, 0xE)
    Sleep(200)
    OP_43(0xF0, 0x0, 0x0, 0xF)

    label("loc_347")

    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    WaitChrThread(0xEE, 0x2)
    Fade(500)
    OP_6D(-800, 0, 4500, 0)
    OP_67(0, 6040, -10000, 0)
    OP_6B(2450, 0)
    OP_6C(315000, 0)
    OP_6E(303, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #0
        0x10F,
        "#1802F#5P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x109,
        (
            "#1065F#6P五年前……\x01",
            "不知道什么人雇佣的猎兵团\x01",
            "占领了这个『紫苑之家』。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 270, 400)
    Sleep(300)

    ChrTalk(    #2
        0x109,
        (
            "#1840F#12P莉丝。\x02\x03",

            "那时的事，\x01",
            "你还记得多少？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10F, 90, 400)
    Sleep(300)

    ChrTalk(    #3
        0x10F,
        (
            "#1802F#5P我、我……\x02\x03",

            "#1445F……那时一群黑衣人\x01",
            "突然破门而入……\x02\x03",

            "把大家都绑了起来……\x01",
            "老师被带去了二楼……\x02\x03",

            "然后……\x02",
        )
    )

    Jump("loc_51F")

    label("loc_51F")

    CloseMessageWindow()

    ChrTalk(    #4
        0x109,
        (
            "#1065F#12P……等你醒来的时候，\x01",
            "已经在城里医院的病床上了。\x02\x03",

            "#1067F然后就听说了\x01",
            "我和露菲娜姐姐前来相助……\x02\x03",

            "以及姐姐\x01",
            "殉职的事情。\x02\x03",

            "#1840F……是这样吧？\x02",
        )
    )

    Jump("loc_5E2")

    label("loc_5E2")

    CloseMessageWindow()

    ChrTalk(    #5
        0x10F,
        (
            "#1446F#5P…………嗯。\x02\x03",

            "#1802F喂，凯文……\x01",
            "那件事到底是怎么回事？\x02\x03",

            "听说是和教会敌对的\x01",
            "某些势力所为……\x02\x03",

            "#1445F从那以后\x01",
            "我就再也没见过凯文……\x02\x03",

            "就算问瑟尔纳特教官，\x01",
            "她也完全不告诉我……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x109,
        (
            "#1075F#12P嗯，站在总长的立场上\x01",
            "也确实无法轻易地说出来吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 0, 400)
    Sleep(300)

    ChrTalk(    #7
        0x109,
        (
            "#1067F#6P……这个设施，\x01",
            "其实是为被指定要进行封印的\x01",
            "『古代遗物』所做的障眼法啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x10F,
        "#1802F#5P………………………………\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #9
        0x10F,
        "#1444F#5P#4S咦。\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_7D8():
        OP_6D(-700, 0, 11410, 4000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_7D8)
    OP_43(0x109, 0x0, 0x0, 0x8)

    def lambda_7F7():

        label("loc_7F7")

        TurnDirection(0xFE, 0x109, 400)
        OP_48()
        Jump("loc_7F7")

    QueueWorkItem2(0xEF, 0, lambda_7F7)

    def lambda_808():

        label("loc_808")

        TurnDirection(0xFE, 0x109, 400)
        OP_48()
        Jump("loc_808")

    QueueWorkItem2(0xF0, 0, lambda_808)

    def lambda_819():

        label("loc_819")

        TurnDirection(0xFE, 0x109, 400)
        OP_48()
        Jump("loc_819")

    QueueWorkItem2(0xF1, 0, lambda_819)
    Sleep(2000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_859")
    OP_43(0xEF, 0x0, 0x0, 0x9)
    Sleep(300)
    OP_43(0xF0, 0x0, 0x0, 0xA)
    Sleep(700)
    OP_43(0xF1, 0x0, 0x0, 0xB)
    Jump("loc_8B6")

    label("loc_859")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_889")
    OP_43(0xF0, 0x0, 0x0, 0x9)
    Sleep(300)
    OP_43(0xEF, 0x0, 0x0, 0xA)
    Sleep(700)
    OP_43(0xF1, 0x0, 0x0, 0xB)
    Jump("loc_8B6")

    label("loc_889")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B6")
    OP_43(0xF1, 0x0, 0x0, 0x9)
    Sleep(300)
    OP_43(0xEF, 0x0, 0x0, 0xA)
    Sleep(700)
    OP_43(0xF0, 0x0, 0x0, 0xB)

    label("loc_8B6")

    WaitChrThread(0xEE, 0x1)

    def lambda_8C1():
        OP_6D(-5400, 0, 14960, 4000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_8C1)

    def lambda_8D9():
        OP_67(0, 5610, -10000, 4000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_8D9)

    def lambda_8F1():
        OP_6B(2450, 4000)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_8F1)

    def lambda_901():
        OP_6E(322, 4000)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_901)
    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    WaitChrThread(0xEE, 0x1)
    Sleep(300)

    ChrTalk(    #10
        0x109,
        "#1063F#5P……这里。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0x64, 0x0, 0x64)
    Sleep(1000)
    OP_43(0x109, 0x0, 0x0, 0x7)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_98C")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_9F3")

    label("loc_98C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9B4")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_9F3")

    label("loc_9B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9DC")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_9F3")

    label("loc_9DC")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_9F3")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A20")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_A87")

    label("loc_A20")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A48")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_A87")

    label("loc_A48")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A70")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_A87")

    label("loc_A70")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_A87")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AB4")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B1B")

    label("loc_AB4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ADC")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B1B")

    label("loc_ADC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B04")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B1B")

    label("loc_B04")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_B1B")

    Sleep(1500)

    ChrTalk(    #11
        0x10F,
        "#1802F#6P！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B6C")

    ChrTalk(    #12
        0x10D,
        "#270F#6P是秘门……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_E1D")

    label("loc_B6C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B9E")

    ChrTalk(    #13
        0x10C,
        "#112F#6P是秘门……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_E1D")

    label("loc_B9E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BD1")

    ChrTalk(    #14
        0x104,
        "#1542F#6P是秘门……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_E1D")

    label("loc_BD1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C03")

    ChrTalk(    #15
        0x10E,
        "#172F#6P是秘门……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_E1D")

    label("loc_C03")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C35")

    ChrTalk(    #16
        0x108,
        "#072F#6P是秘门……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_E1D")

    label("loc_C35")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C67")

    ChrTalk(    #17
        0x106,
        "#057F#6P是秘门……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_E1D")

    label("loc_C67")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C98")

    ChrTalk(    #18
        0x103,
        "#1522F#6P秘门……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_E1D")

    label("loc_C98")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CCD")

    ChrTalk(    #19
        0x105,
        "#1163F#6P秘、秘门……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_E1D")

    label("loc_CCD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D03")

    ChrTalk(    #20
        0x10A,
        "#812F#6P秘、秘门……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_E1D")

    label("loc_D03")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D3D")

    ChrTalk(    #21
        0x107,
        "#065F#6P隐、隐藏的门……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_E1D")

    label("loc_D3D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D7A")

    ChrTalk(    #22
        0x110,
        "#1305F#6P原来如此……是秘门啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_E1D")

    label("loc_D7A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DB4")

    ChrTalk(    #23
        0x10B,
        "#216F#6P隐、隐藏的门……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_E1D")

    label("loc_DB4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DE9")

    ChrTalk(    #24
        0x102,
        "#1502F#6P是秘门吗……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_E1D")

    label("loc_DE9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E1D")

    ChrTalk(    #25
        0x101,
        "#1020F#6P秘、秘门……！？\x02",
    )

    CloseMessageWindow()

    label("loc_E1D")

    WaitChrThread(0x109, 0x0)
    Sleep(300)

    def lambda_E2D():
        OP_6D(-6400, 0, 14960, 2000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_E2D)

    def lambda_E45():
        OP_8E(0xFE, 0xFFFFE2B4, 0x0, 0x3732, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_E45)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x109, 0x0)
    OP_44(0xEE, 0x1)
    OP_E0(239, 0x40, 0x1)
    OP_E0(240, 0x41, 0x1)
    OP_E0(241, 0x42, 0x1)
    SetChrPos(0x109, -35730, 0, 8770, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ED6")
    SetChrPos(0xEF, -35730, 0, 8770, 270)
    SetChrPos(0xF0, -35730, 0, 8770, 270)
    SetChrPos(0xF1, -35730, 0, 8770, 270)
    Jump("loc_F5B")

    label("loc_ED6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F1A")
    SetChrPos(0xF0, -35730, 0, 8770, 270)
    SetChrPos(0xEF, -35730, 0, 8770, 270)
    SetChrPos(0xF1, -35730, 0, 8770, 270)
    Jump("loc_F5B")

    label("loc_F1A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F5B")
    SetChrPos(0xF1, -35730, 0, 8770, 270)
    SetChrPos(0xEF, -35730, 0, 8770, 270)
    SetChrPos(0xF0, -35730, 0, 8770, 270)

    label("loc_F5B")

    SetChrChipByIndex(0xEF, 0)
    SetChrChipByIndex(0xF0, 1)
    SetChrChipByIndex(0xF1, 2)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(-42080, 1500, 11170, 0)
    OP_67(0, 6300, -10000, 0)
    OP_6B(2820, 0)
    OP_6C(315000, 0)
    OP_6E(295, 0)

    def lambda_FD9():
        OP_6D(-42080, -1500, 11170, 4000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_FD9)
    FadeToBright(1000, 0)
    OP_0D()
    OP_43(0x109, 0x0, 0x0, 0x3)
    Sleep(3000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1031")
    OP_43(0xEF, 0x0, 0x0, 0x4)
    Sleep(700)
    OP_43(0xF0, 0x0, 0x0, 0x5)
    Sleep(800)
    OP_43(0xF1, 0x0, 0x0, 0x6)
    Jump("loc_108E")

    label("loc_1031")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1061")
    OP_43(0xF0, 0x0, 0x0, 0x4)
    Sleep(700)
    OP_43(0xEF, 0x0, 0x0, 0x5)
    Sleep(800)
    OP_43(0xF1, 0x0, 0x0, 0x6)
    Jump("loc_108E")

    label("loc_1061")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_108E")
    OP_43(0xF1, 0x0, 0x0, 0x4)
    Sleep(700)
    OP_43(0xEF, 0x0, 0x0, 0x5)
    Sleep(800)
    OP_43(0xF0, 0x0, 0x0, 0x6)

    label("loc_108E")

    WaitChrThread(0x10F, 0x0)

    ChrTalk(    #26
        0x10F,
        (
            "#1449F#11P等、等一下，凯文……！\x02\x03",

            "被指定要封印的古代遗物……\x01",
            "……难道就在这下面……！？\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xEE, 0x3)
    Sleep(300)

    ChrTalk(    #27
        0x109,
        "#1840F#5P……没错。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x109, 0, 400)
    Sleep(300)

    ChrTalk(    #28
        0x109,
        (
            "#1065F#6P这下面有着\x01",
            "和格兰赛尔大圣堂地下\x01",
            "同样的场所……\x02\x03",

            "#1063F对古代遗物进行封印的设施——\x01",
            "『始源之地』。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #29
        0x10F,
        "#1802F#11P#3S！！！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(300)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(2000)
    SetMapFlags(0x2000000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/P7012   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_CE end

    def Function_3_120F(): pass

    label("Function_3_120F")


    def lambda_1215():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1215)
    OP_8E(0xFE, 0xFFFF6C26, 0x0, 0x229C, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF6C08, 0x0, 0x2A80, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF5E20, 0xFFFFFC18, 0x2A58, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF5CAE, 0xFFFFF830, 0x1B80, 0x7D0, 0x0)
    Return()

    # Function_3_120F end

    def Function_4_1272(): pass

    label("Function_4_1272")


    def lambda_1278():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1278)
    OP_8E(0xFE, 0xFFFF6C26, 0x0, 0x229C, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFF6C08, 0x0, 0x2A80, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFF5E20, 0xFFFFFC18, 0x2A58, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 65535)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 180, 600)
    Return()

    # Function_4_1272 end

    def Function_5_12D2(): pass

    label("Function_5_12D2")


    def lambda_12D8():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_12D8)
    OP_8E(0xFE, 0xFFFF6C26, 0x0, 0x229C, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFF6C08, 0x0, 0x2A80, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFF6334, 0xFFFFFDC6, 0x2A6C, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 65535)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 180, 600)
    Return()

    # Function_5_12D2 end

    def Function_6_1332(): pass

    label("Function_6_1332")


    def lambda_1338():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1338)
    OP_8E(0xFE, 0xFFFF6C26, 0x0, 0x229C, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFF6C08, 0x0, 0x2A80, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFF69CE, 0x0, 0x29FE, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 65535)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 180, 600)
    Return()

    # Function_6_1332 end

    def Function_7_1392(): pass

    label("Function_7_1392")

    OP_22(0x6C, 0x0, 0x64)
    Sleep(200)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x168)
    OP_73(0x1)
    OP_23(0x70)
    Return()

    # Function_7_1392 end

    def Function_8_13B1(): pass

    label("Function_8_13B1")

    OP_8E(0xFE, 0x50, 0x0, 0x1B12, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFF92, 0x0, 0x2AE4, 0x7D0, 0x0)
    OP_8C(0xFE, 315, 0)
    OP_8F(0xFE, 0xFFFFEDA4, 0x0, 0x3674, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_8_13B1 end

    def Function_9_13FC(): pass

    label("Function_9_13FC")

    OP_8C(0xFE, 0, 0)
    OP_8E(0xFE, 0x50, 0x0, 0x1B12, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFF92, 0x0, 0x2AE4, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF33A, 0x0, 0x33EA, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_9_13FC end

    def Function_10_1447(): pass

    label("Function_10_1447")

    OP_8E(0xFE, 0x50, 0x0, 0x1B12, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFF92, 0x0, 0x2AE4, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF538, 0x0, 0x2E7C, 0x7D0, 0x0)
    OP_8C(0xFE, 315, 400)
    Return()

    # Function_10_1447 end

    def Function_11_148B(): pass

    label("Function_11_148B")

    OP_8E(0xFE, 0x50, 0x0, 0x1B12, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFF92, 0x0, 0x2AE4, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF998, 0x0, 0x3142, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_11_148B end

    def Function_12_14CF(): pass

    label("Function_12_14CF")


    def lambda_14D5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_14D5)
    OP_8F(0xFE, 0x35C, 0x0, 0xCBC, 0x7D0, 0x0)
    Return()

    # Function_12_14CF end

    def Function_13_14F6(): pass

    label("Function_13_14F6")


    def lambda_14FC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_14FC)
    OP_8F(0xFE, 0xFFFFFD80, 0x0, 0xC76, 0x7D0, 0x0)
    Return()

    # Function_13_14F6 end

    def Function_14_151D(): pass

    label("Function_14_151D")


    def lambda_1523():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1523)
    OP_8F(0xFE, 0x50A, 0x0, 0x564, 0x7D0, 0x0)
    Return()

    # Function_14_151D end

    def Function_15_1544(): pass

    label("Function_15_1544")


    def lambda_154A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_154A)
    OP_8F(0xFE, 0xFFFFFE20, 0x0, 0x53C, 0x7D0, 0x0)
    Return()

    # Function_15_1544 end

    SaveToFile()

Try(main)
