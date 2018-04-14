from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'T0120   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0120.x',
        MapIndex            = 4,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T0120   ._SN',
            'ED6_DT21/T0120_1 ._SN',
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
        '佛莱迪',                               # 9
        '梅尔达斯',                             # 10
        '埃尔格',                               # 11
        '斯蒂娜',                               # 12
        '提克',                                 # 13
        '莫莉',                                 # 14
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
        'ED6_DT07/CH01040 ._CH',             # 00
        'ED6_DT07/CH01000 ._CH',             # 01
        'ED6_DT07/CH01680 ._CH',             # 02
        'ED6_DT07/CH01690 ._CH',             # 03
        'ED6_DT07/CH01050 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT07/CH01040P._CP',             # 00
        'ED6_DT07/CH01000P._CP',             # 01
        'ED6_DT07/CH01680P._CP',             # 02
        'ED6_DT07/CH01690P._CP',             # 03
        'ED6_DT07/CH01050P._CP',             # 04
    )

    DeclNpc(
        X                   = -38180,
        Z                   = 0,
        Y                   = -497,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -39499,
        Z                   = 0,
        Y                   = 678,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -36678,
        Z                   = 0,
        Y                   = 73751,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -86132,
        Z                   = 0,
        Y                   = 71210,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -45100,
        Z                   = 0,
        Y                   = 1430,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -44360,
        Z                   = 0,
        Y                   = -390,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )


    DeclActor(
        TriggerX            = -38537,
        TriggerZ            = 0,
        TriggerY            = -1845,
        TriggerRange        = 400,
        ActorX              = -38180,
        ActorZ              = 1500,
        ActorY              = -497,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -41599,
        TriggerZ            = 0,
        TriggerY            = 299,
        TriggerRange        = 1000,
        ActorX              = -39499,
        ActorZ              = 1500,
        ActorY              = 678,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -36170,
        TriggerZ            = 0,
        TriggerY            = 71651,
        TriggerRange        = 1000,
        ActorX              = -36678,
        ActorZ              = 1500,
        ActorY              = 73751,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1FE",          # 00, 0
        "Function_1_268",          # 01, 1
        "Function_2_28A",          # 02, 2
        "Function_3_2A2",          # 03, 3
        "Function_4_2A7",          # 04, 4
        "Function_5_2AC",          # 05, 5
        "Function_6_1B21",         # 06, 6
        "Function_7_25E5",         # 07, 7
        "Function_8_43E7",         # 08, 8
        "Function_9_60E5",         # 09, 9
        "Function_10_6172",        # 0A, 10
    )


    def Function_0_1FE(): pass

    label("Function_0_1FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_20D")
    SetChrFlags(0x9, 0x80)
    Jump("loc_241")

    label("loc_20D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_217")
    Jump("loc_241")

    label("loc_217")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_22B")
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    Jump("loc_241")

    label("loc_22B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_23A")
    ClearChrFlags(0xD, 0x80)
    Jump("loc_241")

    label("loc_23A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_241")

    label("loc_241")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_267")
    SetChrFlags(0x8, 0x80)
    OP_64(0x1, 0x1)
    SetChrPos(0x9, -38180, 0, -497, 180)

    label("loc_267")

    Return()

    # Function_0_1FE end

    def Function_1_268(): pass

    label("Function_1_268")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_279")
    OP_71(0x1, 0x4)

    label("loc_279")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_289")
    OP_64(0x1, 0x1)

    label("loc_289")

    Return()

    # Function_1_268 end

    def Function_2_28A(): pass

    label("Function_2_28A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29D")
    Call(0, 6)
    Jump("loc_2A1")

    label("loc_29D")

    Call(0, 5)

    label("loc_2A1")

    Return()

    # Function_2_28A end

    def Function_3_2A2(): pass

    label("Function_3_2A2")

    Call(0, 6)
    Return()

    # Function_3_2A2 end

    def Function_4_2A7(): pass

    label("Function_4_2A7")

    Call(0, 7)
    Return()

    # Function_4_2A7 end

    def Function_5_2AC(): pass

    label("Function_5_2AC")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x311, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x413, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_308")
    Call(6, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F7")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2EE")
    OP_A9(0x7)
    Jump("loc_2F0")

    label("loc_2EE")

    OP_A9(0x0)

    label("loc_2F0")

    TalkEnd(0x8)
    Return()

    label("loc_2F7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_308")
    TalkEnd(0x8)
    Return()

    label("loc_308")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_10FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x413, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F06")
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -38800, 0, -2650, 0)
    SetChrPos(0x102, -38000, 0, -2850, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_372")
    SetChrPos(0xF9, -38400, 0, -3850, 0)
    SetChrPos(0xF8, -37500, 0, -4050, 0)
    Jump("loc_394")

    label("loc_372")

    SetChrPos(0xF8, -38400, 0, -3850, 0)
    SetChrPos(0xF9, -37500, 0, -4050, 0)

    label("loc_394")

    OP_8C(0x8, 180, 0)
    OP_6D(-37570, 0, -1360, 0)
    OP_0D()
    Sleep(400)

    ChrTalk(    #0
        0x8,
        "呀，艾丝蒂尔和约修亚……\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #1
        0x8,
        "……咦，这不是约修亚吗！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x102,
        "#1040F#2P您好，好久不见了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x101,
        "#1001F#3P我把他带来的呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "哎呀～好久不见呢。\x01",
            "还好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        (
            "你们两人在一起，\x01",
            "感觉好久没见过了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        "#1016F#3P啊哈哈，确实……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x102,
        (
            "#1040F#2P佛莱迪先生\x01",
            "一点都没变呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        "嗯，我倒没什么……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        (
            "不巧店里\x01",
            "有点困难呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "艾丝蒂尔你们也很辛苦，\x01",
            "可惜帮不上什么忙……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5A2")

    ChrTalk(    #11
        0x101,
        (
            "#1018F#3P啊，这个请放心。\x02\x03",

            "我们带了好东西来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        "咦？怎么回事？\x02",
    )

    CloseMessageWindow()
    Jump("loc_A15")

    label("loc_5A2")


    ChrTalk(    #13
        0x101,
        (
            "#1007F#3P是，是吗……\x02\x03",

            "维修导力器的\x01",
            "工具也不能动啊。\x02\x03",

            "#1015F嗯……不过真伤脑筋啊。\x02\x03",

            "结晶回路的合成和结晶孔的强化\x01",
            "都完全不能进行……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_670")

    ChrTalk(    #14
        0x103,
        (
            "#025F嗯嗯，难得有了这的发生器，\x01",
            "真是太可惜了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70B")

    label("loc_670")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6B3")

    ChrTalk(    #15
        0x108,
        (
            "#072F唔，难得有了这的发生器，\x01",
            "真是太可惜了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70B")

    label("loc_6B3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_70B")

    ChrTalk(    #16
        0x106,
        (
            "#552F啊啊，难得有了这的发生器，\x01",
            "恢复导力魔法了呢。\x02\x03",

            "这真是太可惜了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_70B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_760")

    ChrTalk(    #17
        0x107,
        (
            "#064F啊，不过姐姐……\x02\x03",

            "如果只是一小会儿，\x01",
            "那我或许有点办法喔。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7AE")

    label("loc_760")


    ChrTalk(    #18
        0x102,
        (
            "#1043F#2P话是没错……\x02\x03",

            "#1040F不过，如果只是一小会儿\x01",
            "那我或许有点办法喔。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7AE")

    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_82B")

    def lambda_7DE():
        TurnDirection(0x0, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_7DE)
    Sleep(120)

    def lambda_7F1():
        TurnDirection(0x1, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_7F1)

    def lambda_7FF():
        TurnDirection(0x2, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_7FF)
    Sleep(120)

    def lambda_812():
        TurnDirection(0x3, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_812)

    def lambda_820():
        TurnDirection(0x8, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_820)
    Jump("loc_832")

    label("loc_82B")

    TurnDirection(0x101, 0x102, 400)

    label("loc_832")

    WaitChrThread(0x0, 0x1)
    WaitChrThread(0x1, 0x1)
    WaitChrThread(0x2, 0x1)
    WaitChrThread(0x3, 0x1)

    ChrTalk(    #19
        0x101,
        "#1004F#3P咦……！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_88F")

    ChrTalk(    #20
        0x106,
        "#052F能让工房运作起来吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_8EA")

    label("loc_88F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8BD")

    ChrTalk(    #21
        0x103,
        "#023F能让工房运作起来？\x02",
    )

    CloseMessageWindow()
    Jump("loc_8EA")

    label("loc_8BD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8EA")

    ChrTalk(    #22
        0x108,
        "#073F能让工房运作起来吗？\x02",
    )

    CloseMessageWindow()

    label("loc_8EA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_92E")

    ChrTalk(    #23
        0x107,
        (
            "#062F是、是啊，大概……\x02\x03",

            "用那个发生器的话……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_976")

    label("loc_92E")


    ChrTalk(    #24
        0x102,
        (
            "#1040F#2P是，可能……\x02\x03",

            "如果使用那个发生器，\x01",
            "应该能在短时间内复原。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_976")


    ChrTalk(    #25
        0x101,
        "#1018F#3P啊，原来如此！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        "那～约修亚……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x8,
        "就是说，什么意思？\x02",
    )

    CloseMessageWindow()

    def lambda_9C5():
        TurnDirection(0x0, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_9C5)
    Sleep(120)

    def lambda_9D8():
        TurnDirection(0x1, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_9D8)

    def lambda_9E6():
        TurnDirection(0x2, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_9E6)
    Sleep(120)

    def lambda_9F9():
        TurnDirection(0x3, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_9F9)
    WaitChrThread(0x0, 0x1)
    WaitChrThread(0x1, 0x1)
    WaitChrThread(0x2, 0x1)
    WaitChrThread(0x3, 0x1)

    label("loc_A15")


    ChrTalk(    #28
        0x102,
        "#1040F#2P嗯，其实……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #29
        (
            "\x07\x05说明了使用『零力场发生器』\x01",
            "可暂时恢复工房机能的事。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #30
        0x8,
        "啊～～～很厉害的装置啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x8,
        (
            "嗯，我没有异议。\x01",
            "马上试试吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x101,
        "#1006F#3P谢谢，佛莱迪先生。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B16")

    ChrTalk(    #33
        0x107,
        (
            "#560F那么～\x01",
            "请稍等。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B42")

    label("loc_B16")


    ChrTalk(    #34
        0x102,
        (
            "#1040F#2P那么，就稍微\x01",
            "借用一下机械了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B42")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_22(0x9D, 0x0, 0x64)
    OP_8C(0x8, 90, 0)
    SetChrName("")

    AnonymousTalk(    #35
        "\x07\x05使用『零力场发生器』将工房机能恢复了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #36
        0x8,
        (
            "真的啊……\x01",
            "机械真的开动了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C09")
    TurnDirection(0x8, 0x0, 400)

    ChrTalk(    #37
        0x8,
        (
            "好，趁着机械开动时\x01",
            "赶快办事吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Jump("loc_D26")

    label("loc_C09")


    ChrTalk(    #38
        0x101,
        "#1000F#3P太好了……看来成功了呢。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C82")

    ChrTalk(    #39
        0x107,
        (
            "#063F嗯，不过这\x01",
            "只是暂时能动……\x02\x03",

            "#561F马上又会恢复原状的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CD4")

    label("loc_C82")


    ChrTalk(    #40
        0x102,
        (
            "#1040F#2P嗯，虽然运作得很好……\x02\x03",

            "但并不是真的修好了。\x01",
            "过一段时间又会停止的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CD4")

    TurnDirection(0x8, 0x0, 400)

    ChrTalk(    #41
        0x8,
        (
            "原来如此，从原理看来\x01",
            "确实是这样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x8,
        (
            "好，趁机械开动时\x01",
            "赶快办事吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_59()

    label("loc_D26")

    FadeToBright(300, 0)
    OP_0D()
    OP_A9(0x7)
    OP_56(0x0)
    OP_0D()
    Sleep(30)

    ChrTalk(    #43
        0x8,
        (
            "想使用工房的时候，\x01",
            "就拿那个装置来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x8,
        (
            "随时乐意\x01",
            "帮你们调整。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DE8")

    ChrTalk(    #45
        0x103,
        (
            "#020F协会也正为查明原因\x01",
            "竭尽全力哦。\x02\x03",

            "虽说可能会花一些时间，\x01",
            "但请努力坚持一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E41")

    label("loc_DE8")


    ChrTalk(    #46
        0x102,
        (
            "#1040F#2P协会也正为查明原因\x01",
            "竭尽全力。\x02\x03",

            "虽说可能会花一些时间，\x01",
            "但请努力坚持一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E41")


    ChrTalk(    #47
        0x8,
        (
            "啊啊，能做的事\x01",
            "我会尽量做的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x8,
        (
            "那，艾丝蒂尔你们\x01",
            "工作也要加油哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x8,
        (
            "这种时候能依靠的\x01",
            "还是只有游击士啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x101,
        "#1006F#3P嗯！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x102,
        (
            "#1040F#2P我们会不负众望，\x01",
            "尽一切努力的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    OP_A2(0x188A)
    OP_A2(0x209A)
    OP_A2(0x20E6)
    EventEnd(0x0)
    Jump("loc_10FC")

    label("loc_F06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_1085")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_F60")

    ChrTalk(    #52
        0x8,
        (
            "想使用工房的时候，\x01",
            "就拿那个装置来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x8,
        (
            "随时乐意\x01",
            "帮你们调整。\x02",
        )
    )

    CloseMessageWindow()
    OP_A3(0x6)
    Jump("loc_1082")

    label("loc_F60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1024")

    ChrTalk(    #54
        0x8,
        (
            "老爸应潘杜爷爷的请求\x01",
            "去观察钟楼的情况了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x8,
        (
            "看他还没回来，\x01",
            "应该还在眺望浮游岛吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x8,
        (
            "好像相当在意那个东西，\x01",
            "还画了草图呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x8,
        (
            "真是的，多大年纪了，\x01",
            "好奇心还跟孩子一样强。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_1082")

    label("loc_1024")


    ChrTalk(    #58
        0x8,
        (
            "老爸应潘杜爷爷的请求\x01",
            "去观察钟楼的情况了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x8,
        (
            "看他还没回来，\x01",
            "应该还在眺望那个浮游岛吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1082")

    Jump("loc_10FC")

    label("loc_1085")


    ChrTalk(    #60
        0x8,
        (
            "想使用工房的时候\x01",
            "就拿那个装置来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x8,
        (
            "随时乐意\x01",
            "帮你们调整。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x8,
        (
            "呼，真希望中央工房\x01",
            "赶快将那个发生器量产化啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10FC")

    Jump("loc_1B1D")

    label("loc_10FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_1362")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34B, 1)), scpexpr(EXPR_END)), "loc_1176")

    ChrTalk(    #63
        0x8,
        (
            "虽说好像发生了不少事件，\x01",
            "但不管怎样雾散天晴就好多了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x8,
        (
            "洛连特也好久没来了，\x01",
            "好好休息一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_135F")

    label("loc_1176")

    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x8, 0x101, 0)
    Sleep(400)

    ChrTalk(    #65
        0x8,
        (
            "呀，艾丝蒂尔和雪拉扎德。\x01",
            "这次真是辛苦了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x8,
        (
            "虽说好像发生了不少事件，\x01",
            "但不管怎样雾散天晴就好多了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x8,
        (
            "去做下一件工作之前\x01",
            "好好休息一下如何？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x101,
        (
            "#1006F啊，嗯！\x01",
            "我们也正是这个打算。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x103,
        (
            "#021F呵呵，是啊……\x02\x03",

            "#027F那么，这就\x01",
            "陪我喝一杯如何？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x8,
        "咳、咳咳……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x103, 400)

    ChrTalk(    #71
        0x8,
        (
            "这、这个任务就交给\x01",
            "亚班特的福克纳了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x8,
        (
            "遗，遗憾的是我\x01",
            "还有工作要做呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x101,
        "#1016F啊、啊哈哈……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #74
        0x8,
        (
            "总、总而言之，暂时\x01",
            "放松一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x8,
        (
            "好久没回\x01",
            "洛连特了嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x188A)
    OP_A2(0x1A59)

    label("loc_135F")

    Jump("loc_1B1D")

    label("loc_1362")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_15A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_13F4")

    ChrTalk(    #76
        0x8,
        (
            "王国军刚刚才到达。\x01",
            "已经开始警备了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x8,
        (
            "没想到为了这样的雾\x01",
            "连王国军都出动了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x8,
        (
            "是不是出了什么事，\x01",
            "刚才还和老爸说起呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15A2")

    label("loc_13F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x311, 2)), scpexpr(EXPR_END)), "loc_1429")

    ChrTalk(    #79
        0x8,
        (
            "王国军刚刚才到达。\x01",
            "就已经开始警备了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1512")

    label("loc_1429")

    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x8, 0x101, 0)
    Sleep(400)

    ChrTalk(    #80
        0x8,
        "呀，艾丝蒂尔和雪拉扎德。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x8,
        (
            "好久不见呢。\x01",
            "完成一项工作了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x101,
        "#1025F啊……嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x103,
        (
            "#020F有点急事呢。\x01",
            "刚刚才回来。\x02\x03",

            "……对了，王国军\x01",
            "好像已经开始城里的警备了嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x8,
        "啊啊，刚刚才到达的。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x188A)

    label("loc_1512")


    ChrTalk(    #85
        0x8,
        (
            "队长是阿斯顿先生，\x01",
            "倒是令人比较安心……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x8,
        (
            "不过严重到要出动军队，\x01",
            "反而就觉得有些不安呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x8,
        (
            "是不是出了什么事，\x01",
            "刚才还和老爸说起呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_15A2")

    Jump("loc_1B1D")

    label("loc_15A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_1789")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1601")

    ChrTalk(    #88
        0x8,
        "今天早上也起了好大的雾哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x8,
        (
            "哎呀哎呀，什么时候\x01",
            "才能重现蓝天呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1786")

    label("loc_1601")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x311, 2)), scpexpr(EXPR_END)), "loc_1634")

    ChrTalk(    #90
        0x8,
        (
            "呀，早上好。\x01",
            "今天的雾还是那么大啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1735")

    label("loc_1634")

    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x8, 0x101, 0)
    Sleep(400)

    ChrTalk(    #91
        0x8,
        "呀，艾丝蒂尔和雪拉扎德。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x8,
        (
            "好久不见呢。\x01",
            "你们看起来很精神，这就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x101,
        "#1006F嗯，佛莱迪先生也是。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x103,
        "#020F呵呵，看起来很精神嘛。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x8,
        (
            "啊啊，托你们的福\x01",
            "工作也很顺利。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x8,
        (
            "话虽如此……\x01",
            "今天早上也起了好大的雾哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x188A)

    label("loc_1735")


    ChrTalk(    #97
        0x8,
        (
            "搞不好这雾\x01",
            "比昨天更浓了不是？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x8,
        (
            "哎呀哎呀，什么时候\x01",
            "才能重现蓝天呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_1786")

    Jump("loc_1B1D")

    label("loc_1789")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_1B1D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x311, 2)), scpexpr(EXPR_END)), "loc_1872")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1817")

    ChrTalk(    #99
        0x8,
        (
            "呀，欢迎。\x01",
            "外边的雾还是那么大啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x8,
        (
            "这么浓的雾，老爸\x01",
            "好像也是头一次见呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x8,
        (
            "工作时在外走动\x01",
            "要特别注意哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_186F")

    label("loc_1817")


    ChrTalk(    #102
        0x8,
        (
            "需要调整导力器的时候\x01",
            "随时来找我就是。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x8,
        (
            "我会用中央工房学来的技术\x01",
            "完美调整好的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_186F")

    Jump("loc_1B1D")

    label("loc_1872")

    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x8, 0x101, 0)
    Sleep(400)

    ChrTalk(    #104
        0x8,
        "呀，艾丝蒂尔和雪拉扎德。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x8,
        (
            "好久不见呢。\x01",
            "你们看起来很精神，这就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x285, 2)), scpexpr(EXPR_END)), "loc_1952")

    ChrTalk(    #106
        0x101,
        (
            "#1006F嗯，佛莱迪先生也是。\x02\x03",

            "蔡斯的研修，\x01",
            "看来圆满结束了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x103,
        (
            "#027F呵呵，很想赶快\x01",
            "展示一下成果吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AC5")

    label("loc_1952")


    ChrTalk(    #108
        0x101,
        "#1000F你好，佛莱迪先生。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x103,
        (
            "#027F你看来也\x01",
            "很精神嘛。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x103, 400)

    ChrTalk(    #110
        0x8,
        (
            "啊啊，去了趟蔡斯，\x01",
            "仔细学习了新型导力器的构造。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x8,
        (
            "所以现在可以好好的\x01",
            "回来努力工作了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x101,
        (
            "#1004F咦，佛莱迪先生\x01",
            "也去了蔡斯！？\x02\x03",

            "#1015F哎呀……刚好错过\x01",
            "没能遇见真是遗憾。\x02\x03",

            "应该去了不少次\x01",
            "中央工房的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x103,
        (
            "#020F不过，对于使用战术导力器\x01",
            "的人来说可帮了大忙了。\x02\x03",

            "马上把研修成果\x01",
            "向我们展示一下好吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AC5")


    ChrTalk(    #114
        0x8,
        (
            "啊啊，当然。\x01",
            "随时来找我就是。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x8,
        (
            "我会用中央工房学来的技术\x01",
            "完美的调整好的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x188A)
    OP_A2(0x5)

    label("loc_1B1D")

    TalkEnd(0x8)
    Return()

    # Function_5_2AC end

    def Function_6_1B21(): pass

    label("Function_6_1B21")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_1D38")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34B, 0)), scpexpr(EXPR_END)), "loc_1BAA")

    ChrTalk(    #116
        0x9,
        (
            "游击士真是忙得\x01",
            "不可开交啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x9,
        (
            "嗯，工作告一段落的时候\x01",
            "再来这里吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x9,
        (
            "到那时，\x01",
            "可要把约修亚那小子也带来哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D35")

    label("loc_1BAA")

    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x9, 0x101, 0)
    Sleep(400)

    ChrTalk(    #119
        0x9,
        (
            "哟，是你们。\x01",
            "这次也真是辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x9,
        "莫非已经有了别的地区工作了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x101,
        (
            "#1015F嗯，有是有啦……\x02\x03",

            "#1006F不过在此之前打算\x01",
            "先做做这边的工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x103,
        (
            "#020F嗯嗯，是啊……\x02\x03",

            "不帮一下支部的忙的话，\x01",
            "恐怕爱娜要恨死我们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x9,
        "工作接连不断，也真是够忙的了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x9,
        (
            "嗯，事情告一段落了\x01",
            "再来这里吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x9,
        (
            "对了对了，到那时\x01",
            "可要把约修亚那小子也带来哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x101,
        "#1006F啊……嗯！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1A58)

    label("loc_1D35")

    Jump("loc_25E1")

    label("loc_1D38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_1EFA")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_END)), "loc_1D9B")

    ChrTalk(    #127
        0x9,
        (
            "不过，没想到\x01",
            "连王国军都出动了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x9,
        (
            "不过是点雾而已，\x01",
            "为什么闹得这么大呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EF7")

    label("loc_1D9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x311, 1)), scpexpr(EXPR_END)), "loc_1DD2")

    ChrTalk(    #129
        0xFE,
        (
            "哟，艾丝蒂尔你们啊。\x01",
            "看起来好像很忙啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E9D")

    label("loc_1DD2")

    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x9, 0x101, 0)
    Sleep(400)

    ChrTalk(    #130
        0x9,
        (
            "哦，艾丝蒂尔……\x01",
            "还有雪拉扎德也一起啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x9,
        (
            "为了这次的雾\x01",
            "你们好像很忙嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x101,
        "#1003F嗯……事情是不少。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x103, 400)

    ChrTalk(    #133
        0x103,
        "#020F您这儿没什么问题吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x9,
        "哦，完全没问题。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1889)

    label("loc_1E9D")


    ChrTalk(    #135
        0x9,
        (
            "不过，没想到\x01",
            "连王国军都出动了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x9,
        (
            "再怎么说\x01",
            "也不过是场雾嘛。\x01",
            "是不是紧张过头了？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_1EF7")

    Jump("loc_25E1")

    label("loc_1EFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_2140")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_END)), "loc_1F56")

    ChrTalk(    #137
        0x9,
        "外边的雾仍旧很大啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x9,
        (
            "我在这里住了这么久，\x01",
            "这种事还是头一回呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_213D")

    label("loc_1F56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x311, 1)), scpexpr(EXPR_END)), "loc_1FB8")

    ChrTalk(    #139
        0x9,
        (
            "哦，是你们啊。\x01",
            "外边的雾仍旧很大呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x9,
        (
            "我在这里住了这么久，\x01",
            "这种事还是头一回呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20F0")

    label("loc_1FB8")

    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x9, 0x101, 0)
    Sleep(400)

    ChrTalk(    #141
        0x9,
        (
            "哦，艾丝蒂尔……\x01",
            "还有雪拉扎德也在一起啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x9,
        "你们终于来了啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x101,
        (
            "#1008F嘿嘿……\x01",
            "抱歉哦，这么晚才来打招呼。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x103,
        "#020F您看来一点也没变呢。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x103, 400)

    ChrTalk(    #145
        0x9,
        (
            "哦，当然啦。\x01",
            "可不会输给年轻人哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x9,
        (
            "话说回来，今早也仍旧\x01",
            "是浓雾弥漫啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x9,
        (
            "我在这儿住了这么久\x01",
            "这种事还是头一回呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1889)

    label("loc_20F0")


    ChrTalk(    #148
        0x9,
        (
            "你们在外走动\x01",
            "也要注意啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x9,
        (
            "这么大的雾，走在街道上\x01",
            "视野也很差吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_213D")

    Jump("loc_25E1")

    label("loc_2140")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_23DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x311, 1)), scpexpr(EXPR_END)), "loc_2238")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21E7")

    ChrTalk(    #150
        0x9,
        (
            "哦，辛苦了。\x01",
            "在这大雾下工作也很辛苦吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x9,
        (
            "新型导力器的事\x01",
            "就交给佛莱迪那家伙吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x9,
        (
            "他可是特地跑去\x01",
            "蔡斯研修过的嘛。\x01",
            "尽量使唤他吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2235")

    label("loc_21E7")


    ChrTalk(    #153
        0x9,
        (
            "去蔡斯研修的\x01",
            "佛莱迪也回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x9,
        (
            "新型导力器的调整\x01",
            "就尽管交给那家伙吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2235")

    Jump("loc_23DA")

    label("loc_2238")

    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x9, 0x101, 0)
    Sleep(400)

    ChrTalk(    #155
        0x9,
        (
            "哦，艾丝蒂尔……\x01",
            "还有雪拉扎德也在一起啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x9,
        "好久不见了嘛。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x101,
        (
            "#1017F嘿嘿……\x01",
            "梅尔达斯先生，看起来不错嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x103,
        "#020F呵呵，一点也没变嘛。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x103, 400)

    ChrTalk(    #159
        0x9,
        (
            "哦，当然啦。\x01",
            "可不会输给年轻人哦。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x205, 6)), scpexpr(EXPR_END)), "loc_236D")

    ChrTalk(    #160
        0x9,
        (
            "佛莱迪那家伙\x01",
            "也从蔡斯回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x9,
        (
            "新型导力器的调整\x01",
            "就通通都交给他吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23D4")

    label("loc_236D")


    ChrTalk(    #162
        0x9,
        (
            "为了新型导力器的研修\x01",
            "去了蔡斯的佛莱迪\x01",
            "也终于回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x9,
        (
            "如果要调整或者开封\x01",
            "就尽管交给那家伙吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23D4")

    OP_A2(0x1889)
    OP_A2(0x4)

    label("loc_23DA")

    Jump("loc_25E1")

    label("loc_23DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_25E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x205, 6)), scpexpr(EXPR_END)), "loc_244B")

    ChrTalk(    #164
        0x9,
        (
            "佛莱迪那家伙\x01",
            "去蔡斯了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x9,
        (
            "具体的不太清楚，\x01",
            "不过他说要去中央工房\x01",
            "研修战术导力器来着。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25E1")

    label("loc_244B")


    ChrTalk(    #166
        0x9,
        "哟，欢迎……\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x9, 0x101, 400)
    Sleep(600)
    OP_63(0x9)

    ChrTalk(    #167
        0x9,
        (
            "艾丝蒂尔……\x01",
            "好久不见了嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x101,
        (
            "#000F嘿嘿……\x01",
            "梅尔达斯先生，看起来不错嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x9,
        (
            "当然了。\x01",
            "可不会输给年轻人哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x9,
        (
            "对了，佛莱迪那家伙\x01",
            "去蔡斯了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x101,
        "#505F蔡斯？为什么……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x9,
        (
            "其实我也不太清楚，\x01",
            "不过他说要去中央工房\x01",
            "研修战术导力器来着。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x101,
        "#501F嗯…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x9,
        (
            "真是的，因此\x01",
            "害我忙得快昏头了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x9,
        (
            "研修什么的管它那么多，\x01",
            "赶快回来才是啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x102E)

    label("loc_25E1")

    TalkEnd(0x9)
    Return()

    # Function_6_1B21 end

    def Function_7_25E5(): pass

    label("Function_7_25E5")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2873")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x205, 7)), scpexpr(EXPR_END)), "loc_2674")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2629")

    ChrTalk(    #176
        0xA,
        "艾丝蒂尔，代我向约修亚问好哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2671")

    label("loc_2629")


    ChrTalk(    #177
        0xA,
        "艾丝蒂尔…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x101,
        "#501F嗯，什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xA,
        "…………不，没什么。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_2671")

    Jump("loc_286F")

    label("loc_2674")


    ChrTalk(    #180
        0xA,
        "艾丝蒂尔…………？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0xA,
        "回来了吗！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x101,
        "#001F叔叔，好久不见。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xA,
        (
            "我听说你们的活跃表现了哦。\x01",
            "当上正游击士了嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0xA,
        (
            "真是的，你们可是\x01",
            "一次又一次的让人吃惊呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xA,
        (
            "卡西乌斯似乎也平安无事，\x01",
            "真是个命大的家伙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xA,
        (
            "……哎呀，说起来，\x01",
            "约修亚怎么了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x101,
        (
            "#000F应该先回家了。\x01",
            "我也打算这就回去呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xA,
        "是……那样吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xA,
        (
            "回来也不打个招呼，\x01",
            "那个家伙还真是薄情啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x101,
        (
            "#505F约修亚没来过\x01",
            "这里吗？\x02\x03",

            "#000F那好，回家后\x01",
            "我会让他来露个脸的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xA,
        "啊、啊啊……拜托你了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x142,
        "#1067F………………………………\x02",
    )

    CloseMessageWindow()
    OP_A2(0x102F)

    label("loc_286F")

    TalkEnd(0xA)
    Return()

    label("loc_2873")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x311, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x413, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_28CC")
    Call(6, 4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28BB")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_28B2")
    OP_A9(0x8)
    Jump("loc_28B4")

    label("loc_28B2")

    OP_A9(0x1)

    label("loc_28B4")

    TalkEnd(0xA)
    Return()

    label("loc_28BB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28CC")
    TalkEnd(0xA)
    Return()

    label("loc_28CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2D26")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x413, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A79")
    TurnDirection(0xA, 0x102, 400)
    Sleep(1000)

    ChrTalk(    #193
        0xA,
        "…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xA,
        (
            "哦，约修亚。\x01",
            "总算回来了吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x102,
        (
            "#1035F埃尔格先生。\x01",
            "我回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0xA,
        (
            "嗯……\x01",
            "现在壮多了喔。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xA,
        (
            "看来好像积累了\x01",
            "不少经验嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x102,
        (
            "#1040F是，是成熟些了……\x02\x03",

            "#1043F不过，同时也\x01",
            "让大家担了不少心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xA,
        (
            "哈哈，男人嘛，\x01",
            "这点事没关系的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0xA,
        (
            "约修亚，你可是\x01",
            "这个城市引以为傲的人哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xA,
        (
            "终于回来了………\x01",
            "暂时休息一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x102,
        (
            "#1040F谢谢……\x02\x03",

            "工作做完了之后，\x01",
            "一定会的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    OP_A2(0x209C)
    Jump("loc_2D23")

    label("loc_2A79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2AD3")

    ChrTalk(    #203
        0xA,
        "碰到斯蒂娜了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0xA,
        (
            "还没有的话，\x01",
            "去见见她吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0xA,
        (
            "她可比我\x01",
            "还担心你哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D23")

    label("loc_2AD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_2C30")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BAC")

    ChrTalk(    #206
        0xA,
        "哦，艾丝蒂尔和约修亚。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0xA,
        (
            "定期船的停运倒是知道，\x01",
            "但竟然连搬运车也不能动了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0xA,
        (
            "也就是说，流通路径\x01",
            "完全停止了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xA,
        (
            "虽说洛连特附近有田地\x01",
            "稍微还好一点……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0xA,
        (
            "那柏斯和王都\x01",
            "今后会怎样呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_2C2D")

    label("loc_2BAC")


    ChrTalk(    #211
        0xA,
        (
            "由于这次的事，流通路径\x01",
            "好像都完全停止了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0xA,
        (
            "虽说洛连特附近有田地\x01",
            "稍微还好一点……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0xA,
        (
            "但柏斯和王都\x01",
            "形势不知道有多严重。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C2D")

    Jump("loc_2D23")

    label("loc_2C30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CD3")

    ChrTalk(    #214
        0xA,
        "哦，是艾丝蒂尔你们啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0xA,
        (
            "不过，难得返乡…\x01",
            "时机可不太好啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0xA,
        (
            "现在市内的导力器\x01",
            "全都不能动了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xA,
        (
            "虽说没有太大的混乱，\x01",
            "但还是有点麻烦呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_2D23")

    label("loc_2CD3")


    ChrTalk(    #218
        0xA,
        (
            "现在市内的导力器\x01",
            "全都不能动了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0xA,
        (
            "到底是什么原因，\x01",
            "问了工房也不清楚呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D23")

    Jump("loc_43E3")

    label("loc_2D26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_316E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34B, 2)), scpexpr(EXPR_END)), "loc_2EF5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E6F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2D9C")

    ChrTalk(    #220
        0xA,
        (
            "这次事件的事\x01",
            "以后有机会再问吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0xA,
        (
            "到那时还有约修亚的事\x01",
            "可都要老实交代清楚哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E6C")

    label("loc_2D9C")


    ChrTalk(    #222
        0xA,
        (
            "这次事件中你看来\x01",
            "也是相当活跃嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0xA,
        (
            "到底怎么解决的，\x01",
            "真是令人感兴趣……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0xA,
        (
            "具体的以后有机会\x01",
            "再说来听听吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0xA,
        (
            "嗯，到那时候可得\x01",
            "把约修亚那小子也带来哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0xA,
        (
            "我有些男人之间的话\x01",
            "想和那家伙谈谈。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_2E6C")

    Jump("loc_2EF2")

    label("loc_2E6F")


    ChrTalk(    #227
        0xA,
        (
            "这次事件的冒险故事\x01",
            "以后有机会再问吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0xA,
        (
            "下次来的时候，可一定\x01",
            "要把约修亚也带来哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0xA,
        (
            "我有些男人之间的话\x01",
            "想和那家伙谈谈。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EF2")

    Jump("loc_316B")

    label("loc_2EF5")

    OP_62(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xA, 0x101, 0)
    Sleep(400)

    ChrTalk(    #230
        0xA,
        (
            "哟，艾丝蒂尔和雪拉扎德。\x01",
            "今天天气真好啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0xA,
        (
            "睡着的人们\x01",
            "似乎也都醒了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0xA,
        (
            "……话说，这还是\x01",
            "你们的功劳吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0x101,
        (
            "#1016F嗯、嗯……\x01",
            "有点微妙啦。\x02\x03",

            "#1015F嗯，\x01",
            "就算是吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0xA,
        (
            "我就知道\x01",
            "你们一定能做到的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0xA,
        (
            "虽说想好好问问\x01",
            "到底是怎么解决的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0xA,
        (
            "不过，你们现在这么忙。\x01",
            "下面还有工作等着吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0xA,
        (
            "虽然可惜，冒险故事的发表\x01",
            "还是等下次机会吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0x101,
        (
            "#1008F啊、啊哈哈……\x02\x03",

            "#1007F（不，不愧是埃尔格先生。\x01",
            "  完全把我看穿了。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0x103,
        (
            "#020F呵呵，说实话真是帮了大忙。\x02\x03",

            "那么，日后有机会再叙……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0xA,
        (
            "啊啊，到那时\x01",
            "无论如何也要和约修亚一起来哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0xA,
        (
            "我也会向女神祈祷的，\x01",
            "希望早日收到那家伙的消息。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x188C)
    OP_A2(0x1A5A)
    OP_A2(0x1)

    label("loc_316B")

    Jump("loc_43E3")

    label("loc_316E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_36EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x311, 5)), scpexpr(EXPR_END)), "loc_338A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3318")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_322E")

    ChrTalk(    #242
        0xA,
        (
            "王国军的部队好像\x01",
            "已经加入城市警备了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0xA,
        (
            "这样的话你们游击士\x01",
            "也能专心地好好调查了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0xA,
        (
            "事情虽然很严重，\x01",
            "不过我还是期待你们的表现。\x01",
            "等你们的好消息了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3315")

    label("loc_322E")

    TurnDirection(0xA, 0x101, 0)

    ChrTalk(    #245
        0xA,
        "哟，艾丝蒂尔你们啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0xA,
        (
            "刚才王国军的士兵\x01",
            "过来打过招呼了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0xA,
        (
            "说是今天开始\x01",
            "加入城中警备来着。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0xA,
        (
            "虽说平时那么严肃，\x01",
            "感觉很难以接近似的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0xA,
        (
            "但这种时候有士兵在\x01",
            "还是能够壮胆啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0xA,
        (
            "哎呀，人真是\x01",
            "势利的生物。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_3315")

    Jump("loc_3387")

    label("loc_3318")


    ChrTalk(    #251
        0xA,
        (
            "事件的调查……\x01",
            "要加油哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0xA,
        (
            "但是，你们\x01",
            "也不能鲁莽行事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0xA,
        (
            "如果游击士都倒下了，\x01",
            "就什么希望也没有了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3387")

    Jump("loc_36EC")

    label("loc_338A")

    OP_62(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xA, 0x101, 0)
    Sleep(400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x311, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_346D")

    ChrTalk(    #254
        0xA,
        "哎呀，是艾丝蒂尔你们啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0xA,
        (
            "哈哈，还在想你们什么时候会来，\x01",
            "昨天就开始做准备了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0x101,
        (
            "#1016F哎呀呀……\x01",
            "看来让您久等了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0xA,
        (
            "还是那么忙的样子嘛。\x01",
            "真是的，一大早就那么辛苦啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x188C)
    Jump("loc_349E")

    label("loc_346D")


    ChrTalk(    #258
        0xA,
        (
            "哟，是艾丝蒂尔你们啊。\x01",
            "早上开始就这么忙啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_349E")


    ChrTalk(    #259
        0xA,
        (
            "鲁克他们的情况似乎\x01",
            "暂且也稳定下来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0xA,
        (
            "虽然希望他们早点醒来，\x01",
            "但为这个干着急也无济于事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0xA,
        (
            "艾丝蒂尔你们\x01",
            "也不能鲁莽行事哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0xA,
        (
            "如果你们都倒下了，\x01",
            "那才是彻底没希望了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0x103,
        (
            "#020F没关系的，别担心。\x02\x03",

            "这孩子也是经验丰富、\x01",
            "独当一面的游击士了嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0x101,
        (
            "#1008F嘿嘿，就算是吧……\x02\x03",

            "#1015F不过，和雪拉姐\x01",
            "还差得远呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0xA,
        (
            "哈哈，还有心给师姐面子，\x01",
            "看来是不要紧了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0xA,
        (
            "那么，调查要努力哦。\x01",
            "期待你们的好消息。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3669")

    ChrTalk(    #267
        0x106,
        "#050F啊啊，交给我们吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_36E6")

    label("loc_3669")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3697")

    ChrTalk(    #268
        0x108,
        "#070F啊啊，尽力而为了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_36E6")

    label("loc_3697")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36C9")

    ChrTalk(    #269
        0x104,
        "#030F呵，尽情期待我的表现。\x02",
    )

    CloseMessageWindow()
    Jump("loc_36E6")

    label("loc_36C9")


    ChrTalk(    #270
        0x103,
        "#525F嗯嗯，交给我们吧。\x02",
    )

    CloseMessageWindow()

    label("loc_36E6")

    OP_A2(0x188D)
    OP_A2(0x1)

    label("loc_36EC")

    Jump("loc_43E3")

    label("loc_36EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_3D00")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x311, 5)), scpexpr(EXPR_END)), "loc_3889")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3817")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_375F")

    ChrTalk(    #271
        0xA,
        (
            "虽然我也觉得那雾不寻常，\x01",
            "但竟然发生这种事件……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0xA,
        (
            "你们也要\x01",
            "十分小心啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3814")

    label("loc_375F")

    TurnDirection(0xA, 0x101, 0)

    ChrTalk(    #273
        0xA,
        "哟，艾丝蒂尔你们啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0xA,
        (
            "虽然我就觉得这雾不寻常，\x01",
            "但竟然还发生了昏睡事件什么的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0xA,
        (
            "唉，到底是事件还是意外\x01",
            "都不知道啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0xA,
        (
            "真是的……\x01",
            "真相真的全在雾中某处吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_3814")

    Jump("loc_3886")

    label("loc_3817")


    ChrTalk(    #277
        0xA,
        (
            "事件的调查……\x01",
            "要加油哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0xA,
        (
            "但是，你们\x01",
            "也不能鲁莽行事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0xA,
        (
            "如果游击士都倒下了，\x01",
            "就什么希望也没有了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3886")

    Jump("loc_3CFD")

    label("loc_3889")


    ChrTalk(    #280
        0x101,
        "#1011F早上好，埃尔格先生。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_38CA")

    ChrTalk(    #281
        0x105,
        "#040F早上好。\x02",
    )

    CloseMessageWindow()

    label("loc_38CA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_38EF")

    ChrTalk(    #282
        0x107,
        "#060F嗯，早上好。\x02",
    )

    CloseMessageWindow()

    label("loc_38EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x311, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39CE")
    OP_62(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xA, 0x101, 400)
    Sleep(400)

    ChrTalk(    #283
        0xA,
        "哟，是艾丝蒂尔你们啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0xA,
        (
            "哈哈，还在想你们什么时候会来，\x01",
            "昨天就开始做准备了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0x101,
        (
            "#1008F啊哈哈……\x01",
            "看来让您久等了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0xA,
        (
            "还是那么忙的样子嘛。\x01",
            "今天也是一早就这么辛苦啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x188C)
    Jump("loc_3A11")

    label("loc_39CE")

    TurnDirection(0xA, 0x101, 0)

    ChrTalk(    #287
        0xA,
        "哟，是艾丝蒂尔你们啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0xA,
        "今天也是一早就这么辛苦啊。\x02",
    )

    CloseMessageWindow()

    label("loc_3A11")


    ChrTalk(    #289
        0x103,
        (
            "#025F嗯嗯，真的是……\x01",
            "还想多睡会儿呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0x101,
        (
            "#1015F（不，不过，熬夜\x01",
            "  会这样也是当然的啦……）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x103, 400)

    ChrTalk(    #291
        0xA,
        (
            "这时候，身为游击士前辈\x01",
            "一定要好好撑下去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0xA,
        (
            "鲁克他们的情况似乎\x01",
            "暂且也稳定下来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0xA,
        (
            "虽然希望他们早点醒来，\x01",
            "但为这个干着急也无济于事。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(    #294
        0xA,
        (
            "艾丝蒂尔你们\x01",
            "也不能鲁莽行事哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0xA,
        (
            "如果你们都倒下了\x01",
            "那才是彻底没希望了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0x103,
        (
            "#020F没关系的，别担心。\x02\x03",

            "这孩子也是经验丰富、\x01",
            "独当一面的游击士了嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0x101,
        (
            "#1008F嘿嘿，就算是吧……\x02\x03",

            "#1015F不过，和雪拉姐\x01",
            "还差得远呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0xA,
        (
            "哈哈，还有心给师姐面子，\x01",
            "看来是不要紧了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0xA,
        (
            "那么，调查要努力哦。\x01",
            "期待你们的好消息。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C7A")

    ChrTalk(    #300
        0x106,
        "#050F啊啊，交给我们吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3CF7")

    label("loc_3C7A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3CA8")

    ChrTalk(    #301
        0x108,
        "#070F啊啊，尽力而为了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3CF7")

    label("loc_3CA8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3CDA")

    ChrTalk(    #302
        0x104,
        "#030F呵，尽情期待我的表现。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3CF7")

    label("loc_3CDA")


    ChrTalk(    #303
        0x103,
        "#525F嗯嗯，交给我们吧。\x02",
    )

    CloseMessageWindow()

    label("loc_3CF7")

    OP_A2(0x188D)
    OP_A2(0x1)

    label("loc_3CFD")

    Jump("loc_43E3")

    label("loc_3D00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_43DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x311, 4)), scpexpr(EXPR_END)), "loc_3E0C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D9E")

    ChrTalk(    #304
        0xA,
        (
            "话说回来这么大的雾，\x01",
            "可真是前所未见啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0xA,
        (
            "定期船都停航了，\x01",
            "真是麻烦的天气啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0xA,
        (
            "哎呀，很快就会天晴的吧。\x01",
            "不用那么担心吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E09")

    label("loc_3D9E")

    TurnDirection(0xA, 0x101, 0)

    ChrTalk(    #307
        0xA,
        (
            "别一个人背负一切\x01",
            "有话想说随时都可以来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #308
        0xA,
        (
            "我们这边也准备了各种各样\x01",
            "高质量的装备等着你们呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E09")

    Jump("loc_43D9")

    label("loc_3E0C")

    OP_62(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xA, 0x101, 0)
    Sleep(400)

    ChrTalk(    #309
        0xA,
        "哦，这不是艾丝蒂尔吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #310
        0xA,
        (
            "好久不见啦。\x01",
            "从你去了训练场以后头一次见吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #311
        0x101,
        "#1000F埃尔格先生，好久不见。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #312
        0xA,
        "啊啊，终于回来了啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #313
        0xA,
        (
            "雪拉扎德也在一起，\x01",
            "是不是又在执行协会的什么任务啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0x103,
        "#020F嗯嗯，是啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #315
        0xA,
        (
            "听爱娜说了，\x01",
            "你们俩都很努力嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #316
        0xA,
        (
            "特别是艾丝蒂尔成为正游击士后\x01",
            "表现更加活跃了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #317
        0xA,
        (
            "真是的，才这么一会儿不见，\x01",
            "就变得这么出色了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #318
        0xA,
        (
            "当年你那么讨厌考试，\x01",
            "在研修中发牢骚，真令人怀念啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(    #319
        0x101,
        "#1008F我、我说埃尔格先生……\x02",
    )

    CloseMessageWindow()

    def lambda_400A():
        TurnDirection(0x0, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_400A)

    def lambda_4018():
        TurnDirection(0x1, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_4018)

    def lambda_4026():
        TurnDirection(0x2, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_4026)
    TurnDirection(0x3, 0x101, 400)
    Sleep(400)

    ChrTalk(    #320
        0x103,
        (
            "#021F哎呀，有什么好隐瞒的。\x02\x03",

            "考试确实是很惨，\x01",
            "但实技方面可是出类拔萃。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_40C8")

    ChrTalk(    #321
        0x106,
        (
            "#051F哈哈，果然是这样吗。\x02\x03",

            "真像你的风格啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_417C")

    label("loc_40C8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_40FE")

    ChrTalk(    #322
        0x107,
        (
            "#560F嘿嘿……\x02\x03",

            "哎～姐姐真是的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_417C")

    label("loc_40FE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_413B")

    ChrTalk(    #323
        0x104,
        (
            "#031F呵，感觉\x01",
            "真像是艾丝蒂尔的过去啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_417C")

    label("loc_413B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_417C")

    ChrTalk(    #324
        0x108,
        (
            "#070F哈哈，别害羞嘛。\x02\x03",

            "人有缺点才显得可爱嘛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_417C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_419D")

    ChrTalk(    #325
        0x105,
        "#041F嘻嘻……\x02",
    )

    CloseMessageWindow()

    label("loc_419D")


    ChrTalk(    #326
        0xA,
        "呀，抱歉抱歉。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #327
        0xA,
        (
            "老说过去的事，\x01",
            "大概是因为上了年纪啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #328
        0xA,
        "话说回来，艾丝蒂尔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #329
        0xA,
        (
            "关于约修亚\x01",
            "有什么消息吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_421D():
        TurnDirection(0x0, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_421D)

    def lambda_422B():
        TurnDirection(0x1, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_422B)

    def lambda_4239():
        TurnDirection(0x2, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_4239)
    TurnDirection(0x3, 0xA, 400)
    Sleep(400)

    ChrTalk(    #330
        0x101,
        (
            "#1003F嗯、嗯……\x02\x03",

            "#1007F调查了不少，\x01",
            "但没发现什么。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #331
        0xA,
        (
            "是吗……\x01",
            "果然没那么简单吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #332
        0xA,
        (
            "听卡西乌斯说起的时候，\x01",
            "担心的不得了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #333
        0xA,
        (
            "但现在看来…艾丝蒂尔。\x01",
            "你是没问题了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #334
        0xA,
        (
            "但是，觉得难过的时候\x01",
            "随时都可以来这里哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #335
        0xA,
        (
            "不介意的话我和斯蒂娜\x01",
            "都可以听你倾诉的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #336
        0x101,
        (
            "#1025F埃尔格先生……\x02\x03",

            "#1000F……嗯，谢谢。\x01",
            "我一定会的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #337
        0xA,
        "啊啊，常来逛逛吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #338
        0xA,
        (
            "各种高品质的装备\x01",
            "都等着你哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x188C)
    OP_A2(0x0)

    label("loc_43D9")

    Jump("loc_43E3")

    label("loc_43DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_43E3")

    label("loc_43E3")

    TalkEnd(0xA)
    Return()

    # Function_7_25E5 end

    def Function_8_43E7(): pass

    label("Function_8_43E7")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_494C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x413, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4686")
    TurnDirection(0xB, 0x101, 0)

    ChrTalk(    #339
        0xFE,
        (
            "呀，艾丝蒂尔。\x01",
            "欢迎，终于来……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0xB, 0x102, 400)

    ChrTalk(    #340
        0xFE,
        "……哎呀？哎呀呀？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #341
        0xFE,
        (
            "莫非是……\x01",
            "……约修亚……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #342
        0x102,
        (
            "#1040F好久不见了。\x01",
            "斯蒂娜阿姨。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #343
        0xFE,
        (
            "不，不是做梦……\x01",
            "真的是约修亚！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #344
        0xFE,
        (
            "哎呀，你之前到底\x01",
            "跑到哪里去了！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #345
        0x102,
        (
            "#1043F抱歉……\x01",
            "让您担心了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #346
        0xFE,
        (
            "啊……\x01",
            "对，对不起哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #347
        0xFE,
        (
            "不应该责备\x01",
            "约修亚的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #348
        0xFE,
        (
            "最难过的\x01",
            "应该你自己呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #349
        0x101,
        "#1025F阿姨……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #350
        0xFE,
        (
            "约修亚……\x01",
            "抬起头来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #351
        0xFE,
        (
            "你现在能回到洛连特，\x01",
            "这就足够了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #352
        0xFE,
        (
            "所以，别那样\x01",
            "一脸阴沉哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #353
        0xFE,
        (
            "好不容易才见面，\x01",
            "不高兴点多难受啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #354
        0x102,
        (
            "#1040F哈哈……\x01",
            "确实是这样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #355
        0xFE,
        (
            "嗯嗯，果然\x01",
            "年轻人的笑容就是无敌呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #356
        0xFE,
        (
            "以后都要用这个笑容\x01",
            "突破工作中的难关哦！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    OP_A2(0x209D)
    Jump("loc_4949")

    label("loc_4686")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_4827")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4726")

    ChrTalk(    #357
        0xFE,
        (
            "阿姨也要努力做家务，\x01",
            "不能输给艾丝蒂尔你们才行啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #358
        0xFE,
        (
            "怎么说扫除和洗衣\x01",
            "全部都得靠手来做呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #359
        0xFE,
        (
            "照平时那样子，\x01",
            "不一会儿太阳都要下山了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4824")

    label("loc_4726")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47D8")

    ChrTalk(    #360
        0xFE,
        (
            "哎呀，是艾丝蒂尔啊。\x01",
            "工作的情形怎样了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #361
        0xFE,
        (
            "阿姨也在努力\x01",
            "做家务哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #362
        0xFE,
        (
            "怎么说扫除和洗衣\x01",
            "全部都得靠手来做呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #363
        0xFE,
        (
            "虽然辛苦，\x01",
            "但这可是显示主妇毅力的地方呢！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_4824")

    label("loc_47D8")


    ChrTalk(    #364
        0xFE,
        (
            "阿姨也在努力\x01",
            "做家务哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #365
        0xFE,
        (
            "虽然辛苦，\x01",
            "但这可是显示主妇毅力的地方呢！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4824")

    Jump("loc_4949")

    label("loc_4827")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_48C2")
    TurnDirection(0xB, 0x102, 0)

    ChrTalk(    #366
        0xFE,
        (
            "阿姨也不会\x01",
            "再提过去的事了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #367
        0xFE,
        (
            "最难过的\x01",
            "毕竟是约修亚你自己嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #368
        0xFE,
        (
            "所以，抬起头\x01",
            "开朗一点吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #369
        0xFE,
        (
            "年轻人还是\x01",
            "最适合明朗的笑容了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4949")

    label("loc_48C2")


    ChrTalk(    #370
        0xFE,
        (
            "导力器不能动了，\x01",
            "真是奇怪的事情呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #371
        0xFE,
        (
            "大家的工作也增加了，\x01",
            "不过可千万别勉强哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #372
        0xFE,
        (
            "累了就该好好休息……\x01",
            "这个可绝对不能忘哦？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4949")

    Jump("loc_60E1")

    label("loc_494C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_50FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34B, 3)), scpexpr(EXPR_END)), "loc_4BA2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_49B4")

    ChrTalk(    #373
        0xFE,
        (
            "很可惜，详细的做法\x01",
            "我也没有听过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #374
        0xFE,
        (
            "说不定是只在\x01",
            "洛连特流传的乡土料理。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B9F")

    label("loc_49B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x1, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x1, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_49DF")
    Call(1, 0)
    Jump("loc_4B9F")

    label("loc_49DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B35")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4A58")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #375
        0xFE,
        "那么，艾丝蒂尔。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #376
        0xFE,
        (
            "要多注意身体，\x01",
            "打起精神来哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #377
        0xFE,
        (
            "期待着你和\x01",
            "约修亚一起回来的日子。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B32")

    label("loc_4A58")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #378
        0xFE,
        (
            "艾丝蒂尔你们似乎\x01",
            "这次也是十分活跃呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #379
        0xFE,
        (
            "终于雾散天晴了，\x01",
            "恢复到原来明亮的城市了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #380
        0xFE,
        (
            "艾丝蒂尔\x01",
            "好像又要去别处了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #381
        0xFE,
        (
            "要多注意身体，\x01",
            "打起精神来哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #382
        0xFE,
        (
            "期待着你和约修亚\x01",
            "一起回来的那一天。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 0)
    OP_A2(0x2)

    label("loc_4B32")

    Jump("loc_4B9F")

    label("loc_4B35")

    TurnDirection(0xFE, 0x103, 0)

    ChrTalk(    #383
        0xFE,
        "……雪拉。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #384
        0xFE,
        "阿姨相信你们。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #385
        0x103,
        (
            "#025F没、没问题的啦。\x02\x03",

            "#525F你们可以尽管放心，\x01",
            "只管等吧㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B9F")

    Jump("loc_50F8")

    label("loc_4BA2")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #386
        0xFE,
        (
            "哎呀，欢迎。\x01",
            "艾丝蒂尔！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #387
        0xFE,
        (
            "呼嘿嘿……\x01",
            "看来非常活跃呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #388
        0x101,
        (
            "#1008F哪里……\x01",
            "没做什么的啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #389
        0xFE,
        (
            "哈，怎么说艾丝蒂尔\x01",
            "现在都是游击士了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #390
        0xFE,
        (
            "总觉得，好像不是\x01",
            "阿姨认识的艾丝蒂尔了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #391
        0xFE,
        (
            "呜呜……\x01",
            "阿姨感到有点寂寞……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #392
        0x101,
        "#1004F我、我说阿姨……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #393
        0xFE,
        "……嘿嘿，开玩笑啦～☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #394
        0xFE,
        (
            "呵呵，艾丝蒂尔\x01",
            "的修行还远远不够呢⊙\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #395
        0x101,
        (
            "#1016F呜、呜……别这么说嘛。\x02\x03",

            "（阿、阿姨装哭的功力\x01",
            "  可不是盖的啊。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #396
        0xFE,
        (
            "艾丝蒂尔你们\x01",
            "好像又要去别处了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #397
        0xFE,
        (
            "要多加注意身体，\x01",
            "打起精神来哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #398
        0xFE,
        (
            "期待着你和约修亚\x01",
            "一起回来的那一天。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #399
        0xFE,
        "所以啦，雪拉。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #400
        0xFE,
        (
            "艾丝蒂尔的事，\x01",
            "就交给你照顾了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #401
        0xFE,
        (
            "绝对不能\x01",
            "让她喝酒哦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #402
        0x103,
        (
            "#021F呵呵，这没问题。\x02\x03",

            "#525F不强人所难\x01",
            "是我的原则嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(15)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4E84")
    OP_62(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(10)

    label("loc_4E84")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4EAE")
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(10)

    label("loc_4EAE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4ED8")
    OP_62(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(10)

    label("loc_4ED8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4F02")
    OP_62(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(10)

    label("loc_4F02")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4F2C")
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(10)

    label("loc_4F2C")

    Sleep(1000)

    def lambda_4F37():
        TurnDirection(0x0, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4F37)

    def lambda_4F45():
        TurnDirection(0x1, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_4F45)

    def lambda_4F53():
        TurnDirection(0x2, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_4F53)
    TurnDirection(0x3, 0x103, 400)

    ChrTalk(    #403
        0x101,
        "#1020F咦咦……！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4FAB")

    ChrTalk(    #404
        0x107,
        "#065F你、你刚才说什么……！？\x02",
    )

    CloseMessageWindow()

    label("loc_4FAB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4FDC")

    ChrTalk(    #405
        0x105,
        "#542F（是、是不是听错了……）\x02",
    )

    CloseMessageWindow()

    label("loc_4FDC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4FFF")

    ChrTalk(    #406
        0x104,
        "#036F呼…………\x02",
    )

    CloseMessageWindow()

    label("loc_4FFF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_502C")

    ChrTalk(    #407
        0x108,
        "#073F…………………………\x02",
    )

    CloseMessageWindow()

    label("loc_502C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5059")

    ChrTalk(    #408
        0x106,
        "#055F…………………………\x02",
    )

    CloseMessageWindow()

    label("loc_5059")

    OP_62(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x103, 0x3, 400)
    Sleep(400)
    TurnDirection(0x103, 0x0, 400)

    ChrTalk(    #409
        0x103,
        "#023F哎呀，大家怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #410
        0xFE,
        (
            "阿、阿姨也\x01",
            "开始觉得有点不安了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #411
        0xFE,
        "……雪拉。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #412
        0xFE,
        "真的交给你了哦。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1A5B)
    OP_A2(0x3)

    label("loc_50F8")

    Jump("loc_60E1")

    label("loc_50FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_57A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x311, 6)), scpexpr(EXPR_END)), "loc_53E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_536A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_51DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_5176")

    ChrTalk(    #413
        0xFE,
        (
            "王国军都出动，\x01",
            "让人有点吃惊呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #414
        0xFE,
        (
            "但是，有士兵在\x01",
            "总算比较放心倒是真的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51DA")

    label("loc_5176")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_51DA")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #415
        0xFE,
        (
            "事件的调查很辛苦，\x01",
            "不过可千万别勉强哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #416
        0xFE,
        (
            "艾丝蒂尔要是倒下了…\x01",
            "阿姨会哭的哦！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51DA")

    Jump("loc_5367")

    label("loc_51DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_52AF")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #417
        0xFE,
        (
            "呀，欢迎。\x01",
            "艾丝蒂尔你们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #418
        0xFE,
        (
            "呵呵，看来今天也\x01",
            "一早就在努力工作呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #419
        0xFE,
        (
            "王国军都出动，\x01",
            "虽然吓了一跳……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #420
        0xFE,
        (
            "但是，有士兵在\x01",
            "总算比较放心倒是真的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #421
        0xFE,
        (
            "那么，艾丝蒂尔\x01",
            "工作中也要小心哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5364")

    label("loc_52AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_5364")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #422
        0xFE,
        (
            "哎呀，是艾丝蒂尔啊。\x01",
            "早上好，今天也这么早啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #423
        0xFE,
        (
            "事件的调查很辛苦，\x01",
            "不过可千万别勉强哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #424
        0xFE,
        (
            "艾丝蒂尔要是倒下了…\x01",
            "阿姨会哭的哦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #425
        0x101,
        "#1008F我、我会小心的……\x02",
    )

    CloseMessageWindow()

    label("loc_5364")

    OP_A2(0x2)

    label("loc_5367")

    Jump("loc_53E0")

    label("loc_536A")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #426
        0xFE,
        (
            "艾丝蒂尔看来\x01",
            "也在努力工作呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #427
        0xFE,
        (
            "也像个女孩子似的爱干净\x01",
            "穿得整整洁洁的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #428
        0xFE,
        (
            "呼，阿姨\x01",
            "也感到安心了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53E0")

    Jump("loc_579E")

    label("loc_53E3")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(400)

    ChrTalk(    #429
        0xFE,
        "哎呀…………！？\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #430
        0xFE,
        (
            "呀～怎么办呀。\x01",
            "这不是艾丝蒂尔吗！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #431
        0xFE,
        (
            "昨天就听到传闻\x01",
            "我正等着你来呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #432
        0x101,
        (
            "#1008F嘿嘿……\x01",
            "斯蒂娜阿姨，好久不见。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #433
        0x103,
        "#020F抱歉这么晚才来打招呼。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #434
        0xFE,
        (
            "哪里，别介意。\x01",
            "工作很忙吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #435
        0xFE,
        (
            "听说约修亚的事时\x01",
            "还有点担心……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #436
        0xFE,
        (
            "唔，艾丝蒂尔看来\x01",
            "也在努力呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #437
        0x101,
        "#1016F嗯、嗯……算是吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #438
        0xFE,
        (
            "那，这事就不提了，\x01",
            "艾丝蒂尔……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #439
        0xFE,
        (
            "（盯……………………\x01",
            "　……………………………）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #440
        0x101,
        (
            "#1015F什、什么？\x01",
            "突然盯着我看。\x02\x03",

            "我、我刷了牙，\x01",
            "脸也洗了才来的呀？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #441
        0xFE,
        "#3S真是的，好漂亮呀！\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(    #442
        0x101,
        "#1004F哇哇！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #443
        0xFE,
        "怎么回事，穿这裙子！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #444
        0xFE,
        (
            "有种活跃女孩子的感觉哦～～\x01",
            "很适合你哦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #445
        0x101,
        (
            "#1008F嘿嘿……是、是吗？\x02\x03",

            "这个，是雪拉姐\x01",
            "在王都给我买的。\x02\x03",

            "作为当上正游击士的祝贺哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #446
        0xFE,
        (
            "哦～到底是雪拉。\x01",
            "很有品味嘛！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #447
        0x103,
        (
            "#021F呵呵，阿姨\x01",
            "喜欢就好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #448
        0xFE,
        (
            "注意仪容\x01",
            "可是有心思的表现哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #449
        0xFE,
        (
            "为这次的事件\x01",
            "好像也很努力……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #450
        0xFE,
        (
            "嗯嗯，即使成为正游击士\x01",
            "看来也能做得很出色呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x188E)
    OP_A2(0x3)

    label("loc_579E")

    Jump("loc_60E1")

    label("loc_57A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_5D52")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x311, 6)), scpexpr(EXPR_END)), "loc_5828")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #451
        0xFE,
        (
            "艾丝蒂尔看来\x01",
            "也在努力工作呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #452
        0xFE,
        (
            "也像个女孩子似的爱干净\x01",
            "穿得整整洁洁的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #453
        0xFE,
        (
            "呼，阿姨\x01",
            "也感到安心了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D4F")

    label("loc_5828")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(400)

    ChrTalk(    #454
        0xFE,
        "哎呀…………！？\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #455
        0xFE,
        (
            "呀～怎么办呀。\x01",
            "这不是艾丝蒂尔吗！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #456
        0xFE,
        (
            "哎呀哎呀，仔细一看\x01",
            "连雪拉也在一起呀？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #457
        0x101,
        "#1008F嘿嘿，好久不见。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #458
        0x103,
        "#021F呵呵，好久不见了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #459
        0xFE,
        (
            "真是的～真是好久不见哦！\x01",
            "阿姨都急死了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #460
        0xFE,
        (
            "昨天就听到传闻，\x01",
            "但去碰你却一直没碰上。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #461
        0x101,
        "#1016F啊哈哈，对不起。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #462
        0x103,
        (
            "#027F不过，艾丝蒂尔\x01",
            "也有很多事情啦。\x02\x03",

            "就原谅她吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #463
        0xFE,
        (
            "没问题，这点事\x01",
            "阿姨还是明白的啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #464
        0xFE,
        (
            "听说约修亚的事时，\x01",
            "还有点担心……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #465
        0xFE,
        (
            "嗯，看来艾丝蒂尔\x01",
            "也很努力的样子呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #466
        0x101,
        "#1016F嗯、嗯……算是吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #467
        0xFE,
        (
            "那，别提了，\x01",
            "艾丝蒂尔……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #468
        0xFE,
        (
            "（盯……………………\x01",
            "　……………………………）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #469
        0x101,
        (
            "#1015F什、什么？\x01",
            "突然盯着我看。\x02\x03",

            "我、我刷了牙，\x01",
            "脸也洗了才来的呀？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #470
        0xFE,
        "#3S真是的，多漂亮呀！\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(    #471
        0x101,
        "#1004F哇哇！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #472
        0xFE,
        "怎么回事，穿这裙子！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #473
        0xFE,
        (
            "有种活跃女孩子的感觉哦～～\x01",
            "很适合你哦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #474
        0x101,
        (
            "#1008F嘿嘿……是、是吗？\x02\x03",

            "这个，是雪拉姐\x01",
            "在王都给我买的。\x02\x03",

            "作为当上正游击士的祝贺哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #475
        0xFE,
        (
            "哦～到底是雪拉。\x01",
            "很有品味嘛！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #476
        0x103,
        (
            "#021F呵呵，阿姨\x01",
            "喜欢就好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #477
        0xFE,
        (
            "注意仪容\x01",
            "可是有心思的表现哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #478
        0xFE,
        (
            "嗯嗯，即使成为正游击士\x01",
            "看来也能做得很出色呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #479
        0xFE,
        (
            "以前那么邋遢的艾丝蒂尔\x01",
            "打扮得这么有模有样的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #480
        0xFE,
        (
            "呜呜……\x01",
            "阿、阿姨都快流眼泪了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #481
        0x101,
        (
            "#1008F哈，哈哈……\x02\x03",

            "#1013F（没，没想到\x01",
            "  穿条裙子她都会哭啊。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #482
        0x103,
        (
            "#025F（要是看到艾丝蒂尔穿婚纱\x01",
            "那还不得昏倒了啊……）\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x188E)

    label("loc_5D4F")

    Jump("loc_60E1")

    label("loc_5D52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_60E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x206, 0)), scpexpr(EXPR_END)), "loc_5DAC")

    ChrTalk(    #483
        0xFE,
        (
            "艾丝蒂尔，下次\x01",
            "要和约修亚一起来玩哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #484
        0xFE,
        "我会做好吃的等着你们来。\x02",
    )

    CloseMessageWindow()
    Jump("loc_60E1")

    label("loc_5DAC")

    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xFE, 0x101, 400)
    Sleep(600)
    OP_63(0xFE)

    ChrTalk(    #485
        0xFE,
        "……艾丝蒂尔？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #486
        0x101,
        "#001F Hi～斯蒂娜阿姨。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #487
        0xFE,
        "真是你……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #488
        0x101,
        "#501F咦？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #489
        0xFE,
        "是真正的艾丝蒂尔！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #490
        0xFE,
        (
            "啊啊，感觉已经\x01",
            "１０年没见了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #491
        0x101,
        "#506F哪、哪有那么夸张……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #492
        0xFE,
        (
            "我每天都和家里人\x01",
            "说起你们哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #493
        0xFE,
        (
            "什么都不告诉阿姨，\x01",
            "就突然去旅行……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #494
        0x101,
        "#008F嗯……对不起……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #495
        0xFE,
        (
            "没关系啦，发生那么多\x01",
            "事情，也没办法吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #496
        0xFE,
        (
            "那，赶快\x01",
            "说说旅行的故事吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #497
        0xFE,
        (
            "我也好想见见约修亚呢。\x01",
            "他在洛连特吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #498
        0x101,
        "#501F唔，嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #499
        0x142,
        "#1060F……稍微打扰一下。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x142, 400)

    ChrTalk(    #500
        0xFE,
        "哎呀，你是……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #501
        0x142,
        (
            "#1060F初次见面，我是巡回神父\x01",
            "凯文·格拉汉姆。\x02\x03",

            "打扰你们久别重逢很抱歉，\x01",
            "但现在艾丝蒂尔有急事。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #502
        0xFE,
        "哎、哎呀……是这样啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #503
        0xFE,
        (
            "阿姨真是的，\x01",
            "不知不觉就啰嗦起来……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #504
        0x101,
        (
            "#000F哪里，别在意。\x01",
            "我会再来看您的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #505
        0xFE,
        (
            "嗯嗯，我会做艾丝蒂尔\x01",
            "喜欢吃的等着你来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #506
        0xFE,
        (
            "下次要和约修亚\x01",
            "一起来玩哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1030)

    label("loc_60E1")

    TalkEnd(0xB)
    Return()

    # Function_8_43E7 end

    def Function_9_60E5(): pass

    label("Function_9_60E5")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_616E")

    ChrTalk(    #507
        0xFE,
        (
            "在雾散之前，\x01",
            "好像定期船都不能飞呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #508
        0xFE,
        (
            "这么说，暂时\x01",
            "都会待在这里了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #509
        0xFE,
        (
            "嗯～至少去看看\x01",
            "附近的名胜就不会觉得无聊了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_616E")

    TalkEnd(0xC)
    Return()

    # Function_9_60E5 end

    def Function_10_6172(): pass

    label("Function_10_6172")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_61D9")

    ChrTalk(    #510
        0xFE,
        (
            "格鲁纳门啦，威尔特桥什么的，\x01",
            "想拍的地方还不少呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #511
        0xFE,
        (
            "难得来到洛连特\x01",
            "感觉真可惜啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62FF")

    label("loc_61D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_62FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_6248")

    ChrTalk(    #512
        0xFE,
        (
            "本来是来冲洗之前\x01",
            "旅行拍摄的照片的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #513
        0xFE,
        (
            "由于雾太大哪里也不能去，\x01",
            "想着就看看照片也好啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62FF")

    label("loc_6248")


    ChrTalk(    #514
        0xFE,
        (
            "本来是来冲洗之前\x01",
            "旅行拍摄的照片的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #515
        0xFE,
        (
            "由于雾太大哪里也不能去，\x01",
            "想着就看看照片也好啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #516
        0xFE,
        (
            "也有兴趣去拍摄\x01",
            "洛连特的钟楼……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #517
        0xFE,
        (
            "但是这种天气……\x01",
            "也只是浪费感光结晶回路了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_62FF")

    TalkEnd(0xD)
    Return()

    # Function_10_6172 end

    SaveToFile()

Try(main)
