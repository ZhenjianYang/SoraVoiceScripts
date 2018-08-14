from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'T0301   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0301.x',
        MapIndex            = 15,
        MapDefaultBGM       = "ed60084",
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
        '约修亚',                               # 9
        '卡西乌斯',                             # 10
        '器皿',                                 # 11
        '目标用照相机',                         # 12
        '艾利兹大道方向',                       # 13
        '',                                     # 14
    )

    DeclEntryPoint(
        Unknown_00              = 2000,
        Unknown_04              = 0,
        Unknown_08              = -6000,
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
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 15,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 9600,
        Unknown_04              = 875,
        Unknown_08              = 300,
        Unknown_0C              = 4,
        Unknown_0E              = 118,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 15,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 9600,
        Unknown_04              = 875,
        Unknown_08              = 300,
        Unknown_0C              = 4,
        Unknown_0E              = 118,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 15,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 9600,
        Unknown_04              = 875,
        Unknown_08              = 300,
        Unknown_0C              = 4,
        Unknown_0E              = 118,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 15,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH02750 ._CH',             # 00
        'ED6_DT06/CH20011 ._CH',             # 01
        'ED6_DT06/CH20021 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT07/CH02750P._CP',             # 00
        'ED6_DT06/CH20011P._CP',             # 01
        'ED6_DT06/CH20021P._CP',             # 02
    )

    DeclNpc(
        X                   = 44200,
        Z                   = 240,
        Y                   = 18540,
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
        X                   = 44200,
        Z                   = 240,
        Y                   = 18540,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1C5,
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
        Unknown3            = 262146,
        ChipIndex           = 0x2,
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

    DeclNpc(
        X                   = 4110,
        Z                   = -1000,
        Y                   = -46140,
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


    ScpFunction(
        "Function_0_22E",          # 00, 0
        "Function_1_26C",          # 01, 1
        "Function_2_270",          # 02, 2
        "Function_3_31E",          # 03, 3
    )


    def Function_0_22E(): pass

    label("Function_0_22E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_259")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 3)
    Jump("loc_26B")

    label("loc_259")

    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    Event(0, 2)

    label("loc_26B")

    Return()

    # Function_0_22E end

    def Function_1_26C(): pass

    label("Function_1_26C")

    OP_82(0x80, 0x2)
    Return()

    # Function_1_26C end

    def Function_2_270(): pass

    label("Function_2_270")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, -4360, 0, -2200, 0)
    OP_6D(-500, -1000, -18840, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3490, 0)
    OP_6C(311000, 0)
    OP_6E(328, 0)

    def lambda_2D0():
        OP_6D(-920, 1000, 740, 10000)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_2D0)

    def lambda_2E8():
        OP_6C(317000, 10000)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2E8)
    FadeToBright(3000, 0)
    OP_0D()
    WaitChrThread(0x13, 0x0)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T0311   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_270 end

    def Function_3_31E(): pass

    label("Function_3_31E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, -4360, 0, -2200, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 2100, 450, -1510, 180)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x4)
    SetChrPos(0x11, 9600, 620, -2310, 90)
    SetChrPos(0x12, 10000, 1100, -3300, 0)
    ClearChrFlags(0x12, 0x80)
    OP_6D(2000, 450, -640, 0)
    OP_67(0, 8540, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)

    def lambda_3C5():
        OP_6D(2000, 0, -2280, 6000)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_3C5)

    def lambda_3DD():
        OP_67(0, 6500, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_3DD)

    def lambda_3F5():
        OP_6B(2860, 6000)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_3F5)
    FadeToBright(4000, 0)
    OP_0D()
    OP_72(0x800, 0x0)
    ExitThread()
    OP_72(0x1000, 0x0)
    ExitThread()
    OP_6F(0x0, 0)
    OP_70(0x0, 0x1D)
    OP_73(0x0)

    def lambda_42C():
        OP_8F(0xFE, 0x7D0, 0x1C2, 0xFFFFEF02, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_42C)
    WaitChrThread(0x10, 0x1)
    OP_6F(0x0, 29)
    OP_70(0x0, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    Sleep(500)

    NpcTalk(    #0
        0x11,
        "男性的声音",
        "…………约修亚。\x02",
    )

    CloseMessageWindow()

    def lambda_48F():
        OP_6D(4480, 0, -2420, 3500)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_48F)

    def lambda_4A7():
        OP_6C(299000, 3500)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_4A7)
    WaitChrThread(0x13, 0x0)
    Sleep(500)

    ChrTalk(    #1
        0x11,
        "#085F#5P你又睡在外面了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x10,
        "#1676F………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x11,
        (
            "#080F#5P你还是不想\x01",
            "和艾丝蒂尔住一个房间吗。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_549():
        OP_6D(7130, 450, -2330, 3000)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_549)

    def lambda_561():
        OP_6C(298000, 3000)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_561)

    def lambda_571():
        OP_6B(2700, 3000)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_571)

    def lambda_581():
        OP_67(0, 5220, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_581)
    OP_8E(0x10, 0x19C8, 0x1C2, 0xFFFFF1A0, 0x5DC, 0x0)
    WaitChrThread(0x13, 0x0)
    Sleep(500)

    ChrTalk(    #4
        0x10,
        (
            "#1671F#5P……那女孩太多管闲事了。\x02\x03",

            "而且什么也不明白。\x02\x03",

            "#1675F甚至不知道\x01",
            "自己在做多么危险的事……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #5
        0x10,
        (
            "#1670F#5P卡西乌斯·布莱特。\x01",
            "你应该告诉她吧。\x02\x03",

            "……为什么你什么也不说！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x11)
    Sleep(500)

    ChrTalk(    #6
        0x11,
        (
            "#085F#6P……艾丝蒂尔旁边的房间，\x01",
            "现在还是仓库……\x02\x03",

            "#080F就收拾收拾给你用吧。\x02\x03",

            "记得还有张床呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x10,
        (
            "#1676F#5P…………不用麻烦了。\x02\x03",

            "#1676F我不需要。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x11,
        (
            "#085F#6P嗯…………\x02\x03",

            "艾丝蒂尔那家伙\x01",
            "确实什么事都喜欢出头。\x02\x03",

            "从你的视角来看，\x01",
            "实在是单纯得不知世事，\x01",
            "只不过是个孩子而已吧。\x02\x03",

            "但是呢，约修亚……\x02\x03",

            "#082F……其实什么也不明白的\x01",
            "反而是你才对哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x10,
        "#1678F#5P……………………！！\x02",
    )

    Sleep(100)
    OP_7C(0x0, 0x64, 0xBB8, 0xC8)
    CloseMessageWindow()

    ChrTalk(    #10
        0x11,
        (
            "#080F#6P至少那孩子对于自己\x01",
            "想要什么、该做什么，\x01",
            "有她自己的见解。\x02\x03",

            "这是那孩子\x01",
            "之所以有自己特色的\x01",
            "必要条件吧。\x02\x03",

            "#083F……虽然我作为父亲\x01",
            "还是希望她能\x01",
            "更像个女孩子一点……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x10,
        "#1675F#5P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x11,
        (
            "#085F#6P可是，约修亚……\x02\x03",

            "她和连自己想要什么该做什么\x01",
            "都不明白的你相比………\x02\x03",

            "#082F到底谁更正确呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x10,
        "#1675F#5P#40W………我………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x11,
        (
            "#085F#6P……话说在前头，\x01",
            "我并不打算纵容你。\x02\x03",

            "也不会要求你走或者留下来。\x02\x03",

            "#080F你今后要去哪里，\x01",
            "想做什么……\x02\x03",

            "以及想成为什么样的人，\x01",
            "都由你自己来决定。\x02\x03",

            "#085F因为这是……\x01",
            "谁也不知道答案的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x10,
        (
            "#1675F#5P#40W………………………………\x02\x03",

            "#40W……我………………\x02\x03",

            "#60W（我……到底……？）\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B86():
        OP_6B(2600, 3000)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_B86)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0xFA0)
    OP_21()
    Sleep(1000)
    NewScene("ED6_DT21/R0201   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_31E end

    SaveToFile()

Try(main)
