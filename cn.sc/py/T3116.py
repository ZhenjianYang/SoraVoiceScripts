from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3116   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3116.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
        Flags               = 1,
        EntryFunctionIndex  = 12,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T3116_1 ._SN',
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
        '加鲁诺',                               # 9
        '拉赛尔博士',                           # 10
        '提妲',                                 # 11
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
        'ED6_DT07/CH01190 ._CH',             # 00
        'ED6_DT07/CH02020 ._CH',             # 01
        'ED6_DT07/CH00060 ._CH',             # 02
        'ED6_DT07/CH00137 ._CH',             # 03
        'ED6_DT07/CH00130 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT07/CH01190P._CP',             # 00
        'ED6_DT07/CH02020P._CP',             # 01
        'ED6_DT07/CH00060P._CP',             # 02
        'ED6_DT07/CH00137P._CP',             # 03
        'ED6_DT07/CH00130P._CP',             # 04
    )

    DeclNpc(
        X                   = -2000,
        Z                   = 0,
        Y                   = 3410,
        Direction           = 270,
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
        X                   = -120,
        Z                   = 0,
        Y                   = 13020,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -1920,
        Z                   = 0,
        Y                   = 14190,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )


    DeclActor(
        TriggerX            = -340,
        TriggerZ            = 0,
        TriggerY            = 15310,
        TriggerRange        = 1000,
        ActorX              = -340,
        ActorZ              = 500,
        ActorY              = 15310,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 4350,
        TriggerZ            = 0,
        TriggerY            = 2150,
        TriggerRange        = 1000,
        ActorX              = 4350,
        ActorZ              = 500,
        ActorY              = 2150,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 4600,
        TriggerZ            = 0,
        TriggerY            = 15420,
        TriggerRange        = 1000,
        ActorX              = 4600,
        ActorZ              = 500,
        ActorY              = 15420,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_19E",          # 00, 0
        "Function_1_1CF",          # 01, 1
        "Function_2_1FB",          # 02, 2
        "Function_3_D74",          # 03, 3
        "Function_4_E23",          # 04, 4
    )


    def Function_0_19E(): pass

    label("Function_0_19E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1A8")
    Jump("loc_1CE")

    label("loc_1A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1BE")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)

    label("loc_1BE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6E, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CE")
    SetChrFlags(0x8, 0x10)

    label("loc_1CE")

    Return()

    # Function_0_19E end

    def Function_1_1CF(): pass

    label("Function_1_1CF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EE")
    OP_79(0xFF, 0x2)
    OP_7A(0x8, 0x2)
    OP_7B()
    OP_72(0x3, 0x4)
    OP_72(0x4, 0x4)

    label("loc_1EE")

    OP_64(0x0, 0x1)
    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)
    Return()

    # Function_1_1CF end

    def Function_2_1FB(): pass

    label("Function_2_1FB")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_708")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x419, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x6E, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B8")

    ChrTalk(    #0
        0xFE,
        (
            "嗯……？\x01",
            "哦，是游击士们啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "好久不见。\x01",
            "你们看起来很精神，这就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x101,
        (
            "#1000F好久不见。\x02\x03",

            "不过中央工房\x01",
            "整体都很忙碌呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #3
        0xFE,
        (
            "因为从照明到实验材料，\x01",
            "全都不行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "不过…\x01",
            "那个用枪的人怎么样了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        (
            "#1004F你说奥利维尔？\x02\x03",

            "#1015F那家伙已经\x01",
            "回国了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        "……回国了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "难道\x01",
            "奥利维尔先生是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x102,
        "#1040F嗯，他是外国友人。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #9
        0xFE,
        "是、是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        "嗯，这真是遗憾。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "我还想让他看看\x01",
            "完成了的新型枪呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "不过……\x01",
            "现在也不是时候。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "如果这种现象持续下去的话，\x01",
            "我的研究成果就要被推翻了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        "哈哈，哈哈哈……\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #15
        0x101,
        "#1020F加、加鲁诺先生……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x102,
        "#1048F（看上去一副走投无路的样子……）\x02",
    )

    CloseMessageWindow()
    OP_A2(0x9)
    OP_A2(0x20CF)
    Jump("loc_705")

    label("loc_4B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_5B1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6E, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_533")

    ChrTalk(    #17
        0xFE,
        (
            "如果这种现象持续下去的话\x01",
            "我的研究成果就要被推翻了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        "哈哈，哈哈哈……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        "啊哈哈哈哈……\x02",
    )

    CloseMessageWindow()
    Jump("loc_5AE")

    label("loc_533")


    ChrTalk(    #20
        0xFE,
        (
            "枪不能使用了\x01",
            "确实很打击人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "不过也不能一直\x01",
            "这么消沉下去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "因为一两次挫折就倒下去的话\x01",
            "还谈什么伟大的发明。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5AE")

    Jump("loc_705")

    label("loc_5B1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6E, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_625")

    ChrTalk(    #23
        0xFE,
        (
            "如果这种现象持续下去的话\x01",
            "我的研究成果就要被推翻了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        "哈哈，哈哈哈……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        "啊哈哈哈哈……\x02",
    )

    CloseMessageWindow()
    Jump("loc_705")

    label("loc_625")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A3")

    ChrTalk(    #26
        0xFE,
        (
            "好不容易快要使\x01",
            "新型枪商品化了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        "竟、竟然在这个节骨眼儿上……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "哈哈，好像因为打击\x01",
            "而笑个不停了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_705")

    label("loc_6A3")


    ChrTalk(    #29
        0xFE,
        (
            "好不容易快要使\x01",
            "新型枪商品化了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "竟、竟然在这个节骨眼儿上……\x01",
            "因为受打击而停止研究了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_705")

    Jump("loc_D70")

    label("loc_708")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_716")
    Call(1, 9)
    Jump("loc_D70")

    label("loc_716")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_724")
    Call(1, 11)
    Jump("loc_D70")

    label("loc_724")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_732")
    Call(1, 10)
    Jump("loc_D70")

    label("loc_732")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_78B")

    ChrTalk(    #31
        0xFE,
        (
            "不装备『零式导力枪α』\x01",
            "的话战斗结果是不计算的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        "一定要注意这一点。\x02",
    )

    CloseMessageWindow()
    Jump("loc_D70")

    label("loc_78B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_799")
    Call(1, 8)
    Jump("loc_D70")

    label("loc_799")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_7A7")
    Call(1, 1)
    Jump("loc_D70")

    label("loc_7A7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6E, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x6E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7C0")
    Call(1, 4)
    Jump("loc_D70")

    label("loc_7C0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6E, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x6E, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7EB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6E, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_7E4")
    Call(1, 2)
    Jump("loc_7E8")

    label("loc_7E4")

    Call(1, 0)

    label("loc_7E8")

    Jump("loc_D70")

    label("loc_7EB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6E, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_B14")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_8BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_856")

    ChrTalk(    #33
        0xFE,
        (
            "地震的安全宣言也出来了，\x01",
            "暂时能专注于研究了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "请期待我的\x01",
            "新型导力枪！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8BB")

    label("loc_856")


    ChrTalk(    #35
        0xFE,
        "啊，是你们。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "地震的安全宣言也出来了，\x01",
            "暂时能专注于研究了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "请期待我的\x01",
            "新型导力枪！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_8BB")

    Jump("loc_B11")

    label("loc_8BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_990")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_917")

    ChrTalk(    #38
        0xFE,
        (
            "拉赛尔博士好像\x01",
            "在进行某种实验。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "有空的话我要\x01",
            "不要去看一下啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_98D")

    label("loc_917")


    ChrTalk(    #40
        0xFE,
        "哦，是你们啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "拉赛尔博士好像\x01",
            "在进行某种实验，\x01",
            "你知道具体内容吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "我整理好文件\x01",
            "要不要也去看看呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_98D")

    Jump("loc_B11")

    label("loc_990")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_A41")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_9E4")

    ChrTalk(    #43
        0xFE,
        (
            "你们看上去很忙，\x01",
            "还在进行什么工作吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        "游击士真不容易啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_A3E")

    label("loc_9E4")


    ChrTalk(    #45
        0xFE,
        "哟，是你们啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "你们看上去很忙，\x01",
            "还在进行什么工作吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        "游击士真不容易啊。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_A3E")

    Jump("loc_B11")

    label("loc_A41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_B11")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_AA6")

    ChrTalk(    #48
        0xFE,
        (
            "今天非常感谢。\x01",
            "你们可帮了我大忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "以后再有什么事的话\x01",
            "你们也要帮帮忙啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B11")

    label("loc_AA6")


    ChrTalk(    #50
        0xFE,
        "哟，是你们啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "今天非常感谢。\x01",
            "你们可帮了我大忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "以后再有什么事的话\x01",
            "你们也要帮帮忙啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_B11")

    Jump("loc_D70")

    label("loc_B14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_BDC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_B64")

    ChrTalk(    #53
        0xFE,
        "竟然没有人来应聘……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "难道是应聘资格\x01",
            "定得太严格了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BD9")

    label("loc_B64")


    ChrTalk(    #55
        0xFE,
        "呼，不过真让人感到为难啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "我已经等了很久了，\x01",
            "竟然没有人来应聘……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "难道是应聘资格\x01",
            "定得太严格了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_BD9")

    Jump("loc_D70")

    label("loc_BDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_CA6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_C3E")

    ChrTalk(    #58
        0xFE,
        (
            "呼，终于准备完成了吗？\x01",
            "接下来就是等待应聘的人了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        "那个，没忘记什么吧？\x02",
    )

    CloseMessageWindow()
    Jump("loc_CA3")

    label("loc_C3E")


    ChrTalk(    #60
        0xFE,
        (
            "嗯，导力枪的调整ＯＫ了。\x01",
            "书面手续也弄完了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "好，准备完成。\x01",
            "接下来就是等待应聘的人了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_CA3")

    Jump("loc_D70")

    label("loc_CA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_D70")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_D19")

    ChrTalk(    #62
        0xFE,
        (
            "嗯，导力枪的调整ＯＫ了。\x01",
            "书面手续也弄完了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "好，准备完成。\x01",
            "接下来就是等待应聘的人了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D70")

    label("loc_D19")


    ChrTalk(    #64
        0xFE,
        (
            "呼，真麻烦。\x01",
            "偏偏这种时候来地震了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "都准备好接下来要\x01",
            "进行重要的测试了……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_D70")

    TalkEnd(0x8)
    Return()

    # Function_2_1FB end

    def Function_3_D74(): pass

    label("Function_3_D74")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_E1F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_DC5")

    ChrTalk(    #66
        0x9,
        (
            "#103F怎么？这么关心\x01",
            "我的发明吗？\x02\x03",

            "#101F呵呵，敬请期待。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E1F")

    label("loc_DC5")


    ChrTalk(    #67
        0x9,
        (
            "#100F调查还顺利吗？\x02\x03",

            "我这边的准备\x01",
            "还要有一阵子。\x02\x03",

            "一旦准备妥当\x01",
            "我就会联系协会的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_E1F")

    TalkEnd(0x9)
    Return()

    # Function_3_D74 end

    def Function_4_E23(): pass

    label("Function_4_E23")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_FAE")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EF5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_E8A")

    ChrTalk(    #68
        0xA,
        (
            "#560F这装置一定会\x01",
            "起作用的。\x02\x03",

            "我们会加快速度的，\x01",
            "请再稍微等一等。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EF2")

    label("loc_E8A")


    ChrTalk(    #69
        0xA,
        (
            "#560F啊，阿加特哥哥。\x02\x03",

            "现在在准备的装置\x01",
            "我想一定能帮上忙。\x02\x03",

            "我们会加快速度的，\x01",
            "请再稍微等一等。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_EF2")

    Jump("loc_FAE")

    label("loc_EF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_F48")

    ChrTalk(    #70
        0xA,
        (
            "#060F这个装置\x01",
            "一定会起作用的。\x02\x03",

            "我们会加快速度的，\x01",
            "请再稍微等一等。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FAE")

    label("loc_F48")


    ChrTalk(    #71
        0xA,
        (
            "#060F啊，姐姐是你们。\x02\x03",

            "现在在准备的装置\x01",
            "一定会起作用的。\x02\x03",

            "我们会加快速度的，\x01",
            "请再稍微等一等。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_FAE")

    TalkEnd(0xA)
    Return()

    # Function_4_E23 end

    SaveToFile()

Try(main)
