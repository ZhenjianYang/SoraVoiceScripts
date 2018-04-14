from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T0610_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T0610_1 ._SN',
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
        "Function_1_4D9",          # 01, 1
        "Function_2_69F",          # 02, 2
        "Function_3_15E0",         # 03, 3
        "Function_4_198F",         # 04, 4
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    EventBegin(0x0)
    OP_8C(0xD, 250, 0)
    Fade(1000)
    SetChrPos(0x101, -62390, 0, -22680, 270)
    SetChrPos(0x103, -62210, 0, -24020, 315)
    SetChrPos(0xF8, -61170, 0, -23660, 270)
    SetChrPos(0xF9, -61070, 0, -22240, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12B")
    SetChrPos(0xF9, -61170, 0, -23660, 270)
    SetChrPos(0xF8, -61070, 0, -22240, 270)

    label("loc_12B")

    OP_6D(-63450, 0, -21840, 0)
    OP_67(0, 6710, -10000, 0)
    OP_6B(2710, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_1C3")
    SetChrName("拜舍尔")

    ChrTalk(    #0
        0xD,
        (
            "#1P好了……\x01",
            "总算雾散天晴了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xD,
        (
            "#1P我也还差不多该\x01",
            "准备出发了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DA")

    label("loc_1C3")


    ChrTalk(    #2
        0xD,
        "#1P唉……真没劲。\x02",
    )

    CloseMessageWindow()

    label("loc_1DA")


    ChrTalk(    #3
        0x101,
        "#1015F#2P嗯～打扰一下行吗？\x02",
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0xD)
    TurnDirection(0xD, 0x101, 400)

    ChrTalk(    #4
        0xD,
        "#1P嗯？什么事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        (
            "#1011F#2P我们是协会\x01",
            "派来的……\x02\x03",

            "您是发出委托的\x01",
            "拜舍尔先生？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xD,
        "#1P哦，没错。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xD,
        (
            "#1P太好了。\x01",
            "终于来了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        (
            "#1006F#2P嗯，总之\x01",
            "先来听听需要委托的是什么事吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x103,
        (
            "#020F公告板上看来\x01",
            "您好像是要委托调查什么吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #10
        0xD,
        (
            "#1P啊啊，其实是想委托\x01",
            "调查洛连特地区的钓鱼地点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xD,
        (
            "#1P详细的过程\x01",
            "我稍后再进行说明……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xD,
        (
            "#1P……那，怎样？\x01",
            "能帮忙吗？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3EA")
    Call(1, 2)
    Jump("loc_4D6")

    label("loc_3EA")


    ChrTalk(    #13
        0x101,
        (
            "#1007F#2P唔……\x01",
            "十分抱歉……\x02\x03",

            "很遗憾，现在\x01",
            "没办法马上接受。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #14
        0xD,
        "#1P哎呀……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xD,
        (
            "#1P有什么紧急的\x01",
            "工作在手吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x103,
        (
            "#025F嗯嗯，抱歉哦。\x02\x03",

            "有空了\x01",
            "会再来的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #17
        0xD,
        "#1P嗯，那也没问题。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xD,
        "#1P那么，以后再麻烦你们。\x02",
    )

    CloseMessageWindow()
    OP_28(0x73, 0x1, 0x8000)

    label("loc_4D6")

    EventEnd(0x0)
    Return()

    # Function_0_AA end

    def Function_1_4D9(): pass

    label("Function_1_4D9")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -62390, 0, -22680, 270)
    SetChrPos(0x103, -62210, 0, -24020, 315)
    SetChrPos(0xF8, -61170, 0, -23660, 270)
    SetChrPos(0xF9, -61070, 0, -22240, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_553")
    SetChrPos(0xF9, -61170, 0, -23660, 270)
    SetChrPos(0xF8, -61070, 0, -22240, 270)

    label("loc_553")

    TurnDirection(0xD, 0x101, 0)
    OP_6D(-63450, 0, -21840, 0)
    OP_67(0, 6710, -10000, 0)
    OP_6B(2710, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(    #19
        0xD,
        "#1P哦，游击士们。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xD,
        (
            "#1P钓鱼地点的调查，\x01",
            "能接受了吗？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_62D")
    Call(1, 2)
    Jump("loc_69C")

    label("loc_62D")


    ChrTalk(    #21
        0x101,
        (
            "#1007F#2P抱歉……\x01",
            "还不行呢。\x02\x03",

            "有空了\x01",
            "我们马上回来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xD,
        "#1P怎么，还不行啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xD,
        "#1P那，以后再麻烦你们。\x02",
    )

    CloseMessageWindow()

    label("loc_69C")

    EventEnd(0x0)
    Return()

    # Function_1_4D9 end

    def Function_2_69F(): pass

    label("Function_2_69F")


    ChrTalk(    #24
        0x101,
        (
            "#1006F#2P这点小事没问题的。\x01",
            "交给我们吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #25
        0xD,
        "#1P呀～太感谢了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xD,
        (
            "#1P果然有困难就是\x01",
            "要找游击士啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        (
            "#1015F#2P不过，为什么\x01",
            "要调查什么钓鱼地点呢？\x02\x03",

            "还特地付酬金……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xD,
        (
            "#1P啊啊，其实我是\x01",
            "『钓公师团』的团员。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xD,
        (
            "#1P预计很快就要和同伴们\x01",
            "开个钓鱼的讲习会了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xD,
        (
            "#1P于是就在候补场地洛连特地区\x01",
            "先调查一下情况。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_826")

    ChrTalk(    #31
        0x104,
        (
            "#030F嗬，钓鱼的讲习会啊。\x01",
            "听起来真讲究。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_914")

    label("loc_826")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_871")

    ChrTalk(    #32
        0x108,
        (
            "#070F噢，钓鱼的讲习会啊。\x02\x03",

            "我要是有机会\x01",
            "也想参加呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_914")

    label("loc_871")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8D2")

    ChrTalk(    #33
        0x106,
        (
            "#052F啊啊，有这样的事啊。\x02\x03",

            "听起来更像是同好的聚会，\x01",
            "活动还挺像那么回事呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_914")

    label("loc_8D2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_914")

    ChrTalk(    #34
        0x107,
        (
            "#560F钓鱼的讲习会啊～\x02\x03",

            "嘿嘿，我也\x01",
            "想学学看呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_914")


    ChrTalk(    #35
        0xD,
        "#1P嘿嘿，不错的计划吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xD,
        (
            "#1P在王都也是盛况空前啦，\x01",
            "接下来打算办得更热闹哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xD,
        (
            "#1P本来这个调查\x01",
            "打算自己做的……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_9D5")

    ChrTalk(    #38
        0xD,
        (
            "#1P但是由于这雾耽误了时间。\x01",
            "于是就打算拜托专业人士了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A07")

    label("loc_9D5")


    ChrTalk(    #39
        0xD,
        (
            "#1P不巧起了这雾。\x01",
            "于是就打算拜托专业人士了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A07")


    ChrTalk(    #40
        0x103,
        (
            "#020F……原来如此。\x01",
            "调查的目的明白了。\x02\x03",

            "那么，具体来说\x01",
            "怎么调查才好？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #41
        0xD,
        (
            "#1P啊啊，想拜托大家的就是\x01",
            "确认一下钓鱼地点的位置。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xD,
        (
            "#1P哪里能钓到鱼，\x01",
            "报告这个就可以了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        (
            "#1015F#2P嗯～这也就是说……\x02\x03",

            "#1000F找个看起来不错的水边，\x01",
            "试着钓１条就行了？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #44
        0xD,
        "#1P哦，没错了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xD,
        (
            "#1P你看起来好像很高兴，\x01",
            "难不成也是钓鱼迷？\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0x12, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BA2")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BA2")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0x12, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BEB")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BEB")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0x12, 0x2, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C34")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C34")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0x12, 0x3, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C7D")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C7D")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0x12, 0x4, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CC6")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CC6")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0x12, 0x5, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D0F")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D0F")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0x12, 0x6, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D58")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D58")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0x12, 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DA1")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DA1")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0x12, 0x8, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DEA")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DEA")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0x12, 0x9, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E33")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E33")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0x12, 0xA, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E7C")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E7C")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0x12, 0xB, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EC5")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_EC5")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0x12, 0xC, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F0E")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F0E")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0x12, 0xD, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F57")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F57")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0x12, 0xE, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FA0")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FA0")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0x12, 0xF, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FE9")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FE9")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0x12, 0x10, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1032")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1032")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0x12, 0x11, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_107B")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_107B")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0x12, 0x12, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10C4")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10C4")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0x12, 0x13, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_110D")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_110D")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0x12, 0x14, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1156")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1156")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0x12, 0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_119F")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_119F")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0x12, 0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11E8")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_11E8")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0x12, 0x17, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1231")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1231")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0x12, 0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_127A")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_127A")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0x12, 0x19, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_12C3")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12C3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_12D3")
    OP_A2(0xB)

    label("loc_12D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1369")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "◇经常钓的（其实是用钓鱼系统分歧）\x01",        # 0
            "◇几乎没钓过（其实是用钓鱼系统分歧）\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1369")
    OP_A2(0xB)

    label("loc_1369")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_13DD")

    ChrTalk(    #46
        0x101,
        (
            "#1001F#2P嘿嘿，算是吧⊙\x02\x03",

            "工作就是钓鱼，\x01",
            "还真没想到。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xD,
        (
            "#1P咦～没想到游击士里\x01",
            "也有同样兴趣的人啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1445")

    label("loc_13DD")


    ChrTalk(    #48
        0x101,
        (
            "#1003F#2P嗯～喜欢\x01",
            "倒是喜欢……\x02\x03",

            "#1007F不过最近很忙，\x01",
            "几乎都没怎么钓了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xD,
        "#1P哈哈，真是可怜啊。\x02",
    )

    CloseMessageWindow()

    label("loc_1445")


    ChrTalk(    #50
        0xD,
        (
            "#1P唉，那就趁这次\x01",
            "工作机会歇口气吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xD,
        "#1P钓鱼反正是业余爱好嘛。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x101,
        (
            "#1006F#2P嗯，虽说不能偷懒，\x01",
            "但您这样说真是轻松多了。\x02\x03",

            "那么，我们就立刻\x01",
            "去找钓鱼场了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x103,
        (
            "#020F整理一遍\x01",
            "再回来报告。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #54
        0xD,
        "#1P啊啊，麻烦你们了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xD,
        "#1P那么，小心哦。\x02",
    )

    CloseMessageWindow()
    OP_28(0x73, 0x1, 0x1)
    OP_28(0x73, 0x4, 0x4)
    OP_28(0x73, 0x4, 0x8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x1, 0x400)"), scpexpr(EXPR_END)), "loc_1569")
    OP_28(0x73, 0x1, 0x2)
    OP_28(0x73, 0x1, 0x4)

    label("loc_1569")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x1, 0x800)"), scpexpr(EXPR_END)), "loc_1580")
    OP_28(0x73, 0x1, 0x2)
    OP_28(0x73, 0x1, 0x8)

    label("loc_1580")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x1, 0x1000)"), scpexpr(EXPR_END)), "loc_1597")
    OP_28(0x73, 0x1, 0x2)
    OP_28(0x73, 0x1, 0x10)

    label("loc_1597")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x1, 0x2000)"), scpexpr(EXPR_END)), "loc_15AE")
    OP_28(0x73, 0x1, 0x2)
    OP_28(0x73, 0x1, 0x20)

    label("loc_15AE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x1, 0x4000)"), scpexpr(EXPR_END)), "loc_15C5")
    OP_28(0x73, 0x1, 0x2)
    OP_28(0x73, 0x1, 0x40)

    label("loc_15C5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x1, 0x200)"), scpexpr(EXPR_END)), "loc_15DC")
    OP_28(0x73, 0x1, 0x2)
    OP_28(0x73, 0x1, 0x80)

    label("loc_15DC")

    OP_A2(0x8)
    Return()

    # Function_2_69F end

    def Function_3_15E0(): pass

    label("Function_3_15E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_1623")

    ChrTalk(    #56
        0xD,
        (
            "#1P调查有进展了\x01",
            "再来报告啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xD,
        "#1P哦，那就拜托了！\x02",
    )

    CloseMessageWindow()
    Return()

    label("loc_1623")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -62390, 0, -22680, 270)
    SetChrPos(0x103, -62210, 0, -24020, 315)
    SetChrPos(0xF8, -61170, 0, -23660, 270)
    SetChrPos(0xF9, -61070, 0, -22240, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_169D")
    SetChrPos(0xF9, -61170, 0, -23660, 270)
    SetChrPos(0xF8, -61070, 0, -22240, 270)

    label("loc_169D")

    TurnDirection(0xD, 0x101, 0)
    OP_6D(-63450, 0, -21840, 0)
    OP_67(0, 6710, -10000, 0)
    OP_6B(2710, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_171A")

    ChrTalk(    #58
        0xD,
        "#1P啊，难不成……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xD,
        "#1P就来报告了吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1760")

    label("loc_171A")


    ChrTalk(    #60
        0xD,
        (
            "#1P哦，游击士们。\x01",
            "真是辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xD,
        (
            "#1P那，我来看看\x01",
            "调查的状况。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1760")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #62
        "\x07\x05报告了钓鱼地点的调查状况。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_17BF")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_17BF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_17D4")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_17D4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_17E9")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_17E9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x1, 0x20)"), scpexpr(EXPR_END)), "loc_17FE")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_17FE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x1, 0x40)"), scpexpr(EXPR_END)), "loc_1813")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1813")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x1, 0x80)"), scpexpr(EXPR_END)), "loc_1828")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1828")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_183C")
    Call(1, 4)
    Jump("loc_198C")

    label("loc_183C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1945")

    ChrTalk(    #63
        0xD,
        "#1P嗯～原来如此……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xD,
        (
            "#1P看来调查\x01",
            "是有点进展。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xD,
        (
            "#1P不过，说实话，\x01",
            "希望还能再深入点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x101,
        (
            "#1007F#2P啊……\x02\x03",

            "还不够\x01",
            "达到标准吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xD,
        (
            "#1P嗯，抱歉啦。\x01",
            "就是这意思。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xD,
        (
            "#1P找找看有没有漏下的，\x01",
            "麻烦重新调查一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xD,
        "#1P那么，拜托了！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_198C")

    label("loc_1945")


    ChrTalk(    #70
        0xD,
        (
            "#1P怎么，调查\x01",
            "完全没有进展嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xD,
        (
            "#1P好好调查后\x01",
            "再来报告啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_198C")

    EventEnd(0x0)
    Return()

    # Function_3_15E0 end

    def Function_4_198F(): pass

    label("Function_4_198F")

    OP_62(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0xD)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A5F")
    Sleep(500)
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #72
        0xD,
        "#1P唔唔……这、这是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xD,
        (
            "#1P没、没想到这种地方\x01",
            "居然隐藏着钓鱼场！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xD,
        (
            "#1P这可真厉害啊。\x01",
            "简直是完美的调查结果啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_2B(0x73, 0x2)
    OP_2C(0x73, 0x7D0)
    Jump("loc_1B0B")

    label("loc_1A5F")


    ChrTalk(    #75
        0xD,
        (
            "#1P唔唔……\x01",
            "原来如此，原来如此……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xD,
        (
            "#1P虽然不算完美，\x01",
            "但我看已经调查得够足了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xD,
        (
            "#1P呀～谢谢了。\x01",
            "很努力了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xD,
        (
            "#1P这样出色的调查结果\x01",
            "应该有信心提给总部了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B0B")


    ChrTalk(    #79
        0x101,
        "#1011F#2P这么说……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x103,
        "#020F这样就算完成工作了吧？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #81
        0xD,
        "#1P哦，是啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xD,
        (
            "#1P总而言之，请让我\x01",
            "说声辛苦了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BC0")

    ChrTalk(    #83
        0x104,
        (
            "#034F呼，哎呀哎呀……\x01",
            "总算结束了吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C53")

    label("loc_1BC0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BF1")

    ChrTalk(    #84
        0x107,
        (
            "#067F呼……\x01",
            "终于结束了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C53")

    label("loc_1BF1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C2C")

    ChrTalk(    #85
        0x108,
        (
            "#075F呼，哎呀哎呀……\x01",
            "总算结束了吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C53")

    label("loc_1C2C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C53")

    ChrTalk(    #86
        0x106,
        "#551F终于结束了吗。\x02",
    )

    CloseMessageWindow()

    label("loc_1C53")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C8C")

    ChrTalk(    #87
        0x105,
        (
            "#045F到处跑来跑去\x01",
            "的确是有点累啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D32")

    label("loc_1C8C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CC5")

    ChrTalk(    #88
        0x106,
        (
            "#551F来来回回\x01",
            "还真是转了不少路啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D32")

    label("loc_1CC5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CFE")

    ChrTalk(    #89
        0x108,
        (
            "#070F唔，这工作\x01",
            "比想象的更辛苦啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D32")

    label("loc_1CFE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D32")

    ChrTalk(    #90
        0x107,
        (
            "#067F到处跑来跑去\x01",
            "真是有点累啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_2125")

    ChrTalk(    #91
        0x101,
        (
            "#1015F#2P嗯，确实\x01",
            "够辛苦的……\x02\x03",

            "#1001F不过好久没钓鱼了，\x01",
            "我觉得还挺开心的呢⊙\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x103,
        (
            "#021F呵呵，没想到\x01",
            "好好放松了一下。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #93
        0xD,
        "#1P哦，那就好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xD,
        (
            "#1P委托的报酬\x01",
            "已经给协会了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xD,
        (
            "#1P机会也难得。\x01",
            "顺便也收下这个吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #96
        "\x07\x00得到了\x1F\x53\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x253, 1)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #97
        0x101,
        "#1004F#2P这、这是……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xD,
        (
            "#1P嘿嘿，很棒吧？\x01",
            "这是钓大鱼的特制渔竿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xD,
        (
            "#1P你一定能好好利用的。\x01",
            "代替谢礼送给你吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x101,
        (
            "#1008F#2P可、可以吗？\x01",
            "这么好的东西……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xD,
        "#1P完全可以。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xD,
        (
            "#1P为了发展和普及钓鱼文化，\x01",
            "『钓公师团』可是不惜投资的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xD,
        (
            "#1P哦哟，可不能\x01",
            "再聊下去了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xD,
        (
            "#1P我得带着调查结果\x01",
            "回王都才行啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x101,
        "#1011F#2P啊，是吗……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_200D")

    ChrTalk(    #106
        0x108,
        "#070F那么，路上小心啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2092")

    label("loc_200D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2037")

    ChrTalk(    #107
        0x106,
        "#051F去王都要小心。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2092")

    label("loc_2037")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2063")

    ChrTalk(    #108
        0x104,
        "#030F呼，祝一路顺风。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2092")

    label("loc_2063")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2092")

    ChrTalk(    #109
        0x107,
        "#560F那个，去王都要小心哦。\x02",
    )

    CloseMessageWindow()

    label("loc_2092")


    ChrTalk(    #110
        0xD,
        "#1P那么，就此别过了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xD,
        (
            "#1P今天真是多谢你们了。\x01",
            "今后也要多努力啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xD,
        (
            "#1P有机会要来\x01",
            "王都的总部玩哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x101,
        "#1000F#2P那时就麻烦您了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_24FA")

    label("loc_2125")


    ChrTalk(    #114
        0x101,
        (
            "#1015F#2P嗯，确实\x01",
            "够辛苦的……\x02\x03",

            "不过好久没钓鱼了，\x01",
            "我觉得还挺开心的呢。\x02\x03",

            "#1007F不过，现在可不是\x01",
            "说这种乐观话的时候……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #115
        0xD,
        (
            "#1P是吗，由于这雾，\x01",
            "游击士们也很忙啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xD,
        (
            "#1P这种时候\x01",
            "还给你们添麻烦真抱歉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x103,
        (
            "#020F哪里，别介意。\x02\x03",

            "认真应对委托\x01",
            "是我们的义务。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x101,
        (
            "#1006F#2P对对，\x01",
            "雪拉姐说的对。\x02\x03",

            "多亏了这任务还好好放松了一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xD,
        (
            "#1P哦，谢谢。\x01",
            "这样说我也安心了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xD,
        (
            "#1P那，委托的报酬\x01",
            "就去协会领吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xD,
        (
            "#1P机会也难得。\x01",
            "顺便也收下这个吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #122
        "\x07\x00得到了\x1F\x53\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x253, 1)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #123
        0x101,
        "#1004F#2P这、这是……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xD,
        (
            "#1P嘿嘿，很棒吧？\x01",
            "这是钓大鱼的特制渔竿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xD,
        (
            "#1P你一定能好好利用的。\x01",
            "代替谢礼送给你吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x101,
        (
            "#1008F#2P可、可以吗？\x01",
            "这么好的东西……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xD,
        "#1P完全可以。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xD,
        (
            "#1P为了发展和普及钓鱼文化，\x01",
            "『钓公师团』不惜投资的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xD,
        "#1P那么，就此别过了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xD,
        (
            "#1P今天真是多谢你们了。\x01",
            "今后也要多努力啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x101,
        "#1006F#2P嗯，谢谢！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xD,
        (
            "#1P我也会向女神祈祷\x01",
            "让这雾早点散去的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x103,
        (
            "#020F路上小心哦。\x01",
            "那么，再见。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24FA")


    def lambda_2500():

        label("loc_2500")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_2500")

    QueueWorkItem2(0x101, 3, lambda_2500)

    def lambda_2511():

        label("loc_2511")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_2511")

    QueueWorkItem2(0x103, 3, lambda_2511)

    def lambda_2522():

        label("loc_2522")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_2522")

    QueueWorkItem2(0xF8, 3, lambda_2522)

    def lambda_2533():

        label("loc_2533")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_2533")

    QueueWorkItem2(0xF9, 3, lambda_2533)
    OP_8C(0xD, 0, 400)
    OP_8E(0xD, 0xFFFF0790, 0x0, 0xFFFFAD94, 0x7D0, 0x0)
    OP_8E(0xD, 0xFFFF0DEE, 0x0, 0xFFFFAFCE, 0x7D0, 0x0)
    OP_8C(0xD, 0, 400)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x13)
    OP_73(0x1)
    OP_8E(0xD, 0xFFFF0DEE, 0x0, 0xFFFFB668, 0x7D0, 0x0)
    SetChrFlags(0xD, 0x80)
    Sleep(500)
    OP_72(0x1, 0x800)
    OP_6F(0x1, 19)
    OP_70(0x1, 0x0)
    OP_22(0x7, 0x0, 0x64)
    OP_73(0x1)
    OP_71(0x1, 0x800)
    OP_44(0x101, 0x3)
    OP_44(0x103, 0x3)
    OP_44(0xF8, 0x3)
    OP_44(0xF9, 0x3)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x17, 0x0, 0x64)

    AnonymousTalk(    #134
        "\x07\x02任务【寻找钓鱼场】\x07\x00完成了！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x73, 0x1, 0x100)
    OP_28(0x73, 0x4, 0x10)
    Return()

    # Function_4_198F end

    SaveToFile()

Try(main)
