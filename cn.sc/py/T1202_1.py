from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T1202_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T1202_1 ._SN',
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
        "Function_1_90C",          # 01, 1
        "Function_2_948",          # 02, 2
        "Function_3_980",          # 03, 3
        "Function_4_9B8",          # 04, 4
        "Function_5_9F0",          # 05, 5
        "Function_6_A28",          # 06, 6
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    RemoveParty(0x46, 0xFF)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, -1350, 0, 6540, 0)
    SetChrPos(0x101, -1550, 0, 5470, 0)
    SetChrPos(0xF7, -2700, 0, 5320, 0)
    SetChrPos(0xF8, -1170, 0, 4200, 0)
    SetChrPos(0xF9, -2410, 0, 3740, 0)
    OP_43(0x16, 0x0, 0x1, 0x1)
    Sleep(100)
    OP_43(0x101, 0x0, 0x1, 0x2)
    Sleep(100)
    OP_43(0xF7, 0x0, 0x1, 0x3)
    Sleep(100)
    OP_43(0xF8, 0x0, 0x1, 0x4)
    Sleep(100)
    OP_43(0xF9, 0x0, 0x1, 0x5)
    OP_6D(-1980, 0, 8520, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3240, 0)
    OP_6C(145000, 0)
    OP_6E(262, 0)

    def lambda_18D():
        OP_6D(-1190, 0, 12330, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_18D)
    FadeToBright(2000, 0)
    Sleep(5000)

    def lambda_1B3():
        OP_6D(21820, -4000, 13880, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B3)

    def lambda_1CB():
        OP_6C(45000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1CB)

    def lambda_1DB():
        OP_67(0, 8990, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1DB)
    WaitChrThread(0x101, 0x3)

    def lambda_1F8():
        OP_6C(0, 14000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1F8)
    OP_6B(4000, 4000)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0xF7, 0x0)
    WaitChrThread(0xF8, 0x0)
    WaitChrThread(0xF9, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    Fade(1000)
    OP_44(0x101, 0x3)
    SetChrPos(0x16, 8570, 0, 9930, 90)
    SetChrPos(0x101, 6990, 0, 9850, 92)
    SetChrPos(0xF7, 6630, 0, 11050, 96)
    SetChrPos(0xF8, 6210, 0, 9160, 89)
    SetChrPos(0xF9, 5490, 0, 10320, 93)
    OP_6D(6600, 0, 10880, 0)
    OP_67(0, 6110, -10000, 0)
    OP_6B(3240, 0)
    OP_6C(308000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(    #0
        0x16,
        "原来如此，消息真灵通。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x16,
        (
            "果树园那边\x01",
            "总算也开始重建了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_360")

    ChrTalk(    #2
        0x109,
        (
            "#1060F嗯，看来是的……\x02\x03",

            "虽然重建工作很艰苦，\x01",
            "不过千里之行始于足下……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DC")

    label("loc_360")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3AF")

    ChrTalk(    #3
        0x106,
        (
            "#051F嗯，重建工作很艰苦，\x01",
            "不过已经迈出了重要的第一步呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DC")

    label("loc_3AF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3F8")

    ChrTalk(    #4
        0x103,
        (
            "#020F虽然重建不易，\x01",
            "不过已经迈出了重要的第一步呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DC")

    label("loc_3F8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_45F")

    ChrTalk(    #5
        0x108,
        (
            "#070F嗯，虽然重建十分艰苦，\x01",
            "不过已经迈出了重要的第一步呢。\x02\x03",

            "千里之行始于足下嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DC")

    label("loc_45F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4DC")

    ChrTalk(    #6
        0x104,
        (
            "#030F嗯，虽然重建工作艰苦，\x01",
            "不过已经迈出了重要的第一步呢。\x02\x03",

            "无论田地如何荒芜，\x01",
            "播撒种子后才有可能有收获。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DC")


    ChrTalk(    #7
        0x101,
        (
            "#1000F嗯，也有各种形式的\x01",
            "援助到村子里来了呢。\x02\x03",

            "一定能把村子恢复原状的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x16,
        "嗯，我相信这一点。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x16,
        (
            "我们这些商人\x01",
            "也会想办法为大家出力……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #10
        0x101,
        (
            "#1011F啊，莫非……\x02\x03",

            "米拉诺小姐也是来\x01",
            "支援村子的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x16,
        (
            "想这么愚蠢的事\x01",
            "是会遭报应的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x16,
        (
            "我来这里根本上\x01",
            "就是为了做生意……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x16,
        (
            "总之我先确认了一下\x01",
            "果树园的情况。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x16,
        (
            "当然，有必要的话\x01",
            "我也准备进行『投资』。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x16, 270, 400)

    ChrTalk(    #15
        0x16,
        (
            "──那我就先去\x01",
            "忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        (
            "#1006F啊，嗯。\x02\x03",

            "那就在这里告别吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x16,
        "嗯，是啊。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x15), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7C, 0x1, 0x2000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D7")
    OP_28(0x7C, 0x1, 0x10)
    OP_2B(0x7C, 0x2)
    OP_2C(0x7C, 0x1388)

    label("loc_6D7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7C, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_77E")

    ChrTalk(    #18
        0x16,
        (
            "你们的本事……\x01",
            "很不错啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x16,
        (
            "我已经通知协会\x01",
            "给你们额外奖励了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        "#1004F啊，真的吗……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x16,
        (
            "我干吗要撒\x01",
            "这种谎？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x16,
        "总之，你们就期待着吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7D0")

    label("loc_77E")


    ChrTalk(    #23
        0x16,
        (
            "嗯，你们也算\x01",
            "干得不错了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x16,
        (
            "虽然还没到值得给予\x01",
            "额外奖励的程度，有点遗憾。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D0")


    ChrTalk(    #25
        0x16,
        (
            "那么再见了，回去的\x01",
            "路上要小心哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x101,
        "#1006F您也努力啊。\x02",
    )

    CloseMessageWindow()

    def lambda_815():

        label("loc_815")

        TurnDirection(0xFE, 0x16, 400)
        OP_48()
        Jump("loc_815")

    QueueWorkItem2(0x0, 1, lambda_815)

    def lambda_826():

        label("loc_826")

        TurnDirection(0xFE, 0x16, 400)
        OP_48()
        Jump("loc_826")

    QueueWorkItem2(0x1, 1, lambda_826)

    def lambda_837():

        label("loc_837")

        TurnDirection(0xFE, 0x16, 400)
        OP_48()
        Jump("loc_837")

    QueueWorkItem2(0x2, 1, lambda_837)

    def lambda_848():

        label("loc_848")

        TurnDirection(0xFE, 0x16, 400)
        OP_48()
        Jump("loc_848")

    QueueWorkItem2(0x3, 1, lambda_848)
    OP_43(0x16, 0x0, 0x1, 0x6)
    OP_6D(4800, 0, 14700, 3000)
    Sleep(1000)
    OP_6D(6600, 0, 10880, 2500)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x17, 0x0, 0x64)

    AnonymousTalk(    #27
        "\x07\x02任务【护送商人】\x07\x00完成了！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0xD)
    OP_28(0x7C, 0x1, 0x8)
    OP_28(0x7C, 0x4, 0x10)
    OP_44(0x16, 0x0)
    SetChrPos(0x16, 25990, -4000, 14870, 270)
    OP_43(0x16, 0x0, 0x0, 0x2)
    EventEnd(0x0)
    Return()

    # Function_0_AA end

    def Function_1_90C(): pass

    label("Function_1_90C")

    OP_8E(0x16, 0xFFFFFABA, 0x0, 0x33AE, 0x7D0, 0x0)
    OP_8C(0x16, 180, 400)
    Sleep(1000)
    OP_8C(0x16, 90, 400)
    Sleep(1000)
    OP_94(0x1, 0x16, 0xF, 0xFA0, 0x7D0, 0x0)
    Return()

    # Function_1_90C end

    def Function_2_948(): pass

    label("Function_2_948")

    OP_8E(0x101, 0xFFFFF9F2, 0x0, 0x2D3C, 0x7D0, 0x0)
    Sleep(2500)
    OP_8C(0x101, 90, 400)
    Sleep(2000)
    OP_A6(0xC)
    OP_94(0x1, 0x101, 0x0, 0xBB8, 0x7D0, 0x0)
    Return()

    # Function_2_948 end

    def Function_3_980(): pass

    label("Function_3_980")

    OP_8E(0xF7, 0xFFFFF574, 0x0, 0x2BB6, 0x7D0, 0x0)
    Sleep(2500)
    OP_8C(0xF7, 90, 400)
    Sleep(2000)
    OP_A6(0xC)
    OP_94(0x1, 0xF7, 0x0, 0xBB8, 0x7D0, 0x0)
    Return()

    # Function_3_980 end

    def Function_4_9B8(): pass

    label("Function_4_9B8")

    OP_8E(0xF8, 0xFFFFFB6E, 0x0, 0x2936, 0x7D0, 0x0)
    Sleep(2500)
    OP_8C(0xF8, 90, 400)
    Sleep(2000)
    OP_A6(0xC)
    OP_94(0x1, 0xF8, 0x0, 0xBB8, 0x7D0, 0x0)
    Return()

    # Function_4_9B8 end

    def Function_5_9F0(): pass

    label("Function_5_9F0")

    OP_8E(0xF9, 0xFFFFF696, 0x0, 0x2738, 0x7D0, 0x0)
    Sleep(2500)
    OP_8C(0xF9, 90, 400)
    Sleep(2000)
    OP_A2(0xC)
    OP_94(0x1, 0xF9, 0x0, 0xBB8, 0x7D0, 0x0)
    Return()

    # Function_5_9F0 end

    def Function_6_A28(): pass

    label("Function_6_A28")

    OP_8E(0x16, 0x1662, 0x0, 0x3656, 0x7D0, 0x0)
    OP_8E(0x16, 0x104, 0x0, 0x6E3C, 0x7D0, 0x0)
    Return()

    # Function_6_A28 end

    SaveToFile()

Try(main)
