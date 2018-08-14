from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3221   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3221.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60015",
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
        '毛婆婆',                               # 9
        '亚提',                                 # 10
        '金',                                   # 11
        '雾香',                                 # 12
        '爱尔莎大使',                           # 13
        '玻璃杯',                               # 14
        '玻璃杯',                               # 15
        '赫雷思老人',                           # 16
        '目标用摄影机',                         # 17
        '',                                     # 18
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
        'ED6_DT07/CH02430 ._CH',             # 00
        'ED6_DT07/CH01130 ._CH',             # 01
        'ED6_DT07/CH00073 ._CH',             # 02
        'ED6_DT26/CH20815 ._CH',             # 03
        'ED6_DT27/CH03720 ._CH',             # 04
        'ED6_DT27/CH03723 ._CH',             # 05
        'ED6_DT06/CH20021 ._CH',             # 06
        'ED6_DT07/CH01003 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT07/CH02430P._CP',             # 00
        'ED6_DT07/CH01130P._CP',             # 01
        'ED6_DT07/CH00073P._CP',             # 02
        'ED6_DT26/CH20815P._CP',             # 03
        'ED6_DT27/CH03720P._CP',             # 04
        'ED6_DT27/CH03723P._CP',             # 05
        'ED6_DT06/CH20021P._CP',             # 06
        'ED6_DT07/CH01003P._CP',             # 07
    )

    DeclNpc(
        X                   = 2590,
        Z                   = 250,
        Y                   = 5360,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 8490,
        Z                   = 0,
        Y                   = 340,
        Direction           = 102,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        Unknown3            = 327686,
        ChipIndex           = 0x6,
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
        Unknown3            = 327686,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 8760,
        Z                   = 200,
        Y                   = 6600,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x135,
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
        "Function_0_20A",          # 00, 0
        "Function_1_22A",          # 01, 1
        "Function_2_22B",          # 02, 2
        "Function_3_3A8",          # 03, 3
        "Function_4_88C",          # 04, 4
        "Function_5_8CE",          # 05, 5
    )


    def Function_0_20A(): pass

    label("Function_0_20A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_229")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 6)), scpexpr(EXPR_END)), "loc_229")
    OP_A3(0x2506)
    SetMapFlags(0x10000000)
    Event(0, 5)

    label("loc_229")

    Return()

    # Function_0_20A end

    def Function_1_22A(): pass

    label("Function_1_22A")

    Return()

    # Function_1_22A end

    def Function_2_22B(): pass

    label("Function_2_22B")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_250")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_392")

    label("loc_250")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_269")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_392")

    label("loc_269")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_282")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_392")

    label("loc_282")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29B")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_392")

    label("loc_29B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B4")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_392")

    label("loc_2B4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CD")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_392")

    label("loc_2CD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E6")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_392")

    label("loc_2E6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FF")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_392")

    label("loc_2FF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_318")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_392")

    label("loc_318")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_331")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_392")

    label("loc_331")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34A")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_392")

    label("loc_34A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_363")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_392")

    label("loc_363")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37C")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_392")

    label("loc_37C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_392")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_392")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3A7")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_392")

    label("loc_3A7")

    Return()

    # Function_2_22B end

    def Function_3_3A8(): pass

    label("Function_3_3A8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x13, 0x4)
    SetChrFlags(0x12, 0x4)
    SetChrFlags(0x14, 0x4)
    SetChrPos(0x13, 13110, 200, 10890, 180)
    SetChrPos(0x12, 11150, 100, 10870, 125)
    SetChrPos(0x14, 13070, 200, 8320, 0)
    SetChrChipByIndex(0x14, 5)
    SetChrSubChip(0x14, 0)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x15, 0x4)
    SetChrFlags(0x16, 0x4)
    SetChrPos(0x15, 13250, 800, 9750, 0)
    SetChrPos(0x16, 13300, 800, 8900, 0)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    OP_43(0x10, 0x0, 0x0, 0x2)
    OP_43(0x11, 0x0, 0x0, 0x2)
    OP_6D(-990, 0, 1560, 0)
    OP_67(0, 6700, -10000, 0)
    OP_6B(2580, 0)
    OP_6C(315000, 0)
    OP_6E(326, 0)

    def lambda_4B9():
        OP_6D(11060, 250, 11320, 4000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_4B9)

    def lambda_4D1():
        OP_67(0, 3930, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4D1)

    def lambda_4E9():
        OP_6B(2470, 4000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_4E9)

    def lambda_4F9():
        OP_6E(333, 4000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_4F9)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x0, 0x0)
    Sleep(500)

    ChrTalk(    #0
        0x12,
        (
            "#070F#5P共和国版的……情报部？\x02\x03",

            "这能做得到吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x14,
        (
            "#1110F#6P由总统进行主导，\x01",
            "预定不久即将成立。\x02\x03",

            "『洛克史密斯机关』――\x01",
            "部内给起了这样的外号。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x12,
        (
            "#070F#5P唔……\x01",
            "好刻板的名字啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x13,
        "#790F#2P那么，难道您说的要事就是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x14,
        (
            "#1110F#6P正如你所想的。\x02\x03",

            "希望雾香小姐\x01",
            "能到这次新设立的机关\x01",
            "为共和国工作。\x02\x03",

            "总统阁下为您\x01",
            "准备了机关中枢的职位。\x02\x03",

            "将国内外的情报收集与分析\x01",
            "集于一体的新设机关――\x02\x03",

            "要发挥您的才能，\x01",
            "我认为没有比这更适合的舞台了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x13, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    SetChrSubChip(0x12, 1)
    Sleep(200)

    ChrTalk(    #5
        0x12,
        "#070F#5P喂，雾香……\x02",
    )

    CloseMessageWindow()
    OP_63(0x13)
    Sleep(100)
    SetChrSubChip(0x13, 2)
    Sleep(200)

    ChrTalk(    #6
        0x13,
        (
            "#790F#4P没问题……\x01",
            "我听得很明白。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x14,
        (
            "#1110F呵呵，\x01",
            "看来就算是您也略有迷惑呢。\x02\x03",

            "没关系。\x01",
            "请慢慢考虑。\x02",
        )
    )

    Jump("loc_794")

    label("loc_794")

    CloseMessageWindow()
    SetChrSubChip(0x13, 0)
    Sleep(200)
    SetChrSubChip(0x12, 0)
    Sleep(300)
    Fade(300)
    SetChrChipByIndex(0x14, 4)
    SetChrSubChip(0x14, 0)
    SetChrPos(0x14, 12150, 0, 8230, 0)
    OP_6D(10700, 0, 11350, 1000)
    OP_0D()

    ChrTalk(    #8
        0x14,
        (
            "#1110F#6P我明天再听取您的答复。\x02\x03",

            "期待着最佳的决定。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x13,
        (
            "#790F#2P……谢谢您。\x02\x03",

            "那就这么办吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x14,
        "#1110F#6P好，明天见。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_43(0x14, 0x1, 0x0, 0x4)
    Sleep(1500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_20(0x7D0)
    Sleep(2000)
    OP_A2(0x2507)
    NewScene("ED6_DT21/T3201   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_3A8 end

    def Function_4_88C(): pass

    label("Function_4_88C")

    Sleep(300)
    OP_8E(0xFE, 0x283C, 0x0, 0x1CB6, 0x7D0, 0x0)
    OP_8E(0xFE, 0x1B3A, 0xFA, 0x29C2, 0x7D0, 0x0)
    OP_8E(0xFE, 0x15A4, 0xFA, 0x2A1C, 0x7D0, 0x0)
    Return()

    # Function_4_88C end

    def Function_5_8CE(): pass

    label("Function_5_8CE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x13, 0x4)
    SetChrFlags(0x12, 0x4)
    SetChrFlags(0x14, 0x4)
    SetChrPos(0x13, 13110, 200, 10890, 180)
    SetChrPos(0x12, 11150, 100, 10870, 125)
    SetChrPos(0x14, 13070, 200, 8320, 0)
    SetChrChipByIndex(0x14, 5)
    SetChrSubChip(0x14, 0)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x15, 0x4)
    SetChrFlags(0x16, 0x4)
    SetChrPos(0x15, 13250, 800, 9750, 0)
    SetChrPos(0x16, 13300, 800, 8900, 0)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    OP_43(0x10, 0x0, 0x0, 0x2)
    OP_43(0x11, 0x0, 0x0, 0x2)
    OP_6D(-990, 0, 1560, 0)
    OP_67(0, 6700, -10000, 0)
    OP_6B(2580, 0)
    OP_6C(315000, 0)
    OP_6E(326, 0)

    def lambda_9DF():
        OP_6D(11060, 250, 11320, 5000)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_9DF)

    def lambda_9F7():
        OP_67(0, 3930, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_9F7)

    def lambda_A0F():
        OP_6B(2470, 5000)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_A0F)

    def lambda_A1F():
        OP_6E(333, 5000)
        ExitThread()

    QueueWorkItem(0x18, 3, lambda_A1F)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x18, 0x0)
    Sleep(300)

    ChrTalk(    #11
        0x12,
        (
            "#074F#5P唔……\x02\x03",

            "#070F也就是说，\x01",
            "共和国要设立新的情报机关吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x14,
        (
            "#1110F#6P嗯嗯，\x01",
            "由总统进行主导，预定不久即将成立。\x02\x03",

            "『洛克史密斯机关』――\x02\x03",

            "顾名思义，\x01",
            "是洛克史密斯总统\x01",
            "直接控制的机关。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x12,
        "#073F#5P哦……总统的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x13,
        (
            "#792F#2P原来如此。\x02\x03",

            "#790F……也就是说，\x01",
            "组织运营并不受议会决定所左右吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x14,
        (
            "#1111F#6P呵呵，说得没错。\x01",
            "您理解的这么快，真是太好了。\x02\x03",

            "#1113F决定得不到及时实行，\x01",
            "组织得不到充分活用，\x01",
            "可说是根性不良的体制……\x02\x03",

            "部分特权者所控制的\x01",
            "恶性且不透明的组织运营……\x02\x03",

            "#1110F不受这样虚伪的议会\x01",
            "的权限干涉，\x01",
            "就是本组织最大的亮点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x12,
        (
            "#070F#5P嗯……\x01",
            "听起来真可靠啊。\x02\x03",

            "#074F过去的组织同帝国的情报局\x01",
            "或王国的旧情报部相比，\x01",
            "确实逊色了不少。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x14,
        (
            "#1113F#6P嗯嗯……确实。\x02\x03",

            "#1112F在共和国无论做什么，\x01",
            "缺乏统一性都是瓶颈所在。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x12,
        (
            "#074F#5P不过，\x01",
            "这也可以说是\x01",
            "接受移民的国家的特性吧。\x02\x03",

            "#070F但是，\x01",
            "最让我吃惊的是\x01",
            "总统这种积极的行动。\x02\x03",

            "根据以前的施政方式来看，\x01",
            "我还以为他\x01",
            "一定是保守派……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x13,
        (
            "#792F#2P不过，\x01",
            "考虑到现在共和国的形势，\x01",
            "或许也能令人认同。\x02\x03",

            "帝国的主战派今日依然不断抬头，\x01",
            "而且国内还潜伏着\x01",
            "与激进派相关的恐怖分子集团……\x02\x03",

            "#790F面对这些势力，\x01",
            "已经不是咬着手指\x01",
            "发呆的时候了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x14,
        (
            "#1113F#6P嗯嗯，是啊。\x02\x03",

            "无论如何，\x01",
            "今后的时代经常会需要\x01",
            "柔软灵活的对策是毫无疑问的。\x02\x03",

            "#1110F……不过，\x01",
            "到目前我们说了太多的闲话了。\x02\x03",

            "差不多该\x01",
            "进入正题了吧。\x02",
        )
    )

    Jump("loc_F2A")

    label("loc_F2A")

    CloseMessageWindow()

    ChrTalk(    #21
        0x12,
        (
            "#070F#5P啊啊，\x01",
            "是有话要跟雾香说是吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x13,
        "#790F#2P难不成，您说的要事就是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x14,
        (
            "#1110F#6P正如您所想的。\x02\x03",

            "#1113F直属总统的\x01",
            "将国内外的情报收集与分析\x01",
            "集于一体的情报机关――\x02\x03",

            "#1112F雾香小姐，\x01",
            "希望您务必能成为其中一员\x01",
            "为共和国工作。\x02\x03",

            "为此，\x01",
            "已经为您准备了\x01",
            "机关中枢的职位。\x02\x03",

            "……这也是\x01",
            "总统阁下本人的意向。\x02",
        )
    )

    Jump("loc_1068")

    label("loc_1068")

    CloseMessageWindow()

    ChrTalk(    #24
        0x13,
        "#792F#2P……原来如此。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x12,
        (
            "#075F#5P呼，果然是吗……\x02\x03",

            "#070F但是，\x01",
            "为何要大使亲自来说？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x14,
        (
            "#1111F#6P呵呵，\x01",
            "本来这是派往各地的\x01",
            "猎头者的工作……\x02\x03",

            "#1113F不过别看我这样，\x01",
            "也算是总统的昔日好友。\x02\x03",

            "#1110F雾香小姐的事\x01",
            "是他以个人名义拜托我的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x12,
        "#073F#5P哦，大使还有如此渊源……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x13,
        "#790F#2P……但是，总统为何要邀请我？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x14,
        (
            "#1110F#6P哎呀，\x01",
            "这还用我特意说明吗？\x02\x03",

            "您身为共和国引以为傲的古流武术——\x01",
            "『泰斗流』的奥义传人，\x01",
            "这种名望自不用说……\x02\x03",

            "在协会立下的\x01",
            "种种事务实绩\x01",
            "也是大家有目共睹的吧？\x02\x03",

            "#1111F您既然已经展示了\x01",
            "如此非凡的才能，\x01",
            "还需要什么其它的理由呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x13,
        "#792F#2P………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x12,
        (
            "#075F#5P唉～话虽如此，\x01",
            "居然在游击士的面前\x01",
            "把协会的珍贵人员给……\x02\x03",

            "#070F明知如此\x01",
            "却还让我同席，\x01",
            "还真是老练的作风啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x13,
        (
            "#792F#2P……不过，\x01",
            "从这点上说似乎选错了人呢。\x02\x03",

            "#790F因为你在不在场\x01",
            "跟我是否接受这件事\x01",
            "完全没有关系。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x12,
        (
            "#073F#5P呜……\x01",
            "你还真是不可爱。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x14,
        (
            "#1113F#6P……………………\x02\x03",

            "#1110F那么，怎么样呢……\x01",
            "雾香小姐。\x02\x03",

            "我能听听您\x01",
            "真实的想法吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x13,
        (
            "#792F#2P是啊……\x01",
            "我觉得这事情很难得。\x02\x03",

            "#790F但是……\x01",
            "我还是没有接受的理由。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x14,
        (
            "#1113F#6P不过――也没有拒绝的理由。\x02\x03",

            "#1112F不是吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x13,
        "#793F#2P这、这个嘛……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x12,
        "#074F#5P………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x14,
        (
            "#1110F#6P呵呵，\x01",
            "看来就算是您也略有迷惑呢。\x02\x03",

            "#1111F那么，\x01",
            "能不能好好考虑一个晚上呢。\x02\x03",

            "正是为此，\x01",
            "我才订了这家旅馆的。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x12, 0)
    Sleep(200)
    Fade(500)
    SetChrChipByIndex(0x14, 4)
    SetChrSubChip(0x14, 0)
    SetChrPos(0x14, 12150, 0, 8230, 0)
    OP_6D(10700, 0, 11350, 1000)
    OP_0D()
    Sleep(300)

    ChrTalk(    #40
        0x14,
        (
            "#1110F#6P我明天再听取您的答复吧。\x02\x03",

            "期待能够听到最佳的决定。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x13,
        "#790F#2P……嗯嗯。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x14, 270, 400)
    OP_8C(0x14, 180, 400)
    Sleep(200)
    OP_8E(0x14, 0x3016, 0x0, 0x1CB6, 0x7D0, 0x0)
    TurnDirection(0x14, 0x13, 400)
    Sleep(200)

    ChrTalk(    #42
        0x14,
        (
            "#1113F#6P对了对了，\x01",
            "最后我再说一句话。\x02\x03",

            "#1112F……您的才能\x01",
            "绝不是当协会接待\x01",
            "就能完全发挥的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x13,
        "#792F#2P………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x14,
        "#1111F#6P那么，明天见。\x02",
    )

    CloseMessageWindow()
    OP_43(0x14, 0x1, 0x0, 0x4)
    Sleep(1500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_20(0x7D0)
    Sleep(2000)
    OP_A2(0x2507)
    NewScene("ED6_DT21/T3201   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_8CE end

    SaveToFile()

Try(main)
