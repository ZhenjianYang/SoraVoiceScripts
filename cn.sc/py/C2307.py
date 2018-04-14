from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 卢安

    CreateScenaFile(
        FileName            = 'C2307   ._SN',
        MapName             = 'Ruan',
        Location            = 'C2307.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
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
        '幻惑之铃露茜奥拉',                     # 9
        '福音',                                 # 10
        '残像',                                 # 11
        '残像',                                 # 12
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
        'ED6_DT27/CH04520 ._CH',             # 00
        'ED6_DT06/CH20021 ._CH',             # 01
        'ED6_DT27/CH04000 ._CH',             # 02
        'ED6_DT27/CH04010 ._CH',             # 03
        'ED6_DT07/CH00120 ._CH',             # 04
        'ED6_DT07/CH00024 ._CH',             # 05
        'ED6_DT27/CH04525 ._CH',             # 06
        'ED6_DT27/CH04526 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT27/CH04520P._CP',             # 00
        'ED6_DT06/CH20021P._CP',             # 01
        'ED6_DT27/CH04000P._CP',             # 02
        'ED6_DT27/CH04010P._CP',             # 03
        'ED6_DT07/CH00120P._CP',             # 04
        'ED6_DT07/CH00024P._CP',             # 05
        'ED6_DT27/CH04525P._CP',             # 06
        'ED6_DT27/CH04526P._CP',             # 07
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
        Unknown3            = 458753,
        ChipIndex           = 0x1,
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
        Unknown3            = 65543,
        ChipIndex           = 0x7,
        NpcIndex            = 0x1E1,
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
        Unknown3            = 65543,
        ChipIndex           = 0x7,
        NpcIndex            = 0x1E1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_16A",          # 00, 0
        "Function_1_187",          # 01, 1
        "Function_2_188",          # 02, 2
        "Function_3_A66",          # 03, 3
        "Function_4_B0C",          # 04, 4
        "Function_5_BB2",          # 05, 5
        "Function_6_C39",          # 06, 6
    )


    def Function_0_16A(): pass

    label("Function_0_16A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_186")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x53), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)

    label("loc_186")

    Return()

    # Function_0_16A end

    def Function_1_187(): pass

    label("Function_1_187")

    Return()

    # Function_1_187 end

    def Function_2_188(): pass

    label("Function_2_188")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_19F")
    Call(0, 5)
    Call(0, 6)

    label("loc_19F")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (5, "loc_1BC"),
        (4, "loc_1C9"),
        (6, "loc_1D6"),
        (7, "loc_1E3"),
        (8, "loc_1F0"),
        (SWITCH_DEFAULT, "loc_1FD"),
    )


    label("loc_1BC")

    OP_D2(0x70218, 0x70224, 0x8)
    Jump("loc_1FD")

    label("loc_1C9")

    OP_D2(0x70200, 0x7020C, 0x8)
    Jump("loc_1FD")

    label("loc_1D6")

    OP_D2(0x70230, 0x7023C, 0x8)
    Jump("loc_1FD")

    label("loc_1E3")

    OP_D2(0x70248, 0x70254, 0x8)
    Jump("loc_1FD")

    label("loc_1F0")

    OP_D2(0x270176, 0x270183, 0x8)
    Jump("loc_1FD")

    label("loc_1FD")

    OP_6D(34920, 250, 12030, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3960, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_22(0x1C3, 0x0, 0x64)
    SetChrPos(0x8, 900, 950, 12280, 90)
    ClearChrFlags(0x8, 0x80)
    OP_82(0x80, 0x0)
    OP_82(0x82, 0x0)
    OP_72(0x6, 0x4)
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_79(0x0, 0x2)
    OP_79(0x1, 0x2)
    OP_79(0x2, 0x2)
    OP_79(0x3, 0x2)
    OP_79(0x4, 0x2)
    OP_7B()
    SetChrPos(0x103, 40, 0, 5100, 90)
    SetChrPos(0x101, 1200, 0, 4000, 90)
    SetChrPos(0x102, -1020, 0, 3400, 90)
    SetChrPos(0xF9, 60, 0, 2300, 90)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 2)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0x102, 3)
    SetChrSubChip(0x103, 0)
    SetChrChipByIndex(0x103, 4)
    SetChrSubChip(0xF9, 0)
    SetChrChipByIndex(0xF9, 8)

    def lambda_300():
        OP_6D(1840, 0, 7670, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_300)

    def lambda_318():
        OP_67(0, 5560, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_318)

    def lambda_330():
        OP_6B(4800, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_330)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    WaitChrThread(0x101, 0x0)
    Sleep(500)

    ChrTalk(    #0
        0x8,
        (
            "#241F#6P呵呵……\x01",
            "看来到时间了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(210, 950, 9870, 0)
    OP_67(0, 2820, -10000, 0)
    OP_6B(3400, 0)
    OP_6C(4000, 0)
    OP_6E(343, 0)
    SetChrSubChip(0x103, 0)
    SetChrChipByIndex(0x103, 65535)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0xF9, 0)
    SetChrChipByIndex(0xF9, 65535)
    OP_0D()

    def lambda_3EE():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3EE)
    Sleep(100)

    def lambda_401():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_401)
    Sleep(100)

    def lambda_414():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_414)
    Sleep(100)

    def lambda_427():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_427)
    Sleep(500)

    ChrTalk(    #1
        0x101,
        (
            "#1003F#4P对了、对了……\x02\x03",

            "#1002F这里的结界\x01",
            "是为了什么而张开来的？\x02\x03",

            "『结社』到底，\x01",
            "打算做什么？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 400)
    Sleep(500)

    ChrTalk(    #2
        0x8,
        (
            "#240F#5P很遗憾，我们\x01",
            "也未被告知详情。\x02\x03",

            "我们只是按照\x01",
            "教授的指示做事而已。\x02\x03",

            "#244F仅仅，是在看了隐藏之塔的内部后\x01",
            "察觉到了一些线索。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x101,
        "#1004F#4P哎……\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 6)
    OP_0D()
    Sleep(500)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 7)
    Fade(500)

    def lambda_568():
        OP_6B(3200, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_568)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(240)
    OP_22(0x118, 0x0, 0x64)
    OP_43(0xA, 0x1, 0x0, 0x3)
    OP_43(0xB, 0x1, 0x0, 0x4)
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_625")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_663")

    label("loc_625")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_64C")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_663")

    label("loc_64C")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_663")

    Sleep(1000)

    ChrTalk(    #4
        0x103,
        (
            "#024F#6P等等姐姐！\x01",
            "你还没有全部回答我！\x02\x03",

            "为什么姐姐\x01",
            "一定要杀死团长！？\x02\x03",

            "#527F……把那么温柔的一个人……\x01",
            "如同大家的父亲一般的人……杀死！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        (
            "#244F#5P呵呵……\x01",
            "不好意思，今天就到此为止了。\x02\x03",

            "#241F如果以后还有机会相遇的话，\x01",
            "我会把事情的全部后续告诉你。\x02\x03",

            "在此之前要乖乖听话哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x11E, 0x0, 0x64)

    def lambda_78A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_78A)

    def lambda_79C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_79C)

    def lambda_7AE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_7AE)
    WaitChrThread(0x8, 0x2)
    WaitChrThread(0xA, 0x2)
    WaitChrThread(0xB, 0x2)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    Sleep(1000)

    ChrTalk(    #6
        0x103,
        "#024F#6P姐姐……！\x02",
    )

    CloseMessageWindow()

    def lambda_803():

        label("loc_803")

        TurnDirection(0xFE, 0x103, 400)
        OP_48()
        Jump("loc_803")

    QueueWorkItem2(0x101, 3, lambda_803)

    def lambda_814():
        OP_6D(80, 500, 10820, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_814)

    def lambda_82C():
        OP_6C(0, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_82C)
    OP_91(0x103, 0x0, 0x0, 0x5DC, 0x3E8, 0x0)
    Sleep(500)
    OP_62(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    WaitChrThread(0x101, 0x1)
    Sleep(1500)

    ChrTalk(    #7
        0x101,
        "#1026F#4P那、那个，雪拉姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x102,
        "#1043F#6P雪拉姐……\x02",
    )

    CloseMessageWindow()
    OP_63(0x103)
    Sleep(1000)

    ChrTalk(    #9
        0x103,
        (
            "#522F#5P……我没事，别担心。\x02\x03",

            "我已经离姐姐的真相\x01",
            "更近一步了。\x02\x03",

            "#026F现在……这就足够了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_938")

    ChrTalk(    #10
        0x108,
        "#572F#6P雪拉扎德……\x02",
    )

    CloseMessageWindow()
    Jump("loc_9E6")

    label("loc_938")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_963")

    ChrTalk(    #11
        0x106,
        "#552F#6P雪拉扎德……\x02",
    )

    CloseMessageWindow()
    Jump("loc_9E6")

    label("loc_963")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_98E")

    ChrTalk(    #12
        0x107,
        "#063F#6P雪拉姐姐……\x02",
    )

    CloseMessageWindow()
    Jump("loc_9E6")

    label("loc_98E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9BD")

    ChrTalk(    #13
        0x105,
        "#043F#6P雪拉扎德小姐……\x02",
    )

    CloseMessageWindow()
    Jump("loc_9E6")

    label("loc_9BD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9E6")

    ChrTalk(    #14
        0x109,
        "#1067F#6P雪拉小姐……\x02",
    )

    CloseMessageWindow()

    label("loc_9E6")

    OP_8C(0x103, 180, 400)
    Sleep(500)

    ChrTalk(    #15
        0x103,
        (
            "#524F#5P『四轮之塔』已经解决三个了……\x02\x03",

            "返回『埃尔赛尤』，\x01",
            "前往最后一座塔吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0x7D0)
    OP_21()
    OP_A2(0x10FF)
    OP_A2(0x10F3)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_188 end

    def Function_3_A66(): pass

    label("Function_3_A66")

    SetChrPos(0xA, 900, 950, 12280, 180)
    OP_9F(0xA, 0xFF, 0xFF, 0xFF, 0x5A, 0x0)
    ClearChrFlags(0xA, 0x80)
    OP_91(0xA, 0x32, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xA, 0xFFFFFFCE, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xA, 0x64, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xA, 0xFFFFFF9C, 0x0, 0x0, 0x12C, 0x0)

    label("loc_AD7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B0B")
    OP_91(0xA, 0x96, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xA, 0xFFFFFF6A, 0x0, 0x0, 0x12C, 0x0)
    Jump("loc_AD7")

    label("loc_B0B")

    Return()

    # Function_3_A66 end

    def Function_4_B0C(): pass

    label("Function_4_B0C")

    SetChrPos(0xB, 900, 950, 12280, 180)
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0x5A, 0x0)
    ClearChrFlags(0xB, 0x80)
    OP_91(0xB, 0xFFFFFFCE, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xB, 0x32, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xB, 0xFFFFFF9C, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xB, 0x64, 0x0, 0x0, 0x12C, 0x0)

    label("loc_B7D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BB1")
    OP_91(0xB, 0xFFFFFF6A, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xB, 0x96, 0x0, 0x0, 0x12C, 0x0)
    Jump("loc_B7D")

    label("loc_BB1")

    Return()

    # Function_4_B0C end

    def Function_5_BB2(): pass

    label("Function_5_BB2")

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
        (0, "loc_C2C"),
        (1, "loc_C32"),
        (SWITCH_DEFAULT, "loc_C38"),
    )


    label("loc_C2C")

    OP_A2(0x1200)
    Jump("loc_C38")

    label("loc_C32")

    OP_A2(0x1201)
    Jump("loc_C38")

    label("loc_C38")

    Return()

    # Function_5_BB2 end

    def Function_6_C39(): pass

    label("Function_6_C39")

    FadeToDark(0, 0, -1)
    OP_6D(-66940, 250, 36210, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(3700, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0x2, 0xFF, 0x5, 0x6, 0x4, 0x8, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_6_C39 end

    SaveToFile()

Try(main)
