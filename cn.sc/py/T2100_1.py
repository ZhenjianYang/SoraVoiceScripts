from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2100_1 ._SN',
        MapName             = 'Ruan',
        Location            = 'T2100.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60012",
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
        "Function_1_8F6",          # 01, 1
        "Function_2_C0E",          # 02, 2
        "Function_3_1A8B",         # 03, 3
        "Function_4_2366",         # 04, 4
        "Function_5_278B",         # 05, 5
        "Function_6_2D22",         # 06, 6
        "Function_7_2D80",         # 07, 7
        "Function_8_2DDE",         # 08, 8
        "Function_9_2E41",         # 09, 9
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x245, 3)), scpexpr(EXPR_END)), "loc_53B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D5")
    Call(1, 2)
    Jump("loc_538")

    label("loc_D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_119")

    ChrTalk(    #0
        0xFE,
        (
            "现在正在进行选举，\x01",
            "客人相当少。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "请好好\x01",
            "休息吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_538")

    label("loc_119")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_223")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_187")

    ChrTalk(    #2
        0xFE,
        (
            "呵呵呵，\x01",
            "看起来事件已经解决了嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "我的证言\x01",
            "也稍微派上点用场了不？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CB")

    label("loc_187")

    OP_A2(0x8)

    ChrTalk(    #4
        0xFE,
        (
            "呵呵呵，\x01",
            "看起来事件已经解决了嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        "啊，这真值得庆贺哟。\x02",
    )

    CloseMessageWindow()

    label("loc_1CB")

    Jump("loc_220")

    label("loc_1CE")


    ChrTalk(    #6
        0xFE,
        (
            "无论选举结果如何，\x01",
            "我都只是在这里当班而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "以前是这样，\x01",
            "以后也是这样。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_220")

    Jump("loc_538")

    label("loc_223")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_371")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_277")

    ChrTalk(    #8
        0xFE,
        (
            "需要小船的话\x01",
            "随时都可以来找我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        "现在的话，可以随便坐哟。\x02",
    )

    CloseMessageWindow()
    Jump("loc_36E")

    label("loc_277")

    OP_A2(0x8)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_328")

    ChrTalk(    #10
        0xFE,
        (
            "噢，你是刚才\x01",
            "借用小船的人嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "怎样？\x01",
            "想出好诗来了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x104,
        (
            "#030F呼，托您的福创作出来了。\x02\x03",

            "奥利维尔·朗海姆\x01",
            "毕生的大作啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "呵呵呵，\x01",
            "那可太好喽。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36E")

    label("loc_328")


    ChrTalk(    #14
        0xFE,
        (
            "刚才\x01",
            "桥那边真吵得厉害。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "忽然安静下来了，\x01",
            "我还觉得有点奇怪。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36E")

    Jump("loc_538")

    label("loc_371")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_END)), "loc_3AE")

    ChrTalk(    #16
        0xFE,
        "哎呀，什么啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "好像\x01",
            "驶向大桥那边去了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_538")

    label("loc_3AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_479")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_404")

    ChrTalk(    #18
        0xFE,
        (
            "为了创作诗词\x01",
            "乘船在水上游来游去……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        "还真是风雅的人啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_476")

    label("loc_404")

    OP_A2(0x8)

    ChrTalk(    #20
        0xFE,
        (
            "小船刚刚\x01",
            "借出去了哟。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "自称是什么旅行者，\x01",
            "还真是风雅的人啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "要在船上创作诗词……\x01",
            "他是这么说的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_476")

    Jump("loc_538")

    label("loc_479")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4E3")

    ChrTalk(    #23
        0xFE,
        (
            "我明白选举很重要，\x01",
            "但最好还是不要大声叫喊吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "看了海报谁要说什么\x01",
            "大家也都知道了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_538")

    label("loc_4E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_538")

    ChrTalk(    #25
        0xFE,
        (
            "现在正在进行选举，\x01",
            "客人也少了很多哟。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "太悠闲了，弄得\x01",
            "我都想钓鱼了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_538")

    Jump("loc_8F2")

    label("loc_53B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_581")

    ChrTalk(    #27
        0xFE,
        "哎呀，什么来的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "好像\x01",
            "是驶向大桥那边去了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8F2")

    label("loc_581")

    TurnDirection(0xFE, 0x101, 0)
    OP_A2(0x122B)
    OP_A2(0x9)

    ChrTalk(    #29
        0xFE,
        (
            "哎呀，还在想是谁呢……\x01",
            "真是好久不见了哟。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_722")

    ChrTalk(    #30
        0x101,
        (
            "#1000F啊，老爷爷还好吗？\x02\x03",

            "我记得上桥的时候\x01",
            "借了您的小船吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x105,
        (
            "#048F那时真是\x01",
            "多谢您了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x105, 400)

    ChrTalk(    #32
        0xFE,
        (
            "哪里哪里，\x01",
            "小事一桩。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "那，今天\x01",
            "是来乘船游玩的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x101,
        (
            "#1007F很遗憾，又是工作。\x02\x03",

            "我们正在调查\x01",
            "酒店发生的事件呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #35
        0xFE,
        "呵，那可辛苦哟。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "有什么想知道的\x01",
            "就尽管问吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        (
            "#1006F嗯，谢谢。\x01",
            "那我就问了哟。\x02",
        )
    )

    CloseMessageWindow()
    Call(1, 2)
    Jump("loc_8F2")

    label("loc_722")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_7AD")

    ChrTalk(    #38
        0x101,
        (
            "#1000F啊，老爷爷还好吗？\x02\x03",

            "我记得上桥的时候\x01",
            "借了您的小船吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x105,
        (
            "#047F那时候要是没有船\x01",
            "可就不得了了。\x02\x03",

            "真的非常感谢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_80C")

    label("loc_7AD")


    ChrTalk(    #40
        0x101,
        (
            "#1000F啊，老爷爷还好吗？\x02\x03",

            "记得追赶戴尔蒙市长的时候\x01",
            "借了您的小船吧。\x02\x03",

            "那时候真是帮大忙了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_80C")


    ChrTalk(    #41
        0xFE,
        (
            "哪里哪里，\x01",
            "小事一桩。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "那，今天\x01",
            "是来乘船游玩的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        (
            "#1016F很遗憾，还是工作。\x02\x03",

            "不过，这次看来\x01",
            "是比较轻松了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "是吗。\x01",
            "那就慢慢来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "选举中客人也少。\x01",
            "应该能比之前更放松了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        (
            "#1000F嗯，谢谢。\x01",
            "那就先这样。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8F2")

    TalkEnd(0xFE)
    Return()

    # Function_0_AA end

    def Function_1_8F6(): pass

    label("Function_1_8F6")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CC(0x0, 0x0, 0xA, 0xA, 0x1)
    OP_CC(0x1, 0x0, "关于昆茨")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_97A")
    OP_CC(0x1, 0x0, "声响")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFFFFFF0), scpexpr(EXPR_AND), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_IMUL), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_97A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_9AF")
    OP_CC(0x1, 0x0, "发怒")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFFFFF0F), scpexpr(EXPR_AND), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_IMUL), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9AF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_9EA")
    OP_CC(0x1, 0x0, "关于海利欧")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFFFF0FF), scpexpr(EXPR_AND), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x100), scpexpr(EXPR_IMUL), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9EA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_A1F")
    OP_CC(0x1, 0x0, "午饭")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFFF0FFF), scpexpr(EXPR_AND), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1000), scpexpr(EXPR_IMUL), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A1F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x40)"), scpexpr(EXPR_END)), "loc_A54")
    OP_CC(0x1, 0x0, "钟声")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFF0FFFF), scpexpr(EXPR_AND), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x10000), scpexpr(EXPR_IMUL), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A54")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x800)"), scpexpr(EXPR_END)), "loc_A8D")
    OP_CC(0x1, 0x0, "善后处理")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xF0FFFFF), scpexpr(EXPR_AND), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x100000), scpexpr(EXPR_IMUL), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A8D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x2000)"), scpexpr(EXPR_END)), "loc_AC8")
    OP_CC(0x1, 0x0, "关于贝尔夫")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFFFFFF), scpexpr(EXPR_AND), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1000000), scpexpr(EXPR_IMUL), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_AC8")

    OP_CC(0x1, 0x0, "离开")
    OP_CC(0x2, 0x0)
    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B07")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C0D")

    label("loc_B07")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B2B")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C0D")

    label("loc_B2B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B4F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C0D")

    label("loc_B4F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x100), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B73")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C0D")

    label("loc_B73")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1000), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B97")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C0D")

    label("loc_B97")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x10000), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BBB")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C0D")

    label("loc_BBB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x100000), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BDF")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C0D")

    label("loc_BDF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1000000), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C03")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C0D")

    label("loc_C03")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C0D")

    Return()

    # Function_1_8F6 end

    def Function_2_C0E(): pass

    label("Function_2_C0E")

    Call(1, 1)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_C3B"),
        (1, "loc_C96"),
        (2, "loc_EBD"),
        (3, "loc_F06"),
        (4, "loc_FFE"),
        (5, "loc_163D"),
        (6, "loc_1957"),
        (7, "loc_1A3A"),
        (SWITCH_DEFAULT, "loc_1A87"),
    )


    label("loc_C3B")

    OP_28(0x6A, 0x1, 0x100)

    ChrTalk(    #47
        0xFE,
        (
            "唔，我知道。\x01",
            "在港口工作的年轻人吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "最近大概所有人\x01",
            "都参加选举运动了哟。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A8A")

    label("loc_C96")

    OP_28(0x6A, 0x1, 0x100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x80)"), scpexpr(EXPR_END)), "loc_D21")

    ChrTalk(    #49
        0xFE,
        (
            "我听到\x01",
            "那个大的声响\x01",
            "和钟声交替出现。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        "哎呀？我还以为是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "肚子饿了就没在意，\x01",
            "然后就去拉旺塔尔游戏吧了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EBA")

    label("loc_D21")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_D7F")

    ChrTalk(    #52
        0xFE,
        (
            "忘了是什么时候\x01",
            "听到得那阵很大的声音了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "像是什么碰撞\x01",
            "发出的声音似的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EBA")

    label("loc_D7F")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_28(0x69, 0x1, 0x1)

    ChrTalk(    #54
        0xFE,
        "噢，声响啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "唔，确实上面\x01",
            "有传来过什么很大的声音。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x101,
        (
            "#1004F上面，\x01",
            "是说酒店的阳台附近？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #57
        0xFE,
        "唔，大概就是那吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "像是什么东西碰撞的声音，\x01",
            "听到的声音很大。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "是什么时候听到的，\x01",
            "就想不起来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x101,
        (
            "#1015F嗯……真可惜……\x02\x03",

            "#1006F不过，这情报很有价值。\x02\x03",

            "谢谢老爷爷。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x69, 0x1, 0x4)

    label("loc_EBA")

    Jump("loc_1A8A")

    label("loc_EBD")

    OP_28(0x6A, 0x1, 0x100)

    ChrTalk(    #61
        0xFE,
        (
            "噢，昆茨那家伙\x01",
            "那么生气吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "唉，年轻人\x01",
            "就是脾气暴躁。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A8A")

    label("loc_F06")

    OP_28(0x6A, 0x1, 0x100)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_F70")

    ChrTalk(    #63
        0xFE,
        (
            "海利欧…\x01",
            "就是那个年轻的商人吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "看起来是个教养良好，\x01",
            "老老实实的年轻人哟。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FFB")

    label("loc_F70")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #65
        0xFE,
        (
            "唔，海利欧…\x01",
            "就是那个年轻的商人吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "作为商人，相貌\x01",
            "没有点魄力可是不行的哟。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "脸这么老实，\x01",
            "就都只想跟他讨价还价了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FFB")

    Jump("loc_1A8A")

    label("loc_FFE")

    OP_28(0x6A, 0x1, 0x100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x20)"), scpexpr(EXPR_END)), "loc_1089")

    ChrTalk(    #68
        0xFE,
        (
            "和平常一样听到钟声\x01",
            "就去拉旺塔尔游戏吧了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "那时酒店地下室里\x01",
            "没有一个人哟。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "回来的时候\x01",
            "诺曼的儿子来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_163A")

    label("loc_1089")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_12C9")
    OP_28(0x6A, 0x1, 0x20)

    ChrTalk(    #71
        0xFE,
        (
            "今天中午\x01",
            "去拉旺塔尔游戏吧了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "我习惯每天听到\x01",
            "钟声时出去吃午饭。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x101,
        (
            "#1011F哎呀，真是有品味的生活呢……\x02\x03",

            "#1015F不过，既然出去了，\x01",
            "应该是从酒店中走出去的吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #74
        0xFE,
        "当然喽。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "又不可能\x01",
            "从海上飞过去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x101,
        (
            "#1016F啊哈哈，那倒是。\x02\x03",

            "#1000F……那，当时\x01",
            "在酒店中看见谁了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "当然１楼\x01",
            "有亚内斯特在……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        "其他地方都很安静。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x101,
        (
            "#1011F咦……？\x01",
            "就没别人了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "唔，我去的时候\x01",
            "地下和１楼都很安静。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "回来的时候\x01",
            "诺曼的儿子来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x101,
        (
            "#1015F诺曼的儿子……\x01",
            "对了，是贝尔夫吧。\x02\x03",

            "#1006F嗯，知道这个就足够了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "哪里哪里。\x01",
            "那么，再见喽。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_163A")

    label("loc_12C9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x40)"), scpexpr(EXPR_END)), "loc_1323")

    ChrTalk(    #84
        0xFE,
        (
            "今天要去\x01",
            "拉旺塔尔游戏吧吃饭呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "我习惯每天听到\x01",
            "钟声时出去吃午饭。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_163A")

    label("loc_1323")

    OP_28(0x69, 0x1, 0x40)

    ChrTalk(    #86
        0xFE,
        "唔，午饭吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "今天午饭\x01",
            "是在拉旺塔尔游戏吧吃的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "每天听到\x07\x04『钟声』\x07\x00的时候\x01",
            "出去吃午饭是我的习惯。\x02",
        )
    )

    OP_22(0x11, 0x0, 0x64)
    CloseMessageWindow()

    ChrTalk(    #89
        0x101,
        "#1011F钟声……？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #90
        0x105,
        (
            "#040F就是伦格兰德大桥的钟。\x02\x03",

            "恩，吊桥上\x01",
            "钟响了吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #91
        0x101,
        (
            "#1018F啊，想起来了。\x02\x03",

            "嗯嗯，确实会响。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "固定时间到了就会响。\x01",
            "已经代替我们的钟表了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xFE, 400)

    ChrTalk(    #93
        0x101,
        (
            "#1000F咦，还可以这样用啊。\x02\x03",

            "要代替钟表的话\x01",
            "形状好像稍微大了点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x105,
        (
            "#040F不过，艾丝蒂尔。\x02\x03",

            "问问大家关于钟声的事\x01",
            "说不定很有帮助呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #95
        0x101,
        "#1004F啊？为什么呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x105,
        (
            "#040F钟声响起时发生的事\x01",
            "他们一定记得特别清楚。\x02\x03",

            "钟声就是记忆的标志。\x01",
            "就像这位老爷爷一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x101,
        (
            "#1000F啊啊～原来如此～\x02\x03",

            "#1001F不愧是科洛丝。\x01",
            "好理智的建议哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x105,
        (
            "#048F呵呵，可别\x01",
            "太夸我了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        (
            "唔，虽不知道怎么了，\x01",
            "看来是有好事喽。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xFE, 400)

    ChrTalk(    #100
        0x101,
        (
            "#1006F嗯，很好哦。\x02\x03",

            "那，赶快\x01",
            "去问问看吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x105,
        "#041F好！\x02",
    )

    CloseMessageWindow()

    label("loc_163A")

    Jump("loc_1A8A")

    label("loc_163D")

    OP_28(0x6A, 0x1, 0x100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x80)"), scpexpr(EXPR_END)), "loc_16C8")

    ChrTalk(    #102
        0xFE,
        (
            "我听到\x01",
            "那个大的声响\x01",
            "和钟声交替出现。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        "哎呀？我还以为是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        (
            "肚子饿了就没在意，\x01",
            "然后就去拉旺塔尔游戏吧了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1954")

    label("loc_16C8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_190E")
    OP_28(0x69, 0x1, 0x80)

    ChrTalk(    #105
        0xFE,
        (
            "伦格兰德大桥\x01",
            "的钟声啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "那可是我们生活中\x01",
            "不可缺少的声音哟。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        "啊，说到钟声……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x101,
        "#1002F……想到什么了吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #109
        0xFE,
        (
            "不是，你……\x01",
            "刚才问了什么吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "喏，就是那个，\x01",
            "很大的声音怎么了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x101,
        (
            "#1004F啊，声响的事？\x01",
            "好像碰撞的声音那样的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        "喔，就是那个。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "说起来好像是\x01",
            "听到钟声的同时\x01",
            "也听到那个声音了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x101,
        (
            "#1015F和钟声交替……\x02\x03",

            "……也就是说，那个大的声响\x01",
            "几乎是和钟声同时听见的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "唔，简单的说\x01",
            "就是那样喽。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x105,
        (
            "#042F如果那个声响\x01",
            "是犯人发出的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x101,
        (
            "#1002F钟声响起的时候\x01",
            "没有不在场证明的就是犯人对吧。\x02\x03",

            "嗯，有必要确认\x01",
            "一下嫌疑犯了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1954")

    label("loc_190E")


    ChrTalk(    #118
        0xFE,
        (
            "伦格兰德大桥\x01",
            "的钟声啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "那可是我们生活中\x01",
            "不可缺少的声音哟。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1954")

    Jump("loc_1A8A")

    label("loc_1957")

    OP_28(0x6A, 0x1, 0x100)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_19DB")

    ChrTalk(    #120
        0xFE,
        (
            "唔，到底是谁\x01",
            "帮忙收拾了盘子呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        "问我也没用哟。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "那个时候我正在拉旺塔尔游戏吧里\x01",
            "悠闲地吃着饭呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A37")

    label("loc_19DB")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #123
        0xFE,
        (
            "呵，有人代替亚内斯特\x01",
            "收拾了盘子吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "呵呵呵，那可是近来\x01",
            "少见的好心人那。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A37")

    Jump("loc_1A8A")

    label("loc_1A3A")

    OP_28(0x6A, 0x1, 0x100)

    ChrTalk(    #125
        0xFE,
        (
            "唔，贝尔夫\x01",
            "是说那个年轻人吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        (
            "嗯……应该\x01",
            "不在地下室的呀。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A8A")

    label("loc_1A87")

    Jump("loc_1A8A")

    label("loc_1A8A")

    Return()

    # Function_2_C0E end

    def Function_3_1A8B(): pass

    label("Function_3_1A8B")

    EventBegin(0x0)
    SetChrPos(0x101, 65180, 240, 94310, 90)
    SetChrPos(0xF7, 64550, 0, 95280, 90)
    SetChrPos(0x104, 64319, 0, 93660, 90)
    SetChrPos(0x127, 63690, 170, 94700, 90)
    OP_6D(65440, 260, 94110, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1500, 0)
    OP_0D()
    Sleep(1000)
    OP_70(0x10, 0x14)
    OP_73(0x10)
    Sleep(750)
    SetChrPos(0x31, 69180, 500, 93590, 0)
    ClearChrFlags(0x31, 0x80)
    OP_8E(0x31, 0x1026D, 0x1F4, 0x16F22, 0x7D0, 0x0)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x67, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1F25")

    ChrTalk(    #127
        0x31,
        (
            "今天百忙之中\x01",
            "还麻烦您，真是谢谢了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x31,
        (
            "孩子们也\x01",
            "非常开心呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x67, 0x1, 0x2000)"), scpexpr(EXPR_END)), "loc_1BCD")

    ChrTalk(    #129
        0x31,
        (
            "真是\x01",
            "出色的授课呀。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BCD")


    ChrTalk(    #130
        0x101,
        (
            "#1001F嘿嘿，谢谢。\x02\x03",

            "之前我还挺没底的，\x01",
            "你们满意就太好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x31,
        (
            "还有其他的课，\x01",
            "我就此告辞了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x31,
        (
            "那么，有机会的话\x01",
            "还请多指教。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x101,
        "#1006F嗯，那再见了。\x02",
    )

    CloseMessageWindow()
    OP_8E(0x31, 0x10E3C, 0x1F4, 0x16D96, 0x7D0, 0x0)
    SetChrFlags(0x31, 0x80)
    Sleep(500)
    OP_72(0x10, 0x800)
    OP_6F(0x10, 20)
    OP_70(0x10, 0x0)
    OP_22(0x7, 0x0, 0x64)
    OP_73(0x10)
    OP_71(0x10, 0x800)

    def lambda_1CB0():
        OP_6D(64560, 0, 94340, 2000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1CB0)
    Sleep(2000)
    TurnDirection(0xF7, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1CF6")

    ChrTalk(    #134
        0x106,
        (
            "#051F看来是\x01",
            "顺利完成了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D15")

    label("loc_1CF6")


    ChrTalk(    #135
        0x103,
        "#021F呵呵，不算太顺利啦。\x02",
    )

    CloseMessageWindow()

    label("loc_1D15")

    OP_8C(0x101, 270, 400)

    ChrTalk(    #136
        0x101,
        "#1015F呼，勉强……吧。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 400)

    ChrTalk(    #137
        0x104,
        (
            "#031F呼，不用谦虚了。\x02\x03",

            "你让我见识了\x01",
            "相当棒的讲师哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x101,
        (
            "#1008F是，是吗？\x01",
            "那就好……\x02\x03",

            "#1003F……只不过，还是\x01",
            "感到有点知识不足啊。\x02\x03",

            "一被问到细节\x01",
            "就慌了手脚了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1E40")

    ChrTalk(    #139
        0x106,
        (
            "#053F不过，今后多加努力吧。\x02\x03",

            "连规章都不熟悉的游击士\x01",
            "可是得不到别人信任的哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E97")

    label("loc_1E40")


    ChrTalk(    #140
        0x103,
        (
            "#026F不过，今后多加努力吧。\x02\x03",

            "#027F连规章都不熟悉的游击士\x01",
            "可是得不到别人信任的哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E97")

    TurnDirection(0x101, 0xF7, 400)

    ChrTalk(    #141
        0x101,
        (
            "#1015F说得也是……\x02\x03",

            "#1002F嗯，我会努力的。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #142
        "\x07\x02任务【主日学校的讲师】\x07\x00完成了！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_2361")

    label("loc_1F25")


    ChrTalk(    #143
        0x31,
        (
            "呼，总之\x01",
            "今天真是辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x31,
        (
            "孩子们\x01",
            "是很开心……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x31,
        (
            "不过，也得\x01",
            "再努力点啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #146
        0x101,
        (
            "#1007F呜……\x01",
            "真，真丢脸。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x31,
        (
            "那样授课\x01",
            "可没法得到孩子们的信任哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x31,
        (
            "游击士是孩子们的憧憬，\x01",
            "所以要更加努力啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x101,
        (
            "#1007F是，知道了……\x01",
            "我会铭记于心的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x31,
        (
            "那么，我还有课\x01",
            "就此告辞了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x31,
        (
            "下次再有机会的话\x01",
            "还请多指教。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_8E(0x31, 0x10E3C, 0x1F4, 0x16D96, 0x7D0, 0x0)
    SetChrFlags(0x31, 0x80)
    Sleep(500)
    OP_72(0x10, 0x800)
    OP_6F(0x10, 20)
    OP_70(0x10, 0x0)
    OP_22(0x7, 0x0, 0x64)
    OP_73(0x10)
    OP_71(0x10, 0x800)

    def lambda_20C7():
        OP_6D(64560, 0, 94340, 2000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_20C7)
    Sleep(2000)
    TurnDirection(0xF7, 0x101, 400)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2151")

    ChrTalk(    #152
        0x106,
        "#057F……你上了什么课？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 400)

    ChrTalk(    #153
        0x104,
        (
            "#031F呼，我全都看见了……\x02\x03",

            "简直是超乎想象的授课呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2198")

    label("loc_2151")


    ChrTalk(    #154
        0x103,
        "#025F哈，好厉害的授课啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 400)

    ChrTalk(    #155
        0x104,
        "#031F呼，超乎想象的有趣啊。\x02",
    )

    CloseMessageWindow()

    label("loc_2198")


    ChrTalk(    #156
        0x127,
        "#151F真的好好玩啊～\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)
    OP_8C(0x101, 270, 400)

    ChrTalk(    #157
        0x101,
        (
            "#1022F啊～别说啦！\x01",
            "我心情都变差了！\x02\x03",

            "#1009F呜呜～今后我要好好学习～\x02\x03",

            "要把规章都\x01",
            "倒背如流！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2284")

    ChrTalk(    #158
        0x106,
        (
            "#053F嗯，好好努力吧。\x02\x03",

            "连规章都不熟悉的游击士\x01",
            "谁都不会信任你的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22D7")

    label("loc_2284")


    ChrTalk(    #159
        0x103,
        (
            "#026F嗯，好好努力吧。\x02\x03",

            "#027F身为游击士连规章都不知道\x01",
            "可是得不到别人信任的哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22D7")


    ChrTalk(    #160
        0x101,
        (
            "#1007F唉，果然是这样……\x02\x03",

            "#1002F好，我要加油！\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x106, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #161
        "\x07\x02任务【主日学校的讲师】\x07\x00失败了……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_2361")

    OP_30(0x0)
    EventEnd(0x0)
    Return()

    # Function_3_1A8B end

    def Function_4_2366(): pass

    label("Function_4_2366")

    EventBegin(0x0)
    SetChrPos(0x2F, 28180, 0, 90850, 325)
    OP_4A(0x2F, 255)
    OP_6D(22810, 0, 94820, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_23D9")
    AddParty(0x5, 0xF7, 0xFF)
    SetChrPos(0x106, 17370, 0, 97650, 24)
    Jump("loc_23F5")

    label("loc_23D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_23F5")
    AddParty(0x2, 0xF7, 0xFF)
    SetChrPos(0x103, 17370, 0, 97650, 24)

    label("loc_23F5")

    AddParty(0x3, 0xFF, 0xFF)
    SetChrPos(0x104, 17370, 0, 97650, 24)
    SetChrPos(0x101, 17370, 0, 97650, 24)
    SetChrPos(0x105, 17370, 0, 97650, 24)
    Sleep(1000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    OP_70(0xA, 0x1D)
    OP_73(0xA)
    Sleep(400)
    OP_43(0x101, 0x1, 0x1, 0x8)
    Sleep(500)
    OP_43(0x105, 0x1, 0x1, 0x9)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2478")
    OP_43(0x106, 0x1, 0x1, 0x6)
    Jump("loc_2486")

    label("loc_2478")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_2486")
    OP_43(0x103, 0x1, 0x1, 0x6)

    label("loc_2486")

    Sleep(500)
    OP_43(0x104, 0x1, 0x1, 0x7)
    Sleep(400)
    OP_72(0xA, 0x800)
    OP_6F(0xA, 29)
    OP_70(0xA, 0x0)
    OP_22(0x7, 0x0, 0x64)
    OP_73(0xA)
    OP_71(0xA, 0x800)
    WaitChrThread(0x104, 0x1)
    Sleep(600)

    ChrTalk(    #162
        0x101,
        (
            "#1000F呼，总算解决了。\x02\x03",

            "虽然做梦也没想到\x01",
            "结果会变成这样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x104,
        (
            "#030F真是事实更甚于小说……呢。\x02\x03",

            "#031F呼，能够顺利解决\x01",
            "身为协力人员的我也很得意啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)

    ChrTalk(    #164
        0x101,
        "#1019F你可是什么也没干啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #165
        0x101,
        (
            "#1006F啊，不过\x01",
            "真是非常感谢科洛丝啊。\x02\x03",

            "给了那么多忠告，\x01",
            "调查也帮了好多忙。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #166
        0x105,
        (
            "#048F呵呵，太好了。\x01",
            "看来帮上忙了。\x02\x03",

            "但是，艾丝蒂尔。\x01",
            "感谢就不必了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x101,
        (
            "#1008F是啊，你们俩\x01",
            "都是协力人员了嘛。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF7, 0x105, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_26A7")

    ChrTalk(    #168
        0x106,
        (
            "#050F啊啊，只是做了\x01",
            "该做的事而已。\x02\x03",

            "……那么，差不多该走了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26F2")

    label("loc_26A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_26F2")

    ChrTalk(    #169
        0x103,
        (
            "#020F呵呵，只是做了\x01",
            "该做的事而已。\x02\x03",

            "……那么，差不多该走了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26F2")

    TurnDirection(0x101, 0xF7, 400)

    ChrTalk(    #170
        0x101,
        "#1006F嗯，接下来该去蔡斯地区了。\x02",
    )

    CloseMessageWindow()
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #171
        "\x07\x02任务【选举事务所的伤人事件】\x07\x00完成了！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x69, 0x1, 0x8000)
    OP_28(0x69, 0x4, 0x10)
    EventEnd(0x0)
    OP_4B(0x2F, 255)
    Return()

    # Function_4_2366 end

    def Function_5_278B(): pass

    label("Function_5_278B")

    EventBegin(0x0)
    SetChrPos(0x2F, 28180, 0, 90850, 325)
    OP_4A(0x2F, 255)
    OP_6D(22810, 0, 94820, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_27ED")
    AddParty(0x5, 0xF7, 0xFF)
    Jump("loc_27F8")

    label("loc_27ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_27F8")
    AddParty(0x2, 0xF7, 0xFF)

    label("loc_27F8")

    SetChrPos(0xF7, 17370, 0, 97650, 24)
    AddParty(0x3, 0xFF, 0xFF)
    SetChrPos(0x104, 17370, 0, 97650, 24)
    SetChrPos(0x101, 24000, 0, 94500, 180)
    SetChrPos(0x105, 24000, 0, 93300, 0)
    Sleep(1000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    OP_70(0xA, 0x1D)
    OP_73(0xA)
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    def lambda_287B():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_287B)
    Sleep(50)

    def lambda_288E():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_288E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_28A7")
    OP_43(0x106, 0x1, 0x1, 0x6)
    Jump("loc_28B5")

    label("loc_28A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_28B5")
    OP_43(0x103, 0x1, 0x1, 0x6)

    label("loc_28B5")

    Sleep(500)
    OP_43(0x104, 0x1, 0x1, 0x7)
    WaitChrThread(0x104, 0x1)
    OP_72(0xA, 0x800)
    OP_6F(0xA, 29)
    OP_70(0xA, 0x0)
    OP_22(0x7, 0x0, 0x64)
    OP_73(0xA)
    OP_71(0x0, 0x800)
    Sleep(600)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_291C")

    ChrTalk(    #172
        0x106,
        (
            "#050F久等了……\x02\x03",

            "……那么，走吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2948")

    label("loc_291C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_2948")

    ChrTalk(    #173
        0x103,
        (
            "#020F久等了……\x02\x03",

            "……那么走吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2948")


    ChrTalk(    #174
        0x101,
        "#1002F那到底谁是犯人？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x104,
        "#031F呵呵，没想到居然是……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_29A6")

    ChrTalk(    #176
        0x106,
        "#057F喂，别说啦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_29CA")

    label("loc_29A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_29CA")

    ChrTalk(    #177
        0x103,
        "#026F不行哦，奥利维尔。\x02",
    )

    CloseMessageWindow()

    label("loc_29CA")


    ChrTalk(    #178
        0x101,
        (
            "#1009F啊～为什么嘛。\x01",
            "为什么不告诉我？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2A5B")

    ChrTalk(    #179
        0x106,
        (
            "#050F所谓保密义务吧。\x02\x03",

            "如果没有正当理由，\x01",
            "禁止公开工作内容。\x02\x03",

            "即使对方是游击士也不行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AC4")

    label("loc_2A5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_2AC4")

    ChrTalk(    #180
        0x103,
        (
            "#022F有保密义务吧。\x02\x03",

            "如果没有正当理由，\x01",
            "公开工作内容是禁止事项哦。\x02\x03",

            "即使对方是游击士也不行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AC4")


    ChrTalk(    #181
        0x101,
        "#1007F呜，是吗……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0xF7, 400)

    ChrTalk(    #182
        0x105,
        "#042F……好严格的规定。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF7, 0x105, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2B5C")

    ChrTalk(    #183
        0x106,
        (
            "#050F为了商务上的信誉嘛。\x02\x03",

            "#552F所以爱说漏嘴的家伙\x01",
            "可不适合这工作……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BA7")

    label("loc_2B5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_2BA7")

    ChrTalk(    #184
        0x103,
        (
            "#027F为了工作上的信誉嘛。\x02\x03",

            "所以爱说漏嘴的人\x01",
            "可不适合这工作……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BA7")


    ChrTalk(    #185
        0x104,
        (
            "#033F哎呀，那眼神是什么意思？\x02\x03",

            "#035F呼，你们真是多心了……\x01",
            "我的嘴可不是『漏』哦。\x02\x03",

            "只不过是有点『滑』罢了。\x01",
            "就像上等的香槟气泡一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x101,
        (
            "#1019F是是，你就一辈子都这么说吧。\x02\x03",

            "#1015F唉～唉，不过工作\x01",
            "只要坚持都会有结果的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF7, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2CD9")

    ChrTalk(    #187
        0x106,
        (
            "#053F嗯，不能放弃工作嘛。\x02\x03",

            "#050F……那么，差不多该走了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D1B")

    label("loc_2CD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_2D1B")

    ChrTalk(    #188
        0x103,
        (
            "#020F嗯，放弃工作可不行啊。\x02\x03",

            "……那，差不多该走了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D1B")

    EventEnd(0x0)
    OP_4B(0x2F, 255)
    Return()

    # Function_5_278B end

    def Function_6_2D22(): pass

    label("Function_6_2D22")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 19260, 1200, 94200, 86)

    def lambda_2D44():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2D44)
    OP_90(0xFE, 0x5DC, 0x0, 0x0, 0x5DC, 0x0)
    OP_8E(0xFE, 0x57F8, 0x0, 0x17124, 0x5DC, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_6_2D22 end

    def Function_7_2D80(): pass

    label("Function_7_2D80")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 19260, 1200, 93800, 86)

    def lambda_2DA2():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2DA2)
    OP_90(0xFE, 0x5DC, 0x0, 0x0, 0x5DC, 0x0)
    OP_8E(0xFE, 0x56B8, 0x0, 0x16D1E, 0x5DC, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_7_2D80 end

    def Function_8_2DDE(): pass

    label("Function_8_2DDE")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 19260, 1200, 94200, 86)

    def lambda_2E00():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2E00)
    OP_90(0xFE, 0x5DC, 0x0, 0x0, 0x5DC, 0x0)
    OP_8E(0xFE, 0x5DC0, 0x0, 0x17124, 0x5DC, 0x0)
    Sleep(200)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_8_2DDE end

    def Function_9_2E41(): pass

    label("Function_9_2E41")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 19260, 1200, 93800, 86)

    def lambda_2E63():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2E63)
    OP_90(0xFE, 0x5DC, 0x0, 0x0, 0x5DC, 0x0)
    OP_8E(0xFE, 0x5C94, 0x0, 0x16D1E, 0x5DC, 0x0)
    Sleep(200)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_9_2E41 end

    SaveToFile()

Try(main)
