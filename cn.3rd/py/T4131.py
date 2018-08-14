from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4131   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4131.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
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
        '卡兰大主教',                           # 9
        '利瓦尔副助祭',                         # 10
        '修女诺雅',                             # 11
        '希丝娜',                               # 12
        '梅',                                   # 13
        '尼尔森',                               # 14
        '艾莉卡博士',                           # 15
        '希德中校',                             # 16
        '',                                     # 17
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
        'ED6_DT07/CH01400 ._CH',             # 00
        'ED6_DT07/CH01670 ._CH',             # 01
        'ED6_DT07/CH01410 ._CH',             # 02
        'ED6_DT07/CH01033 ._CH',             # 03
        'ED6_DT27/CH03970 ._CH',             # 04
        'ED6_DT27/CH03590 ._CH',             # 05
        'ED6_DT07/CH02490 ._CH',             # 06
        'ED6_DT07/CH01660 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT07/CH01400P._CP',             # 00
        'ED6_DT07/CH01670P._CP',             # 01
        'ED6_DT07/CH01410P._CP',             # 02
        'ED6_DT07/CH01033P._CP',             # 03
        'ED6_DT27/CH03970P._CP',             # 04
        'ED6_DT27/CH03590P._CP',             # 05
        'ED6_DT07/CH02490P._CP',             # 06
        'ED6_DT07/CH01660P._CP',             # 07
    )

    DeclNpc(
        X                   = -50,
        Z                   = 1000,
        Y                   = 20410,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 2870,
        Z                   = 1000,
        Y                   = 18870,
        Direction           = 272,
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
        X                   = -7950,
        Z                   = 0,
        Y                   = 1210,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -3190,
        Z                   = 150,
        Y                   = 10800,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x195,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -5220,
        Z                   = 0,
        Y                   = 3260,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -131950,
        Z                   = 0,
        Y                   = 2700,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 200,
        TriggerZ            = 1000,
        TriggerY            = 17890,
        TriggerRange        = 400,
        ActorX              = -50,
        ActorZ              = 2500,
        ActorY              = 20410,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -74990,
        TriggerZ            = 0,
        TriggerY            = 66030,
        TriggerRange        = 800,
        ActorX              = -74990,
        ActorZ              = 1000,
        ActorY              = 66030,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_232",          # 00, 0
        "Function_1_270",          # 01, 1
        "Function_2_27A",          # 02, 2
        "Function_3_27F",          # 03, 3
        "Function_4_3D6",          # 04, 4
        "Function_5_4DF",          # 05, 5
        "Function_6_612",          # 06, 6
        "Function_7_6E5",          # 07, 7
        "Function_8_736",          # 08, 8
        "Function_9_ADF",          # 09, 9
        "Function_10_B27",         # 0A, 10
        "Function_11_123E",        # 0B, 11
        "Function_12_1275",        # 0C, 12
    )


    def Function_0_232(): pass

    label("Function_0_232")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25C")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x15, 0x80)

    label("loc_25C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_26F")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 10)

    label("loc_26F")

    Return()

    # Function_0_232 end

    def Function_1_270(): pass

    label("Function_1_270")

    OP_B1("t4131_n")
    Return()

    # Function_1_270 end

    def Function_2_27A(): pass

    label("Function_2_27A")

    Call(0, 3)
    Return()

    # Function_2_27A end

    def Function_3_27F(): pass

    label("Function_3_27F")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_3B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2F5")

    ChrTalk(    #0
        0x10,
        (
            "有时人们也需要拿出勇气，\x01",
            "回头看看曾经走过的路。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x10,
        (
            "没有什么好怕的。\x01",
            "女神会引导我们的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B4")

    label("loc_2F5")


    ChrTalk(    #2
        0x10,
        "人有时会迷失道路。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x10,
        (
            "然而真正可怕的是\x01",
            "对此事实毫无察觉……\x01",
            "或者故意不去正视。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x10,
        (
            "有时人们也需要拿出勇气，\x01",
            "回头看看曾经走过的路。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x10,
        (
            "没有什么好怕的。\x01",
            "女神会引导我们的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_3B4")

    Jump("loc_3D2")

    label("loc_3B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_3C1")
    Jump("loc_3D2")

    label("loc_3C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_3CB")
    Jump("loc_3D2")

    label("loc_3CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_3D2")

    label("loc_3D2")

    TalkEnd(0x10)
    Return()

    # Function_3_27F end

    def Function_4_3D6(): pass

    label("Function_4_3D6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_4C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_450")

    ChrTalk(    #6
        0xFE,
        "自那之后已经过了五年吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "女神啊，\x01",
            "请赐予所有逝去的人\x01",
            "平静的安息吧…………\x02",
        )
    )

    Jump("loc_44C")

    label("loc_44C")

    CloseMessageWindow()
    Jump("loc_4BD")

    label("loc_450")


    ChrTalk(    #8
        0xFE,
        (
            "百日战役的时候，\x01",
            "这个大圣堂里也收留了很多人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "亚宁堡所守护的王都，\x01",
            "对人们来说是最后的希望。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_4BD")

    Jump("loc_4DB")

    label("loc_4C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_4CA")
    Jump("loc_4DB")

    label("loc_4CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_4D4")
    Jump("loc_4DB")

    label("loc_4D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_4DB")

    label("loc_4DB")

    TalkEnd(0xFE)
    Return()

    # Function_4_3D6 end

    def Function_5_4DF(): pass

    label("Function_5_4DF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_5F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_561")
    OP_8C(0xFE, 270, 0)

    ChrTalk(    #10
        0xFE,
        (
            "啊啊，\x01",
            "一个人真是没法解决啊！\x02",
        )
    )

    Jump("loc_524")

    label("loc_524")

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "修女萝萨在的时候，\x01",
            "我们还能一起整理得井井有条……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F0")

    label("loc_561")


    ChrTalk(    #12
        0xFE,
        (
            "这个大圣堂是利贝尔\x01",
            "最古老的建筑之一哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "它已经在这里矗立了几百年，\x01",
            "并且不断照耀着民众。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        "……因此都打扫一遍也很辛苦……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_5F0")

    Jump("loc_60E")

    label("loc_5F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_5FD")
    Jump("loc_60E")

    label("loc_5FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_607")
    Jump("loc_60E")

    label("loc_607")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_60E")

    label("loc_60E")

    TalkEnd(0xFE)
    Return()

    # Function_5_4DF end

    def Function_6_612(): pass

    label("Function_6_612")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_6C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_663")

    ChrTalk(    #15
        0xFE,
        "啊，都这么晚了！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "要赶快回去\x01",
            "帮忙做饭才行……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C3")

    label("loc_663")


    ChrTalk(    #17
        0xFE,
        "当修女真好啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "大家都心平气和的，\x01",
            "每天向女神祈祷……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        "啊，好向往啊～……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_6C3")

    Jump("loc_6E1")

    label("loc_6C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_6D0")
    Jump("loc_6E1")

    label("loc_6D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_6DA")
    Jump("loc_6E1")

    label("loc_6DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_6E1")

    label("loc_6E1")

    TalkEnd(0xFE)
    Return()

    # Function_6_612 end

    def Function_7_6E5(): pass

    label("Function_7_6E5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_717")

    ChrTalk(    #20
        0xFE,
        (
            "空之女神啊，\x01",
            "请引导我们吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_732")

    label("loc_717")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_721")
    Jump("loc_732")

    label("loc_721")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_72B")
    Jump("loc_732")

    label("loc_72B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_732")

    label("loc_732")

    TalkEnd(0xFE)
    Return()

    # Function_7_6E5 end

    def Function_8_736(): pass

    label("Function_8_736")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_AC0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EB, 1)), scpexpr(EXPR_END)), "loc_89D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_7B1")
    OP_8C(0xFE, 0, 0)

    ChrTalk(    #21
        0xFE,
        "这里就是格兰赛尔大圣堂……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "嗯，\x01",
            "我也感受到了严肃的气氛啊。\x02",
        )
    )

    Jump("loc_7AD")

    label("loc_7AD")

    CloseMessageWindow()
    Jump("loc_89A")

    label("loc_7B1")


    ChrTalk(    #23
        0xFE,
        (
            "我和别人\x01",
            "约在这里见面。\x02",
        )
    )

    Jump("loc_7E0")

    label("loc_7E0")

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "顺便也打算\x01",
            "在利贝尔采访一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "因为利贝尔王国\x01",
            "可是以击退强国埃雷波尼亚\x01",
            "而闻名的啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "其『底蕴』\x01",
            "到底在哪里呢…………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        "呵呵，我很有兴趣。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_89A")

    Jump("loc_ABD")

    label("loc_89D")

    OP_8C(0xFE, 0, 0)

    ChrTalk(    #28
        0xFE,
        "哦，你们是……？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 500)
    Sleep(300)

    ChrTalk(    #29
        0xFE,
        (
            "这脚步声我没听过。\x01",
            "是第一次见面吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x103,
        (
            "#1643F嗯、嗯。\x01",
            "应该是的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x151,
        (
            "#1653F请问，难道说……\x02\x03",

            "#1650F您的眼睛\x01",
            "不方便吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "嗯嗯，正是这样。\x01",
            "我双目完全失明了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "不过……真是有趣的组合啊。\x01",
            "其中一位是游击士吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x151, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #34
        0xFE,
        (
            "哈哈，我知道的。\x01",
            "感觉很像我认识的游击士。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "失去了光芒，\x01",
            "反而能清楚地看到原本看不见的东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x103,
        "#1643F哎～……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x151,
        "#1650F是这样吗……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2F59)

    label("loc_ABD")

    Jump("loc_ADB")

    label("loc_AC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_ACA")
    Jump("loc_ADB")

    label("loc_ACA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_AD4")
    Jump("loc_ADB")

    label("loc_AD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_ADB")

    label("loc_ADB")

    TalkEnd(0xFE)
    Return()

    # Function_8_736 end

    def Function_9_ADF(): pass

    label("Function_9_ADF")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #38
        "\x07\x05门上了锁。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_9_ADF end

    def Function_10_B27(): pass

    label("Function_10_B27")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, 850, 0, 14500, 180)
    OP_4A(0x10, 255)
    SetChrPos(0x10, -360, 0, 14000, 180)
    SetChrFlags(0x109, 0x80)
    SetChrPos(0x109, 840, -250, -3240, 0)
    SetChrPos(0x17, -610, -250, -3250, 0)
    OP_6D(-600, 0, 280, 0)
    OP_67(0, 5520, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(295, 0)
    FadeToBright(2000, 0)
    Sleep(500)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)
    OP_43(0x109, 0x0, 0x0, 0xB)
    OP_43(0x17, 0x0, 0x0, 0xC)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x17, 0x0)
    Sleep(300)

    NpcTalk(    #39
        0x10,
        "老人的声音",
        "#3P哦哦，来得正好。\x02",
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_C44():
        OP_6D(-730, 0, 14290, 4000)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_C44)

    def lambda_C5C():
        OP_67(0, 4300, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_C5C)

    def lambda_C74():
        OP_6B(2800, 4000)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_C74)

    def lambda_C84():
        OP_6E(290, 4000)
        ExitThread()

    QueueWorkItem(0x16, 3, lambda_C84)
    Sleep(300)

    def lambda_C99():
        OP_8E(0xFE, 0x2DA, 0x0, 0x2E18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_C99)
    Sleep(300)

    def lambda_CB9():
        OP_8E(0xFE, 0xFFFFFED4, 0x0, 0x2BC0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_CB9)
    WaitChrThread(0x16, 0x0)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x17, 0x0)

    ChrTalk(    #40
        0x109,
        (
            "#1060F#6P卡兰大主教。\x01",
            "久疏问候了。\x02\x03",

            "#1064F……咦，这位是……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D33():
        OP_6D(-730, 0, 13900, 800)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_D33)
    OP_8E(0x16, 0x28A, 0x0, 0x34BC, 0x5DC, 0x0)
    WaitChrThread(0x16, 0x1)
    Sleep(300)

    NpcTalk(    #41
        0x16,
        "白衣的女性",
        (
            "#1450F#2P嗯～……\x01",
            "比传闻中还年轻呢。\x02\x03",

            "你几岁了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x109,
        (
            "#1064F#6P咦……？\x02\x03",

            "２、２２岁了。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #43
        0x16,
        "白衣的女性",
        (
            "#1457F#2P嗯……比想像的还年轻。\x02\x03",

            "#1452F『星杯骑士团』里\x01",
            "即使这么年轻的人\x01",
            "都能担当要职吗？\x02\x03",

            "『守护骑士』第五位──\x01",
            "凯文·格拉汉姆先生。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #44
        0x109,
        "#1063F#6P………………………………\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #45
        0x16,
        "白衣的女性",
        (
            "#1458F#2P呵呵，脸色变了呢。\x02\x03",

            "#1456F遇到这点小事就动摇，\x01",
            "是不是有点修行不足呢？\x02\x03",

            "还是说，\x01",
            "这种态度也是演技的一环？\x02",
        )
    )

    Jump("loc_F7F")

    label("loc_F7F")

    CloseMessageWindow()

    ChrTalk(    #46
        0x109,
        "#1063F#6P……你，到底是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x17,
        (
            "#703F#6P呼，拉赛尔博士……\x02\x03",

            "#701F还是不要用这种\x01",
            "过于挑衅的言行比较好吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x109,
        "#1064F#6P咦……\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #49
        0x16,
        "白衣的女性",
        "#1832F#2P#3S不·要。#2S\x02",
    )

    CloseMessageWindow()
    Sleep(400)

    NpcTalk(    #50
        0x16,
        "白衣的女性",
        (
            "#1457F#2P因为，\x01",
            "这个人要把我好不容易\x01",
            "弄到的那个东西给拿走不是吗？\x02\x03",

            "#1459F还有，\x01",
            "不要用那个名字叫我。\x02\x03",

            "我可不想被别人以\x01",
            "跟那个老东西一样的方式称呼。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x17,
        "#701F#6P哎呀哎呀……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x109,
        (
            "#1064F#6P拉、拉赛尔……\x02\x03",

            "难不成，\x01",
            "你是提妲的……？\x02",
        )
    )

    Jump("loc_117F")

    label("loc_117F")

    CloseMessageWindow()

    NpcTalk(    #53
        0x16,
        "白衣的女性",
        (
            "#1458F#2P哼哼，\x01",
            "我该说初次见面吗。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    NpcTalk(    #54
        0x16,
        "艾莉卡博士",
        (
            "#1456F#2P我叫艾莉卡。\x01",
            "艾莉卡·拉赛尔。\x02\x03",

            "以后我们就算认识了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    ClearMapFlags(0x2000000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T4145   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_10_B27 end

    def Function_11_123E(): pass

    label("Function_11_123E")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_1254():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1254)
    OP_8E(0xFE, 0x32A, 0x0, 0xFFFFFAA6, 0x7D0, 0x0)
    Return()

    # Function_11_123E end

    def Function_12_1275(): pass

    label("Function_12_1275")

    Sleep(500)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_1290():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1290)
    OP_8E(0xFE, 0xFFFFFDD0, 0x0, 0xFFFFF86C, 0x7D0, 0x0)
    Return()

    # Function_12_1275 end

    SaveToFile()

Try(main)
