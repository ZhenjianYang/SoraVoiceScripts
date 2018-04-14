from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1120   ._SN',
        MapName             = 'Bose',
        Location            = 'T1120.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60011",
        Flags               = 0,
        EntryFunctionIndex  = 12,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T1120   ._SN',
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
        '赛恩',                                 # 9
        '科梅尔斯',                             # 10
        '卡莉娅',                               # 11
        '斯丁克',                               # 12
        '阿尔丹',                               # 13
        '库瓦诺老人',                           # 14
        '罗亚',                                 # 15
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
        'ED6_DT07/CH01020 ._CH',             # 00
        'ED6_DT07/CH01040 ._CH',             # 01
        'ED6_DT07/CH01550 ._CH',             # 02
        'ED6_DT27/CH03790 ._CH',             # 03
        'ED6_DT07/CH01000 ._CH',             # 04
        'ED6_DT07/CH01120 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT07/CH01020P._CP',             # 00
        'ED6_DT07/CH01040P._CP',             # 01
        'ED6_DT07/CH01550P._CP',             # 02
        'ED6_DT27/CH03790P._CP',             # 03
        'ED6_DT07/CH01000P._CP',             # 04
        'ED6_DT07/CH01120P._CP',             # 05
    )

    DeclNpc(
        X                   = 500,
        Z                   = 0,
        Y                   = 7400,
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
        X                   = -24500,
        Z                   = 0,
        Y                   = 4690,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -28800,
        Z                   = 0,
        Y                   = 24200,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -2460,
        Z                   = 0,
        Y                   = 2950,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -26270,
        Z                   = 0,
        Y                   = 2690,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -22750,
        Z                   = 0,
        Y                   = 4660,
        Direction           = 266,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -28810,
        Z                   = 0,
        Y                   = 1020,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )


    DeclActor(
        TriggerX            = -24000,
        TriggerZ            = 0,
        TriggerY            = 3580,
        TriggerRange        = 700,
        ActorX              = -24500,
        ActorZ              = 1500,
        ActorY              = 4690,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 920,
        TriggerZ            = 0,
        TriggerY            = 6280,
        TriggerRange        = 700,
        ActorX              = 500,
        ActorZ              = 1500,
        ActorY              = 7400,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_202",          # 00, 0
        "Function_1_265",          # 01, 1
        "Function_2_266",          # 02, 2
        "Function_3_3E3",          # 03, 3
        "Function_4_3E8",          # 04, 4
        "Function_5_B7A",          # 05, 5
        "Function_6_B7F",          # 06, 6
        "Function_7_1AB3",         # 07, 7
        "Function_8_2174",         # 08, 8
        "Function_9_275F",         # 09, 9
        "Function_10_28C3",        # 0A, 10
        "Function_11_29DB",        # 0B, 11
        "Function_12_2A96",        # 0C, 12
        "Function_13_2BBA",        # 0D, 13
        "Function_14_2C30",        # 0E, 14
    )


    def Function_0_202(): pass

    label("Function_0_202")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_235")
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_223")
    ClearChrFlags(0xE, 0x80)
    Jump("loc_232")

    label("loc_223")

    SetChrFlags(0x9, 0x10)
    ClearChrFlags(0xD, 0x10)
    ClearChrFlags(0xC, 0x10)

    label("loc_232")

    Jump("loc_246")

    label("loc_235")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_246")
    SetChrFlags(0xA, 0x10)

    label("loc_246")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_264")
    ClearChrFlags(0xB, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_264")
    SetChrFlags(0xB, 0x10)

    label("loc_264")

    Return()

    # Function_0_202 end

    def Function_1_265(): pass

    label("Function_1_265")

    Return()

    # Function_1_265 end

    def Function_2_266(): pass

    label("Function_2_266")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28B")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_3CD")

    label("loc_28B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A4")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_3CD")

    label("loc_2A4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BD")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_3CD")

    label("loc_2BD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D6")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_3CD")

    label("loc_2D6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EF")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_3CD")

    label("loc_2EF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_308")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_3CD")

    label("loc_308")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_321")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_3CD")

    label("loc_321")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33A")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_3CD")

    label("loc_33A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_353")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_3CD")

    label("loc_353")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36C")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_3CD")

    label("loc_36C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_385")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_3CD")

    label("loc_385")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39E")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_3CD")

    label("loc_39E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B7")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_3CD")

    label("loc_3B7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CD")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_3CD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3E2")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_3CD")

    label("loc_3E2")

    Return()

    # Function_2_266 end

    def Function_3_3E3(): pass

    label("Function_3_3E3")

    Call(0, 4)
    Return()

    # Function_3_3E3 end

    def Function_4_3E8(): pass

    label("Function_4_3E8")

    TalkBegin(0x8)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",        # 0
            "买东西\x01",      # 1
            "离开\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45A")
    OP_0D()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_44F")
    OP_A9(0x53)
    Jump("loc_451")

    label("loc_44F")

    OP_A9(0x33)

    label("loc_451")

    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_45A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_46B")
    TalkEnd(0x8)
    Return()

    label("loc_46B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_552")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F7")

    ChrTalk(    #0
        0x8,
        (
            "真头痛。\x01",
            "几乎都没什么客人来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "人气很旺的护身用导力枪\x01",
            "很多人都用不了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        (
            "一般人对剑和棍\x01",
            "根本就不会有兴趣。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_54F")

    label("loc_4F7")


    ChrTalk(    #3
        0x8,
        (
            "平时的话普通的客人\x01",
            "可是会陆续上门的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "主力商品导力枪\x01",
            "无法使用影响果然巨大。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54F")

    Jump("loc_B76")

    label("loc_552")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_5FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CF")

    ChrTalk(    #5
        0x8,
        (
            "虽然隔壁忙得一塌糊涂，\x01",
            "但正如你所见，我这里生意很差。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "非导力兵器也大量到货了，\x01",
            "请慢慢挑选吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_5FA")

    label("loc_5CF")


    ChrTalk(    #7
        0x8,
        (
            "如你所见我们这里很空闲。\x01",
            "慢慢挑选喔。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5FA")

    Jump("loc_B76")

    label("loc_5FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_6BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_658")

    ChrTalk(    #8
        0x8,
        (
            "龙的事件解决了，\x01",
            "真的是只差一步了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        (
            "这样一来\x01",
            "终于可以当商人了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6BB")

    label("loc_658")


    ChrTalk(    #10
        0x8,
        "欢迎光临。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        (
            "龙的事件解决了，\x01",
            "真的是只差一步了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        (
            "呵呵，这样一来\x01",
            "终于可以当商人了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_6BB")

    Jump("loc_B76")

    label("loc_6BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_964")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x348, 7)), scpexpr(EXPR_END)), "loc_7D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_77B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_71B")

    ChrTalk(    #13
        0x8,
        (
            "王国军的作战\x01",
            "不知道怎么样了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        "怎么几乎没有音讯了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_778")

    label("loc_71B")


    ChrTalk(    #15
        0x8,
        (
            "说来王国军的作战\x01",
            "不知道怎么样了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        (
            "好像连飞行舰队也投入了，\x01",
            "怎么几乎没有音讯了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_778")

    Jump("loc_7D1")

    label("loc_77B")

    TurnDirection(0x8, 0x106, 0)

    ChrTalk(    #17
        0x8,
        "但是不知道要消灭什么……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        (
            "这剑制造得相当坚固。\x01",
            "别担心，尽管放手用吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D1")

    Jump("loc_961")

    label("loc_7D4")

    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x8, 0x106, 0)
    Sleep(400)

    ChrTalk(    #19
        0x8,
        (
            "嘿，是你啊。\x01",
            "剑的情况怎么样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x106,
        (
            "#050F目前没什么问题。\x02\x03",

            "部件的结合部位也\x01",
            "也非常地密实。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        (
            "这样啊。\x01",
            "那真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        (
            "毕竟是把造的很结实的剑啊。\x01",
            "尽情挥舞吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x106,
        (
            "#050F是，不用说\x01",
            "我也会马上这么做。\x02\x03",

            "#552F即使只能用２，３下，\x01",
            "那也就够了……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x8)

    ChrTalk(    #24
        0x8,
        "嗯，虽然不是很清楚……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x8,
        (
            "总之有什么事就来吧。\x01",
            "调整什么的我都会帮你做。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A47)
    OP_A2(0x1)

    label("loc_961")

    Jump("loc_B76")

    label("loc_964")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_A61")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_9CD")

    ChrTalk(    #26
        0x8,
        (
            "超市的商人们\x01",
            "好像改到餐厅和酒店做生意了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x8,
        (
            "因此市民的生活\x01",
            "暂时没有太大的混乱。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A5E")

    label("loc_9CD")


    ChrTalk(    #28
        0x8,
        (
            "超市的商人们\x01",
            "好像改到餐厅和酒店做生意了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x8,
        (
            "听说梅贝尔市长请求\x01",
            "各店铺协力，\x01",
            "真是佩服市长她的果断啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x8,
        (
            "因此市民的生活\x01",
            "也有所好转。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_A5E")

    Jump("loc_B76")

    label("loc_A61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_B34")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_ABB")

    ChrTalk(    #31
        0x8,
        "超市没问题吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x8,
        (
            "那里假如不能营业的话，\x01",
            "市民的生活会非常混乱的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B31")

    label("loc_ABB")


    ChrTalk(    #33
        0x8,
        (
            "感觉好像\x01",
            "出大事了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x8,
        (
            "虽然有人受伤，但\x01",
            "超市没问题吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x8,
        (
            "那里假如不能营业的话，\x01",
            "市民的生活会非常混乱的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_B31")

    Jump("loc_B76")

    label("loc_B34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_B76")

    ChrTalk(    #36
        0x8,
        "噢，欢迎光临。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x8,
        (
            "新进了一批好东西噢。\x01",
            "好好看看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B76")

    TalkEnd(0x8)
    Return()

    # Function_4_3E8 end

    def Function_5_B7A(): pass

    label("Function_5_B7A")

    Call(0, 6)
    Return()

    # Function_5_B7A end

    def Function_6_B7F(): pass

    label("Function_6_B7F")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BD4")
    Call(6, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BC0")
    OP_0D()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BB5")
    OP_A9(0x52)
    Jump("loc_BB7")

    label("loc_BB5")

    OP_A9(0x32)

    label("loc_BB7")

    OP_56(0x0)
    TalkEnd(0x9)
    Return()

    label("loc_BC0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BD1")
    TalkEnd(0x9)
    Return()

    label("loc_BD1")

    Jump("loc_1505")

    label("loc_BD4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1505")
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -23800, 0, 2400, 0)
    SetChrPos(0x102, -24600, 0, 2200, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C3B")
    SetChrPos(0xF9, -24200, 0, 1200, 0)
    SetChrPos(0xF8, -25100, 0, 1000, 0)
    Jump("loc_C5D")

    label("loc_C3B")

    SetChrPos(0xF8, -24200, 0, 1200, 0)
    SetChrPos(0xF9, -25100, 0, 1000, 0)

    label("loc_C5D")

    OP_8C(0x9, 180, 0)
    OP_6D(-24840, 0, 3030, 0)
    OP_0D()
    Sleep(400)

    ChrTalk(    #38
        0x9,
        "啊，欢迎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x9,
        (
            "让你们大老远跑来真的很抱歉，\x01",
            "不过工房暂时无法使用。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x9,
        (
            "工作中用到的器材\x01",
            "全部无法使用……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D50")

    ChrTalk(    #41
        0x101,
        (
            "#1018F#4P啊，那个不用担心。\x02\x03",

            "我们带了好东西来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x9,
        "好东西……吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_119F")

    label("loc_D50")


    ChrTalk(    #43
        0x101,
        (
            "#1026F#4P啊，是吗……\x02\x03",

            "#1015F嗯……不过真伤脑筋啊。\x02\x03",

            "结晶回路的合成和结晶孔的强化\x01",
            "都完全不能进行……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DFF")

    ChrTalk(    #44
        0x103,
        (
            "#025F嗯嗯，难得有了这的发生器，\x01",
            "真是太可惜了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E9A")

    label("loc_DFF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E42")

    ChrTalk(    #45
        0x108,
        (
            "#072F唔，难得有了这的发生器，\x01",
            "真是太可惜了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E9A")

    label("loc_E42")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E9A")

    ChrTalk(    #46
        0x106,
        (
            "#552F啊啊，难得有了这的发生器，\x01",
            "恢复导力魔法了呢。\x02\x03",

            "这真是太可惜了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E9A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EEF")

    ChrTalk(    #47
        0x107,
        (
            "#064F啊，不过姐姐……\x02\x03",

            "如果只是一小会儿，\x01",
            "那我或许有点办法喔。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F3C")

    label("loc_EEF")


    ChrTalk(    #48
        0x102,
        (
            "#1043F的确是这样……\x02\x03",

            "#1040F不过，如果只是一小会儿\x01",
            "那我或许有点办法喔。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F3C")

    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FB9")

    def lambda_F6C():
        TurnDirection(0x0, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_F6C)
    Sleep(120)

    def lambda_F7F():
        TurnDirection(0x1, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_F7F)

    def lambda_F8D():
        TurnDirection(0x2, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_F8D)
    Sleep(120)

    def lambda_FA0():
        TurnDirection(0x3, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_FA0)

    def lambda_FAE():
        TurnDirection(0x9, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_FAE)
    Jump("loc_FC0")

    label("loc_FB9")

    TurnDirection(0x101, 0x102, 400)

    label("loc_FC0")

    WaitChrThread(0x0, 0x1)
    WaitChrThread(0x1, 0x1)
    WaitChrThread(0x2, 0x1)
    WaitChrThread(0x3, 0x1)

    ChrTalk(    #49
        0x101,
        "#1004F#4P啊……！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_101D")

    ChrTalk(    #50
        0x106,
        "#052F能让工房运作起来吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1078")

    label("loc_101D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_104B")

    ChrTalk(    #51
        0x103,
        "#023F能让工房运作起来？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1078")

    label("loc_104B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1078")

    ChrTalk(    #52
        0x108,
        "#073F能让工房运作起来吗？\x02",
    )

    CloseMessageWindow()

    label("loc_1078")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10BC")

    ChrTalk(    #53
        0x107,
        (
            "#060F是，是，大概……\x02\x03",

            "使用那个发生器的话……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1102")

    label("loc_10BC")


    ChrTalk(    #54
        0x102,
        (
            "#1040F#1P是，我想……\x02\x03",

            "如果使用那个发生器\x01",
            "应该能在短时间内复原。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1102")


    ChrTalk(    #55
        0x101,
        "#1018F#4P啊，原来如此！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x9,
        "那、那个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x9,
        "到底在说些什么呢？\x02",
    )

    CloseMessageWindow()

    def lambda_114F():
        TurnDirection(0x0, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_114F)
    Sleep(120)

    def lambda_1162():
        TurnDirection(0x1, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1162)

    def lambda_1170():
        TurnDirection(0x2, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1170)
    Sleep(120)

    def lambda_1183():
        TurnDirection(0x3, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1183)
    WaitChrThread(0x0, 0x1)
    WaitChrThread(0x1, 0x1)
    WaitChrThread(0x2, 0x1)
    WaitChrThread(0x3, 0x1)

    label("loc_119F")


    ChrTalk(    #58
        0x102,
        "#1040F#1P那个，是这样的……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #59
        (
            "\x07\x05说明了使用『零力场发生器』\x01",
            "可暂时恢复工房机能的事。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TurnDirection(0x9, 0x102, 400)

    ChrTalk(    #60
        0x9,
        "啊～～～很厉害的装置啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x9,
        (
            "嗯，全拜托你了。\x01",
            "快点来试试吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        "#1006F#4P嗯，那我们就开始吧。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12B1")

    ChrTalk(    #63
        0x107,
        (
            "#560F那么～\x01",
            "请稍等。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12E1")

    label("loc_12B1")


    ChrTalk(    #64
        0x102,
        (
            "#1040F#1P那么，稍等片刻。\x01",
            "借用一下机械了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12E1")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_22(0x9D, 0x0, 0x64)
    OP_8C(0x9, 270, 0)
    SetChrName("")

    AnonymousTalk(    #65
        "\x07\x05使用『零力场发生器』将工房机能恢复了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #66
        0x9,
        "噢，机械确实动起来了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_137D")
    TurnDirection(0x9, 0x0, 400)
    Jump("loc_146D")

    label("loc_137D")


    ChrTalk(    #67
        0x101,
        "#1000F#4P太好了……看来是成功了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13FC")

    ChrTalk(    #68
        0x107,
        (
            "#063F嗯，不过这\x01",
            "只是暂时能动……\x02\x03",

            "#561F马上又会回到不动的状态的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_144A")

    label("loc_13FC")


    ChrTalk(    #69
        0x102,
        (
            "#1040F#1P嗯，确实很顺利……\x02\x03",

            "但并不是真的修好了。\x01",
            "过一段时间又会停止的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_144A")

    TurnDirection(0x9, 0x0, 400)

    ChrTalk(    #70
        0x9,
        "这样的话必须要赶紧了。\x02",
    )

    CloseMessageWindow()

    label("loc_146D")


    ChrTalk(    #71
        0x9,
        (
            "来，要调整导力器的话\x01",
            "就趁现在。\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    FadeToBright(300, 0)
    OP_0D()
    OP_A9(0x52)
    OP_56(0x0)
    OP_0D()
    Sleep(30)

    ChrTalk(    #72
        0x9,
        (
            "今后要使用工房时\x01",
            "也请把那个装置带来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x9,
        (
            "这样的话就能\x01",
            "一直的使用工房了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)
    OP_A2(0x20E2)
    EventEnd(0x0)
    TalkEnd(0x9)
    Return()

    label("loc_1505")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_15B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_158D")

    ChrTalk(    #74
        0x9,
        (
            "修理什么的\x01",
            "本来就是不可能的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x9,
        (
            "因为各位的导力器\x01",
            "并没有发生故障。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x9,
        (
            "唉哟哟……\x01",
            "这样说明到底是第几次了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_15AE")

    label("loc_158D")


    ChrTalk(    #77
        0x9,
        (
            "都说了……\x01",
            "并不是出故障了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15AE")

    Jump("loc_1AAF")

    label("loc_15B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1681")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1636")

    ChrTalk(    #78
        0x9,
        (
            "从早上开始就不断\x01",
            "有要求修理的顾客前来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x9,
        (
            "就算说明了\x01",
            "不是出故障了也不肯回去……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x9,
        "啊～谁来救救我。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_167E")

    label("loc_1636")


    ChrTalk(    #81
        0x9,
        (
            "要求修理的\x01",
            "客人可真多啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x9,
        (
            "不管怎么说\x01",
            "都会有人源源不断的赶来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_167E")

    Jump("loc_1AAF")

    label("loc_1681")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_177D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_16EC")

    ChrTalk(    #83
        0x9,
        (
            "超市的硬件设施\x01",
            "已经完全恢复到原来的模样了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x9,
        (
            "没有超市的话\x01",
            "果然没有柏斯的感觉呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_177A")

    label("loc_16EC")


    ChrTalk(    #85
        0x9,
        "呀，欢迎。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x9,
        (
            "来看超市的吗？\x01",
            "已经完全恢复了原貌哟。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x9,
        (
            "那里果然是\x01",
            "柏斯市的象征啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x9,
        (
            "超市一开门，\x01",
            "好像整个城市就又恢复了活力。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_177A")

    Jump("loc_1AAF")

    label("loc_177D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_18D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_17EA")

    ChrTalk(    #89
        0x9,
        (
            "感觉在超市做事\x01",
            "是最快乐的事了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x9,
        (
            "将来若是有一天能再次\x01",
            "怀着那样的心情做生意就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18CF")

    label("loc_17EA")


    ChrTalk(    #91
        0x9,
        (
            "为了超市的修复\x01",
            "稍微出了一点力。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x9,
        (
            "我也以那里\x01",
            "作为人生的起点的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x9,
        (
            "现在回想起来\x01",
            "那个超市时代\x01",
            "才是最开心的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x9,
        (
            "和尼冈德那家伙一起\x01",
            "为了追求梦想已经尽了全力了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x9,
        (
            "哈哈，要是时光可以倒流的话，\x01",
            "真想回到那个时代啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_18CF")

    Jump("loc_1AAF")

    label("loc_18D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_1933")

    ChrTalk(    #96
        0x9,
        (
            "古代龙什么的，\x01",
            "真的活着啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x9,
        (
            "以前在酒馆里\x01",
            "听说过这些事，\x01",
            "当时完全不当一回事。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AAF")

    label("loc_1933")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_19A1")

    ChrTalk(    #98
        0x9,
        (
            "北街区的超市似乎\x01",
            "好像出什么事了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x9,
        (
            "大家正在议论，\x01",
            "巨大的怪物什么的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x9,
        "到底出什么事啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AAF")

    label("loc_19A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_1AAF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1A02")

    ChrTalk(    #101
        0x9,
        (
            "霸占我店铺的那个\x01",
            "尼冈德还在服刑。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x9,
        (
            "倒是和他通过信，\x01",
            "监狱生活相当苦啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AAF")

    label("loc_1A02")


    ChrTalk(    #103
        0x9,
        (
            "以前，霸占我店铺的那个\x01",
            "叫尼冈德的家伙还在服刑。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x9,
        (
            "倒是和他通过信，\x01",
            "监狱生活相当苦啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x9,
        (
            "我当上店主之后，\x01",
            "商店的经营变得有条不紊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x9,
        (
            "所以请务必\x01",
            "放心购物吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1AAF")

    TalkEnd(0x9)
    Return()

    # Function_6_B7F end

    def Function_7_1AB3(): pass

    label("Function_7_1AB3")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_1BAD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B59")

    ChrTalk(    #107
        0xFE,
        "客人们好像还在坚持啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        (
            "导力器不是外行能搞懂的。\x01",
            "说明不被理解是自然的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        (
            "但是，做出说明是店主的责任。\x01",
            "虽然有点同情，但没有办法。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_1BAA")

    label("loc_1B59")


    ChrTalk(    #110
        0xFE,
        "客人们好像还在坚持啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        (
            "导力器不是外行能搞懂的。\x01",
            "说明不被理解是自然的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BAA")

    Jump("loc_2170")

    label("loc_1BAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1CA7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C67")

    ChrTalk(    #112
        0xFE,
        (
            "是什么原因让客人们一大早\x01",
            "就气冲冲的冲进来呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        "但是，接待客人是店主的职责。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "自己的工作\x01",
            "只能自己承担。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "包括导力器无法工作在内，\x01",
            "要做的事有一大堆。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_1CA4")

    label("loc_1C67")


    ChrTalk(    #116
        0xFE,
        "接待客人是店主的职责。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "自己的工作，\x01",
            "只能自己承担。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CA4")

    Jump("loc_2170")

    label("loc_1CA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_1DE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1D1A")

    ChrTalk(    #118
        0xFE,
        (
            "市长官邸好像收到了\x01",
            "一块极品金耀石结晶。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "好像是某人赠送的，\x01",
            "世上竟然有出手这么阔绰的人。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DDD")

    label("loc_1D1A")


    ChrTalk(    #120
        0xFE,
        (
            "市长官邸好像收到了\x01",
            "一块特大号的金耀石。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        (
            "好像是某人赠送的，\x01",
            "世上竟然有出手这么阔绰的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "但是，如此巨大的结晶\x01",
            "是无法在城里的工房进行换钱的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "恐怕会被转交王城，\x01",
            "收归国库吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1DDD")

    Jump("loc_2170")

    label("loc_1DE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_1EC8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1E45")

    ChrTalk(    #124
        0xFE,
        (
            "买家虽然曾经表示要来验货，\x01",
            "但是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        (
            "由于定期船停运，\x01",
            "验货事宜延期的下周。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EC5")

    label("loc_1E45")


    ChrTalk(    #126
        0xFE,
        (
            "买家虽然曾经表示要来验货，\x01",
            "但是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        (
            "由于定期船停运，\x01",
            "验货事宜延期的下周。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "嗯，请务必为我们的商品\x01",
            "做一个评价。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1EC5")

    Jump("loc_2170")

    label("loc_1EC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_1FD7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1F2B")

    ChrTalk(    #129
        0xFE,
        (
            "嗯，若是有机会的话\x01",
            "真想亲眼看一看龙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        (
            "会成为导力器工艺品的\x01",
            "良好动机吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FD4")

    label("loc_1F2B")


    ChrTalk(    #131
        0xFE,
        (
            "前几天的骚乱……\x01",
            "是龙引起的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "传说中从『大崩坏』时代\x01",
            "就存在的神兽吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        (
            "嗯，若是有机会的话\x01",
            "真想亲眼看一次啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        (
            "会成为导力器工艺品的\x01",
            "良好动机吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1FD4")

    Jump("loc_2170")

    label("loc_1FD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_203A")

    ChrTalk(    #135
        0xFE,
        "外面好像很吵……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        "但不要分心，专心做好自己的工作。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        "…………………………\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_2170")

    label("loc_203A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_2170")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_20AF")

    ChrTalk(    #138
        0xFE,
        (
            "现在的店主科梅尔斯\x01",
            "是这间工房的创业者。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        (
            "之前的店主被逮捕了。\x01",
            "然后他就回来重新主持大局了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2170")

    label("loc_20AF")


    ChrTalk(    #140
        0xFE,
        (
            "现在的店主科梅尔斯\x01",
            "是这间工房的创业者。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        (
            "虽然临时请了别人担当店主，\x01",
            "但被王国军逮捕了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        (
            "于是创业者科梅尔斯才\x01",
            "重新担当起店主。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        (
            "详细的事情虽然不太清楚，\x01",
            "真是个复杂的故事啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_2170")

    TalkEnd(0xA)
    Return()

    # Function_7_1AB3 end

    def Function_8_2174(): pass

    label("Function_8_2174")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 7)), scpexpr(EXPR_END)), "loc_2181")
    OP_A2(0x4)

    label("loc_2181")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21FD")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇在前篇遇到过斯丁克】\x01",        # 0
            "【◇在前篇没遇到过斯丁克】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_21F1"),
        (1, "loc_21F7"),
        (SWITCH_DEFAULT, "loc_21FD"),
    )


    label("loc_21F1")

    OP_A2(0x4)
    Jump("loc_21FD")

    label("loc_21F7")

    OP_A3(0x4)
    Jump("loc_21FD")

    label("loc_21FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_275B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34A, 3)), scpexpr(EXPR_END)), "loc_22DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_229D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2258")

    ChrTalk(    #144
        0xFE,
        (
            "琐碎的事\x01",
            "就由我来做吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        "……龙的事情就拜托了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_229A")

    label("loc_2258")


    ChrTalk(    #146
        0xFE,
        (
            "前些天在超市\x01",
            "协助我们救助的人是你吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        "……非常感谢。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_229A")

    Jump("loc_22D8")

    label("loc_229D")


    ChrTalk(    #148
        0xFE,
        (
            "琐碎的事\x01",
            "就由我来做吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        "……龙的事情就拜托了。\x02",
    )

    CloseMessageWindow()

    label("loc_22D8")

    Jump("loc_275B")

    label("loc_22DB")


    ChrTalk(    #150
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_24CC")

    ChrTalk(    #151
        0x101,
        (
            "#1011F啊，你是……\x02\x03",

            "斯丁克……对吧？\x01",
            "柏斯支部的游击士。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #152
        0xFE,
        (
            "你是……\x01",
            "那时的准游击士吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        "哦，看样子已经升任正游击士了啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x101,
        "#1016F嗯，是啊。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_246C")

    ChrTalk(    #155
        0x103,
        "#027F好久不见了，斯丁克。\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0xFE)
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #156
        0xFE,
        "雪拉扎德吗…\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        (
            "前些天在超市\x01",
            "协助我们救助的人是你吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xFE,
        "……非常感谢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x103,
        "#026F哪里，那是应该做的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_24C9")

    label("loc_246C")


    ChrTalk(    #160
        0xFE,
        (
            "前些天在超市\x01",
            "协助我们救助的人是你吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        "……非常感谢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x101,
        "#1002F嗯，那是应该的啊。\x02",
    )

    CloseMessageWindow()

    label("loc_24C9")

    Jump("loc_271A")

    label("loc_24CC")


    ChrTalk(    #163
        0x101,
        (
            "#1015F（啊？这个人……）\x02\x03",

            "（仔细看看的话，\x01",
            "　竟然也戴着游击士的徽章啊？）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25E1")

    ChrTalk(    #164
        0x103,
        "#027F好久不见了，斯丁克。\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0xFE)
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #165
        0xFE,
        "雪拉扎德吗…\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xFE,
        (
            "前些天在超市\x01",
            "协助我们救助的人是你吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xFE,
        "……非常感谢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x103,
        "#026F哪里，那是应该做的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_271A")

    label("loc_25E1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2617")

    ChrTalk(    #169
        0x108,
        "#070F（嗯，看来他也是游击士。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_264C")

    label("loc_2617")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_264C")

    ChrTalk(    #170
        0x104,
        "#030F（嗯，看来也是个游击士啊。）\x02",
    )

    CloseMessageWindow()

    label("loc_264C")

    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #171
        0xFE,
        "你是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xFE,
        (
            "卢格兰老爷子提到的那个\x01",
            "新人正游击士吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x101,
        (
            "#1011F啊，嗯。\x01",
            "大概是我吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xFE,
        "是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xFE,
        (
            "前些天在超市\x01",
            "协助我们救助的人是你吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xFE,
        "……非常感谢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x101,
        "#1002F嗯，那是应该的啊。\x02",
    )

    CloseMessageWindow()

    label("loc_271A")


    ChrTalk(    #178
        0xFE,
        (
            "琐碎的事\x01",
            "就由我来做吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xFE,
        "……龙的事情就拜托了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1A53)
    OP_A2(0x5)

    label("loc_275B")

    TalkEnd(0xB)
    Return()

    # Function_8_2174 end

    def Function_9_275F(): pass

    label("Function_9_275F")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_2823")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27EB")

    ChrTalk(    #180
        0xFE,
        "嗯，唉……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0xFE,
        (
            "紧追不舍的我们也\x01",
            "渐渐感到疲劳了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0xFE,
        (
            "从一大早开始\x01",
            "就一直是这样呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xFE,
        "所以实在是累死了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_2820")

    label("loc_27EB")


    ChrTalk(    #184
        0xFE,
        "嗯，唉……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xFE,
        (
            "我们好像也开始\x01",
            "渐渐感到疲劳了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2820")

    Jump("loc_28BF")

    label("loc_2823")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_28BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2882")

    ChrTalk(    #186
        0xFE,
        (
            "修，修不了……\x01",
            "这到底什么意思？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0xFE,
        (
            "难道就那么想\x01",
            "让我们买新的吗！？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_28BF")

    label("loc_2882")


    ChrTalk(    #188
        0xFE,
        "喂，店主！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xFE,
        (
            "除非把相机修好，\x01",
            "否则我们是不会走的！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28BF")

    TalkEnd(0xC)
    Return()

    # Function_9_275F end

    def Function_10_28C3(): pass

    label("Function_10_28C3")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_2934")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2921")

    ChrTalk(    #190
        0xFE,
        (
            "你们的解释\x01",
            "我不管听几次都听不懂。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xFE,
        (
            "唉～唉……\x01",
            "真是太糟糕了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_2931")

    label("loc_2921")


    ChrTalk(    #192
        0xFE,
        "唉～唉……\x02",
    )

    CloseMessageWindow()

    label("loc_2931")

    Jump("loc_29D7")

    label("loc_2934")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_29D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_298D")

    ChrTalk(    #193
        0xFE,
        (
            "辩解我们听够了，\x01",
            "快点给我们修好！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xFE,
        (
            "去钓鱼\x01",
            "这是我计划好的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_29D7")

    label("loc_298D")


    ChrTalk(    #195
        0xFE,
        (
            "辩解我听够了，\x01",
            "快点给我修好！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0xFE,
        (
            "你们跟我家那老太婆\x01",
            "串通一气了吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29D7")

    TalkEnd(0xD)
    Return()

    # Function_10_28C3 end

    def Function_11_29DB(): pass

    label("Function_11_29DB")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A48")

    ChrTalk(    #197
        0xFE,
        (
            "柜台那两个人……\x01",
            "真是剑拔弩张啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0xFE,
        (
            "这里的店主\x01",
            "也真可怜。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xFE,
        "这可真是如坐针毡啊。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_2A92")

    label("loc_2A48")


    ChrTalk(    #200
        0xFE,
        (
            "其实我也是\x01",
            "来请求修理的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xFE,
        (
            "但是还不至于\x01",
            "会像那个人那样不顾一切。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A92")

    TalkEnd(0xE)
    Return()

    # Function_11_29DB end

    def Function_12_2A96(): pass

    label("Function_12_2A96")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x13), scpexpr(EXPR_PUSH_LONG, 0x381), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2AA3")
    Return()

    label("loc_2AA3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2AB5")
    Return()

    label("loc_2AB5")

    SetMapFlags(0x80)
    OP_C0(0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(30)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0x9)"), scpexpr(EXPR_END)), "loc_2AF0")
    Call(0, 13)
    Jump("loc_2BB3")

    label("loc_2AF0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0x8)"), scpexpr(EXPR_END)), "loc_2AFF")
    Call(0, 14)
    Jump("loc_2BB3")

    label("loc_2AFF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0x3E8)"), scpexpr(EXPR_END)), "loc_2B0E")
    Call(0, 13)
    Jump("loc_2BB3")

    label("loc_2B0E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0x3E9)"), scpexpr(EXPR_END)), "loc_2B1D")
    Call(0, 14)
    Jump("loc_2BB3")

    label("loc_2B1D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0xFF)"), scpexpr(EXPR_END)), "loc_2B75")
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #202
        (
            "\x07\x05试着出示了照片，\x01",
            "但似乎没有见过的印象。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jump("loc_2BB3")

    label("loc_2B75")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #203
        "\x07\x05附近没有人可以确认照片。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_2BB3")

    OP_0D()
    ClearMapFlags(0x80)
    Return()

    # Function_12_2A96 end

    def Function_13_2BBA(): pass

    label("Function_13_2BBA")

    TalkBegin(0x9)

    ChrTalk(    #204
        0x9,
        (
            "真可怜，\x01",
            "10年前走失的孩子吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x9,
        (
            "我们的客人里\x01",
            "没有像这个孩子的人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x9,
        (
            "很遗憾，\x01",
            "去别的地方看看吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x9)
    Return()

    # Function_13_2BBA end

    def Function_14_2C30(): pass

    label("Function_14_2C30")

    TalkBegin(0x8)

    ChrTalk(    #207
        0x8,
        "嗯……不记得见过。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x8,
        (
            "女性客人很少，\x01",
            "假如来过的话应该会有印象。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x8,
        (
            "就算是１０年前的照片，\x01",
            "气质上还是有所相似的吧？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)
    Return()

    # Function_14_2C30 end

    SaveToFile()

Try(main)
