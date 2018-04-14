from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T3116_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T3116_1 ._SN',
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
        "Function_1_677",          # 01, 1
        "Function_2_6B6",          # 02, 2
        "Function_3_A39",          # 03, 3
        "Function_4_14B6",         # 04, 4
        "Function_5_1655",         # 05, 5
        "Function_6_18C8",         # 06, 6
        "Function_7_1996",         # 07, 7
        "Function_8_1F4B",         # 08, 8
        "Function_9_1F91",         # 09, 9
        "Function_10_1FFA",        # 0A, 10
        "Function_11_2046",        # 0B, 11
        "Function_12_2091",        # 0C, 12
        "Function_13_240D",        # 0D, 13
        "Function_14_2460",        # 0E, 14
        "Function_15_24B3",        # 0F, 15
        "Function_16_2506",        # 10, 16
        "Function_17_251F",        # 11, 17
        "Function_18_263E",        # 12, 18
        "Function_19_26C6",        # 13, 19
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x22, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_B9")
    OP_A2(0x3)

    label("loc_B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_135")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇在上部完成过QST034】\x01",        # 0
            "【◇在上部没完成过QST034】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_129"),
        (1, "loc_12F"),
        (SWITCH_DEFAULT, "loc_135"),
    )


    label("loc_129")

    OP_A2(0x3)
    Jump("loc_135")

    label("loc_12F")

    OP_A3(0x3)
    Jump("loc_135")

    label("loc_135")

    Call(1, 17)

    ChrTalk(    #0
        0x101,
        (
            "#1011F请问～打扰一下行吗？\x02\x03",

            "我们是从\x01",
            "协会来的。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_8C(0xFE, 90, 400)

    ChrTalk(    #1
        0xFE,
        "哦，你们来了啊？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3F5")
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #2
        0xFE,
        "咦、咦……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x101,
        "#1000F怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        "不，你莫非是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "曾经在卢安\x01",
            "把试制品送来给我的人？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        "#1004F有、有过吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        "嗯，应该没错。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "你和黑发的男孩子\x01",
            "一起来过武器店吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        (
            "#1015F黑发的男孩子……\x01",
            "怎么看都是约修亚吧。\x02\x03",

            "嗯～这么说起来\x01",
            "可能是有过。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_327")

    ChrTalk(    #10
        0x106,
        (
            "#053F反正你要是在意的话\x01",
            "等会儿看看手册好了。\x02\x03",

            "#050F现在要谈的是这次的工作吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37A")

    label("loc_327")


    ChrTalk(    #11
        0x103,
        (
            "#026F反正你要是在意的话\x01",
            "等会儿看看手册好了。\x02\x03",

            "#020F现在要谈的是这次的工作吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37A")


    ChrTalk(    #12
        0x101,
        "#1011F啊，是哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "……这么说你们果然是\x01",
            "来看告示板的喽？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        (
            "#1006F当然是的。\x02\x03",

            "你好像在募集\x01",
            "导力枪的测试者呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_432")

    label("loc_3F5")


    ChrTalk(    #15
        0x101,
        (
            "#1006F我们看了告示板。\x02\x03",

            "你好像在募集\x01",
            "导力枪的测试者呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_432")


    ChrTalk(    #16
        0xFE,
        "嗯，这倒没错……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "不过我其实因为应聘的人\x01",
            "太少而感到为难呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "能不能请你们马上\x01",
            "听我介绍呢？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_586")

    ChrTalk(    #19
        0x101,
        (
            "#1007F嗯～有可能的话\x01",
            "我们也想这样……\x02\x03",

            "不过最重要的那位\x01",
            "枪手现在正好不在。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "哎呀，那不就\x01",
            "没法做介绍了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "总之你们先把那个人\x01",
            "带来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x101,
        (
            "#1016F确实没错。\x02\x03",

            "那么，我们会再来的。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x6E, 0x1, 0x8000)
    OP_28(0x6E, 0x1, 0x4000)
    OP_A2(0x4)
    EventEnd(0x0)
    OP_8C(0xFE, 270, 0)
    ClearChrFlags(0xFE, 0x10)
    Return()

    label("loc_586")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E4")
    OP_28(0x6E, 0x4, 0x4)
    Call(1, 3)
    Return()

    label("loc_5E4")


    ChrTalk(    #23
        0x101,
        "#1007F抱歉，现在还不行。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        "哎呀，是吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        (
            "#1006F嗯，有时间我们会来的。\x01",
            "到时候就要拜托你了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        "嗯，那就最好了。\x02",
    )

    CloseMessageWindow()
    OP_28(0x6E, 0x1, 0x8000)
    EventEnd(0x0)
    OP_8C(0xFE, 270, 0)
    ClearChrFlags(0xFE, 0x10)
    Return()

    # Function_0_AA end

    def Function_1_677(): pass

    label("Function_1_677")


    ChrTalk(    #27
        0xFE,
        (
            "总之你们先把那个枪手\x01",
            "带来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "不然我没办法\x01",
            "做介绍。\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_1_677 end

    def Function_2_6B6(): pass

    label("Function_2_6B6")

    EventBegin(0x0)
    Call(1, 17)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6E, 0x1, 0x4000)"), scpexpr(EXPR_END)), "loc_811")
    OP_8C(0xFE, 90, 400)

    ChrTalk(    #29
        0xFE,
        "哟，是你们啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "你们把那个枪手\x01",
            "带来了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_774")

    ChrTalk(    #31
        0x101,
        "#1006F嗯，就在这里。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x104,
        "#035F呵呵，让你久等了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "好，那么可以谈\x01",
            "测试的问题了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x6E, 0x2, 0x4000)
    Jump("loc_80E")

    label("loc_774")


    ChrTalk(    #34
        0x101,
        (
            "#1003F不，抱歉。\x01",
            "还没带来哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "总之你们先把那个人\x01",
            "带来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "不然我没办法\x01",
            "做介绍。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        (
            "#1000F明白了。\x01",
            "我们会再来的。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x6E, 0x1, 0x4000)
    OP_A2(0x4)
    EventEnd(0x0)
    OP_8C(0xFE, 270, 0)
    ClearChrFlags(0xFE, 0x10)
    Return()

    label("loc_80E")

    Jump("loc_943")

    label("loc_811")

    OP_8C(0xFE, 90, 400)

    ChrTalk(    #38
        0xFE,
        "啊，是你们。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "关于导力枪的测试，\x01",
            "这次可以听我说了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_943")

    ChrTalk(    #40
        0x101,
        (
            "#1007F嗯～有可能的话\x01",
            "我们也想这样……\x02\x03",

            "不过最重要的那位\x01",
            "枪手现在正好不在。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "哎呀，那不就\x01",
            "没法做介绍了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "总之你们先把那个人\x01",
            "带来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        (
            "#1016F确实没错。\x02\x03",

            "那么，我们会再来的。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x6E, 0x1, 0x8000)
    OP_28(0x6E, 0x1, 0x4000)
    OP_A2(0x4)
    EventEnd(0x0)
    OP_8C(0xFE, 270, 0)
    ClearChrFlags(0xFE, 0x10)
    Return()

    label("loc_943")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9A1")
    OP_28(0x6E, 0x4, 0x4)
    Call(1, 3)
    Return()

    label("loc_9A1")


    ChrTalk(    #44
        0x101,
        (
            "#1007F不，抱歉。\x01",
            "还有点不方便。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        "哎呀，怎么这样～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        (
            "#1016F真对不起。\x01",
            "有时间了我会再来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "嗯，拜托了。\x01",
            "我在这里等着。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x6E, 0x1, 0x8000)
    EventEnd(0x0)
    OP_8C(0xFE, 270, 0)
    Return()

    # Function_2_6B6 end

    def Function_3_A39(): pass

    label("Function_3_A39")


    ChrTalk(    #48
        0x101,
        "#1000F嗯，拜托你了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "那么，马上开始\x01",
            "做个说明吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "你们知道，\x01",
            "委托内容是导力枪的测试。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "我希望你们通过实战来检测\x01",
            "它作为武器的可靠性。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x101,
        "#1011F可靠性检测？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "最简单地说就是\x01",
            "测试耐久度。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "任何机械肯定都有只在\x01",
            "实际使用中才会暴露的缺陷。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "很多故障原因都是在\x01",
            "开发过程中想象不到的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "找出这种隐藏的弱点，\x01",
            "并且提高其作为武器的可靠性。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        "这就是测试的目的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x104,
        (
            "#030F是这样啊，主旨我已经明白了。\x02\x03",

            "就是说，用专业词汇来描述的话\x01",
            "就是『实战检测』喽。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x104, 400)

    ChrTalk(    #59
        0xFE,
        "嗯，一点没错。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "对了，你就是\x01",
            "帮忙测试的射手吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x104,
        (
            "#031F嗯，让我来打个招呼。\x02\x03",

            "漂泊的诗人兼演奏家，\x01",
            "奥利维尔·朗海姆是也。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #62
        0xFE,
        "演、演奏家……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x101,
        (
            "#1001F啊，没事的。\x02\x03",

            "这家伙虽然看上去怪怪的，\x01",
            "不过只有枪的技术#5S这一点#2S是可信赖的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 400)

    ChrTalk(    #64
        0x104,
        (
            "#033F咦，是不是我多心了？\x02\x03",

            "好像你在发言中\x01",
            "特别强调了某一部分……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DD1")

    ChrTalk(    #65
        0x108,
        (
            "#071F哈哈，这有什么关系呢。\x02\x03",

            "你的能力\x01",
            "已经得到了大家的认可。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E6D")

    label("loc_DD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_E23")

    ChrTalk(    #66
        0x106,
        (
            "#051F好了，这又有什么关系呢。\x02\x03",

            "你小子的能力\x01",
            "已经得到了大家的认可。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E6D")

    label("loc_E23")


    ChrTalk(    #67
        0x103,
        (
            "#021F哎呀，这又有什么关系呢。\x02\x03",

            "奥利维尔的能力\x01",
            "已经得到了大家的认可。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E6D")


    ChrTalk(    #68
        0xFE,
        "是、是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "好了，既然这样，\x01",
            "就拜托你了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0xFE, 400)

    ChrTalk(    #70
        0x104,
        (
            "#031F哈哈哈。\x01",
            "你就放一百个心吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        "（真、真的没问题吗……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "算、算了。\x01",
            "总之我先把枪给你。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #73
        "\x07\x00得到了\x1F\x5B\x00\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x5B, 1)
    OP_59()
    OP_0D()
    Fade(500)
    SetChrChipByIndex(0x104, 3)
    SetChrSubChip(0x104, 0)
    OP_0D()
    Call(1, 18)

    ChrTalk(    #74
        0xFE,
        "那就是要测试的枪。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "作为你们赶来的谢礼，\x01",
            "就免费送给你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x104,
        (
            "#035F哟，这可太感谢了。\x02\x03",

            "#032F不过话说回来，这把枪……\x01",
            "构造看上去还真不习惯。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "哈哈，那是当然的。\x01",
            "如果你以前见过我倒不好办了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "因为这把枪的驱动方式\x01",
            "是我们发明的新技术。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        "怎么样，会用吗？\x02",
    )

    CloseMessageWindow()
    OP_43(0x104, 0x1, 0x1, 0x10)

    ChrTalk(    #80
        0x104,
        (
            "#035F呼，当然。\x02\x03",

            "我和这把枪一定能\x01",
            "发出美妙的共鸣。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        "多、多谢夸奖……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #82
        0x101,
        (
            "#1007F好了，先不管这些，\x01",
            "请你继续介绍下去。\x02\x03",

            "#1002F我们还不知道\x01",
            "具体要做些什么呢。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x104, 0x1)
    Fade(500)
    SetChrChipByIndex(0x104, 65535)
    SetChrSubChip(0x104, 0)
    OP_0D()

    ChrTalk(    #83
        0x104,
        (
            "#033F哦！确实如此。\x02\x03",

            "来吧，快点介绍。\x02",
        )
    )

    CloseMessageWindow()
    Call(1, 19)

    ChrTalk(    #84
        0xFE,
        (
            "大、大致上和你\x01",
            "前面自己说过的一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "总之，你只要装备着那把枪\x01",
            "去战斗就行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        (
            "测试场所就选在附近的\x01",
            "托兰特平原道吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "在那里就算碰上什么麻烦\x01",
            "也不会引发严重的事态。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x101,
        (
            "#1006F明白了。\x01",
            "托兰特平原道是吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "希望你们最起码\x01",
            "能够进行１０次左右的战斗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "当然这是计算\x01",
            "完成作战次数的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "老是撤退、撤退的，\x01",
            "就不能算是战斗测试了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x104,
        (
            "#030F好，那么确认一下……\x02\x03",

            "装备着这把枪\x01",
            "前往托兰特平原道……\x02\x03",

            "在那里进行１０次\x01",
            "左右的战斗就行了？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1381")

    ChrTalk(    #93
        0x106,
        (
            "#050F那么在完成之后\x01",
            "再回来这里报告。\x02\x03",

            "……就没问题了吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13BF")

    label("loc_1381")


    ChrTalk(    #94
        0x103,
        (
            "#020F那么在完成之后\x01",
            "再回来这里报告。\x02\x03",

            "……就没问题了吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13BF")

    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #95
        0xFE,
        "嗯，应该没问题了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        (
            "如果已经没有疑问的话\x01",
            "接下来就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x101,
        (
            "#1006F没什么疑问了。\x02\x03",

            "那我们走了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x104, 400)

    ChrTalk(    #98
        0xFE,
        (
            "奥利维尔先生……\x01",
            "我可相信着你哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x104,
        "#031F呵呵，我不会辜负你的期待的。\x02",
    )

    CloseMessageWindow()
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_28(0x6E, 0x4, 0x8)
    OP_28(0x6E, 0x1, 0x1)
    OP_28(0x6E, 0x1, 0x2)
    OP_A2(0x5)
    ClearChrFlags(0xFE, 0x10)
    EventEnd(0x0)
    OP_8C(0xFE, 270, 0)
    Return()

    # Function_3_A39 end

    def Function_4_14B6(): pass

    label("Function_4_14B6")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "【报告】\x01",              # 0
            "【确认工作内容】\x01",      # 1
            "【放弃】\x01",              # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1522")
    Call(1, 5)
    Return()

    label("loc_1522")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1631")

    ChrTalk(    #100
        0xFE,
        (
            "我想拜托的\x01",
            "是『零式导力枪』的测试。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "希望你们装备着那把枪\x01",
            "最少进行１０次\x01",
            "左右的战斗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "进行试验的地方就选在\x01",
            "托兰特平原道吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        (
            "这一带就那里\x01",
            "是相对安全的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        (
            "如果达到了目标战斗次数\x01",
            "就再来这里报告吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "工作内容的确认\x01",
            "差不多就是这样。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1654")

    label("loc_1631")


    ChrTalk(    #106
        0xFE,
        (
            "那么，测试\x01",
            "你们也要帮帮忙啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1654")

    Return()

    # Function_4_14B6 end

    def Function_5_1655(): pass

    label("Function_5_1655")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16D8")

    ChrTalk(    #107
        0xFE,
        (
            "咦，奥利维尔先生\x01",
            "怎么不见了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        (
            "关键的射手不在的话\x01",
            "就称不上报告了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        "不好意思，请你们下次再来。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Return()

    label("loc_16D8")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1750")

    ChrTalk(    #110
        0xFE,
        "咦，是来报告的吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x101,
        (
            "#1000F不……\x01",
            "我们现在才刚要去测试。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        (
            "原来是这样啊。\x01",
            "那么，请多关照了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)
    Return()

    label("loc_1750")

    EventBegin(0x0)
    Call(1, 17)
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #113
        0xFE,
        "哟，是来报告的吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x101,
        "#1000F嗯，我们战斗过了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x104,
        (
            "#030F那么就让我把之前的\x01",
            "经过报告一下。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x5B, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_186A")

    ChrTalk(    #116
        0xFE,
        "嗯，这个倒是好事……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "不过关键的『零式导力枪α』\x01",
            "你们好像没带着吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "没有那个的话\x01",
            "就无法确认测试结果了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        "不好意思，请你们下次再来。\x02",
    )

    CloseMessageWindow()
    OP_A2(0xA)
    EventEnd(0x0)
    Return()

    label("loc_186A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #120
        (
            "\x07\x05向加鲁诺介绍了\x01",
            "迄今为止的战斗测试状况。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_18C2")
    Call(1, 6)
    Return()

    label("loc_18C2")

    Call(1, 7)
    Return()

    # Function_5_1655 end

    def Function_6_18C8(): pass

    label("Function_6_18C8")


    ChrTalk(    #121
        0xFE,
        (
            "嗯～原来如此。\x01",
            "似乎也都很努力……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "很遗憾，战斗次数\x01",
            "比预定的还少呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x101,
        "#1008F啊，果然是这样？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "嗯，你们要是能\x01",
            "再多战斗几次就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        "那么下次再来报告吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x104,
        "#030F呵呵，下次再来。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)
    EventEnd(0x0)
    Return()

    # Function_6_18C8 end

    def Function_7_1996(): pass

    label("Function_7_1996")

    TurnDirection(0xFE, 0x104, 400)
    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1A14")

    ChrTalk(    #127
        0xFE,
        (
            "嗯，看来战斗得\x01",
            "已经很充分了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "呀～不管怎样，\x01",
            "你们很努力呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x101,
        "#1001F嘿嘿，谢谢。\x02",
    )

    CloseMessageWindow()
    OP_2B(0x6E, 0x1)
    OP_2C(0x6E, 0x3E8)
    Jump("loc_1AAA")

    label("loc_1A14")


    ChrTalk(    #130
        0xFE,
        (
            "嗯，看来战斗得\x01",
            "已经很充分了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        "好，测试可以算是完成了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x101,
        (
            "#1007F啊，终于结束了。\x02\x03",

            "比我想象的要累得多～\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #133
        0xFE,
        "哈哈，你们好像很疲劳。\x02",
    )

    CloseMessageWindow()

    label("loc_1AAA")


    ChrTalk(    #134
        0x104,
        (
            "#035F呵呵，作为一名协力人员，\x01",
            "做这点事算不了什么。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x104, 400)

    ChrTalk(    #135
        0xFE,
        (
            "对了，奥利维尔先生。\x01",
            "测试下来有什么问题吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x104,
        (
            "#035F不，完全没有问题。\x02\x03",

            "稳定的弹道、\x01",
            "绝妙的重心平衡……\x02\x03",

            "#030F是一件很让人期待其量产化的上品。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "呼～太好了～\x01",
            "听到这些我就放心了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        (
            "好，总算离产品化\x01",
            "只剩一步之遥了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x101,
        (
            "#1000F还没有产品化吗？\x02\x03",

            "以我这个外行的眼光来看\x01",
            "这已经像是完成品了\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #140
        0xFE,
        "不，还有一点工序。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        (
            "接下来就要和生产方\x01",
            "确定细节部分了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        (
            "不过能这么说也是\x01",
            "多亏了这次测试。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        (
            "对接下来的研究也会\x01",
            "起促进作用。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1CD3")

    ChrTalk(    #144
        0x106,
        "#051F嗯，希望你们再接再厉。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CEE")

    label("loc_1CD3")


    ChrTalk(    #145
        0x103,
        "#020F请你们再接再厉。\x02",
    )

    CloseMessageWindow()

    label("loc_1CEE")


    ChrTalk(    #146
        0x104,
        (
            "#031F新型导力枪……\x01",
            "我会大为期待的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x104, 400)

    ChrTalk(    #147
        0xFE,
        "嗯，你们就瞧好吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        (
            "啊，对了……\x01",
            "请先别走。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x101,
        "#1011F咦，还有什么事吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #150
        0xFE,
        "嗯，希望你们收下这个。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #151
        "\x07\x00得到了\x1F\x6C\x02\x07\x00结晶回路。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x26C, 1)
    Sleep(500)

    ChrTalk(    #152
        0xFE,
        (
            "米拉方面的报酬很少，\x01",
            "我挺在意的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        "嘿嘿，就算是补偿吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xFE,
        (
            "而且也算是件有用的东西，\x01",
            "请收下来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x101,
        "#1001F啊，嗯，谢谢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x104,
        "#031F呵呵，我会珍惜它的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        (
            "那以后有什么事的话\x01",
            "我还会再拜托你们的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xFE,
        "你们也当心。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x101,
        "#1018F那么再见了。\x02",
    )

    CloseMessageWindow()
    OP_28(0x6E, 0x4, 0x10)
    OP_28(0x6E, 0x1, 0x80)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #160
        "\x07\x02任务【新型导力枪测试】\x07\x00完成了！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x8)
    EventEnd(0x0)
    Return()

    # Function_7_1996 end

    def Function_8_1F4B(): pass

    label("Function_8_1F4B")


    ChrTalk(    #161
        0xFE,
        "那么，请多关照了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        (
            "尤其是奥利维尔先生，\x01",
            "特别需要拜托你了！\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_8_1F4B end

    def Function_9_1F91(): pass

    label("Function_9_1F91")


    ChrTalk(    #163
        0xFE,
        "各位，今天真是谢谢了，\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xFE,
        (
            "我也会努力做出\x01",
            "了不起的导力枪。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        (
            "那么再见了，\x01",
            "有事我会再找你们的。\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_9_1F91 end

    def Function_10_1FFA(): pass

    label("Function_10_1FFA")


    ChrTalk(    #166
        0xFE,
        (
            "关键的射手不在的话\x01",
            "就称不上报告了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xFE,
        "不好意思，请你们下次再来。\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_10_1FFA end

    def Function_11_2046(): pass

    label("Function_11_2046")


    ChrTalk(    #168
        0xFE,
        (
            "很遗憾，战斗次数\x01",
            "比预定的还少呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0xFE,
        (
            "继续战斗几次\x01",
            "以后再来报告吧。\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_11_2046 end

    def Function_12_2091(): pass

    label("Function_12_2091")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x13), scpexpr(EXPR_PUSH_LONG, 0x382), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_209E")
    Return()

    label("loc_209E")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0xE4E5A8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2132")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x154), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3BCE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2132")
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2132")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x1, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21B1")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x10FE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x866), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_21B1")
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_21B1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x1, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2230")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x11F8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3C3C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2230")
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2230")

    SetMapFlags(0x80)
    OP_C0(0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(30)
    LoadEffect(0x0, "map\\\\mp108_00.eff")
    PlayEffect(0x0, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(600)
    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0xF4240), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2330")
    EventBegin(0x1)
    OP_62(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x0)
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_END)),
        (1, "loc_2316"),
        (2, "loc_231D"),
        (3, "loc_2324"),
        (SWITCH_DEFAULT, "loc_232B"),
    )


    label("loc_2316")

    OP_65(0x0, 0x1)
    Jump("loc_232B")

    label("loc_231D")

    OP_65(0x1, 0x1)
    Jump("loc_232B")

    label("loc_2324")

    OP_65(0x2, 0x1)
    Jump("loc_232B")

    label("loc_232B")

    EventEnd(0x1)
    Jump("loc_2406")

    label("loc_2330")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x4C4B40), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_2380")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #170
        "\x07\x05这附近有反应！\x02",
    )

    OP_22(0xAA, 0x0, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_2406")

    label("loc_2380")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x989680), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_23CC")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #171
        "\x07\x05附近有反应\x02",
    )

    OP_22(0xAA, 0x0, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_2406")

    label("loc_23CC")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #172
        "\x07\x05没有反应\x02",
    )

    OP_22(0xAB, 0x0, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_2406")

    OP_0D()
    ClearMapFlags(0x80)
    Return()

    # Function_12_2091 end

    def Function_13_240D(): pass

    label("Function_13_240D")

    EventBegin(0x1)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #173
        "\x07\x00得到了\x1F\x33\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x233, 1)
    OP_28(0x6F, 0x1, 0x8)
    OP_64(0x0, 0x1)
    EventEnd(0x1)
    Return()

    # Function_13_240D end

    def Function_14_2460(): pass

    label("Function_14_2460")

    EventBegin(0x1)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #174
        "\x07\x00得到了\x1F\x33\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x233, 1)
    OP_28(0x6F, 0x1, 0x10)
    OP_64(0x1, 0x1)
    EventEnd(0x1)
    Return()

    # Function_14_2460 end

    def Function_15_24B3(): pass

    label("Function_15_24B3")

    EventBegin(0x1)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #175
        "\x07\x00得到了\x1F\x33\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x233, 1)
    OP_28(0x6F, 0x1, 0x20)
    OP_64(0x2, 0x1)
    EventEnd(0x1)
    Return()

    # Function_15_24B3 end

    def Function_16_2506(): pass

    label("Function_16_2506")

    SetChrChipByIndex(0x104, 3)
    OP_99(0x104, 0x0, 0xE, 0x7D0)
    WaitChrThread(0x104, 0x0)
    SetChrSubChip(0x104, 14)
    Return()

    # Function_16_2506 end

    def Function_17_251F(): pass

    label("Function_17_251F")

    Fade(1000)
    SetChrPos(0x8, -2000, 0, 3410, 270)
    SetChrPos(0x101, -420, 0, 3410, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2589")
    SetChrPos(0xF7, -490, 0, 5020, 245)
    SetChrPos(0xF8, 590, 0, 2940, 266)
    SetChrPos(0xF9, 950, 0, 4870, 240)
    Jump("loc_25FF")

    label("loc_2589")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25CC")
    SetChrPos(0xF8, -490, 0, 5020, 245)
    SetChrPos(0xF7, 590, 0, 2940, 266)
    SetChrPos(0xF9, 950, 0, 4870, 240)
    Jump("loc_25FF")

    label("loc_25CC")

    SetChrPos(0xF9, -490, 0, 5020, 245)
    SetChrPos(0xF7, 590, 0, 2940, 266)
    SetChrPos(0xF8, 950, 0, 4870, 240)

    label("loc_25FF")

    OP_6D(-790, 0, 3710, 0)
    OP_67(0, 4800, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(57000, 0)
    OP_6E(280, 0)
    OP_0D()
    Return()

    # Function_17_251F end

    def Function_18_263E(): pass

    label("Function_18_263E")


    def lambda_2644():
        TurnDirection(0x101, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2644)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2678")

    def lambda_265F():
        OP_8C(0xF8, 315, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_265F)

    def lambda_266D():
        TurnDirection(0xF9, 0x104, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_266D)
    Jump("loc_26C0")

    label("loc_2678")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26A4")

    def lambda_268B():
        OP_8C(0xF7, 315, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_268B)

    def lambda_2699():
        TurnDirection(0xF9, 0x104, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_2699)
    Jump("loc_26C0")

    label("loc_26A4")


    def lambda_26AA():
        OP_8C(0xF7, 315, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_26AA)

    def lambda_26B8():
        TurnDirection(0xF8, 0x104, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_26B8)

    label("loc_26C0")

    WaitChrThread(0x101, 0x1)
    Return()

    # Function_18_263E end

    def Function_19_26C6(): pass

    label("Function_19_26C6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2700")

    def lambda_26D9():
        OP_8C(0xF7, 245, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_26D9)

    def lambda_26E7():
        OP_8C(0xF8, 266, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_26E7)

    def lambda_26F5():
        OP_8C(0xF9, 240, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_26F5)
    Jump("loc_2764")

    label("loc_2700")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_273A")

    def lambda_2713():
        OP_8C(0xF8, 245, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_2713)

    def lambda_2721():
        OP_8C(0xF7, 266, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_2721)

    def lambda_272F():
        OP_8C(0xF9, 240, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_272F)
    Jump("loc_2764")

    label("loc_273A")


    def lambda_2740():
        OP_8C(0xF9, 245, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_2740)

    def lambda_274E():
        OP_8C(0xF7, 266, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_274E)

    def lambda_275C():
        OP_8C(0xF8, 240, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_275C)

    label("loc_2764")

    Return()

    # Function_19_26C6 end

    SaveToFile()

Try(main)
