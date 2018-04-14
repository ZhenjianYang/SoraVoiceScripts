from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1103_1 ._SN',
        MapName             = 'Bose',
        Location            = 'T1103.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T1103   ._SN',
            'ED6_DT21/T1103_1 ._SN',
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
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    TalkBegin(0x35)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C0")
    TurnDirection(0x4, 0x35, 0)

    label("loc_C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x1, 0x2000)"), scpexpr(EXPR_END)), "loc_10B")
    TurnDirection(0x35, 0x101, 400)

    ChrTalk(    #0
        0x35,
        "怎么了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x35,
        "不是很着急吗？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x35, 0, 0)
    TalkEnd(0x35)
    Return()

    label("loc_10B")

    Fade(1000)
    EventBegin(0x0)
    OP_6D(47700, 0, 47800, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2700, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0xF6, 48200, 0, 48120, 90)
    SetChrPos(0xF7, 48100, 0, 47360, 90)
    SetChrPos(0xF8, 47200, 0, 48130, 90)
    SetChrPos(0xF9, 47100, 0, 47320, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B0")
    SetChrPos(0x4, 46150, 0, 47720, 90)

    label("loc_1B0")

    OP_0D()
    OP_62(0x35, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0x35)
    TurnDirection(0x35, 0x101, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x1, 0x2000)"), scpexpr(EXPR_END)), "loc_28F")

    ChrTalk(    #2
        0x35,
        "哦，是你啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x101,
        (
            "#1007F前阵子真不好意思。\x01",
            "招呼才打了一半就走了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x35,
        "哪里，不用在意。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x35,
        (
            "游击士的工作\x01",
            "好像很忙嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        (
            "#1006F托你的福吧。\x02\x03",

            "叔叔现在\x01",
            "在柏斯做生意？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B9")

    label("loc_28F")


    ChrTalk(    #7
        0x35,
        "啊，你是……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x65, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_46A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_415")

    ChrTalk(    #8
        0x101,
        (
            "#1000F啊，好久不见。\x01",
            "这不是在卢安的商人吗。\x02\x03",

            "在柏斯做生意吗？\x02\x03",

            "#1007F……现在可不是悠闲\x01",
            "让大家自我介绍的时候。\x02\x03",

            "得抓紧时间赶去拉文努村。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x35,
        "看来你们很忙啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x35,
        (
            "看起来\x01",
            "你们正在调查事件？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        (
            "#1002F嗯……\x01",
            "正是这样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x35,
        (
            "是吗……\x01",
            "路上要小心啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x35,
        (
            "等下次有机会\x01",
            "再聊聊近况吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        (
            "#1002F叔叔也要小心。\x02\x03",

            "那么，失陪了。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x7B, 0x1, 0x2000)
    OP_8C(0x35, 0, 0)
    EventEnd(0x0)
    TalkEnd(0x35)
    Return()

    label("loc_415")


    ChrTalk(    #15
        0x101,
        (
            "#1004F啊……\x01",
            "这不是玛诺利亚村的商人吗。\x02\x03",

            "#1000F好久不见了。\x01",
            "在柏斯做生意吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B9")

    label("loc_46A")


    ChrTalk(    #16
        0x101,
        (
            "#1004F啊，我还在想是谁呢……\x02\x03",

            "真是\x01",
            "好久不见了呀。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4CC")

    ChrTalk(    #17
        0x106,
        "#052F熟人吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)
    Jump("loc_558")

    label("loc_4CC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4FF")

    ChrTalk(    #18
        0x103,
        "#023F哎呀，是熟人吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)
    Jump("loc_558")

    label("loc_4FF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_52E")

    ChrTalk(    #19
        0x108,
        "#070F噢，熟人啊？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x108, 400)
    Jump("loc_558")

    label("loc_52E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_558")

    ChrTalk(    #20
        0x104,
        "#030F是熟人吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)

    label("loc_558")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_64C")

    ChrTalk(    #21
        0x101,
        (
            "#1000F嗯，这个人\x01",
            "是做食材生意的商人……\x02\x03",

            "#1007F……现在好像不是悠闲\x01",
            "让大家自我介绍的时候。\x02\x03",

            "得抓紧时间赶去拉文努村。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x35,
        "看来你们很忙啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x35,
        "那么，有机会再见吧。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x35, 400)

    ChrTalk(    #24
        0x101,
        (
            "#1002F啊，嗯。\x01",
            "那么失陪了。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x7B, 0x1, 0x2000)
    OP_8C(0x35, 0, 0)
    EventEnd(0x0)
    TalkEnd(0x35)
    Return()

    label("loc_64C")


    ChrTalk(    #25
        0x101,
        (
            "#1000F嗯，这个人\x01",
            "做食材生意的商人。\x02\x03",

            "很早以前\x01",
            "接受过他的委托。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x35, 400)

    ChrTalk(    #26
        0x101,
        "#1011F现在到柏斯来做生意吗？\x02",
    )

    CloseMessageWindow()

    label("loc_6B9")


    ChrTalk(    #27
        0x35,
        "嗯嗯，为了拓展业务而来。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x35,
        (
            "跟『安特洛丝餐厅』谈成生意\x01",
            "是此次柏斯之行的最终目标……\x02\x03",

            "在这之前本来打算\x01",
            "先到超市兜售寻找买家。\x02\x03",

            "不过，很遗憾……\x01",
            "在那之前出事了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #29
        0x101,
        (
            "#1015F以『安特洛丝餐厅』为目的\x01",
            "为什么却要去超市兜售呢？\x02\x03",

            "听起来有些不太明白呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x35,
        (
            "嗯，当然我也是很想\x01",
            "直接联系那里的……\x02\x03",

            "但听说那里如果没有介绍人，\x01",
            "好像连话也不会听你说一句。\x02\x03",

            "嘿，谁让它那么大名气，\x01",
            "这也是理所当然的嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        (
            "#1004F啊～不愧是『安特洛丝餐厅』。\x01",
            "门坎还真不是一般的高哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x35,
        (
            "话说回来，你们\x01",
            "也在这城里做事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        (
            "#1015F唔，一言难尽……吧。\x02\x03",

            "#1011F啊，对了\x01",
            "说到工作……\x02\x03",

            "那个『安特洛丝餐厅』\x01",
            "委托给我们一个任务呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_969")

    ChrTalk(    #34
        0x106,
        (
            "#050F啊啊，是收集\x01",
            "珍贵食材的事。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A17")

    label("loc_969")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9A0")

    ChrTalk(    #35
        0x103,
        (
            "#020F委托内容是\x01",
            "收集珍贵食材呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A17")

    label("loc_9A0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9E3")

    ChrTalk(    #36
        0x108,
        (
            "#070F啊啊，我记得委托内容\x01",
            "是收集珍贵食材吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A17")

    label("loc_9E3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A17")

    ChrTalk(    #37
        0x104,
        (
            "#030F嗯，是收集\x01",
            "珍贵食材的事呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A17")

    OP_62(0x35, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #38
        0x35,
        (
            "什，什么？\x01",
            "食、食材的收集……！？\x02\x03",

            "而且还是，那个\x01",
            "『安特洛丝餐厅』委托的！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x101,
        (
            "#1007F这可是相当\x01",
            "麻烦的工作哦。\x02\x03",

            "必须收集的食材中\x01",
            "有相当珍贵的东西呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x35,
        (
            "嗯～唔，这可真有趣。\x02\x03",

            "那，需要怎样的食材？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x101,
        (
            "#1015F嗯～稍等一下。\x01",
            "我先看看手册……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #42
        (
            "\x07\x05给奥维德看安特洛丝\x01",
            "订的食材清单。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #43
        0x35,
        (
            "哈哈哈，这也，不过如此嘛。\x02\x03",

            "要是这些食材的话，\x01",
            "我这里随时都有。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x101,
        "#1004F啊啊！？真的！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C27")

    ChrTalk(    #45
        0x109,
        (
            "#1060F哈～这简直就是\x01",
            "女神的指引嘛。\x02\x03",

            "希望\x01",
            "能助我们一臂之力。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D58")

    label("loc_C27")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C76")

    ChrTalk(    #46
        0x104,
        (
            "#030F呵，这真是太好了。\x02\x03",

            "诸位，这下就正好\x01",
            "请他帮个忙吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D58")

    label("loc_C76")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CC3")

    ChrTalk(    #47
        0x108,
        (
            "#070F噢哟，这可真是太好了。\x02\x03",

            "希望您\x01",
            "能助我们一臂之力。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D58")

    label("loc_CC3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D10")

    ChrTalk(    #48
        0x103,
        (
            "#020F哎呀，这可真是太好了。\x02\x03",

            "希望您\x01",
            "能助我们一臂之力。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D58")

    label("loc_D10")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D58")

    ChrTalk(    #49
        0x106,
        (
            "#051F呼，这可真是太好了。\x02\x03",

            "希望您\x01",
            "能助我们一臂之力。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D58")


    ChrTalk(    #50
        0x35,
        (
            "啊啊，我也想拜托你们。\x01",
            "这可是绝好的机会啊。\x02\x03",

            "食材我会免费提供，\x01",
            "请务必帮我做个介绍。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x101,
        (
            "#1017F是，是这样啊……\x02\x03",

            "嗯，这样的话\x01",
            "就麻烦你了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x35,
        "嗯，请多关照了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F2)
    NewScene("ED6_DT21/T1131   ._SN", 103, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    TalkEnd(0x35)
    Return()

    # Function_0_AA end

    SaveToFile()

Try(main)
