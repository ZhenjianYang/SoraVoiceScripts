from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'E0110   ._SN',
        MapName             = 'event',
        Location            = 'E0110.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60087",
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
        '乔丝特',                               # 9
        '多伦',                                 # 10
        '吉尔',                                 # 11
        '空贼雷古',                             # 12
        '通信员利昂',                           # 13
        '空贼阿伦',                             # 14
        '空贼罗尔',                             # 15
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
        'ED6_DT27/CH03100 ._CH',             # 00
        'ED6_DT27/CH03760 ._CH',             # 01
        'ED6_DT27/CH03770 ._CH',             # 02
        'ED6_DT07/CH01380 ._CH',             # 03
        'ED6_DT27/CH03101 ._CH',             # 04
        'ED6_DT26/CH20416 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT27/CH03100P._CP',             # 00
        'ED6_DT27/CH03760P._CP',             # 01
        'ED6_DT27/CH03770P._CP',             # 02
        'ED6_DT07/CH01380P._CP',             # 03
        'ED6_DT27/CH03101P._CP',             # 04
        'ED6_DT26/CH20416P._CP',             # 05
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Direction           = 180,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Direction           = 180,
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


    DeclActor(
        TriggerX            = 51600,
        TriggerZ            = 0,
        TriggerY            = 74000,
        TriggerRange        = 1000,
        ActorX              = 51600,
        ActorZ              = 1000,
        ActorY              = 74000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 18,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1DE",          # 00, 0
        "Function_1_390",          # 01, 1
        "Function_2_465",          # 02, 2
        "Function_3_47B",          # 03, 3
        "Function_4_C2A",          # 04, 4
        "Function_5_1000",         # 05, 5
        "Function_6_1337",         # 06, 6
        "Function_7_137F",         # 07, 7
        "Function_8_16F0",         # 08, 8
        "Function_9_1C6B",         # 09, 9
        "Function_10_1DC3",        # 0A, 10
        "Function_11_2037",        # 0B, 11
        "Function_12_2258",        # 0C, 12
        "Function_13_2F39",        # 0D, 13
        "Function_14_3624",        # 0E, 14
        "Function_15_365C",        # 0F, 15
        "Function_16_3694",        # 10, 16
        "Function_17_371B",        # 11, 17
        "Function_18_37AE",        # 12, 18
    )


    def Function_0_1DE(): pass

    label("Function_0_1DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_238")
    SetChrPos(0xA, 45810, 0, 6940, 0)
    ClearChrFlags(0xA, 0x80)
    OP_43(0xA, 0x0, 0x0, 0x2)
    SetChrPos(0xB, -21870, 650, 4940, 315)
    ClearChrFlags(0xB, 0x80)
    OP_43(0xB, 0x0, 0x0, 0x2)
    SetChrPos(0xD, 46020, 0, 77750, 0)
    ClearChrFlags(0xD, 0x80)
    Jump("loc_309")

    label("loc_238")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_2A8")
    SetChrPos(0xA, 45810, 0, 6940, 0)
    ClearChrFlags(0xA, 0x80)
    OP_43(0xA, 0x0, 0x0, 0x2)
    SetChrPos(0xB, -21870, 650, 4940, 315)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x10)
    OP_43(0xB, 0x0, 0x0, 0x2)
    SetChrPos(0xC, -22620, 650, 5630, 135)
    SetChrPos(0xD, 46020, 0, 77750, 0)
    ClearChrFlags(0xD, 0x80)
    Jump("loc_309")

    label("loc_2A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_2B2")
    Jump("loc_309")

    label("loc_2B2")

    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xB, 45590, 0, 6950, 0)
    SetChrPos(0xD, 46020, 0, 77750, 0)
    SetChrPos(0xE, 47720, 0, 6300, 45)
    OP_43(0xB, 0x0, 0x0, 0x2)
    OP_43(0xD, 0x0, 0x0, 0x2)
    OP_43(0xE, 0x0, 0x0, 0x2)

    label("loc_309")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 4)), scpexpr(EXPR_END)), "loc_323")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x85), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F4)
    Event(0, 11)
    Jump("loc_38F")

    label("loc_323")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_334")
    OP_A3(0x10F0)
    Event(0, 8)
    Jump("loc_38F")

    label("loc_334")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_34B")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x59), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 9)
    Jump("loc_38F")

    label("loc_34B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_362")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x59), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 10)
    Jump("loc_38F")

    label("loc_362")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 3)), scpexpr(EXPR_END)), "loc_373")
    OP_A3(0x10F3)
    Event(0, 12)
    Jump("loc_38F")

    label("loc_373")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_38F")
    Event(0, 7)

    label("loc_38F")

    Return()

    # Function_0_1DE end

    def Function_1_390(): pass

    label("Function_1_390")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AE")
    OP_4F(0x3B, (scpexpr(EXPR_PUSH_LONG, 0x227), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x3C, (scpexpr(EXPR_PUSH_LONG, 0x10A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3AE")

    OP_22(0x7A, 0x1, 0x3C)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_3D2")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x59), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3EE")

    label("loc_3D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_3E5")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3EE")

    label("loc_3E5")

    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x56), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3EE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_443")
    LoadEffect(0x0, "map\\\\mp027_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 51600, 1000, 74000, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)

    label("loc_443")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45B")
    OP_10(0x0, 0x0)
    OP_10(0x5, 0x1)
    OP_10(0x6, 0x0)
    Jump("loc_464")

    label("loc_45B")

    OP_10(0x0, 0x0)
    OP_10(0x5, 0x0)
    OP_10(0x6, 0x1)

    label("loc_464")

    Return()

    # Function_1_390 end

    def Function_2_465(): pass

    label("Function_2_465")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_47A")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_465")

    label("loc_47A")

    Return()

    # Function_2_465 end

    def Function_3_47B(): pass

    label("Function_3_47B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_7D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_769")
    OP_A2(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x452, 6)), scpexpr(EXPR_END)), "loc_5D5")

    ChrTalk(    #0
        0xA,
        (
            "#200F哟，是你们吗。\x02\x03",

            "航行控制的故障\x01",
            "总算已经解决了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_514")

    ChrTalk(    #1
        0x10B,
        (
            "#210F真、真的吗？\x02\x03",

            "太棒了！\x01",
            "不愧是吉尔兄啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_53B")

    label("loc_514")


    ChrTalk(    #2
        0x101,
        (
            "#1000F啊，真的吗？\x01",
            "那不是很好吗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53B")


    ChrTalk(    #3
        0xA,
        (
            "#200F其实，这全都多亏了\x01",
            "拉赛尔博士的建议。\x02\x03",

            "真是个了不起的老爷爷啊。\x01",
            "连看都没看过，就可以\x01",
            "马上说出故障的部位。\x02\x03",

            "果然不愧是世界著名的\x01",
            "导力学者啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_766")

    label("loc_5D5")


    ChrTalk(    #4
        0xA,
        (
            "#200F哟，是你们吗。\x02\x03",

            "航行控制方面出了一些毛病，\x01",
            "不过总算已经解决了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_672")

    ChrTalk(    #5
        0x10B,
        (
            "#210F嘿嘿，吉尔哥哥果然厉害，\x02\x03",

            "简直比导力技师\x01",
            "还要了不起呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C5")

    label("loc_672")


    ChrTalk(    #6
        0x101,
        (
            "#1000F哦～挺了不起的嘛。\x01",
            "居然可以自己一个人修理。\x02\x03",

            "真是没有辜负空贼的称号呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C5")


    ChrTalk(    #7
        0xA,
        (
            "#200F不，其实都多亏了\x01",
            "拉赛尔博士的建议。\x02\x03",

            "我们通过导力通信进行联络，\x01",
            "他马上就找到了原因。\x02\x03",

            "真是好厉害的老爷爷呢。\x01",
            "身为世界著名的导力学者，\x01",
            "果然是名不虚传。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_766")

    Jump("loc_7D3")

    label("loc_769")


    ChrTalk(    #8
        0xA,
        (
            "#200F拉赛尔博士\x01",
            "果然是个了不起的学者啊，\x02\x03",

            "只是听了一下症状，\x01",
            "马上就能找到故障部位……\x01",
            "实在太厉害了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D3")

    Jump("loc_C26")

    label("loc_7D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_C26")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7F4")
    Call(0, 13)
    OP_A2(0x5)
    Return()

    label("loc_7F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_847")

    ChrTalk(    #9
        0xA,
        (
            "#200F车站终端的密码吗……\x01",
            "确实有这个可能。\x02\x03",

            "总之有试一试\x01",
            "的价值呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C26")

    label("loc_847")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x452, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BCF")

    ChrTalk(    #10
        0xA,
        "#200F呼～真是麻烦……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_89C")

    ChrTalk(    #11
        0x10B,
        "#210F吉尔哥，有什么问题吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_8B6")

    label("loc_89C")


    ChrTalk(    #12
        0x101,
        "#1000F有什么问题吗？\x02",
    )

    CloseMessageWindow()

    label("loc_8B6")


    ChrTalk(    #13
        0xA,
        (
            "#200F嗯，航行控制方面\x01",
            "稍微出了点问题。\x02\x03",

            "虽然可以勉强起飞，\x01",
            "但是无法进行长距离的飞行。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_939")

    ChrTalk(    #14
        0x10B,
        "#210F是、是吗……\x02",
    )

    CloseMessageWindow()
    Jump("loc_96C")

    label("loc_939")


    ChrTalk(    #15
        0x101,
        (
            "#1000F虽、虽然听不大懂，\x01",
            "不过看起来很麻烦啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_96C")


    ChrTalk(    #16
        0xA,
        (
            "#200F船体的修复还算可以，\x01",
            "但精密仪器就无能为力了。\x02\x03",

            "不如和『埃尔赛尤』\x01",
            "联络一下寻求帮助吧。\x02\x03",

            "呼，也不知道在通信中\x01",
            "能不能解决问题…\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AD6")

    ChrTalk(    #17
        0x101,
        (
            "#1000F嗯……\x01",
            "提妲不能帮忙吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x107,
        (
            "#060F我、我虽然懂得一点……\x01",
            "不过最好还是让专业人员来做。\x02\x03",

            "因为飞翔引擎在飞船中\x01",
            "是最为复杂的部分了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x101,
        "#1000F有、有那么复杂啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x102,
        (
            "#1030F看来只能够\x01",
            "询问一下了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B91")

    label("loc_AD6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B3D")

    ChrTalk(    #21
        0x10B,
        (
            "#210F不过也只有试试看了。\x02\x03",

            "难得这次可以彼此携手合作，\x01",
            "要是不利用一下就太可惜了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B91")

    label("loc_B3D")


    ChrTalk(    #22
        0x101,
        (
            "#1000F不过，还是有\x01",
            "试试看的必要吧？\x02\x03",

            "拉赛尔博士也在那里，\x01",
            "或许可以给点提示哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B91")


    ChrTalk(    #23
        0xA,
        (
            "#200F嗯，就是这么回事……\x02\x03",

            "还是再耐心地\x01",
            "等一等吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2296)
    Jump("loc_C26")

    label("loc_BCF")


    ChrTalk(    #24
        0xA,
        (
            "#200F航行控制的问题\x01",
            "凭我们是解决不了的。\x02\x03",

            "毕竟这种精密仪器\x01",
            "不是一般人可以修理的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C26")

    TalkEnd(0xFE)
    Return()

    # Function_3_47B end

    def Function_4_C2A(): pass

    label("Function_4_C2A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_E10")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D3E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CCD")
    OP_A2(0x1)

    ChrTalk(    #25
        0xB,
        (
            "噢，小姐，\x01",
            "联络工作辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xB,
        (
            "多亏『埃尔赛尤』的帮忙，\x01",
            "飞翔引擎也修理好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xB,
        (
            "双方一起协力合作，\x01",
            "果然是有所价值啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D3B")

    label("loc_CCD")


    ChrTalk(    #28
        0xB,
        (
            "多亏『埃尔赛尤』的帮忙，\x01",
            "飞翔引擎也修理好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xB,
        (
            "呼，毕竟要是帮不上忙的话，\x01",
            "协力合作就没有什么价值了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D3B")

    Jump("loc_E0D")

    label("loc_D3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DBF")
    OP_A2(0x2)

    ChrTalk(    #30
        0xB,
        (
            "控制装置的故障\x01",
            "似乎也已经解除了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xB,
        (
            "那么～我们也要\x01",
            "赶紧调整计量器了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xB,
        (
            "再磨磨蹭蹭的话\x01",
            "会被老大骂的哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E0D")

    label("loc_DBF")


    ChrTalk(    #33
        0xB,
        (
            "控制装置的故障\x01",
            "似乎也已经解除了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xB,
        (
            "那么～我们也要\x01",
            "赶紧调整计量器了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E0D")

    Jump("loc_FFC")

    label("loc_E10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_FC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F4C")
    OP_A2(0x2)

    ChrTalk(    #35
        0xC,
        (
            "这里是埃尔赛尤号……\x01",
            "……山猫号，请回答。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xC,
        "……重复一次，山猫号请回答。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xB,
        "啊啊，这里是山猫号……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xB,
        (
            "接收信号良好……\x01",
            "埃尔赛尤号，你们那里听得清楚吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xC,
        (
            "埃尔赛尤呼叫山猫号……\x01",
            "我们这边的信号也很好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xC,
        (
            "贵舰现在有\x01",
            "什么物资不足吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xC,
        (
            "重复一次……\x01",
            "山猫号，有什么物资不足吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FC0")

    label("loc_F4C")


    ChrTalk(    #42
        0xB,
        (
            "呃～其实我们的航行控制装置\x01",
            "出了点问题无法解决，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xB,
        (
            "希望贵舰的维修员能提供建议。\x01",
            "重复一次，希望贵舰的维修员…\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FC0")

    Jump("loc_FFC")

    label("loc_FC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_FCD")
    Jump("loc_FFC")

    label("loc_FCD")


    ChrTalk(    #44
        0xB,
        "喔！快点啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xB,
        (
            "多伦老大\x01",
            "在舰桥等着呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FFC")

    TalkEnd(0xFE)
    Return()

    # Function_4_C2A end

    def Function_5_1000(): pass

    label("Function_5_1000")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_114D")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1097")
    OP_A2(0x3)

    ChrTalk(    #46
        0xD,
        (
            "啊，小姐……\x01",
            "您辛苦了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xD,
        (
            "飞翔引擎也修好了，\x01",
            "现在已经完全恢复正常了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xD,
        (
            "『山猫号』马上\x01",
            "就能完全复原了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10ED")

    label("loc_1097")


    ChrTalk(    #49
        0xD,
        (
            "飞翔引擎也修好了，\x01",
            "现在已经完全恢复正常了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xD,
        (
            "『山猫号』马上\x01",
            "就能完全复原了！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10ED")

    Jump("loc_114A")

    label("loc_10F0")


    ChrTalk(    #51
        0xFE,
        (
            "飞翔引擎修复完毕\x01",
            "可真是个好消息啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "这样看来的话，\x01",
            "『山猫号』就能再次起飞了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_114A")

    Jump("loc_1333")

    label("loc_114D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_12DB")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1207")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11BC")
    OP_A2(0x3)

    ChrTalk(    #53
        0xD,
        "啊，小姐！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xD,
        (
            "嘿嘿，刚才您\x01",
            "真是太帅了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xD,
        (
            "小姐果然\x01",
            "是我们的女神啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1204")

    label("loc_11BC")


    ChrTalk(    #56
        0xD,
        (
            "嘿嘿，刚才您\x01",
            "真是太帅了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xD,
        (
            "我们会努力修船，\x01",
            "请小姐耐心期待吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1204")

    Jump("loc_12D8")

    label("loc_1207")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_127A")
    OP_A2(0x4)

    ChrTalk(    #58
        0xD,
        (
            "哦，是你们啊。\x01",
            "刚才多谢了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xD,
        (
            "『结社』的那群家伙\x01",
            "还真是奇怪啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xD,
        (
            "你们最好\x01",
            "也多加小心吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12D8")

    label("loc_127A")


    ChrTalk(    #61
        0xD,
        (
            "『结社』的那群家伙\x01",
            "还真是奇怪啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xD,
        (
            "我们本来也有相当的实力，\x01",
            "但却完全不是他们的对手。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12D8")

    Jump("loc_1333")

    label("loc_12DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_12E5")
    Jump("loc_1333")

    label("loc_12E5")


    ChrTalk(    #63
        0xFE,
        (
            "不过多伦老大竟然会\x01",
            "下这种作战命令，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "仔细想想的话\x01",
            "实在太冒险了啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1333")

    TalkEnd(0xFE)
    Return()

    # Function_5_1000 end

    def Function_6_1337(): pass

    label("Function_6_1337")

    TalkBegin(0xFE)

    ChrTalk(    #65
        0xFE,
        "『山猫号』一切顺利。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "嘿嘿，也就是说\x01",
            "接下来就看你的了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_1337 end

    def Function_7_137F(): pass

    label("Function_7_137F")

    EventBegin(0x0)
    SetChrFlags(0x9, 0x4)
    SetChrPos(0xA, -18850, 3000, 5010, 270)
    SetChrPos(0x9, -22460, 650, 4800, 315)
    SetChrPos(0x8, -19890, 0, 3030, 270)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x102, -15530, 500, 4940, 270)
    SetChrFlags(0x102, 0x80)
    OP_6D(-20530, 650, 5540, 0)
    OP_67(0, 6460, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(313000, 0)
    OP_6E(282, 0)
    Call(0, 14)
    OP_79(0x9, 0x1)
    OP_7B()
    FadeToBright(1000, 0)
    OP_0D()
    ClearChrFlags(0x102, 0x80)
    OP_9F(0x102, 0x0, 0x0, 0x0, 0x0, 0x0)

    def lambda_1444():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1444)
    OP_8E(0x102, 0xFFFFBB9A, 0x0, 0x12FC, 0x7D0, 0x0)
    OP_8C(0x9, 90, 400)
    Sleep(100)
    OP_8C(0x8, 90, 400)

    ChrTalk(    #67
        0x9,
        "#190F喔，来了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x8,
        "#215F#5P…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x102,
        "#1032F状况如何？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x9,
        (
            "#490F嘿，果然如你所料。\x02\x03",

            "过来。\x01",
            "看这里的屏幕。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1500():
        OP_6D(-22030, 650, 5690, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1500)

    def lambda_1518():
        OP_6C(322000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1518)

    def lambda_1528():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1528)

    def lambda_1536():

        label("loc_1536")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_1536")

    QueueWorkItem2(0x8, 1, lambda_1536)
    OP_8E(0x102, 0xFFFFAB3C, 0x28A, 0x14DC, 0x7D0, 0x0)
    OP_8C(0x102, 315, 400)
    Sleep(200)
    WaitChrThread(0x102, 0x2)
    OP_44(0x8, 0x1)
    OP_8C(0x102, 315, 400)

    ChrTalk(    #71
        0x9,
        (
            "#198F#6P他们正在１５６０亚矩的高度，\x01",
            "以２１００塞尔矩的时速\x01",
            "从东北方向潜入利贝尔领空…\x02\x03",

            "从这种高度和速度来看，\x01",
            "绝对不是普通的飞船啊。\x02\x03",

            "#197F你装上的这个特殊雷达\x01",
            "看来还真有点用处啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x102,
        (
            "#1035F#6P不，现在还不能确定。\x02\x03",

            "#1031F也有可能是帝国的\x01",
            "侦察艇呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0xA, 400)
    Sleep(300)

    ChrTalk(    #73
        0x102,
        "#1030F#5P吉尔，目视的情况如何？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xA,
        (
            "#201F……捕捉到了！\x01",
            "我把影像传到你们那里！\x02",
        )
    )

    CloseMessageWindow()
    SetMapFlags(0x2000000)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_A2(0x10F5)
    NewScene("ED6_DT21/E0811   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_137F end

    def Function_8_16F0(): pass

    label("Function_8_16F0")

    EventBegin(0x0)
    SetChrFlags(0x9, 0x4)
    SetChrPos(0xA, -18850, 3000, 5010, 280)
    SetChrPos(0x9, -22460, 650, 4800, 315)
    SetChrPos(0x8, -19890, 0, 3030, 315)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x102, -21700, 650, 5340, 315)
    OP_6D(-22030, 650, 5690, 0)
    OP_67(0, 6460, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(322000, 0)
    OP_6E(282, 0)
    Call(0, 14)
    OP_79(0x9, 0x1)
    OP_7B()
    OP_74(0x4, 0x5, 0x10)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #75
        0x102,
        (
            "#1032F#6P……没错。\x01",
            "这就是此次的目标\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xA,
        (
            "#200F#2P嘿嘿……\x01",
            "终于准备妥当了吗。\x02\x03",

            "还真是有些紧张呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 90, 400)
    Sleep(500)

    ChrTalk(    #77
        0x9,
        (
            "#198F#5P好！这就开始吧！\x02\x03",

            "#490F小子！\x01",
            "做好心理准备了吗！？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 270, 400)
    Sleep(500)

    ChrTalk(    #78
        0x102,
        (
            "#1031F#4P没问题。\x02\x03",

            "等我站好位置之后，\x01",
            "马上就可以开始了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 90, 400)

    def lambda_18B2():
        OP_8E(0xFE, 0xFFFFBB9A, 0x0, 0x12FC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_18B2)

    def lambda_18CD():
        OP_6D(-21030, 500, 5850, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_18CD)

    def lambda_18E5():
        OP_6C(313000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_18E5)

    def lambda_18F5():

        label("loc_18F5")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_18F5")

    QueueWorkItem2(0x8, 3, lambda_18F5)

    ChrTalk(    #79 op#A op#5
        0x8,
        "#216F#12A啊……\x05\x02",
    )

    Sleep(500)
    OP_8C(0xA, 90, 400)
    WaitChrThread(0x102, 0x1)
    OP_44(0x8, 0x3)
    OP_8C(0x8, 90, 400)
    OP_20(0x5DC)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x102)
    Sleep(500)
    OP_1D(0x50)
    Sleep(1500)

    ChrTalk(    #80
        0x102,
        (
            "#1035F#5P多伦兄，吉尔兄，\x01",
            "还有乔丝特……\x02\x03",

            "#1031F这些日子…多谢你们了。\x02\x03",

            "虽然我们只是互利性质的合作关系，\x01",
            "但我是真正发自内心地感谢你们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x8,
        "#213F#5P……咦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xA,
        "#201F#5P嘿……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x9,
        "#192F#5P噢！？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x102, 270, 400)
    Sleep(500)

    ChrTalk(    #84
        0x102,
        (
            "#1031F#4P这些话本来想在战斗\x01",
            "结束之后再说的，不过……\x02\x03",

            "也许再也没有那个机会了，\x01",
            "所以就趁现在先对你们说。\x02\x03",

            "#1053F那么，各位多保重。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 90, 400)
    Sleep(500)

    def lambda_1ACC():
        OP_6D(-20270, 500, 6030, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1ACC)

    def lambda_1AE4():
        OP_8E(0xFE, 0xFFFFBFBE, 0xFA, 0x1324, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1AE4)
    WaitChrThread(0x102, 0x0)

    def lambda_1B04():
        OP_8E(0xFE, 0xFFFFC374, 0x1F4, 0x1338, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1B04)

    def lambda_1B1F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1B1F)
    WaitChrThread(0x102, 0x0)
    WaitChrThread(0x102, 0x1)
    WaitChrThread(0x102, 0x2)
    SetChrFlags(0x102, 0x80)
    Sleep(1000)

    def lambda_1B4A():
        OP_6D(-22030, 650, 5690, 1800)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1B4A)
    WaitChrThread(0x102, 0x2)
    Sleep(500)

    ChrTalk(    #85
        0xA,
        "#207F#5P那家伙……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x9,
        (
            "#197F#5P真是的……\x01",
            "都到最后关头了还是这个样子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x8,
        "#212F#5P……呜………！\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x8, 4)

    def lambda_1BDA():
        OP_6D(-20270, 500, 6030, 1500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1BDA)
    OP_8E(0x8, 0xFFFFB654, 0x0, 0xB72, 0x1388, 0x0)
    OP_8E(0x8, 0xFFFFB9C4, 0x0, 0x10D6, 0x1388, 0x0)
    OP_8E(0x8, 0xFFFFBFBE, 0xFA, 0x1324, 0x1388, 0x0)

    def lambda_1C2E():
        OP_8E(0xFE, 0xFFFFC374, 0x1F4, 0x1338, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1C2E)
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
    SetChrFlags(0x8, 0x80)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/E0811   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_8_16F0 end

    def Function_9_1C6B(): pass

    label("Function_9_1C6B")

    EventBegin(0x0)
    OP_A3(0x10F1)
    OP_24(0x7A, 0x64)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0xA, 0x4)
    SetChrPos(0xA, -24400, -1000, 4970, 270)
    SetChrPos(0x9, -22260, 650, 5230, 308)
    SetChrPos(0x8, -18850, 3000, 5010, 280)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0xA, 5)
    SetChrSubChip(0xA, 0)
    OP_6D(-22890, 0, 6950, 0)
    OP_67(0, 6790, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(322000, 0)
    OP_6E(267, 0)
    Call(0, 14)
    OP_79(0x9, 0x1)
    OP_7B()
    OP_76(0xC, 0x0, 0x1, 0xFFFFFFEC, 0xFFFFFFFC, 0x0, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #88
        0x8,
        "#415F#2P好啊！！……他成功了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x9,
        (
            "#191F#6P哦哦！\x01",
            "竟然成功了吗！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xA,
        (
            "#201F#6P很好！\x01",
            "那我们也可以撤退了！\x02",
        )
    )

    CloseMessageWindow()
    SetMapFlags(0x2000000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F3)
    NewScene("ED6_DT21/E0811   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_9_1C6B end

    def Function_10_1DC3(): pass

    label("Function_10_1DC3")

    EventBegin(0x0)
    OP_A3(0x10F2)
    OP_24(0x7A, 0x50)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0xA, 0x4)
    SetChrPos(0xA, -24400, -1000, 4970, 270)
    SetChrPos(0x9, -22260, 650, 5230, 308)
    SetChrPos(0x8, -18850, 3000, 5010, 280)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0xA, 5)
    SetChrSubChip(0xA, 0)
    OP_6D(-22890, 0, 6950, 0)
    OP_67(0, 6790, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(322000, 0)
    OP_6E(267, 0)
    Call(0, 14)
    OP_76(0xC, 0x0, 0x1, 0xFFFFFFF6, 0xFFFFFFFE, 0x0, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #91
        0x9,
        (
            "#490F#6P嘿嘿……\x01",
            "他们放弃追击了吗。\x02\x03",

            "一切都和那小子\x01",
            "预料的一模一样呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x8,
        (
            "#215F#2P……嗯。\x02\x03",

            "#413F……………………………………\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0xA, 2)
    Sleep(300)

    ChrTalk(    #93
        0xA,
        (
            "#204F#6P乔丝特，不用担心啦。\x02\x03",

            "#200F那家伙的话……\x01",
            "一定可以平安回来的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x8,
        (
            "#215F#2P嗯……说得也是。\x02\x03",

            "#210F我们约定好的……\x01",
            "一定要平安回来。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_20(0xFA0)
    Sleep(300)
    OP_24(0x7A, 0x46)
    Sleep(300)
    OP_24(0x7A, 0x3C)
    Sleep(300)
    OP_24(0x7A, 0x32)
    Sleep(300)
    OP_24(0x7A, 0x28)
    Sleep(300)
    OP_24(0x7A, 0x1E)
    Sleep(300)
    OP_24(0x7A, 0x14)
    Sleep(300)
    OP_24(0x7A, 0xA)
    Sleep(300)
    OP_23(0x7A)
    OP_0D()
    OP_21()
    OP_AD(0x2400A9, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_AE(0xC8)
    Sleep(2000)
    ClearMapFlags(0x2000000)
    OP_A2(0x10F3)
    NewScene("ED6_DT21/T1121   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_10_1DC3 end

    def Function_11_2037(): pass

    label("Function_11_2037")

    EventBegin(0x0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrPos(0xA, -24300, -1000, 4970, 270)
    SetChrPos(0x9, -21860, 650, 4770, 270)
    SetChrPos(0x8, -18850, 3000, 5010, 270)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    OP_6D(-24130, 0, 7440, 0)
    OP_67(0, 5440, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(322000, 0)
    OP_6E(280, 0)
    SetChrFlags(0xB, 0x80)
    OP_44(0xA, 0xFF)
    SetChrChipByIndex(0xA, 5)
    SetChrSubChip(0xA, 0)
    Call(0, 15)
    OP_22(0x7A, 0x1, 0x50)
    OP_76(0xB, 0x0, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xB, 0x1, 0x1, 0xFFFFFFFF, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xB, 0x2, 0x1, 0xFFFFFFFC, 0x0, 0x0, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_6B(3100, 2000)
    OP_0D()

    ChrTalk(    #95
        0x8,
        (
            "#418F#2P求求你，吉尔哥！\x02\x03",

            "这样下去的话\x01",
            "约修亚他们就……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xA,
        (
            "#204F#6P没用的，乔丝特……\x02\x03",

            "#207F……照现在的样子来看，他们恐怕已经……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x8,
        "#417F#2P怎么会……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x9,
        (
            "#198F……可恶……\x01",
            "都已经到了最后一步，为什么……\x02\x03",

            "#196F这种时候……\x01",
            "女神到底在干什么！？\x02",
        )
    )

    CloseMessageWindow()
    SetMapFlags(0x2000000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10FF)
    OP_A2(0x10F5)
    NewScene("ED6_DT21/E0310   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_11_2037 end

    def Function_12_2258(): pass

    label("Function_12_2258")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrPos(0xA, -24300, -1000, 4970, 270)
    SetChrPos(0x9, -21860, 650, 4770, 315)
    SetChrPos(0x8, -18850, 3000, 5010, 270)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    OP_6D(-24130, 0, 8000, 0)
    OP_67(0, 5010, -10000, 0)
    OP_6B(2920, 0)
    OP_6C(322000, 0)
    OP_6E(322, 0)
    SetChrChipByIndex(0xA, 5)
    SetChrSubChip(0xA, 0)
    Call(0, 15)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x1, "C_VIS227._CH")
    OP_C6(0x0, 0x3, -1, 0, 0)
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS180._CH")
    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_C6(0x1, 0x3, -1, 1000, 0)
    Sleep(1000)
    Sleep(1000)
    Sleep(1000)
    Sleep(1000)
    OP_22(0x7C, 0x0, 0x64)
    OP_C5(0x2, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS181._CH")
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    OP_C6(0x2, 0x3, -1, 0, 0)
    OP_C6(0x0, 0x4, 0, 0, 0)
    Sleep(1000)
    Sleep(1000)
    SetMessageWindowPos(400, 340, -1, -1)
    SetChrName("女孩的声音")

    AnonymousTalk(    #99
        "\x07\x00不、不会吧……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C6(0x2, 0x3, 16777215, 1000, 0)
    Sleep(1000)
    OP_C6(0x0, 0x3, 16777215, 0, 0)
    FadeToBright(1000, 0)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)
    OP_8F(0x8, 0xFFFFB816, 0xBB8, 0x127A, 0x7D0, 0x0)
    Sleep(500)

    ChrTalk(    #100
        0x8,
        (
            "#216F#2P那、那是什么东西啊！？\x02\x03",

            "竟然那么大……\x01",
            "也太夸张了吧！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x9,
        (
            "#192F#6P那东西，大概有\x01",
            "５０００亚矩以上吧……\x02\x03",

            "简直是个巨大的空中浮岛……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xA,
        (
            "#204F#6P不……基本上像是座人造建筑物。\x02\x03",

            "#206F与其说是岛屿，\x01",
            "不如说是一座浮游都市……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x8,
        "#213F#2P浮、浮游都市……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x9,
        "#198F#6P……这样的话……\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x9, 0x4)
    OP_8C(0x9, 270, 400)
    OP_8E(0x9, 0xFFFFA876, 0x28A, 0x1248, 0x5DC, 0x0)
    Sleep(500)

    ChrTalk(    #105
        0x9,
        "#196F#6P#3S……很好～～！小子们！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #106
        0x9,
        "#196F#6P#3S一鼓作气给我冲上那座浮游都市！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0xA, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrSubChip(0xA, 2)

    ChrTalk(    #107
        0xA,
        "#201F#6P大、大哥！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x8,
        "#213F#2P你、你是认真的吗！？\x02",
    )

    CloseMessageWindow()
    OP_8F(0x9, 0xFFFFAA9C, 0x28A, 0x12A2, 0x7D0, 0x0)
    OP_8C(0x9, 135, 400)
    Sleep(500)

    ChrTalk(    #109
        0x9,
        (
            "#490F#5P当然是说真的！真的不能再真！\x02\x03",

            "#198F如果这东西是『结社』的那群家伙\x01",
            "所召唤出来的话……\x02\x03",

            "#191F里面肯定会有\x01",
            "数不尽的神秘宝藏！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xA,
        (
            "#203F#6P大、大哥，你就饶了我们吧～……\x02\x03",

            "#201F凭我们的实力，\x01",
            "要硬闯的话实在是太冒险了！\x02\x03",

            "乔丝特，你也是这么想的吧！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x8,
        (
            "#413F#2P嗯，这个……\x02\x03",

            "#215F我觉得，都已经到这种地步了，\x01",
            "不如去确认一下吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xA,
        "#203F#6P呃……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x8,
        (
            "#415F#2P好、好了！总之从昨夜开始\x01",
            "就有点不对劲，还是小心点比较好。\x02\x03",

            "导力通讯也完全收不到了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x9,
        (
            "#197F#5P的确，军方和协会也就算了，\x01",
            "但民间的通信也收不到的话──\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_20(0x7D0)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6D(-24130, 0, 8000, 0)
    OP_67(0, 5010, -10000, 0)
    OP_6B(2720, 0)
    OP_6C(322000, 0)
    OP_6E(322, 0)
    OP_0D()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xA, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrSubChip(0xA, 0)
    OP_8C(0x9, 270, 500)

    ChrTalk(    #115
        0x9,
        "#192F#6P呜喔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xA,
        "#201F#6P什…什么…\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x8,
        "#213F#2P光、光波……？\x02",
    )

    CloseMessageWindow()
    Fade(1000)
    OP_82(0x80, 0x0)
    OP_0D()
    Fade(500)
    OP_22(0xE1, 0x0, 0x64)
    OP_23(0x7A)
    OP_71(0x5, 0x4)
    Sleep(100)
    OP_71(0x6, 0x4)
    Sleep(100)
    OP_71(0x7, 0x4)
    Sleep(100)
    OP_71(0x8, 0x4)
    Sleep(100)
    OP_71(0x9, 0x4)
    OP_74(0x4, 0x5, 0x0)
    OP_0D()
    Sleep(500)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xA, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #118
        0x8,
        "#216F#2P哎哎哎！？\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_1D(0x51)
    Sleep(500)
    OP_8C(0x9, 315, 400)

    ChrTalk(    #119
        0x9,
        "#192F#6P怎么回事？！故障吗！？\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0xB, 0x4)
    SetChrPos(0xB, -14000, 500, 4660, 270)
    OP_4A(0xB, 255)

    ChrTalk(    #120
        0xB,
        "#1P老大，不好了啊！\x02",
    )

    CloseMessageWindow()

    def lambda_2B67():
        OP_6D(-22710, 0, 7190, 1500)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_2B67)

    def lambda_2B7F():
        OP_67(0, 4640, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2B7F)

    def lambda_2B97():
        OP_6B(2920, 1500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2B97)
    ClearChrFlags(0xB, 0x80)

    def lambda_2BAC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_2BAC)

    def lambda_2BBE():
        OP_8E(0xB, 0xFFFFC374, 0x1F4, 0x1306, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2BBE)
    WaitChrThread(0xB, 0x1)
    ClearChrFlags(0xB, 0x4)

    def lambda_2BE3():
        OP_8E(0xB, 0xFFFFBB9A, 0x0, 0x12FC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2BE3)

    def lambda_2BFE():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2BFE)
    Sleep(50)

    def lambda_2C11():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2C11)
    Sleep(50)
    WaitChrThread(0xB, 0x1)
    Sleep(500)
    WaitChrThread(0x9, 0x0)

    ChrTalk(    #121
        0xB,
        (
            "#4P导力引擎，还有飞翔引擎\x01",
            "全都突然停止运转了！！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(    #122
        0x9,
        "#196F#5P什、什么～！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x8,
        "#216F#5P这是怎、怎么回事！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xA,
        (
            "#206F#6P……这下麻烦了……\x02\x03",

            "飞翔引擎所产生的\x01",
            "反重力力场下降……\x02\x03",

            "舵也没有反应了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(50)
    OP_62(0x8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    def lambda_2D44():
        OP_6D(-24130, 0, 7440, 1200)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_2D44)

    def lambda_2D5C():
        OP_67(0, 5440, -10000, 1200)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2D5C)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x9, 0xA, 400)
    TurnDirection(0x8, 0xA, 400)
    WaitChrThread(0x9, 0x0)

    ChrTalk(    #125
        0x9,
        "#196F#5P等、等一下！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x8,
        "#214F#2P怎、怎么会这样呢！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xA,
        (
            "#204F#6P………………………………\x02\x03",

            "#207F……到这种地步的话，\x01",
            "我们能做的就只有一件事了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x9,
        "#192F#1P是什么！？\x02",
    )


    ChrTalk(    #129
        0x8,
        "#213F#2P是什么！？\x02",
    )

    OP_56(0x1)
    OP_59()
    Sleep(100)
    SetChrSubChip(0xA, 2)
    Sleep(300)

    ChrTalk(    #130
        0xA,
        (
            "#203F#6P向女神祈祷，让我们不要\x01",
            "这么早就被召唤到天堂……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_7C(0x0, 0x64, 0xBB8, 0x7D0)
    OP_22(0xEC, 0x0, 0x64)
    OP_D0(5000, 0)
    Sleep(1000)
    OP_22(0x13B, 0x0, 0x64)

    def lambda_2EF0():
        OP_6D(-18330, 15000, 5500, 2000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2EF0)

    def lambda_2F08():
        OP_D0(25000, 2000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_2F08)
    Sleep(1000)
    SetMapFlags(0x2000000)
    SetMapFlags(0x100000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F5)
    NewScene("ED6_DT21/E0800   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_12_2258 end

    def Function_13_2F39(): pass

    label("Function_13_2F39")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F5E")
    Call(0, 16)
    Call(0, 17)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_2F5E")

    Fade(500)
    OP_6D(45440, 0, 6250, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, 45620, 0, 5160, 0)
    SetChrPos(0x102, 46440, 0, 5370, 0)
    SetChrPos(0xF8, 44470, 0, 5520, 45)
    SetChrPos(0xF9, 47260, 0, 5750, 315)
    OP_8C(0xA, 180, 0)
    OP_4A(0xA, 0)
    OP_0D()

    ChrTalk(    #131
        0xA,
        (
            "#200F对了……忘了一件事。\x02\x03",

            "你们听过\x01",
            "『Ｏ·Ｒ·Ｐ·Ｈ·Ｅ·Ｕ·Ｓ』\x01",
            "这个词吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x101,
        "#1000F那、那是什么？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_309C")

    ChrTalk(    #133
        0x10B,
        (
            "#210FＯＲＰＨＥＵＳ……\x01",
            "是读作奥菲斯吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31D5")

    label("loc_309C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30DB")

    ChrTalk(    #134
        0x105,
        (
            "#040FＯＲＰＨＥＵＳ……\x01",
            "是读作奥菲斯吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31D5")

    label("loc_30DB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_311A")

    ChrTalk(    #135
        0x104,
        (
            "#030FＯＲＰＨＥＵＳ……\x01",
            "是读作奥菲斯吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31D5")

    label("loc_311A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_315A")

    ChrTalk(    #136
        0x109,
        (
            "#1060FＯＲＰＨＥＵＳ……\x01",
            "是读作奥菲斯吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31D5")

    label("loc_315A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3199")

    ChrTalk(    #137
        0x107,
        (
            "#060FＯＲＰＨＥＵＳ……\x01",
            "是读作奥菲斯吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31D5")

    label("loc_3199")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_31D5")

    ChrTalk(    #138
        0x106,
        (
            "#050FＯＲＰＨＥＵＳ……\x01",
            "是读作奥菲斯吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31D5")


    ChrTalk(    #139
        0x102,
        "#1030F……这个词怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xA,
        (
            "#200F没什么，只是监视我们的\x01",
            "猎兵们曾经提到过它。\x02\x03",

            "我觉得它可能有什么含义，\x01",
            "所以就记下来了……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_32B7")

    ChrTalk(    #141
        0x10B,
        "#210F原来如此……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x101,
        (
            "#1000F嗯……\x01",
            "确实让人很在意呢。\x02\x03",

            "（啊……也许是！）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32F0")

    label("loc_32B7")


    ChrTalk(    #143
        0x101,
        (
            "#1000F嗯……\x01",
            "确实让人很在意呢。\x02\x03",

            "（啊……也许是！）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32F0")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【工业区域的通称】\x01",      # 0
            "【福音的正式名称】\x01",      # 1
            "【终端密码】\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_336C"),
        (1, "loc_33FC"),
        (2, "loc_3497"),
        (SWITCH_DEFAULT, "loc_34F1"),
    )


    label("loc_336C")


    ChrTalk(    #144
        0x102,
        (
            "#1030F不对，工业区域的名称是\x01",
            "『法克特里亚』哦。\x02\x03",

            "也许是……\x01",
            "工业区域的终端所要求输入\x01",
            "的密码也说不定啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x101,
        "#1000F啊……是车站的终端！\x02",
    )

    CloseMessageWindow()
    Jump("loc_34F1")

    label("loc_33FC")


    ChrTalk(    #146
        0x102,
        (
            "#1030F不，『福音』的名字\x01",
            "在这座都市里似乎也是\x01",
            "同样的叫法。\x02\x03",

            "也许是……\x01",
            "工业区域的终端所要求输入\x01",
            "的密码也说不定啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x101,
        "#1000F啊……是车站的终端！\x02",
    )

    CloseMessageWindow()
    Jump("loc_34F1")

    label("loc_3497")


    ChrTalk(    #148
        0x102,
        (
            "#1030F嗯。\x01",
            "大概就是工业区域车站的终端密码。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x101,
        "#1000F啊，约修亚也是这么想的吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_34F1")

    label("loc_34F1")


    ChrTalk(    #150
        0xA,
        "#200F？　怎么回事？\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #151
        (
            "\x07\x05将工业区域终端\x01",
            "需要输入密码才能打开地下道入口\x01",
            "的事情向吉尔说明了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #152
        0xA,
        (
            "#200F原来如此……\x01",
            "确实有这个可能。\x02\x03",

            "看来很有试一试的价值啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x101,
        "#1000F嘿嘿嘿，果然没错吧？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_35F1")

    ChrTalk(    #154
        0x10B,
        "#210F谢谢啦，吉尔哥！\x02",
    )

    CloseMessageWindow()

    label("loc_35F1")


    ChrTalk(    #155
        0x102,
        "#1030F我们赶快去确认一下吧。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xA, 0, 400)
    OP_4B(0xA, 0)
    OP_A2(0x222D)
    EventEnd(0x0)
    Return()

    # Function_13_2F39 end

    def Function_14_3624(): pass

    label("Function_14_3624")

    OP_71(0x2, 0x4)
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0xB, 0x4)
    OP_72(0xC, 0x4)
    OP_72(0x5, 0x4)
    OP_72(0x6, 0x4)
    OP_72(0x7, 0x4)
    OP_72(0x8, 0x4)
    OP_72(0x9, 0x4)
    Return()

    # Function_14_3624 end

    def Function_15_365C(): pass

    label("Function_15_365C")

    OP_71(0x2, 0x4)
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x3, 0x4)
    OP_72(0xB, 0x4)
    OP_71(0xC, 0x4)
    OP_72(0x5, 0x4)
    OP_72(0x6, 0x4)
    OP_72(0x7, 0x4)
    OP_72(0x8, 0x4)
    OP_72(0x9, 0x4)
    Return()

    # Function_15_365C end

    def Function_16_3694(): pass

    label("Function_16_3694")

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
        (0, "loc_370E"),
        (1, "loc_3714"),
        (SWITCH_DEFAULT, "loc_371A"),
    )


    label("loc_370E")

    OP_A2(0x1200)
    Jump("loc_371A")

    label("loc_3714")

    OP_A2(0x1201)
    Jump("loc_371A")

    label("loc_371A")

    Return()

    # Function_16_3694 end

    def Function_17_371B(): pass

    label("Function_17_371B")

    FadeToDark(0, 0, -1)
    OP_6D(-182260, 0, -191970, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x4, 0x3, 0x6, 0x7, 0x8, 0xA, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_17_371B end

    def Function_18_37AE(): pass

    label("Function_18_37AE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3801")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #156
        "\x07\x05好像是导力停止了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Jump("loc_39BF")

    label("loc_3801")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #157
        "\x07\x05这是一台可供旅行者回复体力的导力器装置。\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "在这里休息\x01",      # 0
            "离开\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39A4")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_82(0x0, 0x2)
    PlayEffect(0x0, 0x0, 0xFF, 51600, 1000, 74000, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    OP_6F(0xA, 0)
    OP_70(0xA, 0x32)
    OP_73(0xA)
    OP_20(0xBB8)
    OP_22(0xC, 0x0, 0x64)
    OP_82(0x0, 0x2)
    LoadEffect(0x1, "map\\\\mp027_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, 51600, 1000, 74000, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0xFF, 0xFE, 0x0)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_82(0x1, 0x2)
    PlayEffect(0x0, 0x0, 0xFF, 51600, 1000, 74000, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    OP_6F(0xA, 0)
    OP_1E()
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_39A4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_39BE")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_39BE")

    Return()

    label("loc_39BF")

    Return()

    # Function_18_37AE end

    SaveToFile()

Try(main)
