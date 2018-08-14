from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'P7011   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'P7011.x',
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
        "Function_1_14E",          # 01, 1
        "Function_2_14F",          # 02, 2
        "Function_3_C42",          # 03, 3
        "Function_4_C84",          # 04, 4
        "Function_5_CC6",          # 05, 5
        "Function_6_D08",          # 06, 6
        "Function_7_D4A",          # 07, 7
        "Function_8_185D",         # 08, 8
        "Function_9_1872",         # 09, 9
        "Function_10_189B",        # 0A, 10
        "Function_11_18C4",        # 0B, 11
        "Function_12_18ED",        # 0C, 12
        "Function_13_26C4",        # 0D, 13
        "Function_14_270D",        # 0E, 14
        "Function_15_274F",        # 0F, 15
        "Function_16_2798",        # 10, 16
        "Function_17_27DA",        # 11, 17
        "Function_18_2B68",        # 12, 18
        "Function_19_2B96",        # 13, 19
        "Function_20_2BBD",        # 14, 20
        "Function_21_2BEE",        # 15, 21
        "Function_22_2C1F",        # 16, 22
        "Function_23_3324",        # 17, 23
        "Function_24_3340",        # 18, 24
        "Function_25_3355",        # 19, 25
        "Function_26_336A",        # 1A, 26
        "Function_27_337F",        # 1B, 27
        "Function_28_375F",        # 1C, 28
        "Function_29_378D",        # 1D, 29
        "Function_30_37D6",        # 1E, 30
        "Function_31_3804",        # 1F, 31
        "Function_32_382B",        # 20, 32
        "Function_33_3C65",        # 21, 33
        "Function_34_3C81",        # 22, 34
        "Function_35_3C96",        # 23, 35
        "Function_36_3CBF",        # 24, 36
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x580, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D5")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C5")
    Event(0, 2)
    Jump("loc_D5")

    label("loc_C5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D5")
    Event(0, 7)

    label("loc_D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x580, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ED")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x72), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ED")
    Event(0, 12)

    label("loc_ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x580, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_105")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_105")
    Event(0, 17)

    label("loc_105")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x580, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11D")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11D")
    Event(0, 22)

    label("loc_11D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x581, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_135")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_135")
    Event(0, 27)

    label("loc_135")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x581, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14D")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x71), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14D")
    Event(0, 32)

    label("loc_14D")

    Return()

    # Function_0_AA end

    def Function_1_14E(): pass

    label("Function_1_14E")

    Return()

    # Function_1_14E end

    def Function_2_14F(): pass

    label("Function_2_14F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, 2470, 0, -170, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B0")
    SetChrPos(0xEF, 2470, 0, -170, 270)
    SetChrPos(0xF0, 2470, 0, -170, 270)
    SetChrPos(0xF1, 2470, 0, -170, 270)
    Jump("loc_235")

    label("loc_1B0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F4")
    SetChrPos(0xF0, 2470, 0, -170, 270)
    SetChrPos(0xEF, 2470, 0, -170, 270)
    SetChrPos(0xF1, 2470, 0, -170, 270)
    Jump("loc_235")

    label("loc_1F4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_235")
    SetChrPos(0xF1, 2470, 0, -170, 270)
    SetChrPos(0xEF, 2470, 0, -170, 270)
    SetChrPos(0xF0, 2470, 0, -170, 270)

    label("loc_235")

    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(840, 0, 410, 0)
    OP_67(0, 7060, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(250, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_22(0x6, 0x0, 0x64)
    Sleep(300)

    def lambda_2BD():
        OP_6D(-3510, 0, 3170, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_2BD)
    OP_43(0x109, 0x0, 0x0, 0x3)
    Sleep(600)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30B")
    OP_43(0xEF, 0x0, 0x0, 0x4)
    Sleep(600)
    OP_43(0xF0, 0x0, 0x0, 0x5)
    Sleep(500)
    OP_43(0xF1, 0x0, 0x0, 0x6)
    Jump("loc_368")

    label("loc_30B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33B")
    OP_43(0xF0, 0x0, 0x0, 0x4)
    Sleep(600)
    OP_43(0xEF, 0x0, 0x0, 0x5)
    Sleep(500)
    OP_43(0xF1, 0x0, 0x0, 0x6)
    Jump("loc_368")

    label("loc_33B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_368")
    OP_43(0xF1, 0x0, 0x0, 0x4)
    Sleep(600)
    OP_43(0xEF, 0x0, 0x0, 0x5)
    Sleep(500)
    OP_43(0xF0, 0x0, 0x0, 0x6)

    label("loc_368")

    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    WaitChrThread(0xEE, 0x3)
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3BB")

    ChrTalk(    #0
        0x105,
        "#1168F#6P啊，这里是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_635")

    label("loc_3BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3EC")

    ChrTalk(    #1
        0x103,
        "#1527F#6P这里是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_635")

    label("loc_3EC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_41D")

    ChrTalk(    #2
        0x101,
        "#1011F#6P这里是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_635")

    label("loc_41D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_44E")

    ChrTalk(    #3
        0x102,
        "#1500F#6P这里是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_635")

    label("loc_44E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_47E")

    ChrTalk(    #4
        0x10B,
        "#210F#6P这里是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_635")

    label("loc_47E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4AE")

    ChrTalk(    #5
        0x110,
        "#264F#6P这里是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_635")

    label("loc_4AE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4DE")

    ChrTalk(    #6
        0x107,
        "#560F#6P这里是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_635")

    label("loc_4DE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_513")

    ChrTalk(    #7
        0x10A,
        "#1310F#6P啊，这里是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_635")

    label("loc_513")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_543")

    ChrTalk(    #8
        0x106,
        "#051F#6P这里是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_635")

    label("loc_543")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_573")

    ChrTalk(    #9
        0x108,
        "#070F#6P这里是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_635")

    label("loc_573")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5A3")

    ChrTalk(    #10
        0x10E,
        "#171F#6P这里是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_635")

    label("loc_5A3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5D4")

    ChrTalk(    #11
        0x104,
        "#1540F#6P这里是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_635")

    label("loc_5D4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_608")

    ChrTalk(    #12
        0x10D,
        "#275F#6P……这里是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_635")

    label("loc_608")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_635")

    ChrTalk(    #13
        0x10C,
        "#111F#6P这里是……\x02",
    )

    CloseMessageWindow()

    label("loc_635")


    def lambda_63B():
        OP_6D(-4070, 0, 11330, 3500)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_63B)

    def lambda_653():
        OP_67(0, 7690, -10000, 3500)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_653)

    def lambda_66B():
        OP_6B(2650, 3500)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_66B)

    def lambda_67B():
        OP_6E(290, 3500)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_67B)
    WaitChrThread(0xEE, 0x0)
    Sleep(500)

    ChrTalk(    #14
        0x10F,
        (
            "#1447F#2P『紫苑之家』的起居室……\x01",
            "吃饭之类的事情就在此进行。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(-4100, 0, 3780, 0)
    OP_67(0, 5630, -10000, 0)
    OP_6B(2700, 0)
    OP_6C(315000, 0)
    OP_6E(278, 0)
    OP_0D()
    Sleep(500)
    OP_8C(0x109, 180, 400)
    Sleep(300)

    ChrTalk(    #15
        0x109,
        (
            "#1068F#11P不过，这里并不像\x01",
            "特蕾莎老师那里那样给人以温暖的感觉。\x02\x03",

            "#1840F这里的院长是个非常严厉，\x01",
            "头脑又很顽固的老修女。\x02\x03",

            "每顿饭之前都要让人祈祷来祈祷去的，\x01",
            "要是不遵守的话，就会挨骂甚至挨打。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_83C")

    ChrTalk(    #16
        0x105,
        "#1165F#6P是这样啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_870")

    label("loc_83C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_870")

    ChrTalk(    #17
        0x10A,
        (
            "#819F#6P嘿……\x01",
            "是这样啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_870")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8FA")

    ChrTalk(    #18
        0x104,
        (
            "#1541F#6P哦……\x01",
            "那还真是辛苦啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8F7")

    ChrTalk(    #19
        0x10D,
        (
            "#278F#6P呵呵，\x01",
            "你看起来就像是总被打的那种孩子吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8F7")

    Jump("loc_976")

    label("loc_8FA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_938")

    ChrTalk(    #20
        0x101,
        (
            "#1016F#6P唉……\x01",
            "那还真是辛苦啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_976")

    label("loc_938")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_976")

    ChrTalk(    #21
        0x10B,
        (
            "#210F#6P唔……\x01",
            "听起来好像很辛苦啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_976")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9CD")

    ChrTalk(    #22
        0x103,
        (
            "#1521F#6P不过，\x01",
            "教会的孤儿院严厉一些\x01",
            "也是理所当然的事情。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B69")

    label("loc_9CD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A23")

    ChrTalk(    #23
        0x106,
        (
            "#051F#6P不过，\x01",
            "教会的孤儿院严厉一些\x01",
            "也是理所当然的事情。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B69")

    label("loc_A23")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A81")

    ChrTalk(    #24
        0x108,
        (
            "#070F#6P反正是教会的孤儿院。\x01",
            "有这种严厉程度\x01",
            "也是理所当然的事情。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B69")

    label("loc_A81")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AD0")

    ChrTalk(    #25
        0x102,
        (
            "#1513F#6P一般来说\x01",
            "教会的孤儿院\x01",
            "管得的确很严厉呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B69")

    label("loc_AD0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B1E")

    ChrTalk(    #26
        0x10E,
        (
            "#179F#6P一般来说\x01",
            "教会的孤儿院\x01",
            "管得的确很严厉呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B69")

    label("loc_B1E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B69")

    ChrTalk(    #27
        0x10C,
        (
            "#119F#6P一般来说\x01",
            "教会的孤儿院\x01",
            "管得的确很严厉呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B69")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BA5")

    ChrTalk(    #28
        0x110,
        "#1300F#6P………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_BA5")


    ChrTalk(    #29
        0x10F,
        (
            "#1446F#6P……凯文，你是自作自受。\x02\x03",

            "#1801F总是不听话，\x01",
            "让老师伤透了脑筋。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x109,
        (
            "#1066F#11P哈哈……\x01",
            "嗯，那个我承认。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2C04)
    OP_28(0x3C, 0x1, 0x4)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_2_14F end

    def Function_3_C42(): pass

    label("Function_3_C42")


    def lambda_C48():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C48)
    OP_8E(0xFE, 0x136, 0x0, 0xFFFFFF74, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF4D4, 0x0, 0xE7E, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_3_C42 end

    def Function_4_C84(): pass

    label("Function_4_C84")


    def lambda_C8A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C8A)
    OP_8E(0xFE, 0x14A, 0x0, 0x10E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF39E, 0x0, 0x88E, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_4_C84 end

    def Function_5_CC6(): pass

    label("Function_5_CC6")


    def lambda_CCC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_CCC)
    OP_8E(0xFE, 0x136, 0x0, 0xFFFFFF74, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF394, 0x0, 0x2A8, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_5_CC6 end

    def Function_6_D08(): pass

    label("Function_6_D08")


    def lambda_D0E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D0E)
    OP_8E(0xFE, 0x14A, 0x0, 0x10E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF970, 0x0, 0x44C, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_6_D08 end

    def Function_7_D4A(): pass

    label("Function_7_D4A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, -3160, 0, 21490, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DAB")
    SetChrPos(0xEF, -3160, 0, 21490, 180)
    SetChrPos(0xF0, -3160, 0, 21490, 180)
    SetChrPos(0xF1, -3160, 0, 21490, 180)
    Jump("loc_E30")

    label("loc_DAB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DEF")
    SetChrPos(0xF0, -3160, 0, 21490, 180)
    SetChrPos(0xEF, -3160, 0, 21490, 180)
    SetChrPos(0xF1, -3160, 0, 21490, 180)
    Jump("loc_E30")

    label("loc_DEF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E30")
    SetChrPos(0xF1, -3160, 0, 21490, 180)
    SetChrPos(0xEF, -3160, 0, 21490, 180)
    SetChrPos(0xF0, -3160, 0, 21490, 180)

    label("loc_E30")

    OP_6D(-4250, 0, 20950, 0)
    OP_67(0, 5770, -10000, 0)
    OP_6B(2770, 0)
    OP_6C(315000, 0)
    OP_6E(267, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_72(0x1001, 0x0)
    ExitThread()
    OP_6F(0x1, 0)
    OP_70(0x1, 0xF)
    OP_73(0x1)

    def lambda_E99():
        OP_6D(-4110, 0, 18840, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_E99)
    OP_43(0x109, 0x0, 0x0, 0x8)
    Sleep(600)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EE7")
    OP_43(0xEF, 0x0, 0x0, 0x9)
    Sleep(600)
    OP_43(0xF0, 0x0, 0x0, 0xA)
    Sleep(500)
    OP_43(0xF1, 0x0, 0x0, 0xB)
    Jump("loc_F44")

    label("loc_EE7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F17")
    OP_43(0xF0, 0x0, 0x0, 0x9)
    Sleep(600)
    OP_43(0xEF, 0x0, 0x0, 0xA)
    Sleep(500)
    OP_43(0xF1, 0x0, 0x0, 0xB)
    Jump("loc_F44")

    label("loc_F17")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F44")
    OP_43(0xF1, 0x0, 0x0, 0x9)
    Sleep(600)
    OP_43(0xEF, 0x0, 0x0, 0xA)
    Sleep(500)
    OP_43(0xF0, 0x0, 0x0, 0xB)

    label("loc_F44")

    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    OP_72(0x1, 0x8)
    ExitThread()
    OP_22(0x7, 0x0, 0x64)
    OP_6F(0x1, 15)
    OP_70(0x1, 0x0)
    OP_73(0x1)
    OP_71(0x1001, 0x0)
    ExitThread()
    WaitChrThread(0xEE, 0x3)
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FBA")

    ChrTalk(    #31
        0x105,
        "#1168F#11P啊，这里是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1241")

    label("loc_FBA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FEC")

    ChrTalk(    #32
        0x103,
        "#1527F#11P这里是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1241")

    label("loc_FEC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_101E")

    ChrTalk(    #33
        0x101,
        "#1011F#11P这里是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1241")

    label("loc_101E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1050")

    ChrTalk(    #34
        0x102,
        "#1500F#11P这里是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1241")

    label("loc_1050")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1081")

    ChrTalk(    #35
        0x10B,
        "#210F#11P这里是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1241")

    label("loc_1081")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10B2")

    ChrTalk(    #36
        0x110,
        "#264F#11P这里是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1241")

    label("loc_10B2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10E3")

    ChrTalk(    #37
        0x107,
        "#560F#11P这里是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1241")

    label("loc_10E3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1119")

    ChrTalk(    #38
        0x10A,
        "#1310F#11P啊，这里是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1241")

    label("loc_1119")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_114A")

    ChrTalk(    #39
        0x106,
        "#051F#11P这里是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1241")

    label("loc_114A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_117B")

    ChrTalk(    #40
        0x108,
        "#070F#11P这里是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1241")

    label("loc_117B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11AC")

    ChrTalk(    #41
        0x10E,
        "#171F#11P这里是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1241")

    label("loc_11AC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11DE")

    ChrTalk(    #42
        0x104,
        "#1540F#11P这里是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1241")

    label("loc_11DE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1213")

    ChrTalk(    #43
        0x10D,
        "#275F#11P……这里是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1241")

    label("loc_1213")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1241")

    ChrTalk(    #44
        0x10C,
        "#111F#11P这里是……\x02",
    )

    CloseMessageWindow()

    label("loc_1241")

    Sleep(150)
    Fade(500)
    OP_6D(-4790, 0, 4000, 0)
    OP_67(0, 7690, -10000, 0)
    OP_6B(2650, 0)
    OP_6C(315000, 0)
    OP_6E(290, 0)
    OP_6D(-4070, 0, 11330, 4000)
    Sleep(500)

    ChrTalk(    #45
        0x10F,
        (
            "#1447F#3P『紫苑之家』的起居室……\x01",
            "吃饭之类的事情就在此进行。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(-4100, 0, 18800, 0)
    OP_67(0, 5590, -10000, 0)
    OP_6B(2770, 0)
    OP_6C(315000, 0)
    OP_6E(268, 0)
    OP_0D()
    Sleep(500)
    OP_8C(0x109, 0, 400)
    Sleep(300)

    ChrTalk(    #46
        0x109,
        (
            "#1068F#6P不过，这里并不像\x01",
            "特蕾莎老师那里那样给人以温暖的感觉。\x02\x03",

            "#1840F这里的院长是个非常严厉，\x01",
            "头脑又很顽固的老修女。\x02\x03",

            "每顿饭之前都要让人祈祷来祈祷去的，\x01",
            "要是不遵守的话，就会挨骂甚至挨打。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_144B")

    ChrTalk(    #47
        0x105,
        "#1165F#11P是这样啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1480")

    label("loc_144B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1480")

    ChrTalk(    #48
        0x10A,
        (
            "#819F#11P嘿……\x01",
            "是这样啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1480")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_150C")

    ChrTalk(    #49
        0x104,
        (
            "#1541F#11P哦……\x01",
            "那还真是辛苦啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1509")

    ChrTalk(    #50
        0x10D,
        (
            "#278F#11P呵呵，\x01",
            "你看起来就像是总被打的那种孩子吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1509")

    Jump("loc_158A")

    label("loc_150C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_154B")

    ChrTalk(    #51
        0x101,
        (
            "#1016F#11P唉……\x01",
            "那还真是辛苦啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_158A")

    label("loc_154B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_158A")

    ChrTalk(    #52
        0x10B,
        (
            "#210F#11P唔……\x01",
            "听起来好像很辛苦啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_158A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15E2")

    ChrTalk(    #53
        0x103,
        (
            "#1521F#11P不过，\x01",
            "教会的孤儿院严厉一些\x01",
            "也是理所当然的事情。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1783")

    label("loc_15E2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1639")

    ChrTalk(    #54
        0x106,
        (
            "#051F#11P不过，\x01",
            "教会的孤儿院严厉一些\x01",
            "也是理所当然的事情。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1783")

    label("loc_1639")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1698")

    ChrTalk(    #55
        0x108,
        (
            "#070F#11P反正是教会的孤儿院。\x01",
            "有这种严厉程度\x01",
            "也是理所当然的事情。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1783")

    label("loc_1698")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16E8")

    ChrTalk(    #56
        0x102,
        (
            "#1513F#11P一般来说\x01",
            "教会的孤儿院\x01",
            "管得的确很严厉呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1783")

    label("loc_16E8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1737")

    ChrTalk(    #57
        0x10E,
        (
            "#179F#11P一般来说\x01",
            "教会的孤儿院\x01",
            "管得的确很严厉呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1783")

    label("loc_1737")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1783")

    ChrTalk(    #58
        0x10C,
        (
            "#119F#11P一般来说\x01",
            "教会的孤儿院\x01",
            "管得的确很严厉呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1783")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17C0")

    ChrTalk(    #59
        0x110,
        "#1300F#11P………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_17C0")


    ChrTalk(    #60
        0x10F,
        (
            "#1446F#11P……凯文，你是自作自受。\x02\x03",

            "#1801F总是不听话，\x01",
            "让老师伤透了脑筋。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x109,
        (
            "#1066F#6P哈哈……\x01",
            "嗯，那个我承认。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2C04)
    OP_28(0x3C, 0x1, 0x4)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_7_D4A end

    def Function_8_185D(): pass

    label("Function_8_185D")

    OP_8F(0xFE, 0xFFFFF56A, 0x0, 0x3E9E, 0x7D0, 0x0)
    Return()

    # Function_8_185D end

    def Function_9_1872(): pass

    label("Function_9_1872")

    OP_8F(0xFE, 0xFFFFF506, 0x0, 0x4E02, 0x7D0, 0x0)
    OP_8F(0xFE, 0xFFFFF6C8, 0x0, 0x431C, 0x7D0, 0x0)
    Return()

    # Function_9_1872 end

    def Function_10_189B(): pass

    label("Function_10_189B")

    OP_8F(0xFE, 0xFFFFF506, 0x0, 0x4E02, 0x7D0, 0x0)
    OP_8F(0xFE, 0xFFFFF164, 0x0, 0x470E, 0x7D0, 0x0)
    Return()

    # Function_10_189B end

    def Function_11_18C4(): pass

    label("Function_11_18C4")

    OP_8F(0xFE, 0xFFFFF506, 0x0, 0x4E02, 0x7D0, 0x0)
    OP_8F(0xFE, 0xFFFFF7B8, 0x0, 0x47AE, 0x7D0, 0x0)
    Return()

    # Function_11_18C4 end

    def Function_12_18ED(): pass

    label("Function_12_18ED")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, 2500, 0, -22240, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_194E")
    SetChrPos(0xEF, 2500, 0, -22240, 270)
    SetChrPos(0xF0, 2500, 0, -22240, 270)
    SetChrPos(0xF1, 2500, 0, -22240, 270)
    Jump("loc_19D3")

    label("loc_194E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1992")
    SetChrPos(0xF0, 2500, 0, -22240, 270)
    SetChrPos(0xEF, 2500, 0, -22240, 270)
    SetChrPos(0xF1, 2500, 0, -22240, 270)
    Jump("loc_19D3")

    label("loc_1992")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19D3")
    SetChrPos(0xF1, 2500, 0, -22240, 270)
    SetChrPos(0xEF, 2500, 0, -22240, 270)
    SetChrPos(0xF0, 2500, 0, -22240, 270)

    label("loc_19D3")

    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(-3060, 0, -16110, 0)
    OP_67(0, 6650, -10000, 0)
    OP_6B(2760, 0)
    OP_6C(315000, 0)
    OP_6E(245, 0)

    def lambda_1A42():
        OP_6D(-2240, 0, -23650, 5500)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_1A42)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_22(0x6, 0x0, 0x64)
    Sleep(300)
    OP_43(0x109, 0x0, 0x0, 0xD)
    Sleep(800)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AA9")
    OP_43(0xEF, 0x0, 0x0, 0xE)
    Sleep(900)
    OP_43(0xF0, 0x0, 0x0, 0xF)
    Sleep(800)
    OP_43(0xF1, 0x0, 0x0, 0x10)
    Jump("loc_1B06")

    label("loc_1AA9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AD9")
    OP_43(0xF0, 0x0, 0x0, 0xE)
    Sleep(900)
    OP_43(0xEF, 0x0, 0x0, 0xF)
    Sleep(800)
    OP_43(0xF1, 0x0, 0x0, 0x10)
    Jump("loc_1B06")

    label("loc_1AD9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B06")
    OP_43(0xF1, 0x0, 0x0, 0xE)
    Sleep(900)
    OP_43(0xEF, 0x0, 0x0, 0xF)
    Sleep(800)
    OP_43(0xF0, 0x0, 0x0, 0x10)

    label("loc_1B06")

    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    WaitChrThread(0xEE, 0x3)
    Sleep(300)

    ChrTalk(    #62
        0x109,
        (
            "#1060F#6P这里是厨房……\x01",
            "是年长的孩子做饭的地方。\x02\x03",

            "而且也是莉丝经常\x01",
            "偷偷跑进来偷吃的地方。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #63
        0x10F,
        "#1441F#11P凯文……！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C29")

    ChrTalk(    #64
        0x101,
        (
            "#1016F#11P哈哈，是这样啊。\x02\x03",

            "#1008F难怪莉丝小姐\x01",
            "这么能吃。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C29")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C8C")

    ChrTalk(    #65
        0x105,
        (
            "#1165F#11P呵呵，是这样啊。\x02\x03",

            "#1168F这让我想起了\x01",
            "达尼艾尔和波利……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C8C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CE0")

    ChrTalk(    #66
        0x10B,
        (
            "#211F#11P哈哈，是这样吗。\x02\x03",

            "#210F这不是挺可爱的嘛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CE0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D1D")

    ChrTalk(    #67
        0x102,
        (
            "#1501F#11P呵呵……\x01",
            "真是意外呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DE6")

    label("loc_1D1D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D61")

    ChrTalk(    #68
        0x10E,
        (
            "#171F#11P呵呵……\x01",
            "听到了意外的事情呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DE6")

    label("loc_1D61")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DA5")

    ChrTalk(    #69
        0x10D,
        (
            "#275F#11P呵呵……\x01",
            "听到了意外的事情呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DE6")

    label("loc_1DA5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DE6")

    ChrTalk(    #70
        0x10C,
        (
            "#111F#11P哈哈……\x01",
            "听到了意外的事情呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DE6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E67")

    ChrTalk(    #71
        0x10A,
        (
            "#1317F#11P潜进厨房偷吃的\x01",
            "小时候的莉丝小姐……\x02\x03",

            "#1311F哈哈～只是想象一下\x01",
            "我都要激动得晕倒了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EDB")

    label("loc_1E67")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EDB")

    ChrTalk(    #72
        0x104,
        (
            "#1545F#11P潜进厨房偷吃的\x01",
            "小时候的莉丝君……\x02\x03",

            "#1547F呵，\x01",
            "真是让人窒息的美妙画面啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EDB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F13")

    ChrTalk(    #73
        0x107,
        "#067F#11P莉丝姐姐，真可爱……\x02",
    )

    CloseMessageWindow()

    label("loc_1F13")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F4E")

    ChrTalk(    #74
        0x110,
        (
            "#261F#11P呵呵……\x01",
            "姐姐还真可爱。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F4E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_204B")

    ChrTalk(    #75
        0x103,
        (
            "#1521F#11P呵呵……\x01",
            "感觉真是怀念啊。\x02\x03",

            "#1527F我也经常\x01",
            "偷喝戏团团长的酒，\x01",
            "然后被姐姐骂呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_200A")

    ChrTalk(    #76
        0x101,
        (
            "#1016F#11P竟然偷喝酒……\x01",
            "雪拉姐啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2048")

    label("loc_200A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2048")

    ChrTalk(    #77
        0x104,
        (
            "#1544F#11P竟然偷喝酒……\x01",
            "雪拉君……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2048")

    Jump("loc_212B")

    label("loc_204B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20BE")

    ChrTalk(    #78
        0x108,
        (
            "#071F#11P哈哈……\x01",
            "有种怀念的感觉呢。\x02\x03",

            "#070F我以前也经常因为\x01",
            "偷吃而被雾香揍呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_212B")

    label("loc_20BE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_212B")

    ChrTalk(    #79
        0x106,
        (
            "#556F#11P嘿……\x01",
            "感觉真是怀念啊。\x02\x03",

            "我以前也经常因为\x01",
            "偷吃东西而惹米夏生气呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_212B")

    OP_62(0x10F, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #80
        0x10F,
        "#1800F#11P真、真是的……大家都……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x109,
        (
            "#1077F#6P哈哈……\x01",
            "算了，这个先不提。\x02\x03",

            "#1840F这里也是露菲娜姐姐的\x01",
            "势力范围呢。\x02\x03",

            "她总是在这里给我和莉丝\x01",
            "以及其他的小朋友准备温暖的食物……\x02\x03",

            "#1075F自从姐姐当上了骑士，\x01",
            "做饭的工作就由我和莉丝接下来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x10F,
        (
            "#1447F#11P嗯……真怀念。\x02\x03",

            "#1801F……不过，\x01",
            "凯文总是随便就溜走了，\x01",
            "每次都是我一个人做的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x109,
        "#1064F#6P呜……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x10F,
        (
            "#1801F#11P……一想起这件事\x01",
            "我就一肚子火。\x02\x03",

            "你现在立刻给我做饭，\x01",
            "请我好好吃一顿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x109,
        (
            "#1841F#6P知道啦、知道啦。\x02\x03",

            "#1066F有机会的话\x01",
            "我就给你露一手。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x10F,
        (
            "#1446F#11P……凯文做的约定\x01",
            "从来没有兑现过。\x02\x03",

            "#1448F我就不抱什么希望\x01",
            "暂且看你怎么办了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x109,
        "#1840F#6P唉……说不过你。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2454")

    ChrTalk(    #88
        0x101,
        "#1016F#11P哈哈……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2480")

    label("loc_2454")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2480")

    ChrTalk(    #89
        0x10B,
        "#211F#11P哈哈……\x02",
    )

    CloseMessageWindow()

    label("loc_2480")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24AF")

    ChrTalk(    #90
        0x107,
        "#061F#11P嘻嘻……\x02",
    )

    CloseMessageWindow()
    Jump("loc_24DC")

    label("loc_24AF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24DC")

    ChrTalk(    #91
        0x105,
        "#1165F#11P嘻嘻……\x02",
    )

    CloseMessageWindow()

    label("loc_24DC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2509")

    ChrTalk(    #92
        0x110,
        "#1306F#11P嘻嘻……\x02",
    )

    CloseMessageWindow()

    label("loc_2509")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2536")

    ChrTalk(    #93
        0x104,
        "#1541F#11P呵呵……\x02",
    )

    CloseMessageWindow()

    label("loc_2536")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2566")

    ChrTalk(    #94
        0x102,
        "#1501F#11P呵呵……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2592")

    label("loc_2566")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2592")

    ChrTalk(    #95
        0x10A,
        "#811F#11P呵呵……\x02",
    )

    CloseMessageWindow()

    label("loc_2592")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25C1")

    ChrTalk(    #96
        0x108,
        "#071F#11P哈哈……\x02",
    )

    CloseMessageWindow()
    Jump("loc_261C")

    label("loc_25C1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25F0")

    ChrTalk(    #97
        0x10E,
        "#171F#11P哈哈……\x02",
    )

    CloseMessageWindow()
    Jump("loc_261C")

    label("loc_25F0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_261C")

    ChrTalk(    #98
        0x10C,
        "#111F#11P哈哈……\x02",
    )

    CloseMessageWindow()

    label("loc_261C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2650")

    ChrTalk(    #99
        0x103,
        "#1527F#11P哎呀哎呀……\x02",
    )

    CloseMessageWindow()
    Jump("loc_26B3")

    label("loc_2650")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2683")

    ChrTalk(    #100
        0x106,
        "#556F#11P哎呀哎呀……\x02",
    )

    CloseMessageWindow()
    Jump("loc_26B3")

    label("loc_2683")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26B3")

    ChrTalk(    #101
        0x10D,
        "#277F#11P哎呀哎呀……\x02",
    )

    CloseMessageWindow()

    label("loc_26B3")

    OP_A2(0x2C05)
    OP_28(0x3C, 0x1, 0x8)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_12_18ED end

    def Function_13_26C4(): pass

    label("Function_13_26C4")


    def lambda_26CA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_26CA)
    OP_8F(0xFE, 0x1CC, 0x0, 0xFFFFA894, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 0)
    OP_8F(0xFE, 0xFFFFFB32, 0x0, 0xFFFF9872, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_13_26C4 end

    def Function_14_270D(): pass

    label("Function_14_270D")


    def lambda_2713():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2713)
    OP_8F(0xFE, 0x1CC, 0x0, 0xFFFFA894, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 0)
    OP_8F(0xFE, 0xFFFFFC9A, 0x0, 0xFFFF9E30, 0x7D0, 0x0)
    Return()

    # Function_14_270D end

    def Function_15_274F(): pass

    label("Function_15_274F")


    def lambda_2755():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2755)
    OP_8F(0xFE, 0x1CC, 0x0, 0xFFFFA894, 0x7D0, 0x0)
    OP_8C(0xFE, 225, 0)
    OP_8F(0xFE, 0xFFFFF8C6, 0x0, 0xFFFFA40C, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_15_274F end

    def Function_16_2798(): pass

    label("Function_16_2798")


    def lambda_279E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_279E)
    OP_8F(0xFE, 0x1CC, 0x0, 0xFFFFA894, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 0)
    OP_8F(0xFE, 0xFFFFFF56, 0x0, 0xFFFFA272, 0x7D0, 0x0)
    Return()

    # Function_16_2798 end

    def Function_17_27DA(): pass

    label("Function_17_27DA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, -31690, 0, 6820, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_283B")
    SetChrPos(0xEF, -31690, 0, 6820, 270)
    SetChrPos(0xF0, -31690, 0, 6820, 270)
    SetChrPos(0xF1, -31690, 0, 6820, 270)
    Jump("loc_28C0")

    label("loc_283B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_287F")
    SetChrPos(0xF0, -31690, 0, 6820, 270)
    SetChrPos(0xEF, -31690, 0, 6820, 270)
    SetChrPos(0xF1, -31690, 0, 6820, 270)
    Jump("loc_28C0")

    label("loc_287F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28C0")
    SetChrPos(0xF1, -31690, 0, 6820, 270)
    SetChrPos(0xEF, -31690, 0, 6820, 270)
    SetChrPos(0xF0, -31690, 0, 6820, 270)

    label("loc_28C0")

    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(-36680, 0, 8370, 0)
    OP_67(0, 6010, -10000, 0)
    OP_6B(2660, 0)
    OP_6C(315000, 0)
    OP_6E(257, 0)
    FadeToBright(1000, 0)
    Sleep(300)
    OP_43(0x109, 0x0, 0x0, 0x12)
    Sleep(800)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2973")
    OP_43(0xEF, 0x0, 0x0, 0x13)
    Sleep(900)
    OP_43(0xF0, 0x0, 0x0, 0x14)
    Sleep(800)
    OP_43(0xF1, 0x0, 0x0, 0x15)
    Jump("loc_29D0")

    label("loc_2973")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29A3")
    OP_43(0xF0, 0x0, 0x0, 0x13)
    Sleep(900)
    OP_43(0xEF, 0x0, 0x0, 0x14)
    Sleep(800)
    OP_43(0xF1, 0x0, 0x0, 0x15)
    Jump("loc_29D0")

    label("loc_29A3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29D0")
    OP_43(0xF1, 0x0, 0x0, 0x13)
    Sleep(900)
    OP_43(0xEF, 0x0, 0x0, 0x14)
    Sleep(800)
    OP_43(0xF0, 0x0, 0x0, 0x15)

    label("loc_29D0")

    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #102
        0x10F,
        (
            "#1445F#6P院长老师的房间……\x01",
            "谁都不在呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x109,
        "#1065F#5P嗯……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x109, 90, 400)
    Sleep(500)

    ChrTalk(    #104
        0x109,
        (
            "#1060F#5P……对了，莉丝。\x02\x03",

            "那之后院长老师怎么样了……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x10F,
        (
            "#1447F#6P……嗯。\x01",
            "那时候受的伤已经没事了。\x02\x03",

            "#1445F不过自从她退休了之后，\x01",
            "果然还是没什么精神……\x02\x03",

            "#1802F……她很想\x01",
            "跟凯文见一面呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x109,
        "#1067F#5P………是吗…………\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2C06)
    OP_28(0x3C, 0x1, 0x10)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_17_27DA end

    def Function_18_2B68(): pass

    label("Function_18_2B68")


    def lambda_2B6E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2B6E)
    OP_8F(0xFE, 0xFFFF7068, 0x0, 0x1BA8, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_18_2B68 end

    def Function_19_2B96(): pass

    label("Function_19_2B96")


    def lambda_2B9C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2B9C)
    OP_8F(0xFE, 0xFFFF769E, 0x0, 0x1C84, 0x7D0, 0x0)
    Return()

    # Function_19_2B96 end

    def Function_20_2BBD(): pass

    label("Function_20_2BBD")

    SetChrFlags(0xFE, 0x4)

    def lambda_2BC8():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2BC8)
    OP_8F(0xFE, 0xFFFF7C34, 0x0, 0x1856, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_20_2BBD end

    def Function_21_2BEE(): pass

    label("Function_21_2BEE")

    SetChrFlags(0xFE, 0x4)

    def lambda_2BF9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2BF9)
    OP_8F(0xFE, 0xFFFF7CCA, 0x0, 0x1D88, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_21_2BEE end

    def Function_22_2C1F(): pass

    label("Function_22_2C1F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, -70500, 0, 8010, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C80")
    SetChrPos(0xEF, -70500, 0, 8010, 90)
    SetChrPos(0xF0, -70500, 0, 8010, 90)
    SetChrPos(0xF1, -70500, 0, 8010, 90)
    Jump("loc_2D05")

    label("loc_2C80")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CC4")
    SetChrPos(0xF0, -70500, 0, 8010, 90)
    SetChrPos(0xEF, -70500, 0, 8010, 90)
    SetChrPos(0xF1, -70500, 0, 8010, 90)
    Jump("loc_2D05")

    label("loc_2CC4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D05")
    SetChrPos(0xF1, -70500, 0, 8010, 90)
    SetChrPos(0xEF, -70500, 0, 8010, 90)
    SetChrPos(0xF0, -70500, 0, 8010, 90)

    label("loc_2D05")

    OP_6D(-69000, 0, 8800, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(256, 0)
    FadeToBright(1000, 0)
    Sleep(500)
    OP_72(0x1004, 0x0)
    ExitThread()
    OP_6F(0x4, 0)
    OP_70(0x4, 0xF)
    OP_73(0x1)
    Sleep(300)

    def lambda_2D72():
        OP_6D(-66580, 0, 8800, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_2D72)
    OP_43(0x109, 0x0, 0x0, 0x17)
    Sleep(600)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DC0")
    OP_43(0xEF, 0x0, 0x0, 0x18)
    Sleep(600)
    OP_43(0xF0, 0x0, 0x0, 0x19)
    Sleep(500)
    OP_43(0xF1, 0x0, 0x0, 0x1A)
    Jump("loc_2E1D")

    label("loc_2DC0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DF0")
    OP_43(0xF0, 0x0, 0x0, 0x18)
    Sleep(600)
    OP_43(0xEF, 0x0, 0x0, 0x19)
    Sleep(500)
    OP_43(0xF1, 0x0, 0x0, 0x1A)
    Jump("loc_2E1D")

    label("loc_2DF0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E1D")
    OP_43(0xF1, 0x0, 0x0, 0x18)
    Sleep(600)
    OP_43(0xEF, 0x0, 0x0, 0x19)
    Sleep(500)
    OP_43(0xF0, 0x0, 0x0, 0x1A)

    label("loc_2E1D")

    Sleep(1000)
    OP_22(0x7, 0x0, 0x64)
    OP_23(0x6)
    OP_6F(0x4, 15)
    OP_70(0x4, 0x0)
    OP_23(0x6)
    OP_73(0x4)
    OP_71(0x1004, 0x0)
    ExitThread()
    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    WaitChrThread(0xEE, 0x3)
    Sleep(300)

    ChrTalk(    #107
        0x109,
        (
            "#1060F#12P这里是孩子们的房间……\x01",
            "是小鬼们睡觉的地方。\x02\x03",

            "我被收留之后\x01",
            "也是睡在这里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x10F,
        (
            "#1447F#5P嗯，但是凯文和\x01",
            "其他孩子们一点也不亲近……\x02\x03",

            "#1806F姐姐为了让你们能够好好相处，\x01",
            "可是费了很大功夫哦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x109,
        (
            "#1067F#12P嗯……是啊。\x02\x03",

            "#1841F那时候的我\x01",
            "简直就像只刺猬一样，\x01",
            "是个一点也不可爱的臭小鬼。\x02\x03",

            "#1840F你能够满不在乎地接近我，\x01",
            "我还觉得不可思议呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x10F,
        (
            "#1447F#5P……我知道你那副样子\x01",
            "只不过是在逞强罢了。\x02\x03",

            "#1442F最初被姐姐强行\x01",
            "灌下巧克力的时候也是……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #111
        0x109,
        (
            "#1069F#12P#3S停！\x01",
            "后面的是禁止事项！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3103")

    ChrTalk(    #112
        0x101,
        "#1016F#5P（总、总觉得有些在意呢。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_3140")

    label("loc_3103")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3140")

    ChrTalk(    #113
        0x10B,
        "#210F#5P（总、总觉得有些在意呢。）\x02",
    )

    CloseMessageWindow()

    label("loc_3140")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3184")

    ChrTalk(    #114
        0x107,
        "#067F#5P（到、到底发生了什么呢……？）\x02",
    )

    CloseMessageWindow()
    Jump("loc_32D0")

    label("loc_3184")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_31CC")

    ChrTalk(    #115
        0x110,
        (
            "#1306F#5P（呵呵……\x01",
            "  到底发生了什么呢？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32D0")

    label("loc_31CC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_320D")

    ChrTalk(    #116
        0x102,
        "#1504F#5P（到底发生了什么呢……？）\x02",
    )

    CloseMessageWindow()
    Jump("loc_32D0")

    label("loc_320D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3251")

    ChrTalk(    #117
        0x10A,
        "#819F#5P（到、到底发生了什么呢……？）\x02",
    )

    CloseMessageWindow()
    Jump("loc_32D0")

    label("loc_3251")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3292")

    ChrTalk(    #118
        0x105,
        "#1165F#5P（到底发生了什么呢……？）\x02",
    )

    CloseMessageWindow()
    Jump("loc_32D0")

    label("loc_3292")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_32D0")

    ChrTalk(    #119
        0x103,
        "#1527F#5P（到底发生了什么呢……？）\x02",
    )

    CloseMessageWindow()

    label("loc_32D0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3313")

    ChrTalk(    #120
        0x104,
        (
            "#1547F#5P（唔……\x01",
            "  勾起我的兴趣来了。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3313")

    OP_A2(0x2C07)
    OP_28(0x3C, 0x1, 0x20)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_22_2C1F end

    def Function_23_3324(): pass

    label("Function_23_3324")

    OP_8F(0xFE, 0xFFFF07F4, 0x0, 0x1D7E, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_23_3324 end

    def Function_24_3340(): pass

    label("Function_24_3340")

    OP_8F(0xFE, 0xFFFF01A0, 0x0, 0x1CC0, 0x7D0, 0x0)
    Return()

    # Function_24_3340 end

    def Function_25_3355(): pass

    label("Function_25_3355")

    OP_8F(0xFE, 0xFFFEFC50, 0x0, 0x1B80, 0x7D0, 0x0)
    Return()

    # Function_25_3355 end

    def Function_26_336A(): pass

    label("Function_26_336A")

    OP_8F(0xFE, 0xFFFEFC8C, 0x0, 0x20BC, 0x7D0, 0x0)
    Return()

    # Function_26_336A end

    def Function_27_337F(): pass

    label("Function_27_337F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, -31770, 0, -21180, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33E0")
    SetChrPos(0xEF, -31770, 0, -21180, 270)
    SetChrPos(0xF0, -31770, 0, -21180, 270)
    SetChrPos(0xF1, -31770, 0, -21180, 270)
    Jump("loc_3465")

    label("loc_33E0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3424")
    SetChrPos(0xF0, -31770, 0, -21180, 270)
    SetChrPos(0xEF, -31770, 0, -21180, 270)
    SetChrPos(0xF1, -31770, 0, -21180, 270)
    Jump("loc_3465")

    label("loc_3424")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3465")
    SetChrPos(0xF1, -31770, 0, -21180, 270)
    SetChrPos(0xEF, -31770, 0, -21180, 270)
    SetChrPos(0xF0, -31770, 0, -21180, 270)

    label("loc_3465")

    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(-36130, 0, -20170, 0)
    OP_67(0, 5390, -10000, 0)
    OP_6B(2690, 0)
    OP_6C(315000, 0)
    OP_6E(264, 0)
    FadeToBright(1000, 0)
    Sleep(300)
    OP_43(0x109, 0x0, 0x0, 0x1C)
    Sleep(800)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3518")
    OP_43(0xEF, 0x0, 0x0, 0x1D)
    Sleep(900)
    OP_43(0xF0, 0x0, 0x0, 0x1E)
    Sleep(800)
    OP_43(0xF1, 0x0, 0x0, 0x1F)
    Jump("loc_3575")

    label("loc_3518")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3548")
    OP_43(0xF0, 0x0, 0x0, 0x1D)
    Sleep(900)
    OP_43(0xEF, 0x0, 0x0, 0x1E)
    Sleep(800)
    OP_43(0xF1, 0x0, 0x0, 0x1F)
    Jump("loc_3575")

    label("loc_3548")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3575")
    OP_43(0xF1, 0x0, 0x0, 0x1D)
    Sleep(900)
    OP_43(0xEF, 0x0, 0x0, 0x1E)
    Sleep(800)
    OP_43(0xF0, 0x0, 0x0, 0x1F)

    label("loc_3575")

    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #121
        0x109,
        (
            "#1065F#5P这里是男生的房间……\x01",
            "我也是１０岁左右\x01",
            "转移到这里的。\x02\x03",

            "#1840F原则上来说，\x01",
            "男生和女生都是不能进入异性房间的……\x02\x03",

            "不过你倒是若无其事的进来过吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x10F,
        (
            "#1801F#6P……那不是都怪凯文吗。\x02\x03",

            "谁叫你做值日的早晨\x01",
            "还若无其事地睡过头。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x109,
        (
            "#1079F#5P那、那种事，\x01",
            "只要敲敲门喊两声\x01",
            "不就解决了吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x10F,
        (
            "#1443F#6P那样也会\x01",
            "吵醒其他人的嘛。\x02\x03",

            "#1446F总之还是凯文的错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x109,
        "#1840F#5P……是是。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2C08)
    OP_28(0x3C, 0x1, 0x40)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_27_337F end

    def Function_28_375F(): pass

    label("Function_28_375F")


    def lambda_3765():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3765)
    OP_8F(0xFE, 0xFFFF72DE, 0x0, 0xFFFFAAD8, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_28_375F end

    def Function_29_378D(): pass

    label("Function_29_378D")


    def lambda_3793():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3793)
    OP_8F(0xFE, 0xFFFF7E14, 0x0, 0xFFFFACFE, 0x7D0, 0x0)
    OP_8C(0xFE, 225, 0)
    OP_8F(0xFE, 0xFFFF7982, 0x0, 0xFFFFA8D0, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_29_378D end

    def Function_30_37D6(): pass

    label("Function_30_37D6")


    def lambda_37DC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_37DC)
    OP_8F(0xFE, 0xFFFF782E, 0x0, 0xFFFFAFD8, 0x7D0, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_30_37D6 end

    def Function_31_3804(): pass

    label("Function_31_3804")


    def lambda_380A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_380A)
    OP_8F(0xFE, 0xFFFF7CAC, 0x0, 0xFFFFAB6E, 0x7D0, 0x0)
    Return()

    # Function_31_3804 end

    def Function_32_382B(): pass

    label("Function_32_382B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, -70500, 0, -22050, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_388C")
    SetChrPos(0xEF, -70500, 0, -22050, 90)
    SetChrPos(0xF0, -70500, 0, -22050, 90)
    SetChrPos(0xF1, -70500, 0, -22050, 90)
    Jump("loc_3911")

    label("loc_388C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38D0")
    SetChrPos(0xF0, -70500, 0, -22050, 90)
    SetChrPos(0xEF, -70500, 0, -22050, 90)
    SetChrPos(0xF1, -70500, 0, -22050, 90)
    Jump("loc_3911")

    label("loc_38D0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3911")
    SetChrPos(0xF1, -70500, 0, -22050, 90)
    SetChrPos(0xEF, -70500, 0, -22050, 90)
    SetChrPos(0xF0, -70500, 0, -22050, 90)

    label("loc_3911")

    OP_6D(-69000, 0, -21100, 0)
    OP_67(0, 5300, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(263, 0)
    FadeToBright(1000, 0)
    Sleep(500)
    OP_72(0x1005, 0x0)
    ExitThread()
    OP_6F(0x5, 0)
    OP_70(0x5, 0xF)
    OP_73(0x5)
    Sleep(300)

    def lambda_397E():
        OP_6D(-66970, 0, -21510, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_397E)
    OP_43(0x109, 0x0, 0x0, 0x21)
    Sleep(600)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39CC")
    OP_43(0xEF, 0x0, 0x0, 0x22)
    Sleep(600)
    OP_43(0xF0, 0x0, 0x0, 0x23)
    Sleep(500)
    OP_43(0xF1, 0x0, 0x0, 0x24)
    Jump("loc_3A29")

    label("loc_39CC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39FC")
    OP_43(0xF0, 0x0, 0x0, 0x22)
    Sleep(600)
    OP_43(0xEF, 0x0, 0x0, 0x23)
    Sleep(500)
    OP_43(0xF1, 0x0, 0x0, 0x24)
    Jump("loc_3A29")

    label("loc_39FC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A29")
    OP_43(0xF1, 0x0, 0x0, 0x22)
    Sleep(600)
    OP_43(0xEF, 0x0, 0x0, 0x23)
    Sleep(500)
    OP_43(0xF0, 0x0, 0x0, 0x24)

    label("loc_3A29")

    Sleep(1000)
    OP_22(0x7, 0x0, 0x64)
    OP_23(0x6)
    OP_6F(0x5, 15)
    OP_70(0x5, 0x0)
    OP_23(0x6)
    OP_73(0x5)
    OP_71(0x1005, 0x0)
    ExitThread()
    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    WaitChrThread(0xEE, 0x3)
    Sleep(300)

    ChrTalk(    #126
        0x109,
        (
            "#1840F#12P这边是……\x01",
            "女生的房间吧。\x02\x03",

            "露菲娜姐姐\x01",
            "一直是在这里生活的啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x10F,
        (
            "#1442F#5P我有时候\x01",
            "还会和姐姐一起睡呢。\x02\x03",

            "#1447F姐姐的床\x01",
            "又温暖又有一股香味……\x02\x03",

            "姐姐离开这里之后\x01",
            "就是我在用了。\x02\x03",

            "#1448F……羡慕吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x109,
        (
            "#1077F#12P哈哈……是啊。\x02\x03",

            "#1078F那个时候\x01",
            "确实有点羡慕呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x10F,
        (
            "#1803F#5P怎么……\x01",
            "还以为你会更焦虑呢。\x02\x03",

            "#1446F这么直率的回答真是没劲。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(    #130
        0x109,
        "#1068F#12P……我说你啊。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2C09)
    OP_28(0x3C, 0x1, 0x80)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_32_382B end

    def Function_33_3C65(): pass

    label("Function_33_3C65")

    OP_8F(0xFE, 0xFFFF0650, 0x0, 0xFFFFA6B4, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_33_3C65 end

    def Function_34_3C81(): pass

    label("Function_34_3C81")

    OP_8F(0xFE, 0xFFFEFF98, 0x0, 0xFFFFA6DC, 0x7D0, 0x0)
    Return()

    # Function_34_3C81 end

    def Function_35_3C96(): pass

    label("Function_35_3C96")

    OP_8F(0xFE, 0xFFFEF462, 0x0, 0xFFFFA90C, 0x7D0, 0x0)
    OP_8F(0xFE, 0xFFFEFBC4, 0x0, 0xFFFFA448, 0x7D0, 0x0)
    Return()

    # Function_35_3C96 end

    def Function_36_3CBF(): pass

    label("Function_36_3CBF")

    OP_8F(0xFE, 0xFFFEFA98, 0x0, 0xFFFFA9B6, 0x7D0, 0x0)
    Return()

    # Function_36_3CBF end

    SaveToFile()

Try(main)
