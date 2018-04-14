from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1230   ._SN',
        MapName             = 'Bose',
        Location            = 'T1230.x',
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
        '@FileName',                            # 8
        '阿波尔',                               # 9
        '莉莫奈',                               # 10
        '鲁伊',                                 # 11
        '弗兰',                                 # 12
        '贝斯卡',                               # 13
        '菲戈',                                 # 14
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
        'ED6_DT07/CH01050 ._CH',             # 00
        'ED6_DT07/CH01150 ._CH',             # 01
        'ED6_DT07/CH01470 ._CH',             # 02
        'ED6_DT07/CH01070 ._CH',             # 03
        'ED6_DT07/CH01143 ._CH',             # 04
        'ED6_DT07/CH01020 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT07/CH01050P._CP',             # 00
        'ED6_DT07/CH01150P._CP',             # 01
        'ED6_DT07/CH01470P._CP',             # 02
        'ED6_DT07/CH01070P._CP',             # 03
        'ED6_DT07/CH01143P._CP',             # 04
        'ED6_DT07/CH01020P._CP',             # 05
    )

    DeclNpc(
        X                   = -730,
        Z                   = 0,
        Y                   = 5300,
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
        X                   = 440,
        Z                   = 0,
        Y                   = 32439,
        Direction           = 270,
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
        X                   = -3550,
        Z                   = 0,
        Y                   = 32400,
        Direction           = 180,
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
        X                   = -3550,
        Z                   = 0,
        Y                   = 31160,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -940,
        Z                   = 300,
        Y                   = 34630,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x1D4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -750,
        Z                   = 0,
        Y                   = 35490,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )


    DeclActor(
        TriggerX            = -780,
        TriggerZ            = 0,
        TriggerY            = 4190,
        TriggerRange        = 400,
        ActorX              = -700,
        ActorZ              = 1500,
        ActorY              = 5300,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -1500,
        TriggerZ            = 0,
        TriggerY            = 31600,
        TriggerRange        = 400,
        ActorX              = 440,
        ActorZ              = 1500,
        ActorY              = 32439,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1E2",          # 00, 0
        "Function_1_20D",          # 01, 1
        "Function_2_277",          # 02, 2
        "Function_3_3F4",          # 03, 3
        "Function_4_3F9",          # 04, 4
        "Function_5_A0E",          # 05, 5
        "Function_6_A13",          # 06, 6
        "Function_7_11BE",         # 07, 7
        "Function_8_1679",         # 08, 8
        "Function_9_183C",         # 09, 9
        "Function_10_1A22",        # 0A, 10
    )


    def Function_0_1E2(): pass

    label("Function_0_1E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1FB")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    Jump("loc_20C")

    label("loc_1FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_20C")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)

    label("loc_20C")

    Return()

    # Function_0_1E2 end

    def Function_1_20D(): pass

    label("Function_1_20D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_220")
    OP_B1("T1230_n")
    Jump("loc_23C")

    label("loc_220")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 2)), scpexpr(EXPR_END)), "loc_233")
    OP_B1("T1230_y")
    Jump("loc_23C")

    label("loc_233")

    OP_B1("T1230_n")

    label("loc_23C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24D")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_24D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_263")
    OP_10(0x0, 0x0)
    OP_10(0x5, 0x0)
    OP_10(0x8, 0x1)
    OP_10(0x9, 0x1)
    Jump("loc_276")

    label("loc_263")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_276")
    OP_10(0x0, 0x0)
    OP_10(0x5, 0x0)
    OP_10(0x6, 0x1)
    OP_10(0x7, 0x1)

    label("loc_276")

    Return()

    # Function_1_20D end

    def Function_2_277(): pass

    label("Function_2_277")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29C")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_3DE")

    label("loc_29C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B5")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_3DE")

    label("loc_2B5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CE")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_3DE")

    label("loc_2CE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E7")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_3DE")

    label("loc_2E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_300")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_3DE")

    label("loc_300")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_319")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_3DE")

    label("loc_319")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_332")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_3DE")

    label("loc_332")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34B")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_3DE")

    label("loc_34B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_364")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_3DE")

    label("loc_364")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37D")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_3DE")

    label("loc_37D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_396")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_3DE")

    label("loc_396")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AF")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_3DE")

    label("loc_3AF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C8")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_3DE")

    label("loc_3C8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DE")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_3DE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3F3")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_3DE")

    label("loc_3F3")

    Return()

    # Function_2_277 end

    def Function_3_3F4(): pass

    label("Function_3_3F4")

    Call(0, 4)
    Return()

    # Function_3_3F4 end

    def Function_4_3F9(): pass

    label("Function_4_3F9")

    TalkBegin(0x8)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",      # 0
            "休息\x01",      # 1
            "离开\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_458")
    OP_0D()
    OP_A9(0x47)
    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_458")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_469")
    TalkEnd(0x8)
    Return()

    label("loc_469")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_54A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FB")

    ChrTalk(    #0
        0x8,
        (
            "仔细想来，最近\x01",
            "好像经常发生奇怪的事件呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "先是出现古龙，\x01",
            "然后又有岛浮在天上……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        (
            "真希望\x01",
            "以后别再发生任何事了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_547")

    label("loc_4FB")


    ChrTalk(    #3
        0x8,
        (
            "我们只想在这村子里\x01",
            "平静地生活下去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "真希望\x01",
            "以后别再发生任何事了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_547")

    Jump("loc_A0A")

    label("loc_54A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_64E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E4")

    ChrTalk(    #5
        0x8,
        "啊，欢迎光临。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "我们村子里的导力器\x01",
            "也全停了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "不过，因为我待在这里\x01",
            "完全没注意到……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "……刚才被莉莫奈\x01",
            "嘲笑了一顿。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_64B")

    label("loc_5E4")


    ChrTalk(    #9
        0x8,
        (
            "我们店里本来\x01",
            "就是用油灯的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "右边的钟\x01",
            "也是发条式的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        (
            "就，就算没注意到\x01",
            "也很正常不是吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_64B")

    Jump("loc_A0A")

    label("loc_64E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_75C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_6BF")

    ChrTalk(    #12
        0x8,
        (
            "果树园的整理也结束了，\x01",
            "总算恢复了平日的生活。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        (
            "期待树苗结出果实，\x01",
            "以后还要更加努力呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_759")

    label("loc_6BF")


    ChrTalk(    #14
        0x8,
        "啊，欢迎光临。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        (
            "果树园的整理也结束了，\x01",
            "总算恢复了平日的生活。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        (
            "总有一天新树苗\x01",
            "会结果的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        (
            "衷心期待那天的到来，\x01",
            "以后还要更加努力呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_759")

    Jump("loc_A0A")

    label("loc_75C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_836")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_7BB")

    ChrTalk(    #18
        0x8,
        (
            "果树园的人们\x01",
            "一直讨论到深夜。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        (
            "虽然知道会很辛苦，\x01",
            "但希望他们加油啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_833")

    label("loc_7BB")


    ChrTalk(    #20
        0x8,
        (
            "果树园的人们\x01",
            "一直讨论到深夜。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        (
            "虽然知道会很辛苦，\x01",
            "但希望他们加油啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        (
            "我们的店\x01",
            "也要靠果树园才能维持啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_833")

    Jump("loc_A0A")

    label("loc_836")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 2)), scpexpr(EXPR_END)), "loc_928")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_89D")

    ChrTalk(    #23
        0x8,
        "呼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        (
            "虽然我安慰莉莫奈\x01",
            "让她打起精神来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x8,
        (
            "但自己却无法轻松\x01",
            "转换心情。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_925")

    label("loc_89D")


    ChrTalk(    #26
        0x8,
        "啊，欢迎光临……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x8,
        (
            "虽然我安慰莉莫奈\x01",
            "让她打起精神来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        (
            "但自己却无法轻松\x01",
            "转换心情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x8,
        (
            "唉，日复一日，\x01",
            "都是叹息不已……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_925")

    Jump("loc_A0A")

    label("loc_928")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_A0A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_991")

    ChrTalk(    #30
        0x8,
        (
            "好不容易结果了，\x01",
            "却全部都被破坏了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x8,
        (
            "该怎么安慰才好呢，\x01",
            "都找不到安慰的话了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A0A")

    label("loc_991")


    ChrTalk(    #32
        0x8,
        "火好像已经被扑灭了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x8,
        (
            "但是，好不容易结果了，\x01",
            "却全部都被破坏了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x8,
        (
            "变成这样，怎样\x01",
            "安慰果园的人才好呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_A0A")

    TalkEnd(0x8)
    Return()

    # Function_4_3F9 end

    def Function_5_A0E(): pass

    label("Function_5_A0E")

    Call(0, 6)
    Return()

    # Function_5_A0E end

    def Function_6_A13(): pass

    label("Function_6_A13")

    TalkBegin(0x9)
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A74")
    OP_0D()
    OP_A9(0x48)
    OP_56(0x0)
    TalkEnd(0x9)
    Return()

    label("loc_A74")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A85")
    TalkEnd(0x9)
    Return()

    label("loc_A85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_DCA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BD0")
    TurnDirection(0x9, 0x106, 0)

    ChrTalk(    #35
        0x9,
        "哎呀，这不是阿加特吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x9,
        "难道有什么工作？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x106,
        (
            "#050F不，不是工作。\x02\x03",

            "只是来看看\x01",
            "村子的情况。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x9,
        "啊，这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x9,
        (
            "导力器停了，\x01",
            "大家正在发愁呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x9,
        (
            "游击士能来巡视\x01",
            "就让人安心多了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x9,
        (
            "虽然很辛苦，今后\x01",
            "也请常来看看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x106,
        (
            "#051F啊啊，会的。\x02\x03",

            "只要到附近来的话\x01",
            "就一定再来打扰。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2092)
    OP_A2(0x2)
    Jump("loc_DC7")

    label("loc_BD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_C22")

    ChrTalk(    #43
        0x9,
        (
            "游击士能来巡视\x01",
            "就让人安心多了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x9,
        (
            "从今以后也要\x01",
            "也请常来看看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DC7")

    label("loc_C22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_D3A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CE1")

    ChrTalk(    #45
        0x9,
        (
            "孩子们也来帮忙了，\x01",
            "村里的生活还算好……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x9,
        (
            "不过导力器停止的原因\x01",
            "好像还不清楚呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x9,
        (
            "王国军方\x01",
            "要是有正式声明就好了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x9,
        (
            "这里离帝国很近，\x01",
            "说实话真是很不安啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_D37")

    label("loc_CE1")


    ChrTalk(    #49
        0x9,
        (
            "不过导力器停止的原因\x01",
            "好像还不清楚呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x9,
        (
            "这里离帝国很近，\x01",
            "说实话真是很不安啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D37")

    Jump("loc_DC7")

    label("loc_D3A")


    ChrTalk(    #51
        0x9,
        "哎呀，游击士们啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x9,
        (
            "难道\x01",
            "是来巡视的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x9,
        (
            "村子现在还算平静，\x01",
            "不过不知道以后还会发生什么事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x9,
        (
            "从今以后也要\x01",
            "也请常来露个面吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DC7")

    Jump("loc_11BA")

    label("loc_DCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_EA4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_E22")

    ChrTalk(    #55
        0x9,
        (
            "村长先生那里\x01",
            "似乎收到了各处来的捐款。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x9,
        "真是个让人振奋的消息。\x02",
    )

    CloseMessageWindow()
    Jump("loc_EA1")

    label("loc_E22")


    ChrTalk(    #57
        0x9,
        "欢迎光临～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x9,
        (
            "村长先生那里\x01",
            "似乎收到了各处来的捐款。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x9,
        (
            "这样果树园\x01",
            "就能重建了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x9,
        "嗯，真是个让人振奋的消息。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_EA1")

    Jump("loc_11BA")

    label("loc_EA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_1009")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x349, 1)), scpexpr(EXPR_END)), "loc_F05")

    ChrTalk(    #61
        0x9,
        (
            "前阵子还受伤躺着，\x01",
            "这么快就回来工作啦……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x9,
        (
            "游击士\x01",
            "果然是辛苦的工作呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1006")

    label("loc_F05")

    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x9, 0x106, 0)
    Sleep(400)

    ChrTalk(    #63
        0x9,
        "啊，阿加特。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x9,
        "就回来工作了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x106,
        (
            "#050F啊啊，最近\x01",
            "比较忙嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x9,
        (
            "是吗，游击士\x01",
            "果然辛苦啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x9,
        (
            "嗯，工作做完了\x01",
            "再来我们这儿喝酒哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x9,
        (
            "请你喝我们\x01",
            "引以为傲的水果酒。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x106,
        (
            "#053F是吗……\x02\x03",

            "#051F那我就期待了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A49)

    label("loc_1006")

    Jump("loc_11BA")

    label("loc_1009")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 2)), scpexpr(EXPR_END)), "loc_10BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_105C")

    ChrTalk(    #70
        0x9,
        (
            "阿加特好像受伤\x01",
            "被抬回家里了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x9,
        (
            "我稍后\x01",
            "也去看望他一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10B9")

    label("loc_105C")


    ChrTalk(    #72
        0x9,
        (
            "阿加特好像受伤\x01",
            "被抬回家里了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x9,
        (
            "好像有个小女孩\x01",
            "跟在他身边……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x9,
        "……那是谁呢？\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_10B9")

    Jump("loc_11BA")

    label("loc_10BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_11BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_111F")

    ChrTalk(    #75
        0x9,
        (
            "大家努力的结晶\x01",
            "瞬间就被摧毁了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x9,
        (
            "真是太不甘心了，\x01",
            "我连眼泪都流不出来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11BA")

    label("loc_111F")


    ChrTalk(    #77
        0x9,
        (
            "那个果树园是村里人共同\x01",
            "管理的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x9,
        (
            "无论刮风下雨\x01",
            "大家都一起照顾的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x9,
        (
            "竟然瞬间\x01",
            "就被完全摧毁了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x9,
        (
            "真是太不甘心了，\x01",
            "我连眼泪都流不出来了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_11BA")

    TalkEnd(0x9)
    Return()

    # Function_6_A13 end

    def Function_7_11BE(): pass

    label("Function_7_11BE")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x349, 0)), scpexpr(EXPR_END)), "loc_13E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_12BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_122E")

    ChrTalk(    #81
        0xFE,
        (
            "爸爸他们\x01",
            "昨天一直\x01",
            "讨论到深夜呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "果园的事\x01",
            "果然有很多问题要处理啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12BC")

    label("loc_122E")


    ChrTalk(    #83
        0xFE,
        (
            "啊，姐姐\x01",
            "和阿加特哥哥……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        "抓到龙了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x106,
        (
            "#050F不，现在\x01",
            "正要去抓呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x106, 400)

    ChrTalk(    #86
        0xFE,
        "是，是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "加油哦！\x01",
            "我会为你们加油的！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_12BC")

    Jump("loc_13AF")

    label("loc_12BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 2)), scpexpr(EXPR_END)), "loc_1376")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1314")

    ChrTalk(    #88
        0xFE,
        (
            "我听爸爸的话\x01",
            "乖乖待在这里呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "爸爸他们还在\x01",
            "整理果树园呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1373")

    label("loc_1314")


    ChrTalk(    #90
        0xFE,
        "啊，是姐姐你们……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "我听爸爸的话\x01",
            "乖乖待在这里呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "爸爸他们还在\x01",
            "整理果树园呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_1373")

    Jump("loc_13AF")

    label("loc_1376")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_13AF")

    ChrTalk(    #93
        0xFE,
        "姐姐你们也要小心哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        "龙是很大很大的……\x02",
    )

    CloseMessageWindow()

    label("loc_13AF")

    Jump("loc_13E4")

    label("loc_13B2")


    ChrTalk(    #95
        0xFE,
        "姐姐你们也要小心哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        "龙是很大很大的……\x02",
    )

    CloseMessageWindow()

    label("loc_13E4")

    Jump("loc_1675")

    label("loc_13E7")

    OP_62(0xFE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(400)

    ChrTalk(    #97
        0xFE,
        "啊，姐姐……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_1479")
    TurnDirection(0xFE, 0x106, 400)
    Sleep(400)

    ChrTalk(    #98
        0xFE,
        "还有阿加特哥哥！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x101,
        "#1000F嗨～鲁伊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x106,
        (
            "#051F哟，小鬼。\x01",
            "还好吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14AC")

    label("loc_1479")


    ChrTalk(    #101
        0x101,
        (
            "#1000F嗨～鲁伊。\x02\x03",

            "#1007F太好了……\x01",
            "你没事啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14AC")


    ChrTalk(    #102
        0xFE,
        "嗯、嗯，我没事呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        "可是……果园……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x101,
        (
            "#1016F真是的，马上就眼泪汪汪的……\x02\x03",

            "#1006F没关系的，放心吧。\x02\x03",

            "姐姐我们来了\x01",
            "就不会再让龙乱来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        "真，真的……？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_15C4")

    ChrTalk(    #106
        0x101,
        "#1006F真的真的啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x106,
        "#051F啊啊，向你保证。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x101,
        (
            "#1000F所以再忍耐一会儿，\x01",
            "听爸爸的话\x01",
            "乖乖的哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1657")

    label("loc_15C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 2)), scpexpr(EXPR_END)), "loc_1614")

    ChrTalk(    #109
        0x101,
        (
            "#1012F真的真的啦。\x02\x03",

            "#1000F所以在此之前，\x01",
            "要听爸爸的话\x01",
            "乖乖的哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1657")

    label("loc_1614")


    ChrTalk(    #110
        0x101,
        (
            "#1012F真的真的啦。\x02\x03",

            "#1000F所以再忍耐一会儿，\x01",
            "乖乖待在家里哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1657")


    ChrTalk(    #111
        0xFE,
        "嗯、嗯……知道了！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1A48)
    OP_A2(0x3)

    label("loc_1675")

    TalkEnd(0xA)
    Return()

    # Function_7_11BE end

    def Function_8_1679(): pass

    label("Function_8_1679")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_16D2")

    ChrTalk(    #112
        0xFE,
        (
            "贝斯卡和库赖\x01",
            "重归于好了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "两个人都这么大了，\x01",
            "差不多该妥协了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1838")

    label("loc_16D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 2)), scpexpr(EXPR_END)), "loc_1754")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_170B")

    ChrTalk(    #114
        0xFE,
        "还不能出去吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        "唉，好无聊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1751")

    label("loc_170B")


    ChrTalk(    #116
        0xFE,
        "还不能出去啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        "唉，好无聊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "让莉莫奈做点\x01",
            "甜点吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_1751")

    Jump("loc_1838")

    label("loc_1754")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_1838")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_17A1")

    ChrTalk(    #119
        0xFE,
        (
            "龙有那么\x01",
            "恐怖吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "故事里面出现的\x01",
            "好像都很善良……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1838")

    label("loc_17A1")


    ChrTalk(    #121
        0xFE,
        (
            "外面还很危险，\x01",
            "不能出去呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "但是，龙有那么\x01",
            "恐怖吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "故事里面出现的\x01",
            "好像都很善良……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "一定像鲁伊和巴德斯一样，\x01",
            "龙也有不同性格吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_1838")

    TalkEnd(0xB)
    Return()

    # Function_8_1679 end

    def Function_9_183C(): pass

    label("Function_9_183C")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_1937")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18E8")

    ChrTalk(    #125
        0xFE,
        (
            "埃米尔那家伙在发牢骚，\x01",
            "因为流通路线好像停了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        (
            "没有运输手段\x01",
            "我们的水果也不能出货，\x01",
            "日用品也很快就会短缺了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        (
            "这，这好像\x01",
            "不太妙啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_1934")

    label("loc_18E8")


    ChrTalk(    #128
        0xFE,
        (
            "流通路线停了\x01",
            "真的是个很严重的问题啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "好，好像不该\x01",
            "在这里喝酒……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1934")

    Jump("loc_1A1E")

    label("loc_1937")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1A1E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19CF")

    ChrTalk(    #130
        0xFE,
        (
            "树苗也栽种完了，\x01",
            "终于能松一口气。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        (
            "就算导力器停止了，\x01",
            "村子的生活也没太大困难。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "煮饭用火炉就成，\x01",
            "照明用油灯也足够了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_1A1E")

    label("loc_19CF")


    ChrTalk(    #133
        0xFE,
        (
            "就算导力器停止了，\x01",
            "村子的生活也没太大困难。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        "这就是住在乡下的好处啊。\x02",
    )

    CloseMessageWindow()

    label("loc_1A1E")

    TalkEnd(0xC)
    Return()

    # Function_9_183C end

    def Function_10_1A22(): pass

    label("Function_10_1A22")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_1B6D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B04")

    ChrTalk(    #135
        0xFE,
        (
            "定期船停止运航了吗……\x01",
            "柏斯那边好像很严重呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        (
            "不过，定期船不行的话，\x01",
            "也就是说飞行舰队也不能飞吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "对住在王国境内的人来说，\x01",
            "这可是大问题啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        (
            "虽然不好声张，\x01",
            "但真担心帝国的动向呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_1B6A")

    label("loc_1B04")


    ChrTalk(    #139
        0xFE,
        (
            "对住在王国境内的人来说，\x01",
            "飞行舰队的问题可就大了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        (
            "虽然不好声张，\x01",
            "但真担心帝国的动向呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B6A")

    Jump("loc_1CE1")

    label("loc_1B6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1CE1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C9C")

    ChrTalk(    #141
        0xFE,
        (
            "树苗也栽种完了，\x01",
            "这下总算能安下心来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        (
            "松了口气……正想这样呢，\x01",
            "但竟然又发生不得了的大事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        (
            "在超市做买卖的\x01",
            "罗亚一家没问题吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        (
            "记得那家伙和太太\x01",
            "一起开一家五金店呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        (
            "导力器不能动的话，\x01",
            "利贝尔最自豪的飞行舰队也白费了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        (
            "虽然不好声张，\x01",
            "真担心帝国的动向……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_1CE1")

    label("loc_1C9C")


    ChrTalk(    #147
        0xFE,
        "柏斯那边应该很严重吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        (
            "真担心在超市做买卖的\x01",
            "罗亚一家人啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CE1")

    TalkEnd(0xD)
    Return()

    # Function_10_1A22 end

    SaveToFile()

Try(main)
