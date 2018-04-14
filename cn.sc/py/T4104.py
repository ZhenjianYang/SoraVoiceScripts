from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4104   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4104.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60081",
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
        '寒冰至尊',                             # 9
        '寒冰碎片',                             # 10
        '寒冰碎片',                             # 11
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
        'ED6_DT09/CH10840 ._CH',             # 00
        'ED6_DT09/CH10841 ._CH',             # 01
        'ED6_DT29/CH12460 ._CH',             # 02
        'ED6_DT29/CH12461 ._CH',             # 03
        'ED6_DT27/CH04000 ._CH',             # 04
        'ED6_DT07/CH00130 ._CH',             # 05
        'ED6_DT07/CH00140 ._CH',             # 06
        'ED6_DT07/CH00170 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT09/CH10840P._CP',             # 00
        'ED6_DT09/CH10841P._CP',             # 01
        'ED6_DT29/CH12460P._CP',             # 02
        'ED6_DT29/CH12461P._CP',             # 03
        'ED6_DT27/CH04000P._CP',             # 04
        'ED6_DT07/CH00130P._CP',             # 05
        'ED6_DT07/CH00140P._CP',             # 06
        'ED6_DT07/CH00170P._CP',             # 07
    )

    DeclNpc(
        X                   = 960,
        Z                   = 0,
        Y                   = 10300,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1960,
        Z                   = 0,
        Y                   = 8260,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -600,
        Z                   = 0,
        Y                   = 8260,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_14A",          # 00, 0
        "Function_1_14F",          # 01, 1
        "Function_2_17A",          # 02, 2
        "Function_3_2F7",          # 03, 3
        "Function_4_AD0",          # 04, 4
        "Function_5_B09",          # 05, 5
        "Function_6_B42",          # 06, 6
        "Function_7_B6F",          # 07, 7
        "Function_8_BA8",          # 08, 8
        "Function_9_C19",          # 09, 9
    )


    def Function_0_14A(): pass

    label("Function_0_14A")

    Event(0, 3)
    Return()

    # Function_0_14A end

    def Function_1_14F(): pass

    label("Function_1_14F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16B")
    OP_B1("t4104_y")
    Jump("loc_174")

    label("loc_16B")

    OP_B1("t4104_n")

    label("loc_174")

    OP_71(0x7, 0x4)
    Return()

    # Function_1_14F end

    def Function_2_17A(): pass

    label("Function_2_17A")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19F")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_2E1")

    label("loc_19F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B8")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_2E1")

    label("loc_1B8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D1")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_2E1")

    label("loc_1D1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EA")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_2E1")

    label("loc_1EA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_203")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_2E1")

    label("loc_203")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21C")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_2E1")

    label("loc_21C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_235")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_2E1")

    label("loc_235")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24E")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_2E1")

    label("loc_24E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_267")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_2E1")

    label("loc_267")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_280")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_2E1")

    label("loc_280")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_299")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_2E1")

    label("loc_299")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B2")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_2E1")

    label("loc_2B2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CB")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_2E1")

    label("loc_2CB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E1")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_2E1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2F6")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_2E1")

    label("loc_2F6")

    Return()

    # Function_2_17A end

    def Function_3_2F7(): pass

    label("Function_3_2F7")

    EventBegin(0x0)
    OP_6D(1520, 0, 1520, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(4400, 0)
    OP_6C(134000, 0)
    OP_6E(262, 0)
    OP_6F(0x0, 0)
    OP_72(0x0, 0x10)
    OP_6F(0x1, 0)
    OP_72(0x1, 0x10)
    SetChrPos(0x101, 440, 0, -25960, 0)
    SetChrPos(0x105, 2060, 0, -26560, 0)
    SetChrPos(0x104, -520, 0, -27220, 0)
    SetChrPos(0x108, 1280, 0, -27820, 0)

    def lambda_398():
        OP_6D(1520, 0, -18920, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_398)
    Sleep(500)
    OP_70(0x0, 0x64)
    OP_43(0x101, 0x1, 0x0, 0x4)
    Sleep(100)
    OP_43(0x105, 0x1, 0x0, 0x5)
    Sleep(100)
    OP_43(0x104, 0x1, 0x0, 0x6)
    Sleep(100)
    OP_43(0x108, 0x1, 0x0, 0x7)
    WaitChrThread(0x101, 0x2)
    Sleep(1000)
    Fade(500)
    OP_6D(1280, 0, -12260, 0)
    OP_67(0, 6900, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    WaitChrThread(0x108, 0x1)

    ChrTalk(    #0
        0x101,
        (
            "#1000F格兰竞技场……\x01",
            "感觉好怀念。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x108,
        (
            "#070F啊，明明没过多久，\x01",
            "真不可思议。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x104,
        (
            "#035F呼，只要站在这里，\x01",
            "就好像还能听见那时的欢呼声。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4C3():
        OP_8C(0x101, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4C3)
    Sleep(50)

    def lambda_4D6():
        OP_8C(0x105, 270, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4D6)
    Sleep(50)

    def lambda_4E9():
        OP_8C(0x104, 45, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4E9)
    Sleep(50)

    def lambda_4FC():
        OP_8C(0x108, 0, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_4FC)
    WaitChrThread(0x108, 0x1)

    ChrTalk(    #3
        0x105,
        (
            "#040F我记得艾丝蒂尔你们\x01",
            "在获得武术大会冠军后\x01",
            "被邀请进入城堡了吧？\x02\x03",

            "#041F呵呵，我也很想观战啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        (
            "#1016F哈哈，现在想想\x01",
            "我那时还很不成熟。\x02\x03",

            "#1006F不过等这回的骚乱平息之后，\x01",
            "我想再次参加明年的武术大会。\x02\x03",

            "这也是为了测试自己的实力。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x108,
        (
            "#071F哈哈，这才是大人的女儿。\x02\x03",

            "#070F是啊……\x01",
            "到时候让我也参战吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        (
            "#1016F金、金先生做我对手的话\x01",
            "我实在没取胜的信心……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x104,
        (
            "#031F呵呵，那我就在观众席\x01",
            "唱歌来\x01",
            "支持艾丝蒂尔吧。\x02\x03",

            "#030F用我充满爱意和力量的歌声…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        (
            "#1019F……你的好意\x01",
            "我就心领了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x105,
        "#041F呵呵……\x02",
    )

    CloseMessageWindow()
    OP_70(0x1, 0x64)
    Sleep(200)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x108, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(200)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0x8, 1)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x9, 3)
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0xA, 3)
    SetChrSubChip(0xA, 0)

    def lambda_7B4():
        OP_8F(0xFE, 0x3C0, 0x0, 0xFFFFFB78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_7B4)

    def lambda_7CF():
        OP_8F(0xFE, 0x7A8, 0x0, 0xFFFFF3D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_7CF)

    def lambda_7EA():
        OP_8F(0xFE, 0xFFFFFDA8, 0x0, 0xFFFFF3D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_7EA)

    def lambda_805():
        OP_6D(1880, 0, 5500, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_805)

    def lambda_81D():
        OP_67(0, 5420, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_81D)

    def lambda_835():
        OP_6B(3200, 2000)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_835)

    def lambda_845():
        OP_6C(45000, 2000)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_845)

    def lambda_855():
        OP_8C(0x101, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_855)
    Sleep(50)

    def lambda_868():
        OP_8C(0x105, 0, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_868)
    Sleep(50)

    def lambda_87B():
        OP_8C(0x104, 0, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_87B)
    WaitChrThread(0x101, 0x2)
    SetChrChipByIndex(0x101, 4)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x104, 5)
    SetChrSubChip(0x104, 0)
    SetChrChipByIndex(0x105, 6)
    SetChrSubChip(0x105, 0)
    SetChrChipByIndex(0x108, 7)
    SetChrSubChip(0x108, 0)
    SetChrPos(0x101, 320, 0, -8590, 0)
    SetChrPos(0x105, 1670, 0, -9190, 0)
    SetChrPos(0x104, -430, 0, -10240, 0)
    SetChrPos(0x108, 920, 0, -10990, 0)

    def lambda_8FA():
        OP_6D(1620, 0, -5360, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8FA)

    def lambda_912():
        OP_6B(3400, 4000)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_912)
    WaitChrThread(0x101, 0x2)
    Fade(250)
    SetChrChipByIndex(0x8, 0)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x9, 2)
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0xA, 2)
    SetChrSubChip(0xA, 0)
    OP_0D()

    ChrTalk(    #10
        0x101,
        "#1004F魔、魔兽！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x108,
        (
            "#072F好像是要模仿古代\x01",
            "竞技场呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x104,
        (
            "#035F呵呵，这舞台令人满意。\x02\x03",

            "#030F不过没有观战的客人，\x01",
            "真是有点遗憾啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x105,
        "#046F……敌人来了！\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x8, 1)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x9, 3)
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0xA, 3)
    SetChrSubChip(0xA, 0)
    OP_43(0x8, 0x0, 0x0, 0x8)

    def lambda_A16():
        OP_8F(0xFE, 0x3C0, 0x0, 0xFFFFD468, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_A16)

    def lambda_A31():
        OP_8F(0xFE, 0x7A8, 0x0, 0xFFFFCCC0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_A31)

    def lambda_A4C():
        OP_8F(0xFE, 0xFFFFFDA8, 0x0, 0xFFFFCCC0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_A4C)

    def lambda_A67():
        OP_6B(2600, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_A67)
    Sleep(400)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0x104, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AA6")
    Battle(0xCEA, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_AB3")

    label("loc_AA6")

    Battle(0xCE9, 0x0, 0x0, 0x0, 0xFF)

    label("loc_AB3")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_AC3"),
        (0, "loc_AC8"),
        (SWITCH_DEFAULT, "loc_ACF"),
    )


    label("loc_AC3")

    OP_B4(0x0)
    Jump("loc_ACF")

    label("loc_AC8")

    Call(0, 9)
    Jump("loc_ACF")

    label("loc_ACF")

    Return()

    # Function_3_2F7 end

    def Function_4_AD0(): pass

    label("Function_4_AD0")

    OP_8E(0x101, 0x1B8, 0x0, 0xFFFFD530, 0x7D0, 0x0)
    Sleep(200)
    OP_8C(0xFE, 270, 400)
    Sleep(500)
    OP_8C(0xFE, 360, 400)
    Sleep(500)
    OP_8C(0xFE, 315, 400)
    Return()

    # Function_4_AD0 end

    def Function_5_B09(): pass

    label("Function_5_B09")

    OP_8E(0x105, 0x80C, 0x0, 0xFFFFD2D8, 0x7D0, 0x0)
    Sleep(200)
    OP_8C(0xFE, 45, 400)
    Sleep(500)
    OP_8C(0xFE, 135, 400)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_5_B09 end

    def Function_6_B42(): pass

    label("Function_6_B42")

    OP_8E(0x104, 0xFFFFFDF8, 0x0, 0xFFFFD044, 0x7D0, 0x0)
    Sleep(200)
    OP_8C(0xFE, 225, 400)
    Sleep(500)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_6_B42 end

    def Function_7_B6F(): pass

    label("Function_7_B6F")

    OP_8E(0x108, 0x500, 0x0, 0xFFFFCDEC, 0x7D0, 0x0)
    Sleep(200)
    OP_8C(0xFE, 45, 400)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    Sleep(500)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_7_B6F end

    def Function_8_BA8(): pass

    label("Function_8_BA8")

    OP_8C(0xFE, 90, 1000)
    OP_8C(0xFE, 0, 1000)
    OP_8C(0xFE, 270, 1000)
    OP_8C(0xFE, 180, 1000)
    OP_8C(0xFE, 90, 1000)
    OP_8C(0xFE, 0, 1000)
    OP_8C(0xFE, 270, 1000)
    OP_8C(0xFE, 180, 1000)
    OP_8C(0xFE, 90, 1000)
    OP_8C(0xFE, 0, 1000)
    OP_8C(0xFE, 270, 1000)
    OP_8C(0xFE, 180, 1000)
    OP_8C(0xFE, 90, 1000)
    OP_8C(0xFE, 0, 1000)
    OP_8C(0xFE, 270, 1000)
    OP_8C(0xFE, 180, 1000)
    Return()

    # Function_8_BA8 end

    def Function_9_C19(): pass

    label("Function_9_C19")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "craft\\\\cr162_02.eff")
    OP_6D(1620, 0, -5360, 0)
    OP_67(0, 5420, -10000, 0)
    OP_6B(3400, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrChipByIndex(0x101, 4)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x104, 5)
    SetChrSubChip(0x104, 0)
    SetChrChipByIndex(0x105, 6)
    SetChrSubChip(0x105, 0)
    SetChrChipByIndex(0x108, 7)
    SetChrSubChip(0x108, 0)
    SetChrPos(0x101, 320, 0, -8590, 0)
    SetChrPos(0x105, 1670, 0, -9190, 0)
    SetChrPos(0x104, -430, 0, -10240, 0)
    SetChrPos(0x108, 920, 0, -10990, 0)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    PlayEffect(0x0, 0x1, 0xFF, 720, 0, -3320, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_72(0x7, 0x4)

    ChrTalk(    #14
        0x101,
        "#1004F哇哇……\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x105, 65535)
    SetChrChipByIndex(0x104, 65535)
    SetChrChipByIndex(0x108, 65535)
    OP_0D()

    ChrTalk(    #15
        0x101,
        "#1019F什、什么啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x105,
        "#044F看上去像是魔术……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x104,
        (
            "#030F呵呵，水平\x01",
            "不是还不错吗？\x02\x03",

            "#035F确实有实力当我的\x01",
            "候补对手。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x108,
        (
            "#075F唉，比我想象的\x01",
            "要有性格……\x02\x03",

            "#070F好了，赶快看一下\x01",
            "里面的内容吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x101,
        "#1000F嗯，是啊。\x02",
    )

    CloseMessageWindow()

    def lambda_E54():
        OP_6B(2700, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E54)

    def lambda_E64():
        OP_8E(0xFE, 0x208, 0x0, 0xFFFFEF0C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E64)
    Sleep(400)

    def lambda_E84():
        OP_90(0xFE, 0xFFFFFF38, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_E84)
    Sleep(50)

    def lambda_EA4():
        OP_90(0xFE, 0xFFFFFF38, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_EA4)
    Sleep(50)

    def lambda_EC4():
        OP_90(0xFE, 0xFFFFFF38, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_EC4)
    WaitChrThread(0x101, 0x1)
    Sleep(400)
    OP_70(0x7, 0x3C)
    OP_22(0x2B, 0x0, 0x64)
    OP_73(0x7)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #20
        "\x07\x00得到了\x07\x02#16I埃尔赛尤的照片\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #21
        (
            "\x07\x05箱子底部\x01",
            "贴着一张卡片。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    OP_AD(0x240093, 0xBE, 0x64, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(-1, 300, -1, 3)
    SetChrName("")

    AnonymousTalk(    #22
        (
            "\x07\x05　　　　我的公主和劲敌，\x01",
            "　　还有勇敢的诸位游击士啊。　　\x02\x03",

            "　　对我精心装备的招待\x01",
            "　　　 你们可满意否？ 　　　\x02\x03",

            "　　我不想伤害主角的心情，\x01",
            "所以就让我这个配角退席吧。\x02\x03",

            "敬请期待来日的重逢。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_AE(0x1F4)
    Sleep(1000)
    OP_8C(0x101, 180, 400)

    ChrTalk(    #23
        0x101,
        (
            "#1009F真是的，什么来日的重逢啊。\x02\x03",

            "真希望他能够适可而止。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x105,
        (
            "#042F不过他写的东西\x01",
            "挺令人在意的。\x02\x03",

            "主角和配角什么的\x01",
            "究竟是指？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        (
            "#1015F被你这么一说……\x02\x03",

            "#1000F好了，总之先把这张照片\x01",
            "送回资料馆。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T4135   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_9_C19 end

    SaveToFile()

Try(main)
