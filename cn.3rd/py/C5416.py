from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C5416   ._SN',
        MapName             = 'Other',
        Location            = 'C5416.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60000",
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
        '小丑肯帕雷拉',                         # 9
        '怀斯曼之杖',                           # 10
        '杖之光',                               # 11
        '使徒 No.Ⅰ',                           # 12
        '使徒 No.Ⅱ',                           # 13
        '使徒 No.Ⅳ',                           # 14
        '使徒 No.Ⅴ',                           # 15
        '使徒 No.Ⅵ',                           # 16
        '使徒 No.Ⅶ',                           # 17
        '盟主',                                 # 18
        '目标用照相机',                         # 19
        '',                                     # 20
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT27/CH03600 ._CH',             # 00
        'ED6_DT26/CH20766 ._CH',             # 01
        'ED6_DT26/CH20485 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT27/CH03600P._CP',             # 00
        'ED6_DT26/CH20766P._CP',             # 01
        'ED6_DT26/CH20485P._CP',             # 02
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C4,
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
        NpcIndex            = 0x1C4,
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
        NpcIndex            = 0x1C4,
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
        NpcIndex            = 0x1C4,
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
        NpcIndex            = 0x1C4,
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
        NpcIndex            = 0x1C4,
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
        NpcIndex            = 0x1C4,
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
        "Function_0_222",          # 00, 0
        "Function_1_24B",          # 01, 1
        "Function_2_308",          # 02, 2
        "Function_3_1144",         # 03, 3
        "Function_4_34A7",         # 04, 4
        "Function_5_350A",         # 05, 5
        "Function_6_3521",         # 06, 6
        "Function_7_3647",         # 07, 7
        "Function_8_3682",         # 08, 8
        "Function_9_36BD",         # 09, 9
        "Function_10_36EE",        # 0A, 10
        "Function_11_3729",        # 0B, 11
        "Function_12_3764",        # 0C, 12
        "Function_13_379F",        # 0D, 13
    )


    def Function_0_222(): pass

    label("Function_0_222")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1D), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_24A")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xE0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 3)

    label("loc_24A")

    Return()

    # Function_0_222 end

    def Function_1_24B(): pass

    label("Function_1_24B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_307")
    OP_82(0x80, 0x0)
    OP_82(0x82, 0x0)
    OP_82(0x83, 0x0)
    OP_82(0x84, 0x0)
    OP_82(0x85, 0x0)
    OP_82(0x86, 0x0)
    OP_82(0x87, 0x0)
    OP_82(0x88, 0x0)
    OP_72(0x800, 0x0)
    ExitThread()
    OP_72(0x2000, 0x0)
    ExitThread()
    OP_6F(0x0, 0)
    OP_72(0x801, 0x0)
    ExitThread()
    OP_72(0x2001, 0x0)
    ExitThread()
    OP_6F(0x1, 0)
    OP_72(0x802, 0x0)
    ExitThread()
    OP_72(0x2002, 0x0)
    ExitThread()
    OP_6F(0x2, 0)
    OP_72(0x803, 0x0)
    ExitThread()
    OP_72(0x2003, 0x0)
    ExitThread()
    OP_6F(0x3, 0)
    OP_72(0x804, 0x0)
    ExitThread()
    OP_72(0x2004, 0x0)
    ExitThread()
    OP_6F(0x4, 0)
    OP_72(0x805, 0x0)
    ExitThread()
    OP_72(0x2005, 0x0)
    ExitThread()
    OP_6F(0x5, 0)
    OP_72(0x806, 0x0)
    ExitThread()
    OP_72(0x2006, 0x0)
    ExitThread()
    OP_6F(0x6, 0)
    OP_72(0x807, 0x0)
    ExitThread()
    OP_72(0x2007, 0x0)
    ExitThread()
    OP_6F(0x7, 0)

    label("loc_307")

    Return()

    # Function_1_24B end

    def Function_2_308(): pass

    label("Function_2_308")

    EventBegin(0x0)
    OP_4F(0x43, (scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 0, -100, -2940, 0)
    SetChrFlags(0x11, 0x800)
    SetChrFlags(0x11, 0x2)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 0, -100, -1940, 0)
    SetChrChipByIndex(0x11, 2)
    SetChrSubChip(0x11, 5)
    OP_6D(1180, -100, -1600, 0)
    OP_67(0, 4690, -10000, 0)
    OP_6B(3520, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Fade(500)
    OP_6D(0, -1900, 2700, 0)
    OP_67(0, 5280, -10000, 0)
    OP_6B(3030, 0)
    OP_6C(0, 0)
    OP_6E(558, 0)

    def lambda_3ED():
        OP_6D(0, 0, 4000, 5000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_3ED)

    def lambda_405():
        OP_67(0, 3900, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_405)

    def lambda_41D():
        OP_6B(4000, 5000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_41D)

    def lambda_42D():
        OP_6E(644, 5000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_42D)
    OP_22(0xEB, 0x0, 0x64)
    OP_43(0x13, 0x0, 0x0, 0x7)
    Sleep(500)
    OP_43(0x14, 0x0, 0x0, 0x8)
    Sleep(500)
    OP_43(0x19, 0x0, 0x0, 0x9)
    Sleep(500)
    OP_43(0x15, 0x0, 0x0, 0xA)
    Sleep(500)
    OP_43(0x16, 0x0, 0x0, 0xB)
    Sleep(500)
    OP_43(0x17, 0x0, 0x0, 0xC)
    Sleep(500)
    OP_43(0x18, 0x0, 0x0, 0xD)
    Sleep(1000)
    OP_23(0xEB)
    WaitChrThread(0x18, 0x0)
    WaitChrThread(0x0, 0x0)
    OP_22(0x13D, 0x0, 0x64)
    OP_22(0x1BF, 0x0, 0x64)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(600)
    OP_22(0x13D, 0x0, 0x64)
    OP_22(0x1BF, 0x0, 0x64)
    PlayEffect(0x87, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(600)
    OP_22(0x13D, 0x0, 0x64)
    OP_22(0x1BF, 0x0, 0x64)
    PlayEffect(0x86, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(600)
    OP_22(0x13D, 0x0, 0x64)
    OP_22(0x1BF, 0x0, 0x64)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(600)
    OP_22(0x13D, 0x0, 0x64)
    OP_22(0x1BF, 0x0, 0x64)
    PlayEffect(0x85, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(600)
    OP_22(0x13D, 0x0, 0x64)
    OP_22(0x1BF, 0x0, 0x64)
    PlayEffect(0x84, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(600)
    OP_9F(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 500, 3000, 12000, 0)
    OP_9F(0x14, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -9720, 3000, 8420, 0)
    OP_9F(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 13850, 3000, 580, 0)
    OP_9F(0x16, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, -13650, 3000, 730, 0)
    OP_9F(0x17, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, -9640, 3000, -7050, 0)
    OP_9F(0x18, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, 9870, 3000, -7050, 0)
    Sleep(1500)

    NpcTalk(    #0
        0x17,
        "声音",
        "#4P唔，等得好苦啊……\x02",
    )

    Jump("loc_727")

    label("loc_727")

    CloseMessageWindow()

    NpcTalk(    #1
        0x18,
        "声音",
        "#3P辛苦你了……\x02",
    )

    Jump("loc_749")

    label("loc_749")

    CloseMessageWindow()

    NpcTalk(    #2
        0x16,
        "声音",
        "#2P这就是『环』的本体吗……\x02",
    )

    Jump("loc_777")

    label("loc_777")

    CloseMessageWindow()

    NpcTalk(    #3
        0x15,
        "声音",
        "#1P看来回收得很顺利……\x02",
    )

    Jump("loc_7A1")

    label("loc_7A1")

    CloseMessageWindow()

    NpcTalk(    #4
        0x14,
        "声音",
        (
            "#5P可是，又付出了牺牲……\x02\x03",

            "这样的事情也不应该忘记……\x02",
        )
    )

    Jump("loc_7EB")

    label("loc_7EB")

    CloseMessageWindow()

    NpcTalk(    #5
        0x13,
        "声音",
        (
            "#5P……大家都安静。\x02\x03",

            "『盟主』要降临了……\x02",
        )
    )

    Jump("loc_829")

    label("loc_829")

    CloseMessageWindow()
    Sleep(300)
    OP_1D(0x79)
    Fade(500)
    OP_6D(0, -1550, 7650, 0)
    OP_67(0, 3780, -10000, 0)
    OP_6B(2350, 0)
    OP_6C(0, 0)
    OP_6E(826, 0)
    OP_0D()
    Fade(250)
    SetChrChipByIndex(0x10, 1)
    SetChrSubChip(0x10, 0)
    OP_0D()
    OP_99(0x10, 0x0, 0x3, 0x5DC)

    def lambda_893():
        OP_6D(0, 8500, 16050, 3500)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_893)

    def lambda_8AB():
        OP_67(0, -2100, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_8AB)

    def lambda_8C3():
        OP_6B(2510, 3500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_8C3)

    def lambda_8D3():
        OP_6E(864, 3500)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_8D3)
    Sleep(500)
    OP_22(0xEB, 0x0, 0x64)
    OP_6F(0x7, 0)
    OP_70(0x7, 0x140)
    Sleep(3000)
    OP_23(0xEB)
    OP_73(0x7)
    WaitChrThread(0x0, 0x0)
    OP_22(0x13D, 0x0, 0x64)
    OP_22(0x1BF, 0x0, 0x64)
    PlayEffect(0x88, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(2000)
    OP_9F(0x19, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, 800, 8000, 19010, 0)
    Sleep(1000)
    Fade(500)
    OP_6D(1430, 2890, 5390, 0)
    OP_67(0, 1920, -10000, 0)
    OP_6B(2950, 0)
    OP_6C(44000, 0)
    OP_6E(940, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #6
        0x10,
        (
            "#850F#4PＮｏ．０――\x01",
            "『小丑肯帕雷拉』。\x02\x03",

            "――前来复命。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #7
        0x19,
        "声音",
        (
            "#5P抬起头来吧――\x02\x03",

            "还有，肯帕雷拉啊――\x02\x03",

            "――世界的动向\x01",
            "是否如我所料？\x02",
        )
    )

    Jump("loc_A54")

    label("loc_A54")

    CloseMessageWindow()
    Sleep(300)
    OP_99(0x10, 0x3, 0x0, 0x5DC)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 0)), scpexpr(EXPR_END)), "loc_B47")

    ChrTalk(    #8
        0x10,
        (
            "#850F是……\x02\x03",

            "正如『盟主』的预言，\x01",
            "虽然『环』启动成功――\x02\x03",

            "但由于之后产生的不确定要素，\x01",
            "『第三支柱』以及执行者Ｎｏ．Ⅱ\x01",
            "相继踏上去往『外』的旅程。\x02\x03",

            "此外，Ｎｏ．Ⅵ、Ｎｏ．ⅩⅤ\x01",
            "目前也行踪不明。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C08")

    label("loc_B47")


    ChrTalk(    #9
        0x10,
        (
            "#850F是……\x02\x03",

            "正如『盟主』的预言，\x01",
            "虽然『环』启动成功――\x02\x03",

            "但由于之后产生的不确定要素，\x01",
            "『第三支柱』以及执行者Ｎｏ．Ⅱ\x01",
            "相继踏上去往『外』的旅程。\x02\x03",

            "此外，Ｎｏ．ⅩⅤ\x01",
            "目前也行踪不明。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C08")


    NpcTalk(    #10
        0x19,
        "声音",
        (
            "真可悲――\x02\x03",

            "还是没能\x01",
            "通过试炼啊。\x02",
        )
    )

    Jump("loc_C49")

    label("loc_C49")

    CloseMessageWindow()

    ChrTalk(    #11
        0x10,
        (
            "#850F#4P请不要责怪自己。\x02\x03",

            "我们已经获得了\x01",
            "足以弥补这牺牲的胜利――\x02\x03",

            "――请收下吧。\x01",
            "当这『环』回归您手上之时，\x01",
            "『福音计划』也将完成。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(500)
    OP_6D(1180, -100, -1600, 0)
    OP_67(0, 4690, -10000, 0)
    OP_6B(3520, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    def lambda_D27():

        label("loc_D27")

        OP_99(0xFE, 0x8, 0xF, 0x5DC)
        OP_48()
        Jump("loc_D27")

    QueueWorkItem2(0x11, 0, lambda_D27)
    Sleep(2000)
    Fade(300)
    OP_44(0x11, 0x0)
    SetChrSubChip(0x11, 5)
    OP_9F(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 0, -600, -1940, 0)
    OP_22(0x138, 0x0, 0x64)
    LoadEffect(0x0, "monster\\ms31000.eff")
    PlayEffect(0x0, 0x0, 0x12, 200, 800, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(1000)
    OP_8F(0x12, 0x0, 0x578, 0xFFFFF86C, 0x7D0, 0x0)
    PlayEffect(0x0, 0x1, 0x12, 200, 800, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Sleep(300)

    def lambda_E12():
        OP_6D(7550, 2000, 23500, 2500)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_E12)

    def lambda_E2A():
        OP_67(0, 6030, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_E2A)

    def lambda_E42():
        OP_6B(3830, 2500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_E42)

    def lambda_E52():
        OP_6E(421, 2500)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_E52)
    OP_43(0x12, 0x0, 0x0, 0x6)
    WaitChrThread(0x12, 0x0)
    WaitChrThread(0x0, 0x0)
    Sleep(1000)

    NpcTalk(    #12
        0x19,
        "声音",
        (
            "#5P『辉之环』――\x01",
            "终于回归吾之手中了吗。\x02",
        )
    )

    Jump("loc_EAC")

    label("loc_EAC")

    CloseMessageWindow()
    Sleep(500)
    OP_22(0x138, 0x0, 0x64)
    PlayEffect(0x0, 0x0, 0x12, 200, 800, 0, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    OP_22(0x2DF, 0x0, 0x64)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    Sleep(2000)
    Fade(500)
    OP_6D(1430, 2890, 5390, 0)
    OP_67(0, 1920, -10000, 0)
    OP_6B(2950, 0)
    OP_6C(44000, 0)
    OP_6E(940, 0)
    OP_0D()
    Sleep(300)

    NpcTalk(    #13
        0x19,
        "声音",
        (
            "#5P西方的钟已敲响，\x01",
            "第一至宝的任务完成了。\x02\x03",

            "此刻，我宣布\x01",
            "『福音计划』完毕――\x02\x03",

            "以及下一计划――\x01",
            "『奥菲斯』启动。\x02",
        )
    )

    Jump("loc_FCF")

    label("loc_FCF")

    CloseMessageWindow()
    Sleep(1000)
    OP_20(0x7D0)
    Fade(2000)
    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    OP_82(0x82, 0x0)
    OP_82(0x83, 0x0)
    OP_82(0x84, 0x0)
    OP_82(0x85, 0x0)
    OP_82(0x86, 0x0)
    OP_82(0x87, 0x0)
    OP_82(0x88, 0x0)
    OP_72(0x800, 0x0)
    ExitThread()
    OP_72(0x2000, 0x0)
    ExitThread()
    OP_6F(0x0, 0)
    OP_72(0x801, 0x0)
    ExitThread()
    OP_72(0x2001, 0x0)
    ExitThread()
    OP_6F(0x1, 0)
    OP_72(0x802, 0x0)
    ExitThread()
    OP_72(0x2002, 0x0)
    ExitThread()
    OP_6F(0x2, 0)
    OP_72(0x803, 0x0)
    ExitThread()
    OP_72(0x2003, 0x0)
    ExitThread()
    OP_6F(0x3, 0)
    OP_72(0x804, 0x0)
    ExitThread()
    OP_72(0x2004, 0x0)
    ExitThread()
    OP_6F(0x4, 0)
    OP_72(0x805, 0x0)
    ExitThread()
    OP_72(0x2005, 0x0)
    ExitThread()
    OP_6F(0x5, 0)
    OP_72(0x806, 0x0)
    ExitThread()
    OP_72(0x2006, 0x0)
    ExitThread()
    OP_6F(0x6, 0)
    OP_72(0x807, 0x0)
    ExitThread()
    OP_72(0x2007, 0x0)
    ExitThread()
    OP_6F(0x7, 0)
    OP_6D(51430, 2890, 5390, 0)
    OP_67(0, 1920, -10000, 0)
    OP_6B(2950, 0)
    OP_6C(44000, 0)
    OP_6E(940, 0)
    SetChrPos(0x10, 50000, -100, -2940, 0)
    OP_0D()
    Sleep(1000)
    Fade(500)
    OP_6D(50770, -100, -1860, 0)
    OP_67(0, 6490, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(308, 0)
    OP_0D()
    Sleep(1000)
    OP_A2(0x2507)
    OP_4F(0x43, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("ED6_DT21/C5401   ._SN", 100, 1, 0)
    IdleLoop()
    Return()

    # Function_2_308 end

    def Function_3_1144(): pass

    label("Function_3_1144")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    LoadEffect(0x0, "monster\\ms31000.eff")
    LoadEffect(0x1, "map\\\\mp049_22.eff")
    SetChrPos(0x0, 0, 0, -2940, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 0, -100, -2940, 0)
    OP_6D(0, 0, -320, 0)
    OP_67(0, 6020, -10000, 0)
    OP_6B(2500, 0)
    OP_6C(0, 0)
    OP_6E(558, 0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C8(0x200, 0x46, "C_PLAC40._CH", 0x0, 0x3E8)
    FadeToBright(2500, 0)
    OP_6B(1700, 4000)
    OP_0D()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1500)
    SetMessageWindowPos(-1, 90, -1, -1)
    SetChrName("声音")

    AnonymousTalk(    #14
        "\x07\x05……等得好苦啊……\x02",
    )

    Jump("loc_1263")

    label("loc_1263")

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #15
        0x10,
        (
            "#853F#6P呵呵……\x01",
            "大家好像都来齐了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_43(0x10, 0x2, 0x0, 0x4)
    Fade(500)
    OP_6D(2280, 0, 10380, 0)
    OP_67(0, 18060, -10000, 0)
    OP_6B(840, 0)
    OP_6C(308000, 0)
    OP_6E(582, 0)
    Sleep(1000)

    def lambda_12ED():
        OP_6D(-780, 0, 10850, 4000)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_12ED)

    def lambda_1305():
        OP_67(0, 4900, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1305)

    def lambda_131D():
        OP_6B(1900, 4000)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_131D)

    def lambda_132D():
        OP_6E(582, 4000)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_132D)

    def lambda_133D():
        OP_6C(36000, 4000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_133D)
    WaitChrThread(0x1A, 0x0)
    Sleep(1000)

    def lambda_1357():
        OP_6D(-8520, 0, -2100, 5000)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_1357)

    def lambda_136F():
        OP_67(0, 4900, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_136F)

    def lambda_1387():
        OP_6B(1900, 5000)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_1387)

    def lambda_1397():
        OP_6E(682, 5000)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_1397)

    def lambda_13A7():
        OP_6C(306000, 5000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_13A7)
    WaitChrThread(0x1A, 0x0)
    Sleep(1000)
    Fade(500)
    OP_6D(8520, 0, -2100, 0)
    OP_67(0, 4900, -10000, 0)
    OP_6B(1900, 0)
    OP_6C(54000, 0)
    OP_6E(682, 0)

    def lambda_1403():
        OP_6D(0, 0, 0, 5000)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_1403)

    def lambda_141B():
        OP_67(0, 5560, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_141B)

    def lambda_1433():
        OP_6B(2320, 5000)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_1433)

    def lambda_1443():
        OP_6E(964, 5000)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_1443)

    def lambda_1453():
        OP_6C(0, 5000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_1453)
    WaitChrThread(0x1A, 0x0)
    Sleep(2000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_1476():
        OP_67(0, 5060, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1476)

    def lambda_148E():
        OP_6B(2620, 3000)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_148E)
    OP_22(0x13D, 0x0, 0x64)
    OP_22(0x1BF, 0x0, 0x64)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x87, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x86, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x85, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x84, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(4000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(-730, 0, -2029, 0)
    OP_67(0, 5280, -10000, 0)
    OP_6B(1020, 0)
    OP_6C(312000, 0)
    OP_6E(795, 0)
    OP_0D()
    Sleep(1000)
    SetMessageWindowPos(400, 100, -1, -1)
    SetChrName("第五支柱")

    AnonymousTalk(    #16
        (
            "\x07\x05不过……\x01",
            "没想到『白面』会被打败啊。\x02",
        )
    )

    Jump("loc_168F")

    label("loc_168F")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(200, 50, -1, -1)
    SetChrName("第二支柱")

    AnonymousTalk(    #17
        (
            "\x07\x05呵呵，看来他在\x01",
            "自己的老巢顽皮过头了。\x02\x03",

            "喂，肯帕雷拉。\x01",
            "他是怎么死的？\x02",
        )
    )

    Jump("loc_1706")

    label("loc_1706")

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #18
        0x10,
        (
            "#853F呵呵，那可是杰作啊。\x02\x03",

            "#854F从头顶到指尖\x01",
            "全都变成了盐。\x02\x03",

            "到最后\x01",
            "就粉身碎骨了。\x02",
        )
    )

    Jump("loc_177E")

    label("loc_177E")

    CloseMessageWindow()
    SetMessageWindowPos(200, 50, -1, -1)
    SetChrName("第二支柱")

    AnonymousTalk(    #19
        (
            "\x07\x05哇……\x01",
            "真让人毛骨悚然。\x02\x03",

            "啊啊，\x01",
            "要是我也在场就好了。\x02",
        )
    )

    Jump("loc_17F5")

    label("loc_17F5")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(20, 320, -1, -1)
    SetChrName("第六支柱")

    AnonymousTalk(    #20
        (
            "\x07\x05『盐之桩』……\x01",
            "在诺桑普里亚出现的\x01",
            "那个特异产物吗。\x02\x03",

            "嗯～\x01",
            "真想亲眼见一下实物……\x02",
        )
    )

    Jump("loc_187D")

    label("loc_187D")

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(300)
    OP_44(0x1A, 0xFF)
    OP_44(0x10, 0xFF)
    Fade(500)
    OP_6D(-4940, 2000, 560, 0)
    OP_67(0, 3400, -10000, 0)
    OP_6B(2220, 0)
    OP_6B(2620, 0)
    OP_6C(119000, 0)
    OP_6E(706, 0)
    OP_0D()

    def lambda_18DF():
        OP_6B(2200, 25000)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_18DF)
    Sleep(1000)
    SetMessageWindowPos(380, 310, -1, -1)
    SetChrName("第四支柱")

    AnonymousTalk(    #21
        (
            "\x07\x05哈哈，不过真意外啊。\x02\x03",

            "那个精明的人\x01",
            "竟会露出这种破绽。\x02",
        )
    )

    Jump("loc_1953")

    label("loc_1953")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(30, 50, -1, -1)
    SetChrName("第五支柱")

    AnonymousTalk(    #22
        (
            "\x07\x05……恐怕对手是\x01",
            "『守护骑士』之一吧。\x02\x03",

            "而且一定是至今为止\x01",
            "都缺席的『第五位』。\x02",
        )
    )

    Jump("loc_19D2")

    label("loc_19D2")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(380, 310, -1, -1)
    SetChrName("第四支柱")

    AnonymousTalk(    #23
        (
            "\x07\x05原来如此啊……\x01",
            "所以才会出现破绽吗。\x02\x03",

            "那家伙，叫什么名字？\x02",
        )
    )

    Jump("loc_1A3E")

    label("loc_1A3E")

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #24
        0x10,
        (
            "#853F#11P──凯文·格拉汉姆。\x02\x03",

            "他师从于那个『红耀石』，\x01",
            "名号『异端制裁者』。\x02\x03",

            "#854F呵呵，\x01",
            "是个非常古怪有趣的大哥呢。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(30, 320, -1, -1)
    SetChrName("第二支柱")

    AnonymousTalk(    #25
        (
            "\x07\x05『红耀石』的……\x02\x03",

            "嘻嘻，\x01",
            "感觉越来越有意思了呢。\x02",
        )
    )

    Jump("loc_1B38")

    label("loc_1B38")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(380, 310, -1, -1)
    SetChrName("第四支柱")

    AnonymousTalk(    #26
        (
            "\x07\x05喂喂，『深渊』。\x02\x03",

            "你曾经那么中意莱恩哈特，\x01",
            "他刚一死，\x01",
            "你就马上要另寻新欢了？\x02",
        )
    )

    Jump("loc_1BB7")

    label("loc_1BB7")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(30, 320, -1, -1)
    SetChrName("第二支柱")

    AnonymousTalk(    #27
        (
            "\x07\x05哎呀，什么话。\x02\x03",

            "我这也是\x01",
            "在为莱恩伤心啊。\x02\x03",

            "直到最后\x01",
            "他也没转投我的怀抱，\x01",
            "真是更让人难以忘怀了。\x02",
        )
    )

    Jump("loc_1C67")

    label("loc_1C67")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(300, 30, -1, -1)
    SetChrName("第七支柱")

    AnonymousTalk(    #28
        (
            "\x07\x05……是啊。\x02\x03",

            "那么优秀的剑士，\x01",
            "真是可惜了。\x02",
        )
    )

    Jump("loc_1CC3")

    label("loc_1CC3")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(30, 50, -1, -1)
    SetChrName("第五支柱")

    AnonymousTalk(    #29
        (
            "\x07\x05执行者之中\x01",
            "能和您比剑的\x01",
            "好像也只有他了……\x02",
        )
    )

    Jump("loc_1D1A")

    label("loc_1D1A")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(300, 20, -1, -1)
    SetChrName("第七支柱")

    AnonymousTalk(    #30
        (
            "\x07\x05是啊，\x01",
            "我经常勉强他陪我练习的。\x02\x03",

            "总有一天会成为\x01",
            "凌驾我之上的剑士吧。\x02\x03",

            "一想到这个还真是觉得可惜……\x02",
        )
    )

    Jump("loc_1DBE")

    label("loc_1DBE")

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(300)
    OP_44(0x1A, 0xFF)
    OP_44(0x10, 0xFF)
    Fade(1000)
    OP_6D(-6200, 1000, -3100, 0)
    OP_67(0, 4090, -10000, 0)
    OP_6B(2400, 0)
    OP_6C(41000, 0)
    OP_6E(698, 0)
    OP_0D()

    def lambda_1E17():
        OP_6B(2100, 25000)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1E17)
    Sleep(500)
    SetMessageWindowPos(200, 300, -1, -1)
    SetChrName("第六支柱")

    AnonymousTalk(    #31
        (
            "\x07\x05呵呵，这个没什么问题吧？\x02\x03",

            "整体战斗力损失是极其轻微的——\x01",
            "而且在预定范围之内哦。\x02\x03",

            "考虑到今后的影响，\x01",
            "『歼灭天使』才是大问题。\x02",
        )
    )

    Jump("loc_1ED8")

    label("loc_1ED8")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(0, 250, -1, -1)
    SetChrName("第四支柱")

    AnonymousTalk(    #32
        (
            "\x07\x05哈哈，那个小姑娘吗。\x02\x03",

            "她的心情似乎相当混乱，\x01",
            "到底会不会回来呢？\x02",
        )
    )

    Jump("loc_1F4A")

    label("loc_1F4A")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("第一支柱")

    AnonymousTalk(    #33
        (
            "\x07\x05嗯，这要看她自己了。\x02\x03",

            "虽然我们地位在他们之上，\x01",
            "但也无法限制他们的行动。\x02\x03",

            "这是『规定』。\x02",
        )
    )

    Jump("loc_1FDA")

    label("loc_1FDA")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(200, 300, -1, -1)
    SetChrName("第六支柱")

    AnonymousTalk(    #34
        "\x07\x05……但是啊………\x02",
    )

    Jump("loc_2017")

    label("loc_2017")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("第一支柱")

    AnonymousTalk(    #35
        (
            "\x07\x05博士，\x01",
            "我们也十分理解\x01",
            "『极限级』的重要程度。\x02\x03",

            "……但这是\x01",
            "那位大人所做的『规定』。\x02\x03",

            "这意思您明白吧？\x02",
        )
    )

    Jump("loc_20BC")

    label("loc_20BC")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(200, 300, -1, -1)
    SetChrName("第六支柱")

    AnonymousTalk(    #36
        "\x07\x05………………………………\x02",
    )

    Jump("loc_2101")

    label("loc_2101")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(10, 80, -1, -1)
    SetChrName("第二支柱")

    AnonymousTalk(    #37
        (
            "\x07\x05呵呵……\x01",
            "我觉得教授对那个漆黑小子的执着\x01",
            "似乎有些过度了。\x02",
        )
    )

    Jump("loc_2172")

    label("loc_2172")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("第一支柱")

    AnonymousTalk(    #38
        (
            "\x07\x05对，而这事实上\x01",
            "就是毁灭他的契机……\x02\x03",

            "对吧，肯帕雷拉？\x02",
        )
    )

    Jump("loc_21DA")

    label("loc_21DA")

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #39
        0x10,
        (
            "#853F#12P呵呵，过分拘泥于\x01",
            "约修亚确实是败因之一。\x02\x03",

            "#854F那个凯文似乎\x01",
            "也是看准了这一点。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(200, 300, -1, -1)
    SetChrName("第六支柱")

    AnonymousTalk(    #40
        (
            "\x07\x05……是是，我知道了。\x02\x03",

            "但是，我也是\x01",
            "管理『十三工房』的人。\x02\x03",

            "就算是为了确认\x01",
            "『极限级』的使用状况，\x01",
            "我也必须继续监视。\x02",
        )
    )

    Jump("loc_22F0")

    label("loc_22F0")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("第一支柱")

    AnonymousTalk(    #41
        (
            "\x07\x05嗯，那就交给你了。\x02\x03",

            "对了，各位──\x01",
            "盟主差不多要降临了哦。\x02",
        )
    )

    Jump("loc_235C")

    label("loc_235C")

    CloseMessageWindow()
    OP_56(0x0)
    OP_20(0x7D0)
    Sleep(500)
    SetMessageWindowPos(360, 10, -1, -1)
    SetChrName("第五支柱")

    AnonymousTalk(    #42
        "\x07\x05嗯……是吗。\x02",
    )

    Jump("loc_239F")

    label("loc_239F")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(10, 80, -1, -1)
    SetChrName("第二支柱")

    AnonymousTalk(    #43
        (
            "\x07\x05嘻嘻……\x01",
            "真令人兴奋啊。\x02",
        )
    )

    Jump("loc_23EF")

    label("loc_23EF")

    CloseMessageWindow()
    OP_56(0x0)
    OP_21()
    OP_1D(0xB6)
    Fade(1000)
    OP_44(0x1A, 0xFF)
    OP_6D(0, -1550, 7650, 0)
    OP_67(0, 3780, -10000, 0)
    OP_6B(2550, 0)
    OP_6C(0, 0)
    OP_6E(826, 0)
    OP_0D()

    def lambda_2442():
        OP_6B(2350, 2000)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_2442)
    Sleep(500)
    SetChrChipByIndex(0x10, 1)
    SetChrSubChip(0x10, 0)
    OP_0D()
    OP_99(0x10, 0x0, 0x3, 0x3E8)

    def lambda_246B():
        OP_6D(0, 12000, 16050, 3500)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_246B)

    def lambda_2483():
        OP_67(0, -2500, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_2483)

    def lambda_249B():
        OP_6B(2510, 3500)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_249B)

    def lambda_24AB():
        OP_6E(864, 3500)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_24AB)
    OP_22(0xEB, 0x0, 0x64)
    OP_6F(0x7, 0)
    OP_B0(0x7, 0x1E)
    OP_70(0x7, 0x140)
    Sleep(4500)

    def lambda_24D7():
        OP_6D(0, 8000, 16050, 3000)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_24D7)

    def lambda_24EF():
        OP_67(0, -2000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_24EF)
    Sleep(1000)
    OP_23(0xEB)
    OP_73(0x7)
    WaitChrThread(0x1A, 0x0)
    OP_22(0x13D, 0x0, 0x64)
    OP_22(0x1BF, 0x0, 0x64)
    PlayEffect(0x88, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(4000)

    def lambda_255B():
        OP_6D(5710, 1250, 13110, 3000)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_255B)

    def lambda_2573():
        OP_67(0, 3000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_2573)

    def lambda_258B():
        OP_6B(2950, 3000)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_258B)

    def lambda_259B():
        OP_6E(940, 3000)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_259B)

    def lambda_25AB():
        OP_6C(44000, 3000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_25AB)
    WaitChrThread(0x1A, 0x0)
    Sleep(500)
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(220, 120, -1, -1)
    SetChrName("")

    AnonymousTalk(    #44
        (
            "#7C#40W各位……\x01",
            "似乎都到齐了呢。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(300)
    SetMessageWindowPos(150, 260, -1, -1)
    SetChrName("第一支柱")

    AnonymousTalk(    #45
        (
            "\x07\x05是……\x02\x03",

            "除了『第三支柱』，\x01",
            "全员都到齐了。\x02",
        )
    )

    Jump("loc_268D")

    label("loc_268D")

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(220, 120, -1, -1)
    SetChrName("")

    AnonymousTalk(    #46
        (
            "#7C#40W……辛苦了。#0C\x02\x03",

            "还有，肯帕雷拉……\x01",
            "你作为我的代理见证人，\x01",
            "发挥了重要的作用。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(300)

    ChrTalk(    #47
        0x10,
        (
            "#853F#11P……不胜惶恐。\x02\x03",

            "#853F您应该已经了解了\x01",
            "『福音计划』的始末……\x02\x03",

            "不过请允许我在这里\x01",
            "完成最重要的任务。\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(1380, 0, 820, 0)
    OP_67(0, 3860, -10000, 0)
    OP_6B(2000, 0)
    OP_6C(35000, 0)
    OP_6E(493, 0)
    OP_0D()
    OP_99(0x10, 0x3, 0x5, 0x3E8)
    Sleep(500)
    ClearChrFlags(0x11, 0x1)
    SetChrFlags(0x11, 0x800)
    SetChrFlags(0x11, 0x2)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 0, -100, -740, 90)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x11, 2)
    SetChrSubChip(0x11, 8)

    def lambda_284F():

        label("loc_284F")

        OP_99(0xFE, 0x8, 0xF, 0x4B0)
        OP_48()
        Jump("loc_284F")

    QueueWorkItem2(0x11, 1, lambda_284F)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    PlayEffect(0x1, 0x1, 0x11, 0, 600, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_28A1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_28A1)
    WaitChrThread(0x11, 0x2)
    OP_83(0x1, 0x2)
    Sleep(3000)
    Fade(500)
    OP_44(0x11, 0x1)
    OP_44(0x11, 0x0)
    SetChrSubChip(0x11, 5)
    OP_9F(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 0, -600, -740, 0)
    OP_22(0x138, 0x0, 0x64)
    PlayEffect(0x0, 0x0, 0x12, 200, 800, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(1000)

    def lambda_2933():
        OP_6D(1380, 500, 820, 2000)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_2933)
    OP_8F(0x12, 0x0, 0x578, 0xFFFFFD1C, 0x3E8, 0x0)
    PlayEffect(0x0, 0x1, 0x12, 200, 800, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0x1A, 0x0)
    Sleep(500)
    SetMessageWindowPos(400, 50, -1, -1)
    SetChrName("第五支柱")

    AnonymousTalk(    #48
        "\x07\x05哦哦……！\x02",
    )

    Jump("loc_29CC")

    label("loc_29CC")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(30, 200, -1, -1)
    SetChrName("第二支柱")

    AnonymousTalk(    #49
        "\x07\x05这是……\x02",
    )

    Jump("loc_2A0D")

    label("loc_2A0D")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(70, 320, -1, -1)
    SetChrName("第四支柱")

    AnonymousTalk(    #50
        (
            "\x07\x05七至宝之一，\x01",
            "『辉之环』吗……！\x02",
        )
    )

    Jump("loc_2A59")

    label("loc_2A59")

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(300)

    def lambda_2A67():
        OP_6D(7550, 2000, 23500, 4000)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_2A67)

    def lambda_2A7F():
        OP_67(0, 6030, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_2A7F)

    def lambda_2A97():
        OP_6B(3830, 4000)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_2A97)

    def lambda_2AA7():
        OP_6E(421, 4000)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_2AA7)

    def lambda_2AB7():
        OP_6C(45000, 4000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_2AB7)
    OP_43(0x12, 0x0, 0x0, 0x6)
    WaitChrThread(0x12, 0x0)
    WaitChrThread(0x1A, 0x0)
    Sleep(1000)
    OP_22(0x138, 0x0, 0x64)
    PlayEffect(0x0, 0x0, 0x12, 200, 800, 0, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    OP_22(0x2DF, 0x0, 0x64)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    Sleep(2000)
    Fade(500)
    OP_6D(5710, 1250, 13110, 0)
    OP_67(0, 3000, -10000, 0)
    OP_6B(2950, 0)
    OP_6C(44000, 0)
    OP_6E(940, 0)
    OP_0D()
    Sleep(300)

    def lambda_2B74():
        OP_6D(1430, 2490, 5390, 30000)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_2B74)

    def lambda_2B8C():
        OP_67(0, 1920, -10000, 30000)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_2B8C)
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(200, 120, -1, -1)
    SetChrName("")

    AnonymousTalk(    #51
        (
            "#7C#40W空之至宝……\x01",
            "我已经收下了。\x02\x03",

            "不过……\x01",
            "支付的代价实在过于惨痛。\x02\x03",

            "怀斯曼……\x01",
            "以及莱恩哈特……\x02\x03",

            "不，不仅如此，\x01",
            "与计划相关的所有牺牲……\x02\x03",

            "一切责任都在我身上。#0C\x02",
        )
    )

    Jump("loc_2C8F")

    label("loc_2C8F")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(300)
    SetMessageWindowPos(370, 150, -1, -1)
    SetChrName("第五支柱")

    AnonymousTalk(    #52
        "\x07\x05绝、绝无此事！\x02",
    )

    Jump("loc_2CE7")

    label("loc_2CE7")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(430, 250, -1, -1)
    SetChrName("第七支柱")

    AnonymousTalk(    #53
        (
            "\x07\x05……请您千万\x01",
            "不要责怪自己。\x02\x03",

            "『白面』大人的死\x01",
            "可说是自作自受。\x02",
        )
    )

    Jump("loc_2D58")

    label("loc_2D58")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(20, 280, -1, -1)
    SetChrName("第二支柱")

    AnonymousTalk(    #54
        (
            "\x07\x05一定要责怪的话，\x01",
            "应该怪我们这些没有向他提出劝告\x01",
            "而置之不理的全体『使徒』。\x02",
        )
    )

    Jump("loc_2DCF")

    label("loc_2DCF")

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(200, 120, -1, -1)
    SetChrName("")

    AnonymousTalk(    #55
        (
            "#7C#40W不，这个事态\x01",
            "我早已预料到了。\x02\x03",

            "即使如此……\x01",
            "我还是将所有决定托付于他。\x02\x03",

            "因为我判断，\x01",
            "这对世界来说是必要的……\x02\x03",

            "因此……\x01",
            "一切责任都在我。#0C\x02",
        )
    )

    Jump("loc_2EAB")

    label("loc_2EAB")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(300)
    SetMessageWindowPos(370, 150, -1, -1)
    SetChrName("第五支柱")

    AnonymousTalk(    #56
        "\x07\x05『盟主』啊……\x02",
    )

    Jump("loc_2F03")

    label("loc_2F03")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(420, 250, -1, -1)
    SetChrName("第七支柱")

    AnonymousTalk(    #57
        "\x07\x05为何要如此责怪自己……\x02",
    )

    Jump("loc_2F46")

    label("loc_2F46")

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(200, 120, -1, -1)
    SetChrName("")

    AnonymousTalk(    #58
        (
            "#7C#40W…………………………………\x02\x03",

            "可以预料到\x01",
            "今后会产生的风波……\x02\x03",

            "关于这件事，\x01",
            "教会恐怕会有所行动。\x02\x03",

            "就交给他们吧。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(300)
    SetMessageWindowPos(150, 250, -1, -1)
    SetChrName("第一支柱")

    AnonymousTalk(    #59
        "\x07\x05……明白了。\x02",
    )

    Jump("loc_3052")

    label("loc_3052")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(220, 340, -1, -1)
    SetChrName("第六支柱")

    AnonymousTalk(    #60
        (
            "\x07\x05呵呵……\x01",
            "虽然有点在意，\x01",
            "但就按您的旨意办吧。\x02",
        )
    )

    Jump("loc_30B7")

    label("loc_30B7")

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    SetMessageWindowPos(30, 320, -1, -1)
    SetChrName("第四支柱")

    AnonymousTalk(    #61
        (
            "\x07\x05那么，\x01",
            "今后我们应该如何行动？\x02",
        )
    )

    Jump("loc_310F")

    label("loc_310F")

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(200, 120, -1, -1)
    SetChrName("")

    AnonymousTalk(    #62
        "#7C#40W…………………………………#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(300)
    Fade(1000)
    OP_44(0x1A, 0xFF)
    OP_6D(0, 7500, 8680, 0)
    OP_67(0, -1860, -10000, 0)
    OP_6B(2050, 0)
    OP_6C(0, 0)
    OP_6E(940, 0)
    OP_0D()

    def lambda_31CC():
        OP_6B(3150, 20000)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_31CC)
    Sleep(1000)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(200, 120, -1, -1)
    SetChrName("")

    AnonymousTalk(    #63
        (
            "#7C#40W西方的钟已经敲响，\x01",
            "第一盟约解放完毕。#0C\x02\x03",

            "现在，我宣布——\x01",
            "『奥菲斯最终计划』之一，\x01",
            "『福音计划』完毕──#0C\x02\x03",

            "以及下一阶段──\x01",
            "『幻焰计划』启动。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(500)
    SetMessageWindowPos(380, 275, -1, -1)
    SetChrName("第五支柱")

    AnonymousTalk(    #64
        "\x07\x05哦哦……！\x02",
    )

    Jump("loc_32F9")

    label("loc_32F9")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(20, 200, -1, -1)
    SetChrName("第二支柱")

    AnonymousTalk(    #65
        (
            "\x07\x05嘻嘻……\x01",
            "明白了。\x02",
        )
    )

    Jump("loc_334F")

    label("loc_334F")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(40, 280, -1, -1)
    SetChrName("第六支柱")

    AnonymousTalk(    #66
        "\x07\x05是，请放心。\x02",
    )

    Jump("loc_3388")

    label("loc_3388")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(80, 340, -1, -1)
    SetChrName("第四支柱")

    AnonymousTalk(    #67
        "\x07\x05我们全体『蛇之使徒』……\x02",
    )

    Jump("loc_33CD")

    label("loc_33CD")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(400, 280, -1, -1)
    SetChrName("第七支柱")

    AnonymousTalk(    #68
        (
            "\x07\x05将遵从\x01",
            "伟大『盟主』的旨意……\x02",
        )
    )

    Jump("loc_3420")

    label("loc_3420")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 320, -1, -1)
    SetChrName("第一支柱")

    AnonymousTalk(    #69
        (
            "\x07\x05今后会竭尽全力\x01",
            "着手实行计划。\x02",
        )
    )

    Jump("loc_346A")

    label("loc_346A")

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToDark(3000, 16777215, -1)
    OP_0D()
    OP_20(0x1388)
    OP_AD(0x240184, 0x0, 0x0, 0x5DC)
    OP_21()
    Sleep(500)
    OP_A2(0x2505)
    NewScene("ED6_DT21/C5401   ._SN", 100, 20, 0)
    IdleLoop()
    Return()

    # Function_3_1144 end

    def Function_4_34A7(): pass

    label("Function_4_34A7")

    OP_43(0x13, 0x3, 0x0, 0x5)
    OP_43(0x13, 0x0, 0x0, 0x7)
    Sleep(3000)
    OP_43(0x14, 0x0, 0x0, 0x8)
    Sleep(1000)
    OP_43(0x15, 0x0, 0x0, 0xA)
    Sleep(1000)
    OP_43(0x17, 0x0, 0x0, 0xC)
    Sleep(4000)
    OP_43(0x19, 0x0, 0x0, 0x9)
    Sleep(1000)
    OP_43(0x16, 0x0, 0x0, 0xB)
    Sleep(1000)
    OP_43(0x18, 0x0, 0x0, 0xD)
    Sleep(5000)
    OP_44(0x13, 0x3)
    OP_23(0xBA)
    Return()

    # Function_4_34A7 end

    def Function_5_350A(): pass

    label("Function_5_350A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3520")
    OP_22(0xBA, 0x0, 0x64)
    Sleep(6000)
    Jump("Function_5_350A")

    label("loc_3520")

    Return()

    # Function_5_350A end

    def Function_6_3521(): pass

    label("Function_6_3521")


    def lambda_3527():
        OP_8F(0xFE, 0x320, 0x1F40, 0x3A98, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3527)
    Sleep(500)

    def lambda_3547():
        OP_8F(0xFE, 0x320, 0x1F40, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3547)
    Sleep(500)

    def lambda_3567():
        OP_8F(0xFE, 0x320, 0x1F40, 0x3A98, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3567)
    Sleep(500)

    def lambda_3587():
        OP_8F(0xFE, 0x320, 0x1F40, 0x3A98, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3587)
    Sleep(500)

    def lambda_35A7():
        OP_8F(0xFE, 0x320, 0x1F40, 0x3A98, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_35A7)
    Sleep(1500)

    def lambda_35C7():
        OP_8F(0xFE, 0x320, 0x1F40, 0x3A98, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_35C7)
    Sleep(500)

    def lambda_35E7():
        OP_8F(0xFE, 0x320, 0x1F40, 0x3A98, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_35E7)
    Sleep(400)

    def lambda_3607():
        OP_8F(0xFE, 0x320, 0x1F40, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3607)
    Sleep(300)

    def lambda_3627():
        OP_8F(0xFE, 0x320, 0x1F40, 0x3A98, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3627)
    Sleep(200)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_6_3521 end

    def Function_7_3647(): pass

    label("Function_7_3647")

    OP_6F(0x0, 0)
    OP_B0(0x0, 0x1E)
    OP_70(0x0, 0x140)
    Sleep(4900)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Sleep(700)
    OP_22(0x2D8, 0x0, 0x64)
    OP_73(0x0)
    Return()

    # Function_7_3647 end

    def Function_8_3682(): pass

    label("Function_8_3682")

    OP_6F(0x1, 0)
    OP_B0(0x1, 0x1E)
    OP_70(0x1, 0x140)
    Sleep(4900)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Sleep(700)
    OP_22(0x2D8, 0x0, 0x64)
    OP_73(0x1)
    Return()

    # Function_8_3682 end

    def Function_9_36BD(): pass

    label("Function_9_36BD")

    OP_6F(0x2, 0)
    OP_B0(0x2, 0x1E)
    OP_70(0x2, 0x140)
    Sleep(4900)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_73(0x2)
    Return()

    # Function_9_36BD end

    def Function_10_36EE(): pass

    label("Function_10_36EE")

    OP_6F(0x3, 0)
    OP_B0(0x3, 0x1E)
    OP_70(0x3, 0x140)
    Sleep(4900)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Sleep(700)
    OP_22(0x2D8, 0x0, 0x64)
    OP_73(0x3)
    Return()

    # Function_10_36EE end

    def Function_11_3729(): pass

    label("Function_11_3729")

    OP_6F(0x4, 0)
    OP_B0(0x4, 0x1E)
    OP_70(0x4, 0x140)
    Sleep(4900)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Sleep(700)
    OP_22(0x2D8, 0x0, 0x64)
    OP_73(0x4)
    Return()

    # Function_11_3729 end

    def Function_12_3764(): pass

    label("Function_12_3764")

    OP_6F(0x5, 0)
    OP_B0(0x5, 0x1E)
    OP_70(0x5, 0x140)
    Sleep(4900)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Sleep(700)
    OP_22(0x2D8, 0x0, 0x64)
    OP_73(0x5)
    Return()

    # Function_12_3764 end

    def Function_13_379F(): pass

    label("Function_13_379F")

    OP_6F(0x6, 0)
    OP_B0(0x6, 0x1E)
    OP_70(0x6, 0x140)
    Sleep(4900)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Sleep(700)
    OP_22(0x2D8, 0x0, 0x64)
    OP_73(0x6)
    Return()

    # Function_13_379F end

    SaveToFile()

Try(main)
