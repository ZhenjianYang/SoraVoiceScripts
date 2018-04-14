from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3118   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3118.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
        Flags               = 1,
        EntryFunctionIndex  = 0,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T3118_1 ._SN',
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
        '米妮亚姆医生',                         # 9
        '安东尼',                               # 10
        '安东尼',                               # 11
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
        'ED6_DT07/CH01430 ._CH',             # 00
        'ED6_DT07/CH01700 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH01430P._CP',             # 00
        'ED6_DT07/CH01700P._CP',             # 01
    )

    DeclNpc(
        X                   = -1410,
        Z                   = 0,
        Y                   = 6690,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -5510,
        Z                   = 0,
        Y                   = -3140,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -5510,
        Z                   = 0,
        Y                   = -3140,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = -5510,
        TriggerZ            = 0,
        TriggerY            = -3140,
        TriggerRange        = 1000,
        ActorX              = -5510,
        ActorZ              = 500,
        ActorY              = -3140,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 1,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_13E",          # 00, 0
        "Function_1_16F",          # 01, 1
        "Function_2_19F",          # 02, 2
        "Function_3_200",          # 03, 3
        "Function_4_1093",         # 04, 4
    )


    def Function_0_13E(): pass

    label("Function_0_13E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_15B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_158")
    ClearChrFlags(0x9, 0x80)
    OP_43(0x9, 0x0, 0x0, 0x2)

    label("loc_158")

    Jump("loc_16E")

    label("loc_15B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_16E")
    ClearChrFlags(0x9, 0x80)
    OP_43(0x9, 0x0, 0x0, 0x2)

    label("loc_16E")

    Return()

    # Function_0_13E end

    def Function_1_16F(): pass

    label("Function_1_16F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19A")
    OP_6F(0x0, 29)
    OP_72(0x0, 0x10)
    OP_79(0xFF, 0x2)
    OP_7A(0x7, 0x2)
    OP_7B()
    OP_72(0x6, 0x4)
    OP_72(0x7, 0x4)

    label("loc_19A")

    OP_64(0x0, 0x1)
    Return()

    # Function_1_16F end

    def Function_2_19F(): pass

    label("Function_2_19F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1FF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x1, 0x400)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x0, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E5")
    OP_8D(0xFE, -3860, -2270, -5240, -3760, 1000)
    Jump("loc_1FC")

    label("loc_1E5")

    OP_8D(0xFE, -6290, -6030, -3150, 520, 1000)

    label("loc_1FC")

    Jump("Function_2_19F")

    label("loc_1FF")

    Return()

    # Function_2_19F end

    def Function_3_200(): pass

    label("Function_3_200")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_599")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_295")
    TurnDirection(0xFE, 0x107, 0)

    ChrTalk(    #0
        0xFE,
        "哎呀，诸位游击士……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        "还有提妲也在啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x107,
        "#560F米妮亚姆医生，你好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x101,
        "#1000F嘿嘿，好久不见。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C9")

    label("loc_295")


    ChrTalk(    #4
        0xFE,
        "哎呀，诸位游击士……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        "#1000F嗯，好久不见。\x02",
    )

    CloseMessageWindow()

    label("loc_2C9")

    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #6
        0xFE,
        "你看起来很有精神，真是太好了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x101,
        (
            "#1000F米妮亚姆医生也是。\x02\x03",

            "#1007F不过你的工作\x01",
            "好像很忙……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "嗯，我刚检查了\x01",
            "医药品的储备情况。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "关键的时候\x01",
            "没有药可就麻烦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x102,
        (
            "#1043F是啊……\x02\x03",

            "现状运输手段\x01",
            "也很匮乏……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "暂时只能控制一下\x01",
            "药品的使用量了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "所以你们也要\x01",
            "小心一点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "如果受重伤的话\x01",
            "我可饶不了你们。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_475")

    ChrTalk(    #14
        0x101,
        (
            "#1016F啊哈哈……我会注意的。\x02\x03",

            "……听到吗？阿加特。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x106,
        "#552F为什么问我？\x02",
    )

    CloseMessageWindow()
    Jump("loc_4A9")

    label("loc_475")


    ChrTalk(    #16
        0x101,
        "#1016F啊哈哈……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x102,
        "#1035F我们会充分注意的。\x02",
    )

    CloseMessageWindow()

    label("loc_4A9")

    OP_A2(0x0)
    OP_A2(0x20D3)
    Jump("loc_596")

    label("loc_4B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_554")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_509")

    ChrTalk(    #18
        0xFE,
        (
            "暂时只能控制一下\x01",
            "药品的使用量了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "你们也要\x01",
            "也要多加小心哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_551")

    label("loc_509")


    ChrTalk(    #20
        0xFE,
        (
            "总觉得好久\x01",
            "没见到安东尼了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "真是的，这孩子之前\x01",
            "究竟去了哪儿。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_551")

    Jump("loc_596")

    label("loc_554")


    ChrTalk(    #22
        0xFE,
        (
            "暂时只能控制一下\x01",
            "药品的使用量了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "你们也要\x01",
            "多加小心哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_596")

    Jump("loc_108F")

    label("loc_599")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x285, 6)), scpexpr(EXPR_END)), "loc_A6E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A25")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_70E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_658")

    ChrTalk(    #24
        0xFE,
        (
            "七耀教会的神父\x01",
            "现在也在开发着新药哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "虽然他们为什么能开发新药\x01",
            "到现在仍然是个疑问……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "不过我看了那篇论文以后就明白了。\x01",
            "总之是有很强的人在里面。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70B")

    label("loc_658")


    ChrTalk(    #27
        0xFE,
        (
            "最近在一本医学杂志上\x01",
            "读了神父写的论文。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "实在是写得太棒了。\x01",
            "我都有点受打击了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "不仅了解教会的传统医疗，\x01",
            "连现代医学也懂……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "有机会真想和作者\x01",
            "迪拜恩神父聊聊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_70B")

    Jump("loc_A22")

    label("loc_70E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_828")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_77D")

    ChrTalk(    #31
        0xFE,
        (
            "我最近的研究课题\x01",
            "就是做教会处方的药的分析。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "整理一下知识的话\x01",
            "一定能发现一些什么的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_825")

    label("loc_77D")


    ChrTalk(    #33
        0xFE,
        (
            "我最近的研究课题\x01",
            "就是做教会处方的药的分析。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "结果已经把那种治肩酸的药的\x01",
            "药理结构都已经掌握了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "虽然可能只是一小步，\x01",
            "不过积累下去的话就能找到突破口了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_825")

    Jump("loc_A22")

    label("loc_828")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_97A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_8C4")

    ChrTalk(    #36
        0xFE,
        (
            "医学者赖以立足的\x01",
            "近代医学还历史尚浅。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "虽然在外科领域有了成果，\x01",
            "不过药学的知识还不及教会。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "因为他们积累了\x01",
            "一千年以上的经验。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_977")

    label("loc_8C4")


    ChrTalk(    #39
        0xFE,
        (
            "阿加特能够得救也是\x01",
            "因为有了七耀教会的药吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "这药很令人感兴趣，\x01",
            "所以我也试着分析了一下……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "不过还是不明白\x01",
            "为什么会起效果。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "唉，近代医学的力量\x01",
            "还不过如此啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_977")

    Jump("loc_A22")

    label("loc_97A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_A22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_9DD")

    ChrTalk(    #43
        0xFE,
        (
            "在中央工房的研究室里\x01",
            "也有危险的药品哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "如果瓶子碎了的话\x01",
            "就不好收拾了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A22")

    label("loc_9DD")


    ChrTalk(    #45
        0xFE,
        (
            "没有人因\x01",
            "地震受伤呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "呼，客人\x01",
            "摇晃得不厉害真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_A22")

    Jump("loc_A6B")

    label("loc_A25")


    ChrTalk(    #47
        0xFE,
        (
            "如果再有什么事的话\x01",
            "你们随时都可以来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "我一般都在\x01",
            "这个房间。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A6B")

    Jump("loc_108F")

    label("loc_A6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_D2A")
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #49
        0xFE,
        "哎呀，是你们呀……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x101,
        (
            "#1011F啊，米妮亚姆医生。\x02\x03",

            "#1007F那时候太\x01",
            "麻烦您，真是谢谢了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x106,
        "#053F嗯，受你照顾了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x106, 400)

    ChrTalk(    #52
        0xFE,
        (
            "阿加特。\x01",
            "你看起来很有精神，真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        "后来身体的情况怎么样？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x106,
        (
            "#050F没问题。\x01",
            "托你的福，完全恢复了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "那真是太好了。\x01",
            "好像也没有后遗症……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "呵呵，了不起的恢复能力。\x01",
            "到底是以身体作为资本的游击士。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x101,
        (
            "#1016F嗯，这就是阿加特。\x01",
            "只有体力是没话说的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C3A")

    ChrTalk(    #58
        0x107,
        "#067F哎，嘿嘿……\x02",
    )

    CloseMessageWindow()

    label("loc_C3A")


    ChrTalk(    #59
        0xFE,
        (
            "如果再有什么事的话\x01",
            "随时可以到这里来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "当然，那种伤势\x01",
            "还是不希望再见到了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x106,
        (
            "#051F嗯，不用担心。\x02\x03",

            "我也不想再受\x01",
            "那样的伤了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        "嗯，你可别忘记这话啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "一定要小心\x01",
            "继续努力吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        (
            "#1006F嗯，明白了。\x02\x03",

            "那么再见了，医生。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1089")

    label("loc_D2A")

    TurnDirection(0xFE, 0x101, 0)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #65
        0xFE,
        "哎呀，你是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x101,
        (
            "#1011F啊，米妮亚姆医生。\x02\x03",

            "#1007F那时候真是\x01",
            "还麻烦您，真是谢谢了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DC8")

    ChrTalk(    #67
        0x107,
        "#562F真、真的……\x02",
    )

    CloseMessageWindow()

    label("loc_DC8")


    ChrTalk(    #68
        0xFE,
        "不，我什么也没做。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "要感谢的话\x01",
            "就感谢教区长吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "那么……\x01",
            "阿加特还好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x101,
        (
            "#1006F嗯，没问题。\x01",
            "看上去已经完全恢复了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        "是吗，那就太好了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "呵呵，了不起的恢复能力。\x01",
            "到底是以身体作为资本的游击士。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x101,
        (
            "#1016F嗯，这就是阿加特。\x01",
            "只有体力是没话说的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EFA")

    ChrTalk(    #75
        0x107,
        "#067F哎，嘿嘿……\x02",
    )

    CloseMessageWindow()

    label("loc_EFA")


    ChrTalk(    #76
        0xFE,
        (
            "如果再有什么事的话\x01",
            "你们随时可以过来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "当然，那种伤势\x01",
            "还是不希望再见到了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x101,
        (
            "#1015F是啊……\x01",
            "得小心谨慎。\x02\x03",

            "无论怎样的工作\x01",
            "都隐藏着危险……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x103,
        (
            "#026F嗯，就像艾丝蒂尔说的。\x02\x03",

            "为了防备看不见的威胁\x01",
            "要经常把感觉磨练的敏感……\x02\x03",

            "#027F卡西乌斯老师也经常说\x01",
            "这是游击士的心得。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #80
        0xFE,
        "嗯，请一定不要忘记那些话。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #81
        0xFE,
        (
            "今后也要小心\x01",
            "继续努力吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x101,
        (
            "#1006F嗯，明白了。\x02\x03",

            "那么再见了，医生。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1089")

    OP_A2(0x142E)
    OP_A2(0x0)

    label("loc_108F")

    TalkEnd(0x8)
    Return()

    # Function_3_200 end

    def Function_4_1093(): pass

    label("Function_4_1093")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_10B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_10B3")
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #83
        0xFE,
        "喵～\x02",
    )

    CloseMessageWindow()

    label("loc_10B3")

    Jump("loc_10C5")

    label("loc_10B6")

    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #84
        0xFE,
        "喵～\x02",
    )

    CloseMessageWindow()

    label("loc_10C5")

    TalkEnd(0x9)
    Return()

    # Function_4_1093 end

    SaveToFile()

Try(main)
