from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2210   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2210.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60012",
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
        '管家达里奥',                           # 9
        '秘书基尔巴特',                         # 10
        '杯子',                                 # 11
        '杯子',                                 # 12
        '水壶',                                 # 13
        '目标用照相机',                         # 14
        '',                                     # 15
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
        'ED6_DT07/CH01560 ._CH',             # 00
        'ED6_DT07/CH02420 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH01560P._CP',             # 00
        'ED6_DT07/CH02420P._CP',             # 01
    )

    DeclNpc(
        X                   = 67820,
        Z                   = -30,
        Y                   = -5200,
        Direction           = 90,
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
        X                   = 67820,
        Z                   = -30,
        Y                   = -5200,
        Direction           = 90,
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
        X                   = 35510,
        Z                   = 750,
        Y                   = 27280,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1638400,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 35450,
        Z                   = 750,
        Y                   = 26890,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1638400,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 35490,
        Z                   = 750,
        Y                   = 26520,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1703936,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1E6,
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


    DeclActor(
        TriggerX            = -475,
        TriggerZ            = 0,
        TriggerY            = 3173,
        TriggerRange        = 800,
        ActorX              = -475,
        ActorZ              = 800,
        ActorY              = 3173,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -63800,
        TriggerZ            = 0,
        TriggerY            = 50790,
        TriggerRange        = 900,
        ActorX              = -63800,
        ActorZ              = -300,
        ActorY              = 50790,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -62370,
        TriggerZ            = 0,
        TriggerY            = -43110,
        TriggerRange        = 500,
        ActorX              = -62370,
        ActorZ              = 2000,
        ActorY              = -43110,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -59500,
        TriggerZ            = 250,
        TriggerY            = -36760,
        TriggerRange        = 800,
        ActorX              = -59500,
        ActorZ              = 1250,
        ActorY              = -36760,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_20A",          # 00, 0
        "Function_1_220",          # 01, 1
        "Function_2_234",          # 02, 2
        "Function_3_3B1",          # 03, 3
        "Function_4_422",          # 04, 4
        "Function_5_C72",          # 05, 5
        "Function_6_D21",          # 06, 6
        "Function_7_D2B",          # 07, 7
        "Function_8_D35",          # 08, 8
    )


    def Function_0_20A(): pass

    label("Function_0_20A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21F")
    SetMapFlags(0x10000000)
    Event(0, 4)

    label("loc_21F")

    Return()

    # Function_0_20A end

    def Function_1_220(): pass

    label("Function_1_220")

    OP_72(0x1010, 0x0)
    ExitThread()
    OP_72(0x810, 0x0)
    ExitThread()
    OP_6F(0x10, 360)
    Return()

    # Function_1_220 end

    def Function_2_234(): pass

    label("Function_2_234")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_259")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_39B")

    label("loc_259")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_272")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_39B")

    label("loc_272")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28B")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_39B")

    label("loc_28B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A4")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_39B")

    label("loc_2A4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BD")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_39B")

    label("loc_2BD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D6")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_39B")

    label("loc_2D6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EF")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_39B")

    label("loc_2EF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_308")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_39B")

    label("loc_308")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_321")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_39B")

    label("loc_321")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33A")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_39B")

    label("loc_33A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_353")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_39B")

    label("loc_353")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36C")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_39B")

    label("loc_36C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_385")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_39B")

    label("loc_385")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39B")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_39B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3B0")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_39B")

    label("loc_3B0")

    Return()

    # Function_2_234 end

    def Function_3_3B1(): pass

    label("Function_3_3B1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_421")
    OP_8E(0xFE, 0xFFFFEE6C, 0x0, 0xFFFFEAA2, 0x3E8, 0x0)
    OP_62(0xFE, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_8C(0xFE, 90, 400)
    Sleep(3500)
    OP_8E(0xFE, 0xFFFFEE6C, 0x0, 0xFFFFF204, 0x3E8, 0x0)
    OP_8C(0xFE, 90, 400)
    OP_62(0xFE, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sleep(4500)
    Jump("Function_3_3B1")

    label("loc_421")

    Return()

    # Function_3_3B1 end

    def Function_4_422(): pass

    label("Function_4_422")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(72840, -2000, -12380, 0)
    OP_67(0, 4840, -10000, 0)
    OP_6B(3040, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x10, 68100, 0, -9000, 90)
    SetChrPos(0x11, 66600, -30, -7100, 90)
    SetChrPos(0x105, 70000, -3750, -14500, 90)
    OP_9F(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(2000, 0)

    def lambda_4C2():
        OP_6D(68060, -30, -7600, 6800)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_4C2)

    def lambda_4DA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_4DA)

    def lambda_4EC():
        OP_8E(0xFE, 0x11D8C, 0xFFFFF830, 0xFFFFC75C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4EC)
    WaitChrThread(0x105, 0x1)

    def lambda_50C():
        OP_8E(0xFE, 0x11D8C, 0xFFFFFFE2, 0xFFFFDECC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_50C)
    WaitChrThread(0x105, 0x1)

    def lambda_52C():
        OP_8E(0xFE, 0x111AC, 0xFFFFFFE2, 0xFFFFDECC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_52C)
    WaitChrThread(0x105, 0x1)
    Sleep(500)

    ChrTalk(    #0
        0x105,
        (
            "#543F#12P那个，不好意思。\x02\x03",

            "#040F我是为了\x01",
            "杰尼丝王立学院\x01",
            "学生会的事前来拜访的……\x02\x03",

            "能不能让我\x01",
            "见见戴尔蒙市长呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x10,
        "#5P啊，要见市长吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x10,
        (
            "#5P十分抱歉。\x01",
            "现在市长不在……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x10,
        (
            "#5P如果不是非常紧急的事\x01",
            "今天就请回吧……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    NpcTalk(    #4
        0x11,
        "声音",
        "#2P哎呀，有事的话跟我说吧。\x02",
    )

    Jump("loc_68C")

    label("loc_68C")

    CloseMessageWindow()
    OP_59()
    Sleep(1000)
    SetChrPos(0x11, 65500, -30, -7100, 90)

    def lambda_6AA():

        label("loc_6AA")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_6AA")

    QueueWorkItem2(0x105, 2, lambda_6AA)

    def lambda_6BB():

        label("loc_6BB")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_6BB")

    QueueWorkItem2(0x10, 2, lambda_6BB)
    OP_72(0x100B, 0x0)
    ExitThread()
    OP_70(0xB, 0x1E)
    OP_73(0xB)
    Sleep(300)

    def lambda_6E1():
        OP_8E(0xFE, 0x109DC, 0xFFFFFFE2, 0xFFFFE444, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6E1)
    WaitChrThread(0x11, 0x1)
    Sleep(100)
    OP_72(0xB, 0x8)
    ExitThread()
    OP_22(0x7, 0x0, 0x64)
    OP_70(0xB, 0x0)
    Sleep(300)
    OP_8C(0x11, 130, 400)
    Sleep(500)
    OP_44(0x105, 0x2)
    OP_44(0x11, 0x2)

    NpcTalk(    #5
        0x11,
        "爽快的青年",
        (
            "#678F#5P我是担任市长代理的\x01",
            "秘书基尔巴特。\x02\x03",

            "#670F你是……王立学院的学生对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x105,
        (
            "#044F#6P啊，是的。\x02\x03",

            "#040F那个，\x01",
            "这是学生会提交的文件……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        "\x07\x05科洛丝将信封交给爽快的青年。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(    #8
        0x11,
        "#672F#5P啊啊，是本年度的学生名簿吧……\x02",
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #9
        0x11,
        (
            "#670F#5P因为杰尼丝王立学院\x01",
            "基本上都是住校制啊。\x01",
            "毎年都有学生入学毕业吧？\x02\x03",

            "为了简化居民登记\x01",
            "就以学院为单位来提交了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x105,
        "#542F#6P啊，是这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x11,
        (
            "#678F#5P呵呵，不瞒你说，\x01",
            "我也是王立学院出身的啊。\x02\x03",

            "别看我这样，\x01",
            "也曾经作为学生会的一员努力过呢。\x02\x03",

            "#670F嗯，\x01",
            "那所学院的学生会实在是很出色。\x02\x03",

            "#673F高贵，纯粹，\x01",
            "更重要的是有坚定的理念……\x02",
        )
    )

    Jump("loc_A02")

    label("loc_A02")

    CloseMessageWindow()

    ChrTalk(    #12
        0x105,
        (
            "#044F#6P是、是这样吗。\x02\x03",

            "#047F（虽然现在已经完全变样了……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x11,
        (
            "#670F#5P那时候的经验\x01",
            "在现在市长秘书的工作中\x01",
            "也的确非常有用。\x02\x03",

            "你作为学生会的一员\x01",
            "也要多加努力才是。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x105,
        (
            "#045F#6P是、是的。\x01",
            "非常感谢……\x02\x03",

            "（其实我只是\x01",
            "  帮学生会的忙而已……）\x02\x03",

            "#542F嗯，那么……\x01",
            "我就先告辞了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x11,
        (
            "#670F#5P嗯。\x02\x03",

            "遇到什么困难的话，\x01",
            "随时都可以来这里。\x02\x03",

            "#678F我应该能助你一臂之力。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x105,
        "#543F#6P非常感谢。\x02",
    )

    CloseMessageWindow()

    def lambda_BDC():

        label("loc_BDC")

        TurnDirection(0xFE, 0x105, 400)
        OP_48()
        Jump("loc_BDC")

    QueueWorkItem2(0x11, 2, lambda_BDC)

    def lambda_BED():

        label("loc_BED")

        TurnDirection(0xFE, 0x105, 400)
        OP_48()
        Jump("loc_BED")

    QueueWorkItem2(0x10, 2, lambda_BED)
    OP_8C(0x105, 90, 600)

    def lambda_C05():
        OP_8E(0xFE, 0x11D8C, 0xFFFFFFE2, 0xFFFFDECC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_C05)
    WaitChrThread(0x105, 0x1)

    def lambda_C25():
        OP_8E(0xFE, 0x11D8C, 0xFFFFF830, 0xFFFFC75C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_C25)
    WaitChrThread(0x105, 0x1)

    def lambda_C45():
        OP_8E(0xFE, 0x11170, 0xFFFFF15A, 0xFFFFC75C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_C45)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2505)
    NewScene("ED6_DT21/T2100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_422 end

    def Function_5_C72(): pass

    label("Function_5_C72")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #17
        (
            "\x07\x05『苍耀之灯火』\x01",
            "  被认为是初期导力艺术\x01",
            "　极致的作品。\x01",
            "　导力革命之后\x01",
            "　由卢安市民\x01",
            "　赠送给为城市发展\x01",
            "　作出贡献的戴尔蒙家。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_5_C72 end

    def Function_6_D21(): pass

    label("Function_6_D21")

    NewScene("ED6_DT21/T2210   ._SN", 123, 1, 0)
    IdleLoop()
    Return()

    # Function_6_D21 end

    def Function_7_D2B(): pass

    label("Function_7_D2B")

    NewScene("ED6_DT21/T2210   ._SN", 121, 1, 0)
    IdleLoop()
    Return()

    # Function_7_D2B end

    def Function_8_D35(): pass

    label("Function_8_D35")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #18
        "\x07\x05有吊桥的控制装置。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_8_D35 end

    SaveToFile()

Try(main)
