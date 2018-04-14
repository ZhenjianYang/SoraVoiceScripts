from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3130   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3130.x',
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '皮克塞恩教区长',                       # 9
        '修女琪爱拉',                           # 10
        '莱恩',                                 # 11
        '艾妲',                                 # 12
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
        'ED6_DT07/CH01400 ._CH',             # 00
        'ED6_DT07/CH01410 ._CH',             # 01
        'ED6_DT07/CH01450 ._CH',             # 02
        'ED6_DT07/CH01030 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT07/CH01400P._CP',             # 00
        'ED6_DT07/CH01410P._CP',             # 01
        'ED6_DT07/CH01450P._CP',             # 02
        'ED6_DT07/CH01030P._CP',             # 03
    )

    DeclNpc(
        X                   = 59010,
        Z                   = 1000,
        Y                   = 52150,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 56310,
        Z                   = 1000,
        Y                   = 50360,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 59970,
        Z                   = 0,
        Y                   = 43850,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 59010,
        Z                   = 1000,
        Y                   = 50160,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )


    DeclActor(
        TriggerX            = 58950,
        TriggerZ            = 1000,
        TriggerY            = 50290,
        TriggerRange        = 400,
        ActorX              = 58800,
        ActorZ              = 2500,
        ActorY              = 52200,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_16E",          # 00, 0
        "Function_1_1F1",          # 01, 1
        "Function_2_1F2",          # 02, 2
        "Function_3_1F7",          # 03, 3
        "Function_4_10EF",         # 04, 4
        "Function_5_160D",         # 05, 5
        "Function_6_193F",         # 06, 6
    )


    def Function_0_16E(): pass

    label("Function_0_16E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_17D")
    SetChrFlags(0xA, 0x80)
    Jump("loc_1F0")

    label("loc_17D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_198")
    SetChrPos(0xA, 62680, 0, 45050, 0)
    Jump("loc_1F0")

    label("loc_198")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_1D3")
    SetChrFlags(0x8, 0x10)
    SetChrPos(0xB, 56190, 0, 46550, 0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x10)
    SetChrPos(0xA, 62680, 0, 45050, 0)
    Jump("loc_1F0")

    label("loc_1D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_1F0")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xA, 62680, 0, 45050, 0)

    label("loc_1F0")

    Return()

    # Function_0_16E end

    def Function_1_1F1(): pass

    label("Function_1_1F1")

    Return()

    # Function_1_1F1 end

    def Function_2_1F2(): pass

    label("Function_2_1F2")

    Call(0, 3)
    Return()

    # Function_2_1F2 end

    def Function_3_1F7(): pass

    label("Function_3_1F7")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_338")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D7")

    ChrTalk(    #0
        0x8,
        (
            "导力器无法使用的话，\x01",
            "保安方面也有很大问题啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "如你所知，导力灯具有\x01",
            "驱散魔兽的效果。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        (
            "以前遭到魔兽侵犯时\x01",
            "王国军都会替我们击退魔兽……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "但那个时候导力器可以使用，\x01",
            "和现在的情况不同啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_335")

    label("loc_2D7")


    ChrTalk(    #4
        0x8,
        (
            "导力器无法使用的话，\x01",
            "保安方面也有很大问题啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        (
            "如你所知，导力灯具有\x01",
            "驱散魔兽的效果。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_335")

    Jump("loc_10EB")

    label("loc_338")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_49C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_434")

    ChrTalk(    #6
        0x8,
        (
            "异变发生之后\x01",
            "引起了很大的混乱……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "不过城里的状况总算是\x01",
            "稍微安定下来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "对城里的居民来说，导力器的意义\x01",
            "已经不止是一个普通的机械了，\x01",
            "因此出现这么大的骚乱也不奇怪。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        (
            "虽然技术力的不断进步，\x01",
            "这里也发展得越来越快了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_499")

    label("loc_434")


    ChrTalk(    #10
        0x8,
        (
            "对城里的居民来说，导力器的意义\x01",
            "已经不止是一个普通的机械了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        "因此引发这么大的混乱也不奇怪。\x02",
    )

    CloseMessageWindow()

    label("loc_499")

    Jump("loc_10EB")

    label("loc_49C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x285, 0)), scpexpr(EXPR_END)), "loc_998")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_94D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_58F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_518")

    ChrTalk(    #12
        0x8,
        (
            "清楚认识到自己能力的不足\x01",
            "也是迈上成功之道的第一步。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        (
            "只要相信神\x01",
            "一切就都会有希望。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58C")

    label("loc_518")


    ChrTalk(    #14
        0x8,
        (
            "愿女神可以保佑\x01",
            "别再发生地震了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        (
            "希望我的祈祷\x01",
            "能管用啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        (
            "我们要清楚地认识到\x01",
            "自己能力的不足才行。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_58C")

    Jump("loc_94A")

    label("loc_58F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_5CC")

    ChrTalk(    #17
        0x8,
        "空之女神啊！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        (
            "愿女神永远\x01",
            "引导保护我们……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_94A")

    label("loc_5CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_END)), "loc_781")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_629")
    TurnDirection(0x8, 0x107, 0)

    ChrTalk(    #19
        0x8,
        "那么，你们就加油吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x8,
        (
            "如果有什么困难的话\x01",
            "随时可以到这里来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_77E")

    label("loc_629")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_660")

    ChrTalk(    #21
        0x8,
        "啊，提妲。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        "又在帮博士的忙吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_6A7")

    label("loc_660")

    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x8, 0x107, 0)

    ChrTalk(    #23
        0x8,
        "呀，提妲也在啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        "又在帮博士的忙吗？\x02",
    )

    CloseMessageWindow()

    label("loc_6A7")


    ChrTalk(    #25
        0x107,
        (
            "#560F啊…嗯，是啊。\x02\x03",

            "只是设置测量仪而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        "嗯，真让人佩服。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x8,
        (
            "下次主日学校的课\x01",
            "一定要再来听哦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        (
            "只要有你在，\x01",
            "大家就都充满活力了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x107,
        (
            "#067F嘿嘿嘿……\x01",
            "是，我知道啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x8,
        (
            "那么，你就\x01",
            "继续加油吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_77E")

    Jump("loc_94A")

    label("loc_781")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_879")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_7E0")

    ChrTalk(    #31
        0x8,
        (
            "最近修女琪爱拉\x01",
            "一直很热心帮忙呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x8,
        (
            "她似乎理解了社会活动\x01",
            "的重要性了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_876")

    label("loc_7E0")


    ChrTalk(    #33
        0x8,
        (
            "提供医疗服务\x01",
            "是礼拜堂的重要作用。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x8,
        (
            "不管是心中的苦闷还是身体上的伤痛\x01",
            "都需要别人来抚平。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x8,
        (
            "只有将这两种痛苦全部消除\x01",
            "才能算是真正的拯救。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_876")

    Jump("loc_94A")

    label("loc_879")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_END)), "loc_94A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_8D8")

    ChrTalk(    #36
        0x8,
        (
            "虽然只是小型地震，\x01",
            "但也许会有人受伤，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x8,
        (
            "还是要事先把伤药\x01",
            "准备好才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_94A")

    label("loc_8D8")


    ChrTalk(    #38
        0x8,
        (
            "嗯，刚才的摇晃\x01",
            "似乎是地震啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x8,
        (
            "虽然震动不算大，\x01",
            "但也许会有人受伤，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x8,
        (
            "还是要事先把伤药\x01",
            "准备好才行。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_94A")

    Jump("loc_995")

    label("loc_94D")


    ChrTalk(    #41
        0x8,
        (
            "如果有事\x01",
            "那就请再来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x8,
        (
            "如果有需要的话，\x01",
            "随时可以来找我商谈哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_995")

    Jump("loc_10EB")

    label("loc_998")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_CCB")

    ChrTalk(    #43
        0x8,
        "啊，你们是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x101,
        (
            "#1025F啊～教区长先生。\x02\x03",

            "#1007F那……那个时候\x01",
            "真是～多亏了您的帮忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x106,
        "#552F……多亏您的照顾了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x106, 400)

    ChrTalk(    #46
        0x8,
        (
            "喔喔，看样子你已经\x01",
            "完全康复了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x8,
        (
            "没想到竟然恢复得这么快，\x01",
            "看来完全不用担心你了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x8,
        (
            "不过，以后也不要蛮干啊。\x01",
            "要小心身体才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x106,
        (
            "#050F嗯，我一定会铭记在心的。\x02\x03",

            "#555F真是的，我又不是小孩子了。\x01",
            "不用那么担心啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x8,
        "嗯，虽然如此，不过呢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x8,
        "你能得救也是多亏了女神的守护，\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x8,
        (
            "今后一定还有需要你完成的\x01",
            "使命在等着你的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x8,
        (
            "所以，你可是有用之身，\x01",
            "不能轻易就犯险乱来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x8,
        (
            "这也是\x01",
            "我对你的一点希望。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x106,
        "#552F…………………………\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #56
        0x8,
        "……哎呀，我这人真是的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x8,
        (
            "只是救过你一次，\x01",
            "就非要让你听这么多说教。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)

    ChrTalk(    #58
        0x8,
        "那么，欢迎以后再来。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x8,
        (
            "如果有需要的话，\x01",
            "有问题随时都可以找我商量。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x101,
        (
            "#1000F嗯，谢谢。\x02\x03",

            "那再见啦，教区长先生。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10E5")

    label("loc_CCB")


    ChrTalk(    #61
        0x8,
        "啊，你们是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        (
            "#1025F啊～教区长先生。\x02\x03",

            "#1007F阿加特受伤的时候\x01",
            "真是～多亏了您的帮忙了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #63
        0x103,
        (
            "#023F受……伤？\x01",
            "有那种事吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DE6")

    ChrTalk(    #64
        0x107,
        "#561F嗯，是的……………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #65
        0x101,
        (
            "#1003F中了特务兵的毒弹，\x01",
            "情况非常危险呢。\x02\x03",

            "#1015F嗯，多亏了教区长的药\x01",
            "才能顺利脱险呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ED5")

    label("loc_DE6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E7B")

    def lambda_DFA():
        TurnDirection(0x101, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DFA)
    TurnDirection(0x108, 0x103, 400)

    ChrTalk(    #66
        0x108,
        (
            "#072F嗯，他被有毒的子弹\x01",
            "射中，\x02\x03",

            "当时的情况好像很危险呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x101,
        (
            "#1015F嗯，多亏了教区长的药\x01",
            "才能顺利脱险呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ED5")

    label("loc_E7B")


    ChrTalk(    #68
        0x101,
        (
            "#1003F嗯，被毒弹击伤，\x01",
            "情况非常危险呢。\x02\x03",

            "#1015F嗯，多亏了教区长的药\x01",
            "才能顺利脱险呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ED5")


    ChrTalk(    #69
        0x8,
        (
            "啊，我也只是帮了\x01",
            "一点小忙而已……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #70
        0x8,
        (
            "对了，他现在怎么样了？\x01",
            "已经彻底痊愈了吧？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F4E")

    def lambda_F46():
        TurnDirection(0x108, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_F46)

    label("loc_F4E")

    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #71
        0x101,
        (
            "#1006F嗯，已经完全恢复了。\x02\x03",

            "他现在和我们\x01",
            "分头行动呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x8,
        (
            "嗯…希望他不要再像\x01",
            "以前那么乱来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x8,
        "他能获救都是因为女神的意志。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x8,
        (
            "这也说明他以后还有\x01",
            "自己应尽的使命……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #75
        0x8,
        "……哎呀，我这人真是的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x8,
        (
            "只是救了他一次，\x01",
            "就要让你们听这么多说教。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x8,
        "那么，欢迎以后再来，\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x8,
        (
            "如果有需要的话，\x01",
            "有问题随时都可以找我商量。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x101,
        (
            "#1000F嗯，谢谢。\x02\x03",

            "那，再见啦，教区长先生。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10E5")

    OP_A2(0x1428)
    OP_A2(0x0)

    label("loc_10EB")

    TalkEnd(0x8)
    Return()

    # Function_3_1F7 end

    def Function_4_10EF(): pass

    label("Function_4_10EF")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_1166")

    ChrTalk(    #80
        0xFE,
        (
            "为了预防紧急事态\x01",
            "必须要多制作一些药。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "如果可能的话，我倒更希望\x01",
            "自己的这些努力全部变成无用劳动。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1609")

    label("loc_1166")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_12A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1241")

    ChrTalk(    #82
        0xFE,
        (
            "因为导力器停止而受惊的市民们\x01",
            "都聚集在了中央工房……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "转眼之间，\x01",
            "城里就变得一片混乱了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "但即使大家都聚在一起\x01",
            "也都完全做不了什么……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "……不过这样一来，\x01",
            "也可以认识到自己力量的不足。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_12A3")

    label("loc_1241")


    ChrTalk(    #86
        0xFE,
        (
            "因为导力器停止而受惊的市民们\x01",
            "都聚集在了中央工房……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "转眼之间，\x01",
            "城里好像已经一片骚乱了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12A3")

    Jump("loc_1609")

    label("loc_12A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_1394")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1303")

    ChrTalk(    #88
        0xFE,
        (
            "在教区长看来，\x01",
            "只要求神保佑就ＯＫ了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "呼，女神未免也太\x01",
            "宽容了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1391")

    label("loc_1303")


    ChrTalk(    #90
        0xFE,
        (
            "在教区长看来，\x01",
            "只要求神保佑就ＯＫ了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "虽然从某种意义上说\x01",
            "我可以理解他们的做法……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "可是，不管怎么说\x01",
            "从心情上也没办法接受呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1391")

    Jump("loc_1609")

    label("loc_1394")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_1497")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_13E7")

    ChrTalk(    #93
        0xFE,
        (
            "只有在遇到困难的时候\x01",
            "才来祈祷……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "未免也太\x01",
            "不虔诚了吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1494")

    label("loc_13E7")


    ChrTalk(    #95
        0xFE,
        (
            "来做礼拜的人\x01",
            "最近急剧增多了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        (
            "大家都是希望地震不要再来\x01",
            "才来向女神祈祷的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "虽然教区长总是一脸笑容\x01",
            "地欢迎他们，不过……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "我还是觉得这样子\x01",
            "太不虔诚了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1494")

    Jump("loc_1609")

    label("loc_1497")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_1560")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_14FC")

    ChrTalk(    #99
        0xFE,
        (
            "不管任何困难也要克服，\x01",
            "努力为他人解决困难。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "教区长这种想法\x01",
            "实在是很伟大。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_155D")

    label("loc_14FC")


    ChrTalk(    #101
        0xFE,
        (
            "研制药品的处方\x01",
            "也是教会的重要职责。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "开始的时候还有些抵触，\x01",
            "但现在已经完全没问题了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_155D")

    Jump("loc_1609")

    label("loc_1560")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_END)), "loc_1609")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_15B6")

    ChrTalk(    #103
        0xFE,
        "城里那边没什么问题……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        (
            "嗯，比起那个\x01",
            "我更加担心中央工房呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1609")

    label("loc_15B6")


    ChrTalk(    #105
        0xFE,
        (
            "虽然震动很小，\x01",
            "但毕竟也是场地震啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "我来到这里之后\x01",
            "还是第一次发生呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1609")

    TalkEnd(0x9)
    Return()

    # Function_4_10EF end

    def Function_5_160D(): pass

    label("Function_5_160D")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_1724")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_167A")

    ChrTalk(    #107
        0xFE,
        "呜～今天要通宵工作了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        (
            "呼，果然，对宗教的热情\x01",
            "和现实社会的生活是密不可分的啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1721")

    label("loc_167A")


    ChrTalk(    #109
        0xFE,
        "听过中央工房发表的声明了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "只要虔诚祈祷的话\x01",
            "地震就会停止的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        "喔，还有……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        (
            "在祈祷的时候，\x01",
            "我的工作就要先放下了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        "啊啊，工作怎么办呢……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1721")

    Jump("loc_193B")

    label("loc_1724")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_17DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1787")

    ChrTalk(    #114
        0xFE,
        (
            "大家都来祈祷\x01",
            "地震不要再发生呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "虽然要耽误工作，\x01",
            "但我也不能自己先回去。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17DA")

    label("loc_1787")


    ChrTalk(    #116
        0xFE,
        (
            "大家都来祈祷\x01",
            "地震不要再发生呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "在这种时候，\x01",
            "情绪也受到大家的影响了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_17DA")

    Jump("loc_193B")

    label("loc_17DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_1882")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_183A")

    ChrTalk(    #118
        0xFE,
        (
            "好了，在回去工作之前\x01",
            "先认真祈祷吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "啊啊～希望地震\x01",
            "不要再来了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_187F")

    label("loc_183A")


    ChrTalk(    #120
        0xFE,
        (
            "今天来礼拜堂的人\x01",
            "好像很多啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        (
            "大家都来祈祷\x01",
            "真让人吃惊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_187F")

    Jump("loc_193B")

    label("loc_1882")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_END)), "loc_193B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_18D8")

    ChrTalk(    #122
        0xFE,
        (
            "难得来一次教会，\x01",
            "却都在祈祷同一件事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        "让地震不要再来了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_193B")

    label("loc_18D8")


    ChrTalk(    #124
        0xFE,
        (
            "呼，看来是被刚才的地震\x01",
            "吓得太厉害吧～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        (
            "虽然还在工作中，但想也没想\x01",
            "就直接跑到教会来了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_193B")

    TalkEnd(0xA)
    Return()

    # Function_5_160D end

    def Function_6_193F(): pass

    label("Function_6_193F")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_199E")

    ChrTalk(    #126
        0xFE,
        (
            "伟大的女神啊……\x01",
            "请让地震不要再发生了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        (
            "还有，感谢您\x01",
            "总是赐予我们良药。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AA0")

    label("loc_199E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_1AA0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1A09")

    ChrTalk(    #128
        0xFE,
        (
            "好了，今天就好好\x01",
            "祈祷一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "希望地震不要再发生，\x01",
            "女神一定能听到我们的祈愿吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AA0")

    label("loc_1A09")


    ChrTalk(    #130
        0xFE,
        (
            "教区长的药\x01",
            "非常管用啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        (
            "我的肩膀也\x01",
            "彻底治好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "好了，今天就好好\x01",
            "祈祷一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        (
            "希望地震不要再发生，\x01",
            "女神一定能听到我们的祈愿吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_1AA0")

    TalkEnd(0xB)
    Return()

    # Function_6_193F end

    SaveToFile()

Try(main)
