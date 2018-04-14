from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 洛连特

    CreateScenaFile(
        FileName            = 'C2219_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60015",
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
        "Function_1_175E",         # 01, 1
        "Function_2_182A",         # 02, 2
        "Function_3_19C0",         # 03, 3
        "Function_4_1B6C",         # 04, 4
        "Function_5_1D1F",         # 05, 5
        "Function_6_1F59",         # 06, 6
        "Function_7_20CB",         # 07, 7
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6B, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x6B, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FDD")
    OP_8C(0xFE, 270, 0)
    OP_4A(0xFE, 0)
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -1410, 0, 201500, 270)
    SetChrPos(0xF7, -1250, 0, 202500, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_124")
    SetChrPos(0x104, 0, 0, 201500, 270)
    SetChrPos(0x105, 250, 0, 202500, 270)
    Jump("loc_176")

    label("loc_124")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x26)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_157")
    SetChrPos(0x104, 0, 0, 201500, 270)
    SetChrPos(0x127, 250, 0, 202500, 270)
    Jump("loc_176")

    label("loc_157")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_176")
    SetChrPos(0x109, 125, 0, 202000, 270)

    label("loc_176")

    OP_6D(-1660, 0, 202610, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()
    Sleep(400)

    ChrTalk(    #0
        0xFE,
        (
            "嗯……\x01",
            "还有点痛呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        "这下可不能逞强了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x1C, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_201")
    OP_A2(0xA)
    Jump("loc_204")

    label("loc_201")

    OP_A3(0xA)

    label("loc_204")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_295")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "◇前篇完成过【灯塔的魔兽扫荡】或者【整备用箱子的搬运】\x01",      # 0
            "◇两个都没完成\x01",                                              # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_292")
    OP_A2(0xA)
    Jump("loc_295")

    label("loc_292")

    OP_A3(0xA)

    label("loc_295")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_440")

    ChrTalk(    #2
        0x101,
        "#1001F老爷爷，好久不见！\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x101, 400)
    Sleep(1000)

    ChrTalk(    #3
        0xFE,
        "哎呀，怎么是你啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        "看起来还是那么有精神啊。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3BF")

    ChrTalk(    #5
        0x106,
        (
            "#051F啊啊，想起来了……\x02\x03",

            "这不就是黑衣人事件中\x01",
            "被催眠的老爷爷吗?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(    #6
        0x101,
        "#1001F嗯，是守灯塔的弗科特先生。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #7
        0x101,
        (
            "#1000F好久不见了，\x01",
            "老爷爷您还好吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43D")

    label("loc_3BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_43D")
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #8
        0x103,
        "#023F难道之前你们见过吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #9
        0x101,
        "#1000F嗯，说来话长。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #10
        0x101,
        (
            "#1000F好久不见了，\x01",
            "老爷爷您还好吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43D")

    Jump("loc_637")

    label("loc_440")


    ChrTalk(    #11
        0x101,
        "#1000F老爷爷，好久不见呢。\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x101, 400)
    Sleep(1000)
    OP_62(0xFE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1500)

    ChrTalk(    #12
        0xFE,
        "咦，你是？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x101,
        (
            "#1016F啊，对哦。\x01",
            "嗯，不记得了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_548")

    ChrTalk(    #14
        0x106,
        (
            "#051F啊啊，想起来了……\x02\x03",

            "是黑衣人事件中\x01",
            "被催眠的老爷爷吗?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(    #15
        0x101,
        "#1000F对，是守灯塔的老爷爷。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5A1")

    label("loc_548")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_5A1")
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #16
        0x103,
        "#023F以前见过吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #17
        0x101,
        (
            "#1015F嗯，这个地方\x01",
            "就是那次事件的现场。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A1")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #18
        0xFE,
        (
            "哦，这样啊。\x01",
            "事件发生的时候你们也过来啊……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #19
        0x101,
        (
            "#1006F嗯，就是那个时候的游击士哦。\x02\x03",

            "好久不见了，\x01",
            "老爷爷您还好吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_637")


    ChrTalk(    #20
        0xFE,
        (
            "还好吧，\x01",
            "就是近来总有点……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #21
        0xFE,
        "……啊，痛痛痛！\x02",
    )

    CloseMessageWindow()
    OP_8C(0xF7, 270, 400)

    ChrTalk(    #22
        0x101,
        (
            "#1004F怎、怎么了！？\x02\x03",

            "您、您看起来\x01",
            "不是很精神呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "嗯，最近\x01",
            "腰痛又发作了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "只要一弯腰\x01",
            "就疼得好厉害啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_746")

    ChrTalk(    #25
        0x105,
        "#043F啊，这可真够难受啊……\x02",
    )

    CloseMessageWindow()

    label("loc_746")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_769")

    ChrTalk(    #26
        0x106,
        "#052F好像很难受啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_789")

    label("loc_769")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_789")

    ChrTalk(    #27
        0x103,
        "#022F好像很难受啊。\x02",
    )

    CloseMessageWindow()

    label("loc_789")


    ChrTalk(    #28
        0x101,
        "#1015F没有什么药吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "已经是老毛病了。\x01",
            "事到如今也不可能治好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "只能静静地待着\x01",
            "等疼痛减轻了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "唉，不过老实说\x01",
            "还真没办法休息……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x101,
        "#1011F咦……？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "【有什么事情吗？】\x01",        # 0
            "【啊，请多保重……】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A0F")
    OP_28(0x6B, 0x4, 0x40)
    OP_A2(0x0)

    ChrTalk(    #33
        0x101,
        "#1000F啊，请您多保重啊。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_90E")

    ChrTalk(    #34
        0xFE,
        "………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "……呼，还是那么\x01",
            "不机灵啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_965")

    label("loc_90E")


    ChrTalk(    #36
        0xFE,
        "………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        "……呼，哎呀呀。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "近来的游击士\x01",
            "真是一点儿也不机灵呀。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_965")


    ChrTalk(    #39
        0x101,
        "#1004F咦？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        "算了，没什么事。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        "……哦，不好不好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "一不留神\x01",
            "就光顾着说话了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "好了，你们也要\x01",
            "努力工作啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x101,
        "#1006F那么，您多保重。\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    OP_8C(0xFE, 270, 0)
    OP_4B(0xFE, 0)
    Jump("loc_FCD")

    label("loc_A0F")

    OP_28(0x6B, 0x4, 0x2)
    OP_28(0x6B, 0x4, 0x4)
    OP_28(0x6B, 0x4, 0x8)
    OP_65(0x0, 0x1)

    ChrTalk(    #45
        0x101,
        "#1015F有什么要事吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "唔，其实有很重要的工作\x01",
            "还搁着没做完呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "……你们知道吗？\x01",
            "灯塔也是使用导力器的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "虽然已经更换了零件，\x01",
            "但还是没法试运行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x101,
        "#1007F哎呀呀，那可伤脑筋了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "嗯，不过这可是件\x01",
            "责任重大的工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "要是拜托别人的话，\x01",
            "我这灯塔看守就没有立足之地了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "所以我打算忍着腰痛，\x01",
            "自己慢慢地做。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        (
            "#1003F是吗…………\x02\x03",

            "#1002F但是，可别太勉强哦。\x01",
            "万一恶化就糟糕了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "这点不用担心。\x01",
            "我自己的身体自己知道。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "哦，不好不好……\x01",
            "一不留神就只顾着说话了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "那好，\x01",
            "你们也要加油哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x101,
        (
            "#1006F嗯，谢谢。\x02\x03",

            "那么，请多保重。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    def lambda_C5F():
        OP_8C(0x0, 90, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_C5F)
    Sleep(100)

    def lambda_C72():
        OP_8C(0x1, 90, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_C72)
    Sleep(50)

    def lambda_C85():
        OP_8C(0x2, 90, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_C85)
    Sleep(100)

    def lambda_C98():
        OP_8C(0x3, 90, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_C98)
    Sleep(400)

    def lambda_CAB():
        OP_94(0x1, 0x0, 0x0, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_CAB)
    Sleep(50)

    def lambda_CC6():
        OP_94(0x1, 0x1, 0x0, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_CC6)

    def lambda_CDC():
        OP_94(0x1, 0x2, 0x0, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_CDC)
    Sleep(50)

    def lambda_CF7():
        OP_94(0x1, 0x3, 0x0, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_CF7)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    ChrTalk(    #58
        0xFE,
        "……哦哦，等一下。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        "差点给忘了。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)

    def lambda_D55():
        OP_8C(0x0, 270, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_D55)
    Sleep(100)

    def lambda_D68():
        OP_8C(0x1, 270, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_D68)
    Sleep(50)

    def lambda_D7B():
        OP_8C(0x2, 270, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_D7B)
    Sleep(100)

    def lambda_D8E():
        OP_8C(0x3, 270, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_D8E)
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #60
        0x101,
        "#1000F嗯，怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "唔，就是刚才说的\x01",
            "试运行的事情啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 315, 400)

    ChrTalk(    #62
        0xFE,
        (
            "有关操作方法的说明书\x01",
            "放在那边的书架上。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #63
        0xFE,
        (
            "如果有兴趣的话，\x01",
            "就去看看好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        (
            "#1004F咦？\x02\x03",

            "#1016F啊，嗯，知道了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "说是重要的工作，\x01",
            "其实也就是转转开开关而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "只要看了说明书之后，\x01",
            "大概谁都会做吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)

    ChrTalk(    #67
        0x101,
        (
            "#1019F（这、这难不成是……）\x02\x03",

            "（绕了好大一圈,\x01",
            "  还是要我们去做吧。)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_F65")

    ChrTalk(    #68
        0x106,
        "#551F（不用想也知道是了。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_F8F")

    label("loc_F65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_F8F")

    ChrTalk(    #69
        0x103,
        "#025F（不用想也知道是了吧。）\x02",
    )

    CloseMessageWindow()

    label("loc_F8F")


    ChrTalk(    #70
        0xFE,
        "嗯？怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x101,
        (
            "#1016F不，没什么。\x02\x03",

            "那，那我们走了哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FCD")

    EventEnd(0x0)
    OP_8C(0xFE, 270, 0)
    OP_4B(0xFE, 0)
    Jump("loc_175D")

    label("loc_FDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_102E")
    TalkBegin(0xFE)

    ChrTalk(    #72
        0xFE,
        "呼，真没办法……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "现在的年轻人真是\x01",
            "一点也不会察言观色。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_175D")

    label("loc_102E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_109E")
    TalkBegin(0xFE)

    ChrTalk(    #74
        0xFE,
        (
            "呼，给你们\x01",
            "添麻烦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "不过，最近\x01",
            "要麻烦年轻人的事变多了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        "我毕竟也是上了年纪啊。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_175D")

    label("loc_109E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_115E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1128")

    ChrTalk(    #77
        0xFE,
        "唔唔……伤脑筋。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "明明哪里都正常，\x01",
            "灯塔却还是动不了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "或许就像扎古那小子所说的，\x01",
            "可能不是故障吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_115B")

    label("loc_1128")


    ChrTalk(    #80
        0xFE,
        "唔唔……伤脑筋。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "这可能真的\x01",
            "不是故障吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_115B")

    Jump("loc_175A")

    label("loc_115E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1257")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1218")

    ChrTalk(    #82
        0xFE,
        (
            "那个乳臭未干的小子\x01",
            "真是多嘴……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "这个灯塔的事\x01",
            "我是最清楚的了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "这一次的故障\x01",
            "肯定是内部结构的原因。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "这点程度的异常，你看着吧!\x01",
            "马上就可以修理好的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_1254")

    label("loc_1218")


    ChrTalk(    #86
        0xFE,
        (
            "那小子\x01",
            "真是多嘴……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "这个灯塔的事\x01",
            "我是最清楚的了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1254")

    Jump("loc_175A")

    label("loc_1257")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_13BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EXEC_OP, "OP_29(0x6B, 0x0, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x6B, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12B8")

    ChrTalk(    #88
        0xFE,
        "说明书在书架上。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "如果有兴趣的话\x01",
            "就读读看好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13BA")

    label("loc_12B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_131A")

    ChrTalk(    #90
        0xFE,
        (
            "要是换成波尔多斯，\x01",
            "他会明白灯塔的重要性的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "一定能帮我找个\x01",
            "看守灯塔的后继者。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13BA")

    label("loc_131A")

    OP_A2(0x2)

    ChrTalk(    #92
        0xFE,
        (
            "唔，到底下任市长\x01",
            "会是谁呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "就我个人来说是\x01",
            "很期待波尔多斯呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x6B, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13BA")

    ChrTalk(    #94
        0xFE,
        (
            "此外……\x01",
            "说明书在书架上。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        (
            "如果有兴趣的话\x01",
            "就读读看好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13BA")

    Jump("loc_175A")

    label("loc_13BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_1547")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EXEC_OP, "OP_29(0x6B, 0x0, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x6B, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_141E")

    ChrTalk(    #96
        0xFE,
        "说明书在书架上。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "如果有兴趣的话\x01",
            "就读读看好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1544")

    label("loc_141E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1478")

    ChrTalk(    #98
        0xFE,
        (
            "看守灯塔的工作\x01",
            "可不是谁都能胜任的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        (
            "希望有志向的年轻人\x01",
            "能够来继承啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1544")

    label("loc_1478")

    OP_A2(0x2)

    ChrTalk(    #100
        0xFE,
        (
            "看守灯塔虽然是孤独的工作，\x01",
            "但却具有守护海上安全的重要作用。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "愿意为了大家而付出，\x01",
            "有这种志向的人才能胜任。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x6B, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1544")

    ChrTalk(    #102
        0xFE,
        (
            "此外……\x01",
            "说明书在书架上。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        (
            "如果有兴趣的话\x01",
            "就读读看好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1544")

    Jump("loc_175A")

    label("loc_1547")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_165B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EXEC_OP, "OP_29(0x6B, 0x0, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x6B, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15AC")

    ChrTalk(    #104
        0xFE,
        "说明书在书架上。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "如果有兴趣的话\x01",
            "就读读看好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1658")

    label("loc_15AC")

    OP_A2(0x2)

    ChrTalk(    #106
        0xFE,
        (
            "我也上年纪了，\x01",
            "身体衰弱也没办法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "差不多该找个\x01",
            "能交托这项工作的继任人了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x6B, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1658")

    ChrTalk(    #108
        0xFE,
        (
            "此外……\x01",
            "说明书在书架上。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        (
            "如果有兴趣的话\x01",
            "就读读看好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1658")

    Jump("loc_175A")

    label("loc_165B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_175A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EXEC_OP, "OP_29(0x6B, 0x0, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x6B, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16BC")

    ChrTalk(    #110
        0xFE,
        "说明书在书架上。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        (
            "如果有兴趣的话\x01",
            "就读读看好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_175A")

    label("loc_16BC")

    OP_A2(0x2)

    ChrTalk(    #112
        0xFE,
        (
            "呼，腰这么痛\x01",
            "也没法好好工作了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "我也差不多该\x01",
            "找个后继者了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x6B, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_175A")

    ChrTalk(    #114
        0xFE,
        (
            "此外……\x01",
            "说明书在书架上。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "如果有兴趣的话\x01",
            "就读读看好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_175A")

    TalkEnd(0xFE)

    label("loc_175D")

    Return()

    # Function_0_AA end

    def Function_1_175E(): pass

    label("Function_1_175E")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #116
        "\x07\x05书架上有巴伦诺灯塔·导力器简易手册。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "【读书】\x01",      # 0
            "【放弃】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1826")
    OP_B8(0x231, 0x0)
    OP_28(0x6B, 0x1, 0x1)
    OP_28(0x6B, 0x1, 0x8000)
    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)

    label("loc_1826")

    TalkEnd(0xFF)
    Return()

    # Function_1_175E end

    def Function_2_182A(): pass

    label("Function_2_182A")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 0, -1, -1)

    AnonymousTalk(    #117 op#5
        "导力器启动开关\x05\x02",
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_189C")

    Menu(
        0,
        -1,
        100,
        1,
        (
            "★【 ＯＮ 】\x01",      # 0
            "　【ＯＦＦ】\x01",      # 1
            "　【 放弃 】\x01",      # 2
        )
    )

    Jump("loc_18CC")

    label("loc_189C")


    Menu(
        0,
        -1,
        100,
        1,
        (
            "　【 ＯＮ 】\x01",      # 0
            "★【ＯＦＦ】\x01",      # 1
            "　【 放弃 】\x01",      # 2
        )
    )


    label("loc_18CC")

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_56(0x1)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1995")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_192B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1925")
    OP_22(0x9C, 0x0, 0x64)
    Sleep(400)
    OP_22(0x9E, 0x1, 0x5A)

    label("loc_1925")

    OP_A2(0x3)
    Jump("loc_1992")

    label("loc_192B")

    OP_22(0x9C, 0x0, 0x64)
    Sleep(400)
    OP_22(0x9E, 0x0, 0x5A)
    Sleep(1000)
    OP_23(0x9E)
    OP_22(0xE1, 0x0, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1992")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #118
        "\x07\x05错误！　启动失败！\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_1992")

    Jump("loc_19BC")

    label("loc_1995")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_19B6")
    OP_22(0x9C, 0x0, 0x64)
    Sleep(400)
    OP_23(0x9E)

    label("loc_19B6")

    OP_A3(0x8)
    OP_A3(0x3)

    label("loc_19BC")

    TalkEnd(0xFF)
    Return()

    # Function_2_182A end

    def Function_3_19C0(): pass

    label("Function_3_19C0")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 0, -1, -1)

    AnonymousTalk(    #119 op#5
        "导力压\x05\x02",
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1A46")

    Menu(
        0,
        -1,
        100,
        1,
        (
            "★【 ＨＩＧＨ 】\x01",      # 0
            "　【  ＭＩＤ  】\x01",      # 1
            "　【  ＬＯＷ  】\x01",      # 2
            "　【  放 弃  】\x01",       # 3
        )
    )

    Jump("loc_1AEA")

    label("loc_1A46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1A9D")

    Menu(
        0,
        -1,
        100,
        1,
        (
            "　【 ＨＩＧＨ 】\x01",      # 0
            "　【  ＭＩＤ  】\x01",      # 1
            "★【  ＬＯＷ  】\x01",      # 2
            "　【  放　弃  】\x01",      # 3
        )
    )

    Jump("loc_1AEA")

    label("loc_1A9D")


    Menu(
        0,
        -1,
        100,
        1,
        (
            "　【 ＨＩＧＨ 】\x01",      # 0
            "★【  ＭＩＤ  】\x01",      # 1
            "　【  ＬＯＷ  】\x01",      # 2
            "　【  放　弃  】\x01",      # 3
        )
    )


    label("loc_1AEA")

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_56(0x1)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B2A")
    OP_22(0x64, 0x0, 0x64)
    OP_A2(0x4)
    OP_A3(0x5)
    Jump("loc_1B64")

    label("loc_1B2A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B45")
    OP_22(0x64, 0x0, 0x64)
    OP_A3(0x4)
    OP_A3(0x5)
    Jump("loc_1B64")

    label("loc_1B45")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B60")
    OP_22(0x64, 0x0, 0x64)
    OP_A3(0x4)
    OP_A2(0x5)
    Jump("loc_1B64")

    label("loc_1B60")

    TalkEnd(0xFF)
    Return()

    label("loc_1B64")

    Call(1, 6)
    TalkEnd(0xFF)
    Return()

    # Function_3_19C0 end

    def Function_4_1B6C(): pass

    label("Function_4_1B6C")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 0, -1, -1)

    AnonymousTalk(    #120 op#5
        "水平尾翼强度\x05\x02",
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1BF9")

    Menu(
        0,
        -1,
        100,
        1,
        (
            "★【 ＨＩＧＨ 】\x01",      # 0
            "　【  ＭＩＤ  】\x01",      # 1
            "　【  ＬＯＷ  】\x01",      # 2
            "　【  放　弃  】\x01",      # 3
        )
    )

    Jump("loc_1C9D")

    label("loc_1BF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_1C50")

    Menu(
        0,
        -1,
        100,
        1,
        (
            "　【 ＨＩＧＨ 】\x01",      # 0
            "　【  ＭＩＤ  】\x01",      # 1
            "★【  ＬＯＷ  】\x01",      # 2
            "　【  放　弃  】\x01",      # 3
        )
    )

    Jump("loc_1C9D")

    label("loc_1C50")


    Menu(
        0,
        -1,
        100,
        1,
        (
            "　【 ＨＩＧＨ 】\x01",      # 0
            "★【  ＭＩＤ  】\x01",      # 1
            "　【  ＬＯＷ  】\x01",      # 2
            "　【  放　弃  】\x01",      # 3
        )
    )


    label("loc_1C9D")

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_56(0x1)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CDD")
    OP_22(0x64, 0x0, 0x64)
    OP_A2(0x6)
    OP_A3(0x7)
    Jump("loc_1D17")

    label("loc_1CDD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CF8")
    OP_22(0x64, 0x0, 0x64)
    OP_A3(0x6)
    OP_A3(0x7)
    Jump("loc_1D17")

    label("loc_1CF8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D13")
    OP_22(0x64, 0x0, 0x64)
    OP_A3(0x6)
    OP_A2(0x7)
    Jump("loc_1D17")

    label("loc_1D13")

    TalkEnd(0xFF)
    Return()

    label("loc_1D17")

    Call(1, 6)
    TalkEnd(0xFF)
    Return()

    # Function_4_1B6C end

    def Function_5_1D1F(): pass

    label("Function_5_1D1F")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 0, -1, -1)

    AnonymousTalk(    #121 op#5
        "结晶回路连接\x05\x02",
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_1D8F")

    Menu(
        0,
        -1,
        100,
        1,
        (
            "★【 ＯＮ 】\x01",      # 0
            "　【ＯＦＦ】\x01",      # 1
            "　【 放弃 】\x01",      # 2
        )
    )

    Jump("loc_1DBF")

    label("loc_1D8F")


    Menu(
        0,
        -1,
        100,
        1,
        (
            "　【 ＯＮ 】\x01",      # 0
            "★【ＯＦＦ】\x01",      # 1
            "　【 放弃 】\x01",      # 2
        )
    )


    label("loc_1DBF")

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_56(0x1)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F40")
    OP_22(0x64, 0x0, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E83")
    OP_A2(0x8)
    EventBegin(0x0)
    Sleep(1000)
    OP_22(0x9A, 0x0, 0x64)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    OP_22(0xA1, 0x1, 0x64)
    OP_23(0x9E)
    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #122
        0x101,
        "#1004F啊……！？\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C2209   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1F3D")

    label("loc_1E83")

    Sleep(400)
    OP_23(0x9E)
    OP_22(0xE1, 0x0, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1EEF")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #123
        "\x07\x05错误！　输出不足！　启动解除！\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jump("loc_1F3A")

    label("loc_1EEF")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #124
        "\x07\x05控制不稳定化！　启动解除！\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_1F3A")

    OP_A3(0x3)

    label("loc_1F3D")

    Jump("loc_1F55")

    label("loc_1F40")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F55")
    OP_22(0x64, 0x0, 0x64)
    OP_A3(0x8)

    label("loc_1F55")

    TalkEnd(0xFF)
    Return()

    # Function_5_1D1F end

    def Function_6_1F59(): pass

    label("Function_6_1F59")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1F8B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1FA9")

    label("loc_1F8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1F9F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1FA9")

    label("loc_1F9F")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1FA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1FBD")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1FDB")

    label("loc_1FBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_1FD1")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1FDB")

    label("loc_1FD1")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1FDB")

    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_205B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2058")
    Sleep(400)
    OP_23(0x9E)
    OP_22(0xE1, 0x0, 0x64)
    OP_A3(0x3)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #125
        "\x07\x05错误！　输出为零！　启动解除！\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_2058")

    Jump("loc_20CA")

    label("loc_205B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_20CA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_20CA")
    Sleep(400)
    OP_23(0x9E)
    OP_22(0xE1, 0x0, 0x64)
    OP_A3(0x3)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #126
        "\x07\x05控制不稳定化！　启动解除！\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_20CA")

    Return()

    # Function_6_1F59 end

    def Function_7_20CB(): pass

    label("Function_7_20CB")

    EventBegin(0x0)
    OP_28(0x6B, 0x1, 0x2)
    OP_6D(-1670, 0, 199940, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_4A(0x8, 0)
    OP_8C(0x8, 180, 0)
    OP_22(0xA1, 0x1, 0x64)
    SetChrPos(0x101, -3090, 0, 199520, 0)
    SetChrPos(0xF7, -2130, 0, 199060, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2175")
    SetChrPos(0x104, -2150, 0, 197690, 0)
    SetChrPos(0x105, -3300, 0, 198050, 0)
    Jump("loc_21C7")

    label("loc_2175")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x26)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21A8")
    SetChrPos(0x104, -2150, 0, 197690, 0)
    SetChrPos(0x127, -3300, 0, 198050, 0)
    Jump("loc_21C7")

    label("loc_21A8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21C7")
    SetChrPos(0x109, -2725, 0, 197870, 0)

    label("loc_21C7")

    FadeToBright(2000, 0)
    OP_0D()
    Sleep(400)

    ChrTalk(    #127
        0x8,
        "哦，似乎成功了嘛！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x101,
        "#1015F现在开始放着不管就行了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x8,
        (
            "唔，现在进入的是\x01",
            "试运行模式。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x8,
        (
            "应该会\x01",
            "自动停掉的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x101,
        "#1011F啊，那就放心了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x8,
        "话说回来这还真了不起。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x8,
        (
            "光靠那个说明书\x01",
            "就完全明白怎么操作了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x101,
        (
            "#1016F啊哈哈……\x01",
            "这可是相当难懂的呢。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)
    OP_23(0xA1)
    OP_22(0x9A, 0x0, 0x64)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    Sleep(1000)
    OP_8C(0x101, 90, 400)

    ChrTalk(    #135
        0x101,
        (
            "#1004F啊……\x02\x03",

            "#1015F好、好像停下了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x8,
        "唔，测试平安结束了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_238F")

    ChrTalk(    #137
        0x8,
        (
            "不过，真是又给你们\x01",
            "添麻烦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x8,
        "实在不好意思啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_23C6")

    label("loc_238F")


    ChrTalk(    #139
        0x8,
        (
            "呀，真是又给你们\x01",
            "添麻烦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x8,
        "实在不好意思啊。\x02",
    )

    CloseMessageWindow()

    label("loc_23C6")

    OP_8C(0x101, 0, 400)

    ChrTalk(    #141
        0x101,
        "#1001F哪里，没关系的。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2425")

    ChrTalk(    #142
        0x106,
        (
            "#051F#2P嗯嗯，道谢就不必了,\x01",
            "早点把腰治好吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2460")

    label("loc_2425")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_2460")

    ChrTalk(    #143
        0x103,
        (
            "#021F#2P嗯嗯，道谢就不必了,\x01",
            "请早点把腰治好吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2460")


    ChrTalk(    #144
        0x8,
        (
            "不不，那样说的话\x01",
            "我心里过意不去啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x8,
        "把这些拿去吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #146
        "\x07\x00得到了５个\x1F\xDB\x03\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #147
        "\x07\x00得到了５个\x1F\xDC\x03\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3E(0x3DB, 5)
    OP_3E(0x3DC, 5)

    ChrTalk(    #148
        0x101,
        "#1011F啊……这是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x8,
        "唔，是海钓专用的鱼饵。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x8,
        (
            "在这个灯塔的岩壁旁，\x01",
            "偶尔也能意外地钓到大家伙呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x8,
        (
            "如果有空的话\x01",
            "就去试试好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x101,
        (
            "#1001F嘿嘿，谢谢。\x02\x03",

            "#1015F嗯～那么\x01",
            "我们就先走了……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "【爷爷要保重身体】\x01",      # 0
            "【还有其他事吗？】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26D3")

    ChrTalk(    #153
        0x101,
        "#1000F……爷爷要保重身体哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x8,
        "唔，我会小心……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x8,
        (
            "要是你们能再多问候一句，\x01",
            "那才称得上细心到家了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x8,
        (
            "也罢……\x01",
            "那么，保重了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27D1")

    label("loc_26D3")


    ChrTalk(    #157
        0x101,
        "#1000F……没其他别的事了吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x8,
        "唔，没有别的事情了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x8,
        "不过，能细致地问这么一句才是最重要的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x8,
        (
            "最近，像你们这样机灵的游击士\x01",
            "还真不多见呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x101,
        "#1001F嘿嘿，没什么。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x8,
        (
            "今后，也要时刻不能忘记\x01",
            "这份细心才好哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x8,
        "那么，保重。\x02",
    )

    CloseMessageWindow()
    OP_2B(0x6B, 0x1)
    OP_2C(0x6B, 0x1F4)

    label("loc_27D1")

    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #164
        "\x07\x02任务【灯塔的试运转】\x07\x00完成了！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x6B, 0x4, 0x10)
    OP_A2(0x1)
    OP_64(0x0, 0x1)
    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)
    OP_64(0x3, 0x1)
    OP_64(0x4, 0x1)
    EventEnd(0x0)
    OP_8C(0x8, 270, 0)
    OP_4B(0x8, 0)
    Return()

    # Function_7_20CB end

    SaveToFile()

Try(main)
