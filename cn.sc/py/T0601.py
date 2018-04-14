from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'T0601   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0601.x',
        MapIndex            = 17,
        MapDefaultBGM       = "ed60016",
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
        '士兵塞维安',                           # 9
        '古利乌副队长',                         # 10
        '凯文神父',                             # 11
        '目标探索者',                           # 12
        '目标探索者',                           # 13
        '古利乌副队长',                         # 14
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
        Unknown_3A              = 17,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01640 ._CH',             # 00
        'ED6_DT27/CH03080 ._CH',             # 01
        'ED6_DT29/CH12581 ._CH',             # 02
        'ED6_DT07/CH01310 ._CH',             # 03
        'ED6_DT27/CH04000 ._CH',             # 04
        'ED6_DT27/CH04080 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT07/CH01640P._CP',             # 00
        'ED6_DT27/CH03080P._CP',             # 01
        'ED6_DT29/CH12581P._CP',             # 02
        'ED6_DT07/CH01310P._CP',             # 03
        'ED6_DT27/CH04000P._CP',             # 04
        'ED6_DT27/CH04080P._CP',             # 05
    )

    DeclNpc(
        X                   = -940,
        Z                   = 7250,
        Y                   = -94770,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -5540,
        Z                   = 7250,
        Y                   = -68220,
        Direction           = 266,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -5700,
        Y                   = -2000,
        Z                   = -21100,
        Range               = 3800,
        Unknown_10          = 0x2328,
        Unknown_14          = 0xFFFFBA14,
        Unknown_18          = 0x0,
        Unknown_1C          = 6,
    )


    ScpFunction(
        "Function_0_1BA",          # 00, 0
        "Function_1_240",          # 01, 1
        "Function_2_286",          # 02, 2
        "Function_3_29C",          # 03, 3
        "Function_4_2C0",          # 04, 4
        "Function_5_CBB",          # 05, 5
        "Function_6_D51",          # 06, 6
        "Function_7_E3D",          # 07, 7
        "Function_8_1A15",         # 08, 8
        "Function_9_2635",         # 09, 9
        "Function_10_2651",        # 0A, 10
        "Function_11_267A",        # 0B, 11
    )


    def Function_0_1BA(): pass

    label("Function_0_1BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1DC")
    SetChrPos(0x8, -2980, 7250, -67430, 335)
    OP_43(0x8, 0x0, 0x0, 0x2)
    Jump("loc_201")

    label("loc_1DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1E6")
    Jump("loc_201")

    label("loc_1E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 0)), scpexpr(EXPR_END)), "loc_1F5")
    ClearChrFlags(0x9, 0x80)
    Jump("loc_201")

    label("loc_1F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 6)), scpexpr(EXPR_END)), "loc_201")
    SetChrFlags(0x8, 0x80)

    label("loc_201")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_21D")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 7)

    label("loc_21D")

    OP_51(0xB, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_1BA end

    def Function_1_240(): pass

    label("Function_1_240")

    OP_16(0x2, 0xFA0, 0xFFFE0818, 0xFFFD7790, 0x230012)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_27C")
    OP_B1("t0601_y")
    OP_C4(0x0, 0x2)
    OP_7E(0xFC18, 0x1F4, 0x3E8, 0x96, 0x0)
    Jump("loc_285")

    label("loc_27C")

    OP_B1("t0601_n")

    label("loc_285")

    Return()

    # Function_1_240 end

    def Function_2_286(): pass

    label("Function_2_286")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_29B")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_286")

    label("loc_29B")

    Return()

    # Function_2_286 end

    def Function_3_29C(): pass

    label("Function_3_29C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2BF")
    OP_8D(0xFE, -3140, -97580, 1480, -73120, 3000)
    Jump("Function_3_29C")

    label("loc_2BF")

    Return()

    # Function_3_29C end

    def Function_4_2C0(): pass

    label("Function_4_2C0")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_3D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_388")

    ChrTalk(    #0
        0xFE,
        (
            "那个浮游岛好像是悬浮在\x01",
            "相当高的地方……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "这么说来，帝国军肯定\x01",
            "也在监视它吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "出现在王国领空的\x01",
            "谜样巨大飞行物体……吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "不，不要有什么\x01",
            "不切实际的误解就好……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_3D6")

    label("loc_388")


    ChrTalk(    #4
        0xFE,
        (
            "帝国军应该也在\x01",
            "监视那座岛吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "不，不要有什么\x01",
            "不切实际的误解就好……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D6")

    Jump("loc_CB7")

    label("loc_3D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_53E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D3")

    ChrTalk(    #6
        0xFE,
        (
            "那天晚上我看见了哦。\x01",
            "浮游岛出现的瞬间。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "好像太阳升起一般，\x01",
            "一下子照亮天空……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "等清醒过来那座岛\x01",
            "就在天空正中挂着了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "虽然难以置信，\x01",
            "但真的是从什么都没有的地方突然出现的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "好像很久以前\x01",
            "就已经在那里似的……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_53B")

    label("loc_4D3")


    ChrTalk(    #11
        0xFE,
        (
            "那座浮游岛，\x01",
            "真的是从什么都没有的地方突然出现的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "直到亲眼看习惯之前，\x01",
            "一直都觉得难以置信呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53B")

    Jump("loc_CB7")

    label("loc_53E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_620")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_59F")

    ChrTalk(    #13
        0xFE,
        (
            "晴空万里的蓝天\x01",
            "和浩瀚无边的大森林……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "这种对比\x01",
            "正是洛连特景色的魅力。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_61D")

    label("loc_59F")


    ChrTalk(    #15
        0xFE,
        (
            "晴空万里的蓝天\x01",
            "和浩瀚无边的大森林……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "嗯，洛连特\x01",
            "就是要这样才行啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "天空与大地的对比\x01",
            "正是这里景色的亮点嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_61D")

    Jump("loc_CB7")

    label("loc_620")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_708")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_679")

    ChrTalk(    #18
        0xFE,
        (
            "要是有那个雾，\x01",
            "周围都看不清了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "你们要是出城\x01",
            "也要多加注意哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_705")

    label("loc_679")


    ChrTalk(    #20
        0xFE,
        (
            "今天也没什么异常……\x01",
            "呼，虽然跟队长报告过了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "洛连特那边白茫茫的一片，\x01",
            "巡逻也没什么意义呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "你们要是出城\x01",
            "也要多加注意哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_705")

    Jump("loc_CB7")

    label("loc_708")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_7E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_769")

    ChrTalk(    #23
        0xFE,
        (
            "嗯～雾好像\x01",
            "比昨天更浓了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "我在这里工作也很久了，\x01",
            "这还是头一次遇到。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E5")

    label("loc_769")


    ChrTalk(    #25
        0xFE,
        (
            "嗯～雾好像\x01",
            "比昨天更浓了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "格兰赛尔那边的空气\x01",
            "今天也很清新……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "我在这里工作也很久了，\x01",
            "这还是头一次遇到。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_7E5")

    Jump("loc_CB7")

    label("loc_7E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_8D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_84F")

    ChrTalk(    #28
        0xFE,
        (
            "今天洛连特这边的景色\x01",
            "都笼罩在白色中了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "平时森林鲜艳的绿色\x01",
            "可是很耀眼的呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8D3")

    label("loc_84F")


    ChrTalk(    #30
        0xFE,
        (
            "王都那边是大晴天，\x01",
            "虽然风景优美……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "但另一方面，洛连特这边\x01",
            "却笼罩在白色之中。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "平时森林鲜艳的绿色\x01",
            "可是很耀眼的呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_8D3")

    Jump("loc_CB7")

    label("loc_8D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_946")

    ChrTalk(    #33
        0xFE,
        (
            "结果，『结社』和特务兵\x01",
            "那些家伙之后都没出现呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "王都有亲卫队\x01",
            "和游击士守护嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        "谢谢了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_CB7")

    label("loc_946")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 0)), scpexpr(EXPR_END)), "loc_99E")

    ChrTalk(    #36
        0xFE,
        (
            "『结社』的事情我们\x01",
            "也才刚刚听说。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "总之要赶快吧？\x01",
            "这里就交给我们吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CB7")

    label("loc_99E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_A0B")

    ChrTalk(    #38
        0xFE,
        "情报部的特务兵吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "虽然现在被追捕，\x01",
            "但以前可是精英部队啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        "要打起精神好好警戒了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_CB7")

    label("loc_A0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_C5E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CA, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C07")

    ChrTalk(    #41
        0xFE,
        "呀，欢迎来到格鲁纳门。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x12F, 0x8, 400)

    ChrTalk(    #42
        0x12F,
        (
            "#264F呼呼，记得在王都南边\x01",
            "也有相似的建筑物啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x12F, 400)

    ChrTalk(    #43
        0xFE,
        (
            "哈哈，这个建筑物呢，\x01",
            "是包围这个地区整体的长城——\x01",
            "亚宁堡的一部分。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "小妹妹看到的长城\x01",
            "是南边的圣海姆门吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x12F,
        (
            "#260F啊……明白啦，\x01",
            "是这么回事啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x12F, 0x101, 400)

    ChrTalk(    #46
        0x101,
        (
            "#1007F呼～啊，景色又好，\x01",
            "森林吹来的风也好舒服…\x02\x03",

            "#1006F我好像\x01",
            "挺喜欢这个地方的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x12F,
        (
            "#261F呼嘿嘿，姐姐真是的。\x02\x03",

            "#265F不过，真是巧呢……\x01",
            "玲也非常喜欢这个地方呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "哈哈，和圣海姆门不一样，\x01",
            "来的人很少，\x01",
            "是个很安静的地方呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1652)
    Jump("loc_C5B")

    label("loc_C07")


    ChrTalk(    #49
        0xFE,
        (
            "这个格鲁纳门\x01",
            "和圣海姆门不一样，\x01",
            "来的人很少吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        "所以应该是个安静的地方呢。\x02",
    )

    CloseMessageWindow()

    label("loc_C5B")

    Jump("loc_CB7")

    label("loc_C5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_CB7")

    ChrTalk(    #51
        0xFE,
        (
            "这里还是那么大，\x01",
            "警备起来很辛苦呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "好风景和清爽的风\x01",
            "多少也算是补偿了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CB7")

    TalkEnd(0x8)
    Return()

    # Function_4_2C0 end

    def Function_5_CBB(): pass

    label("Function_5_CBB")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 0)), scpexpr(EXPR_END)), "loc_D4D")

    ChrTalk(    #53
        0xFE,
        (
            "袭击你们的机械\x01",
            "说不定是那『结社』的东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "不只是周游道，\x01",
            "这一带也出现了的话，\x01",
            "就必须加强警戒了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "你们赶快\x01",
            "回王都协会吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D4D")

    TalkEnd(0x9)
    Return()

    # Function_5_CBB end

    def Function_6_D51(): pass

    label("Function_6_D51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D5E")
    Return()

    label("loc_D5E")

    EventBegin(0x0)
    Fade(1000)
    AddParty(0x8, 0xF7, 0xFF)
    SetChrPos(0x109, 3570, 7250, -68040, 90)
    SetChrPos(0x101, -780, 7250, -45000, 180)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3250, 0)
    OP_6C(145000, 0)
    OP_6E(262, 0)
    OP_69(0x101, 0x0)
    OP_6A(0x101)
    Sleep(100)
    OP_8E(0x101, 0xFFFFFDA8, 0x1C52, 0xFFFF2946, 0xBB8, 0x0)
    OP_6A(0xFF)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_6D(-1190, 7250, -61210, 2000)

    ChrTalk(    #56
        0x101,
        "#1025F#5P……啊………\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T4103   ._SN", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_6_D51 end

    def Function_7_E3D(): pass

    label("Function_7_E3D")

    EventBegin(0x0)
    AddParty(0x8, 0xF7, 0xFF)
    OP_31(0x8, 0x0, 0x37)
    OP_31(0x8, 0xFE, 0x0)
    OP_31(0x8, 0x5, 0x5A)
    OP_41(0x8, 0xE9, 0xFF)
    OP_41(0x8, 0x100, 0xFF)
    OP_41(0x8, 0x121, 0xFF)
    OP_41(0x8, 0x273, 0x0)
    OP_41(0x8, 0x25C, 0x1)
    OP_41(0x8, 0x259, 0x2)
    OP_41(0x8, 0x265, 0x3)
    OP_41(0x8, 0x262, 0x4)
    OP_35(0x8, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x109, 3570, 7250, -68040, 90)
    SetChrPos(0x101, -600, 7250, -54970, 180)
    OP_6D(-1190, 7250, -61210, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3250, 0)
    OP_6C(145000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #57
        0x101,
        "#1018F#5P约，约修──\x02",
    )

    CloseMessageWindow()

    def lambda_F0D():
        OP_8E(0x101, 0xFFFFFF74, 0x1C52, 0xFFFF15B4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_F0D)

    def lambda_F28():
        OP_6D(500, 7250, -63380, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F28)
    WaitChrThread(0x101, 0x0)
    OP_44(0x101, 0x1)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 65535)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #58
        0x101,
        "#1004F#6P啊……？\x02",
    )

    CloseMessageWindow()
    OP_6D(1140, 7250, -65340, 1200)
    OP_62(0x109, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_FAE():

        label("loc_FAE")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_FAE")

    QueueWorkItem2(0x109, 0, lambda_FAE)
    Sleep(400)

    ChrTalk(    #59
        0x109,
        (
            "#1064F#6P咦……\x02\x03",

            "艾丝蒂尔吗……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x101,
        (
            "#1020F#5P凯文先生……\x02\x03",

            "为…为什么会在这里…？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)
    Sleep(500)

    def lambda_102A():
        OP_8E(0xFE, 0xFFFFFBF0, 0x1C52, 0xFFFEF700, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_102A)

    def lambda_1045():
        OP_6D(160, 7250, -67940, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1045)

    def lambda_105D():
        OP_67(0, 8210, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_105D)

    def lambda_1075():
        OP_6B(2570, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1075)

    def lambda_1085():
        OP_6E(334, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1085)
    OP_6C(134000, 3000)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x101, 270, 400)
    Sleep(500)
    OP_8C(0x101, 90, 400)
    Sleep(500)
    OP_8C(0x101, 180, 400)
    Sleep(500)

    ChrTalk(    #61
        0x101,
        "#1026F#6P不，不在这里……\x02",
    )

    CloseMessageWindow()
    OP_44(0x109, 0x0)
    OP_8E(0x109, 0x244, 0x1C52, 0xFFFEF746, 0x7D0, 0x0)

    ChrTalk(    #62
        0x109,
        (
            "#1062F#5P呀～好久不见啦。\x02\x03",

            "#1061F不过竟能在这种地方重逢，\x01",
            "我们果然有缘──\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 600)

    ChrTalk(    #63
        0x101,
        (
            "#1002F#4P对了，凯文先生！\x02\x03",

            "你在这里\x01",
            "碰到过什么其它人吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x109,
        (
            "#1064F#5P咦……什么人啊。\x02\x03",

            "难道艾丝蒂尔\x01",
            "也是在这里等人吗～？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x101,
        (
            "#1026F#4P啊，嗯……\x02\x03",

            "#1015F……那，凯文先生也是？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x109,
        (
            "#1063F#5P啊啊……\x01",
            "收到一封信，要我来这里的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x101,
        (
            "#1011F#4P我，我也是。\x02\x03",

            "#1016F嘿嘿。\x01",
            "居然有这么有趣的巧合啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x109,
        (
            "#1061F#5P哈哈，是呢～\x02\x03",

            "#1069F──唔？\x01",
            "会有这种巧合吗！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x101,
        (
            "#1015F#4P难，难道说？\x02\x03",

            "凯文先生\x01",
            "也是被约修亚叫来的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x109,
        (
            "#1064F#5P约修亚？\x02\x03",

            "就是……\x01",
            "你那个男朋友？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x101,
        "#1026F#4P嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x109,
        (
            "#1067F#5P我，我不知道……\x02\x03",

            "约修亚其实\x01",
            "是个上了年纪的大叔吗。\x02\x03",

            "#1068F当然，如果有爱，\x01",
            "年龄差距倒也不是问题……\x02\x03",

            "既然如此\x01",
            "我也还是很有机会的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x101,
        (
            "#1007F#4P那个～\x01",
            "我觉得话题好像\x01",
            "微妙的错开了。\x02\x03",

            "#1015F凯文先生是被谁的\x01",
            "信叫出来的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x109,
        (
            "#1060F#5P啊啊，格兰赛尔大圣堂\x01",
            "收到了给我的信。\x02\x03",

            "送来信的人好像是个体面的\x01",
            "中年男子……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x101,
        (
            "#1019F#4P约，约修亚\x01",
            "和我同年的啦！\x02\x03",

            "不可能是大叔吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x109,
        (
            "#1064F#5P啊，果然？\x02\x03",

            "#1061F呀～我也正觉得\x01",
            "有点奇怪呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x101,
        (
            "#1007F#4P说的没错……\x02\x03",

            "#1002F不过，那\x01",
            "到底是怎么回事呢？\x02\x03",

            "难、难道说……\x02",
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
            "【真的只是巧合？】\x01",              # 0
            "【为了解决两人设下的陷阱】\x01",      # 1
            "【中年男子是约修亚的变装】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_15D8"),
        (1, "loc_161F"),
        (2, "loc_165C"),
        (SWITCH_DEFAULT, "loc_16DC"),
    )


    label("loc_15D8")


    ChrTalk(    #78
        0x109,
        (
            "#1067F#5P嗯，虽然可能性\x01",
            "不是零……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Jump("loc_16DC")

    label("loc_161F")

    OP_2B(0x8E, 0x3)

    ChrTalk(    #79
        0x109,
        "#1063F#5P什么……？\x02",
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Jump("loc_16DC")

    label("loc_165C")

    OP_2B(0x8E, 0x1)

    ChrTalk(    #80
        0x109,
        (
            "#1064F#5P哈～想到\x01",
            "奇怪的事了。\x02\x03",

            "#1063F约修亚\x01",
            "很会变装吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x101,
        "#1015F#4P嗯～很难说……\x02",
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Jump("loc_16DC")

    label("loc_16DC")

    OP_20(0x3E8)

    def lambda_16E7():
        OP_6B(2850, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_16E7)
    OP_51(0xB, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xC, 0x4)
    SetChrPos(0xB, 11930, 10500, -73000, 90)
    SetChrPos(0xC, -11930, 10500, -62000, 270)
    OP_22(0xCF, 0x1, 0xA)
    OP_43(0xB, 0x3, 0x0, 0x2)
    OP_43(0xC, 0x3, 0x0, 0x2)

    def lambda_1756():
        OP_8E(0xFE, 0xFFFFFB96, 0x2134, 0xFFFEE2D8, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1756)

    def lambda_1771():
        OP_8E(0xFE, 0xFFFFFDDA, 0x2134, 0xFFFF0DD0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1771)
    Sleep(100)
    OP_24(0xCF, 0x1E)
    Sleep(100)
    OP_24(0xCF, 0x32)
    Sleep(100)
    OP_24(0xCF, 0x3C)
    Sleep(100)
    OP_24(0xCF, 0x46)
    Sleep(100)
    OP_24(0xCF, 0x50)
    Sleep(100)
    OP_24(0xCF, 0x5A)
    Sleep(100)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_24(0xCF, 0x64)
    WaitChrThread(0xC, 0x1)

    def lambda_17E7():
        OP_97(0xFE, 0xFFFFFBF0, 0xFFFEF700, 0x57E40, 0x2AF8, 0x1)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_17E7)
    WaitChrThread(0xB, 0x1)

    def lambda_1808():
        OP_97(0xFE, 0xFFFFFBF0, 0xFFFEF700, 0x57E40, 0x2AF8, 0x1)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_1808)
    OP_1D(0x35)
    OP_8C(0x101, 0, 600)
    OP_8C(0x109, 180, 600)

    ChrTalk(    #82 op#A
        0x101,
        "#1020F#6P#12A什…么\x02",
    )

    Sleep(1200)

    ChrTalk(    #83 op#A
        0x109,
        "#1063F#5P#12A真的假的……\x02",
    )

    Sleep(1200)

    def lambda_1874():
        OP_95(0xFE, 0x0, 0x0, 0x1F4, 0xFA, 0x1770)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1874)
    SetChrChipByIndex(0x101, 4)
    SetChrSubChip(0x101, 0)
    OP_22(0xD5, 0x0, 0x64)
    Sleep(100)

    def lambda_18A6():
        OP_95(0xFE, 0x0, 0x0, 0xFFFFFE0C, 0xFA, 0x1770)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_18A6)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 5)
    SetChrSubChip(0x109, 0)
    WaitChrThread(0xB, 0x0)
    OP_8C(0xB, 0, 400)
    WaitChrThread(0xC, 0x0)
    OP_8C(0xC, 180, 400)

    def lambda_18EB():
        OP_91(0xFE, 0x0, 0xFFFFFA24, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_18EB)

    def lambda_1906():
        OP_91(0xFE, 0x0, 0xFFFFFA24, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1906)
    Sleep(500)

    def lambda_1926():
        OP_91(0xFE, 0x0, 0xFFFFFE0C, 0x0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1926)

    def lambda_1941():
        OP_91(0xFE, 0x0, 0xFFFFFE0C, 0x0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1941)
    Sleep(1000)

    ChrTalk(    #84
        0x109,
        (
            "#1067F#5P哼，好像也不是\x01",
            "认错人的感觉……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x101,
        "#1005F#6P嗯……来了！\x02",
    )

    CloseMessageWindow()

    def lambda_19AA():
        OP_6B(2100, 500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_19AA)

    def lambda_19BA():
        OP_8E(0xFE, 0xFFFFFDA8, 0x1C52, 0xFFFEF278, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_19BA)

    def lambda_19D5():
        OP_8E(0xFE, 0xFFFFFE70, 0x1C52, 0xFFFEFDF4, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_19D5)
    WaitChrThread(0xB, 0x1)
    OP_23(0xCF)
    Battle(0x45A, 0x0, 0x1, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_1A0B"),
        (SWITCH_DEFAULT, "loc_1A10"),
    )


    label("loc_1A0B")

    OP_B4(0x0)
    Jump("loc_1A10")

    label("loc_1A10")

    Call(0, 8)
    Return()

    # Function_7_E3D end

    def Function_8_1A15(): pass

    label("Function_8_1A15")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_1D(0x51)
    Sleep(500)
    OP_6D(-430, 7250, -70700, 0)
    OP_67(0, 8210, -10000, 0)
    OP_6B(2580, 0)
    OP_6C(134000, 0)
    OP_6E(334, 0)
    OP_51(0xB, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xC, 0x4)
    SetChrPos(0x101, -2170, 7250, -68100, 180)
    SetChrPos(0x109, -180, 7250, -67940, 180)
    SetChrPos(0xB, -2080, 8500, -72570, 0)
    SetChrPos(0xC, 800, 8500, -72820, 0)
    OP_43(0xB, 0x3, 0x0, 0x2)
    OP_43(0xC, 0x3, 0x0, 0x2)
    OP_22(0xCF, 0x1, 0x64)
    OP_24(0xCF, 0x64)
    SetChrChipByIndex(0x101, 4)
    SetChrChipByIndex(0x109, 5)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x109, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #86
        0x101,
        "#1005F#6P这，这些家伙……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x109,
        "#1063F！！\x02",
    )

    CloseMessageWindow()
    OP_8C(0xB, 270, 400)
    OP_8C(0xC, 270, 400)

    def lambda_1B54():
        OP_6D(-6930, 7250, -69700, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1B54)

    def lambda_1B6C():
        OP_8E(0xFE, 0xFFFFB9CE, 0x280A, 0xFFFEE8DC, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1B6C)
    Sleep(200)

    def lambda_1B8C():
        OP_8E(0xFE, 0xFFFFB9CE, 0x280A, 0xFFFEE8DC, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1B8C)

    def lambda_1BA7():

        label("loc_1BA7")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_1BA7")

    QueueWorkItem2(0x101, 2, lambda_1BA7)

    def lambda_1BB8():

        label("loc_1BB8")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_1BB8")

    QueueWorkItem2(0x109, 2, lambda_1BB8)
    OP_24(0xCF, 0x5A)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(200)
    OP_24(0xCF, 0x5A)
    Sleep(150)
    OP_24(0xCF, 0x50)
    Sleep(150)
    OP_24(0xCF, 0x46)
    Sleep(100)
    OP_24(0xCF, 0x3C)
    Sleep(100)
    OP_24(0xCF, 0x32)
    Sleep(100)
    OP_24(0xCF, 0x28)
    Sleep(100)
    OP_24(0xCF, 0x1E)
    Sleep(100)
    OP_24(0xCF, 0x14)
    Sleep(100)
    OP_24(0xCF, 0xA)
    Sleep(100)
    OP_23(0xCF)

    ChrTalk(    #88
        0x101,
        "#1004F#6P啊……！？\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0x2)
    OP_44(0x109, 0x2)
    SetChrChipByIndex(0x101, 65535)

    def lambda_1C63():
        OP_8E(0xFE, 0xFFFFEEB2, 0x1C52, 0xFFFEF58E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1C63)
    Sleep(200)
    SetChrChipByIndex(0x109, 65535)

    def lambda_1C88():
        OP_8E(0xFE, 0xFFFFEDEA, 0x1C52, 0xFFFEF066, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1C88)
    WaitChrThread(0x109, 0x1)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x109, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_6D(-4350, 7250, -69080, 1500)
    OP_63(0x101)
    OP_63(0x109)

    ChrTalk(    #89
        0x101,
        (
            "#1020F#6P什，什么啊……\x02\x03",

            "这些机械……\x01",
            "与其说是魔兽……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x109,
        (
            "#1063F#5P啊啊，似乎和城中封印区域里的\x01",
            "人形兵器一样。\x02\x03",

            "#1065F不过和那不同的是，\x01",
            "好像是最近制造的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 400)

    ChrTalk(    #91
        0x101,
        "#1015F#6P这是怎么回事？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 400)

    ChrTalk(    #92
        0x109,
        (
            "#1060F封印区域的人形兵器\x01",
            "如果说是一种古代遗物……\x02\x03",

            "那刚才机械的就是导力驱动的\x01",
            "现代人形兵器。\x02\x03",

            "而且性能\x01",
            "似乎毫不逊色。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x101,
        (
            "#1007F#6P原，原来如此……\x02\x03",

            "……………………………………\x02\x03",

            "#1019F为什么凯文先生\x01",
            "知道封印区域的事？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x109,
        "#1064F……（惊讶）。\x02",
    )

    CloseMessageWindow()
    OP_4A(0x8, 255)
    SetChrPos(0xD, -1180, 7250, -58700, 180)
    SetChrPos(0x8, -570, 7250, -57570, 180)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0x8, 0x80)

    NpcTalk(    #95
        0x8,
        "男人的声音",
        "#2P喂，在干什么！？\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x109, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_1F3D():

        label("loc_1F3D")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_1F3D")

    QueueWorkItem2(0x101, 2, lambda_1F3D)

    def lambda_1F4E():

        label("loc_1F4E")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_1F4E")

    QueueWorkItem2(0x109, 2, lambda_1F4E)
    Fade(1000)
    OP_6D(-2190, 7250, -67000, 0)
    OP_67(0, 7650, -10000, 0)
    OP_6B(2420, 0)
    OP_6C(89000, 0)
    OP_6E(334, 0)
    OP_6E(334, 0)

    def lambda_1FAA():
        OP_8E(0xFE, 0xFFFFFAA6, 0x1C52, 0xFFFF031D, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1FAA)
    Sleep(300)

    def lambda_1FCA():
        OP_8E(0xFE, 0xFFFFFDE4, 0x1C52, 0xFFFF0614, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1FCA)
    WaitChrThread(0xD, 0x1)
    OP_8C(0xD, 225, 400)
    WaitChrThread(0x8, 0x1)
    OP_8C(0x8, 225, 400)
    OP_44(0x101, 0x2)
    OP_44(0x109, 0x2)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #96
        0x101,
        "#1004F#6P啊，士兵先生……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xD,
        "#5P就觉得有什么骚动……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xD,
        (
            "#5P你们在这里\x01",
            "干什么！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x101,
        (
            "#1020F#6P等、等一下！\x02\x03",

            "我们只是在这里被奇怪的\x01",
            "机械袭击……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xD,
        "#5P奇怪的机械……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x109,
        (
            "#1062F啊啊，惊动你们\x01",
            "实在是不好意思。\x02\x03",

            "其实她是协会\x01",
            "所属的游击士。\x02\x03",

            "为追捕某些人，\x01",
            "正在调查中。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x101,
        "#1004F#6P啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xD,
        "#5P游击士……真的吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x109,
        (
            "#1060F那，艾丝蒂尔。\x01",
            "把游击士手册给他们看吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x101,
        "#1015F#6P啊，嗯……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #106
        "\x07\x05艾丝蒂尔急忙展示了游击士手册。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #107
        0xD,
        "#5P……原来如此，好像是真的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xD,
        (
            "#5P某些人\x01",
            "到底是什么人？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x109,
        (
            "#1065F是称为『结社』\x01",
            "身份不明的家伙们。\x02\x03",

            "似乎在各地进行\x01",
            "各种各样奇怪的实验。\x02\x03",

            "#1063F我们追寻他们的线索\x01",
            "来到这里，\x01",
            "却被奇怪的机械袭击了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x101,
        "#1026F#6P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xD,
        (
            "#5P这么说来司令部\x01",
            "发来了关于『结社』那些家伙的\x01",
            "注意事项……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xD,
        (
            "#5P那么说周游道出现的\x01",
            "就是那个『结社』的人吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x101,
        (
            "#1020F#6P啊，等一下！\x02\x03",

            "周游道出现了……？\x01",
            "到底发生什么事？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xD,
        (
            "#5P啊啊，之前艾尔贝离宫的\x01",
            "警备本部发来了联络。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xD,
        (
            "#5P似乎是有某个不明武装集团\x01",
            "袭击了离宫。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #116
        0x101,
        "#1005F#6P你、你说什么～！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xD,
        (
            "#5P幸好有希德中校在，\x01",
            "似乎轻松击退了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xD,
        (
            "#5P现在，周游道已被封锁，\x01",
            "军队正在追捕那个集团。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x109,
        (
            "#1068F呼啦～\x01",
            "发生了大事啊。\x02\x03",

            "那我们也暂时\x01",
            "返回协会比较好吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x101,
        "#1026F#6P呼，啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xD,
        (
            "#5P啊啊，说不定\x01",
            "就是你们\x01",
            "在追捕的人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xD,
        (
            "#5P好啦，附近的警戒\x01",
            "就这样交给我们吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xD,
        (
            "#5P你们赶快\x01",
            "回王都协会吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x109,
        (
            "#1061F谢谢！\x02\x03",

            "#1062F那艾丝蒂尔。\x01",
            "赶快回去吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_25A0():

        label("loc_25A0")

        TurnDirection(0xFE, 0x109, 400)
        OP_48()
        Jump("loc_25A0")

    QueueWorkItem2(0x101, 2, lambda_25A0)

    ChrTalk(    #125
        0x101,
        "#1020F#6P等、等等……\x02",
    )

    CloseMessageWindow()

    def lambda_25CC():

        label("loc_25CC")

        TurnDirection(0xFE, 0x109, 400)
        OP_48()
        Jump("loc_25CC")

    QueueWorkItem2(0xD, 2, lambda_25CC)

    def lambda_25DD():

        label("loc_25DD")

        TurnDirection(0xFE, 0x109, 400)
        OP_48()
        Jump("loc_25DD")

    QueueWorkItem2(0x8, 2, lambda_25DD)
    OP_43(0x109, 0x0, 0x0, 0xA)
    Sleep(1500)
    OP_44(0x101, 0x2)
    OP_43(0x101, 0x0, 0x0, 0xB)
    OP_6D(-2110, 7250, -63810, 3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x109, 0x1)
    OP_44(0x101, 0x1)
    SetMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T0610   ._SN", 107, 0, 0)
    IdleLoop()
    Return()

    # Function_8_1A15 end

    def Function_9_2635(): pass

    label("Function_9_2635")

    OP_8E(0xFE, 0xFFFFFD3A, 0x1C52, 0xFFFEF9E4, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x101, 400)
    Return()

    # Function_9_2635 end

    def Function_10_2651(): pass

    label("Function_10_2651")

    OP_8E(0xFE, 0xFFFFF51A, 0x1C52, 0xFFFEF84A, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFF8F8, 0x1C52, 0xFFFF30D0, 0xBB8, 0x0)
    Return()

    # Function_10_2651 end

    def Function_11_267A(): pass

    label("Function_11_267A")

    OP_8E(0xFE, 0xFFFFF4B6, 0x1C52, 0xFFFEFC82, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFF8F8, 0x1C52, 0xFFFF30D0, 0xBB8, 0x0)
    Return()

    # Function_11_267A end

    SaveToFile()

Try(main)
