from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2600   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2600.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60032",
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
        '安敦',                                 # 9
        '利库斯',                               # 10
        '米克',                                 # 11
        '目标用照相机',                         # 12
        '王立学院·小道',                       # 13
        '',                                     # 14
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
        'ED6_DT07/CH02900 ._CH',             # 00
        'ED6_DT26/CH20783 ._CH',             # 01
        'ED6_DT07/CH01080 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT07/CH02900P._CP',             # 00
        'ED6_DT26/CH20783P._CP',             # 01
        'ED6_DT07/CH01080P._CP',             # 02
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x195,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 800,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 170,
        Z                   = 0,
        Y                   = -16239,
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
        TriggerX            = 0,
        TriggerZ            = 1000,
        TriggerY            = 9720,
        TriggerRange        = 800,
        ActorX              = 0,
        ActorZ              = 2000,
        ActorY              = 9720,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_186",          # 00, 0
        "Function_1_24B",          # 01, 1
        "Function_2_270",          # 02, 2
        "Function_3_3ED",          # 03, 3
        "Function_4_411",          # 04, 4
        "Function_5_750",          # 05, 5
        "Function_6_9C9",          # 06, 6
        "Function_7_A90",          # 07, 7
        "Function_8_E3E",          # 08, 8
    )


    def Function_0_186(): pass

    label("Function_0_186")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_1C8")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x10, 200, 500, 4560, 180)
    SetChrPos(0x11, -640, 750, 5900, 180)
    Jump("loc_24A")

    label("loc_1C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_1D2")
    Jump("loc_24A")

    label("loc_1D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_1E1")
    ClearChrFlags(0x12, 0x80)
    Jump("loc_24A")

    label("loc_1E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_217")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x10, 200, 500, 4560, 0)
    SetChrPos(0x11, -640, 750, 5900, 180)
    Jump("loc_24A")

    label("loc_217")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_24A")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x10, 200, 500, 4560, 0)
    SetChrPos(0x11, -550, 750, 5900, 180)

    label("loc_24A")

    Return()

    # Function_0_186 end

    def Function_1_24B(): pass

    label("Function_1_24B")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFE61F0, 0x23004E)
    OP_72(0x1000, 0x0)
    ExitThread()
    OP_71(0x2, 0x0)
    ExitThread()
    OP_71(0x402, 0x0)
    ExitThread()
    Return()

    # Function_1_24B end

    def Function_2_270(): pass

    label("Function_2_270")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_295")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_3D7")

    label("loc_295")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AE")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_3D7")

    label("loc_2AE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C7")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_3D7")

    label("loc_2C7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E0")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_3D7")

    label("loc_2E0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F9")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_3D7")

    label("loc_2F9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_312")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_3D7")

    label("loc_312")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32B")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_3D7")

    label("loc_32B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_344")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_3D7")

    label("loc_344")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35D")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_3D7")

    label("loc_35D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_376")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_3D7")

    label("loc_376")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38F")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_3D7")

    label("loc_38F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A8")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_3D7")

    label("loc_3A8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C1")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_3D7")

    label("loc_3C1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D7")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_3D7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3EC")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_3D7")

    label("loc_3EC")

    Return()

    # Function_2_270 end

    def Function_3_3ED(): pass

    label("Function_3_3ED")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_410")
    OP_8D(0xFE, -1300, 1420, 1300, -1760, 2000)
    Jump("Function_3_3ED")

    label("loc_410")

    Return()

    # Function_3_3ED end

    def Function_4_411(): pass

    label("Function_4_411")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_4FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_455")

    ChrTalk(    #0
        0xFE,
        "现在感觉非常爽朗啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        "早安，太阳！\x02",
    )

    CloseMessageWindow()
    Jump("loc_4F9")

    label("loc_455")


    ChrTalk(    #2
        0xFE,
        (
            "昨天晚上，\x01",
            "我找到了一朵绽放在月光下的小花。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "虽然这么小，\x01",
            "却健康地展开花瓣。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "看到这情景，\x01",
            "仿佛心灵都被洗涤了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        "啊啊，我在烦恼什么呢。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_4F9")

    Jump("loc_74C")

    label("loc_4FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_506")
    Jump("loc_74C")

    label("loc_506")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_510")
    Jump("loc_74C")

    label("loc_510")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_655")
    OP_8C(0xFE, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_56C")

    ChrTalk(    #6
        0xFE,
        (
            "利库斯总是\x01",
            "故意岔开谈话重点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "一定是在心里\x01",
            "嘲笑我吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_652")

    label("loc_56C")


    ChrTalk(    #8
        0xFE,
        "喂，利库斯，你倒是说点什么啊！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        "就这样下去我们没问题吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x11,
        "哎，冷静点安敦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x11,
        (
            "从刚才开始\x01",
            "你说话就语无伦次的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "利库斯总是\x01",
            "像这样岔开话题……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        "这是错误的！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "这样做的话\x01",
            "会变得很差劲的！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_652")

    Jump("loc_74C")

    label("loc_655")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_74C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 6)), scpexpr(EXPR_END)), "loc_748")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_6CF")

    ChrTalk(    #15
        0xFE,
        (
            "我总觉得事情的发展\x01",
            "有点太顺利了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "……唉，如果那时候不入学\x01",
            "就不会有这样的经历了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_745")

    label("loc_6CF")


    ChrTalk(    #17
        0xFE,
        (
            "唉，决定入学的时候\x01",
            "还高兴得跟什么似的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        "我一定是被捉弄了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        "…………被命运玩弄于股掌之中……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_745")

    Jump("loc_74C")

    label("loc_748")

    Call(0, 7)

    label("loc_74C")

    TalkEnd(0xFE)
    Return()

    # Function_4_411 end

    def Function_5_750(): pass

    label("Function_5_750")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_824")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_7D8")

    ChrTalk(    #20
        0xFE,
        (
            "安敦不知道什么时候\x01",
            "就回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "还说着什么\x01",
            "『终于想开了』……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "哈哈，\x01",
            "结果什么都没变嘛。\x02",
        )
    )

    Jump("loc_7D4")

    label("loc_7D4")

    CloseMessageWindow()
    Jump("loc_821")

    label("loc_7D8")


    ChrTalk(    #23
        0xFE,
        "呵啊～…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        "呀，天气真好呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        "今天要做什么呢。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_821")

    Jump("loc_9C5")

    label("loc_824")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_82E")
    Jump("loc_9C5")

    label("loc_82E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_838")
    Jump("loc_9C5")

    label("loc_838")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_8D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_886")

    ChrTalk(    #26
        0xFE,
        "镇定下来啦，安敦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "那样大吵大闹\x01",
            "也不是办法啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8D0")

    label("loc_886")


    ChrTalk(    #28
        0xFE,
        (
            "安敦那家伙\x01",
            "又开始叫唤了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "这么做\x01",
            "也不是办法啊。\x02",
        )
    )

    Jump("loc_8CC")

    label("loc_8CC")

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_8D0")

    Jump("loc_9C5")

    label("loc_8D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_9C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_944")

    ChrTalk(    #30
        0xFE,
        (
            "安敦那家伙\x01",
            "去专攻社会系课程了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "哈哈，我都说那种要背\x01",
            "超多东西的课程还是放弃算了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9C5")

    label("loc_944")


    ChrTalk(    #32
        0xFE,
        "呀，你好像很着急呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        "咦？　在找社会系的人吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        "这么说来，安敦也是社会系的吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        "怎么想他都不适合啊。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_9C5")

    TalkEnd(0xFE)
    Return()

    # Function_5_750 end

    def Function_6_9C9(): pass

    label("Function_6_9C9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_A8C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_A26")

    ChrTalk(    #36
        0xFE,
        (
            "最近感觉好像给艾福托老师\x01",
            "逼得紧紧的呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        "嘁，被盯上了吗……\x02",
    )

    CloseMessageWindow()
    Jump("loc_A8C")

    label("loc_A26")


    ChrTalk(    #38
        0xFE,
        (
            "好久没偷懒了，\x01",
            "正打算放松一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        "可是半路上有艾福托老师在。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        "这样可没法回去啊。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_A8C")

    TalkEnd(0xFE)
    Return()

    # Function_6_9C9 end

    def Function_7_A90(): pass

    label("Function_7_A90")

    EventBegin(0x0)
    OP_8C(0x10, 0, 0)
    Fade(1000)
    SetChrSubChip(0x10, 0)
    OP_6D(1330, 250, 4710, 0)
    OP_67(0, 6320, -10000, 0)
    OP_6B(3190, 0)
    OP_6C(45000, 0)
    OP_6E(252, 0)
    SetChrPos(0x105, 200, 250, 3320, 0)
    Sleep(1000)

    ChrTalk(    #41
        0x10,
        "#11P我说利库斯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x10,
        (
            "#11P我们为什么\x01",
            "会在这种地方呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x10,
        (
            "#11P春天已经来了。\x01",
            "然而我的心却仍留在冬天。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x10,
        (
            "#11P唉，\x01",
            "为什么事事都不顺心呢……\x02",
        )
    )

    Jump("loc_BAC")

    label("loc_BAC")

    CloseMessageWindow()

    ChrTalk(    #45
        0x105,
        (
            "#044F#12P那个～\x01",
            "不好意思……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x10, 180, 400)
    Sleep(300)

    ChrTalk(    #46
        0x10,
        "#5P咦，你是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x10,
        "#5P记得是一年级的插班生吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x10,
        (
            "#5P唉，真羡慕啊～……\x01",
            "像你这么聪明的人。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #49
        0x105,
        (
            "#043F#12P那、那个……\x02\x03",

            "#045F这个是碧欧拉老师\x01",
            "让我发的……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #50
        "\x07\x05把资料交给安敦。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(    #51
        0x10,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x10,
        (
            "#5P我…………\x01",
            "又留级了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x105,
        "#044F#12P哎…………？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x10,
        (
            "#5P又要读一遍三年级了。\x01",
            "唉，真是糟透了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x10,
        (
            "#5P我一年级的时候\x01",
            "也是充满希望的啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x105,
        (
            "#043F#12P那、那个……\x02\x03",

            "#540F（要、要怎么\x01",
            "　安慰他才好呢……）\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2F66)
    EventEnd(0x0)
    Return()

    # Function_7_A90 end

    def Function_8_E3E(): pass

    label("Function_8_E3E")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #57
        "\x07\x05门上了锁。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_8_E3E end

    SaveToFile()

Try(main)
