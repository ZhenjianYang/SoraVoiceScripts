from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2812   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2812.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60084",
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
        '乔儿',                                 # 9
        '罗迪',                                 # 10
        '雅莉丝',                               # 11
        '米克',                                 # 12
        '罗伊斯',                               # 13
        '莫妮卡',                               # 14
        '德尼斯',                               # 15
        '芙拉瑟',                               # 16
        '帕布尔',                               # 17
        '艾福托老师',                           # 18
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
        'ED6_DT26/CH20271 ._CH',             # 00
        'ED6_DT07/CH02390 ._CH',             # 01
        'ED6_DT07/CH01360 ._CH',             # 02
        'ED6_DT07/CH01780 ._CH',             # 03
        'ED6_DT07/CH01080 ._CH',             # 04
        'ED6_DT07/CH01580 ._CH',             # 05
        'ED6_DT07/CH01370 ._CH',             # 06
        'ED6_DT07/CH01363 ._CH',             # 07
        'ED6_DT07/CH01090 ._CH',             # 08
        'ED6_DT07/CH01093 ._CH',             # 09
        'ED6_DT07/CH01460 ._CH',             # 0A
        'ED6_DT07/CH01583 ._CH',             # 0B
    )

    AddCharChipPat(
        'ED6_DT26/CH20271P._CP',             # 00
        'ED6_DT07/CH02390P._CP',             # 01
        'ED6_DT07/CH01360P._CP',             # 02
        'ED6_DT07/CH01780P._CP',             # 03
        'ED6_DT07/CH01080P._CP',             # 04
        'ED6_DT07/CH01580P._CP',             # 05
        'ED6_DT07/CH01370P._CP',             # 06
        'ED6_DT07/CH01363P._CP',             # 07
        'ED6_DT07/CH01090P._CP',             # 08
        'ED6_DT07/CH01093P._CP',             # 09
        'ED6_DT07/CH01460P._CP',             # 0A
        'ED6_DT07/CH01583P._CP',             # 0B
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
        X                   = -1340,
        Z                   = 4000,
        Y                   = -1350,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -58700,
        Z                   = 0,
        Y                   = 25010,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -29460,
        Z                   = 0,
        Y                   = 30840,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -30830,
        Z                   = 450,
        Y                   = 26450,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -62080,
        Z                   = 0,
        Y                   = 27320,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -28980,
        Z                   = 0,
        Y                   = 970,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -60470,
        Z                   = 0,
        Y                   = 950,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -61916,
        Z                   = 200,
        Y                   = 30650,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 30000,
        Z                   = 0,
        Y                   = 30750,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 2,
    )


    ScpFunction(
        "Function_0_24A",          # 00, 0
        "Function_1_25E",          # 01, 1
        "Function_2_25F",          # 02, 2
        "Function_3_29D",          # 03, 3
        "Function_4_30F",          # 04, 4
        "Function_5_3F6",          # 05, 5
        "Function_6_4AD",          # 06, 6
        "Function_7_58E",          # 07, 7
        "Function_8_69B",          # 08, 8
        "Function_9_6D7",          # 09, 9
        "Function_10_78D",         # 0A, 10
        "Function_11_825",         # 0B, 11
        "Function_12_8E1",         # 0C, 12
        "Function_13_905",         # 0D, 13
        "Function_14_FD9",         # 0E, 14
        "Function_15_172E",        # 0F, 15
    )


    def Function_0_24A(): pass

    label("Function_0_24A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_25D")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 12)

    label("loc_25D")

    Return()

    # Function_0_24A end

    def Function_1_25E(): pass

    label("Function_1_25E")

    Return()

    # Function_1_25E end

    def Function_2_25F(): pass

    label("Function_2_25F")

    TalkBegin(0xFE)

    ChrTalk(    #0
        0xFE,
        "哦，怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "马上就是门禁了，\x01",
            "别出去太久哦。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_2_25F end

    def Function_3_29D(): pass

    label("Function_3_29D")

    TalkBegin(0xFE)

    ChrTalk(    #2
        0xFE,
        (
            "小说的登场人物，\x01",
            "多数也是以现实的人们\x01",
            "为模型构思出来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "只凭想象来写的话，\x01",
            "人物很容易变得单薄。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_3_29D end

    def Function_4_30F(): pass

    label("Function_4_30F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_382")

    ChrTalk(    #4
        0xFE,
        "虽说是下人……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "对来自帝国的我来说\x01",
            "蕾娜是我最好的朋友。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "到现在为止一直\x01",
            "都是这么想的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F2")

    label("loc_382")

    OP_A2(0x5)

    ChrTalk(    #7
        0xFE,
        (
            "我有多么\x01",
            "期待着旅行，\x01",
            "蕾娜也应该知道。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "知道如此却瞒着我\x01",
            "计划回去……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        "……这等于是背叛的行为。\x02",
    )

    CloseMessageWindow()

    label("loc_3F2")

    TalkEnd(0xFE)
    Return()

    # Function_4_30F end

    def Function_5_3F6(): pass

    label("Function_5_3F6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_444")

    ChrTalk(    #10
        0xFE,
        (
            "现在考试刚刚结束，\x01",
            "正是制造区别的机会。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        "好！要学习了！\x02",
    )

    CloseMessageWindow()
    Jump("loc_4A9")

    label("loc_444")

    OP_A2(0x4)

    ChrTalk(    #12
        0xFE,
        (
            "现在考试刚刚结束\x01",
            "正是制造区别的机会。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "呵呵，现在开始努力学习，\x01",
            "下次考试一定要再拿高分。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A9")

    TalkEnd(0xFE)
    Return()

    # Function_5_3F6 end

    def Function_6_4AD(): pass

    label("Function_6_4AD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_50A")

    ChrTalk(    #14
        0xFE,
        (
            "这个房间里的学生\x01",
            "完全是七零八落的呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "不过正因此\x01",
            "才能相处好也说不定。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58A")

    label("loc_50A")

    OP_A2(0x3)

    ChrTalk(    #16
        0xFE,
        (
            "帕布尔是个文学少女，\x01",
            "雅莉丝可爱又好奇……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "……而我却\x01",
            "喜欢运动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "住在这个房间里的学生，\x01",
            "是来自不同的班级的呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_58A")

    TalkEnd(0xFE)
    Return()

    # Function_6_4AD end

    def Function_7_58E(): pass

    label("Function_7_58E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_5F7")

    ChrTalk(    #19
        0xFE,
        (
            "学生之中对选举\x01",
            "漠不关心的人似乎也挺多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "好不容易有深刻讨论政治\x01",
            "的机会，真是遗憾。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_697")

    label("loc_5F7")

    OP_A2(0x2)

    ChrTalk(    #21
        0xFE,
        (
            "我作为学习政治经济的人，\x01",
            "对这次的选举也很有兴趣。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "但是，学生之中\x01",
            "漠不关心的人似乎也挺多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "罗基克的父亲就是候选人，\x01",
            "想想是和自己非常近的事……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_697")

    TalkEnd(0xFE)
    Return()

    # Function_7_58E end

    def Function_8_69B(): pass

    label("Function_8_69B")

    TalkBegin(0xFE)

    ChrTalk(    #24
        0xFE,
        (
            "这么说来\x01",
            "亚吉鲁那家伙不在呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        "去哪儿了呢？\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_69B end

    def Function_9_6D7(): pass

    label("Function_9_6D7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_721")

    ChrTalk(    #26
        0xFE,
        (
            "这套衣服，是坎诺\x01",
            "帮我做的哦～\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 10)

    ChrTalk(    #27
        0xFE,
        "不愧是美术部呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_786")

    label("loc_721")

    OP_A2(0x1)

    ChrTalk(    #28
        0xFE,
        (
            "在整理的时候发现了\x01",
            "学院祭上穿的衣服！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "这个是坎诺\x01",
            "帮我做的哦～\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 10)

    ChrTalk(    #30
        0xFE,
        "嘿嘿，很可爱吧㈱\x02",
    )

    CloseMessageWindow()

    label("loc_786")

    OP_63(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_9_6D7 end

    def Function_10_78D(): pass

    label("Function_10_78D")

    OP_62(0xFE, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(30)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(30)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(30)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(30)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(30)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(30)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(30)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(30)
    Return()

    # Function_10_78D end

    def Function_11_825(): pass

    label("Function_11_825")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_88E")

    ChrTalk(    #31
        0xFE,
        (
            "德尼斯那家伙\x01",
            "每次都拿高分。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "他总是拼命\x01",
            "学习真是令人讨厌。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        "富人更加富……吗。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8DD")

    label("loc_88E")

    OP_A2(0x0)

    ChrTalk(    #34
        0xFE,
        (
            "室友德尼斯那家伙\x01",
            "已经开始学习了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "考试才刚刚结束\x01",
            "真是讨厌的家伙。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8DD")

    TalkEnd(0xFE)
    Return()

    # Function_11_825 end

    def Function_12_8E1(): pass

    label("Function_12_8E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8F2")
    Call(0, 15)

    label("loc_8F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_900")
    Call(0, 13)
    Jump("loc_904")

    label("loc_900")

    Call(0, 14)

    label("loc_904")

    Return()

    # Function_12_8E1 end

    def Function_13_905(): pass

    label("Function_13_905")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x106, 0x8)
    SetChrFlags(0x104, 0x8)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x4)
    ClearChrFlags(0x101, 0x1)
    SetChrChipByIndex(0x101, 0)
    SetChrSubChip(0x101, 24)
    OP_6F(0x9, 12)
    SetChrPos(0x101, -118350, 500, -2400, 0)
    SetChrPos(0x105, -118420, 0, -1130, 175)
    SetChrPos(0x8, -119240, 0, -1120, 145)
    SetChrPos(0x127, -120350, 0, -2570, 90)
    OP_6D(-118450, 500, -2400, 0)
    OP_67(0, 4720, -10000, 0)
    OP_6B(3030, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_69(0x101, 0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("女孩的声音")

    AnonymousTalk(    #36
        "……艾丝蒂尔……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("女孩的声音")

    AnonymousTalk(    #37
        "艾丝蒂尔……来吧……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(    #38
        "#1007F嗯……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_1D(0x54)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    SetChrSubChip(0x101, 39)
    Sleep(100)
    SetChrSubChip(0x101, 40)
    Sleep(500)

    ChrTalk(    #39
        0x101,
        "#1004F咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x127,
        "#150F啊，小艾！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x105,
        (
            "#542F#5P太好了……\x01",
            "你醒了呢。\x02\x03",

            "那个，感觉如何？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x101,
        "#1000F嗯……还好。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_6F(0x9, 12)
    OP_70(0x9, 0xF)
    SetChrPos(0x101, -118250, 500, -2400, 0)
    OP_99(0x101, 0x19, 0x20, 0x3E8)
    Sleep(500)
    SetChrSubChip(0x101, 41)
    Sleep(100)
    SetChrSubChip(0x101, 42)
    Sleep(500)

    ChrTalk(    #43
        0x101,
        (
            "#1015F咦……\x01",
            "这里是女子宿舍吧？\x02\x03",

            "我怎么会在这里……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1500, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Sleep(200)
    SetChrFlags(0x101, 0x4)
    ClearChrFlags(0x101, 0x40)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    OP_96(0x101, 0xFFFE3072, 0x0, 0xFFFFF0EC, 0x64, 0xFA0)
    SetChrFlags(0x101, 0x1)
    OP_8C(0x101, 16, 0)
    OP_6F(0x9, 15)
    OP_70(0x9, 0xC)

    def lambda_BD9():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_BD9)

    def lambda_BE7():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x127, 1, lambda_BE7)

    def lambda_BF5():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_BF5)
    WaitChrThread(0x105, 0x1)
    WaitChrThread(0x127, 0x1)
    WaitChrThread(0x8, 0x1)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #44
        0x101,
        (
            "#1020F#2P啊，我！\x01",
            "在窗外看到了『白影』！\x02\x03",

            "然后……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x8,
        (
            "#645F#1P唉……\x01",
            "果然是看到幽灵了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x105,
        (
            "#043F#5P艾丝蒂尔……\x02\x03",

            "那个『白影』\x01",
            "是什么样子的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        (
            "#1007F#2P嗯、嗯……\x02\x03",

            "#1003F穿着古代的衣服，\x01",
            "戴着面具的男人……\x02\x03",

            "白白的一边发光\x01",
            "一边在空中滴溜溜地转……\x02\x03",

            "往旧校舍\x01",
            "那边飞了去……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x127,
        (
            "#153F哎～看起来相当\x01",
            "快乐的幽灵啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x105,
        (
            "#047F#5P和各地目击\x01",
            "『白影』的证言相同啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x8,
        "#644F#1P而且，果然是旧校舍吗?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x101,
        "#1019F#2P……什么玩笑。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x8,
        "#643F#1P咦……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        (
            "#1022F#2P谁知道是不是幽灵\x01",
            "这不是正好吗……\x02\x03",

            "装神弄鬼的吓人\x01",
            "还害我晕倒……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #54
        0x101,
        (
            "#1005F#2P#3S这笔帐，\x01",
            "绝对要算清楚！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #55
        0x8,
        "#645F#1P算、算帐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x127,
        (
            "#153F小艾。\x01",
            "你不是怕幽灵的吗～？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x127, 500)
    Sleep(300)

    ChrTalk(    #57
        0x101,
        (
            "#1019F#2P我怕幽灵是因为\x01",
            "不知道到底有没有！\x02\x03",

            "既然亲眼看到了，\x01",
            "事到如今就没什么好怕的了！\x02\x03",

            "我要让它再也出不来\x01",
            "好好整治它一番！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x8,
        (
            "#644F#1P嗯～说你是顽强\x01",
            "还是不正常了呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x105,
        (
            "#041F#5P呵呵……\x01",
            "到底是艾丝蒂尔。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T2811   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_13_905 end

    def Function_14_FD9(): pass

    label("Function_14_FD9")

    EventBegin(0x0)
    OP_20(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x104, 0x8)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x4)
    ClearChrFlags(0x101, 0x1)
    SetChrChipByIndex(0x101, 0)
    SetChrSubChip(0x101, 24)
    OP_6F(0x9, 12)
    SetChrPos(0x101, -118350, 500, -2400, 0)
    SetChrPos(0x103, -120030, 0, -4110, 35)
    SetChrPos(0x105, -118420, 0, -1130, 180)
    SetChrPos(0x8, -119240, 0, -1120, 145)
    SetChrPos(0x127, -120350, 0, -2570, 90)
    OP_6D(-118450, 500, -2400, 0)
    OP_67(0, 4720, -10000, 0)
    OP_6B(3030, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_69(0x101, 0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("女孩的声音")

    AnonymousTalk(    #60
        "……艾丝蒂尔……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("女孩的声音")

    AnonymousTalk(    #61
        "艾丝蒂尔……醒醒……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(    #62
        "#1007F嗯……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_1D(0x54)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    SetChrSubChip(0x101, 39)
    Sleep(100)
    SetChrSubChip(0x101, 40)
    Sleep(500)

    ChrTalk(    #63
        0x101,
        "#1004F咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x127,
        "#150F啊，小艾！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x105,
        (
            "#542F#5P太好了……\x01",
            "你醒了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x103,
        (
            "#025F呼……\x01",
            "冷汗都出来了。\x02\x03",

            "#020F那么，感觉如何？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x101,
        "#1000F嗯……还好。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_6F(0x9, 12)
    OP_70(0x9, 0xF)
    SetChrPos(0x101, -118250, 500, -2400, 0)
    OP_99(0x101, 0x19, 0x20, 0x3E8)
    Sleep(500)
    SetChrSubChip(0x101, 41)
    Sleep(100)
    SetChrSubChip(0x101, 42)
    Sleep(500)

    ChrTalk(    #68
        0x101,
        (
            "#1015F咦……\x01",
            "这里是女子宿舍吧？\x02\x03",

            "我怎么会在这里……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1500, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Sleep(200)
    SetChrFlags(0x101, 0x4)
    ClearChrFlags(0x101, 0x40)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    OP_96(0x101, 0xFFFE3072, 0x0, 0xFFFFF0EC, 0x64, 0xFA0)
    SetChrFlags(0x101, 0x1)
    OP_8C(0x101, 16, 0)
    OP_6F(0x9, 15)
    OP_70(0x9, 0xC)

    def lambda_12E3():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_12E3)

    def lambda_12F1():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_12F1)

    def lambda_12FF():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x127, 1, lambda_12FF)

    def lambda_130D():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_130D)
    WaitChrThread(0x105, 0x1)
    WaitChrThread(0x127, 0x1)
    WaitChrThread(0x8, 0x1)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #69
        0x101,
        (
            "#1020F#2P啊，我！\x01",
            "在窗外看到了『白影』！\x02\x03",

            "然后……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x103,
        (
            "#020F是是。\x01",
            "我知道了，你镇定一点吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x8,
        (
            "#645F#1P唉……\x01",
            "果然是看到幽灵了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x105,
        (
            "#043F#5P艾丝蒂尔……\x02\x03",

            "那个『白影』\x01",
            "是什么样子的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x101,
        (
            "#1007F#2P嗯、嗯……\x02\x03",

            "#1003F穿着古代的衣服，\x01",
            "戴着面具的男人……\x02\x03",

            "白白的一边发光\x01",
            "一边在空中滴溜溜地转……\x02\x03",

            "往旧校舍\x01",
            "那边飞了去……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x127,
        (
            "#153F哎～看起来相当\x01",
            "快乐的幽灵啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x105,
        (
            "#047F#5P和各地目击\x01",
            "『白影』的证言相同啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x8,
        "#644F#1P而且，果然是旧校舍吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x101,
        "#1019F#2P……开什么玩笑。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x8,
        "#643F#1P咦……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x101,
        (
            "#1022F#2P是幽灵也好，恶作剧也好，\x01",
            "胆子还真是不小啊……\x02\x03",

            "装神弄鬼地吓人，\x01",
            "还害我丢脸晕倒……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #80
        0x101,
        (
            "#1005F#2P#3S这笔帐，\x01",
            "绝对要算清楚！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #81
        0x8,
        "#645F#1P算、算帐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x103,
        (
            "#027F真是的……\x01",
            "你不是怕幽灵的吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    ChrTalk(    #83
        0x101,
        (
            "#1019F#2P我怕幽灵是因为\x01",
            "不知道到底有没有！\x02\x03",

            "既然亲眼看到了，\x01",
            "也就没什么好怕的了！\x02\x03",

            "我要好好整治它一番！\x01",
            "让它再也不敢出来！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x8,
        (
            "#644F#1P嗯～该说你顽强\x01",
            "还是不正常呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x105,
        (
            "#041F#5P呵呵……\x01",
            "到底是艾丝蒂尔。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T2811   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_14_FD9 end

    def Function_15_172E(): pass

    label("Function_15_172E")

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
        (0, "loc_17A8"),
        (1, "loc_17AE"),
        (SWITCH_DEFAULT, "loc_17B4"),
    )


    label("loc_17A8")

    OP_A2(0x1200)
    Jump("loc_17B4")

    label("loc_17AE")

    OP_A2(0x1201)
    Jump("loc_17B4")

    label("loc_17B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_17C2")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_17C6")

    label("loc_17C2")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_17C6")

    Return()

    # Function_15_172E end

    SaveToFile()

Try(main)
