from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1300   ._SN',
        MapName             = 'Bose',
        Location            = 'T1300.x',
        MapIndex            = 1,
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
        '士兵卡多尔斯',                         # 9
        '士兵阿萨',                             # 10
        '玛诺利亚海岸方向',                     # 11
        '西柏斯街道方向',                       # 12
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
        'ED6_DT07/CH01640 ._CH',             # 00
        'ED6_DT07/CH01300 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH01640P._CP',             # 00
        'ED6_DT07/CH01300P._CP',             # 01
    )

    DeclNpc(
        X                   = -47800,
        Z                   = -50,
        Y                   = 11380,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -47800,
        Z                   = -50,
        Y                   = -8500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -50220,
        Z                   = -500,
        Y                   = -35780,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -40370,
        Z                   = -500,
        Y                   = 36990,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = -51690,
        TriggerZ            = -470,
        TriggerY            = 23510,
        TriggerRange        = 1500,
        ActorX              = -51690,
        ActorZ              = 1800,
        ActorY              = 23510,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -53780,
        TriggerZ            = -510,
        TriggerY            = -19530,
        TriggerRange        = 1500,
        ActorX              = -53780,
        ActorZ              = 1900,
        ActorY              = -19530,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -42460,
        TriggerZ            = -50,
        TriggerY            = -11830,
        TriggerRange        = 1700,
        ActorX              = -42460,
        ActorZ              = 1200,
        ActorY              = -11830,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1A6",          # 00, 0
        "Function_1_1BF",          # 01, 1
        "Function_2_21A",          # 02, 2
        "Function_3_397",          # 03, 3
        "Function_4_7D9",          # 04, 4
        "Function_5_B95",          # 05, 5
        "Function_6_BC3",          # 06, 6
        "Function_7_C52",          # 07, 7
        "Function_8_CE1",          # 08, 8
    )


    def Function_0_1A6(): pass

    label("Function_0_1A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1BE")
    SetChrPos(0x9, -45660, -50, -12110, 90)

    label("loc_1BE")

    Return()

    # Function_0_1A6 end

    def Function_1_1BF(): pass

    label("Function_1_1BF")

    OP_16(0x2, 0xFA0, 0xFFFD48B0, 0xFFFE17B8, 0x230044)
    OP_B1("T1300_n")
    OP_71(0x0, 0x10)
    OP_1C(0x0, 0x0, 0x8)
    OP_1C(0x1, 0x0, 0x8)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20D")
    OP_72(0x0, 0x10)
    OP_6F(0x0, 99)
    OP_72(0x1, 0x10)
    OP_6F(0x1, 99)

    label("loc_20D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_219")
    OP_64(0x2, 0x1)

    label("loc_219")

    Return()

    # Function_1_1BF end

    def Function_2_21A(): pass

    label("Function_2_21A")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23F")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_381")

    label("loc_23F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_258")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_381")

    label("loc_258")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_271")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_381")

    label("loc_271")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28A")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_381")

    label("loc_28A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A3")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_381")

    label("loc_2A3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BC")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_381")

    label("loc_2BC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D5")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_381")

    label("loc_2D5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EE")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_381")

    label("loc_2EE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_307")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_381")

    label("loc_307")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_320")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_381")

    label("loc_320")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_339")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_381")

    label("loc_339")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_352")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_381")

    label("loc_352")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36B")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_381")

    label("loc_36B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_381")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_381")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_396")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_381")

    label("loc_396")

    Return()

    # Function_2_21A end

    def Function_3_397(): pass

    label("Function_3_397")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_4B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_442")

    ChrTalk(    #0
        0xFE,
        (
            "就是在那个浮游物体出现后，\x01",
            "导力停止现象马上就发生了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "刚发现照明灯熄灭，\x01",
            "就看见湖面上出现了光亮。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "简直就像是日出时\x01",
            "太阳一样的强光。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_4AE")

    label("loc_442")


    ChrTalk(    #3
        0xFE,
        (
            "就是在那个浮游物体出现后，\x01",
            "导力停止现象马上就发生了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "刚发现照明灯熄灭，\x01",
            "就看见湖面上出现了光亮。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AE")

    Jump("loc_7D5")

    label("loc_4B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_602")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_599")

    ChrTalk(    #5
        0xFE,
        (
            "在这关所的卢安方向\x01",
            "也能很清楚地看见那个浮游物体。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "阿萨那家伙\x01",
            "竟然把警备工作扔下不管……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "那东西，到底\x01",
            "是什么呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "情报部的理查德上校\x01",
            "如果在的话就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "不管是什么疑问\x01",
            "他也一定可以解答。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_5FF")

    label("loc_599")


    ChrTalk(    #10
        0xFE,
        (
            "有关那个浮游物体的原因，\x01",
            "现在还是没有定论。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "呼，这种时候，要是情报部的\x01",
            "理查德上校在就好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5FF")

    Jump("loc_7D5")

    label("loc_602")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_666")

    ChrTalk(    #12
        0xFE,
        (
            "定期船恢复航行之后，\x01",
            "超市也重新开始营业了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "这样一来，龙的事件\x01",
            "总算是解决了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7D5")

    label("loc_666")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_6E4")

    ChrTalk(    #14
        0xFE,
        (
            "因为发生了龙的事件，\x01",
            "这里的关所也保持着警戒状态。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "呵，虽然应该不会再遭到袭击了，\x01",
            "不过还是不能松懈大意啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7D5")

    label("loc_6E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_7D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_753")

    ChrTalk(    #16
        0xFE,
        (
            "最近受通缉的魔兽相当多，\x01",
            "使得街道也陷入一片混乱之中。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "呼，在关所中\x01",
            "稍微休息一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7D5")

    label("loc_753")


    ChrTalk(    #18
        0xFE,
        (
            "呀，步行到这里\x01",
            "真是辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "最近受通缉的魔兽相当多，\x01",
            "使得街道也陷入一片混乱之中。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "呼，在关所中\x01",
            "稍微休息一下吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_7D5")

    TalkEnd(0x8)
    Return()

    # Function_3_397 end

    def Function_4_7D9(): pass

    label("Function_4_7D9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_8E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_87C")

    ChrTalk(    #21
        0xFE,
        (
            "现今的状况和湖上的浮游物体\x01",
            "究竟有什么关系呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "那种东西本来\x01",
            "直接击落就好，不过…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "似乎不太可能啊。\x01",
            "毕竟现在不能使用导力炮了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_8E2")

    label("loc_87C")


    ChrTalk(    #24
        0xFE,
        (
            "那种高度的话，火炮也打不到。\x01",
            "还有飞艇也不能用了…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "总之，想把那东西击落\x01",
            "根本就是不可能的嘛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8E2")

    Jump("loc_B91")

    label("loc_8E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_9BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_96F")

    ChrTalk(    #26
        0xFE,
        (
            "在这里也能很清楚地\x01",
            "看到那个浮游物体…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "怎么看也像是\x01",
            "人工制造的建筑物啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "就这么放着它不管\x01",
            "也没关系吗…\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_9B9")

    label("loc_96F")


    ChrTalk(    #29
        0xFE,
        (
            "怎么看也像是\x01",
            "人工制造的建筑物啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "就这么放着它不管\x01",
            "也没关系吗…\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9B9")

    Jump("loc_B91")

    label("loc_9BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_9F9")

    ChrTalk(    #31
        0xFE,
        "哟，辛苦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "走这么远的路，\x01",
            "一定累了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B91")

    label("loc_9F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_AEA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_A63")

    ChrTalk(    #33
        0xFE,
        (
            "情报部和空贼团都已经被捕了，\x01",
            "警备总算是稍微轻松了一点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        "啊，暂时还是很艰难啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_AE7")

    label("loc_A63")

    OP_A2(0x1)

    ChrTalk(    #35
        0xFE,
        (
            "因为定期船的原因，\x01",
            "现在这里几乎没有人了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "只是情报部的余党\x01",
            "和空贼团的漏网之鱼还是行踪不明。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "暂时还是\x01",
            "不能松懈啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AE7")

    Jump("loc_B91")

    label("loc_AEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_B91")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_B2C")

    ChrTalk(    #38
        0xFE,
        (
            "附近还有很多凶猛的魔兽。\x01",
            "请好好休息一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B91")

    label("loc_B2C")

    OP_A2(0x1)

    ChrTalk(    #39
        0xFE,
        (
            "哎呀，旅行者真是少见，\x01",
            "是步行来到这里的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "附近的魔兽可是很厉害啊。\x01",
            "请好好休息一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B91")

    TalkEnd(0xFE)
    Return()

    # Function_4_7D9 end

    def Function_5_B95(): pass

    label("Function_5_B95")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_AD(0x2400CF, 0x0, 0x0, 0x1F4)
    Sleep(500)
    OP_56(0x3)
    OP_AE(0x1F4)
    Sleep(500)
    OP_A2(0x20EA)
    TalkEnd(0xFF)
    Return()

    # Function_5_B95 end

    def Function_6_BC3(): pass

    label("Function_6_BC3")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #41
        (
            "\x07\x05东北　柏斯市　　　４４１塞尔矩\x01",
            "西南　卢安市　　　６６９塞尔矩\x01",
            "　　　玛诺利亚村　３５７塞尔矩\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_6_BC3 end

    def Function_7_C52(): pass

    label("Function_7_C52")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #42
        (
            "\x07\x05西南　卢安市　　　６６９塞尔矩\x01",
            "　　　玛诺利亚村　３５７塞尔矩\x01",
            "东北　柏斯市　　　４４１塞尔矩\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_7_C52 end

    def Function_8_CE1(): pass

    label("Function_8_CE1")

    TalkBegin(0xFF)
    Sleep(400)
    TalkEnd(0xFF)
    Return()

    # Function_8_CE1 end

    SaveToFile()

Try(main)
