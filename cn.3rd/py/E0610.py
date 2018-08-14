from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'E0610   ._SN',
        MapName             = 'Event',
        Location            = 'E0610.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60001",
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
        '强化猎兵',                             # 9
        '强化猎兵',                             # 10
        '强化猎兵',                             # 11
        '基尔巴特',                             # 12
        '目标用照相机',                         # 13
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
        'ED6_DT26/CH20396 ._CH',             # 00
        'ED6_DT26/CH20760 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT26/CH20396P._CP',             # 00
        'ED6_DT26/CH20760P._CP',             # 01
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_15A",          # 00, 0
        "Function_1_198",          # 01, 1
        "Function_2_19E",          # 02, 2
        "Function_3_79D",          # 03, 3
    )


    def Function_0_15A(): pass

    label("Function_0_15A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_197")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_180")
    OP_A3(0x2505)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 3)
    Jump("loc_197")

    label("loc_180")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_197")
    OP_A3(0x2504)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x52), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)

    label("loc_197")

    Return()

    # Function_0_15A end

    def Function_1_198(): pass

    label("Function_1_198")

    OP_22(0x7A, 0x1, 0x46)
    Return()

    # Function_1_198 end

    def Function_2_19E(): pass

    label("Function_2_19E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_24(0x7A, 0x46)
    OP_6D(-72100, 1000, 980, 0)
    OP_67(0, 5680, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(320000, 0)
    OP_6E(262, 0)
    SetChrPos(0x13, -70600, 1200, -160, 270)
    SetChrPos(0x11, -70600, 1200, 2150, 270)
    SetChrPos(0x12, -70600, 1200, -2500, 270)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x4)
    SetChrFlags(0x11, 0x4)
    SetChrFlags(0x12, 0x4)
    SetChrSubChip(0x13, 0)
    SetChrSubChip(0x11, 0)
    SetChrSubChip(0x12, 0)
    SetChrFlags(0x13, 0x2)
    OP_76(0x4, 0x0, 0x1, 0xFFFFFFFA, 0xFFFFFFFD, 0x0, 0x0, 0x0)
    OP_76(0x4, 0x1, 0x1, 0xFFFFFFF8, 0xFFFFFFFB, 0x0, 0x0, 0x0)
    OP_71(0x403, 0x0)
    ExitThread()
    OP_72(0x404, 0x0)
    ExitThread()
    OP_71(0x405, 0x0)
    ExitThread()
    FadeToBright(1500, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #0
        0x12,
        (
            "#6P是帝国莱恩福尔特社\x01",
            "制造的『山猫号』……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x12,
        "#6P是认识的船吗？\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #2
        0x13,
        "青发的猎兵",
        "啊，是老相识了。\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #3
        0x13,
        "青发的猎兵",
        (
            "话说回来……\x01",
            "这个资料，很有意思呢。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #4
        0x13,
        "青发的猎兵",
        (
            "『卡普亚特急便』……\x01",
            "那些空贼们现在\x01",
            "弄起了物流公司呢。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #5
        0x13,
        "青发的猎兵",
        (
            "哎呀哎呀……\x01",
            "还真是小家子气啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x11,
        (
            "哼，不管怎样，\x01",
            "那边好像没什么战斗的意思。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x11,
        "就这样先放着吧。\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #8
        0x13,
        "青发的猎兵",
        (
            "……等等。\x01",
            "忘了我们的任务了吗？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #9
        0x13,
        "青发的猎兵",
        (
            "那不是正适合充当\x01",
            "这次测试的对手吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x12, 0xC8, 1700, 0x2, 0x7, 0x64, 0x1)
    Sleep(50)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x11, 0xC8, 1700, 0x2, 0x7, 0x64, 0x1)
    Sleep(1000)
    SetChrSubChip(0x11, 1)
    Sleep(50)
    SetChrSubChip(0x12, 2)
    Sleep(300)

    ChrTalk(    #10
        0x11,
        (
            "难道……\x01",
            "你想和他们交手？\x02",
        )
    )

    Jump("loc_51F")

    label("loc_51F")

    CloseMessageWindow()

    ChrTalk(    #11
        0x12,
        (
            "#6P不管怎么说，\x01",
            "这次的计划只有测试运行而已。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #12
        0x13,
        "青发的猎兵",
        (
            "哼，就是因为你老说这种话\x01",
            "才一直升不了官。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #13
        0x13,
        "青发的猎兵",
        "对手是王国军的话则另当别论……\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #14
        0x13,
        "青发的猎兵",
        (
            "那些家伙们可没有任何背景。\x01",
            "攻击他们不会冒任何风险。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x11,
        "那、那倒也是……\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #16
        0x13,
        "青发的猎兵",
        (
            "而且『十三工房』\x01",
            "也正期待着精确的实战数据。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #17
        0x13,
        "青发的猎兵",
        (
            "所以我们只会得到表扬，\x01",
            "不用担心被处罚啦。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x11, 0)
    Sleep(300)

    ChrTalk(    #18
        0x11,
        "……明白了，既然你都说到这份上了。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x12, 0)
    Sleep(300)

    ChrTalk(    #19
        0x12,
        "#6P但是，责任你来承担哦。\x02",
    )

    CloseMessageWindow()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_734():

        label("loc_734")

        OP_7C(0x32, 0x32, 0xBB8, 0x3E8)
        OP_48()
        Jump("loc_734")

    QueueWorkItem2(0x10, 3, lambda_734)
    OP_24(0x7A, 0x50)
    Sleep(200)
    OP_24(0x7A, 0x5A)
    Sleep(200)
    OP_24(0x7A, 0x64)
    Sleep(600)

    def lambda_76A():
        OP_6D(-32100, 1000, 980, 3000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_76A)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x2505)
    NewScene("ED6_DT21/E0110   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_19E end

    def Function_3_79D(): pass

    label("Function_3_79D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_24(0x7A, 0x46)
    OP_6D(-72100, 1000, 980, 0)
    OP_67(0, 5680, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(320000, 0)
    OP_6E(262, 0)
    SetChrPos(0x11, -70600, 1200, 2150, 270)
    SetChrPos(0x12, -70600, 1200, -2500, 270)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x11, 0x4)
    SetChrFlags(0x12, 0x4)
    SetChrSubChip(0x11, 0)
    SetChrSubChip(0x12, 0)
    OP_76(0x4, 0x0, 0x1, 0xFFFFFFFA, 0xFFFFFFFD, 0x0, 0x0, 0x0)
    OP_76(0x4, 0x1, 0x1, 0xFFFFFFF8, 0xFFFFFFFB, 0x0, 0x0, 0x0)
    OP_71(0x403, 0x0)
    ExitThread()
    OP_72(0x404, 0x0)
    ExitThread()
    OP_71(0x405, 0x0)
    ExitThread()
    OP_62(0x12, 0xC8, 1500, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x11, 0xC8, 1500, 0x18, 0x1B, 0xFA, 0x0)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    OP_63(0x12)
    OP_63(0x11)
    Sleep(500)
    SetChrSubChip(0x12, 2)
    Sleep(300)

    ChrTalk(    #20
        0x12,
        "#6P……怎么办？要把他回收吗？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x11, 1)
    Sleep(300)

    ChrTalk(    #21
        0x11,
        "哎？啊啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x11,
        "不回收应该没什么关系的吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x12,
        (
            "#6P但是，肯帕雷拉大人\x01",
            "好像挺中意那个家伙呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x11,
        "所以最好还是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x11,
        (
            "更何况，\x01",
            "肯帕雷拉大人的性情又那么特别。\x02",
        )
    )

    Jump("loc_9BB")

    label("loc_9BB")

    CloseMessageWindow()

    ChrTalk(    #26
        0x11,
        (
            "要是如实报告，\x01",
            "他说不定会更高兴呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x12,
        "#6P…………………………\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x12, 0)
    Sleep(500)

    ChrTalk(    #28
        0x12,
        "#6P……说的也是。\x02",
    )

    CloseMessageWindow()
    OP_59()
    SetChrSubChip(0x11, 0)
    Sleep(300)

    def lambda_A49():
        OP_6D(-32100, 1000, 980, 7000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_A49)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2507)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_79D end

    SaveToFile()

Try(main)
