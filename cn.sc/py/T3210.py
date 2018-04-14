from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3210   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3210.x',
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '林',                                   # 9
        '希利尔',                               # 10
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
        'ED6_DT07/CH01030 ._CH',             # 00
        'ED6_DT07/CH01120 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH01030P._CP',             # 00
        'ED6_DT07/CH01120P._CP',             # 01
    )

    DeclNpc(
        X                   = 28010,
        Z                   = 0,
        Y                   = 4920,
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
        X                   = 3350,
        Z                   = 250,
        Y                   = 3380,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )


    ScpFunction(
        "Function_0_FA",           # 00, 0
        "Function_1_13B",          # 01, 1
        "Function_2_13C",          # 02, 2
        "Function_3_58F",          # 03, 3
    )


    def Function_0_FA(): pass

    label("Function_0_FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_104")
    Jump("loc_13A")

    label("loc_104")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_10E")
    Jump("loc_13A")

    label("loc_10E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_118")
    Jump("loc_13A")

    label("loc_118")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_133")
    SetChrPos(0x8, 27000, 0, 3050, 270)
    Jump("loc_13A")

    label("loc_133")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_13A")

    label("loc_13A")

    Return()

    # Function_0_FA end

    def Function_1_13B(): pass

    label("Function_1_13B")

    Return()

    # Function_1_13B end

    def Function_2_13C(): pass

    label("Function_2_13C")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_203")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C1")

    ChrTalk(    #0
        0xFE,
        (
            "我从来巡逻的士兵\x01",
            "那里听说了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "现在整个利贝尔\x01",
            "好像都不能使用导力器。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "那、那不是\x01",
            "挺麻烦的吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_200")

    label("loc_1C1")


    ChrTalk(    #3
        0xFE,
        (
            "全国的导力器\x01",
            "竟然都停下来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        "……真令人无法相信。\x02",
    )

    CloseMessageWindow()

    label("loc_200")

    Jump("loc_58B")

    label("loc_203")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_255")

    ChrTalk(    #5
        0xFE,
        (
            "好～像温泉又\x01",
            "发生什么事了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "导力灯也打不开，\x01",
            "是怎么回事呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58B")

    label("loc_255")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_344")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2AE")

    ChrTalk(    #7
        0x8,
        (
            "总算水的温度也\x01",
            "好像恢复正常了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "『红叶亭』的澡堂\x01",
            "看来能用了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_341")

    label("loc_2AE")


    ChrTalk(    #9
        0x8,
        (
            "总算水的温度也\x01",
            "好像恢复正常了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "『红叶亭』的澡堂\x01",
            "看来能用了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        (
            "说起来最近\x01",
            "好像发生了地震……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        (
            "这次的温泉的事也跟\x01",
            "那个有关系？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_341")

    Jump("loc_58B")

    label("loc_344")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_422")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3A4")

    ChrTalk(    #13
        0x8,
        (
            "可我们村的温泉\x01",
            "是直接从后山取的水啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        "难道是在源泉那边发生了什么事？\x02",
    )

    CloseMessageWindow()
    Jump("loc_41F")

    label("loc_3A4")


    ChrTalk(    #15
        0x8,
        (
            "我想外面怎么这么吵，\x01",
            "原来是温泉的水沸腾了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        (
            "对主妇来说不用花时间\x01",
            "烧开水可是件好事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        "不过问题不在这里。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_41F")

    Jump("loc_58B")

    label("loc_422")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_4D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_46F")

    ChrTalk(    #18
        0x8,
        (
            "最近我女儿也在\x01",
            "旅馆打工。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        (
            "在认真地做\x01",
            "就很好了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D0")

    label("loc_46F")


    ChrTalk(    #20
        0x8,
        (
            "我女儿终于\x01",
            "也开始工作了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        (
            "不过也只是\x01",
            "旅馆的帮工而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        "但只要不是闲在家里就好。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_4D0")

    Jump("loc_58B")

    label("loc_4D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_58B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_53C")

    ChrTalk(    #23
        0x8,
        (
            "我丈夫是在『红叶亭』\x01",
            "做东方料理的厨师哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        (
            "评价好像还不错，\x01",
            "经常有杂志来采访。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58B")

    label("loc_53C")


    ChrTalk(    #25
        0x8,
        (
            "哎呀，莫非你们\x01",
            "在找旅馆？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        (
            "『红叶亭』就在\x01",
            "外面的大街走到底的地方。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_58B")

    TalkEnd(0x8)
    Return()

    # Function_2_13C end

    def Function_3_58F(): pass

    label("Function_3_58F")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_686")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_641")

    ChrTalk(    #27
        0xFE,
        (
            "哎呀，泵能够修好\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "旅馆的营业当然\x01",
            "也一样……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "最重要的是\x01",
            "省去烧开水的工夫了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "在如今这种不能使用导力器的\x01",
            "时候就更是如此了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_683")

    label("loc_641")


    ChrTalk(    #31
        0xFE,
        (
            "泵能够修好\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "最重要的是\x01",
            "省去烧开水的工夫了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_683")

    Jump("loc_B42")

    label("loc_686")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_785")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_726")

    ChrTalk(    #33
        0xFE,
        (
            "导力器不能用了，\x01",
            "温泉的泵也停止运转了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "温泉可是我们村子招揽\x01",
            "疗养客人的法宝啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "不快点修好的话，\x01",
            "我们的生活可就不好过了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_782")

    label("loc_726")


    ChrTalk(    #36
        0xFE,
        (
            "导力器不能用了，\x01",
            "温泉的泵也停止运转了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "不快点修好的话，\x01",
            "我们的生活可就不好过了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_782")

    Jump("loc_B42")

    label("loc_785")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_7F2")

    ChrTalk(    #38
        0x9,
        (
            "温泉的水温\x01",
            "也好像恢复正常了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x9,
        (
            "尽管如此\x01",
            "这真是件怪事啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x9,
        (
            "可能还是因为地震\x01",
            "的影响吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B42")

    label("loc_7F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_8B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_84D")

    ChrTalk(    #41
        0x9,
        (
            "说不定是地壳\x01",
            "产生变化了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x9,
        (
            "而且还发生了地震，\x01",
            "完全有那个可能性。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8B0")

    label("loc_84D")


    ChrTalk(    #43
        0x9,
        "呼，真令人感到为难。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x9,
        (
            "温泉不能用的话\x01",
            "旅馆也不能营业了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x9,
        (
            "说不定是地壳\x01",
            "产生变化了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_8B0")

    Jump("loc_B42")

    label("loc_8B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_A6E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x70, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_937")

    ChrTalk(    #46
        0x9,
        (
            "我、我刚才看见我家后面\x01",
            "有什么东西飞快地\x01",
            "跑过去了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x9,
        (
            "那、那到底\x01",
            "是什么？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x9,
        (
            "看、看上去\x01",
            "像是魔兽……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A6B")

    label("loc_937")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_9AF")

    ChrTalk(    #49
        0x9,
        (
            "听说露天浴场好像\x01",
            "有偷窥犯出没，要小心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x9,
        (
            "实在无法相信这个\x01",
            "村里会有那种人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x9,
        "一定是客人的错觉。\x02",
    )

    CloseMessageWindow()
    Jump("loc_A6B")

    label("loc_9AF")


    ChrTalk(    #52
        0x9,
        (
            "我从在旅馆工作的\x01",
            "老婆那里听说了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x9,
        (
            "听说露天浴场好像\x01",
            "有偷窥犯出没，要小心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x9,
        (
            "实在无法相信这个\x01",
            "村里会有那种人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x9,
        (
            "毛婆婆为慎重起见\x01",
            "好像联系协会了，\x01",
            "一定是客人的错觉。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_A6B")

    Jump("loc_B42")

    label("loc_A6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_B42")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_ACF")

    ChrTalk(    #56
        0x9,
        (
            "呀，欢迎。\x01",
            "欢迎来到亚尔摩村。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x9,
        (
            "这里自古以来就是温泉地区。\x01",
            "常客也很多。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B42")

    label("loc_ACF")


    ChrTalk(    #58
        0x9,
        (
            "呀，欢迎。\x01",
            "欢迎来到亚尔摩村。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x9,
        "你们也是来做温泉疗养的吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x9,
        (
            "这里自古以来就是温泉地区。\x01",
            "常客也很多。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_B42")

    TalkEnd(0x9)
    Return()

    # Function_3_58F end

    SaveToFile()

Try(main)
