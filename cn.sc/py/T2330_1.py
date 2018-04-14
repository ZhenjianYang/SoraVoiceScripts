from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T2330_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
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
        '',                                     # 8
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
        "Function_1_4E8",          # 01, 1
        "Function_2_5A1",          # 02, 2
        "Function_3_F22",          # 03, 3
        "Function_4_119F",         # 04, 4
        "Function_5_1297",         # 05, 5
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_EE")
    TalkBegin(0xB)

    ChrTalk(    #0
        0xB,
        "诸位，这次辛苦你们了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xB,
        "下次工作时再见吧。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xB)
    Jump("loc_4E7")

    label("loc_EE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x65, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_419")
    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_18B")
    OP_A2(0x5)

    ChrTalk(    #2
        0xB,
        "接下来的贸易谈判是在柏斯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xB,
        (
            "离定期船开船\x01",
            "还有足够的时间呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xB,
        (
            "不过在卢安\x01",
            "打发时间很容易。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xB,
        (
            "提前出发可能\x01",
            "也不错。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_413")

    label("loc_18B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_26B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_200")

    ChrTalk(    #6
        0xB,
        (
            "很希望将来能有机会品尝一下\x01",
            "一流厨师烹调的本地珍馐。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xB,
        (
            "我们奥维德商会\x01",
            "也要为此更加努力才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_268")

    label("loc_200")

    OP_A2(0x5)

    ChrTalk(    #8
        0xB,
        (
            "果然本地的土产\x01",
            "有重新审视的价值。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xB,
        (
            "这种珍贵的食材\x01",
            "要是能够在高级餐馆\x01",
            "也简单地品尝到就好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_268")

    Jump("loc_413")

    label("loc_26B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_362")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2D1")

    ChrTalk(    #10
        0xB,
        (
            "不过我一打算自己去探索\x01",
            "就会被我侄女阿梅莉雅挽留。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xB,
        "所以我就拜托了协会。\x02",
    )

    CloseMessageWindow()
    Jump("loc_35F")

    label("loc_2D1")

    OP_A2(0x5)

    ChrTalk(    #12
        0xB,
        (
            "本来这次也想\x01",
            "自己去探索的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xB,
        (
            "不过被我侄女阿梅莉雅阻止了。\x01",
            "所以我就拜托了协会。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xB,
        (
            "平常总是让那孩子担心，\x01",
            "偶尔也要听听她的话。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35F")

    Jump("loc_413")

    label("loc_362")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_3B6")

    ChrTalk(    #15
        0xB,
        (
            "海味、河味……\x01",
            "连山珍都能享受到。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xB,
        (
            "呵呵，不愧是\x01",
            "孕育了我的土地。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_413")

    label("loc_3B6")

    OP_A2(0x5)

    ChrTalk(    #17
        0xB,
        (
            "嗯～卢安果然是一片\x01",
            "富于变化的土地啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xB,
        (
            "看着食材的清单，\x01",
            "再次让我认识到了这一点。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_413")

    TalkEnd(0xB)
    Jump("loc_4E7")

    label("loc_419")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x65, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_42A")
    Call(1, 4)
    Jump("loc_4E7")

    label("loc_42A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x65, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_43B")
    Call(1, 2)
    Jump("loc_4E7")

    label("loc_43B")

    SetChrFlags(0xB, 0x10)
    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_480")

    ChrTalk(    #19
        0xB,
        (
            "唔～为了接下来的贸易谈判\x01",
            "也要快点完成清单……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DF")

    label("loc_480")

    OP_A2(0x5)

    ChrTalk(    #20
        0xB,
        (
            "唔～不管怎么看都像是\x01",
            "还有遗漏啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xB,
        (
            "为了准备接下来的贸易谈判\x01",
            "也要快点完成清单……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DF")

    TalkEnd(0xB)
    ClearChrFlags(0xB, 0x10)

    label("loc_4E7")

    Return()

    # Function_0_AA end

    def Function_1_4E8(): pass

    label("Function_1_4E8")

    SetChrPos(0x101, 650, 0, 880, 0)
    SetChrPos(0xF7, 1540, 0, 670, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_53D")
    SetChrPos(0x104, 650, 0, -380, 0)
    SetChrPos(0x105, 1490, 0, -570, 0)
    Jump("loc_58F")

    label("loc_53D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x26)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_570")
    SetChrPos(0x104, 650, 0, -380, 0)
    SetChrPos(0x127, 1490, 0, -570, 0)
    Jump("loc_58F")

    label("loc_570")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_58F")
    SetChrPos(0x109, 1095, 0, -475, 0)

    label("loc_58F")

    OP_6D(90, 0, 1990, 0)
    Return()

    # Function_1_4E8 end

    def Function_2_5A1(): pass

    label("Function_2_5A1")

    OP_4A(0xB, 0)
    EventBegin(0x0)
    Fade(1000)
    Call(1, 1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x65, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_5F8")
    TurnDirection(0xB, 0x101, 400)
    Sleep(500)

    ChrTalk(    #22
        0xB,
        (
            "#2P哟，是你们啊。\x02\x03",

            "怎么样？有时间了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8F4")

    label("loc_5F8")


    ChrTalk(    #23
        0x101,
        "#1011F#1P你好，能打搅你一下吗？\x02",
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xB, 0x101, 400)
    Sleep(500)

    ChrTalk(    #24
        0xB,
        "#2P嗯……？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x5, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x1F, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_668")
    OP_A2(0x7)
    Jump("loc_66B")

    label("loc_668")

    OP_A3(0x7)

    label("loc_66B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E8")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "◇完成过上一部的关联任务的情况下\x01",      # 0
            "◇没有完成的情况下\x01",                    # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E5")
    OP_A2(0x7)
    Jump("loc_6E8")

    label("loc_6E5")

    OP_A3(0x7)

    label("loc_6E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_866")

    ChrTalk(    #25
        0xB,
        "#2P哦，原来是你啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xB,
        (
            "#2P还记得我吗？\x01",
            "是很早以前拜托过你们工作的人。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF7, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_771")

    ChrTalk(    #27
        0x106,
        "#052F#4P什么啊，原来你们认识？\x02",
    )

    CloseMessageWindow()
    Jump("loc_78D")

    label("loc_771")


    ChrTalk(    #28
        0x103,
        "#023F#4P咦，你们认识？\x02",
    )

    CloseMessageWindow()

    label("loc_78D")

    TurnDirection(0x101, 0xF7, 400)

    ChrTalk(    #29
        0x101,
        (
            "#1016F#1P嗯，算是认识吧。\x01",
            "这个人是位食材商人。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xB, 400)

    ChrTalk(    #30
        0x101,
        "#1000F#1P真是好久不见了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xB,
        (
            "#2P嗯，最后一次见面应该\x01",
            "是在诞辰庆典之前吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xB,
        (
            "#2P没问题的话\x01",
            "我立即来做工作的说明……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xB,
        "#2P现在有时间吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_8F4")

    label("loc_866")


    ChrTalk(    #34
        0xB,
        "#2P哦，是游击士啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xB,
        "#2P看来告示板过来的吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x101,
        "#1000F#1P嗯，算是吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xB,
        (
            "#2P那么\x01",
            "我立即来做工作的说明……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xB,
        "#2P现在有时间吗？\x02",
    )

    CloseMessageWindow()

    label("loc_8F4")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【听工作的说明】\x01",      # 0
            "【放弃】\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9B9")
    OP_28(0x65, 0x1, 0x8000)

    ChrTalk(    #39
        0x101,
        (
            "#1007F#1P不，对不起。\x01",
            "现在有点不方便。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xB,
        (
            "#2P哦，这样啊。\x02\x03",

            "那么你们下次再来吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F12")

    label("loc_9B9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x5, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x1F, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9E4")

    ChrTalk(    #41
        0x101,
        "#1006F#1P没问题。\x02",
    )

    CloseMessageWindow()
    Jump("loc_9FB")

    label("loc_9E4")


    ChrTalk(    #42
        0x101,
        "#1006F#1P没问题。\x02",
    )

    CloseMessageWindow()

    label("loc_9FB")

    TurnDirection(0xF7, 0xB, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_A30")

    ChrTalk(    #43
        0x106,
        "#050F#4P那么，工作内容是什么？\x02",
    )

    CloseMessageWindow()
    Jump("loc_A54")

    label("loc_A30")


    ChrTalk(    #44
        0x103,
        "#020F#4P那么，委托内容是什么？\x02",
    )

    CloseMessageWindow()

    label("loc_A54")


    ChrTalk(    #45
        0xB,
        "#2P嗯，你们听我说。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xB,
        (
            "#2P其实我现在在做\x01",
            "整个卢安地区的食材清单……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xB,
        (
            "#2P不过最近有很多危险的魔兽出没，\x01",
            "我想去探索也没那个本事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xB,
        (
            "#2P所以就想到要找你们\x01",
            "这些游击士帮忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x101,
        (
            "#1015F#1P哦，原来是这样……\x02\x03",

            "#1000F具体需要帮你\x01",
            "做些什么呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xB,
        "#2P先看看这个吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #51
        (
            "\x07\x05【暂定版魔兽食材清单】\x01",
            "·魔兽羽翼·魔兽尾巴\x01",
            "·魔兽眼珠·魔兽甲壳\x01",
            "·魔兽之肉·魔兽之种\x01",
            "·魔兽鱼肉·魔兽明胶\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #52
        0x101,
        (
            "#1015F#1P等等啊，总之我先记下来了……\x01",
            "这就是你刚才说的清单？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xB,
        "#2P嗯，虽然还是未完成版。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xB,
        (
            "#2P我希望你们能找到这张\x01",
            "清单上没有列出的魔兽食材。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xB,
        (
            "#2P记住，是清单上『没有』的食材。\x01",
            "这点可别搞错了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xB,
        (
            "#2P发现了上面没有的食材\x01",
            "就再到这里来报告吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xB,
        (
            "#2P当然，收集了一定数量后\x01",
            "再来报告也没问题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xB,
        (
            "#2P只不过每种食材\x01",
            "需要留下一个作为样本，\x01",
            "注意别吃得过头了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x101,
        (
            "#1006F#1P得到了清单上没有的食材\x01",
            "再来这里报告就行了是吧？\x02\x03",

            "#1015F不过一共有多少种类呢？\x01",
            "就是没有出现在那个清单上的食材。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xB,
        (
            "#2P我也不知道确切数字，\x01",
            "不过充其量也就是５、６种。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xB,
        (
            "#2P你们只要找到其中的一半\x01",
            "我就会正常支付报酬的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xB,
        "#2P还有什么其它要问的吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x101,
        (
            "#1000F#1P不，基本上都明白了。\x02\x03",

            "好，我们会耐心地做的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xB,
        (
            "#2P嗯，那就好。\x01",
            "不过这不是什么紧急的工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xB,
        "#2P那么我就静候佳音了。\x02",
    )

    CloseMessageWindow()
    OP_28(0x65, 0x4, 0x4)
    OP_28(0x65, 0x4, 0x8)
    OP_28(0x65, 0x1, 0x1)
    OP_28(0x65, 0x1, 0x2)

    label("loc_F12")

    OP_30(0x0)
    OP_4B(0xB, 0)
    OP_8C(0xB, 0, 0)
    EventEnd(0x0)
    Return()

    # Function_2_5A1 end

    def Function_3_F22(): pass

    label("Function_3_F22")

    EventBegin(0x0)
    Fade(1000)
    OP_8C(0xB, 180, 0)
    OP_4A(0xB, 255)
    Call(1, 1)
    OP_69(0xB, 0x0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #66
        0xB,
        "#2P哟，找到什么了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x101,
        (
            "#1015F#1P不，这倒没有。\x02\x03",

            "其实是我们有事情要办……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xB,
        (
            "#2P莫非是调查\x01",
            "不能继续了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x101,
        (
            "#1007F#1P嗯，是的。\x02\x03",

            "对不起，\x01",
            "半途而废了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xB,
        "#2P不，别介意。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xB,
        (
            "#2P因为我拜托你们调查的部分\x01",
            "你们已经完成了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xB,
        (
            "#2P那么，我会通知协会说\x01",
            "你们已经完成了委托。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xB,
        "#2P那样的话你们应该能拿到报酬的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x101,
        "#1000F#1P谢谢，真是帮了我们的忙了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xB,
        (
            "#2P那么，诸位。\x01",
            "这回辛苦你们了。\x02\x03",

            "#2P下次工作时再见。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x101,
        "#1000F#1P嗯，再见。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1128")

    ChrTalk(    #77
        0x106,
        "#051F#4P嗯，再见。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1140")

    label("loc_1128")


    ChrTalk(    #78
        0x103,
        "#020F#4P嗯，再见。\x02",
    )

    CloseMessageWindow()

    label("loc_1140")

    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #79
        "\x07\x02任务【收集食材】\x07\x00完成了！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x4)
    OP_4B(0xB, 255)
    OP_8C(0xB, 0, 0)
    EventEnd(0x0)
    Return()

    # Function_3_F22 end

    def Function_4_119F(): pass

    label("Function_4_119F")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x65, 0x1, 0x4000)"), scpexpr(EXPR_END)), "loc_1239")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "【报告】\x01",          # 0
            "【结束调查】\x01",      # 1
            "【放弃】\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1214")
    Call(1, 5)
    Jump("loc_1236")

    label("loc_1214")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1236")
    Call(1, 3)
    OP_28(0x65, 0x4, 0x10)
    OP_28(0x65, 0x1, 0x400)
    OP_A2(0x4)
    Jump("loc_1236")

    label("loc_1236")

    Jump("loc_1293")

    label("loc_1239")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "【报告】\x01",      # 0
            "【放弃】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_128F")
    Jump("loc_1293")

    label("loc_128F")

    Call(1, 5)

    label("loc_1293")

    TalkEnd(0xB)
    Return()

    # Function_4_119F end

    def Function_5_1297(): pass

    label("Function_5_1297")

    OP_4A(0xB, 255)

    ChrTalk(    #80
        0xB,
        "哟，找到了什么吗？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #81
        "\x07\x05给奥维德看了身上的食材。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x3A1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x65, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_130C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_130C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x3A3, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x65, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1328")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1328")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x39E, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x65, 0x1, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1344")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1344")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x3A7, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x65, 0x1, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1360")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1360")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x3AA, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x65, 0x1, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_137C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_137C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x3A9, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x65, 0x1, 0x80)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1398")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1398")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1F44")
    OP_62(0xB, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0xB)
    Sleep(400)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #82
        0xB,
        "哟……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xB,
        (
            "这个食材\x01",
            "清单上应该没有。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x3A1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x65, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1458")
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #84
        "\x1F\xA1\x03\x07\x00的报告完成！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_28(0x65, 0x1, 0x4)

    label("loc_1458")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x3A3, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x65, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1497")
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #85
        "\x1F\xA3\x03\x07\x00的报告完成！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_28(0x65, 0x1, 0x8)

    label("loc_1497")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x39E, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x65, 0x1, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14D6")
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #86
        "\x1F\x9E\x03\x07\x00的报告完成！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_28(0x65, 0x1, 0x10)

    label("loc_14D6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x3A7, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x65, 0x1, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1515")
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #87
        "\x1F\xA7\x03\x07\x00的报告完成！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_28(0x65, 0x1, 0x20)

    label("loc_1515")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x3AA, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x65, 0x1, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1554")
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #88
        "\x1F\xAA\x03\x07\x00的报告完成！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_28(0x65, 0x1, 0x40)

    label("loc_1554")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x3A9, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x65, 0x1, 0x80)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1593")
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #89
        "\x1F\xA9\x03\x07\x00的报告完成！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_28(0x65, 0x1, 0x80)

    label("loc_1593")

    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_0D()
    Sleep(400)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x65, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_15CA")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_15CA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x65, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_15DF")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_15DF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x65, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_15F4")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_15F4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x65, 0x1, 0x20)"), scpexpr(EXPR_END)), "loc_1609")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1609")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x65, 0x1, 0x40)"), scpexpr(EXPR_END)), "loc_161E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_161E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x65, 0x1, 0x80)"), scpexpr(EXPR_END)), "loc_1633")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1633")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19DA")
    FadeToDark(1000, 0, -1)
    OP_0D()
    EventBegin(0x0)
    OP_8C(0xB, 180, 0)
    Call(1, 1)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #90
        0xB,
        (
            "#2P嗯，这个可了不得。\x01",
            "是超过我预计的成果。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xB,
        (
            "#2P现在可以说\x01",
            "已经是完美的清单了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xB,
        (
            "#2P哎呀，诸位游击士。\x01",
            "你们这次的工作完成得非常出色。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x101,
        (
            "#1001F#1P嘿嘿，您过奖了。\x02\x03",

            "那么，委托就算完成了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xB,
        (
            "#2P嗯，成果超过了预期，\x01",
            "所以我要给你们额外奖励。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xB,
        (
            "#2P这是我的产品，\x01",
            "祝你们好胃口。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #96
        "\x07\x00得到了２０个\x1F\x9F\x03\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x39F, 20)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x26)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1819")

    ChrTalk(    #97
        0x127,
        (
            "#153F#3P哇、哇～！？\x02\x03",

            "这…这些东西…\x01",
            "这个能吃吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1819")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_184B")

    ChrTalk(    #98
        0x106,
        "#053F#4P（……………………………）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1873")

    label("loc_184B")


    ChrTalk(    #99
        0x103,
        "#026F#4P（……………………………）\x02",
    )

    CloseMessageWindow()

    label("loc_1873")


    ChrTalk(    #100
        0x101,
        (
            "#1008F#1P哈、哈哈……\x02\x03",

            "拿、拿了这么多\x01",
            "真不好意思。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xB,
        (
            "#2P不，这是和你们的\x01",
            "工作成果相符的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xB,
        (
            "#2P好了，别客气，\x01",
            "收下来吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x101,
        (
            "#1016F#1P哈哈……\x01",
            "那、那我们就不客气了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xB,
        (
            "#2P嗯，你们这次\x01",
            "真是辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xB,
        "#2P那么，我们在下次工作时再见。\x02",
    )

    CloseMessageWindow()
    OP_2B(0x65, 0x1)
    OP_2C(0x65, 0x3E8)
    OP_28(0x65, 0x4, 0x10)
    OP_28(0x65, 0x1, 0x400)
    OP_A2(0x4)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #106
        "\x07\x02任务【收集食材】\x07\x00完成了！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x4)
    EventEnd(0x0)
    Jump("loc_1F41")

    label("loc_19DA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "OP_29(0x65, 0x1, 0x4000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F08")
    FadeToDark(1000, 0, -1)
    OP_0D()
    EventBegin(0x0)
    OP_8C(0xB, 180, 0)
    Call(1, 1)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #107
        0xB,
        "#2P嗯，你们已经找到很多了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xB,
        (
            "#2P清单也几乎要完成了。\x01",
            "可以说你们的工作已经干得很不错了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x101,
        "#1000F#1P那么，委托算是完成了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xB,
        "#2P嗯，这么说确实也可以……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xB,
        (
            "#2P怎么样，想不想\x01",
            "继续调查呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x101,
        "#1004F#1P咦？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xB,
        (
            "#2P就是问你们想不想\x01",
            "帮我完成清单。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xB,
        (
            "#2P估计还有２、３种\x01",
            "食材没被找到。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xB,
        (
            "#2P如果你们都能找到的话，\x01",
            "我也会提供额外奖励……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xB,
        "#2P怎么样？\x02",
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
            "【结束调查】\x01",      # 0
            "【继续调查】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D82")

    ChrTalk(    #117
        0x101,
        (
            "#1015F#1P不了，还是\x01",
            "到此为止吧。\x02\x03",

            "我们也还有其它的工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xB,
        "#2P唔，看来你们完全没兴趣啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xB,
        (
            "#2P不过这也没办法。\x01",
            "工作就到此为止吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xB,
        (
            "#2P我会按照约定\x01",
            "全额支付报酬的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xB,
        (
            "#2P好，辛苦你们了。\x01",
            "下次工作时再见。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1CE3")

    ChrTalk(    #122
        0x106,
        "#051F#4P嗯，再见。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CFB")

    label("loc_1CE3")


    ChrTalk(    #123
        0x103,
        "#020F#4P嗯，再见。\x02",
    )

    CloseMessageWindow()

    label("loc_1CFB")


    ChrTalk(    #124
        0x101,
        "#1006F#1P那么也希望你努力工作。\x02",
    )

    CloseMessageWindow()
    OP_28(0x65, 0x4, 0x10)
    OP_28(0x65, 0x1, 0x400)
    OP_A2(0x4)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #125
        "\x07\x02任务【收集食材】\x07\x00完成了！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x4)
    Jump("loc_1F03")

    label("loc_1D82")

    OP_28(0x65, 0x1, 0x4000)

    ChrTalk(    #126
        0x101,
        (
            "#1006F#1P嗯，我们试试。\x02\x03",

            "只做到一半，我们\x01",
            "也觉得不畅快。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xB,
        "#2P我就知道你会这么说。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xB,
        (
            "#2P那报告什么的\x01",
            "都请按和以前一样的顺序来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xB,
        (
            "#2P如果你们有急事\x01",
            "而不能继续的话就跟我说吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xB,
        (
            "#2P到时候我再想办法。\x01",
            "不过报酬就只有一般程度的了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1EA7")

    ChrTalk(    #131
        0x106,
        "#051F#4P原来如此，明白了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1EC7")

    label("loc_1EA7")


    ChrTalk(    #132
        0x103,
        "#020F#4P原来如此，明白了。\x02",
    )

    CloseMessageWindow()

    label("loc_1EC7")


    ChrTalk(    #133
        0x101,
        "#1006F#1P那我们就走了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xB,
        "#2P我可等着你们的报告哦。\x02",
    )

    CloseMessageWindow()

    label("loc_1F03")

    EventEnd(0x0)
    Jump("loc_1F41")

    label("loc_1F08")


    ChrTalk(    #135
        0xB,
        (
            "应该还有一些食材\x01",
            "是清单上没有的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xB,
        "继续努力吧。\x02",
    )

    CloseMessageWindow()

    label("loc_1F41")

    Jump("loc_1FA6")

    label("loc_1F44")

    OP_62(0xB, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0xB)
    Sleep(400)

    ChrTalk(    #137
        0xB,
        "唔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xB,
        (
            "很遗憾，\x01",
            "好像没有新的东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xB,
        "下次再来报告吧。\x02",
    )

    CloseMessageWindow()

    label("loc_1FA6")

    OP_4B(0xB, 0)
    OP_8C(0xB, 0, 0)
    Return()

    # Function_5_1297 end

    SaveToFile()

Try(main)
