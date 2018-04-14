from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'R3403   ._SN',
        MapName             = 'Zeiss',
        Location            = 'R3403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60030",
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '鲁迪',                                 # 9
        '王',                                   # 10
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


    AddCharChip(
        'ED6_DT07/CH01500 ._CH',             # 00
        'ED6_DT07/CH01760 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH01500P._CP',             # 00
        'ED6_DT07/CH01760P._CP',             # 01
    )

    DeclNpc(
        X                   = 613590,
        Z                   = 20,
        Y                   = -52010,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 2,
    )

    DeclNpc(
        X                   = 604750,
        Z                   = 0,
        Y                   = -52330,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )


    ScpFunction(
        "Function_0_FA",           # 00, 0
        "Function_1_179",          # 01, 1
        "Function_2_1D0",          # 02, 2
        "Function_3_10DF",         # 03, 3
        "Function_4_10E0",         # 04, 4
        "Function_5_13F7",         # 05, 5
        "Function_6_15A3",         # 06, 6
        "Function_7_15D3",         # 07, 7
        "Function_8_1603",         # 08, 8
        "Function_9_1633",         # 09, 9
    )


    def Function_0_FA(): pass

    label("Function_0_FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_109")
    SetChrFlags(0x8, 0x80)
    Jump("loc_140")

    label("loc_109")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_118")
    SetChrFlags(0x8, 0x80)
    Jump("loc_140")

    label("loc_118")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_133")
    SetChrPos(0x8, 609020, -20, -62710, 135)
    Jump("loc_140")

    label("loc_133")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x290, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_140")
    SetChrFlags(0x8, 0x10)

    label("loc_140")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_178")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_178")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 1)), scpexpr(EXPR_END)), "loc_161")
    OP_A2(0x2082)
    Jump("loc_178")

    label("loc_161")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x150, 0x2)"), scpexpr(EXPR_END)), "loc_171")
    Event(0, 5)
    Jump("loc_175")

    label("loc_171")

    Event(0, 4)

    label("loc_175")

    OP_A2(0x2082)

    label("loc_178")

    Return()

    # Function_0_FA end

    def Function_1_179(): pass

    label("Function_1_179")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BD")
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_71(0x5, 0x4)
    OP_71(0x6, 0x4)
    OP_79(0xFF, 0x2)
    OP_7A(0x8, 0x2)
    OP_C4(0x0, 0x1)
    OP_78(0x0, 0x0, 0x0)
    Jump("loc_1CF")

    label("loc_1BD")

    OP_16(0x2, 0xFA0, 0x76E58, 0xFFFD40E0, 0x23003A)

    label("loc_1CF")

    Return()

    # Function_1_179 end

    def Function_2_1D0(): pass

    label("Function_2_1D0")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x1, 0x20)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E8")
    OP_A2(0x1)

    label("loc_1E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26E")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇【爱的使者】高评价完成】\x01",          # 0
            "【◇【爱的使者】没有高评价完成】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_262"),
        (1, "loc_268"),
        (SWITCH_DEFAULT, "loc_26E"),
    )


    label("loc_262")

    OP_A2(0x1)
    Jump("loc_26E")

    label("loc_268")

    OP_A3(0x1)
    Jump("loc_26E")

    label("loc_26E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_469")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_356")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2E8")

    ChrTalk(    #0
        0xFE,
        (
            "菲前辈乘坐工房的飞船\x01",
            "出发前往雷斯顿要塞了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "听说是为了在那里更换\x01",
            "『埃尔赛尤』的引擎。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_353")

    label("loc_2E8")


    ChrTalk(    #2
        0xFE,
        (
            "那么～前辈不在的时候，\x01",
            "我就先一个人努力工作吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "在新的邂逅来临之前，\x01",
            "每天的工作就是我的恋人！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_353")

    Jump("loc_466")

    label("loc_356")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3FB")

    ChrTalk(    #4
        0xFE,
        (
            "为了装配『埃尔赛尤』的引擎，\x01",
            "似乎要到要塞那边更换。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "哈，我正准备向前辈提出\x01",
            "正式交往的请求呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "可恶的『埃尔赛尤』……\x01",
            "竟敢把我和前辈拆散～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_466")

    label("loc_3FB")


    ChrTalk(    #7
        0xFE,
        (
            "菲前辈乘坐工房的飞船\x01",
            "出发前往雷斯顿要塞了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "我、我今天原本打算向前辈\x01",
            "提出正式交往的请求呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_466")

    Jump("loc_10DB")

    label("loc_469")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_673")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_597")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_510")

    ChrTalk(    #9
        0xFE,
        (
            "唉，但是我\x01",
            "绝对不能够消沉下去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "总之要专注在工作上，\x01",
            "努力忘掉前辈的事才行！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "……不过，尽管话是这么说…\x01",
            "想彻底忘记又谈何容易啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_594")

    label("loc_510")


    ChrTalk(    #12
        0xFE,
        (
            "唉～前辈最近……\x01",
            "好像很幸福的样子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "看样子果然是和\x01",
            "以前的男友重修旧好了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "呜呜……\x01",
            "这就是所谓的『破镜重圆』吗。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_594")

    Jump("loc_670")

    label("loc_597")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_609")

    ChrTalk(    #15
        0xFE,
        (
            "不行！今天一定要向前辈\x01",
            "坦白我的心意才行！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "呼、呼啊～光是想象一下，\x01",
            "心脏就噗通噗通地跳个不停。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_670")

    label("loc_609")


    ChrTalk(    #17
        0xFE,
        (
            "决、决定了！今天我就要向\x01",
            "菲前辈做出正式的表白！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "毕竟我也是个男人，\x01",
            "不能老是这么优柔寡断。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_670")

    Jump("loc_10DB")

    label("loc_673")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 3)), scpexpr(EXPR_END)), "loc_7C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_6F0")

    ChrTalk(    #19
        0xFE,
        (
            "前辈虽然平时看起来很可爱，\x01",
            "工作起来却不输给男人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "嗯～太棒了。\x01",
            "这种美妙的错差感真令人受不了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C1")

    label("loc_6F0")


    ChrTalk(    #21
        0xFE,
        (
            "刚才经过这里的那两个人\x01",
            "是你们的游击士同伴吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "那、那个绑发带的女孩\x01",
            "实在是太可爱了啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "不过，穿着那么可爱的服装…\x01",
            "真的可以去和魔兽战斗吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "嗯～太棒了。\x01",
            "这种美妙的错差感真令人受不了啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_7C1")

    Jump("loc_10DB")

    label("loc_7C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_9C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_8EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_86E")

    ChrTalk(    #25
        0xFE,
        (
            "难道说菲前辈……\x01",
            "和以前的恋人重归于好了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        "呜啊啊啊～我真是个笨蛋。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "早知如此的话，在事态发展到这种地步之前\x01",
            "就应该展开攻势才对啊～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8E7")

    label("loc_86E")


    ChrTalk(    #28
        0xFE,
        (
            "为、为什么在诞辰庆典之后，\x01",
            "菲前辈的脸上就一直洋溢着幸福的微笑！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "难、难道说她和前男友\x01",
            "已经重修旧好了吗！？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_8E7")

    Jump("loc_9C1")

    label("loc_8EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_944")

    ChrTalk(    #30
        0xFE,
        (
            "可是，菲前辈和我\x01",
            "毕竟还没有正式交往。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "原、原本打算\x01",
            "在最近向她表白的…\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9C1")

    label("loc_944")


    ChrTalk(    #32
        0xFE,
        (
            "呵呵～和菲前辈一起参加的\x01",
            "诞辰庆典实在是太完美了～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "我们两个人静静地\x01",
            "眺望着『埃尔赛尤』……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        "真是太浪漫了啊。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_9C1")

    Jump("loc_10DB")

    label("loc_9C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_10DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x290, 0)), scpexpr(EXPR_END)), "loc_A8F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A3F")

    ChrTalk(    #35
        0xFE,
        (
            "不管是地震也好，\x01",
            "那个黑衣服的怪家伙也罢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "总有种不祥的预感啊。\x01",
            "但愿别发生什么事才好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A8C")

    label("loc_A3F")


    ChrTalk(    #37
        0xFE,
        (
            "虽然我不是很清楚，\x01",
            "但能帮上你们就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        "那么，我也要继续工作了……\x02",
    )

    CloseMessageWindow()

    label("loc_A8C")

    Jump("loc_10DB")

    label("loc_A8F")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 614200, 20, -53200, 0)
    SetChrPos(0xF7, 613000, 0, -53200, 0)
    SetChrPos(0x105, 614200, 0, -54440, 0)
    SetChrPos(0x104, 613000, 0, -54440, 0)
    OP_6B(2715, 0)
    OP_6D(613510, 10, -52620, 0)
    OP_0D()
    Sleep(600)

    ChrTalk(    #39
        0xFE,
        (
            "呼，真是的……\x01",
            "希望地震不要再来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "嗯，还有之前遇到的\x01",
            "那个怪家伙……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        "……总让人有种不祥的预感啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x101,
        (
            "#1002F怪家伙……\x02\x03",

            "……有那样的人出现吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    OP_8C(0xFE, 180, 400)
    Sleep(400)

    ChrTalk(    #43
        0xFE,
        (
            "啊、啊啊……\x01",
            "我昨天看见了一个奇怪的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "是我从来没见过的生面孔，\x01",
            "一言不发地就站在这个地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "因为这里平时不太有人走动，\x01",
            "所以让人感觉有点毛骨悚然。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_CB5")

    ChrTalk(    #46
        0x106,
        (
            "#052F确实值得注意啊……\x02\x03",

            "#050F能不能把那个人的\x01",
            "外貌特征详细地告诉我们？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D01")

    label("loc_CB5")


    ChrTalk(    #47
        0x103,
        (
            "#022F确实很值得注意啊……\x02\x03",

            "能不能把那个怪人的\x01",
            "外貌特征详细地告诉我们？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D01")

    TurnDirection(0xFE, 0xF7, 400)

    ChrTalk(    #48
        0xFE,
        "啊，那当然没问题。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        "总之是一名个子很高的家伙。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "除了身穿黑色大衣之外，\x01",
            "还戴着同样颜色的黑手套……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "其中最引人注目的\x01",
            "就是他脸上那一副墨镜。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x101,
        (
            "#1011F墨镜……\x02\x03",

            "#1015F…………那是什么东西啊？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #53
        0xFE,
        "那是一种可以遮挡阳光的特殊眼镜。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "你看到的话马上就会明白了。\x01",
            "因为整个镜片都是漆黑的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x101,
        (
            "#1004F那、那样的话\x01",
            "岂不是看不见前边了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "哈哈，不会的。\x01",
            "还是可以看见前方的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "只不过，这附近似乎\x01",
            "从没见过有人戴着那种东西呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_F0B")

    ChrTalk(    #58
        0x106,
        (
            "#050F嗯嗯，是吗……\x02\x03",

            "这可是相当有价值\x01",
            "的情报啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F42")

    label("loc_F0B")


    ChrTalk(    #59
        0x103,
        (
            "#026F嗯，是吗……\x02\x03",

            "#022F这可是相当有用\x01",
            "的情报啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F42")


    ChrTalk(    #60
        0x101,
        (
            "#1019F黑大衣、黑手套，\x01",
            "连眼镜也是黑色的……\x02\x03",

            "#1007F不管怎么想也是个\x01",
            "可疑的怪家伙啊。\x02\x03",

            "这件事情最好也向\x01",
            "雾香小姐报告一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_100B")

    ChrTalk(    #61
        0x106,
        (
            "#050F嗯，说的对。\x02\x03",

            "等堡垒的调查结束之后\x01",
            "再一起去报告吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1047")

    label("loc_100B")


    ChrTalk(    #62
        0x103,
        (
            "#020F嗯，没错。\x02\x03",

            "等堡垒的调查结束之后\x01",
            "再一起去报告吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1047")

    OP_8C(0xFE, 180, 400)

    ChrTalk(    #63
        0xFE,
        (
            "虽然不知道发生了什么事，\x01",
            "不过好像对你们有些用处？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        (
            "#1006F嗯，当然。\x02\x03",

            "真是谢谢了。\x01",
            "这些情报对我们非常有用。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1480)
    OP_A2(0x0)
    OP_28(0x85, 0x1, 0x8)
    OP_28(0x85, 0x1, 0x10)
    ClearChrFlags(0x8, 0x10)
    EventEnd(0x0)

    label("loc_10DB")

    TalkEnd(0x8)
    Return()

    # Function_2_1D0 end

    def Function_3_10DF(): pass

    label("Function_3_10DF")

    Return()

    # Function_3_10DF end

    def Function_4_10E0(): pass

    label("Function_4_10E0")

    EventBegin(0x0)
    OP_6D(619280, 500, -53640, 0)
    OP_67(0, 8500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 622820, 1000, -55100, 270)
    SetChrPos(0x102, 623820, 1000, -55100, 270)
    SetChrPos(0xF8, 624820, 1000, -55100, 270)
    SetChrPos(0xF9, 625820, 1000, -55100, 270)
    FadeToBright(1500, 0)
    OP_43(0x101, 0x1, 0x0, 0x6)
    Sleep(200)
    OP_43(0x102, 0x1, 0x0, 0x7)
    Sleep(100)
    OP_43(0xF8, 0x1, 0x0, 0x8)
    Sleep(200)
    OP_43(0xF9, 0x1, 0x0, 0x9)
    WaitChrThread(0xF8, 0x1)

    ChrTalk(    #65
        0x101,
        "#1020F这、这是……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xF9, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11F2")

    ChrTalk(    #66
        0x108,
        (
            "#072F不行啊……\x01",
            "眼前完全一片漆黑。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1260")

    label("loc_11F2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_122B")

    ChrTalk(    #67
        0x106,
        (
            "#055F喂喂……\x01",
            "根本什么都看不见啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1260")

    label("loc_122B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1260")

    ChrTalk(    #68
        0x103,
        "#022F没办法了……完全漆黑一团呢。\x02",
    )

    CloseMessageWindow()

    label("loc_1260")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12A7")

    ChrTalk(    #69
        0x107,
        (
            "#065F没、没有了导力灯，\x01",
            "这里竟然会变得这么暗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_132E")

    label("loc_12A7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12EE")

    ChrTalk(    #70
        0x103,
        (
            "#025F……没有了导力灯，\x01",
            "这里居然会变得这么暗啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_132E")

    label("loc_12EE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_132E")

    ChrTalk(    #71
        0x106,
        (
            "#057F没有了导力灯，\x01",
            "这里竟然会变得这么暗……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_132E")


    ChrTalk(    #72
        0x102,
        (
            "#1043F#5P如果不戴上『夜视眼镜』的话，\x01",
            "想通过这里实在太困难了……\x02\x03",

            "#1042F若是身上没有的话，\x01",
            "就回城镇上的道具店找找看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x101,
        (
            "#1007F嗯，明白了。\x02\x03",

            "#1002F看来，在通过这里时\x01",
            "最好要事先准备齐全呢。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_4_10E0 end

    def Function_5_13F7(): pass

    label("Function_5_13F7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(619280, 500, -53640, 0)
    OP_67(0, 8500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 622820, 1000, -55100, 270)
    SetChrPos(0x102, 623820, 1000, -55100, 270)
    SetChrPos(0xF8, 624820, 1000, -55100, 270)
    SetChrPos(0xF9, 625820, 1000, -55100, 270)
    OP_43(0x101, 0x1, 0x0, 0x6)
    Sleep(200)
    OP_43(0x102, 0x1, 0x0, 0x7)
    Sleep(100)
    OP_43(0xF8, 0x1, 0x0, 0x8)
    Sleep(200)
    OP_43(0xF9, 0x1, 0x0, 0x9)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0xF9, 0x1)
    Sleep(500)

    ChrTalk(    #74
        0x101,
        (
            "#1019F还好有夜视眼镜，\x01",
            "总算可以看见路了……\x02\x03",

            "但如果把它摘下来的话\x01",
            "就会又什么都看不见了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x102,
        (
            "#1035F#5P嗯，完全一片漆黑啊。\x02\x03",

            "#1042F如果不想迷路的话，\x01",
            "在通过这个地方时\x01",
            "就一定要戴着夜视眼镜啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x101,
        "#1002F嗯，了解。\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_5_13F7 end

    def Function_6_15A3(): pass

    label("Function_6_15A3")

    OP_8E(0xFE, 0x97EAA, 0x3E8, 0xFFFF28F6, 0x7D0, 0x0)
    OP_8E(0xFE, 0x9766C, 0x3E8, 0xFFFF26F8, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_6_15A3 end

    def Function_7_15D3(): pass

    label("Function_7_15D3")

    OP_8E(0xFE, 0x97EAA, 0x3E8, 0xFFFF28F6, 0x7D0, 0x0)
    OP_8E(0xFE, 0x97680, 0x3E8, 0xFFFF2A40, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_7_15D3 end

    def Function_8_1603(): pass

    label("Function_8_1603")

    OP_8E(0xFE, 0x97C7A, 0x3E8, 0xFFFF284C, 0x7D0, 0x0)
    OP_8E(0xFE, 0x979E6, 0x3E8, 0xFFFF266C, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_8_1603 end

    def Function_9_1633(): pass

    label("Function_9_1633")

    OP_8E(0xFE, 0x97EAA, 0x3E8, 0xFFFF28F6, 0x7D0, 0x0)
    OP_8E(0xFE, 0x979BE, 0x3E8, 0xFFFF29B4, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_9_1633 end

    SaveToFile()

Try(main)
