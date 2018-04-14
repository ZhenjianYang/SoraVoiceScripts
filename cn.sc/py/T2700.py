from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2700   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2700.x',
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
        '士兵尼克斯',                           # 9
        '士兵威尔斯',                           # 10
        '士兵库隆',                             # 11
        '梅尔茨',                               # 12
        '阿伊纳街道',                           # 13
        '卡鲁迪亚隧道',                         # 14
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
        'ED6_DT07/CH01300 ._CH',             # 02
        'ED6_DT07/CH01760 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT07/CH01640P._CP',             # 00
        'ED6_DT07/CH01300P._CP',             # 01
        'ED6_DT07/CH01300P._CP',             # 02
        'ED6_DT07/CH01760P._CP',             # 03
    )

    DeclNpc(
        X                   = 18400,
        Z                   = 5000,
        Y                   = 1400,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -18600,
        Z                   = 0,
        Y                   = 2300,
        Direction           = 270,
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
        X                   = 18400,
        Z                   = 5000,
        Y                   = 1400,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -22780,
        Z                   = 0,
        Y                   = 6880,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -62340,
        Z                   = 0,
        Y                   = -1100,
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
        X                   = 21320,
        Z                   = 5000,
        Y                   = 460,
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
        TriggerX            = 19830,
        TriggerZ            = 5000,
        TriggerY            = -50,
        TriggerRange        = 800,
        ActorX              = 19830,
        ActorZ              = 6000,
        ActorY              = -50,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -45890,
        TriggerZ            = 0,
        TriggerY            = 2240,
        TriggerRange        = 1500,
        ActorX              = -45890,
        ActorZ              = 1700,
        ActorY              = 2240,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 3110,
        TriggerZ            = 5000,
        TriggerY            = 2490,
        TriggerRange        = 1000,
        ActorX              = 7850,
        ActorZ              = -5000,
        ActorY              = 9160,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1F6",          # 00, 0
        "Function_1_255",          # 01, 1
        "Function_2_2D8",          # 02, 2
        "Function_3_3A6",          # 03, 3
        "Function_4_461",          # 04, 4
        "Function_5_788",          # 05, 5
        "Function_6_CF1",          # 06, 6
        "Function_7_DDD",          # 07, 7
        "Function_8_1192",         # 08, 8
        "Function_9_19E6",         # 09, 9
        "Function_10_1A7F",        # 0A, 10
        "Function_11_1AC9",        # 0B, 11
        "Function_12_1B2D",        # 0C, 12
        "Function_13_1B39",        # 0D, 13
    )


    def Function_0_1F6(): pass

    label("Function_0_1F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_21E")
    SetChrPos(0x8, 18400, 5000, 1400, 90)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21B")
    ClearChrFlags(0xB, 0x80)

    label("loc_21B")

    Jump("loc_234")

    label("loc_21E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_234")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)

    label("loc_234")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_240"),
        (SWITCH_DEFAULT, "loc_254"),
    )


    label("loc_240")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_251")
    SetMapFlags(0x10000000)
    Event(0, 7)

    label("loc_251")

    Jump("loc_254")

    label("loc_254")

    Return()

    # Function_0_1F6 end

    def Function_1_255(): pass

    label("Function_1_255")

    OP_16(0x2, 0xFA0, 0xFFFDC5B0, 0xFFFE0C00, 0x23004F)
    OP_1C(0x1, 0x0, 0xC)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_284"),
        (101, "loc_284"),
        (102, "loc_28C"),
        (103, "loc_28C"),
        (SWITCH_DEFAULT, "loc_294"),
    )


    label("loc_284")

    OP_22(0x1CE, 0x1, 0x64)
    Jump("loc_294")

    label("loc_28C")

    OP_22(0x1CA, 0x1, 0x64)
    Jump("loc_294")

    label("loc_294")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A8")
    OP_72(0x2, 0x10)
    OP_65(0x0, 0x1)
    Jump("loc_2BF")

    label("loc_2A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_END)), "loc_2BF")
    OP_72(0x2, 0x10)
    OP_6F(0x2, 160)
    OP_64(0x0, 0x1)

    label("loc_2BF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D7")
    OP_72(0x1, 0x10)
    OP_6F(0x1, 99)

    label("loc_2D7")

    Return()

    # Function_1_255 end

    def Function_2_2D8(): pass

    label("Function_2_2D8")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FD")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_390")

    label("loc_2FD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_316")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_390")

    label("loc_316")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32F")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_390")

    label("loc_32F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_348")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_390")

    label("loc_348")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_361")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_390")

    label("loc_361")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37A")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_390")

    label("loc_37A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_390")
    OP_99(0xFE, 0x6, 0x7, 0x546)

    label("loc_390")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3A5")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_390")

    label("loc_3A5")

    Return()

    # Function_2_2D8 end

    def Function_3_3A6(): pass

    label("Function_3_3A6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3FC")

    ChrTalk(    #0
        0xFE,
        "今天轮到我放哨。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "……这么说来，到底是谁在下面\x01",
            "办理通行手续呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45D")

    label("loc_3FC")

    OP_A2(0x2)

    ChrTalk(    #2
        0xFE,
        (
            "尼克斯那家伙不能值勤，\x01",
            "换我代替他放哨了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "呼，虽然不大明白…\x01",
            "但这也是任务，没办法。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45D")

    TalkEnd(0xFE)
    Return()

    # Function_3_3A6 end

    def Function_4_461(): pass

    label("Function_4_461")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_51C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C9")

    ChrTalk(    #4
        0xFE,
        (
            "虽然扛着枪，\x01",
            "但现在不能放子弹……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "想到就觉得不安，\x01",
            "还是尽量不去想了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_519")

    label("loc_4C9")


    ChrTalk(    #6
        0xFE,
        (
            "虽然扛着枪，\x01",
            "但现在不能放子弹……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "只靠枪和剑作战\x01",
            "的演习都好久没做了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_519")

    Jump("loc_784")

    label("loc_51C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_5FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A4")

    ChrTalk(    #8
        0xFE,
        (
            "协会的游击士\x01",
            "偶尔会来巡逻。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "好像在各地巡视，\x01",
            "真是辛苦啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "与我们巡逻的范围相比\x01",
            "那可不是一个等级的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_5FA")

    label("loc_5A4")


    ChrTalk(    #11
        0xFE,
        (
            "这种时候我也明白\x01",
            "巡视是很重要的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "对方如此拼命\x01",
            "自然这边也要精神振作起来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5FA")

    Jump("loc_784")

    label("loc_5FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_693")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_64A")

    ChrTalk(    #13
        0xFE,
        (
            "最近危险的魔兽\x01",
            "也增加了不少。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "不过，好好\x01",
            "休息吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_690")

    label("loc_64A")

    OP_A2(0x1)

    ChrTalk(    #15
        0xFE,
        "哎呀，辛苦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "竟然来到这种地方，\x01",
            "是来消灭通缉魔兽的吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_690")

    Jump("loc_784")

    label("loc_693")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_710")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_6CB")

    ChrTalk(    #17
        0xFE,
        (
            "尼克斯那家伙好像\x01",
            "真的看到了什么。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70D")

    label("loc_6CB")

    OP_A2(0x1)

    ChrTalk(    #18
        0xFE,
        (
            "尼克斯那家伙好像\x01",
            "真的看到了什么。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        "……还好我没看到。\x02",
    )

    CloseMessageWindow()

    label("loc_70D")

    Jump("loc_784")

    label("loc_710")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_784")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_745")

    ChrTalk(    #20
        0xFE,
        (
            "近来游客也少,\x01",
            "真是令人犯困啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_784")

    label("loc_745")

    OP_A2(0x1)

    ChrTalk(    #21
        0xFE,
        "呀，终于有人来了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "近来游客也少,\x01",
            "真是令人犯困啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_784")

    TalkEnd(0xFE)
    Return()

    # Function_4_461 end

    def Function_5_788(): pass

    label("Function_5_788")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_854")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_821")

    ChrTalk(    #23
        0xFE,
        (
            "刚、刚才真令人难以置信，\x01",
            "有人进了隧道。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "好像有急事\x01",
            "要返回蔡斯……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "那、那小哥真勇敢啊。\x01",
            "我要是女人真要喜欢上他了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_84E")

    label("loc_821")


    ChrTalk(    #26
        0xFE,
        (
            "刚、刚才真令人难以置信，\x01",
            "有人进了隧道。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_84E")

    TalkEnd(0xFE)
    Jump("loc_CF0")

    label("loc_854")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_8BE")
    TalkBegin(0xFE)

    ChrTalk(    #27
        0xFE,
        (
            "不妙啊……\x01",
            "隧道一片漆黑的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "好像随时会有魔兽跑出来似的。\x01",
            "说、说实话，有点害怕。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_CF0")

    label("loc_8BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 3)), scpexpr(EXPR_END)), "loc_C61")
    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_9AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_933")

    ChrTalk(    #29
        0xFE,
        (
            "配合条约签字仪式\x01",
            "警备好像也强化了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "我明白是重要的仪式，\x01",
            "不过跟我们没啥关系啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9AA")

    label("loc_933")


    ChrTalk(    #31
        0xFE,
        (
            "配合互不侵犯条约的签字仪式\x01",
            "关所的警备好像都强化了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "要是王都周边倒还好说，\x01",
            "不过我觉得这里好像没啥关系吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_9AA")

    Jump("loc_C5B")

    label("loc_9AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_A3E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_9FD")

    ChrTalk(    #33
        0xFE,
        "那两个人相当着急呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "呼，游击士\x01",
            "好像都很忙，真够呛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A3B")

    label("loc_9FD")


    ChrTalk(    #35
        0xFE,
        (
            "之前像是游击士\x01",
            "的两个人来过呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        "在隧道没碰到吗？\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_A3B")

    Jump("loc_C5B")

    label("loc_A3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_AE5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_A99")

    ChrTalk(    #37
        0xFE,
        (
            "卡鲁迪亚丘陵周边\x01",
            "地盘好像也还稳定。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "因此地震什么的\x01",
            "几乎没印象。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AE2")

    label("loc_A99")


    ChrTalk(    #39
        0xFE,
        (
            "好像在蔡斯地区\x01",
            "发生地震了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "利贝尔的地震\x01",
            "好像很少见不是吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_AE2")

    Jump("loc_C5B")

    label("loc_AE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_B5A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_B1D")

    ChrTalk(    #41
        0xFE,
        (
            "哈，难得来一趟。\x01",
            "稍微休息一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B57")

    label("loc_B1D")


    ChrTalk(    #42
        0xFE,
        "呀，是你们啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "竟然要过隧道\x01",
            "又是什么工作吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_B57")

    Jump("loc_C5B")

    label("loc_B5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_BFE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_BAA")

    ChrTalk(    #44
        0xFE,
        (
            "不知道会不会再出现，\x01",
            "每晚都战战兢兢的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        "赶快解决吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_BFB")

    label("loc_BAA")

    OP_A2(0x0)

    ChrTalk(    #46
        0xFE,
        (
            "哟，辛苦了。\x01",
            "之后的调查怎样了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "不早点解决的话，\x01",
            "永远都不能安心啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BFB")

    Jump("loc_C5B")

    label("loc_BFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 2)), scpexpr(EXPR_END)), "loc_C5B")

    ChrTalk(    #48
        0xFE,
        (
            "事到如今就算知道不是梦\x01",
            "也够惹人生气了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "唉，看到那个以后\x01",
            "真是完全没好事啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C5B")

    TalkEnd(0x8)
    Jump("loc_CF0")

    label("loc_C61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 2)), scpexpr(EXPR_END)), "loc_C6F")
    Call(0, 8)
    Jump("loc_CF0")

    label("loc_C6F")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_CA5")

    ChrTalk(    #50
        0xFE,
        (
            "隧道又暗又长呢。\x01",
            "近来通过的人也少。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CED")

    label("loc_CA5")

    OP_A2(0x0)

    ChrTalk(    #51
        0xFE,
        "这里是卡鲁迪亚隧道的入口。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "没有通行准许证\x01",
            "可不能再向前啦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CED")

    TalkEnd(0x8)

    label("loc_CF0")

    Return()

    # Function_5_788 end

    def Function_6_CF1(): pass

    label("Function_6_CF1")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D7F")

    ChrTalk(    #53
        0xFE,
        "啊，辛苦了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "我是卢安支部所属\x01",
            "梅尔茨准游击士！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "现在正在到处\x01",
            "巡视中！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "虽然真是够累的，\x01",
            "但这工作正适合我！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_DD9")

    label("loc_D7F")


    ChrTalk(    #57
        0xFE,
        (
            "现在正在\x01",
            "步行警戒中！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "虽然真是够累的，\x01",
            "但说到体力的话，我可是不会输给任何人的！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DD9")

    TalkEnd(0xB)
    Return()

    # Function_6_CF1 end

    def Function_7_DDD(): pass

    label("Function_7_DDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DEE")
    Call(0, 9)

    label("loc_DEE")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_4A(0x8, 255)
    OP_6D(5900, 12000, 13400, 0)
    OP_6C(85000, 0)
    OP_6B(8000, 0)
    StopSound(0x7D00, 0x3D090, 0x0)
    SetChrPos(0x101, -52500, 0, -1800, 90)
    SetChrPos(0xF7, -52500, 0, -600, 90)
    OP_C8(0x200, 0x46, "C_PLAC05._CH", 0x0, 0x7D0)
    FadeToBright(2000, 0)
    StopSound(0x7D00, 0x1FBD0, 0x2EE0)

    def lambda_E7C():
        OP_6B(2800, 11000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_E7C)

    def lambda_E8C():
        OP_6C(45000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E8C)
    Sleep(3000)

    def lambda_EA1():
        OP_6D(-50000, 0, -1500, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_EA1)
    Sleep(8500)

    ChrTalk(    #59
        0x101,
        (
            "#1011F#6P艾尔·雷登关所……\x01",
            "感觉好久没来了呢。\x02\x03",

            "#1016F这里有看到那个\x01",
            "的士兵吧？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1058")

    ChrTalk(    #60
        0x106,
        (
            "#051F#5P啊啊，嘉恩是这么说的。\x02\x03",

            "首先去找关所的队长\x01",
            "问问看是谁吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x101,
        (
            "#1015F#6P嗯，明白了。\x02\x03",

            "#1007F哎～话说回来。\x02\x03",

            "这么漂亮的地方\x01",
            "竟然会有那个出现……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x101, 400)
    Sleep(500)

    ChrTalk(    #62
        0x106,
        (
            "#552F#5P什么白影啊，那个什么的啊，\x01",
            "真是不死心。\x02\x03",

            "坦率地承认是幽灵不就好了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(    #63
        0x101,
        (
            "#1014F#6P啊～别管我啦！\x02\x03",

            "我在努力想办法\x01",
            "让自己不去在意啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1188")

    label("loc_1058")


    ChrTalk(    #64
        0x103,
        (
            "#020F#5P嘉恩是这么说的。\x02\x03",

            "首先去找关所的队长\x01",
            "问问看是谁吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x101,
        (
            "#1015F#6P嗯，明白了。\x02\x03",

            "#1007F哎～话说回来。\x02\x03",

            "这么漂亮的地方\x01",
            "竟然会有那个出现……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)
    Sleep(500)

    ChrTalk(    #66
        0x103,
        (
            "#027F#5P艾丝蒂尔……\x01",
            "不能自欺欺人哦。\x02\x03",

            "什么白影啊那个的\x01",
            "就承认是幽灵吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #67
        0x101,
        (
            "#1014F#6P我听不见，我听不见！\x02\x03",

            "我绝对\x01",
            "不承认那个！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1188")

    OP_A2(0x1211)
    OP_4B(0x8, 255)
    EventEnd(0x0)
    Return()

    # Function_7_DDD end

    def Function_8_1192(): pass

    label("Function_8_1192")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11AC")
    Call(0, 9)
    FadeToBright(0, 0)

    label("loc_11AC")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_4A(0x8, 255)
    Fade(1000)
    SetChrPos(0x101, 16230, 5000, 1730, 90)
    SetChrPos(0xF7, 16120, 5000, 530, 45)
    OP_6B(2800, 0)
    OP_4F(0x65, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x66, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x67, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()

    ChrTalk(    #68
        0x8,
        "哦，想进隧道吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x8,
        (
            "稍等一下。\x01",
            "我现在就开门。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x101,
        (
            "#1016F#6P啊，不是。\x01",
            "不是想通过。\x02\x03",

            "#1000F我们\x01",
            "是游击士协会的人。\x02\x03",

            "正在调查\x01",
            "『白影』的事。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #71
        0x8,
        "那难道是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x8,
        (
            "但、但是那个\x01",
            "不只是我睡着了后做梦而已吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x101,
        (
            "#1002F#6P嗯，不是的。\x02\x03",

            "其实，除了你以外\x01",
            "在卢安各地都有\x01",
            "目击了白影的人哦。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_13BC")

    ChrTalk(    #74
        0x106,
        (
            "#051F你和这里的队长\x01",
            "好像都不知道这事啊。\x02\x03",

            "这可恶的白影可是惹了不少麻烦啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1400")

    label("loc_13BC")


    ChrTalk(    #75
        0x103,
        (
            "#020F你和队长\x01",
            "好像都不知道这事啊。\x02\x03",

            "据说白影搞出了不少乱子呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1400")


    ChrTalk(    #76
        0x8,
        "是，是这样吗?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x8,
        (
            "是吗～我放心了。\x01",
            "作为梦来说也太真实了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #78
        0x8,
        (
            "……唔。\x01",
            "知道不是梦\x01",
            "突然害怕起来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x101,
        (
            "#1007F#6P……我明白你的心情。\x02\x03",

            "#1008F嗯，这个暂且不管,\x01",
            "那时的事情能告诉我们吗？\x02\x03",

            "尽量详细具体一点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x8,
        "啊啊，明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x8,
        (
            "……３天前的半夜，\x01",
            "我在放哨，和平常一样\x01",
            "站在这里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x8,
        "这里瀑布的声音很大吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x8,
        (
            "但是我习惯了这个节奏\x01",
            "反而犯起困来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x8,
        (
            "刚刚吃了饭\x01",
            "就换岗了,\x01",
            "更加想睡了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x8,
        (
            "因此，为了赶走睡意\x01",
            "就在这上面走来走去\x01",
            "做步哨。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x8,
        (
            "那时……\x01",
            "我就看到了那个。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x101,
        (
            "#1002F#6P是、是吗……\x02\x03",

            "那个\x01",
            "是怎样的那个？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x8,
        (
            "白色的，轻飘飘的\x01",
            "穿着古老的衣服。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x8,
        (
            "还在瀑布正上方\x01",
            "滴溜溜地跳着舞。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x8,
        (
            "我打起了寒颤\x01",
            "忍不住架起枪……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #91
        0x101,
        (
            "#1004F#6P咦咦！？\x02\x03",

            "幽灵……\x01",
            "难道你向它开枪了吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x8,
        (
            "啊、啊啊……\x01",
            "本想威吓射击的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x8,
        (
            "但是好像没打中,\x01",
            "还是在那里漂浮着……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x8,
        "然后突然飞向北方去了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x101,
        "#1013F#6P啊…啊……?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_17A4")

    ChrTalk(    #96
        0x106,
        (
            "#552F哼……\x01",
            "搞得像真的一样。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17D0")

    label("loc_17A4")


    ChrTalk(    #97
        0x103,
        (
            "#025F哎呀呀……\x01",
            "这搞不好真的是幽灵呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17D0")


    ChrTalk(    #98
        0x8,
        (
            "然后，慌慌张张跑回里面\x01",
            "把队长他们叫起来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x8,
        (
            "『放哨时睡大觉是怎么回事！』\x01",
            "『而且还乱开枪吗！』\x01",
            "这样被狠训了一顿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x8,
        "唉……真是狼狈啊。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #101
        0x101,
        (
            "#1025F#6P真，真可怜啊。\x02\x03",

            "#1016F不过当成是梦\x01",
            "忘掉是最好的了，嗯嗯。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x8,
        (
            "就算这么说\x01",
            "也忘不掉啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x8,
        (
            "……虽然不知道它\x01",
            "为什么要出来晃悠，\x01",
            "不过赶快想想办法啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x8,
        (
            "要是游击士，心灵的烦恼\x01",
            "也能解决吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x101,
        (
            "#1007F#6P少、少来啦。\x01",
            "我们又不是神父。\x02\x03",

            "#1015F不过确实……\x01",
            "应该有什么出现的理由吧。\x02\x03",

            "想办法努力调查看看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x8,
        "啊啊，拜托了。\x02",
    )

    CloseMessageWindow()
    OP_4B(0x8, 255)
    OP_A2(0x1213)
    OP_28(0x82, 0x2, 0x4)
    OP_28(0x82, 0x1, 0x8)
    EventEnd(0x0)
    Return()

    # Function_8_1192 end

    def Function_9_19E6(): pass

    label("Function_9_19E6")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇选择雪拉扎德为队友】\x01",      # 0
            "【◇选择阿加特为队友】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1A60"),
        (1, "loc_1A66"),
        (SWITCH_DEFAULT, "loc_1A6C"),
    )


    label("loc_1A60")

    OP_A2(0x1200)
    Jump("loc_1A6C")

    label("loc_1A66")

    OP_A2(0x1201)
    Jump("loc_1A6C")

    label("loc_1A6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_1A7A")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_1A7E")

    label("loc_1A7A")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_1A7E")

    Return()

    # Function_9_19E6 end

    def Function_10_1A7F(): pass

    label("Function_10_1A7F")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #107
        "\x07\x05门紧紧地关着。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_10_1A7F end

    def Function_11_1AC9(): pass

    label("Function_11_1AC9")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #108
        (
            "\x07\x05西　卢安市　１７５塞尔矩\x01",
            "东　蔡斯市　４４８塞尔矩\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_11_1AC9 end

    def Function_12_1B2D(): pass

    label("Function_12_1B2D")

    TalkBegin(0xFF)
    Sleep(200)
    TalkEnd(0xFF)
    Return()

    # Function_12_1B2D end

    def Function_13_1B39(): pass

    label("Function_13_1B39")

    EventBegin(0x1)

    ChrTalk(    #109
        0x101,
        "#1001F这里好像可以钓上什么来。\x02",
    )

    CloseMessageWindow()

    def lambda_1B65():
        OP_6D(3950, 5000, 6930, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1B65)

    def lambda_1B7D():
        OP_6B(3250, 1500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1B7D)

    def lambda_1B8D():
        OP_6C(60000, 1500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_1B8D)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #110
        "\x07\x05钓鱼吗？\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "钓鱼\x01",      # 0
            "离开\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    WaitChrThread(0x0, 0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CE1")
    OP_C0(0xE, 0x1A, 0xCE4, 0x1838, 0xD3E, 0x0, 0xC8A, 0xFFFFFC18, 0x1A72)
    Fade(500)
    ClearChrFlags(0x1, 0x8)
    ClearChrFlags(0x2, 0x8)
    ClearChrFlags(0x3, 0x8)
    ClearChrFlags(0x4, 0x8)
    ClearChrFlags(0x5, 0x8)
    ClearChrFlags(0x6, 0x8)
    ClearChrFlags(0x7, 0x8)
    SetChrChipByIndex(0x0, 65535)
    ClearChrFlags(0x0, 0x2)
    ClearChrFlags(0x0, 0x40)
    ClearChrFlags(0x0, 0x4)
    SetChrPos(0x0, 4210, 5000, 2040, 0)
    SetChrPos(0x1, 4210, 5000, 2040, 0)
    SetChrPos(0x2, 4210, 5000, 2040, 0)
    SetChrPos(0x3, 4210, 5000, 2040, 0)
    SetChrPos(0x4, 4210, 5000, 2040, 0)
    SetChrPos(0x5, 4210, 5000, 2040, 0)
    SetChrPos(0x6, 4210, 5000, 2040, 0)
    SetChrPos(0x7, 4210, 5000, 2040, 0)
    OP_69(0x0, 0x0)
    OP_30(0x0)
    OP_0D()
    EventEnd(0x1)
    Jump("loc_1CF0")

    label("loc_1CE1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CF0")
    EventEnd(0x1)

    label("loc_1CF0")

    Return()

    # Function_13_1B39 end

    SaveToFile()

Try(main)
