from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'C3607   ._SN',
        MapName             = 'Zeiss',
        Location            = 'C3607.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60033",
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
        '瘦狼瓦鲁特',                           # 9
        '雾香',                                 # 10
        '福音',                                 # 11
        '',                                     # 12
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
        'ED6_DT27/CH03500 ._CH',             # 00
        'ED6_DT07/CH02610 ._CH',             # 01
        'ED6_DT06/CH20021 ._CH',             # 02
        'ED6_DT26/CH20242 ._CH',             # 03
        'ED6_DT26/CH20280 ._CH',             # 04
        'ED6_DT29/CH12140 ._CH',             # 05
        'ED6_DT29/CH12141 ._CH',             # 06
    )

    AddCharChipPat(
        'ED6_DT27/CH03500P._CP',             # 00
        'ED6_DT07/CH02610P._CP',             # 01
        'ED6_DT06/CH20021P._CP',             # 02
        'ED6_DT26/CH20242P._CP',             # 03
        'ED6_DT26/CH20280P._CP',             # 04
        'ED6_DT29/CH12140P._CP',             # 05
        'ED6_DT29/CH12141P._CP',             # 06
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 458754,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 9600,
        Z                   = 250,
        Y                   = 1400,
        Unknown_0C          = 270,
        Unknown_0E          = 5,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1F5,
        Unknown_18          = 8448,
        Unknown_1A          = 0,
    )


    ScpFunction(
        "Function_0_15E",          # 00, 0
        "Function_1_195",          # 01, 1
        "Function_2_23A",          # 02, 2
        "Function_3_F0E",          # 03, 3
        "Function_4_F3E",          # 04, 4
        "Function_5_F6E",          # 05, 5
        "Function_6_F9E",          # 06, 6
        "Function_7_1025",         # 07, 7
    )


    def Function_0_15E(): pass

    label("Function_0_15E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16C")
    OP_B5(0x0)

    label("loc_16C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x420, 0)), scpexpr(EXPR_END)), "loc_178")
    SetChrFlags(0xB, 0x80)

    label("loc_178")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_194")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)

    label("loc_194")

    Return()

    # Function_0_15E end

    def Function_1_195(): pass

    label("Function_1_195")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E3")
    OP_72(0x8, 0x4)
    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    OP_82(0x82, 0x0)
    OP_82(0x83, 0x0)
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
    Jump("loc_21D")

    label("loc_1E3")

    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    OP_82(0x82, 0x0)
    OP_82(0x83, 0x0)
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

    label("loc_21D")

    OP_51(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_239")
    OP_22(0x1C3, 0x0, 0x64)

    label("loc_239")

    Return()

    # Function_1_195 end

    def Function_2_23A(): pass

    label("Function_2_23A")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_251")
    Call(0, 6)
    Call(0, 7)

    label("loc_251")

    OP_6D(34920, 250, 12030, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3960, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_22(0x1C3, 0x0, 0x64)
    SetChrPos(0x8, -2540, 250, 9040, 90)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 4)
    SetChrSubChip(0x8, 0)
    SetChrPos(0x9, 40, 0, 6000, 90)
    ClearChrFlags(0x9, 0x80)
    OP_82(0x80, 0x0)
    OP_82(0x82, 0x0)
    SetChrPos(0x108, 2730, 250, 8740, 90)
    SetChrPos(0x101, 200, 0, 2110, 90)
    SetChrPos(0x102, 1000, 0, 1470, 90)
    SetChrPos(0xF9, -800, 0, 1110, 90)
    OP_72(0x7, 0x4)
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

    def lambda_34C():
        OP_6D(1840, 0, 7670, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_34C)

    def lambda_364():
        OP_67(0, 5560, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_364)

    def lambda_37C():
        OP_6B(4800, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_37C)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    WaitChrThread(0x101, 0x0)
    Sleep(500)

    ChrTalk(    #0
        0x8,
        (
            "#252F嘻嘻……\x01",
            "此次的任务完成了吗。\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x20)
    TurnDirection(0x8, 0x9, 400)
    ClearChrFlags(0x8, 0x20)

    def lambda_3DE():

        label("loc_3DE")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_3DE")

    QueueWorkItem2(0x9, 1, lambda_3DE)
    Sleep(50)

    def lambda_3F4():

        label("loc_3F4")

        OP_8C(0xFE, 225, 400)
        OP_48()
        Jump("loc_3F4")

    QueueWorkItem2(0x108, 1, lambda_3F4)
    Sleep(50)

    def lambda_40A():

        label("loc_40A")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_40A")

    QueueWorkItem2(0x101, 1, lambda_40A)
    Sleep(50)

    def lambda_420():

        label("loc_420")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_420")

    QueueWorkItem2(0x102, 1, lambda_420)
    Sleep(50)

    def lambda_436():

        label("loc_436")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_436")

    QueueWorkItem2(0xF9, 1, lambda_436)
    Sleep(400)
    Fade(500)
    OP_6D(210, 0, 8800, 0)
    OP_67(0, 4650, -10000, 0)
    OP_6B(2880, 0)
    OP_6C(0, 0)
    OP_6E(315, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #1
        0x8,
        (
            "#251F……雾香。\x01",
            "最后能遇见你我很高兴。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x9,
        (
            "#794F我则是忧喜参半呢。\x02\x03",

            "#792F以后大概不会再见面了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "#257F嗯……\x01",
            "以后就是我和这家伙的问题了。\x02\x03",

            "#251F不过你啊，这种时候\x01",
            "就不能表现得温顺点吗？\x02\x03",

            "到了最后还是这么不饶人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x9,
        (
            "#791F呵呵……\x01",
            "你喜欢的不就是我这一点么？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        "#253F嘿嘿嘿……没错。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 90, 400)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x8, 0x4)
    OP_7D(0x0, 0x8, 0x32, 0x1F4)
    SetChrChipByIndex(0x8, 3)
    SetChrSubChip(0x8, 1)
    Sleep(300)
    OP_22(0x23B, 0x0, 0x64)
    SetChrSubChip(0x8, 2)

    def lambda_5F4():
        OP_96(0xFE, 0x820, 0x3B6, 0x3246, 0x5DC, 0x1F40)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5F4)
    WaitChrThread(0x8, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrSubChip(0x8, 1)
    Sleep(50)
    OP_22(0x23B, 0x0, 0x64)
    SetChrSubChip(0x8, 2)

    def lambda_630():
        OP_96(0xFE, 0x31B0, 0xFA, 0x334A, 0x3E8, 0x1F40)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_630)
    SetChrSubChip(0x8, 1)
    Fade(500)
    OP_6D(15140, 250, 15230, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(33000, 0)
    OP_6E(277, 0)
    WaitChrThread(0x8, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    OP_7D(0x1, 0x8, 0x0, 0x0)
    WaitChrThread(0x102, 0x3)
    Sleep(500)
    Fade(500)
    SetChrChipByIndex(0x8, 4)
    SetChrSubChip(0x8, 0)
    Sleep(500)
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0xF9, 0x1)
    OP_44(0x108, 0x1)
    OP_44(0x9, 0x1)

    ChrTalk(    #6
        0x108,
        "#073F#2P喂、喂！？\x02",
    )

    CloseMessageWindow()

    def lambda_6F1():
        OP_6D(13250, 250, 13830, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6F1)

    def lambda_709():
        OP_67(0, 6960, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_709)
    OP_8E(0x108, 0x5E6, 0x0, 0x259E, 0x1770, 0x0)
    OP_8E(0x108, 0x2396, 0xFA, 0x3228, 0x1770, 0x0)
    TurnDirection(0x108, 0x8, 400)
    Sleep(500)
    OP_44(0x8, 0x1)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #7
        0x8,
        (
            "#250F#5P……金。\x02\x03",

            "为什么我会和老头子\x01",
            "进行生死决斗……\x02\x03",

            "如果想知道的话，\x01",
            "就试着将我打败吧。\x02\x03",

            "用老头子\x01",
            "传给你的『活人拳』。\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x8, 3)
    SetChrSubChip(0x8, 1)
    Sleep(300)
    OP_22(0x23B, 0x0, 0x64)
    SetChrSubChip(0x8, 2)
    ClearChrFlags(0x8, 0x1)

    def lambda_7FB():
        OP_6D(14850, 250, 15000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7FB)

    def lambda_813():
        OP_67(0, 6450, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_813)

    def lambda_82B():
        OP_96(0xFE, 0x36E2, 0x514, 0x33F4, 0x7D0, 0xFA0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_82B)
    SetChrSubChip(0x8, 1)
    WaitChrThread(0x8, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x8, 4)
    SetChrSubChip(0x8, 0)
    WaitChrThread(0x8, 0x1)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x8, 270, 400)
    WaitChrThread(0x8, 0x0)
    Sleep(500)
    OP_7D(0x0, 0x8, 0x32, 0x1F4)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    SetChrChipByIndex(0x8, 3)
    SetChrSubChip(0x8, 1)
    Sleep(300)
    OP_22(0x23B, 0x0, 0x64)
    SetChrSubChip(0x8, 0)

    def lambda_8AC():
        OP_6B(2800, 500)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_8AC)

    def lambda_8BC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_8BC)

    def lambda_8CE():
        OP_96(0xFE, 0x40CE, 0xFFFFEC78, 0x3700, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_8CE)
    Sleep(500)
    OP_62(0x108, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    WaitChrThread(0x8, 0x1)
    SetChrFlags(0x8, 0x80)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)

    ChrTalk(    #8
        0x108,
        "#077F#5P什……！\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    SetMapFlags(0x10)
    OP_6D(1580, 0, 5260, 0)
    OP_67(0, 3900, -10000, 0)
    OP_6B(2670, 0)
    OP_6C(21000, 0)
    OP_6E(303, 0)
    OP_0D()

    ChrTalk(    #9
        0x101,
        "#1020F#6P慢、慢着！？\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(12720, 250, 13130, 0)
    OP_67(0, 6250, -10000, 0)
    OP_6B(3330, 0)
    OP_6C(45000, 0)
    OP_6E(301, 0)

    def lambda_9E5():
        OP_6D(15810, 250, 13140, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9E5)

    def lambda_9FD():
        OP_67(0, 5700, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_9FD)

    def lambda_A15():
        OP_6B(3000, 4000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A15)

    def lambda_A25():
        OP_8E(0xFE, 0x3426, 0xFA, 0x316A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_A25)
    OP_43(0x101, 0x1, 0x0, 0x3)
    Sleep(500)
    OP_43(0x102, 0x1, 0x0, 0x4)
    Sleep(500)
    OP_43(0xF9, 0x1, 0x0, 0x5)
    WaitChrThread(0x108, 0x1)
    WaitChrThread(0x101, 0x2)
    Sleep(500)

    ChrTalk(    #10
        0x108,
        "#572F#6P…………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        (
            "#1020F#6P开，开玩笑吧！？\x02\x03",

            "『执行者』\x01",
            "从这个高度落下也没事吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x102,
        (
            "#1035F#6P虽然不是所有人都这样……\x02\x03",

            "#1042F但是像他这种高手\x01",
            "就算没事也不足为奇。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x108,
        (
            "#074F#6P啊啊，撑住外壁\x01",
            "降低下落速度。\x02\x03",

            "#072F好厉害的硬功和化劲。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x9, 2760, 250, 10680, 90)

    ChrTalk(    #14
        0x9,
        (
            "#2P真是的……\x01",
            "吓唬人也要有个程度啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_BB1():
        OP_6D(13910, 250, 12760, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_BB1)

    def lambda_BC9():
        OP_67(0, 6000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_BC9)

    def lambda_BE1():
        OP_8E(0xFE, 0x27CE, 0xFA, 0x2CA6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_BE1)

    def lambda_BFC():

        label("loc_BFC")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_BFC")

    QueueWorkItem2(0x101, 1, lambda_BFC)
    Sleep(50)

    def lambda_C12():

        label("loc_C12")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_C12")

    QueueWorkItem2(0x108, 1, lambda_C12)
    Sleep(50)

    def lambda_C28():

        label("loc_C28")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_C28")

    QueueWorkItem2(0x102, 1, lambda_C28)
    Sleep(50)

    def lambda_C3E():

        label("loc_C3E")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_C3E")

    QueueWorkItem2(0xF9, 1, lambda_C3E)
    WaitChrThread(0x9, 0x1)
    WaitChrThread(0x101, 0x2)
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0x108, 0x1)
    OP_44(0xF9, 0x1)

    ChrTalk(    #15
        0x108,
        (
            "#072F#5P雾香……\x02\x03",

            "你怎么知道瓦鲁特\x01",
            "来了这里？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x9,
        (
            "#794F#6P你以为我不知道？\x02\x03",

            "#792F真是的……\x01",
            "你也好瓦鲁特也好。\x02\x03",

            "#791F男人为什么\x01",
            "都这么笨拙呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x108,
        "#075F#5P呜唔……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #18
        0x101,
        "#1019F#5P……………………（盯）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x102,
        (
            "#1048F#2P……我在反省啦\x01",
            "拜托别用那种眼神看我。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D92")

    ChrTalk(    #20
        0x103,
        "#027F#6P呵呵……\x02",
    )

    CloseMessageWindow()

    label("loc_D92")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DB6")

    ChrTalk(    #21
        0x107,
        "#061F#6P嘿嘿……\x02",
    )

    CloseMessageWindow()

    label("loc_DB6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DDC")

    ChrTalk(    #22
        0x105,
        "#048F#6P哈哈哈……\x02",
    )

    CloseMessageWindow()

    label("loc_DDC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E11")

    ChrTalk(    #23
        0x106,
        (
            "#051F#6P嘿……\x01",
            "怎么扯到那么远了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E11")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E43")

    ChrTalk(    #24
        0x109,
        (
            "#1068F#6P嗯……\x01",
            "这话真刺耳啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E43")


    ChrTalk(    #25
        0x9,
        (
            "#792F#6P好了，私事解决了，\x01",
            "我也差不多该回蔡斯了。\x02\x03",

            "#791F……祝各位好运。\x01",
            "去其他的塔时也请当心。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_EAE():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_EAE)
    Sleep(300)

    ChrTalk(    #26
        0x101,
        "#1025F#2P雾香……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x108,
        "#070F#5P嗯嗯……明白了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0x7D0)
    OP_21()
    OP_A2(0x10F3)
    NewScene("ED6_DT21/E0311   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_2_23A end

    def Function_3_F0E(): pass

    label("Function_3_F0E")

    OP_8E(0xFE, 0x92E, 0xFA, 0x1FC2, 0x1388, 0x0)
    OP_8E(0xFE, 0x3674, 0xFA, 0x2CCE, 0x1388, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_3_F0E end

    def Function_4_F3E(): pass

    label("Function_4_F3E")

    OP_8E(0xFE, 0x92E, 0xFA, 0x1FC2, 0x1388, 0x0)
    OP_8E(0xFE, 0x35C0, 0xFA, 0x27E2, 0x1388, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_4_F3E end

    def Function_5_F6E(): pass

    label("Function_5_F6E")

    OP_8E(0xFE, 0x92E, 0xFA, 0x1FC2, 0x1388, 0x0)
    OP_8E(0xFE, 0x3124, 0xFA, 0x2B70, 0x1388, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_5_F6E end

    def Function_6_F9E(): pass

    label("Function_6_F9E")

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
        (0, "loc_1018"),
        (1, "loc_101E"),
        (SWITCH_DEFAULT, "loc_1024"),
    )


    label("loc_1018")

    OP_A2(0x1200)
    Jump("loc_1024")

    label("loc_101E")

    OP_A2(0x1201)
    Jump("loc_1024")

    label("loc_1024")

    Return()

    # Function_6_F9E end

    def Function_7_1025(): pass

    label("Function_7_1025")

    FadeToDark(0, 0, -1)
    OP_6D(-66940, 250, 36210, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(3700, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0x7, 0xFF, 0x5, 0x2, 0x6, 0x4, 0x8, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_7_1025 end

    SaveToFile()

Try(main)
