from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C5503   ._SN',
        MapName             = 'Other',
        Location            = 'C5503.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60031",
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
        '克鲁茨',                               # 9
        '魔兽',                                 # 10
        '魔兽',                                 # 11
        '魔兽',                                 # 12
        '魔兽',                                 # 13
        '目标用照相机',                         # 14
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
        'ED6_DT07/CH01620 ._CH',             # 00
        'ED6_DT29/CH12220 ._CH',             # 01
        'ED6_DT07/CH00410 ._CH',             # 02
        'ED6_DT07/CH00414 ._CH',             # 03
        'ED6_DT07/CH00411 ._CH',             # 04
        'ED6_DT07/CH00100 ._CH',             # 05
        'ED6_DT07/CH00420 ._CH',             # 06
        'ED6_DT29/CH12210 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT07/CH01620P._CP',             # 00
        'ED6_DT29/CH12220P._CP',             # 01
        'ED6_DT07/CH00410P._CP',             # 02
        'ED6_DT07/CH00414P._CP',             # 03
        'ED6_DT07/CH00411P._CP',             # 04
        'ED6_DT07/CH00100P._CP',             # 05
        'ED6_DT07/CH00420P._CP',             # 06
        'ED6_DT29/CH12210P._CP',             # 07
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -13940,
        Z                   = 0,
        Y                   = 19260,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -27580,
        Z                   = 0,
        Y                   = 27680,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -36160,
        Z                   = 0,
        Y                   = 35380,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -36190,
        Z                   = 0,
        Y                   = 46820,
        Direction           = 170,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xC0,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = 7400,
        Y                   = 2500,
        Z                   = 3900,
        Range               = 9700,
        Unknown_10          = 0x1A90,
        Unknown_14          = 0x2008,
        Unknown_18          = 0x0,
        Unknown_1C          = 6,
    )

    DeclEvent(
        X                   = -7750,
        Y                   = 0,
        Z                   = 199430,
        Range               = -4280,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x31ECA,
        Unknown_18          = 0x0,
        Unknown_1C          = 7,
    )

    DeclEvent(
        X                   = -16720,
        Y                   = -1000,
        Z                   = 19250,
        Range               = -11910,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x34EE,
        Unknown_18          = 0x0,
        Unknown_1C          = 10,
    )

    DeclEvent(
        X                   = -24000,
        Y                   = -1000,
        Z                   = 30610,
        Range               = -25500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x634C,
        Unknown_18          = 0x0,
        Unknown_1C          = 12,
    )

    DeclEvent(
        X                   = -38590,
        Y                   = -1000,
        Z                   = 33670,
        Range               = -33820,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x7B0C,
        Unknown_18          = 0x0,
        Unknown_1C          = 14,
    )

    DeclEvent(
        X                   = -38410,
        Y                   = -1000,
        Z                   = 46310,
        Range               = -33920,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xA21C,
        Unknown_18          = 0x0,
        Unknown_1C          = 16,
    )


    DeclActor(
        TriggerX            = 31770,
        TriggerZ            = 200,
        TriggerY            = 202040,
        TriggerRange        = 800,
        ActorX              = 31770,
        ActorZ              = 1200,
        ActorY              = 202040,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -5000,
        TriggerZ            = 0,
        TriggerY            = 6610,
        TriggerRange        = 1600,
        ActorX              = -5000,
        ActorZ              = 1000,
        ActorY              = 6730,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 19,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2B2",          # 00, 0
        "Function_1_2EF",          # 01, 1
        "Function_2_4E9",          # 02, 2
        "Function_3_590",          # 03, 3
        "Function_4_608",          # 04, 4
        "Function_5_B3F",          # 05, 5
        "Function_6_B62",          # 06, 6
        "Function_7_105B",         # 07, 7
        "Function_8_1835",         # 08, 8
        "Function_9_185E",         # 09, 9
        "Function_10_18A4",        # 0A, 10
        "Function_11_1C1C",        # 0B, 11
        "Function_12_1C84",        # 0C, 12
        "Function_13_21CF",        # 0D, 13
        "Function_14_2237",        # 0E, 14
        "Function_15_24CA",        # 0F, 15
        "Function_16_2532",        # 10, 16
        "Function_17_270E",        # 11, 17
        "Function_18_2776",        # 12, 18
        "Function_19_29EA",        # 13, 19
    )


    def Function_0_2B2(): pass

    label("Function_0_2B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x201, 1)), scpexpr(EXPR_END)), "loc_2DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x201, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DE")
    SetChrPos(0x8, -770, 0, 7450, 170)
    ClearChrFlags(0x8, 0x80)
    OP_43(0x8, 0x0, 0x0, 0x2)

    label("loc_2DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x201, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x201, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2EE")
    Event(0, 4)

    label("loc_2EE")

    Return()

    # Function_0_2B2 end

    def Function_1_2EF(): pass

    label("Function_1_2EF")

    OP_22(0x1C7, 0x0, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22C, 0)), scpexpr(EXPR_END)), "loc_300")
    SetChrFlags(0x9, 0x80)

    label("loc_300")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22C, 1)), scpexpr(EXPR_END)), "loc_30C")
    SetChrFlags(0xA, 0x80)

    label("loc_30C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22C, 2)), scpexpr(EXPR_END)), "loc_318")
    SetChrFlags(0xB, 0x80)

    label("loc_318")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22C, 3)), scpexpr(EXPR_END)), "loc_324")
    SetChrFlags(0xC, 0x80)

    label("loc_324")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_373")
    Call(0, 8)
    SetChrPos(0x0, -13990, 50, 12500, 0)
    SetChrPos(0x1, -13990, 50, 12500, 0)
    OP_30(0x0)
    OP_69(0x101, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_373")
    OP_A2(0x1160)
    SetChrFlags(0x9, 0x80)

    label("loc_373")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C2")
    Call(0, 8)
    SetChrPos(0x0, -23500, 0, 28000, 270)
    SetChrPos(0x1, -23500, 0, 28000, 270)
    OP_30(0x0)
    OP_69(0x101, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C2")
    OP_A2(0x1161)
    SetChrFlags(0xA, 0x80)

    label("loc_3C2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_411")
    Call(0, 8)
    SetChrPos(0x0, -36130, 0, 28500, 0)
    SetChrPos(0x1, -36130, 0, 28500, 0)
    OP_30(0x0)
    OP_69(0x101, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_411")
    OP_A2(0x1162)
    SetChrFlags(0xB, 0x80)

    label("loc_411")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_460")
    Call(0, 8)
    SetChrPos(0x0, -36010, 0, 40500, 0)
    SetChrPos(0x1, -36010, 0, 40500, 0)
    OP_30(0x0)
    OP_69(0x101, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_460")
    OP_A2(0x1163)
    SetChrFlags(0xC, 0x80)

    label("loc_460")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x201, 1)), scpexpr(EXPR_END)), "loc_46A")
    OP_10(0x0, 0x0)

    label("loc_46A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4D5")
    LoadEffect(0x0, "map\\\\mp027_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, -5000, 1000, 6730, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    OP_72(0x2, 0x20)
    OP_6F(0x2, 0)
    OP_70(0x2, 0x0)
    Jump("loc_4E8")

    label("loc_4D5")

    OP_72(0x2, 0x20)
    OP_6F(0x2, 0)
    OP_70(0x2, 0x0)

    label("loc_4E8")

    Return()

    # Function_1_2EF end

    def Function_2_4E9(): pass

    label("Function_2_4E9")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_51A"),
        (1, "loc_526"),
        (2, "loc_532"),
        (3, "loc_53E"),
        (4, "loc_54A"),
        (5, "loc_556"),
        (6, "loc_562"),
        (SWITCH_DEFAULT, "loc_56E"),
    )


    label("loc_51A")

    OP_99(0xFE, 0x0, 0x7, 0x5AA)
    Jump("loc_57A")

    label("loc_526")

    OP_99(0xFE, 0x0, 0x7, 0x60E)
    Jump("loc_57A")

    label("loc_532")

    OP_99(0xFE, 0x0, 0x7, 0x640)
    Jump("loc_57A")

    label("loc_53E")

    OP_99(0xFE, 0x0, 0x7, 0x578)
    Jump("loc_57A")

    label("loc_54A")

    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_57A")

    label("loc_556")

    OP_99(0xFE, 0x0, 0x7, 0x546)
    Jump("loc_57A")

    label("loc_562")

    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_57A")

    label("loc_56E")

    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_57A")

    label("loc_57A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_58F")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_57A")

    label("loc_58F")

    Return()

    # Function_2_4E9 end

    def Function_3_590(): pass

    label("Function_3_590")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E9")

    ChrTalk(    #0
        0x8,
        (
            "#840F你们两个怎么了？\x02\x03",

            "想恢复体力的时候，\x01",
            "就利用那里的回复装置吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_604")

    label("loc_5E9")


    ChrTalk(    #1
        0x8,
        "#840F那么，祝你好运。\x02",
    )

    CloseMessageWindow()

    label("loc_604")

    TalkEnd(0x8)
    Return()

    # Function_3_590 end

    def Function_4_608(): pass

    label("Function_4_608")

    EventBegin(0x0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x10A, 0x80)
    OP_6D(-13420, 0, 6250, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    def lambda_657():
        OP_6D(150, 0, 5990, 5000)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_657)
    OP_C8(0x200, 0x46, "C_PLAC02._CH", 0x0, 0x3E8)
    FadeToBright(1000, 0)
    Sleep(300)
    SetChrPos(0x8, 7310, 3250, 6000, 270)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x40)

    def lambda_6AD():
        OP_8E(0x8, 0xFFFFFCE0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_6AD)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8)
    SetChrPos(0xD, 7310, 3250, 6000, 270)
    Sleep(500)

    def lambda_6E8():
        OP_8E(0xD, 0x8C, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_6E8)

    def lambda_703():

        label("loc_703")

        OP_69(0xD, 0x0)
        OP_48()
        Jump("loc_703")

    QueueWorkItem2(0xD, 3, lambda_703)
    Sleep(1000)
    SetChrPos(0x101, 7230, 3000, 5320, 270)
    SetChrPos(0x10A, 7230, 3250, 6550, 270)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x10A, 0x80)

    def lambda_745():
        OP_8E(0x10A, 0x438, 0x0, 0x1996, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_745)
    Sleep(500)

    def lambda_765():
        OP_8E(0x101, 0x44C, 0x0, 0x14C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_765)
    WaitChrThread(0x8, 0x1)
    OP_44(0xD, 0x3)
    OP_8C(0x8, 90, 1000)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #2
        0x101,
        "#4P#1002F这里就是『巴斯塔尔水道』……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x10A,
        (
            "#5P#812F看来是相当大的\x01",
            "地下水道呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "#6P#843F虽然比不上王都的地下水道，\x01",
            "但还是十分宽敞呢。\x02\x03",

            "#840F今天的演习，就是回收存放在\x01",
            "水道最深处的机密文件。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        "#4P#1004F机、机密文件？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "#6P#840F哈哈，这纯粹是\x01",
            "演习的预定内容。\x02\x03",

            "总之到达水路的最深处\x01",
            "应该就能够找到目标文件。\x02\x03",

            "将它回收之后，演习就结束了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x10A,
        (
            "#5P#816F嗯～听起来\x01",
            "倒是相当简单……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        (
            "#4P#1006F既然说是演习的话，\x01",
            "一定准备了各式各样的东西吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        (
            "#6P#843F嗯，这就任凭各位想象了。\x02\x03",

            "#842F顺带一提，四处游荡的魔兽\x01",
            "确实是相当难对付。\x02\x03",

            "也许会使用到\x01",
            "『连锁战技』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x101,
        "#4P#1004F说到『连锁战技』……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x10A,
        (
            "#5P#812F就是来到这里后特训的绝招，\x01",
            "和同伴们一起进行的协力攻击吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        (
            "#6P#840F没错，是多位同伴\x01",
            "可以同时攻击敌人的战技。\x02\x03",

            "机会难得，\x01",
            "就在这次演习中试试看吧。\x02\x03",
        )
    )
    
    CloseMessageWindow()

    ChrTalk(    #900
        0x101,
        "#4P#1006F嗯，知道了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #901
        0x8,
        (
            "#6P#840F另外，如果受了伤就不要勉强，\x01",
            "先选择撤退吧。\x02\x03",

            "为了慎重起见，\x01",
            "也准备了导力器的恢复装置。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x101,
        (
            "#4P#1006F哈哈，真不愧是克鲁茨先生。\x01",
            "万事周到呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10A,
        (
            "#5P#810F嗯，我们也要好好回应期待才行。\x02",

            "#5P#816F那么我们出发了！\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x8, 0x1, 0x0, 0x5)
    OP_10(0x0, 0x0)
    OP_A2(0x1009)
    OP_28(0x7E, 0x4, 0x2)
    OP_28(0x7E, 0x4, 0x8)
    OP_28(0x7E, 0x1, 0x80)
    ClearChrFlags(0x8, 0x40)
    EventEnd(0x0)
    Return()

    # Function_4_608 end

    def Function_5_B3F(): pass

    label("Function_5_B3F")

    OP_8E(0x8, 0xFFFFFCFE, 0x0, 0x1D1A, 0x7D0, 0x0)
    OP_8C(0x8, 170, 500)
    OP_43(0x8, 0x0, 0x0, 0x2)
    Return()

    # Function_5_B3F end

    def Function_6_B62(): pass

    label("Function_6_B62")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x204, 2)), scpexpr(EXPR_END)), "loc_B80")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B91")

    label("loc_B80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x202, 2)), scpexpr(EXPR_END)), "loc_B91")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B91")

    SetMapFlags(0x80)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS137._CH")
    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_C6(0x0, 0x3, -1, 500, 0)
    OP_C7(0x0, 0x0, 0x3)
    OP_77(0x0, 0x0, 0x0, 0x0, 0x0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C02")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F1F")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_C2D"),
        (1, "loc_C59"),
        (2, "loc_C96"),
        (SWITCH_DEFAULT, "loc_CE8"),
    )


    label("loc_C2D")


    Menu(
        0,
        30,
        80,
        0,
        (
            "【训练场宿舍】\x01",        # 0
            "【巴斯塔尔水道】\x01",      # 1
        )
    )

    Jump("loc_CE8")

    label("loc_C59")


    Menu(
        0,
        30,
        80,
        0,
        (
            "【训练场宿舍】\x01",        # 0
            "【巴斯塔尔水道】\x01",      # 1
            "【圣科洛瓦森林】\x01",      # 2
        )
    )

    Jump("loc_CE8")

    label("loc_C96")


    Menu(
        0,
        30,
        80,
        0,
        (
            "【训练场宿舍】\x01",            # 0
            "【巴斯塔尔水道】\x01",          # 1
            "【圣科洛瓦森林】\x01",          # 2
            "【格林姆瑟尔小要塞】\x01",      # 3
        )
    )

    Jump("loc_CE8")

    label("loc_CE8")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_D12"),
        (1, "loc_D92"),
        (2, "loc_E14"),
        (3, "loc_E96"),
        (SWITCH_DEFAULT, "loc_F1C"),
    )


    label("loc_D12")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #15
        "\x07\x05要移动至【训练场宿舍】吗？\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_D7F"),
        (1, "loc_D8C"),
        (SWITCH_DEFAULT, "loc_D8F"),
    )


    label("loc_D7F")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D8F")

    label("loc_D8C")

    Jump("loc_D8F")

    label("loc_D8F")

    Jump("loc_F1C")

    label("loc_D92")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #16
        "\x07\x05要移动至【巴斯塔尔水道】吗？\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_E01"),
        (1, "loc_E0E"),
        (SWITCH_DEFAULT, "loc_E11"),
    )


    label("loc_E01")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E11")

    label("loc_E0E")

    Jump("loc_E11")

    label("loc_E11")

    Jump("loc_F1C")

    label("loc_E14")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #17
        "\x07\x05要移动至【圣科洛瓦森林】吗？\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_E83"),
        (1, "loc_E90"),
        (SWITCH_DEFAULT, "loc_E93"),
    )


    label("loc_E83")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E93")

    label("loc_E90")

    Jump("loc_E93")

    label("loc_E93")

    Jump("loc_F1C")

    label("loc_E96")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #18
        "\x07\x05要移动至【格林姆瑟尔小要塞】吗？\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_F09"),
        (1, "loc_F16"),
        (SWITCH_DEFAULT, "loc_F19"),
    )


    label("loc_F09")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F19")

    label("loc_F16")

    Jump("loc_F19")

    label("loc_F19")

    Jump("loc_F1C")

    label("loc_F1C")

    Jump("loc_C02")

    label("loc_F1F")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_F38"),
        (1, "loc_F6C"),
        (2, "loc_FA0"),
        (3, "loc_FD4"),
        (SWITCH_DEFAULT, "loc_1008"),
    )


    label("loc_F38")

    OP_C6(0x0, 0x0, -640000, 0, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_1008")

    label("loc_F6C")

    OP_C6(0x0, 0x0, -358000, -37000, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_1008")

    label("loc_FA0")

    OP_C6(0x0, 0x0, -362000, -266000, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_1008")

    label("loc_FD4")

    OP_C6(0x0, 0x0, -64000, -340000, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_1008")

    label("loc_1008")

    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_102A"),
        (1, "loc_1036"),
        (2, "loc_1042"),
        (3, "loc_104E"),
        (SWITCH_DEFAULT, "loc_105A"),
    )


    label("loc_102A")

    NewScene("ED6_DT21/T5100   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_105A")

    label("loc_1036")

    NewScene("ED6_DT21/C5503   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_105A")

    label("loc_1042")

    NewScene("ED6_DT21/C5507   ._SN", 101, 0, 0)
    IdleLoop()
    Jump("loc_105A")

    label("loc_104E")

    NewScene("ED6_DT21/C5508   ._SN", 101, 0, 0)
    IdleLoop()
    Jump("loc_105A")

    label("loc_105A")

    Return()

    # Function_6_B62 end

    def Function_7_105B(): pass

    label("Function_7_105B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x201, 3)), scpexpr(EXPR_END)), "loc_1063")
    Return()

    label("loc_1063")

    EventBegin(0x0)
    SetChrPos(0x8, 10060, 0, 201910, 270)
    OP_44(0x8, 0x0)
    SetChrSubChip(0x8, 0)

    NpcTalk(    #19
        0x8,
        "男人的声音",
        "呵，总算来了吗。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x8, 1000)
    TurnDirection(0x10A, 0x8, 1000)

    def lambda_10E7():
        OP_6D(8550, 0, 201870, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_10E7)

    def lambda_10FF():
        OP_67(0, 6500, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10FF)

    def lambda_1117():
        OP_6C(89000, 2000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1117)

    def lambda_1127():
        OP_6B(3150, 2000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1127)
    Sleep(2000)
    SetChrPos(0x10A, -3580, 0, 200950, 90)
    SetChrPos(0x101, -3660, 0, 202230, 90)

    def lambda_115E():
        OP_8E(0x101, 0x18F6, 0x0, 0x31786, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_115E)
    Sleep(200)

    def lambda_117E():
        OP_8E(0x10A, 0x17DE, 0x0, 0x311F0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_117E)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x10A, 0x1)

    ChrTalk(    #20
        0x10A,
        "#814F#4P克、克鲁茨前辈！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x101,
        (
            "#1004F#6P咦，等一下……\x02\x03",

            "你应该在入口处才对，\x01",
            "怎么会先到达这里？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        (
            "#841F其实是有其他捷径的。\x02\x03",

            "在你们解除装置期间，\x01",
            "我就直接来了这里哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        (
            "#1007F#6P受打击了……\x02\x03",

            "#1019F好不容易\x01",
            "辛辛苦苦地解除了装置……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x10A,
        (
            "#812F#4P先、先不说这个了……\x02\x03",

            "这里确实是\x01",
            "地下水路的最深处吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x8,
        "#840F嗯嗯，没错？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x10A,
        (
            "#819F#4P那么……\x01",
            "要回收的机密文件呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x8,
        "#841F呵呵……\x02",
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x8, 2)
    OP_0D()
    Sleep(500)
    OP_62(0x10A, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_1368():
        OP_91(0x101, 0xFFFFFC18, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1368)
    Sleep(100)

    def lambda_1388():
        OP_91(0x10A, 0xFFFFFC18, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_1388)
    WaitChrThread(0x10A, 0x1)
    WaitChrThread(0x101, 0x2)
    Sleep(200)

    ChrTalk(    #28
        0x101,
        "#1020F#6P咦！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x10A,
        "#1316F#4P果、果然……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x8,
        (
            "#845F你们就把我当成是来抢夺\x01",
            "机密文件的某国武装工作人员吧。\x02\x03",

            "当然，对于目的相同的人\x01",
            "都要以实力加以排除。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        "#1005F#6P你、你说什么～！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x10A,
        (
            "#815F#4P机密文件不过是借口……\x02\x03",

            "真正的演习课题，是在探索中\x01",
            "出乎预料的交战吧！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x8,
        (
            "#841F呵呵，就是这么回事。\x02\x03",

            "#846F那么……\x01",
            "我就先下手了！\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x8, 0x1)
    Battle(0x393, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_151A"),
        (SWITCH_DEFAULT, "loc_151F"),
    )


    label("loc_151A")

    OP_B4(0x0)
    Jump("loc_151F")

    label("loc_151F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x1)
    OP_44(0x8, 0x0)
    OP_6C(45000, 0)
    SetChrPos(0x8, 10060, 0, 201910, 270)
    SetChrFlags(0x8, 0x800)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 3)
    SetChrSubChip(0x8, 3)
    SetChrPos(0x101, 6350, 0, 202970, 92)
    SetChrChipByIndex(0x101, 5)
    SetChrPos(0x10A, 6350, 0, 200970, 92)
    SetChrChipByIndex(0x10A, 6)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #34
        0x8,
        (
            "#843F哎呀哎呀……\x01",
            "本来不打算手下留情的。\x02\x03",

            "看来是我输了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        (
            "#1003F呼呼……\x02\x03",

            "我们……赢了……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x10A,
        (
            "#813F#6P嗯、嗯……\x02\x03",

            "不愧是『方术使』……\x01",
            "两个人联手好不容易才能赢……\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #37
        0x8,
        (
            "#841F好了……\x01",
            "使得工作人员丧失战斗力后，\x01",
            "你们回收了机密文件。\x02\x03",

            "此次的演习到此结束。\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 65535)
    Sleep(100)
    SetChrChipByIndex(0x10A, 65535)
    OP_0D()
    Sleep(400)

    ChrTalk(    #38
        0x101,
        "#1011F那、那今天的训练……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x10A,
        "#1310F#6P就到此结束了吗……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x8,
        (
            "#840F哈哈，怎么可能。\x02\x03",

            "回到宿舍吃完午餐后，\x01",
            "再去南边的『圣科洛瓦森林』。\x02\x03",

            "要修正演习中值得反省的地方，\x01",
            "必须继续接受充分的训练啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x10A, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #41
        0x101,
        "#1007F哎～……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x10A,
        (
            "#1316F#6P克鲁茨前辈……\x01",
            "真是一点也不留情面啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x9C4)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    NewScene("ED6_DT21/T5101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_105B end

    def Function_8_1835(): pass

    label("Function_8_1835")

    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    OP_51(0x0, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    Return()

    # Function_8_1835 end

    def Function_9_185E(): pass

    label("Function_9_185E")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #43
        "\x07\x05门上着锁。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_9_185E end

    def Function_10_18A4(): pass

    label("Function_10_18A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22C, 0)), scpexpr(EXPR_END)), "loc_18AC")
    Return()

    label("loc_18AC")

    EventBegin(0x0)
    TurnDirection(0x0, 0x9, 0)
    TurnDirection(0x1, 0x9, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_18CA")
    Call(0, 11)
    Jump("loc_1C19")

    label("loc_18CA")

    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #44
        0x101,
        "#1002F啊，马上就出现了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x10A,
        (
            "#810F嗯，用来小试身手\x01",
            "再适合不过了。\x02\x03",

            "好久没实战了，想一边确认\x01",
            "战斗方法的同时并进行战斗……\x02\x03",

            "怎么办？艾丝蒂尔。\x02\x03",

            "从基础开始全部复习一遍？\x01",
            "还是只确认连锁战技？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "【从基础开始复习】\x01",      # 0
            "【只确认连锁战技】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    TurnDirection(0x101, 0x10A, 400)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1A1C"),
        (1, "loc_1AC0"),
        (SWITCH_DEFAULT, "loc_1B5A"),
    )


    label("loc_1A1C")


    ChrTalk(    #46
        0x101,
        (
            "#1015F嗯～为了保险起见，\x01",
            "我还是想从基础开始。\x02\x03",

            "正如亚妮拉丝所说的一样，\x01",
            "好久没跟魔兽战斗了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x10A,
        (
            "#816F嗯！明白了。\x02\x03",

            "那么走吧，艾丝蒂尔！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x101,
        "#1018F好！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B5A")

    label("loc_1AC0")

    OP_A2(0x1064)

    ChrTalk(    #49
        0x101,
        (
            "#1015F我只想确认\x01",
            "连锁战技。\x02\x03",

            "毕竟想早点试试\x01",
            "练习过的连锁战技……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x10A,
        (
            "#816F嗯！明白了。\x02\x03",

            "那么，就去把这里的魔兽\x01",
            "统统都踹飞吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x101,
        "#1018F好！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B5A")

    label("loc_1B5A")

    OP_59()
    OP_A2(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 4)), scpexpr(EXPR_END)), "loc_1C15")
    OP_A2(0x1160)
    OP_A2(0x1161)
    OP_A2(0x1162)
    FadeToDark(1000, 0, -1)

    def lambda_1B7E():
        OP_69(0x9, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1B7E)

    def lambda_1B8C():
        OP_8E(0x0, 0xFFFFC9B4, 0x0, 0x4A24, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_1B8C)

    def lambda_1BA7():
        OP_8E(0x1, 0xFFFFC9B4, 0x0, 0x4A24, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_1BA7)
    OP_0D()
    OP_44(0x0, 0x1)
    OP_44(0x0, 0x0)
    OP_44(0x1, 0x0)
    SetChrPos(0x0, -36020, 0, 38300, 0)
    SetChrPos(0x1, -36020, 0, 38300, 0)
    OP_69(0x0, 0x0)
    OP_4A(0x0, 0)
    OP_4A(0x1, 0)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Sleep(4000)
    Call(0, 18)
    Jump("loc_1C19")

    label("loc_1C15")

    Call(0, 11)

    label("loc_1C19")

    EventEnd(0x3)
    Return()

    # Function_10_18A4 end

    def Function_11_1C1C(): pass

    label("Function_11_1C1C")

    OP_59()

    def lambda_1C23():
        OP_69(0x9, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1C23)

    def lambda_1C31():
        OP_8E(0x0, 0xFFFFC9B4, 0x0, 0x4A24, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_1C31)

    def lambda_1C4C():
        OP_8E(0x1, 0xFFFFC9B4, 0x0, 0x4A24, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_1C4C)
    Sleep(300)
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    Battle(0x11, 0x0, 0x0, 0x0, 0xFF)
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    Return()

    # Function_11_1C1C end

    def Function_12_1C84(): pass

    label("Function_12_1C84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22C, 1)), scpexpr(EXPR_END)), "loc_1C8C")
    Return()

    label("loc_1C8C")

    EventBegin(0x0)
    TurnDirection(0x0, 0xA, 0)
    TurnDirection(0x1, 0xA, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1E44")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B9(0x0, 0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_B9(0x9, 0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_B9(0x0, 0x14)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_B9(0x9, 0x14)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_B9(0x0, 0x1E)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_B9(0x9, 0x1E)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_B9(0x0, 0x32)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_B9(0x9, 0x32)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_B9(0x0, 0x41)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_B9(0x9, 0x41)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1DD4")

    ChrTalk(    #52
        0x10A,
        (
            "#814F艾丝蒂尔。\x01",
            "准备好攻击魔法了吗？\x02\x03",

            "#810F前进之前要先\x01",
            "设定好结晶回路哦。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #53
        (
            "\x07\x05※结晶回路的设置在[Orbment]画面进行。\x01",
            "  要打开[Orbment]画面，\x01",
            "  请在整备画面中点选[Orbment]栏。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_59()
    OP_A2(0x1)
    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    EventEnd(0x0)
    Return()

    label("loc_1DD4")


    ChrTalk(    #54
        0x10A,
        (
            "#810F对付武器难以伤害的敌人，\x01",
            "魔法就很有效了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x101,
        (
            "#1006FＯＫ。\x01",
            "用魔法就行了吧。\x02\x03",

            "好，那么上吧。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 13)
    Jump("loc_21CC")

    label("loc_1E44")

    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #56
        0x101,
        "#1002F来了，是增援啊。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B9(0x0, 0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_B9(0x9, 0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_B9(0x0, 0x14)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_B9(0x9, 0x14)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_B9(0x0, 0x1E)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_B9(0x9, 0x1E)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_B9(0x0, 0x32)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_B9(0x9, 0x32)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_B9(0x0, 0x41)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_B9(0x9, 0x41)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2047")

    ChrTalk(    #57
        0x10A,
        (
            "#1316F这只魔兽软绵绵的，\x01",
            "武器应该很难起作用吧。\x02\x03",

            "#812F基本上这种时候\x01",
            "就要使用魔法……\x02\x03",

            "艾丝蒂尔。\x01",
            "准备好攻击魔法了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x101,
        (
            "#1015F嗯～这个嘛……\x02\x03",

            "还是先确认一下\x01",
            "导力器比较好吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0x101, 400)

    ChrTalk(    #59
        0x10A,
        (
            "#810F了解，设定好\x01",
            "结晶回路后再前进吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #60
        (
            "\x07\x05※结晶回路的设置在[Orbment]画面进行。\x01",
            "  要打开[Orbment]画面，\x01",
            "  请在整备画面中点选[Orbment]栏。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_59()
    OP_A2(0x1)
    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    EventEnd(0x0)
    Return()

    label("loc_2047")


    ChrTalk(    #61
        0x10A,
        (
            "#1316F这只魔兽软绵绵的，\x01",
            "武器应该很难起作用吧。\x02\x03",

            "#810F对付这种敌人，\x01",
            "魔法的攻击很有效。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        (
            "#1006FＯＫ。\x01",
            "用魔法就行了吧。\x02\x03",

            "好，那么上吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #63
        (
            "\x07\x05※对于普通攻击无效的敌人，魔法是很有效的。\x01",
            "  魔法可以进行长距离攻击，\x01",
            "  但发动之前需要花费时间（驱动时间）。\x02\x03",

            "※使用魔法的话会消耗ＥＰ。\x01",
            "  ＥＰ可在酒馆·饭店·回复点等地休息，\x01",
            "  或者使用ＥＰ填充剂等道具来回复。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_59()
    OP_A2(0x1)
    Call(0, 13)

    label("loc_21CC")

    EventEnd(0x3)
    Return()

    # Function_12_1C84 end

    def Function_13_21CF(): pass

    label("Function_13_21CF")

    OP_59()

    def lambda_21D6():
        OP_69(0xA, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_21D6)

    def lambda_21E4():
        OP_8E(0x0, 0xFFFF9AD4, 0x0, 0x6CDE, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_21E4)

    def lambda_21FF():
        OP_8E(0x1, 0xFFFF9AD4, 0x0, 0x6CDE, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_21FF)
    Sleep(300)
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    Battle(0x12, 0x0, 0x0, 0x0, 0xFF)
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    Return()

    # Function_13_21CF end

    def Function_14_2237(): pass

    label("Function_14_2237")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22C, 2)), scpexpr(EXPR_END)), "loc_223F")
    Return()

    label("loc_223F")

    EventBegin(0x0)
    TurnDirection(0x0, 0xB, 0)
    TurnDirection(0x1, 0xB, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_225D")
    Call(0, 15)
    Jump("loc_24C7")

    label("loc_225D")

    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #64
        0x101,
        "#1007F呼，又出现了呢。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0x101, 400)

    ChrTalk(    #65
        0x10A,
        (
            "#816F艾丝蒂尔，\x01",
            "这次使用战技看看吧。\x02\x03",

            "战技不仅仅是攻击，\x01",
            "还有着各式各样的效果。\x02\x03",

            "如果ＣＰ在１００以上的话，\x01",
            "就能使用更强力的Ｓ战技哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10A, 400)

    ChrTalk(    #66
        0x101,
        (
            "#1011F原来如此……\x02\x03",

            "要扩大战术的幅度，\x01",
            "战技是不可或缺的呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x10A,
        (
            "#816FＳ战技可作为\x01",
            "Ｓ爆发技来使用，\x01",
            "这可是战斗的关键呢。\x02\x03",

            "关于Ｓ爆发技的使用法，\x01",
            "在战斗中复习看看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x101,
        (
            "#1006F嗯！\x01",
            "拜托你了，亚妮拉丝！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #69
        (
            "\x07\x05※战技的射程虽有限制，但可以立即发动。\x01",
            "  使用战技时所需的ＣＰ，在攻击和受到伤害\x01",
            "  的时候会自然积蓄。\x02\x03",

            "※当ＣＰ超过１００时\x01",
            "　就能使用强力的战技：\x01",
            "　Ｓ战技和Ｓ爆发技。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_A2(0x2)
    Call(0, 15)

    label("loc_24C7")

    EventEnd(0x3)
    Return()

    # Function_14_2237 end

    def Function_15_24CA(): pass

    label("Function_15_24CA")

    OP_59()

    def lambda_24D1():
        OP_69(0xB, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_24D1)

    def lambda_24DF():
        OP_8E(0x0, 0xFFFF72E8, 0x0, 0x83A4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_24DF)

    def lambda_24FA():
        OP_8E(0x1, 0xFFFF72E8, 0x0, 0x83A4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_24FA)
    Sleep(300)
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    Battle(0x13, 0x0, 0x0, 0x0, 0xFF)
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    Return()

    # Function_15_24CA end

    def Function_16_2532(): pass

    label("Function_16_2532")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22C, 3)), scpexpr(EXPR_END)), "loc_253A")
    Return()

    label("loc_253A")

    EventBegin(0x0)
    TurnDirection(0x0, 0xC, 0)
    TurnDirection(0x1, 0xC, 0)
    OP_35(0x0, 0x8C)
    OP_35(0x9, 0x8C)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_25C5")

    ChrTalk(    #70
        0x10A,
        (
            "#810F有机会的话\x01",
            "就试试连锁战技吧。\x02\x03",

            "既然是新的攻击，\x01",
            "就想早点试试看呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x101,
        "#1006F嗯，明白了。\x02",
    )

    CloseMessageWindow()
    Call(0, 17)
    Jump("loc_270B")

    label("loc_25C5")


    ChrTalk(    #72
        0x101,
        "#1011F这条通道到尽头了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x10A,
        (
            "#810F看来是的……\x02\x03",

            "……艾丝蒂尔。\x01",
            "要不要试试那个？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10A, 400)

    ChrTalk(    #74
        0x101,
        (
            "#1011F#3P那个是…………\x02\x03",

            "#1018F啊，连锁战技吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0x101, 400)

    ChrTalk(    #75
        0x10A,
        (
            "#1310F嘿嘿，好不容易才特训出的\x01",
            "全新联合攻击嘛。\x02\x03",

            "为了要抓住感觉，\x01",
            "必须早点在实战中尝试才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x101,
        (
            "#1006F#3P那么，有机会\x01",
            "就试试看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x10A,
        "#810F嗯！拜托你了！\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_A2(0x3)
    Call(0, 17)

    label("loc_270B")

    EventEnd(0x3)
    Return()

    # Function_16_2532 end

    def Function_17_270E(): pass

    label("Function_17_270E")

    OP_59()

    def lambda_2715():
        OP_69(0xC, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2715)

    def lambda_2723():
        OP_8E(0x0, 0xFFFF728E, 0x0, 0xB6B2, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_2723)

    def lambda_273E():
        OP_8E(0x1, 0xFFFF728E, 0x0, 0xB6B2, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_273E)
    Sleep(300)
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    Battle(0x10, 0x0, 0x0, 0x0, 0xFF)
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    Return()

    # Function_17_270E end

    def Function_18_2776(): pass

    label("Function_18_2776")

    EventBegin(0x0)
    OP_6D(-26300, 0, 26230, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(11000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -36520, 0, 36440, 0)
    SetChrPos(0xF7, -35650, 0, 35240, 0)

    def lambda_27DD():
        OP_94(0x1, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_27DD)
    Sleep(250)

    def lambda_27F8():
        OP_94(0x1, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_27F8)

    def lambda_280E():
        OP_6D(-36080, 0, 43850, 4500)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_280E)

    def lambda_2826():
        OP_6C(45000, 4500)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_2826)
    FadeToBright(1500, 0)
    OP_0D()
    WaitChrThread(0x0, 0x1)
    WaitChrThread(0x1, 0x1)
    WaitChrThread(0x0, 0x0)
    WaitChrThread(0x1, 0x0)
    Sleep(1000)
    OP_35(0x0, 0x8C)
    OP_35(0x9, 0x8C)

    ChrTalk(    #78
        0x101,
        (
            "#1015F#3P呼，总之\x01",
            "一路把魔兽打败了……\x02\x03",

            "#1011F这条通道也到尽头了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x10A,
        (
            "#810F嗯，似乎是吧……\x02\x03",

            "……对了，艾丝蒂尔。\x01",
            "要不要试试那个？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10A, 400)

    ChrTalk(    #80
        0x101,
        (
            "#1011F#3P那个是…………\x02\x03",

            "#1018F啊，连锁战技吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0x101, 400)

    ChrTalk(    #81
        0x10A,
        (
            "#1310F嘿嘿，因为是专门特训的\x01",
            "全新联合攻击嘛。\x02\x03",

            "为了要抓住感觉，\x01",
            "赶快在实战中试试如何？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x101,
        (
            "#1006F#3P那么，有机会\x01",
            "就试试看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x10A,
        "#816F嗯！　拜托你了！\x02",
    )

    CloseMessageWindow()
    OP_59()

    def lambda_29D0():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_29D0)
    OP_8C(0x101, 0, 400)
    OP_A2(0x3)
    OP_6A(0xFF)
    Call(0, 17)
    Return()

    # Function_18_2776 end

    def Function_19_29EA(): pass

    label("Function_19_29EA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A3B")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #84
        "\x07\x05导力好像停止了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Jump("loc_2BF9")

    label("loc_2A3B")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #85
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BDE")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_82(0x0, 0x2)
    PlayEffect(0x0, 0x0, 0xFF, -5000, 1000, 6730, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    OP_6F(0x2, 0)
    OP_70(0x2, 0x32)
    OP_73(0x2)
    OP_20(0xBB8)
    OP_22(0xC, 0x0, 0x64)
    OP_82(0x0, 0x2)
    LoadEffect(0x1, "map\\\\mp027_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, -5000, 1000, 6730, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0xFF, 0xFE, 0x0)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_82(0x1, 0x2)
    PlayEffect(0x0, 0x0, 0xFF, -5000, 1000, 6730, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    OP_6F(0x2, 0)
    OP_1E()
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_2BDE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2BF8")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_2BF8")

    Return()

    label("loc_2BF9")

    Return()

    # Function_19_29EA end

    SaveToFile()

Try(main)
