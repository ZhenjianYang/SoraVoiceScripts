from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T1101_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T1101_1 ._SN',
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
        "Function_1_1B0",          # 01, 1
        "Function_2_272",          # 02, 2
        "Function_3_39E",          # 03, 3
        "Function_4_9CD",          # 04, 4
        "Function_5_157B",         # 05, 5
        "Function_6_192D",         # 06, 6
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x13), scpexpr(EXPR_PUSH_LONG, 0x381), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B7")
    Return()

    label("loc_B7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C9")
    Return()

    label("loc_C9")

    SetMapFlags(0x80)
    OP_C0(0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(30)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0xA)"), scpexpr(EXPR_END)), "loc_104")
    Call(1, 1)
    Jump("loc_1A9")

    label("loc_104")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0x11)"), scpexpr(EXPR_END)), "loc_113")
    Call(1, 2)
    Jump("loc_1A9")

    label("loc_113")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0xFF)"), scpexpr(EXPR_END)), "loc_16B")
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #0
        (
            "\x07\x05试着出示了照片，\x01",
            "但似乎没有见过的印象。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jump("loc_1A9")

    label("loc_16B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        "\x07\x05附近没有人可以确认照片。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_1A9")

    OP_0D()
    ClearMapFlags(0x80)
    Return()

    # Function_0_AA end

    def Function_1_1B0(): pass

    label("Function_1_1B0")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_202")

    ChrTalk(    #2
        0xA,
        (
            "嗯，照片上的小女孩\x01",
            "确实有见过的印象……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xA,
        "哎呀，是谁来着呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_26E")

    label("loc_202")


    ChrTalk(    #4
        0xA,
        "啊，那个照片……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        "#1004F认识这女孩吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(    #6
        0xA,
        "嗯，有见过的印象……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xA,
        "哎呀，是谁来着呢。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_26E")

    TalkEnd(0xA)
    Return()

    # Function_1_1B0 end

    def Function_2_272(): pass

    label("Function_2_272")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34A, 3)), scpexpr(EXPR_END)), "loc_396")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_2EC")

    ChrTalk(    #8
        0x11,
        (
            "这个情况……\x01",
            "线索是头发的颜色……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x11,
        (
            "表情伴随着成长\x01",
            "有了很大的变化……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x11,
        "……不能先入为主。\x02",
    )

    CloseMessageWindow()
    Jump("loc_393")

    label("loc_2EC")


    ChrTalk(    #11
        0x11,
        "……行踪调查正在进行啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x11,
        "………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x11,
        (
            "这个情况……\x01",
            "线索是头发的颜色……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x11,
        (
            "表情伴随着成长\x01",
            "有了很大的变化……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x11,
        "……不能先入为主。\x02",
    )

    CloseMessageWindow()
    OP_A2(0xB)

    label("loc_393")

    Jump("loc_39A")

    label("loc_396")

    Call(0, 12)

    label("loc_39A")

    TalkEnd(0x11)
    Return()

    # Function_2_272 end

    def Function_3_39E(): pass

    label("Function_3_39E")

    EventBegin(0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x8, 33010, 0, 74070, 180)
    SetChrPos(0x9, 33850, 0, 74840, 180)
    OP_4A(0xE, 255)
    SetChrFlags(0x0, 0x8)
    SetChrFlags(0x1, 0x8)
    SetChrFlags(0x2, 0x8)
    SetChrFlags(0x3, 0x8)
    OP_6D(48680, 0, 82940, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3470, 0)
    OP_6C(46000, 0)
    OP_6E(262, 0)

    def lambda_427():
        OP_67(0, 7520, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_427)

    def lambda_43F():
        OP_6B(2800, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_43F)

    def lambda_44F():
        OP_6C(359000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_44F)

    def lambda_45F():
        OP_8E(0x8, 0x80F2, 0x0, 0x10338, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_45F)
    Sleep(150)

    def lambda_47F():
        OP_8E(0x9, 0x843A, 0x0, 0x1063A, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_47F)
    OP_6D(33430, 0, 67300, 6000)
    WaitChrThread(0x8, 0x1)
    WaitChrThread(0x101, 0x3)
    Sleep(400)
    TurnDirection(0x8, 0x9, 400)

    ChrTalk(    #16
        0x8,
        "#610F对了，莉拉。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 400)

    ChrTalk(    #17
        0x9,
        "#620F是，小姐。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        (
            "#610F关于刚才的事……\x02\x03",

            "你定在什么时候？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x9,
        (
            "#620F回乡的日期吗？\x02\x03",

            "嗯，当然\x01",
            "还没决定……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x8,
        (
            "#610F是吗……\x02\x03",

            "决定了的话，\x01",
            "就尽快告诉我。\x02\x03",

            "我也得调整\x01",
            "日程表才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x9,
        "#622F小姐您吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        (
            "#610F嗯，我也打算\x01",
            "一起去呢。\x02\x03",

            "你的故乡是怎样的地方，\x01",
            "我很想亲眼看看呢。\x02\x03",

            "而且……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x9,
        "#624F而且……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        (
            "#610F还想听听各种\x01",
            "莉拉小时候的事。\x02\x03",

            "你不也听我父亲\x01",
            "说了许多我的事吗？\x02\x03",

            "要是我不掌握点你的弱点\x01",
            "交易就不公平了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x9,
        (
            "#621F原来如此，目的是这个啊……\x02\x03",

            "#620F不过，恐怕会让您失望，\x01",
            "我小时候可是绝对的品行端正。\x02\x03",

            "跟任性妄为的小姐不同，\x01",
            "我可没什么把柄怕能让您知道。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        (
            "#611F哎呀，这可难说。\x02\x03",

            "最好还是别小看\x01",
            "我的交涉手腕哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x9,
        (
            "#621F呵呵，那就期待您的表现了。\x02\x03",

            "那么，回乡的日期\x01",
            "随后就会告知给您。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        (
            "#610F嗯，拜托了。\x02\x03",

            "好了，今天的预定行程\x01",
            "是怎么安排的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x9,
        (
            "#620F是，午茶时间以前\x01",
            "需要回市长官邸办公……\x02\x03",

            "此后，还有超市的\x01",
            "新成员加入审查会。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #30
        0x8,
        (
            "#613F呀，审查会\x01",
            "是今天！？\x02\x03",

            "不，不得了，\x01",
            "得先看一遍文件才行。\x02\x03",

            "#614F莉拉，要赶快了！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8B2():

        label("loc_8B2")

        TurnDirection(0x9, 0x8, 400)
        OP_48()
        Jump("loc_8B2")

    QueueWorkItem2(0x9, 1, lambda_8B2)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0x8, 0x80F2, 0x0, 0xE678, 0x1388, 0x0)

    ChrTalk(    #31
        0x9,
        (
            "#623F呼，真是的……\x02\x03",

            "照这个情形，休假什么的\x01",
            "根本就是遥不可及嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x9, 0x1)

    def lambda_933():
        OP_8E(0x9, 0x843A, 0x0, 0xE678, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_933)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    ClearChrFlags(0x0, 0x8)
    ClearChrFlags(0x1, 0x8)
    ClearChrFlags(0x2, 0x8)
    ClearChrFlags(0x3, 0x8)
    OP_6D(36200, 400, 79200, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Sleep(1000)
    EventEnd(0x0)
    FadeToBright(2000, 0)
    OP_0D()
    OP_4B(0xA, 255)
    OP_4B(0xE, 255)
    Return()

    # Function_3_39E end

    def Function_4_9CD(): pass

    label("Function_4_9CD")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9E3")
    TurnDirection(0x4, 0xD, 0)

    label("loc_9E3")

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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A88")
    SetChrPos(0x4, 46150, 0, 47720, 90)

    label("loc_A88")

    OP_0D()
    OP_62(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0xD)
    TurnDirection(0xD, 0x101, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x1, 0x2000)"), scpexpr(EXPR_END)), "loc_B67")

    ChrTalk(    #32
        0xD,
        "哦，是你啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        (
            "#1007F前阵子真不好意思。\x01",
            "招呼才打了一半就走了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xD,
        "哪里，不用在意。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xD,
        (
            "游击士的工作\x01",
            "好像很忙嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x101,
        (
            "#1006F托你的福吧。\x02\x03",

            "叔叔现在\x01",
            "在柏斯做生意？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E2F")

    label("loc_B67")


    ChrTalk(    #37
        0xD,
        "啊，你是……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x65, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_BD8")

    ChrTalk(    #38
        0x101,
        (
            "#1004F啊……\x01",
            "这不是玛诺利亚村的商人吗。\x02\x03",

            "#1000F好久不见了。\x01",
            "在柏斯做生意吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E2F")

    label("loc_BD8")


    ChrTalk(    #39
        0x101,
        (
            "#1004F啊，我还在想是谁呢……\x02\x03",

            "#1001F真的是\x01",
            "好久不见了呀。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C42")

    ChrTalk(    #40
        0x106,
        "#052F熟人吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)
    Jump("loc_CCE")

    label("loc_C42")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C75")

    ChrTalk(    #41
        0x103,
        "#023F哎呀，是熟人吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)
    Jump("loc_CCE")

    label("loc_C75")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CA4")

    ChrTalk(    #42
        0x108,
        "#070F呼，熟人啊？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x108, 400)
    Jump("loc_CCE")

    label("loc_CA4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CCE")

    ChrTalk(    #43
        0x104,
        "#030F是熟人吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)

    label("loc_CCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DC0")

    ChrTalk(    #44
        0x101,
        (
            "#1000F嗯，这个人\x01",
            "是做食材生意的商人……\x02\x03",

            "#1007F……现在可不是悠闲\x01",
            "让大家自我介绍的时候。\x02\x03",

            "得抓紧时间赶去拉文努村。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xD,
        "看来你们很忙啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xD,
        "那么，有机会再见吧。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xD, 400)

    ChrTalk(    #47
        0x101,
        (
            "#1002F啊，嗯。\x01",
            "那么失陪了。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x7B, 0x1, 0x2000)
    OP_8C(0xD, 0, 0)
    EventEnd(0x0)
    TalkEnd(0xD)
    Return()

    label("loc_DC0")


    ChrTalk(    #48
        0x101,
        (
            "#1000F嗯，这个人\x01",
            "是做食材生意的商人。\x02\x03",

            "很早以前\x01",
            "接受过他的委托。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xD, 400)

    ChrTalk(    #49
        0x101,
        "#1011F现在到柏斯来做生意吗？\x02",
    )

    CloseMessageWindow()

    label("loc_E2F")


    ChrTalk(    #50
        0xD,
        "嗯嗯，为了拓展业务而来。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xD,
        (
            "跟『安特洛丝餐厅』谈成生意\x01",
            "是此次柏斯之行的最终目标……\x02\x03",

            "不过首先还是脚踏实地\x01",
            "到超市兜售一下食材吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #52
        0x101,
        (
            "#1015F以『安特洛丝餐厅』为目的，\x01",
            "为什么却要去超市兜售呢？\x02\x03",

            "听起来有些不太明白呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xD,
        (
            "嗯，当然我也是很想\x01",
            "直接联系那里的……\x02\x03",

            "但听说那里如果没有介绍人，\x01",
            "好像连话也不会听你说一句。\x02\x03",

            "嘿，谁让它那么大的名气呢，\x01",
            "这也是理所当然的嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x101,
        (
            "#1004F啊～不愧是『安特洛丝餐厅』。\x01",
            "门坎还真不是一般的高哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xD,
        (
            "话说回来，你们\x01",
            "也在这城里做事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10C6")

    ChrTalk(    #57
        0x106,
        (
            "#050F啊啊，是收集\x01",
            "珍贵食材的事。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1174")

    label("loc_10C6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10FD")

    ChrTalk(    #58
        0x103,
        (
            "#020F委托内容是\x01",
            "收集珍贵食材呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1174")

    label("loc_10FD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1140")

    ChrTalk(    #59
        0x108,
        (
            "#070F啊啊，我记得委托内容\x01",
            "是收集珍贵食材吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1174")

    label("loc_1140")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1174")

    ChrTalk(    #60
        0x104,
        (
            "#030F嗯，是收集\x01",
            "珍贵食材的事呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1174")

    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #61
        0xD,
        (
            "什，什么？\x01",
            "食、食材的收集……！？\x02\x03",

            "而且还是，那个\x01",
            "『安特洛丝餐厅』委托的！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        (
            "#1007F这可是相当\x01",
            "麻烦的工作哦。\x02\x03",

            "必须收集的食材中\x01",
            "有相当珍贵的东西呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xD,
        (
            "嗯～唔，这可真有趣。\x02\x03",

            "那，需要怎样的食材？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        (
            "#1015F嗯～稍等一下。\x01",
            "我先看看手册……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #65
        (
            "\x07\x05给奥维德看安特洛丝\x01",
            "订的食材清单。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #66
        0xD,
        (
            "哈哈哈，这也，不过如此嘛。\x02\x03",

            "要是这些食材的话，\x01",
            "我这里随时都有。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x101,
        "#1004F啊啊！？真的！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1386")

    ChrTalk(    #68
        0x109,
        (
            "#1060F哈～这简直就是\x01",
            "女神的指引嘛。\x02\x03",

            "希望您\x01",
            "能助我们一臂之力。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14B7")

    label("loc_1386")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13D5")

    ChrTalk(    #69
        0x104,
        (
            "#030F呵，这真是太好了。\x02\x03",

            "诸位，这下就正好\x01",
            "请他帮个忙吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14B7")

    label("loc_13D5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1422")

    ChrTalk(    #70
        0x108,
        (
            "#070F噢哟，这可真是太好了。\x02\x03",

            "希望您\x01",
            "能助我们一臂之力。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14B7")

    label("loc_1422")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_146F")

    ChrTalk(    #71
        0x103,
        (
            "#020F哎呀，这可真是太好了。\x02\x03",

            "希望您\x01",
            "能助我们一臂之力。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14B7")

    label("loc_146F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14B7")

    ChrTalk(    #72
        0x106,
        (
            "#051F呼，这可真是太好了。\x02\x03",

            "希望您\x01",
            "能助我们一臂之力。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14B7")


    ChrTalk(    #73
        0xD,
        (
            "啊啊，我也想拜托你们。\x01",
            "这可是绝好的机会啊。\x02\x03",

            "食材我会免费提供，\x01",
            "请务必帮我做个介绍。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x101,
        (
            "#1017F是，是这样啊……\x02\x03",

            "嗯，这样的话\x01",
            "就麻烦你了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xD,
        "嗯，请多关照了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F2)
    NewScene("ED6_DT21/T1131   ._SN", 103, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    TalkEnd(0xD)
    Return()

    # Function_4_9CD end

    def Function_5_157B(): pass

    label("Function_5_157B")

    EventBegin(0x0)
    Fade(1000)
    OP_4A(0x12, 255)
    SetChrPos(0x12, 19300, 0, 48720, 135)
    SetChrPos(0x101, 20510, 0, 47110, 320)
    SetChrPos(0xF7, 21430, 0, 47400, 315)
    SetChrPos(0xF8, 21520, 0, 46030, 315)
    SetChrPos(0xF9, 22470, 0, 46390, 315)
    OP_6D(20450, 0, 47700, 0)
    OP_67(0, 8520, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(359000, 0)
    OP_6E(262, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7C, 0x1, 0x4000)"), scpexpr(EXPR_END)), "loc_1665")

    ChrTalk(    #76
        0x12,
        "已经准备好了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x101,
        (
            "#1006F嗯，久等了。\x02\x03",

            "那么，出发吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1903")

    label("loc_1665")


    ChrTalk(    #78
        0x12,
        "喔，我可等好久了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x12,
        "赶快出发吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x101,
        (
            "#1006F嗯，走吧。\x02\x03",

            "目的地拉文努村吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1721")

    ChrTalk(    #81
        0x106,
        (
            "#050F啊啊，虽然是走惯了的路\x01",
            "但可别忘了有人同行啊。\x02\x03",

            "途中的魔兽\x01",
            "要尽可能的避开哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_185C")

    label("loc_1721")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1787")

    ChrTalk(    #82
        0x103,
        (
            "#020F嗯，虽然是走惯了的路\x01",
            "但可别忘了有人同行哦。\x02\x03",

            "途中的魔兽\x01",
            "要尽可能的避开哟。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_185C")

    label("loc_1787")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17F5")

    ChrTalk(    #83
        0x108,
        (
            "#070F啊啊，虽然怎么走应该都知道，\x01",
            "但可别忘了有人同行哦。\x02\x03",

            "途中的魔兽\x01",
            "要尽可能的避开哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_185C")

    label("loc_17F5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_185C")

    ChrTalk(    #84
        0x104,
        (
            "#030F呼，走什么路都知道的吧。\x01",
            "不过这次有人同行哦。\x02\x03",

            "途中的魔兽\x01",
            "要尽可能的避开它们。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_185C")


    ChrTalk(    #85
        0x12,
        (
            "是呀，没有意义的战斗…\x01",
            "而是尽量避开为好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x12,
        (
            "根据工作的质量好坏，\x01",
            "奖金也会增加哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x101,
        (
            "#1006F那我好好努力一下，\x01",
            "争取不辜负大家的期望。\x02\x03",

            "#1018F那么，出发前进！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1903")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_28(0x7C, 0x1, 0x4)
    OP_28(0x7C, 0x4, 0x8)
    OP_CE(0x0, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x15), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    AddParty(0x46, 0xFF, 0xFF)
    NewScene("ED6_DT21/R1200   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_157B end

    def Function_6_192D(): pass

    label("Function_6_192D")

    EventBegin(0x0)
    RemoveParty(0x46, 0xFF)
    SetChrPos(0x12, 19300, 0, 48720, 135)
    OP_4A(0x12, 255)
    SetChrPos(0x101, 20510, 0, 47110, 320)
    SetChrPos(0xF7, 21430, 0, 47400, 315)
    SetChrPos(0xF8, 21520, 0, 46030, 315)
    SetChrPos(0xF9, 22470, 0, 46390, 315)
    OP_6D(20450, 0, 47700, 0)
    OP_67(0, 8520, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(359000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(    #88
        0x12,
        (
            "怎么了？\x01",
            "城里还有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x101,
        (
            "#1006F嗯，要回去一趟，\x01",
            "需要准备一下。\x02\x03",

            "马上回来，\x01",
            "还在这里集合吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x12,
        "麻烦快点咯。\x02",
    )

    CloseMessageWindow()
    OP_28(0x7C, 0x1, 0x4000)
    OP_28(0x7C, 0x3, 0x8)
    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x15), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A5E")
    OP_28(0x7C, 0x1, 0x2000)

    label("loc_1A5E")

    OP_4B(0x12, 255)
    SetChrPos(0x12, 19300, 0, 48720, 180)
    EventEnd(0x0)
    Return()

    # Function_6_192D end

    SaveToFile()

Try(main)
