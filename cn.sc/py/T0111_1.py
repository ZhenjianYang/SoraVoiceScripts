from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T0111_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T0111_1 ._SN',
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
        "Function_1_33E",          # 01, 1
        "Function_2_43D",          # 02, 2
        "Function_3_1894",         # 03, 3
    )


    def Function_0_AA(): pass

    label("Function_0_AA")


    ChrTalk(    #0
        0xF,
        "#2P唉～～……真伤脑筋。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xF,
        (
            "#2P好不容易重新开工的时候\x01",
            "那东西却偏偏不见了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x101,
        "#1000F看上去似乎在烦恼什么呢。\x02",
    )

    CloseMessageWindow()
    OP_62(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0xF)
    TurnDirection(0xF, 0x101, 400)

    ChrTalk(    #3
        0xF,
        "#2P喔！是你们吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xF,
        (
            "#2P难不成是看了公告板\x01",
            "才来我这里的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        "#1011F啊，嗯，是啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x103,
        "#022F是不是被偷了什么呢。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x103, 400)

    ChrTalk(    #7
        0xF,
        (
            "#2P啊啊，不知道怎么回事，\x01",
            "现在正在发愁呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xF,
        (
            "#2P希望能马上开始调查，\x01",
            "你们方便吗？\x02",
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

    MenuEnd(0xD)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27C")
    Call(1, 2)
    Jump("loc_33D")

    label("loc_27C")


    ChrTalk(    #9
        0x101,
        (
            "#1015F抱歉，现在不能\x01",
            "马上开始。\x02\x03",

            "我还会回来的，\x01",
            "那时再听您说明吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x101, 400)

    ChrTalk(    #10
        0xF,
        (
            "#2P嗯……看来\x01",
            "是忙得很呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xF,
        (
            "#2P唉，没办法了。\x01",
            "那下次再麻烦你吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x103,
        "#020F嗯，等等再过来。\x02",
    )

    CloseMessageWindow()
    OP_28(0x77, 0x1, 0x8000)
    OP_8C(0xF, 90, 0)

    label("loc_33D")

    Return()

    # Function_0_AA end

    def Function_1_33E(): pass

    label("Function_1_33E")

    TurnDirection(0xF, 0x101, 400)

    ChrTalk(    #13
        0xF,
        "#2P哦，是你们。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xF,
        (
            "#2P如何？\x01",
            "可以开始调查了吗？\x02",
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

    MenuEnd(0xD)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D4")
    Call(1, 2)
    Jump("loc_43C")

    label("loc_3D4")


    ChrTalk(    #15
        0x101,
        "#1007F抱歉，还不行……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xF,
        (
            "#2P怎么，你们一直～\x01",
            "都这么忙啊。\x02\x03",

            "唉，没办法。\x01",
            "下次再麻烦你们。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xF, 90, 0)

    label("loc_43C")

    Return()

    # Function_1_33E end

    def Function_2_43D(): pass

    label("Function_2_43D")


    ChrTalk(    #17
        0x101,
        (
            "#1006F没问题。\x01",
            "随时都ＯＫ哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x101, 400)

    ChrTalk(    #18
        0xF,
        "#2P哦，这可帮大忙了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xF,
        (
            "#2P那么，在开始关键的\x01",
            "说明之前──\x02",
        )
    )

    CloseMessageWindow()
    OP_4A(0xE, 255)
    TurnDirection(0xF, 0xE, 400)

    ChrTalk(    #20
        0xF,
        "#2P……呼，阿妮娅。\x02",
    )

    CloseMessageWindow()
    OP_62(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_4E6():
        TurnDirection(0xF9, 0xE, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_4E6)

    def lambda_4F4():
        TurnDirection(0xF6, 0xE, 400)
        ExitThread()

    QueueWorkItem(0xF6, 1, lambda_4F4)
    Sleep(120)

    def lambda_507():
        TurnDirection(0xF7, 0xE, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_507)

    def lambda_515():
        TurnDirection(0xF8, 0xE, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_515)
    TurnDirection(0xE, 0xF, 400)

    ChrTalk(    #21
        0xE,
        "爸爸，什么事～？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xF,
        (
            "#2P爸爸现在\x01",
            "有重要的事要谈。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xF,
        (
            "#2P不好意思，你能去\x01",
            "找妈妈念故事书好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xE,
        "嗯，明白了～\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xD, 400)

    ChrTalk(    #25
        0xE,
        "妈妈～念故事书给我听～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x101,
        (
            "#1001F啊哈哈，原来如此～\x01",
            "还有这样那样的准备工作要做啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x103,
        "#525F您费心了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    EventBegin(0x0)
    SetChrPos(0x101, 1850, 0, 31530, 90)
    SetChrPos(0x103, 1160, 0, 32390, 90)
    SetChrPos(0xF8, 520, 0, 30850, 90)
    SetChrPos(0xF9, 100, 0, 31910, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_691")
    SetChrPos(0xF9, 520, 0, 30850, 90)
    SetChrPos(0xF8, 100, 0, 31910, 90)

    label("loc_691")

    SetChrPos(0xF, 3600, 0, 31530, 270)
    SetChrPos(0xE, -5340, 0, 35800, 0)
    OP_6D(3340, 0, 32130, 0)
    OP_67(0, 4370, -10000, 0)
    OP_6B(2960, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #28
        0xF,
        "──好了，其他事都解决了吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xF,
        (
            "首先，我先说明一下\x01",
            "发生了什么事吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x101,
        "#1006F#4P嗯，请说吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x103,
        "#020F#5P嗯，麻烦你了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xF,
        (
            "不见了的东西是\x01",
            "玛鲁加矿山的管理委任书。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xF,
        (
            "这是女王陛下授予的\x01",
            "重要的证明书……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xF,
        (
            "里面记载了委任矿山长\x01",
            "负责开采管理的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xF,
        (
            "玛鲁加矿山的所有权\x01",
            "也是归女王陛下嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xF,
        (
            "要有那个委任书，\x01",
            "我们才能采掘矿山。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        (
            "#1004F#4P是，是这样的啊。\x02\x03",

            "#1015F矿山是女王陛下所有，\x01",
            "我以前完全不知道。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_91D")

    ChrTalk(    #38
        0x104,
        (
            "#030F实际上虽说是民主国家，\x01",
            "但从法律上看这里还是女王的国家……\x02\x03",

            "国家资产的一部分\x01",
            "归属于女王是当然的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A54")

    label("loc_91D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_98F")

    ChrTalk(    #39
        0x108,
        (
            "#070F不过，虽说是民主国家，\x01",
            "这里也还算是女王的国家嘛。\x02\x03",

            "矿山是王室的东西\x01",
            "一点儿也不奇怪吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A54")

    label("loc_98F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9F3")

    ChrTalk(    #40
        0x105,
        (
            "#040F嗯嗯，王国宪章里\x01",
            "是这么规定的……\x02\x03",

            "当然，委任书\x01",
            "其实不过是形式上的东西。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A54")

    label("loc_9F3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A54")

    ChrTalk(    #41
        0x106,
        (
            "#050F嗯，这个利贝尔\x01",
            "在形式上还是女王的国家嘛。\x02\x03",

            "王室拥有一两座山\x01",
            "也不奇怪啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A54")


    ChrTalk(    #42
        0x103,
        (
            "#020F#5P原来如此，不过因此\x01",
            "才有委任书之类的东西吧。\x02\x03",

            "虽说是形式上，\x01",
            "但玛鲁加矿山的确归女王所有……\x02\x03",

            "开采七耀石\x01",
            "确实需要一些权限。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xF,
        "嗯，就是这样。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xF,
        (
            "现在你们明白是\x01",
            "多么重要的东西被盗了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x101,
        (
            "#1002F#4P嗯……\x01",
            "明白是很重要的东西了。\x02\x03",

            "那，关于事件的经过──\x02\x03",

            "委任书不见了\x01",
            "是何时发现的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xF,
        "哦，就是今天早上的事。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xF,
        (
            "发现存放委任书的\x01",
            "小箱子开着，就觉得不对劲。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xF,
        (
            "看看箱子里，\x01",
            "果然不见了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x103,
        (
            "#027F#5P那么，发现出了事\x01",
            "还没过多久……\x02\x03",

            "断定是失窃\x01",
            "说不定还稍微早了点。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C8F")

    ChrTalk(    #50
        0x106,
        (
            "#053F啊啊，我也同意。\x02\x03",

            "#050F也应该考虑一下\x01",
            "是不是小孩子的恶作剧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D6A")

    label("loc_C8F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CCF")

    ChrTalk(    #51
        0x108,
        (
            "#070F啊啊，是啊。\x02\x03",

            "说不定是孩子的恶作剧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D6A")

    label("loc_CCF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D1E")

    ChrTalk(    #52
        0x104,
        (
            "#030F呼，我也同意。\x02\x03",

            "孩子们的恶作剧\x01",
            "这种情况也应该考虑。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D6A")

    label("loc_D1E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D6A")

    ChrTalk(    #53
        0x105,
        (
            "#042F嗯，也可能是这样。\x02\x03",

            "或许是孩子们\x01",
            "弄丢的也说不定……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D6A")


    ChrTalk(    #54
        0xF,
        (
            "如果真是这样\x01",
            "我也就放心了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xF,
        (
            "可惜不是。\x01",
            "这次绝对不会的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x101,
        "#1011F#4P啊，为什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x103,
        (
            "#022F#5P难不成……\x02\x03",

            "有什么可以证明\x01",
            "被盗的线索吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xF,
        (
            "呼，不愧是专业人员。\x01",
            "其实正是如此。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xF,
        "──请看这个。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_AD(0x240093, 0xBE, 0x64, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(-1, 300, -1, 3)
    SetChrName("")

    AnonymousTalk(    #60
        (
            "\x07\x05　美丽的公主及其随从啊。　　\x01",
            "　  女王真迹在吾手中。　\x01\x02",

            "　　   若想取回\x01",
            "　就从混沌中寻找真实吧。\x02\x03",

            "　　　　　　　　　　　　　　　　\x01",
            "　　　 第一把钥匙在市内。 　　　\x01",
            "询问『坐在女神旁边的人』。\x01",
            "　　　　　　　　　　　　　　　　\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_AE(0x1F4)
    Sleep(1000)

    ChrTalk(    #61
        0xF,
        (
            "──这张卡片\x01",
            "是取而代之放在盒里的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xF,
        "怎么看都是盗窃者留下的吧。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x0, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x0, 0x4)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_FC4")
    OP_A2(0xA)

    label("loc_FC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_104E")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇查看2章或3章中的布卢布兰任务】\x01",      # 0
            "【◇没有变更】\x01",                          # 1
        )
    )

    MenuEnd(0xD)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_END)),
        (0, "loc_1045"),
        (1, "loc_104B"),
        (SWITCH_DEFAULT, "loc_104E"),
    )


    label("loc_1045")

    OP_A2(0xA)
    Jump("loc_104E")

    label("loc_104B")

    Jump("loc_104E")

    label("loc_104E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_128B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_108F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_108C")

    ChrTalk(    #63
        0x106,
        "#053F…………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_108C")

    label("loc_108C")

    Jump("loc_10B1")

    label("loc_108F")


    ChrTalk(    #64
        0x103,
        "#025F#5P…………………………\x02",
    )

    CloseMessageWindow()

    label("loc_10B1")


    ChrTalk(    #65
        0x101,
        "#1007F#4P啊呼……………………\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10FF")

    ChrTalk(    #66
        0x105,
        "#047F呼……………………\x02",
    )

    CloseMessageWindow()

    label("loc_10FF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_112A")

    ChrTalk(    #67
        0x104,
        "#032F唔……………………\x02",
    )

    CloseMessageWindow()

    label("loc_112A")

    OP_62(0xF, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #68
        0xF,
        "怎、怎么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xF,
        (
            "叹什么气呢。\x01",
            "怎么回事？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_11DD")

    ChrTalk(    #70
        0x101,
        (
            "#1016F#4P唔，没什么，别在意。\x02\x03",

            "#1007F#4P『怪盗绅士』布卢布兰……\x02\x03",

            "……真是个烦人的家伙啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1288")

    label("loc_11DD")


    ChrTalk(    #71
        0x101,
        "#1016F#4P不，哪里～只是有点……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x103,
        (
            "#025F#5P请别介意。\x02\x03",

            "唉，不管怎样……\x01",
            "这下犯人就有了大致的目标吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x101,
        (
            "#1007F#4P『怪盗绅士』布卢布兰……\x02\x03",

            "……真是烦人的家伙啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1288")

    Jump("loc_1445")

    label("loc_128B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_131F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12E5")

    ChrTalk(    #74
        0x106,
        (
            "#057F哼，又是卡片谜题啊……\x02\x03",

            "前不久不是也\x01",
            "见过一样的手法吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_131C")

    label("loc_12E5")


    ChrTalk(    #75
        0x101,
        (
            "#1007F#4P卡、卡片谜题……\x02\x03",

            "这手法好像在哪见过呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_131C")

    Jump("loc_1362")

    label("loc_131F")


    ChrTalk(    #76
        0x103,
        (
            "#027F#5P卡片展开的谜题……\x02\x03",

            "……好像在哪儿\x01",
            "见过类似的手法嘛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1362")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1397")

    ChrTalk(    #77
        0x105,
        (
            "#042F艾丝蒂尔……\x01",
            "这难道是……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13EC")

    label("loc_1397")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13C3")

    ChrTalk(    #78
        0x104,
        "#032F唔，看来这是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_13EC")

    label("loc_13C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_13EC")

    ChrTalk(    #79
        0x103,
        "#023F#5P哎呀，有线索吗……？\x02",
    )

    CloseMessageWindow()

    label("loc_13EC")

    OP_8C(0x101, 270, 400)

    ChrTalk(    #80
        0x101,
        (
            "#1002F#4P嗯、嗯……\x02\x03",

            "『怪盗绅士』布卢布兰……\x02\x03",

            "看来是那家伙\x01",
            "干得好事没错了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1445")

    OP_62(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #81
        0xF,
        (
            "什、什么啊，\x01",
            "那奇怪的家伙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xF,
        (
            "就是偷了\x01",
            "委任书的犯人吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #83
        0x101,
        (
            "#1015F#4P虽然不能断言……\x01",
            "我想很有这个可能。\x02\x03",

            "#1002F嗯，稍后再向您解释吧。\x01",
            "不管怎样先开始调查才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x103,
        (
            "#022F#5P嗯，明智的选择……\x02\x03",

            "首先确认一下\x01",
            "卡片的内容吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15C3")

    ChrTalk(    #85
        0x104,
        (
            "#032F必须要找到的是\x01",
            "『坐在女神旁边的人』吧。\x02\x03",

            "#034F唉，怪盗绅士不知为何\x01",
            "好像很喜欢用这手法嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16AB")

    label("loc_15C3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1628")

    ChrTalk(    #86
        0x106,
        (
            "#050F必须找到的是，\x01",
            "『坐在女神旁边的人』……吗？\x02\x03",

            "#053F哼，相当\x01",
            "夸张的小子嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16AB")

    label("loc_1628")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_166D")

    ChrTalk(    #87
        0x107,
        (
            "#062F必须找到的是，\x01",
            "『坐在女神旁边的人』对吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16AB")

    label("loc_166D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16AB")

    ChrTalk(    #88
        0x108,
        (
            "#072F必须找到的是\x01",
            "『坐在女神旁边的人』吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16AB")


    ChrTalk(    #89
        0x101,
        (
            "#1003F#4P大概这也是什么\x01",
            "某种『喻示』……\x02\x03",

            "总之只有先在城里\x01",
            "试着找找看了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xF,
        (
            "看来调查方针\x01",
            "也差不多定了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xF,
        (
            "小姑娘啊。\x01",
            "就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x101,
        "#1006F#4P嗯！我们会努力的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x103,
        (
            "#020F#5P那么，赶快\x01",
            "着手调查吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xF,
        (
            "哦！无论如何\x01",
            "都要找回委任书！\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x77, 0x4, 0x4)
    OP_28(0x77, 0x4, 0x8)
    OP_28(0x77, 0x1, 0x1)
    OP_28(0x77, 0x1, 0x2)
    OP_28(0x77, 0x1, 0x4)
    OP_A2(0xB)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(1850, 0, 31530, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x0, 1850, 0, 31530, 90)
    SetChrPos(0x1, 1850, 0, 31530, 90)
    SetChrPos(0x2, 1850, 0, 31530, 90)
    SetChrPos(0x3, 1850, 0, 31530, 90)
    SetChrPos(0xF, 4600, 0, 31530, 90)
    SetChrPos(0xE, 3140, 0, 32100, 180)
    OP_69(0x0, 0x0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_4B(0xE, 255)
    ClearChrFlags(0xF, 0x10)
    EventEnd(0x4)
    Return()

    # Function_2_43D end

    def Function_3_1894(): pass

    label("Function_3_1894")

    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    SetChrPos(0xF, 4600, 0, 31530, 90)
    OP_4A(0xF, 255)
    SetChrPos(0x101, 1850, 0, 31530, 90)
    SetChrPos(0x103, 1300, 0, 32390, 90)
    SetChrPos(0xF8, 520, 0, 30850, 90)
    SetChrPos(0xF9, 100, 0, 31910, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1928")
    SetChrPos(0xF9, 520, 0, 30850, 90)
    SetChrPos(0xF8, 100, 0, 31910, 90)

    label("loc_1928")

    SetChrPos(0xE, -5340, 0, 35800, 0)
    OP_4A(0xE, 255)
    OP_6D(3340, 0, 32130, 0)
    OP_67(0, 4370, -10000, 0)
    OP_6B(2960, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #95
        0xF,
        "──这样就放心了……\x02",
    )

    CloseMessageWindow()
    OP_8C(0xF, 270, 400)
    OP_8E(0xF, 0xE10, 0x0, 0x7B2A, 0x7D0, 0x0)

    ChrTalk(    #96
        0xF,
        (
            "哎呀～小姑娘……\x01",
            "今天真多亏了你们啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xF,
        (
            "没想到这么简单\x01",
            "就找回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xF,
        (
            "真不愧是洛连特的骄傲，\x01",
            "年轻游击士们的希望啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x101,
        (
            "#1008F#4P啊、啊哈哈……\x01",
            "过奖过奖。\x02\x03",

            "我们只是\x01",
            "完成使命罢了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xF,
        "哈哈哈，很谦虚嘛。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xF,
        (
            "年轻的时候\x01",
            "这种态度最重要了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xF,
        (
            "哦，此外……\x01",
            "忘了问一件重要的事了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xF,
        (
            "这次偷盗的犯人，\x01",
            "已经抓到了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x101,
        (
            "#1015F#4P呼……犯人是谁\x01",
            "倒是有目标……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x103,
        (
            "#025F#5P但要抓住狐狸尾巴\x01",
            "可没那么简单哦。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #106
        (
            "\x07\x05说明了犯人名为布卢布兰，\x01",
            "以及他个人为了乐趣而犯罪的事实。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #107
        0xF,
        (
            "哦～国际犯罪组织成员啊。\x01",
            "相当夸张的家伙嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xF,
        (
            "那样的家伙居然特地\x01",
            "跑来洛连特找麻烦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xF,
        (
            "这种人脑袋里\x01",
            "真不知到底在想些什么。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x103,
        (
            "#026F#5P唉，这个\x01",
            "我们也有同感……\x02\x03",

            "#020F#5P不过，委任书的管理\x01",
            "希望以后能更加严格。\x02\x03",

            "这次的事还好，\x01",
            "万一被用于恐吓就危险了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xF,
        (
            "哦，是……\x01",
            "确实不得不考虑呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xF,
        (
            "嗯……但是我家的话，\x01",
            "也没什么可以安全保管的地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xF,
        (
            "干脆拜托市长\x01",
            "放进金库吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x101,
        (
            "#1018F#4P啊，那也不错啊？\x02\x03",

            "#1016F不，不过，对这个犯人来说\x01",
            "也不能说是绝对安全……\x02\x03",

            "（也有过被偷得\x01",
            "干干净净的例子……）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E0D")

    ChrTalk(    #115
        0x106,
        (
            "#051F但是，还是比这里好点吧。\x02\x03",

            "这想法不错呢。\x01",
            "应该去请求看看。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F11")

    label("loc_1E0D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E5A")

    ChrTalk(    #116
        0x108,
        (
            "#070F话虽如此，\x01",
            "一定比这里好些吧。\x02\x03",

            "应该去请求看看啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F11")

    label("loc_1E5A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EBC")

    ChrTalk(    #117
        0x104,
        (
            "#031F哈哈，怎么说呢，\x01",
            "事件也告一段落了。\x02\x03",

            "你这想法不错呢。\x01",
            "应该试试看才对。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F11")

    label("loc_1EBC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F11")

    ChrTalk(    #118
        0x105,
        (
            "#040F话虽如此，\x01",
            "我想总比这里安全吧。\x02\x03",

            "要不就试着\x01",
            "去说说看怎么样？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F11")


    ChrTalk(    #119
        0xF,
        (
            "是啊……\x01",
            "过几天就去拜托看看。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xF,
        (
            "今天马上要去\x01",
            "山那边才行呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x103,
        "#023F#5P哎呀，还真是忙呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xF,
        (
            "啊啊，一直保持\x01",
            "很稳定的出产量呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xF,
        (
            "无论怎么采掘七耀石\x01",
            "都不见底哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xF,
        (
            "要使用导力器，\x01",
            "七耀石是很重要的，都知道吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x101,
        (
            "#1008F#4P啊哈哈……\x01",
            "这当然，我们非常了解。\x02\x03",

            "但耀晶片总是不够，\x01",
            "去工房都想哭呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_207C")

    ChrTalk(    #126
        0x107,
        (
            "#067F好的结晶回路\x01",
            "成本也高嘛～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2160")

    label("loc_207C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20D3")

    ChrTalk(    #127
        0x104,
        (
            "#034F呼，多么烦恼啊。\x02\x03",

            "与我的实力相称的结晶回路\x01",
            "总是很难到手呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2160")

    label("loc_20D3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2118")

    ChrTalk(    #128
        0x105,
        (
            "#040F嗯嗯，性能优良的结晶回路\x01",
            "总是很难合成呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2160")

    label("loc_2118")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2160")

    ChrTalk(    #129
        0x108,
        (
            "#070F哈哈，性能好的结晶回路\x01",
            "可是相当花费耀晶片的呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2160")


    ChrTalk(    #130
        0xF,
        (
            "怎么，原来\x01",
            "这么辛苦的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xF,
        (
            "那你们就\x01",
            "拿点耀晶片去好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xF,
        (
            "昨天正好拿了\x01",
            "几袋回来呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #133
        0x101,
        (
            "#1004F#4P咦？\x01",
            "可，可以给我们些耀晶片吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xF,
        (
            "是啊，没必要\x01",
            "那么客气啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xF,
        (
            "进了山里\x01",
            "要多少就能挖多少的嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xF,
        "要哪个属性的耀晶片？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "地之耀晶片×５００\x01",      # 0
            "水之耀晶片×５００\x01",      # 1
            "火之耀晶片×５００\x01",      # 2
            "风之耀晶片×５００\x01",      # 3
            "时之耀晶片×５００\x01",      # 4
            "空之耀晶片×５００\x01",      # 5
            "幻之耀晶片×５００\x01",      # 6
        )
    )

    MenuEnd(0xD)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23A1")

    ChrTalk(    #137
        0xF,
        "哦，琥耀石啊。\x02",
    )

    CloseMessageWindow()
    AddSepith(0x0, 0x1F4)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #138
        (
            "\x07\x00得到了\x07\x02#56I地之耀晶片×５００\x01",
            "\x07\x00。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_26A9")

    label("loc_23A1")

    Jc((scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2420")

    ChrTalk(    #139
        0xF,
        "哦，苍耀石啊。\x02",
    )

    CloseMessageWindow()
    AddSepith(0x1, 0x1F4)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #140
        (
            "\x07\x00得到了\x07\x02#57I水之耀晶片×５００\x01",
            "\x07\x00。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_26A9")

    label("loc_2420")

    Jc((scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_249F")

    ChrTalk(    #141
        0xF,
        "哦，红耀石啊。\x02",
    )

    CloseMessageWindow()
    AddSepith(0x2, 0x1F4)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #142
        (
            "\x07\x00得到了\x07\x02#58I火之耀晶片×５００\x01",
            "\x07\x00。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_26A9")

    label("loc_249F")

    Jc((scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_252F")

    ChrTalk(    #143
        0xF,
        (
            "哦，说到洛连特，\x01",
            "还是翠耀石啊。\x02",
        )
    )

    CloseMessageWindow()
    AddSepith(0x3, 0x1F4)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #144
        (
            "\x07\x00得到了\x07\x02#59I风之耀晶片×５００\x01",
            "\x07\x00。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_26A9")

    label("loc_252F")

    Jc((scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25AE")

    ChrTalk(    #145
        0xF,
        "哦，黑耀石啊。\x02",
    )

    CloseMessageWindow()
    AddSepith(0x4, 0x1F4)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #146
        (
            "\x07\x00得到了\x07\x02#62I时之耀晶片×５００\x01",
            "\x07\x00。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_26A9")

    label("loc_25AE")

    Jc((scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_262D")

    ChrTalk(    #147
        0xF,
        "哦，金耀石啊。\x02",
    )

    CloseMessageWindow()
    AddSepith(0x5, 0x1F4)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #148
        (
            "\x07\x00得到了\x07\x02#60I空之耀晶片×５００\x01",
            "\x07\x00。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_26A9")

    label("loc_262D")

    Jc((scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26A9")

    ChrTalk(    #149
        0xF,
        "哦，银耀石啊。\x02",
    )

    CloseMessageWindow()
    AddSepith(0x6, 0x1F4)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #150
        (
            "\x07\x00得到了\x07\x02#61I幻之耀晶片×５００\x01",
            "\x07\x00。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_26A9")


    ChrTalk(    #151
        0xF,
        (
            "嗯，数量虽然不多，\x01",
            "去工房还是够了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xF,
        (
            "努力合成出\x01",
            "优良的结晶回路吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x101,
        "#1001F#4P嗯、嗯！谢谢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x103,
        "#021F#5P真是帮大忙了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xF,
        (
            "那么，我差不多\x01",
            "也该去矿山了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xF,
        (
            "小姑娘你们有空\x01",
            "也要再回洛连特哦。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2780():

        label("loc_2780")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_2780")

    QueueWorkItem2(0x101, 3, lambda_2780)

    def lambda_2791():

        label("loc_2791")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_2791")

    QueueWorkItem2(0x103, 3, lambda_2791)

    def lambda_27A2():

        label("loc_27A2")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_27A2")

    QueueWorkItem2(0xF8, 3, lambda_27A2)

    def lambda_27B3():

        label("loc_27B3")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_27B3")

    QueueWorkItem2(0xF9, 3, lambda_27B3)
    OP_8E(0xF, 0xC30, 0x0, 0x7710, 0x7D0, 0x0)
    OP_8C(0xF, 270, 400)
    OP_44(0x101, 0x3)
    OP_44(0x103, 0x3)
    OP_44(0xF8, 0x3)
    OP_44(0xF9, 0x3)

    ChrTalk(    #157
        0xF,
        "#2P芙莉莎！阿妮娅！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xF,
        "#2P那么，我走了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xD,
        "#4P好……路上小心。\x02",
    )

    CloseMessageWindow()

    def lambda_2838():

        label("loc_2838")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_2838")

    QueueWorkItem2(0xF, 3, lambda_2838)

    ChrTalk(    #160
        0xE,
        "#4P爸爸～！\x02",
    )


    def lambda_2859():

        label("loc_2859")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_2859")

    QueueWorkItem2(0x101, 3, lambda_2859)

    def lambda_286A():

        label("loc_286A")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_286A")

    QueueWorkItem2(0x103, 3, lambda_286A)

    def lambda_287B():

        label("loc_287B")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_287B")

    QueueWorkItem2(0xF8, 3, lambda_287B)

    def lambda_288C():

        label("loc_288C")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_288C")

    QueueWorkItem2(0xF9, 3, lambda_288C)
    OP_8E(0xE, 0xFFFFEDB8, 0x0, 0x7EDF, 0x1770, 0x0)
    OP_8E(0xE, 0xFFFFFF10, 0x0, 0x74CC, 0x1770, 0x0)
    OP_8E(0xE, 0x898, 0x0, 0x7710, 0x1770, 0x0)
    OP_56(0x0)
    OP_59()
    OP_44(0xF, 0x3)

    ChrTalk(    #161
        0xE,
        "早点回来哦！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xE,
        (
            "阿妮娅会乖乖\x01",
            "等你的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xF,
        (
            "#2P哦，我会尽量\x01",
            "早点回来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xF,
        (
            "#2P要好好\x01",
            "帮妈妈的忙哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xE,
        "嗯！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x101,
        "#1016F#1P（唔～多么温馨……）\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0x3)
    OP_44(0x103, 0x3)
    OP_44(0xF8, 0x3)
    OP_44(0xF9, 0x3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29BF")

    ChrTalk(    #167
        0x107,
        (
            "#560F（嘿嘿……\x01",
            "真有点令人羡慕呢。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29F7")

    label("loc_29BF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29F7")

    ChrTalk(    #168
        0x105,
        (
            "#048F（嗯嗯……\x01",
            "多么幸福的一幕啊。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29F7")


    ChrTalk(    #169
        0x103,
        (
            "#021F#5P（呵呵，这下\x01",
            "大叔的威严也都没了呢。）\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xF, 315, 400)

    ChrTalk(    #170
        0xF,
        "#2P那，我就此告辞了。\x02",
    )

    CloseMessageWindow()

    def lambda_2A52():

        label("loc_2A52")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_2A52")

    QueueWorkItem2(0x103, 3, lambda_2A52)

    def lambda_2A63():

        label("loc_2A63")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_2A63")

    QueueWorkItem2(0xF8, 3, lambda_2A63)

    def lambda_2A74():

        label("loc_2A74")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_2A74")

    QueueWorkItem2(0xF9, 3, lambda_2A74)

    def lambda_2A85():

        label("loc_2A85")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_2A85")

    QueueWorkItem2(0xE, 3, lambda_2A85)

    ChrTalk(    #171
        0x103,
        "#525F#5P嗯，工作辛苦了。\x02",
    )

    CloseMessageWindow()

    def lambda_2AB4():

        label("loc_2AB4")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_2AB4")

    QueueWorkItem2(0x101, 3, lambda_2AB4)

    ChrTalk(    #172
        0x101,
        "#1001F#2P老大也要多加小心哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xE,
        "路上小心～！\x02",
    )

    CloseMessageWindow()
    OP_8E(0xF, 0xC30, 0x0, 0x6FB8, 0x7D0, 0x0)

    def lambda_2B0E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2B0E)
    OP_8E(0xF, 0xC30, 0x0, 0x6B6C, 0x7D0, 0x0)
    OP_44(0x101, 0x3)
    OP_44(0x103, 0x3)
    OP_44(0xF8, 0x3)
    OP_44(0xF9, 0x3)
    OP_44(0xE, 0x3)
    OP_28(0x77, 0x1, 0x100)
    OP_28(0x77, 0x4, 0x10)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x17, 0x0, 0x64)

    AnonymousTalk(    #174
        "\x07\x02任务【矿山的委任书】\x07\x00完成了！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x9)
    OP_3F(0x235, 1)
    SetChrFlags(0xF, 0x80)
    EventEnd(0x0)
    OP_4B(0xE, 255)
    Return()

    # Function_3_1894 end

    SaveToFile()

Try(main)
