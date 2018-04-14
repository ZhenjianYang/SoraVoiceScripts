from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 洛连特

    CreateScenaFile(
        FileName            = 'R1503_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/R1503_1 ._SN',
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
        "Function_1_CFA",          # 01, 1
        "Function_2_F49",          # 02, 2
        "Function_3_1908",         # 03, 3
        "Function_4_2349",         # 04, 4
        "Function_5_2376",         # 05, 5
        "Function_6_23A3",         # 06, 6
        "Function_7_23D0",         # 07, 7
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    EventBegin(0x0)
    Fade(1000)
    OP_4A(0x9, 255)
    OP_4A(0xA, 255)
    OP_4A(0x8, 255)
    SetChrPos(0x101, 1420, -10, 17940, 0)
    SetChrPos(0xF7, 2150, 10, 17460, 0)
    SetChrPos(0xF8, 1230, -10, 16430, 0)
    SetChrPos(0xF9, 2280, 0, 16219, 0)
    OP_6D(2100, 20, 17860, 0)
    OP_67(0, 7330, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(    #0
        0x9,
        (
            "#2P少尉……\x01",
            "光靠我们对付不了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x9,
        (
            "#2P我想应该要向\x01",
            "师团总部紧急请求增援。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        "真、真的那么棘手吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x9,
        (
            "#2P嗯，因为是\x01",
            "没见过的魔兽。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x9,
        (
            "#2P不，根本不知道那\x01",
            "能不能称为魔兽……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        (
            "#1011F？？？\x02\x03",

            "请问，出什么事了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(100)
    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_24E():
        OP_8C(0x8, 180, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_24E)
    Sleep(100)
    OP_8C(0x9, 180, 400)

    ChrTalk(    #6
        0x8,
        "唔……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        "你、你们……？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D1")

    ChrTalk(    #8
        0x106,
        (
            "#551F从外表也应该能\x01",
            "看出来的吧？\x02\x03",

            "……我们是游击士。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BA")

    label("loc_2D1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_31E")

    ChrTalk(    #9
        0x103,
        (
            "#027F咦，你们看不见\x01",
            "这枚徽章吗？\x02\x03",

            "……我们是游击士哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BA")

    label("loc_31E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_375")

    ChrTalk(    #10
        0x108,
        (
            "#070F唔，我以为你们能\x01",
            "从这枚徽章上看出来……\x02\x03",

            "……我们是游击士。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BA")

    label("loc_375")


    ChrTalk(    #11
        0x101,
        (
            "#1000F我以为你们能\x01",
            "从这枚徽章上看出来……\x02\x03",

            "……我们是游击士哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BA")

    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #12
        0x8,
        "游、游击士！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_41F")

    ChrTalk(    #13
        0x104,
        (
            "#030F看起来\x01",
            "你们遇到了些麻烦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F2")

    label("loc_41F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_454")

    ChrTalk(    #14
        0x108,
        (
            "#072F看起来\x01",
            "你们遇到了些麻烦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F2")

    label("loc_454")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_489")

    ChrTalk(    #15
        0x103,
        (
            "#027F看起来\x01",
            "你们遇到了些麻烦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F2")

    label("loc_489")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C0")

    ChrTalk(    #16
        0x106,
        (
            "#052F怎么了？\x01",
            "遇到什么麻烦了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F2")

    label("loc_4C0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4F2")

    ChrTalk(    #17
        0x109,
        "#1063F你们似乎遇到了些麻烦呢。\x02",
    )

    CloseMessageWindow()

    label("loc_4F2")


    ChrTalk(    #18
        0x8,
        "嗯、嗯……是的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        (
            "发生了出乎预料\x01",
            "的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        "#1002F出乎预料的事情？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        "嗯，其实……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        (
            "……废坑内部\x01",
            "出现了魔兽。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5C3")

    ChrTalk(    #23
        0x109,
        (
            "#1068F这哪里\x01",
            "出乎预料了？\x02\x03",

            "出现魔兽什么的\x01",
            "可是家常便饭哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_704")

    label("loc_5C3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_614")

    ChrTalk(    #24
        0x106,
        (
            "#052F这叫出乎预料的事？\x02\x03",

            "出现魔兽之类的\x01",
            "不是常有的事情吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_704")

    label("loc_614")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_665")

    ChrTalk(    #25
        0x103,
        (
            "#023F这叫出乎预料的事？\x02\x03",

            "出现魔兽之类的\x01",
            "不是常有的事情吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_704")

    label("loc_665")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6B4")

    ChrTalk(    #26
        0x108,
        (
            "#073F这叫出乎预料的事？\x02\x03",

            "出现魔兽之类的\x01",
            "是常有的事情吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_704")

    label("loc_6B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_704")

    ChrTalk(    #27
        0x104,
        (
            "#033F这叫出乎预料的事？\x02\x03",

            "出现魔兽之类的\x01",
            "应该是常有的事情吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_704")


    ChrTalk(    #28
        0x8,
        "嗯，说是这么说……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x8,
        (
            "可那种魔兽\x01",
            "不是一般的魔兽哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x101,
        "#1002F……什么意思？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x9,
        (
            "#2P嗯，好像是金属\x01",
            "制成的昆虫一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x9,
        (
            "#2P它们从废坑各处\x01",
            "突然涌现出来……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7F9")

    ChrTalk(    #33
        0x107,
        "#065F金属制成的昆虫……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x101,
        "#1002F确实很令人在意呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_964")

    label("loc_7F9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_836")

    ChrTalk(    #35
        0x105,
        (
            "#042F原来如此……\x01",
            "确实很令人在意呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_964")

    label("loc_836")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_878")

    ChrTalk(    #36
        0x104,
        (
            "#035F呼，原来如此……\x02\x03",

            "确实很令人在意呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_964")

    label("loc_878")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8B8")

    ChrTalk(    #37
        0x108,
        (
            "#072F呼，原来如此……\x02\x03",

            "确实很令人在意呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_964")

    label("loc_8B8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8EE")

    ChrTalk(    #38
        0x103,
        (
            "#022F原来如此……\x02\x03",

            "确实很奇怪。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_964")

    label("loc_8EE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_92C")

    ChrTalk(    #39
        0x106,
        (
            "#057F呼，原来如此。\x02\x03",

            "确实很令人在意呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_964")

    label("loc_92C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_964")

    ChrTalk(    #40
        0x109,
        (
            "#1064F啊～原来如此。\x02\x03",

            "这确实很古怪。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_964")


    ChrTalk(    #41
        0x8,
        (
            "我们是被派遣过来\x01",
            "进行警备的部队。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x8,
        (
            "很遗憾，我们没有多余的力量\x01",
            "去消灭那些不知来历的魔兽。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x8,
        (
            "但是，这个地方距离\x01",
            "拉文努村后方相当近。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x8,
        (
            "我们也不能对这种来路不明的\x01",
            "魔兽的出现坐视不管。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x101,
        (
            "#1015F那就是说，\x01",
            "我们来得正是时候了。\x02\x03",

            "#1007F我、我知道你们\x01",
            "很期望我们能够出马。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x8,
        "哎呀，被你看出来了啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x8,
        (
            "不过最近我们和协会的\x01",
            "关系也在不断改善。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x8,
        (
            "不好意思，\x01",
            "能不能帮我们一把？\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x7D, 0x4, 0x4)
    OP_28(0x7D, 0x1, 0x1)
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B88")

    ChrTalk(    #49
        0x101,
        (
            "#1006F当然没问题。\x02\x03",

            "这么古怪的事件\x01",
            "我们怎么会错过呢。\x02",
        )
    )

    CloseMessageWindow()
    Call(1, 2)
    Jump("loc_CDD")

    label("loc_B88")


    ChrTalk(    #50
        0x101,
        (
            "#1015F不，虽然我们很想\x01",
            "帮助你们……\x02\x03",

            "可是很遗憾，\x01",
            "现在有点困难。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x8,
        "是、是这样啊…\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x8,
        (
            "这么唐突的请求。\x01",
            "也难怪……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        (
            "#1007F对不起啊。\x02\x03",

            "一旦有空，\x01",
            "我们会马上返回来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x8,
        "嗯，拜托你们了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x8,
        (
            "你们要是不行的话，\x01",
            "我们只能请求增援了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x8,
        (
            "在事情闹大之前，\x01",
            "若是能解决就最好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x101,
        (
            "#1006F嗯，我们会努力的。\x02\x03",

            "那么再见了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    OP_28(0x7D, 0x1, 0x8000)

    label("loc_CDD")

    OP_4B(0x9, 255)
    OP_4B(0xA, 255)
    OP_4B(0x8, 255)
    OP_8C(0x8, 90, 0)
    OP_8C(0x9, 270, 0)
    EventEnd(0x0)
    Return()

    # Function_0_AA end

    def Function_1_CFA(): pass

    label("Function_1_CFA")

    Fade(1000)
    OP_4A(0x9, 255)
    OP_4A(0xA, 255)
    OP_4A(0x8, 255)
    SetChrPos(0x101, 1420, -10, 17940, 0)
    SetChrPos(0xF7, 2150, 10, 17460, 0)
    SetChrPos(0xF8, 1230, -10, 16430, 0)
    SetChrPos(0xF9, 2280, 0, 16219, 0)
    OP_6D(2100, 20, 17860, 0)
    OP_67(0, 7330, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_8C(0x8, 180, 0)
    OP_8C(0x9, 180, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_DC8")

    ChrTalk(    #58
        0x8,
        (
            "怎么了？莫非你们能\x01",
            "帮忙了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E0E")

    label("loc_DC8")


    ChrTalk(    #59
        0x8,
        (
            "啊，各位游击士。\x01",
            "你们回来了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x8,
        (
            "那么，怎么样？\x01",
            "可以帮忙吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E0E")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EA1")

    ChrTalk(    #61
        0x101,
        (
            "#1006F当然没问题。\x02\x03",

            "这么古怪的事件\x01",
            "我们怎么能错过呢。\x02",
        )
    )

    CloseMessageWindow()
    Call(1, 2)
    Jump("loc_F2C")

    label("loc_EA1")


    ChrTalk(    #62
        0x101,
        (
            "#1007F不，抱歉。\x01",
            "现在还是不行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x8,
        "唔，是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        (
            "#1002F一旦有空\x01",
            "我们会马上返回来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x8,
        "嗯，拜托你们了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x8,
        "那就拜托了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_F2C")

    OP_4B(0x9, 255)
    OP_4B(0xA, 255)
    OP_4B(0x8, 255)
    OP_8C(0x8, 90, 0)
    OP_8C(0x9, 270, 0)
    EventEnd(0x0)
    Return()

    # Function_1_CFA end

    def Function_2_F49(): pass

    label("Function_2_F49")


    ChrTalk(    #67
        0x8,
        "不好意思，真是感恩不尽。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x101,
        (
            "#1010F哪里，情况这么紧急，帮忙是应该的。\x02\x03",

            "#1002F好了，那就让我们\x01",
            "再重新确认一下任务……\x02\x03",

            "总之只要击退那些\x01",
            "怪异的魔兽就行了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x8,
        "嗯，就是这样。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x8,
        (
            "希望你们能击退所有\x01",
            "残留在废坑里的魔兽。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x8,
        (
            "它们外形特殊，应该很容易\x01",
            "跟其他魔兽区分开来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x101,
        "#1002F明白了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10BB")

    ChrTalk(    #73
        0x107,
        (
            "#064F请问还有没有更多\x01",
            "关于那种魔兽的情报？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x107, 400)
    Jump("loc_11C8")

    label("loc_10BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10FF")

    ChrTalk(    #74
        0x108,
        (
            "#072F还有没有更多\x01",
            "关于那种魔兽的情报？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x108, 400)
    Jump("loc_11C8")

    label("loc_10FF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1143")

    ChrTalk(    #75
        0x103,
        (
            "#022F还有没有更多\x01",
            "关于那种魔兽的情报？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x103, 400)
    Jump("loc_11C8")

    label("loc_1143")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1187")

    ChrTalk(    #76
        0x106,
        (
            "#050F还有没有更多\x01",
            "关于那种魔兽的情报？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x106, 400)
    Jump("loc_11C8")

    label("loc_1187")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11C8")

    ChrTalk(    #77
        0x104,
        (
            "#030F还有没有更多\x01",
            "关于那种魔兽的情报？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x104, 400)

    label("loc_11C8")


    ChrTalk(    #78
        0x9,
        "#2P让我想想……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x9,
        (
            "#2P单体威力\x01",
            "不算很强……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x9,
        (
            "#2P不过要特别注意\x01",
            "偶尔出现的那些不同颜色的家伙。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 400)

    ChrTalk(    #81
        0x101,
        "#1015F不同颜色的家伙？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #82
        0x9,
        (
            "#2P嗯，它会使用\x01",
            "类似魔法的攻击……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x9,
        (
            "#2P不管怎么说，那是一种\x01",
            "从来没见过的魔法……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #84
        0x101,
        "#1020F那、那是什么……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_133A")

    ChrTalk(    #85
        0x106,
        (
            "#057F哼，看来还挺难对付……\x02\x03",

            "大家提高警觉\x01",
            "开始工作吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1468")

    label("loc_133A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1381")

    ChrTalk(    #86
        0x103,
        (
            "#022F确实挺危险的……\x02\x03",

            "大家提高警觉\x01",
            "开始工作吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1468")

    label("loc_1381")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13D0")

    ChrTalk(    #87
        0x108,
        (
            "#072F呼，这还真是危险呢。\x02\x03",

            "大家最好提高警觉\x01",
            "开始工作吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1468")

    label("loc_13D0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_141D")

    ChrTalk(    #88
        0x104,
        (
            "#032F呼，这还真是危险呢……\x02\x03",

            "大家提高警觉\x01",
            "开始工作吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1468")

    label("loc_141D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1468")

    ChrTalk(    #89
        0x109,
        (
            "#1068F真的是不知来历呢。\x02\x03",

            "#1063F我们就\x01",
            "提高警觉前进吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1468")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_148E")

    ChrTalk(    #90
        0x105,
        "#042F嗯，是啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_152A")

    label("loc_148E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14B4")

    ChrTalk(    #91
        0x107,
        "#062F是、是的！\x02",
    )

    CloseMessageWindow()
    Jump("loc_152A")

    label("loc_14B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14DC")

    ChrTalk(    #92
        0x104,
        "#030F呼，明白了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_152A")

    label("loc_14DC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1506")

    ChrTalk(    #93
        0x108,
        "#072F嗯，就这么办。\x02",
    )

    CloseMessageWindow()
    Jump("loc_152A")

    label("loc_1506")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_152A")

    ChrTalk(    #94
        0x109,
        "#1063F嗯，是啊。\x02",
    )

    CloseMessageWindow()

    label("loc_152A")


    ChrTalk(    #95
        0x8,
        "说明也已经很充分了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x8,
        "那么，我把门打开吧。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)

    ChrTalk(    #97
        0x101,
        "#1002F嗯，拜托了。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 0, 400)

    def lambda_158A():
        OP_8E(0x8, 0x500, 0x14, 0x58AC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_158A)
    OP_8C(0x9, 0, 400)
    Sleep(100)

    def lambda_15B1():
        OP_8E(0x9, 0xAA0, 0x14, 0x58AC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_15B1)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x8, 0x1)
    OP_44(0x9, 0x1)
    OP_22(0x73, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x6E, 0x0, 0x64)
    Sleep(1000)
    SetChrPos(0x8, -107910, 0, 19880, 225)
    SetChrPos(0x9, -108310, 10, 21740, 180)
    SetChrPos(0xA, -112120, -20, 21740, 180)
    SetChrPos(0x101, -110760, -10, 18000, 0)
    SetChrPos(0xF7, -109590, 30, 18000, 0)
    SetChrPos(0xF8, -110360, -10, 16780, 0)
    SetChrPos(0xF9, -109070, -20, 16780, 0)
    OP_6D(-108800, 30, 17820, 0)
    OP_4A(0xA, 255)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #98
        0x8,
        "诸位请小心。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x8,
        (
            "如果需要休息\x01",
            "就请回到这里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x8,
        (
            "请使用王国军设置的\x01",
            "回复装置。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 0)

    ChrTalk(    #101
        0x101,
        (
            "#1006F谢谢，太好了。\x02\x03",

            "等击退了所有需要消灭的魔兽，\x01",
            "我们会回到这里来报告的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x8,
        "嗯，那就好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x8,
        (
            "愿女神\x01",
            "保佑诸位。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_178C")

    ChrTalk(    #104
        0x106,
        "#050F那我们走吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1809")

    label("loc_178C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17B4")

    ChrTalk(    #105
        0x103,
        "#022F那我们走吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1809")

    label("loc_17B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17E0")

    ChrTalk(    #106
        0x108,
        "#072F嗯，那我们走吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1809")

    label("loc_17E0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1809")

    ChrTalk(    #107
        0x104,
        "#035F呼，那我们走吧。\x02",
    )

    CloseMessageWindow()

    label("loc_1809")

    OP_8C(0x101, 0, 400)

    ChrTalk(    #108
        0x101,
        "#1002F嗯，走吧。\x02",
    )

    CloseMessageWindow()

    def lambda_182C():

        label("loc_182C")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_182C")

    QueueWorkItem2(0x8, 1, lambda_182C)

    def lambda_183D():
        OP_6D(-109790, -40, 22610, 4000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_183D)

    def lambda_1855():
        OP_8E(0x101, 0xFFFE4F58, 0xFFFFFFF6, 0x6464, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1855)
    Sleep(100)

    def lambda_1875():
        OP_8E(0xF7, 0xFFFE53EA, 0xFFFFFFF6, 0x6464, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_1875)

    def lambda_1890():
        OP_8E(0xF8, 0xFFFE50E8, 0xFFFFFFF6, 0x607C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_1890)
    Sleep(100)

    def lambda_18B0():
        OP_8E(0xF9, 0xFFFE55F2, 0xFFFFFFF6, 0x607C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_18B0)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x101, 0x1)
    OP_44(0xF7, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    OP_44(0x8, 0x1)
    OP_44(0x8, 0x2)
    OP_28(0x7D, 0x4, 0x8)
    OP_28(0x7D, 0x1, 0x2)
    OP_28(0x7D, 0x1, 0x4)
    NewScene("ED6_DT21/C1102   ._SN", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_2_F49 end

    def Function_3_1908(): pass

    label("Function_3_1908")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4A(0x9, 255)
    OP_4A(0xA, 255)
    SetChrPos(0x8, -108020, 30, 18910, 270)
    SetChrPos(0x9, -108310, 10, 21740, 180)
    SetChrPos(0xA, -112120, -20, 21740, 180)
    OP_6D(-109690, 20, 20450, 0)
    OP_67(0, 7330, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(2000, 0)
    OP_0D()
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_4A(0x8, 255)
    Sleep(1000)
    OP_8C(0x8, 0, 400)
    OP_4A(0x8, 255)
    Sleep(500)
    OP_6D(-109010, 0, 23650, 1500)

    def lambda_19D8():

        label("loc_19D8")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_19D8")

    QueueWorkItem2(0x8, 1, lambda_19D8)
    Sleep(1000)
    OP_43(0x101, 0x0, 0x1, 0x4)
    Sleep(150)
    OP_43(0xF7, 0x0, 0x1, 0x5)
    Sleep(100)
    OP_43(0xF8, 0x0, 0x1, 0x6)
    Sleep(150)
    OP_43(0xF9, 0x0, 0x1, 0x7)
    OP_6D(-109690, 20, 20450, 2500)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0xF7, 0x0)
    WaitChrThread(0xF8, 0x0)
    WaitChrThread(0xF9, 0x0)
    OP_44(0x8, 0x1)

    ChrTalk(    #109
        0x8,
        "啊，情况怎样？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x101,
        (
            "#1006F嗯，需要消灭的魔兽\x01",
            "已经被我们全部打倒了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1ADD")

    ChrTalk(    #111
        0x106,
        (
            "#051F总之这样一来\x01",
            "应该就没问题了。\x02\x03",

            "接下来的警戒\x01",
            "就交给王国军了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C54")

    label("loc_1ADD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B35")

    ChrTalk(    #112
        0x103,
        (
            "#020F总之这样一来\x01",
            "应该就没问题了。\x02\x03",

            "接下来的警戒\x01",
            "就交给王国军了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C54")

    label("loc_1B35")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B91")

    ChrTalk(    #113
        0x108,
        (
            "#070F总之这样一来\x01",
            "应该就没问题了。\x02\x03",

            "接下来的警戒\x01",
            "就交给你们王国军了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C54")

    label("loc_1B91")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BED")

    ChrTalk(    #114
        0x104,
        (
            "#030F总之这样一来\x01",
            "应该就没问题了。\x02\x03",

            "接下来的警戒\x01",
            "就交给你们王国军了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C54")

    label("loc_1BED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C54")

    ChrTalk(    #115
        0x105,
        (
            "#040F嗯，总之这样一来\x01",
            "应该就没问题了。\x02\x03",

            "接下来的警戒就要交给\x01",
            "边防师团的诸位官兵了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C54")


    ChrTalk(    #116
        0x8,
        "呼，你们搞定了啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x8,
        "嗯，这样一来可以暂时放心了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x101,
        (
            "#1015F嗯，这次的问题\x01",
            "的确是解决了……\x02\x03",

            "#1003F不过那种魔兽……\x01",
            "怎么看都是机械啊。\x02\x03",

            "莫非这也是\x01",
            "结社那帮家伙捣的鬼……？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D57")

    ChrTalk(    #119
        0x109,
        (
            "#1067F大概没错。\x02\x03",

            "但可惜的是我们\x01",
            "不知道他们的目的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E09")

    label("loc_1D57")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D8E")

    ChrTalk(    #120
        0x104,
        (
            "#032F嗯，这么想\x01",
            "或许很有道理呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E09")

    label("loc_1D8E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DB8")

    ChrTalk(    #121
        0x108,
        "#074F嗯，恐怕是的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E09")

    label("loc_1DB8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DE2")

    ChrTalk(    #122
        0x103,
        "#022F嗯，恐怕是的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E09")

    label("loc_1DE2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E09")

    ChrTalk(    #123
        0x106,
        "#053F嗯，很有可能。\x02",
    )

    CloseMessageWindow()

    label("loc_1E09")


    ChrTalk(    #124
        0x8,
        (
            "结社就是……\x01",
            "那个犯罪组织？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x8,
        (
            "原来如此，就是说也有可能\x01",
            "是他们干的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x101,
        (
            "#1002F嗯……\x02\x03",

            "我们已经和他们交手多次了，\x01",
            "对方并不是等闲之辈。\x02\x03",

            "士兵先生们\x01",
            "也请多加小心。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F15")

    ChrTalk(    #127
        0x103,
        (
            "#022F我们游击士\x01",
            "也在调查他们的情况。\x02\x03",

            "要是有什么情况\x01",
            "我们也会联络军方的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2093")

    label("loc_1F15")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F75")

    ChrTalk(    #128
        0x106,
        (
            "#050F我们游击士\x01",
            "也在调查他们的情况。\x02\x03",

            "要是有什么情况\x01",
            "我们也会联络军方的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2093")

    label("loc_1F75")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FD5")

    ChrTalk(    #129
        0x108,
        (
            "#072F我们游击士\x01",
            "也在调查他们的情况。\x02\x03",

            "要是有什么情况\x01",
            "我们也会联络军方的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2093")

    label("loc_1FD5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2033")

    ChrTalk(    #130
        0x104,
        (
            "#032F我们也在\x01",
            "全力调查他们的情况。\x02\x03",

            "要是有什么情况\x01",
            "我们也会联络军方的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2093")

    label("loc_2033")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2093")

    ChrTalk(    #131
        0x109,
        (
            "#1063F协会方面正在\x01",
            "全力调查他们的情况。\x02\x03",

            "如果有所发现，\x01",
            "我们也会联络军方的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2093")


    ChrTalk(    #132
        0x8,
        "嗯，那就好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x8,
        (
            "关于这一次的事件，\x01",
            "我们会从师团总部联络协会的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x8,
        (
            "你们可以去支部\x01",
            "领取我们支付的报酬。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x101,
        "#1006F谢谢，太好了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x8,
        (
            "那么诸位，\x01",
            "回去的路上也请小心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x8,
        (
            "我们都不能\x01",
            "放松警惕。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x8,
        (
            "因为只有这样才能\x01",
            "和看不见的敌人对抗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x101,
        (
            "#1002F嗯，我明白。\x02\x03",

            "那么，接下来\x01",
            "就交给你们负责了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x8,
        "嗯，交给我们吧。\x02",
    )

    CloseMessageWindow()

    def lambda_21DD():

        label("loc_21DD")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_21DD")

    QueueWorkItem2(0x8, 1, lambda_21DD)

    def lambda_21EE():
        OP_8C(0x101, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_21EE)
    Sleep(200)

    def lambda_2201():
        OP_8E(0x101, 0xFFFE4FF8, 0xA, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2201)

    def lambda_221C():
        OP_6D(-110030, 10, 15330, 4000)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_221C)
    Sleep(200)

    def lambda_2239():
        OP_8C(0xF7, 180, 400)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_2239)
    Sleep(250)

    def lambda_224C():
        OP_8E(0xF7, 0xFFFE4FF8, 0xA, 0x2AF8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_224C)

    def lambda_2267():
        OP_8C(0xF8, 180, 400)
        ExitThread()

    QueueWorkItem(0xF8, 0, lambda_2267)
    Sleep(200)

    def lambda_227A():
        OP_8E(0xF8, 0xFFFE5336, 0xA, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_227A)

    def lambda_2295():
        OP_8C(0xF9, 180, 400)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_2295)
    Sleep(200)

    def lambda_22A8():
        OP_8E(0xF9, 0xFFFE4C2E, 0xA, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_22A8)
    Sleep(1400)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x101, 0x1)
    OP_44(0xF7, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    OP_44(0x8, 0x1)
    OP_44(0x8, 0x0)
    OP_28(0x7D, 0x4, 0x10)
    OP_28(0x7D, 0x1, 0x10)
    Sleep(2000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x17, 0x0, 0x64)

    AnonymousTalk(    #141
        "\x07\x02任务【废坑扫荡战】\x07\x00完成了！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(1000)
    OP_20(0x1388)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/C1102   ._SN", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_3_1908 end

    def Function_4_2349(): pass

    label("Function_4_2349")

    SetChrPos(0x101, -109630, -110, 25000, 180)
    OP_8E(0x101, 0xFFFE53C2, 0x28, 0x4A88, 0x7D0, 0x0)
    OP_8C(0x101, 90, 400)
    Return()

    # Function_4_2349 end

    def Function_5_2376(): pass

    label("Function_5_2376")

    SetChrPos(0xF7, -110530, -110, 25700, 180)
    OP_8E(0xF7, 0xFFFE503E, 0x1E, 0x4CF4, 0x7D0, 0x0)
    OP_8C(0xF7, 90, 400)
    Return()

    # Function_5_2376 end

    def Function_6_23A3(): pass

    label("Function_6_23A3")

    SetChrPos(0xF8, -109640, 30, 26310, 180)
    OP_8E(0xF8, 0xFFFE53B8, 0x1E, 0x4F56, 0x7D0, 0x0)
    OP_8C(0xF8, 135, 400)
    Return()

    # Function_6_23A3 end

    def Function_7_23D0(): pass

    label("Function_7_23D0")

    SetChrPos(0xF9, -110560, 10, 27530, 180)
    OP_8E(0xF9, 0xFFFE5020, 0xA, 0x5208, 0x7D0, 0x0)
    OP_8C(0xF9, 135, 400)
    Return()

    # Function_7_23D0 end

    SaveToFile()

Try(main)
