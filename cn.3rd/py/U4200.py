from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'U4200   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U4200.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60221",
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
        '甲胄兵',                               # 9
        '',                                     # 10
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
        'ED6_DT29/CH14510 ._CH',             # 00
    )

    AddCharChipPat(
        'ED6_DT29/CH14510P._CP',             # 00
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 35780,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -5190,
        Y                   = -1000,
        Z                   = 32000,
        Range               = 4870,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x8732,
        Unknown_18          = 0x0,
        Unknown_1C          = 3,
    )


    DeclActor(
        TriggerX            = 7050,
        TriggerZ            = 0,
        TriggerY            = 11870,
        TriggerRange        = 1000,
        ActorX              = 8000,
        ActorZ              = 3000,
        ActorY              = 12000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_116",          # 00, 0
        "Function_1_18F",          # 01, 1
        "Function_2_1D9",          # 02, 2
        "Function_3_356",          # 03, 3
        "Function_4_588",          # 04, 4
        "Function_5_A6C",          # 05, 5
        "Function_6_AE0",          # 06, 6
        "Function_7_CA7",          # 07, 7
        "Function_8_D5D",          # 08, 8
        "Function_9_E08",          # 09, 9
    )


    def Function_0_116(): pass

    label("Function_0_116")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_126")
    ClearChrFlags(0x10, 0x80)
    Jump("loc_131")

    label("loc_126")

    OP_51(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_131")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_165")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (103, "loc_149"),
        (SWITCH_DEFAULT, "loc_165"),
    )


    label("loc_149")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 7)), scpexpr(EXPR_END)), "loc_162")
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 9)

    label("loc_162")

    Jump("loc_165")

    label("loc_165")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_17B")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    Event(0, 8)
    Jump("loc_18E")

    label("loc_17B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_18E")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 4)

    label("loc_18E")

    Return()

    # Function_0_116 end

    def Function_1_18F(): pass

    label("Function_1_18F")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFE4A80, 0x230060)
    OP_22(0x1CC, 0x1, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E4, 1)), scpexpr(EXPR_END)), "loc_1B9")
    OP_B1("U4200_y")
    Jump("loc_1C2")

    label("loc_1B9")

    OP_B1("U4200_n")

    label("loc_1C2")

    OP_82(0x80, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xD, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_1D5")
    OP_82(0x81, 0x0)
    Jump("loc_1D8")

    label("loc_1D5")

    OP_82(0x82, 0x0)

    label("loc_1D8")

    Return()

    # Function_1_18F end

    def Function_2_1D9(): pass

    label("Function_2_1D9")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FE")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_340")

    label("loc_1FE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_217")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_340")

    label("loc_217")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_230")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_340")

    label("loc_230")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_249")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_340")

    label("loc_249")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_262")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_340")

    label("loc_262")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27B")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_340")

    label("loc_27B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_294")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_340")

    label("loc_294")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AD")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_340")

    label("loc_2AD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C6")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_340")

    label("loc_2C6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DF")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_340")

    label("loc_2DF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F8")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_340")

    label("loc_2F8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_311")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_340")

    label("loc_311")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32A")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_340")

    label("loc_32A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_340")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_340")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_355")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_340")

    label("loc_355")

    Return()

    # Function_2_1D9 end

    def Function_3_356(): pass

    label("Function_3_356")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E0, 4)), scpexpr(EXPR_END)), "loc_35E")
    Return()

    label("loc_35E")

    EventBegin(0x1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #0
        (
            "\x07\x05人高马大的甲胄兵\x01",
            "阻挡在城门前。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #1
        "\x07\x05要挑战吗？\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3CC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_587")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "  挑战\x01",        # 0
            "离开这里\x01",      # 1
        )
    )

    Jump("loc_404")

    label("loc_404")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_429"),
        (SWITCH_DEFAULT, "loc_4F8"),
    )


    label("loc_429")

    Battle(0xF0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_454"),
        (2, "loc_463"),
        (1, "loc_4E6"),
        (SWITCH_DEFAULT, "loc_4EB"),
    )


    label("loc_454")

    OP_A2(0x2504)
    NewScene("ED6_DT21/U4100   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_4EB")

    label("loc_463")

    EventBegin(0x1)
    SetChrPos(0x0, 0, 0, 30130, 180)
    SetChrPos(0x1, 0, 0, 30130, 180)
    SetChrPos(0x2, 0, 0, 30130, 180)
    SetChrPos(0x3, 0, 0, 30130, 180)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    OP_69(0x0, 0x0)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Jump("loc_4EB")

    label("loc_4E6")

    OP_B4(0x0)
    Jump("loc_4EB")

    label("loc_4EB")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_584")

    label("loc_4F8")

    Sleep(300)
    Fade(500)
    SetChrPos(0x0, 0, 0, 30130, 180)
    SetChrPos(0x1, 0, 0, 30130, 180)
    SetChrPos(0x2, 0, 0, 30130, 180)
    SetChrPos(0x3, 0, 0, 30130, 180)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    OP_69(0x0, 0x0)
    EventEnd(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_584")

    label("loc_584")

    Jump("loc_3CC")

    label("loc_587")

    Return()

    # Function_3_356 end

    def Function_4_588(): pass

    label("Function_4_588")

    EventBegin(0x0)
    SetChrPos(0x10E, 0, 0, 28790, 0)
    SetChrPos(0x109, -950, 0, 27120, 0)
    SetChrPos(0x10F, 830, 0, 26490, 0)
    SetChrPos(0x107, -160, 0, 24800, 0)
    SetChrFlags(0x10, 0x80)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    OP_6D(0, 5750, 42120, 0)
    OP_67(0, 4100, -10000, 0)
    OP_6B(3150, 0)
    OP_6C(0, 0)
    OP_6E(300, 0)
    FadeToBright(2000, 0)
    OP_0D()

    def lambda_648():
        OP_6D(0, 4600, 36000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_648)

    def lambda_660():
        OP_67(0, 3200, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_660)

    def lambda_678():
        OP_6B(3300, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_678)

    def lambda_688():
        OP_6E(343, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_688)

    def lambda_698():
        OP_8E(0xFE, 0xFFFFFFD8, 0x0, 0x9B3C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 0, lambda_698)
    Sleep(100)

    def lambda_6B8():
        OP_8E(0xFE, 0xFFFFFC40, 0x0, 0x93EE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6B8)
    Sleep(100)

    def lambda_6D8():
        OP_8E(0xFE, 0x3B6, 0x0, 0x918C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_6D8)
    Sleep(100)

    def lambda_6F8():
        OP_8E(0xFE, 0xFFFFFFC4, 0x0, 0x8C00, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_6F8)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0x107, 0x0)
    WaitChrThread(0x10E, 0x0)
    WaitChrThread(0x109, 0x1)
    Fade(500)
    OP_6D(2350, 600, 43360, 0)
    OP_67(0, 3900, -10000, 0)
    OP_6B(3370, 0)
    OP_6C(45000, 0)
    OP_6E(327, 0)
    SetChrPos(0x10E, -30, 0, 40240, 0)
    SetChrPos(0x109, -1110, 0, 38370, 0)
    SetChrPos(0x10F, 780, 0, 38590, 0)
    SetChrPos(0x107, -380, 0, 37000, 0)
    OP_0D()
    WaitChrThread(0x10E, 0x0)
    Sleep(500)

    ChrTalk(    #2
        0x10E,
        "#178F#5P……这是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x107,
        "#065F#4P魔、魔法纹章……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x10F,
        (
            "#1443F……看来被某种精神力量\x01",
            "给封印住了。\x02\x03",

            "单靠蛮力的话\x01",
            "是很难突破的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x10E,
        (
            "#176F#5P啊……\x01",
            "看起来正是这样。\x02\x03",

            "#175F果然还是得做些什么\x01",
            "才能把这个封印解除掉吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x109,
        (
            "#1065F#6P很有可能。\x02\x03",

            "#1063F……怎么办？\x01",
            "到别的地方去看看吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10E, 180, 400)
    Sleep(300)

    ChrTalk(    #7
        0x10E,
        (
            "#178F#5P好吧……\x01",
            "现在也只有向女神祈求\x01",
            "陛下他们平安无事了。\x02\x03",

            "暂且回到街上搜索吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x109,
        (
            "#1060F#6P明白了。\x02\x03",

            "总之先把能去的地方\x01",
            "都转个遍吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(30, 0, 38110, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x10E, 30, 0, 38110, 180)
    SetChrPos(0x109, 30, 0, 38110, 180)
    SetChrPos(0x10F, 30, 0, 38110, 180)
    SetChrPos(0x107, 30, 0, 38110, 180)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_A2(0x2704)
    OP_28(0x2B, 0x1, 0x20)
    EventEnd(0x0)
    Return()

    # Function_4_588 end

    def Function_5_A6C(): pass

    label("Function_5_A6C")

    SetMessageWindowPos(-1, 110, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x05打开『门』吗？\x18\x02",
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    Jump("loc_AC9")

    label("loc_AC9")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Sleep(300)
    Return()

    # Function_5_A6C end

    def Function_6_AE0(): pass

    label("Function_6_AE0")

    EventBegin(0x0)
    OP_22(0x222, 0x0, 0x64)
    Fade(500)
    SetChrPos(0x0, 5590, 0, 12650, 90)
    SetChrPos(0x1, 5450, 0, 10750, 90)
    SetChrPos(0x2, 3540, 0, 12510, 90)
    SetChrPos(0x3, 3520, 0, 10430, 90)
    OP_6D(5630, 0, 11740, 0)
    OP_67(0, 6820, -10000, 0)
    OP_6B(3520, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xD, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BB6")
    OP_28(0xD, 0x4, 0x2)
    OP_82(0x81, 0x2)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_BB6")

    Sleep(1000)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #10
        (
            "\x07\x05#40W　　 汝须将王宫守护之刀，\x01",
            "　  与侍奉皇室之钢剑一同\x01",
            "　　  引领至吾面前。\x01",
            "#500W\x01",
            "#40W   如此，则『门』将开启……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C9B")
    Call(0, 5)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C98")
    Call(0, 7)

    label("loc_C98")

    Jump("loc_C9B")

    label("loc_C9B")

    FadeToBright(300, 0)
    EventEnd(0x0)
    Return()

    # Function_6_AE0 end

    def Function_7_CA7(): pass

    label("Function_7_CA7")

    FadeToBright(300, 0)
    Sleep(500)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x78)
    Sleep(300)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x3)
    Sleep(500)

    def lambda_D10():
        OP_6B(2830, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_D10)
    OP_22(0x138, 0x0, 0x64)
    FadeToDark(2000, 16777215, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    FadeToBright(2000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    OP_E3(0x0, 0x0, 0, 0x0)
    NewScene("ED6_DT21/P9001   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_CA7 end

    def Function_8_D5D(): pass

    label("Function_8_D5D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    Sleep(500)
    SetChrPos(0x0, 5590, 0, 12650, 90)
    SetChrPos(0x1, 5450, 0, 10750, 90)
    SetChrPos(0x2, 3540, 0, 12510, 90)
    SetChrPos(0x3, 3520, 0, 10430, 90)
    OP_6D(5630, 0, 11740, 0)
    OP_67(0, 6820, -10000, 0)
    OP_6B(3520, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    EventEnd(0x0)
    Return()

    # Function_8_D5D end

    def Function_9_E08(): pass

    label("Function_9_E08")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("ED6_DT21/U4203   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_9_E08 end

    SaveToFile()

Try(main)
