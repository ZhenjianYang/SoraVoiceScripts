from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T1102_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T1102_1 ._SN',
            '',
            '',
            '',
            '',
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '',                                     # 9
        '',                                     # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
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
        "Function_1_18E8",         # 01, 1
        "Function_2_18FA",         # 02, 2
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_319")

    ChrTalk(    #0
        0x101,
        (
            "#1002F卡片里的地方……\x02\x03",

            "……莫非是指这里？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_174")

    ChrTalk(    #1
        0x103,
        (
            "#022F嗯，虽然有这可能性……\x02\x03",

            "那个事件的调查稍后再进行吧。\x01",
            "现在要赶紧前往拉文努村哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #2
        0x101,
        "#1002F啊，嗯……明白。\x02",
    )

    CloseMessageWindow()
    Jump("loc_315")

    label("loc_174")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_202")

    ChrTalk(    #3
        0x108,
        (
            "#072F嗯，是有很可能……\x02\x03",

            "不过那个事件的调查稍后再进行吧。\x01",
            "现在应该赶紧前往拉文努村。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x108, 400)

    ChrTalk(    #4
        0x101,
        "#1002F啊，嗯……明白。\x02",
    )

    CloseMessageWindow()
    Jump("loc_315")

    label("loc_202")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_290")

    ChrTalk(    #5
        0x104,
        (
            "#030F唔，是很有可能……\x02\x03",

            "不过那个事件的调查稍后再进行吧。\x01",
            "现在先赶紧前往拉文努村吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)

    ChrTalk(    #6
        0x101,
        "#1002F啊，嗯……明白。\x02",
    )

    CloseMessageWindow()
    Jump("loc_315")

    label("loc_290")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_315")

    ChrTalk(    #7
        0x105,
        (
            "#042F嗯，说不定就是……\x02\x03",

            "不过这里迟些再调查吧。\x01",
            "现在得赶紧前往拉文努村啊……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #8
        0x101,
        "#1002F啊，嗯……说得对。\x02",
    )

    CloseMessageWindow()

    label("loc_315")

    TalkEnd(0xFF)
    Return()

    label("loc_319")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 23790, -3000, 12560, 135)
    SetChrPos(0xF7, 22600, -3000, 12510, 135)
    SetChrPos(0xF8, 23080, -3000, 13980, 135)
    SetChrPos(0xF9, 21720, -3000, 13710, 135)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_381")
    SetChrPos(0x4, 21150, -3000, 12710, 135)

    label("loc_381")

    SetChrPos(0x19, 36190, -3000, 13170, 270)
    OP_6D(26500, -3000, 9360, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2950, 0)
    OP_6C(166000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_6D(23790, -3000, 12560, 2000)

    ChrTalk(    #9
        0x101,
        (
            "#1011F这就是『被托起的棺材』吗……\x02\x03",

            "虽然看上去不像是『棺』，\x01",
            "不过『被托住』看起来是的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_47F")

    ChrTalk(    #10
        0x106,
        (
            "#050F嗯，不过……\x02\x03",

            "好像没发现\x01",
            "关键的卡片。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_545")

    label("loc_47F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C0")

    ChrTalk(    #11
        0x103,
        (
            "#020F嗯，不过……\x02\x03",

            "好像没发现\x01",
            "关键的卡片。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_545")

    label("loc_4C0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_501")

    ChrTalk(    #12
        0x108,
        (
            "#070F嗯，不过……\x02\x03",

            "好像没发现\x01",
            "关键的卡片。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_545")

    label("loc_501")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_545")

    ChrTalk(    #13
        0x104,
        (
            "#030F确实如此，不过……\x02\x03",

            "好像没发现\x01",
            "关键的卡片。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_545")


    ChrTalk(    #14
        0x101,
        (
            "#1015F唔，真奇怪～\x02\x03",

            "感觉地方\x01",
            "应该没找错……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x101, 300, 400)

    ChrTalk(    #15
        0x101,
        (
            "#1018F啊，莫非！？\x01",
            "会不会在货箱底下？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_613")

    ChrTalk(    #16
        0x107,
        (
            "#063F嗯，有可能……\x02\x03",

            "但是，要钻下去调查\x01",
            "好像空隙不够呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_707")

    label("loc_613")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_668")

    ChrTalk(    #17
        0x105,
        (
            "#043F嗯，这么想也有道理……\x02\x03",

            "但是，要钻下去调查\x01",
            "好像空隙不够。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_707")

    label("loc_668")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6BB")

    ChrTalk(    #18
        0x104,
        (
            "#030F嗯，有这个可能性……\x02\x03",

            "但是，要钻下去调查\x01",
            "好像空隙不够。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_707")

    label("loc_6BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_707")

    ChrTalk(    #19
        0x108,
        (
            "#070F嗯，也有可能……\x02\x03",

            "但是，要钻下去调查\x01",
            "好像空隙不够。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_707")


    ChrTalk(    #20
        0x101,
        "#1007F确、确实……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 135, 400)

    ChrTalk(    #21
        0x101,
        (
            "#1003F嗯，可我觉得这个\x01",
            "货箱实在很可疑……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #22
        0x19,
        "男人的声音",
        "#2P喂，你们在干吗！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF6)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7A0")
    OP_62(0xF6, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_7DE")

    label("loc_7A0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF6)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C7")
    OP_62(0xF6, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_7DE")

    label("loc_7C7")

    OP_62(0xF6, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_7DE")

    Sleep(150)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_80A")
    OP_62(0xF7, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_848")

    label("loc_80A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_831")
    OP_62(0xF7, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_848")

    label("loc_831")

    OP_62(0xF7, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_848")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_86F")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_8AD")

    label("loc_86F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_896")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_8AD")

    label("loc_896")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_8AD")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D9")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_917")

    label("loc_8D9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_900")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_917")

    label("loc_900")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_917")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_960")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_949")
    OP_62(0x4, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_960")

    label("loc_949")

    OP_62(0x4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_960")

    Sleep(1000)

    def lambda_96B():
        OP_8C(0x2, 90, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_96B)
    Sleep(100)

    def lambda_97E():
        OP_8C(0x3, 90, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_97E)

    def lambda_98C():
        OP_8C(0x1, 90, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_98C)
    Sleep(100)

    def lambda_99F():
        OP_8C(0x0, 90, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_99F)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9C1")

    def lambda_9B9():
        OP_8C(0x4, 90, 400)
        ExitThread()

    QueueWorkItem(0x4, 1, lambda_9B9)

    label("loc_9C1")


    def lambda_9C7():
        OP_6C(225000, 4000)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_9C7)
    OP_43(0x101, 0x2, 0x1, 0x1)
    OP_8E(0x19, 0x639C, 0xFFFFF448, 0x3322, 0xBB8, 0x0)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A0C")
    OP_44(0x4, 0x1)

    label("loc_A0C")

    OP_4A(0x19, 255)

    ChrTalk(    #23
        0x19,
        (
            "你们是不是在\x01",
            "乱动这里的机器？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x19,
        "到底想干什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        (
            "#1009F我、我们没有乱动。\x02\x03",

            "只是有点事情\x01",
            "想要调查。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x19,
        "啊？想要调查事情？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B04")

    ChrTalk(    #27
        0x106,
        "#050F嗯，我们的职业是…\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #28
        "\x07\x05阿加特拿出了游击士的徽章。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jump("loc_C43")

    label("loc_B04")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B74")

    ChrTalk(    #29
        0x103,
        "#020F嗯，我们的职业是…\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #30
        "\x07\x05雪拉扎德拿出了游击士的徽章。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jump("loc_C43")

    label("loc_B74")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BDE")

    ChrTalk(    #31
        0x108,
        "#070F嗯，我们的职业是…\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #32
        "\x07\x05金拿出了游击士的徽章。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jump("loc_C43")

    label("loc_BDE")


    ChrTalk(    #33
        0x101,
        (
            "#1002F嗯，我们\x01",
            "的职业其实是…\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #34
        "\x07\x05艾丝蒂尔拿出了游击士的徽章。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_C43")


    ChrTalk(    #35
        0x19,
        "啊，原来是游击士。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x19,
        "在调查案件吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        (
            "#1002F正调查到关键的地方了。\x02\x03",

            "#1011F啊，对了。\x01",
            "有件事我想问一下……\x02\x03",

            "大叔你能\x01",
            "操纵这部机器吗？？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x19,
        "嗯，当然能啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x19,
        "怎么了？你们想让我操纵它？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x101,
        (
            "#1002F嗯，实际上我们\x01",
            "必须要调查一下货箱的底部。\x02\x03",

            "能不能麻烦你把它提升到\x01",
            "能看得到下面的程度？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x19,
        "嗯，这个好办。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x19,
        (
            "好，那么你们\x01",
            "稍微在那边等一下。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_DAA():

        label("loc_DAA")

        TurnDirection(0xFE, 0x19, 400)
        OP_48()
        Jump("loc_DAA")

    QueueWorkItem2(0x0, 1, lambda_DAA)

    def lambda_DBB():

        label("loc_DBB")

        TurnDirection(0xFE, 0x19, 400)
        OP_48()
        Jump("loc_DBB")

    QueueWorkItem2(0x1, 1, lambda_DBB)

    def lambda_DCC():

        label("loc_DCC")

        TurnDirection(0xFE, 0x19, 400)
        OP_48()
        Jump("loc_DCC")

    QueueWorkItem2(0x2, 1, lambda_DCC)

    def lambda_DDD():

        label("loc_DDD")

        TurnDirection(0xFE, 0x19, 400)
        OP_48()
        Jump("loc_DDD")

    QueueWorkItem2(0x3, 1, lambda_DDD)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E05")

    def lambda_DFA():

        label("loc_DFA")

        TurnDirection(0xFE, 0x19, 400)
        OP_48()
        Jump("loc_DFA")

    QueueWorkItem2(0x4, 1, lambda_DFA)

    label("loc_E05")


    def lambda_E0B():
        OP_6C(155000, 4000)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_E0B)

    def lambda_E1B():
        OP_6D(26860, -3000, 9620, 4000)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_E1B)
    OP_8C(0x19, 135, 400)
    OP_8E(0x19, 0x6D4C, 0xFFFFF448, 0x2A26, 0x7D0, 0x0)
    OP_8C(0x19, 225, 400)
    OP_8E(0x19, 0x6C16, 0xFFFFF448, 0x28F0, 0x3E8, 0x0)
    SetChrFlags(0x19, 0x40)
    SetChrFlags(0x19, 0x4)
    SetChrFlags(0x19, 0x10)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    OP_8E(0x19, 0x6A68, 0xFFFFF6A0, 0x249A, 0x3E8, 0x0)
    OP_8C(0x19, 315, 400)
    OP_8E(0x19, 0x6932, 0xFFFFF5D8, 0x25B2, 0x3E8, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EC1")
    OP_44(0x4, 0x1)

    label("loc_EC1")

    Sleep(1000)
    Sleep(100)
    OP_22(0x9D, 0x0, 0x64)
    Sleep(400)
    OP_22(0xCF, 0x1, 0x55)

    ChrTalk(    #43
        0x19,
        "好，那么我要开始了。\x02",
    )

    CloseMessageWindow()
    OP_24(0xCF, 0x64)
    OP_B0(0xD, 0xA)
    OP_70(0xD, 0x1E)
    OP_73(0xD)
    OP_22(0x9A, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #44
        0x19,
        "嗯～已经固定好了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x19,
        (
            "你们可以到\x01",
            "货箱下面去调查了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        (
            "#1006F#1P嗯，明白了。\x01",
            "我们马上调查。\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x101, 0x620C, 0xFFFFF448, 0x2AEE, 0x7D0, 0x0)
    Sleep(500)
    OP_8C(0x101, 270, 400)
    Sleep(200)
    OP_8C(0x101, 90, 400)
    Sleep(500)
    OP_8C(0x101, 120, 400)
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #47
        (
            "\x07\x05调查了货箱底部，\x01",
            "发现贴着卡片。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #48
        0x101,
        "#1006F#1P好，有了⊙\x02",
    )

    CloseMessageWindow()
    OP_8E(0x101, 0x5CEE, 0xFFFFF448, 0x3110, 0x7D0, 0x0)
    OP_8C(0x101, 120, 400)

    ChrTalk(    #49
        0x101,
        (
            "#1018F#1P谢谢你，大叔。\x01",
            "已经好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x19,
        (
            "嗯，那么我要放下\x01",
            "货箱了哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_B0(0xD, 0xA)
    OP_6F(0xD, 30)
    OP_70(0xD, 0x0)
    OP_73(0xD)
    OP_22(0x9A, 0x0, 0x64)
    OP_23(0x9D)
    OP_23(0xCF)
    Sleep(400)
    Fade(1000)
    OP_6C(225000, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2950, 0)
    OP_6E(262, 0)
    SetChrPos(0x19, 27780, -3000, 10390, 30)
    SetChrFlags(0x19, 0x40)
    SetChrFlags(0x19, 0x4)
    SetChrFlags(0x19, 0x10)

    def lambda_110C():

        label("loc_110C")

        TurnDirection(0xFE, 0x19, 400)
        OP_48()
        Jump("loc_110C")

    QueueWorkItem2(0x0, 1, lambda_110C)

    def lambda_111D():

        label("loc_111D")

        TurnDirection(0xFE, 0x19, 400)
        OP_48()
        Jump("loc_111D")

    QueueWorkItem2(0x1, 1, lambda_111D)

    def lambda_112E():

        label("loc_112E")

        TurnDirection(0xFE, 0x19, 400)
        OP_48()
        Jump("loc_112E")

    QueueWorkItem2(0x2, 1, lambda_112E)

    def lambda_113F():

        label("loc_113F")

        TurnDirection(0xFE, 0x19, 400)
        OP_48()
        Jump("loc_113F")

    QueueWorkItem2(0x3, 1, lambda_113F)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1167")

    def lambda_115C():

        label("loc_115C")

        TurnDirection(0xFE, 0x19, 400)
        OP_48()
        Jump("loc_115C")

    QueueWorkItem2(0x4, 1, lambda_115C)

    label("loc_1167")


    def lambda_116D():
        OP_6D(23760, -3000, 13010, 3000)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_116D)
    OP_8E(0x19, 0x6A2C, 0xFFFFF448, 0x2D78, 0x7D0, 0x0)
    OP_8E(0x19, 0x639C, 0xFFFFF448, 0x3322, 0x7D0, 0x0)
    TurnDirection(0x19, 0x101, 400)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11CE")
    OP_44(0x4, 0x1)

    label("loc_11CE")

    WaitChrThread(0x2A, 0x1)
    WaitChrThread(0x2A, 0x2)

    ChrTalk(    #51
        0x19,
        (
            "看来你们已经\x01",
            "找到了要找的东西。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1227")

    ChrTalk(    #52
        0x104,
        "#030F多谢您的帮助。\x02",
    )

    CloseMessageWindow()
    Jump("loc_12A0")

    label("loc_1227")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1251")

    ChrTalk(    #53
        0x108,
        "#070F谢谢您的帮助。\x02",
    )

    CloseMessageWindow()
    Jump("loc_12A0")

    label("loc_1251")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_127B")

    ChrTalk(    #54
        0x103,
        "#525F谢谢您的帮助。\x02",
    )

    CloseMessageWindow()
    Jump("loc_12A0")

    label("loc_127B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12A0")

    ChrTalk(    #55
        0x106,
        "#051F谢谢您帮忙。\x02",
    )

    CloseMessageWindow()

    label("loc_12A0")


    ChrTalk(    #56
        0x19,
        (
            "哈哈，不用介意。\x01",
            "我也没做什么了不得的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x19,
        (
            "虽然不知道你们在调查什么，\x01",
            "总之好好地解决掉它吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x19,
        "那我就回去工作啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x101,
        "#1001F嗯，谢谢您。\x02",
    )

    CloseMessageWindow()
    OP_43(0x101, 0x2, 0x1, 0x2)
    OP_8E(0x19, 0x8D5E, 0xFFFFF448, 0x3372, 0x7D0, 0x0)

    ChrTalk(    #60
        0x101,
        (
            "#1011F呼，想不到在这时候\x01",
            "出现了一个帮手。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13BE")
    TurnDirection(0x108, 0x101, 400)

    ChrTalk(    #61
        0x108,
        (
            "#070F嗯，那么\x01",
            "我们就继续工作吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1475")

    label("loc_13BE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13FC")
    TurnDirection(0x106, 0x101, 400)

    ChrTalk(    #62
        0x106,
        (
            "#050F嗯，那么\x01",
            "我们就继续工作吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1475")

    label("loc_13FC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_143A")
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #63
        0x103,
        (
            "#020F嗯，那么\x01",
            "我们就继续工作吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1475")

    label("loc_143A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1475")
    TurnDirection(0x104, 0x101, 400)

    ChrTalk(    #64
        0x104,
        (
            "#030F嗯，那么\x01",
            "我们就继续工作吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1475")


    def lambda_147B():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_147B)

    def lambda_1489():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_1489)

    def lambda_1497():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_1497)

    def lambda_14A5():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_14A5)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14C7")

    def lambda_14BF():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x4, 1, lambda_14BF)

    label("loc_14C7")

    WaitChrThread(0x101, 0x1)
    WaitChrThread(0xF7, 0x1)
    WaitChrThread(0xF8, 0x1)
    WaitChrThread(0xF9, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14EC")
    WaitChrThread(0x4, 0x1)

    label("loc_14EC")


    ChrTalk(    #65
        0x101,
        (
            "#1000F#1P嗯，赶快确认\x01",
            "卡片内容吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)
    Fade(500)
    SetChrChipByIndex(0x101, 32)
    OP_0D()
    FadeToDark(300, 0, 100)
    OP_AD(0x240093, 0xBE, 0x64, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(-1, 300, -1, 3)
    SetChrName("")

    AnonymousTalk(    #66
        (
            "\x07\x05　　 门已经被打开了。 　 　\x01",
            "　　　寻求虚荣之证　　　\x01",
            "　就在『女神的话语』中。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_AE(0x1F4)
    Sleep(1000)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Fade(500)
    SetChrChipByIndex(0x101, 65535)
    OP_0D()

    ChrTalk(    #67
        0x101,
        (
            "#1000F#1P…………就这些。\x02\x03",

            "#1000F看来只差最后一步了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_165E")

    ChrTalk(    #68
        0x107,
        (
            "#060F嗯，好像是的。\x02\x03",

            "接下来的提示是\x01",
            "『女神的话语』啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1748")

    label("loc_165E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16AD")

    ChrTalk(    #69
        0x105,
        (
            "#040F嗯，好像是的。\x02\x03",

            "接下来的提示是\x01",
            "『女神的话语』啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1748")

    label("loc_16AD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16FC")

    ChrTalk(    #70
        0x104,
        (
            "#030F嗯，好像是的。\x02\x03",

            "接下来的提示是\x01",
            "『女神的话语』啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1748")

    label("loc_16FC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1748")

    ChrTalk(    #71
        0x108,
        (
            "#070F嗯，好像是的。\x02\x03",

            "接下来的提示是\x01",
            "『女神的话语』啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1748")


    ChrTalk(    #72
        0x101,
        (
            "#1015F#1P说起城里的『女神』的话\x01",
            "就只有那一个地方了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17C8")

    ChrTalk(    #73
        0x106,
        (
            "#050F确实如此。\x02\x03",

            "马上去那里\x01",
            "调查一下吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)
    Jump("loc_189B")

    label("loc_17C8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_180E")

    ChrTalk(    #74
        0x103,
        (
            "#020F确实如此。\x02\x03",

            "马上去那里\x01",
            "调查一下吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)
    Jump("loc_189B")

    label("loc_180E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1854")

    ChrTalk(    #75
        0x108,
        (
            "#070F确实如此。\x02\x03",

            "马上去那里\x01",
            "调查一下吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x108, 400)
    Jump("loc_189B")

    label("loc_1854")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_189B")

    ChrTalk(    #76
        0x104,
        (
            "#030F嗯，确实如此。\x02\x03",

            "马上去那里\x01",
            "调查一下吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)

    label("loc_189B")


    ChrTalk(    #77
        0x101,
        "#1006F#1P嗯，就这么办。\x02",
    )

    CloseMessageWindow()
    OP_4B(0x19, 255)
    ClearChrFlags(0x19, 0x10)
    SetChrPos(0x19, 27300, -10000, 26800, 315)
    OP_28(0x78, 0x1, 0x40)
    OP_28(0x78, 0x1, 0x80)
    OP_A2(0x11)
    OP_64(0x1, 0x1)
    EventEnd(0x0)
    Return()

    # Function_0_AA end

    def Function_1_18E8(): pass

    label("Function_1_18E8")

    OP_6D(23760, -3000, 13010, 2000)
    Return()

    # Function_1_18E8 end

    def Function_2_18FA(): pass

    label("Function_2_18FA")

    OP_6D(27220, -3000, 13160, 2000)
    Sleep(1000)
    OP_6D(22860, -3000, 13110, 2000)
    Return()

    # Function_2_18FA end

    SaveToFile()

Try(main)
