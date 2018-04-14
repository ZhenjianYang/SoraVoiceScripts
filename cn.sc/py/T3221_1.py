from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T3221_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T3221_1 ._SN',
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
        "Function_1_9B0",          # 01, 1
        "Function_2_B46",          # 02, 2
        "Function_3_251D",         # 03, 3
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x8, 2590, 250, 5360, 180)
    SetChrPos(0x101, 2000, 250, 3320, 0)
    SetChrPos(0x107, 3030, 250, 2920, 0)
    SetChrPos(0xF7, 1910, 250, 1820, 0)
    SetChrPos(0xF9, 3060, 250, 1500, 0)
    OP_6D(1350, 250, 4070, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x290, 2)), scpexpr(EXPR_END)), "loc_27B")

    ChrTalk(    #0
        0x8,
        (
            "#683F哎呀，你们几个。\x02\x03",

            "今天又凑在一起\x01",
            "怎么了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x101,
        (
            "#1001F嗯，当然是\x01",
            "来投宿的！\x02\x03",

            "#1007F……真想早点有机会\x01",
            "能这么说啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1F6")

    ChrTalk(    #2
        0x106,
        (
            "#050F#1P很遗憾，今天也是为了工作。\x02\x03",

            "我们看了告示板，\x01",
            "这里好像发生什么问题。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_249")

    label("loc_1F6")


    ChrTalk(    #3
        0x103,
        (
            "#020F#1P很遗憾，今天也是为了工作。\x02\x03",

            "我们看了告示板，\x01",
            "这里好像发生什么问题了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_249")


    ChrTalk(    #4
        0x8,
        (
            "#682F告示板……\x02\x03",

            "就是说我联络协会的事吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_802")

    label("loc_27B")

    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0x8)

    ChrTalk(    #5
        0x8,
        (
            "#680F哟，你们来了啊。\x01",
            "咦，提妲也在。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x107,
        "#061F您好，婆婆。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x101,
        "#1001F#1P毛婆婆，好久不见。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "#681F嗯，艾丝蒂尔，好久不见。\x02\x03",

            "与以前来的时候相比\x01",
            "一下子变得更像大人了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        "#1008F#1P嘿嘿……是吗。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_71F")

    ChrTalk(    #10
        0x104,
        "#035F老板娘，上回有劳你了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x104, 400)

    ChrTalk(    #11
        0x8,
        (
            "#683F哎呀，我还以为是谁呢，\x01",
            "这不是奥利维尔吗？\x02\x03",

            "怎么你也来了？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_3FB():
        TurnDirection(0x107, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_3FB)
    Sleep(100)

    def lambda_40E():
        TurnDirection(0x101, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_40E)
    Sleep(200)
    TurnDirection(0xF7, 0x104, 400)

    ChrTalk(    #12
        0x107,
        "#064F啊……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x104,
        (
            "#031F呵呵，这里头有些缘故。\x02\x03",

            "现在我作为协力人员\x01",
            "和他们一起行动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        "#1004F#1P你、你们认识？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #15
        0x8,
        (
            "#680F嗯，不久前他\x01",
            "在这里住宿过。\x02\x03",

            "#685F我还是第一次看到有客人\x01",
            "在澡堂里弹琴呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(100)
    OP_62(0x107, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(100)
    OP_62(0xF7, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_579")

    ChrTalk(    #16
        0x106,
        (
            "#551F#1P无论到哪里\x01",
            "都会做同样的事啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A8")

    label("loc_579")


    ChrTalk(    #17
        0x103,
        (
            "#025F#1P唉，无论到哪里\x01",
            "都会做同样的事啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A8")


    ChrTalk(    #18
        0x104,
        (
            "#031F这是我们艺术家的宿命。\x02\x03",

            "对为美的女神服务的人来说\x01",
            "时间和空间根本就是无关紧要的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x101,
        (
            "#1007F#1P就算这样全裸\x01",
            "状态下弹琴也太那个什么了。\x02\x03",

            "#1013F啊……不好……\x01",
            "在脑中想象了一下。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #20
        0x107,
        "#562F姐、姐姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        (
            "#680F反正无论如何，\x01",
            "你能喜欢我很高兴。\x02\x03",

            "这样的话大家\x01",
            "一起住下来怎么样？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6E2():
        TurnDirection(0xF7, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_6E2)
    Sleep(100)

    def lambda_6F5():
        TurnDirection(0x101, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6F5)
    Sleep(150)

    def lambda_708():
        TurnDirection(0x104, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_708)
    Sleep(50)
    TurnDirection(0x107, 0x8, 400)
    Jump("loc_766")

    label("loc_71F")


    ChrTalk(    #22
        0x8,
        (
            "#680F话虽这么说，难得\x01",
            "大家都来了\x02\x03",

            "既然这样好好歇息\x01",
            "一晚上怎么样？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_766")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_7A1")

    ChrTalk(    #23
        0x106,
        (
            "#050F#1P我倒是想这样，\x01",
            "不过不是还有工作吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7D2")

    label("loc_7A1")


    ChrTalk(    #24
        0x103,
        (
            "#020F#1P我倒是想这样，\x01",
            "不过不是还有工作吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D2")


    ChrTalk(    #25
        0x8,
        (
            "#680F工作……\x02\x03",

            "就是说我联络协会的事吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1482)

    label("loc_802")


    ChrTalk(    #26
        0x101,
        (
            "#1002F#1P嗯，就是那个。\x02\x03",

            "好像是说有\x01",
            "偷窥犯出现什么的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x8,
        (
            "#682F嗯，很有可能有。\x02\x03",

            "如果你们方便的话，\x01",
            "希望你们马上展开调查……\x02\x03",

            "你们有时间吗？\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_91A")

    ChrTalk(    #28
        0x101,
        "#1006F#1P嗯，没问题。\x02",
    )

    CloseMessageWindow()
    OP_28(0x70, 0x4, 0x8)
    OP_28(0x70, 0x1, 0x1)
    OP_28(0x70, 0x1, 0x2)
    Call(1, 2)
    Jump("loc_9AF")

    label("loc_91A")


    ChrTalk(    #29
        0x101,
        (
            "#1007F#1P抱歉，现在暂时还不行。\x02\x03",

            "#1002F我们很快会回来的，\x01",
            "到时候再拜托你合作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x8,
        (
            "#680F哎呀，是吗。\x02\x03",

            "也没关系，\x01",
            "不过请你们早点回来。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x70, 0x1, 0x8000)
    EventEnd(0x0)
    Return()

    label("loc_9AF")

    Return()

    # Function_0_AA end

    def Function_1_9B0(): pass

    label("Function_1_9B0")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x8, 2590, 250, 5360, 180)
    SetChrPos(0x101, 2000, 250, 3320, 0)
    SetChrPos(0x107, 3030, 250, 2920, 0)
    SetChrPos(0xF7, 1910, 250, 1820, 0)
    SetChrPos(0xF9, 3060, 250, 1500, 0)
    OP_6D(1350, 250, 4070, 0)
    OP_0D()

    ChrTalk(    #31
        0x8,
        (
            "#683F哎呀，你们几个。\x02\x03",

            "已经可以接\x01",
            "这边的工作了吗？\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AD4")

    ChrTalk(    #32
        0x101,
        "#1006F#1P嗯，已经没问题了。\x02",
    )

    CloseMessageWindow()
    OP_28(0x70, 0x4, 0x8)
    Call(1, 2)
    Jump("loc_B45")

    label("loc_AD4")


    ChrTalk(    #33
        0x101,
        (
            "#1007F#1P不，对不起。\x01",
            "还有点困难。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x8,
        (
            "#685F你们好像很忙呢。\x02\x03",

            "#680F也没关系，\x01",
            "不过请你们早点回来。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x70, 0x1, 0x8000)
    EventEnd(0x0)

    label("loc_B45")

    Return()

    # Function_1_9B0 end

    def Function_2_B46(): pass

    label("Function_2_B46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_B74")

    ChrTalk(    #35
        0x106,
        "#050F#1P请马上告诉我们情况吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B9B")

    label("loc_B74")


    ChrTalk(    #36
        0x103,
        (
            "#020F#1P能不能马上\x01",
            "告诉我们情况？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B9B")


    ChrTalk(    #37
        0x8,
        (
            "#682F嗯，好像有人\x01",
            "在偷窥我们的浴场。\x02\x03",

            "最近有好几次\x01",
            "听到女性客人这么说。\x02\x03",

            "我有点在意，\x01",
            "就联系了协会。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #38
        0x101,
        (
            "#1009F#1P唔……\x01",
            "偷窥最差劲了。\x02\x03",

            "发现罪犯的话\x01",
            "一定要他好看。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_CA9")

    ChrTalk(    #39
        0x106,
        (
            "#050F#1P女性客人具体是\x01",
            "怎么说的？\x02\x03",

            "看到过罪犯的样子吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CF3")

    label("loc_CA9")


    ChrTalk(    #40
        0x103,
        (
            "#022F#1P女性客人具体是\x01",
            "怎么说的？\x02\x03",

            "如果有看到过\x01",
            "罪犯的样子就好办了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CF3")


    ChrTalk(    #41
        0x8,
        (
            "#682F不不，没有\x01",
            "那么明确。\x02\x03",

            "充其量只是感觉到有人\x01",
            "或者是听到了响声之类的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D7F")

    ChrTalk(    #42
        0x104,
        (
            "#032F唔，这么说的话\x01",
            "也有可能是误解了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DBD")

    label("loc_D7F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DBD")

    ChrTalk(    #43
        0x105,
        (
            "#042F感觉和响声吗……\x02\x03",

            "也有可能是\x01",
            "误解呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DBD")


    ChrTalk(    #44
        0x8,
        (
            "#682F嗯，一开始\x01",
            "我也这么认为。\x02\x03",

            "不过就像刚才所说的，\x01",
            "那样的说法出现过好几次了。\x02\x03",

            "这样一来也没办法简单地\x01",
            "用错觉来解释了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x101,
        (
            "#1015F#1P确实如此……\x01",
            "这倒是有点为难。\x02\x03",

            "也不知道算不算是案件，\x01",
            "这样子根本没法调查啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_F10")

    ChrTalk(    #46
        0x106,
        (
            "#053F#1P既然情况不明了，\x01",
            "就只能先试验一下了。\x02\x03",

            "无论怎样，这一类的罪犯\x01",
            "如果不当场抓捕的话是很难将其逮捕的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F7C")

    label("loc_F10")


    ChrTalk(    #47
        0x103,
        (
            "#026F#1P既然情况不明了，\x01",
            "就只能先实际试验一下了。\x02\x03",

            "无论怎样，这一类的案件\x01",
            "不当场抓捕的话是很难侦破的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F7C")


    def lambda_F82():
        TurnDirection(0x107, 0xF7, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_F82)
    Sleep(50)

    def lambda_F95():
        TurnDirection(0x101, 0xF7, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F95)
    Sleep(100)
    TurnDirection(0xF9, 0xF7, 400)

    ChrTalk(    #48
        0x107,
        (
            "#064F试验……\x02\x03",

            "到底要试验什么？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF7, 0x107, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_100D")

    ChrTalk(    #49
        0x106,
        (
            "#050F#1P这还用问。\x02\x03",

            "当然是去实地洗澡了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1041")

    label("loc_100D")


    ChrTalk(    #50
        0x103,
        (
            "#021F#1P呵呵，这还用问。\x02\x03",

            "当然是我们去洗澡了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1041")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_14ED")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1283")
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #51
        0x101,
        (
            "#1004F#1P用自己做诱饵\x01",
            "引蛇出洞！？\x02\x03",

            "#1015F我、我倒是没关系……\x02\x03",

            "感觉还是有\x01",
            "些问题的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x105,
        "#540F……………………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF7, 0x105, 400)

    ChrTalk(    #53
        0x106,
        (
            "#050F#1P我不会勉强你们的。\x02\x03",

            "#053F不过，你们愿意帮忙的话\x01",
            "确实会很有助于调查。\x02\x03",

            "因为诱饵越多\x01",
            "效果就越好。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #54
        0x105,
        (
            "#540F对、对不起……\x01",
            "让你劳心了……\x02\x03",

            "#047F这样的话，\x01",
            "也请让我帮忙。\x02\x03",

            "#045F难得当了协力人员，\x01",
            "我不希望自己帮不上忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x106,
        (
            "#053F#1P太好了，不好意思。\x02\x03",

            "#552F说实话，光有这家伙的话\x01",
            "我还担心能不能构成诱饵呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xF7, 400)

    ChrTalk(    #56
        0x101,
        (
            "#1007F#1P是是，对不起。\x01",
            "反正我不够性感。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1398")

    label("loc_1283")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1398")

    ChrTalk(    #57
        0x101,
        (
            "#1004F#1P用自己做诱饵\x01",
            "引蛇出洞！？\x02\x03",

            "#1015F不，我倒是\x01",
            "没什么关系……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x106,
        (
            "#552F#1P虽然能不能构成诱饵还是\x01",
            "相当微妙的事情，不过也没办法。\x02\x03",

            "#053F就尽量拜托你了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x101,
        (
            "#1007F#1P是是，对不起。\x01",
            "反正我不够性感。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x104,
        (
            "#031F呵呵，与其说艾丝蒂尔\x01",
            "性感不如说是健康之美。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1398")


    ChrTalk(    #61
        0x107,
        "#061F嘿嘿……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x107, 400)

    ChrTalk(    #62
        0x101,
        (
            "#1009F#1P啊，过分。\x01",
            "怎么连提妲也笑了！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(    #63
        0x107,
        (
            "#064F……不、不是的！\x02\x03",

            "#560F只、只是感觉\x01",
            "有点高兴。\x02\x03",

            "好久没有和很多人\x01",
            "在一起洗澡了……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #64
        0x101,
        (
            "#1016F#1P很、很多人在一起洗澡……\x02\x03",

            "那个，这好歹也算\x01",
            "是诱饵搜查计划。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF7, 0x8, 400)
    Sleep(400)

    ChrTalk(    #65
        0x106,
        (
            "#051F#1P……那么，\x01",
            "能不能请你借露天浴场给我们？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B84")

    label("loc_14ED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18B2")
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #66
        0x101,
        (
            "#1004F#1P用自己做诱饵\x01",
            "引蛇出洞！？\x02\x03",

            "#1015F我、我和雪拉姐\x01",
            "一起的话倒是没关系……\x02\x03",

            "感觉一小部分里还是有\x01",
            "很严重的问题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x105,
        "#540F……………………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF7, 0x105, 400)

    ChrTalk(    #68
        0x103,
        (
            "#026F#1P不会勉强你们的……\x02\x03",

            "#027F不过，你们愿意帮忙的话\x01",
            "确实会很有助于调查。\x02\x03",

            "热闹一点能\x01",
            "增加诱饵的效果。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #69
        0x105,
        (
            "#540F对、对不起……\x01",
            "让你劳心了……\x02\x03",

            "#047F这样的话，\x01",
            "也请让我帮忙。\x02\x03",

            "#045F难得当了协力人员，\x01",
            "我不希望自己帮不上忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x103,
        (
            "#021F#1P呵呵，感谢你的帮助。\x02\x03",

            "#525F有这点资本的话\x01",
            "诱饵就能够成立了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x107,
        "#061F嘿嘿……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x107, 400)

    ChrTalk(    #72
        0x101,
        (
            "#1011F#1P咦，提妲。\x01",
            "你看起来好像很高兴。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(    #73
        0x107,
        (
            "#560F啊，嗯……\x01",
            "因为我很期待。\x02\x03",

            "好久没有和大家\x01",
            "这样悠闲得在一起了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #74
        0x101,
        (
            "#1016F#1P很、很多人在一起洗澡……\x02\x03",

            "那个，这好歹也算\x01",
            "是诱饵搜查计划。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1805():
        TurnDirection(0xF9, 0x107, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_1805)
    TurnDirection(0xF7, 0x101, 400)

    ChrTalk(    #75
        0x103,
        (
            "#020F#1P虽然，忘记这一点\x01",
            "看上去不是更自然吗？\x02\x03",

            "这回是全女性阵容，\x01",
            "就尽量放松一点吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF7, 0x8, 400)
    Sleep(400)

    ChrTalk(    #76
        0x103,
        (
            "#020F#1P……那么，\x01",
            "能不能请你借露天浴场给我们？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B84")

    label("loc_18B2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B84")
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #77
        0x101,
        (
            "#1004F#1P用自己做诱饵\x01",
            "引蛇出洞！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x103,
        (
            "#020F#1P嗯，总比干等\x01",
            "偷窥犯出现来得好。\x02\x03",

            "#525F你一个人的话虽然有点那个，\x01",
            "加上我和提妲的话\x01",
            "诱饵就绰绰有余了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x101,
        (
            "#1007F#1P是是，对不起。\x01",
            "反正我不够性感。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x104,
        (
            "#031F呵呵，与其说艾丝蒂尔\x01",
            "性感不如说是健康之美。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x107,
        "#061F嘿嘿……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x107, 400)

    ChrTalk(    #82
        0x101,
        (
            "#1009F#1P啊，过分。\x01",
            "怎么连提妲也笑了！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(    #83
        0x107,
        (
            "#064F啊……不、不是的！\x02\x03",

            "#560F只、只是感觉\x01",
            "有点高兴。\x02\x03",

            "好久没有和很多人\x01",
            "在一起洗澡了……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #84
        0x101,
        (
            "#1016F#1P很、很多人在一起洗澡……\x02\x03",

            "那个，这好歹也算\x01",
            "是诱饵搜查计划。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x103,
        (
            "#020F#1P虽然，忘记这一点\x01",
            "看上去不是更自然吗？\x02\x03",

            "就当作临时休假\x01",
            "就尽量放松一点吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF7, 0x8, 400)
    Sleep(400)

    ChrTalk(    #86
        0x103,
        (
            "#020F#1P……那么，\x01",
            "能不能请你借露天浴场给我们？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B84")


    ChrTalk(    #87
        0x8,
        (
            "#681F嗯，尽管用吧。\x02\x03",

            "我会暂时打烊的，\x01",
            "你们四个就好好地泡泡吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1BCE():
        TurnDirection(0x107, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1BCE)
    Sleep(250)

    def lambda_1BE1():
        TurnDirection(0x101, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1BE1)
    Sleep(150)
    TurnDirection(0xF9, 0x8, 400)

    ChrTalk(    #88
        0x107,
        "#061F谢谢毛婆婆。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x101,
        "#1015F#1P嗯，这样就决定了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_20FD")

    ChrTalk(    #90
        0x106,
        (
            "#051F#1P嗯，是啊。\x02\x03",

            "那就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x101,
        "#1004F#1P啊……！？\x02",
    )

    CloseMessageWindow()

    def lambda_1C7D():
        TurnDirection(0x107, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1C7D)

    def lambda_1C8B():
        TurnDirection(0xF9, 0x106, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_1C8B)
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(    #92
        0x101,
        (
            "#1004F#1P拜托我们……\x02\x03",

            "莫非你\x01",
            "不打算洗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x106,
        (
            "#055F#1P啊！？\x01",
            "你说什么呢？\x02\x03",

            "为什么连我\x01",
            "也要去洗澡？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x8,
        (
            "#682F等等等等，\x01",
            "你才是在胡说八道。\x02\x03",

            "不过都到了这里，\x01",
            "我是不会允许你\x01",
            "不去泡露天浴的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D9D")

    ChrTalk(    #95
        0x104,
        (
            "#031F呼～真服了你们。\x02\x03",

            "没什么好\x01",
            "害羞的吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DE8")

    label("loc_1D9D")


    ChrTalk(    #96
        0x101,
        (
            "#1012F#1P是啊是啊。\x01",
            "而且是你提议的。\x02\x03",

            "#1002F……咦，你难道\x01",
            "是在害羞？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DE8")

    OP_62(0x106, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #97
        0x106,
        (
            "#552F#1P我、我可不是害羞。\x02\x03",

            "我只会考虑\x01",
            "工作的事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x8,
        (
            "#685F啊，真要把人给急死了。\x01",
            "别再说那种硬邦邦的事了。\x02\x03",

            "#682F是男人的话就别啰嗦，\x01",
            "乖乖地去泡澡。\x02\x03",

            "来温泉竟然不洗澡？\x01",
            "我怎么能容忍这么愚蠢的事情发生。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x101,
        "#1015F#1P…………我说你啊？\x02",
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x106)

    ChrTalk(    #100
        0x106,
        (
            "#551F#1P啊～你废话真多。\x02\x03",

            "明白了啦。\x01",
            "我去洗还不行啊。\x02\x03",

            "#057F不过，你们几个……\x01",
            "可别忘了自己是在工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x101,
        "#1006F#1P嗯，这你就放心吧。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x107, 400)

    ChrTalk(    #102
        0x101,
        "#1006F#1P……我说？　提妲？\x02",
    )

    CloseMessageWindow()

    def lambda_1FCB():
        TurnDirection(0xF9, 0x107, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_1FCB)
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(    #103
        0x107,
        "#560F嗯、嗯……不用担心。\x02",
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x107, 0x8, 400)

    ChrTalk(    #104
        0x107,
        (
            "#064F……啊，不好！\x02\x03",

            "婆婆，\x01",
            "借我一套毛巾。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x8,
        "#683F哎呀，你忘带了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x107,
        (
            "#063F嗯，我没想到\x01",
            "会来泡澡……\x02\x03",

            "#064F啊，还有香波。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x101,
        (
            "#1016F#1P（嗯、嗯。\x01",
            "她真给当成是洗澡时间了。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x106,
        "#551F#1P（完全……没紧张感呢。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_2505")

    label("loc_20FD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23EF")

    ChrTalk(    #109
        0x104,
        "#035F呼，那我们走吧。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)

    ChrTalk(    #110
        0x101,
        (
            "#1019F#1P……咦，你在这儿\x01",
            "摆好架势干吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 400)

    ChrTalk(    #111
        0x104,
        (
            "#031F哈哈哈。\x01",
            "因为对这个旅馆很熟悉。\x02\x03",

            "我只是在想\x01",
            "要不要给你们带路。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x101,
        (
            "#1007F#1P嘴上这么说……\x02\x03",

            "……实际上准备不声不响地\x01",
            "跟到更衣室里面来吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #113
        0x104,
        (
            "#033F呀………！？\x02\x03",

            "#031F你、你在说什么？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x101,
        (
            "#1019F#1P别以为你一直都能\x01",
            "耍成这一招。\x02\x03",

            "#1007F……所以呢，\x01",
            "雪拉姐你们先去。\x02\x03",

            "我首先押送这家伙\x01",
            "去男澡堂的更衣室。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x104, 400)

    ChrTalk(    #115
        0x103,
        (
            "#021F#1P呵呵，拜托你了。\x02\x03",

            "那么奥利维尔，\x01",
            "不好意思我先行一步了㈱\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x104, 400)

    ChrTalk(    #116
        0x107,
        "#560F露天浴场见。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x104,
        (
            "#035F呵、呵呵……没关系。\x02\x03",

            "我会把这笔帐\x01",
            "留在露天浴场……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x101,
        (
            "#1019F#1P……如果你想这样讨还\x01",
            "肯定饶不了你。\x02\x03",

            "把你当作偷窥犯\x01",
            "押去协会。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #119
        0x104,
        (
            "#034F知、知道了。\x01",
            "我会自重的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2505")

    label("loc_23EF")


    ChrTalk(    #120
        0x103,
        "#020F#1P嗯，那就走吧。\x02",
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x107, 0x8, 400)

    ChrTalk(    #121
        0x107,
        (
            "#064F啊，不行！\x02\x03",

            "婆婆，\x01",
            "借我一套毛巾。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2460():
        TurnDirection(0xF7, 0x107, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_2460)

    def lambda_246E():
        TurnDirection(0xF9, 0x107, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_246E)
    TurnDirection(0x101, 0x107, 400)

    ChrTalk(    #122
        0x8,
        "#683F怎么了，忘了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x107,
        (
            "#063F嗯，我没想到\x01",
            "会来泡澡……\x02\x03",

            "#064F啊，还有香波。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x101,
        (
            "#1016F#1P（嗯、嗯。\x01",
            "她真给当成是洗澡时间了。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2505")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T3200   ._SN", 107, 0, 0)
    IdleLoop()
    Return()

    # Function_2_B46 end

    def Function_3_251D(): pass

    label("Function_3_251D")

    EventBegin(0x0)
    SetChrPos(0x8, 2590, 250, 5360, 180)
    SetChrPos(0x101, 2000, 250, 3320, 0)
    SetChrPos(0x107, 3030, 250, 2920, 0)
    SetChrPos(0xF7, 1910, 250, 1820, 0)
    SetChrPos(0xF9, 3060, 250, 1500, 0)
    OP_6D(1350, 250, 4070, 0)
    OP_4A(0x8, 255)
    OP_0D()

    ChrTalk(    #125
        0x8,
        (
            "#683F#2P──原来如此。\x02\x03",

            "偷窥犯的真身\x01",
            "是魔兽啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_261E")

    ChrTalk(    #126
        0x106,
        (
            "#050F虽然不敢确定，\x01",
            "不过可能性很高。\x02\x03",

            "我们已经教训过它们了，\x01",
            "应该不会再来了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2673")

    label("loc_261E")


    ChrTalk(    #127
        0x103,
        (
            "#020F虽然不敢确定，\x01",
            "不过可能性很高。\x02\x03",

            "我们已经教训过它们了，\x01",
            "应该不会再来了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2673")


    ChrTalk(    #128
        0x101,
        (
            "#1015F#1P不过，一两只\x01",
            "误闯进来还能让人理解……\x02\x03",

            "#1002F一下子来那么多，\x01",
            "你们不觉得有些奇怪吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x8,
        (
            "#682F#2P嗯，我第一次碰到这种事。\x02\x03",

            "可能发生过什么事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x107,
        (
            "#063F说不定……\x01",
            "和地震有关系。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_273A():
        TurnDirection(0x101, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_273A)
    Sleep(150)

    def lambda_274D():
        TurnDirection(0xF7, 0x107, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_274D)
    Sleep(100)
    TurnDirection(0xF9, 0x107, 400)

    ChrTalk(    #131
        0x101,
        "#1004F#1P和地震？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(    #132
        0x107,
        (
            "#063F嗯、嗯，地震有可能\x01",
            "造成魔兽发狂。\x02\x03",

            "居住地的环境如果发生变化，\x01",
            "好像也有可能会这样。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_280F")

    ChrTalk(    #133
        0x105,
        (
            "#042F原来如此……\x01",
            "有道理呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_283D")

    label("loc_280F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_283D")

    ChrTalk(    #134
        0x104,
        (
            "#030F原来如此……\x01",
            "有道理。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_283D")


    ChrTalk(    #135
        0x8,
        (
            "#680F#2P算了，反正如果是自然\x01",
            "造成的话也没办法。\x02\x03",

            "如果再出现的话\x01",
            "先放弃调查，和协会联络吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_28A3():
        OP_8C(0xF7, 0, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_28A3)
    Sleep(150)

    def lambda_28B6():
        OP_8C(0x101, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_28B6)
    Sleep(100)

    def lambda_28C9():
        OP_8C(0xF9, 0, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_28C9)
    Sleep(50)
    OP_8C(0x107, 0, 400)

    ChrTalk(    #136
        0x101,
        (
            "#1006F#1P嗯，应该这么做。\x02\x03",

            "#1001F到时候又能\x01",
            "好好洗澡了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2957")

    ChrTalk(    #137
        0x106,
        (
            "#551F嗯，总之我也想以\x01",
            "和工作无关的方式来洗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_298B")

    label("loc_2957")


    ChrTalk(    #138
        0x103,
        (
            "#021F呵呵，总之我也想以\x01",
            "和工作无关的方式来洗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_298B")


    ChrTalk(    #139
        0x8,
        (
            "#681F哈哈，你们随时\x01",
            "都可以来洗。\x02\x03",

            "不管怎样，今天你们是帮了大忙了。\x01",
            "有什么需要我会再找你们的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x101,
        "#1006F#1P嗯，那么再见了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x107,
        "#061F再见，毛婆婆。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x8)
    OP_28(0x70, 0x4, 0x10)
    OP_28(0x70, 0x1, 0x4)
    OP_28(0x70, 0x1, 0x8)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #142
        "\x07\x02任务【击退偷窥色魔】\x07\x00完成了！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_4B(0x8, 255)
    ClearMapFlags(0x10000000)
    EventEnd(0x0)
    Return()

    # Function_3_251D end

    SaveToFile()

Try(main)
