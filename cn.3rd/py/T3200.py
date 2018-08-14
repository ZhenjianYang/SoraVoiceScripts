from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3200   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3200.x',
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '金',                                   # 9
        '雾香',                                 # 10
        '爱尔莎大使',                           # 11
        '拉克',                                 # 12
        '库安',                                 # 13
        '法露茨',                               # 14
        '观光客',                               # 15
        '目标用摄像机',                         # 16
        '',                                     # 17
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
        'ED6_DT07/CH00070 ._CH',             # 00
        'ED6_DT07/CH02610 ._CH',             # 01
        'ED6_DT27/CH03720 ._CH',             # 02
        'ED6_DT07/CH00071 ._CH',             # 03
        'ED6_DT07/CH01160 ._CH',             # 04
        'ED6_DT07/CH01060 ._CH',             # 05
        'ED6_DT07/CH01140 ._CH',             # 06
        'ED6_DT07/CH01020 ._CH',             # 07
        'ED6_DT07/CH01020 ._CH',             # 08
        'ED6_DT26/CH20816 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT07/CH00070P._CP',             # 00
        'ED6_DT07/CH02610P._CP',             # 01
        'ED6_DT27/CH03720P._CP',             # 02
        'ED6_DT07/CH00071P._CP',             # 03
        'ED6_DT07/CH01160P._CP',             # 04
        'ED6_DT07/CH01060P._CP',             # 05
        'ED6_DT07/CH01140P._CP',             # 06
        'ED6_DT07/CH01020P._CP',             # 07
        'ED6_DT07/CH01020P._CP',             # 08
        'ED6_DT26/CH20816P._CP',             # 09
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 13780,
        Z                   = 2500,
        Y                   = 18450,
        Direction           = 90,
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
        X                   = 12020,
        Z                   = 2000,
        Y                   = 14160,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 21790,
        Z                   = 2000,
        Y                   = 5570,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_1FA",          # 00, 0
        "Function_1_233",          # 01, 1
        "Function_2_269",          # 02, 2
        "Function_3_3E6",          # 03, 3
        "Function_4_84E",          # 04, 4
        "Function_5_863",          # 05, 5
        "Function_6_8C3",          # 06, 6
        "Function_7_928",          # 07, 7
        "Function_8_999",          # 08, 8
        "Function_9_12E3",         # 09, 9
        "Function_10_1348",        # 0A, 10
        "Function_11_13A6",        # 0B, 11
        "Function_12_1404",        # 0C, 12
        "Function_13_1DD9",        # 0D, 13
    )


    def Function_0_1FA(): pass

    label("Function_0_1FA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_232")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_222")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    Event(0, 12)
    Jump("loc_232")

    label("loc_222")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A1, 0)), scpexpr(EXPR_END)), "loc_232")
    SetMapFlags(0x10000000)
    Event(0, 13)

    label("loc_232")

    Return()

    # Function_0_1FA end

    def Function_1_233(): pass

    label("Function_1_233")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_268")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_255")
    OP_A3(0x2505)
    OP_B1("T3200_y")
    Jump("loc_268")

    label("loc_255")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A1, 0)), scpexpr(EXPR_END)), "loc_268")
    OP_A3(0x2508)
    OP_B1("T3200_n")

    label("loc_268")

    Return()

    # Function_1_233 end

    def Function_2_269(): pass

    label("Function_2_269")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28E")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_3D0")

    label("loc_28E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A7")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_3D0")

    label("loc_2A7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C0")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_3D0")

    label("loc_2C0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D9")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_3D0")

    label("loc_2D9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F2")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_3D0")

    label("loc_2F2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30B")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_3D0")

    label("loc_30B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_324")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_3D0")

    label("loc_324")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33D")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_3D0")

    label("loc_33D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_356")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_3D0")

    label("loc_356")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36F")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_3D0")

    label("loc_36F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_388")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_3D0")

    label("loc_388")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A1")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_3D0")

    label("loc_3A1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BA")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_3D0")

    label("loc_3BA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D0")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_3D0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3E5")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_3D0")

    label("loc_3E5")

    Return()

    # Function_2_269 end

    def Function_3_3E6(): pass

    label("Function_3_3E6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Sleep(500)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 13770, 2500, 18460, 90)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x13, 18420, 2000, 11830, 270)
    SetChrPos(0x14, 20510, 2000, 11850, 270)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05之后过了两天――\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(1000)
    OP_6D(-12560, -2000, 15790, 0)
    OP_67(0, 8690, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(45000, 0)
    OP_6E(312, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x11, -3160, 0, 14840, 90)
    SetChrPos(0x10, -2220, 0, 15780, 90)

    def lambda_4EF():
        OP_8E(0xFE, 0x2698, 0x7D0, 0x3B56, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_4EF)
    Sleep(100)

    def lambda_50F():
        OP_8E(0xFE, 0x2332, 0x7D0, 0x3746, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_50F)

    def lambda_52A():
        OP_6D(12680, 2250, 15980, 5500)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_52A)
    FadeToBright(2000, 0)
    OP_0D()
    OP_43(0x13, 0x0, 0x0, 0x5)
    OP_43(0x14, 0x0, 0x0, 0x6)
    OP_43(0x16, 0x0, 0x0, 0x7)
    WaitChrThread(0x0, 0x0)
    Sleep(1000)
    Fade(500)
    OP_6D(11200, 2000, 16070, 0)
    OP_67(0, 5940, -10000, 0)
    OP_6B(2460, 0)
    OP_6C(45000, 0)
    OP_6E(340, 0)
    OP_0D()
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x11, 0x0)
    Sleep(300)

    ChrTalk(    #1
        0x10,
        (
            "#070F#5P唔，亚尔摩村吗……\x02\x03",

            "难得再来拜访一次，\x01",
            "果然是风情十足的地方啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x11,
        (
            "#790F#6P是啊……\x02\x03",

            "偶尔体味一下\x01",
            "故乡的气氛也不错。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 17420, 2000, 8480, 315)
    Sleep(300)

    NpcTalk(    #3
        0x12,
        "女性的声音",
        "#1P哎呀，两位。\x02",
    )

    CloseMessageWindow()

    def lambda_686():
        OP_6D(11890, 2000, 14110, 2500)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_686)

    def lambda_69E():
        OP_67(0, 5090, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_69E)

    def lambda_6B6():
        OP_6B(2410, 2500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_6B6)

    def lambda_6C6():
        OP_6C(90000, 2500)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_6C6)

    def lambda_6D6():
        OP_6E(339, 2500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_6D6)
    OP_43(0x12, 0x0, 0x0, 0x4)
    Sleep(500)
    OP_8C(0x10, 135, 400)
    OP_8C(0x11, 135, 400)
    WaitChrThread(0x12, 0x0)
    WaitChrThread(0x0, 0x0)
    Sleep(300)

    ChrTalk(    #4
        0x12,
        "#1110F#2P呵呵，恭候多时了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x10,
        "#070F#6P您好，大使。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x11,
        "#790F#6P承蒙您的招待，感激不尽。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x12,
        (
            "#1110F#2P是我叫你们来的，\x01",
            "就不要客气了。\x02\x03",

            "那么，\x01",
            "总之先进去谈吧。\x02\x03",

            "赶快把工作解决掉，\x01",
            "就能悠闲享受了。\x02",
        )
    )

    Jump("loc_7EA")

    label("loc_7EA")

    CloseMessageWindow()

    ChrTalk(    #8
        0x10,
        "#070F#6P哈哈，非常赞成您的想法。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x11,
        "#790F#6P嗯，我们走吧。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2506)
    NewScene("ED6_DT21/T3221   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_3E6 end

    def Function_4_84E(): pass

    label("Function_4_84E")

    OP_8F(0xFE, 0x2B70, 0x7D0, 0x332C, 0x7D0, 0x0)
    Return()

    # Function_4_84E end

    def Function_5_863(): pass

    label("Function_5_863")

    OP_8E(0xFE, 0x2ED6, 0x7D0, 0x2D96, 0x1770, 0x0)

    def lambda_87D():
        OP_8E(0xFE, 0x2F58, 0x7D0, 0x56D6, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_87D)
    OP_62(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    WaitChrThread(0xFE, 0x1)
    OP_8E(0xFE, 0x3660, 0xFA0, 0x8AE8, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_5_863 end

    def Function_6_8C3(): pass

    label("Function_6_8C3")

    OP_8E(0xFE, 0x2ED6, 0x7D0, 0x2D96, 0x1770, 0x0)

    def lambda_8DD():
        OP_8E(0xFE, 0x2F58, 0x7D0, 0x56D6, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8DD)
    Sleep(300)
    OP_62(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    WaitChrThread(0xFE, 0x1)
    OP_8E(0xFE, 0x3660, 0xFA0, 0x8AE8, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_6_8C3 end

    def Function_7_928(): pass

    label("Function_7_928")

    OP_72(0x800, 0x0)
    ExitThread()
    OP_72(0x1000, 0x0)
    ExitThread()
    OP_6F(0x0, 0)
    OP_70(0x0, 0x1D)
    OP_73(0x0)
    Sleep(300)
    SetChrPos(0xFE, 1070, 500, 19890, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x384, 0x0, 0x460A, 0x7D0, 0x0)
    Sleep(300)
    OP_8C(0xFE, 270, 400)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_7_928 end

    def Function_8_999(): pass

    label("Function_8_999")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_22(0x1C2, 0x50, 0x64)
    Sleep(1500)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(19580, 2000, 5840, 0)
    OP_67(0, 7880, -10000, 0)
    OP_6B(3050, 0)
    OP_6C(45000, 0)
    OP_6E(271, 0)

    def lambda_A06():
        OP_6D(27070, 2000, 5410, 3500)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_A06)

    def lambda_A1E():
        OP_67(0, 7160, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_A1E)

    def lambda_A36():
        OP_6B(2330, 3500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_A36)

    def lambda_A46():
        OP_6E(341, 3500)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_A46)
    FadeToBright(2000, 0)
    OP_0D()
    OP_72(0x804, 0x0)
    ExitThread()
    OP_72(0x1004, 0x0)
    ExitThread()
    OP_6F(0x4, 0)
    OP_70(0x4, 0x1D)
    OP_73(0x4)
    Sleep(200)
    OP_43(0x12, 0x0, 0x0, 0x9)
    OP_43(0x11, 0x0, 0x0, 0xA)
    OP_43(0x10, 0x0, 0x0, 0xB)
    WaitChrThread(0x0, 0x0)
    Sleep(1000)
    OP_6F(0x4, 29)
    OP_70(0x4, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    WaitChrThread(0x12, 0x0)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x10, 0x0)

    ChrTalk(    #10
        0x12,
        (
            "#1113F#6P啊，\x01",
            "好久没有睡得这么香了。\x02\x03",

            "#1110F你们两位\x01",
            "玩得可开心？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x10,
        "#071F#5P嗯嗯，那当然了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x11,
        (
            "#792F#11P托您的福，好好休养了一番。\x02\x03",

            "#791F至少有足够的精神\x01",
            "向新环境发起挑战了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #13
        0x12,
        "#1111F#6P那么……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x11,
        (
            "#792F#11P……谨遵吩咐。\x02\x03",

            "#791F请代我们\x01",
            "向总统阁下问好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x12,
        (
            "#1111F#6P嗯嗯，当然了！\x02\x03",

            "#1110F呵呵，听了你们的答复，\x01",
            "身体感觉更轻快了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x11,
        (
            "#790F#1P只不过我还要安排工作交接，\x01",
            "回国将在两、三个月后。\x02\x03",

            "这点请您谅解。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x12,
        (
            "#1110F#6P没问题。\x02\x03",

            "那就期待和您\x01",
            "在共和国再见。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x11,
        "#790F#2P嗯嗯，彼此彼此。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_24(0x1C2, 0x46)
    Sleep(100)
    OP_24(0x1C2, 0x3C)
    Sleep(100)
    OP_24(0x1C2, 0x32)
    Sleep(100)
    OP_24(0x1C2, 0x28)
    Sleep(100)
    OP_24(0x1C2, 0x1E)
    Sleep(100)
    OP_24(0x1C2, 0x14)
    Sleep(100)
    OP_24(0x1C2, 0xA)
    Sleep(100)
    OP_24(0x1C2, 0x0)
    OP_23(0x1C2)
    OP_6D(-80, 2120, 14670, 0)
    OP_67(0, 6910, -10000, 0)
    OP_6B(2330, 0)
    OP_6C(45000, 0)
    OP_6E(325, 0)
    SetChrFlags(0x12, 0x80)
    SetChrPos(0x11, 9940, 2000, 14630, 270)
    SetChrPos(0x10, 10440, 2000, 15880, 270)

    def lambda_DB2():
        OP_8E(0xFE, 0x2A8, 0x0, 0x38F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_DB2)
    Sleep(100)

    def lambda_DD2():
        OP_8E(0xFE, 0x1C2, 0x0, 0x3F0C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_DD2)

    def lambda_DED():
        OP_6D(1860, 0, 16830, 4000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_DED)

    def lambda_E05():
        OP_67(0, 5370, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_E05)

    def lambda_E1D():
        OP_6B(2490, 4000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_E1D)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(2500)

    ChrTalk(    #19
        0x10,
        "#070F#5P唔……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x0, 0x0)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x10, 0xB4)
    Sleep(100)
    OP_8C(0x11, 0, 400)

    ChrTalk(    #20
        0x11,
        "#790F#4P你在考虑什么？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10, 180, 400)

    ChrTalk(    #21
        0x10,
        (
            "#070F#5P啊，关于刚才的事。\x02\x03",

            "你说工作交接完成需要\x01",
            "两、三个月吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x11,
        (
            "#790F#4P嗯嗯，是啊……\x02\x03",

            "这有什么问题吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x10,
        (
            "#070F#5P现在又没有什么\x01",
            "特别紧急的工作……\x02\x03",

            "……既然如此，\x01",
            "我也待到那时候好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x11,
        (
            "#790F#4P我才不需要陪同。\x01",
            "你赶快回去吧。\x02\x03",

            "那边还有工作在等着你呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x10,
        (
            "#070F#5P………………………………\x02\x03",

            "真是冷淡的家伙啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x11,
        (
            "#790F#4P呵呵，不好吗。\x02\x03",

            "反正今后就算不愿意，\x01",
            "也得一直见面了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x10,
        "#070F#5P雾香……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 270, 400)
    SetChrFlags(0x10, 0x2)
    SetChrChipByIndex(0x10, 9)
    SetChrSubChip(0x10, 0)

    def lambda_1063():
        OP_8E(0xFE, 0xFFFFF2EA, 0x0, 0x39D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_1063)

    ChrTalk(    #28
        0x10,
        (
            "#070F#5P……哈哈，是啊。\x02\x03",

            "没什么好着急的……吗。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x11, 0x0)
    Sleep(300)

    def lambda_10C2():
        OP_6D(-220, 0, 16580, 1500)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_10C2)
    OP_8C(0x11, 90, 400)
    WaitChrThread(0x0, 0x0)
    Sleep(200)

    ChrTalk(    #29
        0x11,
        (
            "#790F#6P金……\x02\x03",

            "你在发什么呆？\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x10, 0x2)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)

    ChrTalk(    #30
        0x10,
        "#070F#5P啊……！？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10, 270, 400)

    ChrTalk(    #31
        0x10,
        "#070F#2P哦、哦……抱歉。\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_1168():
        OP_6D(-2290, 0, 16590, 1000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_1168)

    def lambda_1180():

        label("loc_1180")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_1180")

    QueueWorkItem2(0x11, 1, lambda_1180)
    SetChrChipByIndex(0x10, 3)

    def lambda_1196():
        OP_8E(0xFE, 0xFFFFF290, 0x0, 0x3EA8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1196)
    WaitChrThread(0x10, 0x0)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)
    OP_8C(0x10, 180, 400)
    OP_44(0x11, 0x1)
    Sleep(500)
    OP_8C(0x11, 270, 400)

    def lambda_11D7():
        OP_8E(0xFE, 0xFFFFCA72, 0xFFFFF830, 0x3A02, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_11D7)
    Sleep(200)
    OP_8C(0x10, 270, 400)

    def lambda_11FE():
        OP_8E(0xFE, 0xFFFFCA68, 0xFFFFF830, 0x3F2A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_11FE)
    Sleep(1500)

    def lambda_121E():
        OP_6B(3000, 5000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_121E)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x0, 0x2)
    OP_20(0x7D0)
    Sleep(2000)
    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12D6")
    Sleep(1000)
    OP_28(0x9, 0x4, 0x10)
    OP_28(0x9, 0x4, 0x20)
    OP_3E(0x2D7, 1)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #32
        "\x07\x00得到了\x1F\xD7\x02\x07\x00。\x02",
    )

    Jump("loc_1296")

    label("loc_1296")

    CloseMessageWindow()
    AddMira(4000)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #33
        "\x07\x00得到了\x07\x02４０００米拉\x07\x00。\x02",
    )

    Jump("loc_12C1")

    label("loc_12C1")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_12D6")

    OP_A2(0x2505)
    NewScene("ED6_DT21/M7102   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_8_999 end

    def Function_9_12E3(): pass

    label("Function_9_12E3")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 31000, 2500, 4000, 270)

    def lambda_130A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_130A)

    def lambda_131C():
        OP_8E(0xFE, 0x5FDC, 0x7D0, 0x1054, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_131C)
    WaitChrThread(0xFE, 0x1)
    WaitChrThread(0xFE, 0x2)
    Sleep(200)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_9_12E3 end

    def Function_10_1348(): pass

    label("Function_10_1348")

    Sleep(800)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 31000, 2500, 3870, 270)

    def lambda_1374():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1374)

    def lambda_1386():
        OP_8E(0xFE, 0x678E, 0x7D0, 0xF5A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1386)
    WaitChrThread(0xFE, 0x1)
    WaitChrThread(0xFE, 0x2)
    Return()

    # Function_10_1348 end

    def Function_11_13A6(): pass

    label("Function_11_13A6")

    Sleep(1500)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 31000, 2500, 4000, 270)

    def lambda_13D2():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_13D2)

    def lambda_13E4():
        OP_8E(0xFE, 0x6874, 0x7D0, 0x1310, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_13E4)
    WaitChrThread(0xFE, 0x1)
    WaitChrThread(0xFE, 0x2)
    Return()

    # Function_11_13A6 end

    def Function_12_1404(): pass

    label("Function_12_1404")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x13, 18420, 2000, 11830, 270)
    SetChrPos(0x14, 20510, 2000, 11850, 270)
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #34
        "\x07\x00#40W之后过了两天――\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(1000)
    OP_6D(-12560, -2000, 15790, 0)
    OP_67(0, 8690, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(45000, 0)
    OP_6E(312, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x11, -3160, 0, 14840, 90)
    SetChrPos(0x10, -2220, 0, 15780, 90)
    OP_1D(0xF)

    def lambda_1509():
        OP_8E(0xFE, 0x2698, 0x7D0, 0x3B56, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1509)
    Sleep(100)

    def lambda_1529():
        OP_8E(0xFE, 0x2332, 0x7D0, 0x3746, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_1529)

    def lambda_1544():
        OP_6D(12680, 2250, 15980, 6000)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_1544)
    OP_C8(0x200, 0x46, "C_PLAC10._CH", 0x1, 0x7D0)
    FadeToBright(2000, 0)
    OP_0D()
    OP_43(0x13, 0x0, 0x0, 0x5)
    OP_43(0x14, 0x0, 0x0, 0x6)
    OP_43(0x16, 0x0, 0x0, 0x7)
    WaitChrThread(0x17, 0x0)
    Sleep(500)
    Fade(500)
    OP_6D(11200, 2000, 16070, 0)
    OP_67(0, 5940, -10000, 0)
    OP_6B(2460, 0)
    OP_6C(45000, 0)
    OP_6E(340, 0)
    OP_0D()
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x11, 0x0)
    Sleep(500)

    ChrTalk(    #35
        0x10,
        (
            "#070F#5P唔，亚尔摩村吗……\x02\x03",

            "难得再来拜访一次，\x01",
            "果然是风情十足的地方啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x11,
        (
            "#792F#6P呵呵，是啊……\x02\x03",

            "#791F这里和我们的故乡\x01",
            "十分相像呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x10,
        (
            "#075F#5P……呼。\x01",
            "不过我还真是有些焦虑。\x02\x03",

            "刚听说这件事时，\x01",
            "还以为难不成\x01",
            "要和爱尔莎大使两人来旅行呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x10, 400)
    Sleep(300)

    ChrTalk(    #38
        0x11,
        (
            "#791F#6P哎呀，金……你好像觉得很遗憾嘛。\x02\x03",

            "#792F要不我就在这里\x01",
            "打道回府吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x10, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x10, 0x11, 500)

    ChrTalk(    #39
        0x10,
        (
            "#072F#5P我、我说啊……\x01",
            "就算是我，也不会把大使作为目标啊。\x02\x03",

            "再说了，\x01",
            "大使其实是找你有事吧？\x02",
        )
    )

    Jump("loc_181E")

    label("loc_181E")

    CloseMessageWindow()

    ChrTalk(    #40
        0x11,
        (
            "#794F#6P呵呵，这种程度的玩笑就让你动摇，\x01",
            "你还真是老样子。\x02\x03",

            "你就不能回答得\x01",
            "更机灵点儿吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x10,
        (
            "#075F#5P唔……\x02\x03",

            "#072F真是的……\x01",
            "你还是那么毫不留情啊。\x02\x03",

            "利贝尔的游击士们\x01",
            "居然还能跟你相处下去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x11,
        (
            "#792F#6P嗯，\x01",
            "因为只有对你才用这种态度嘛。\x02\x03",

            "#791F……这么说你会高兴吗？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #43
        0x10,
        "#075F#5P#3S高兴才怪！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 17420, 2000, 8480, 315)
    Sleep(500)

    NpcTalk(    #44
        0x12,
        "女性的声音",
        "#1P哎呀，两位。\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x10, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_1A17():
        OP_6D(11890, 2000, 14110, 2500)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_1A17)

    def lambda_1A2F():
        OP_67(0, 5090, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_1A2F)

    def lambda_1A47():
        OP_6B(2410, 2500)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_1A47)

    def lambda_1A57():
        OP_6C(90000, 2500)
        ExitThread()

    QueueWorkItem(0x17, 3, lambda_1A57)

    def lambda_1A67():
        OP_6E(339, 2500)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_1A67)
    OP_43(0x12, 0x0, 0x0, 0x4)
    Sleep(500)
    OP_8C(0x10, 135, 400)
    OP_8C(0x11, 135, 400)
    WaitChrThread(0x12, 0x0)
    WaitChrThread(0x17, 0x0)
    Sleep(500)

    ChrTalk(    #45
        0x12,
        "#1111F#11P呵呵，我恭候多时了呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x10,
        "#070F#6P您、您好，大使。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x11,
        "#792F#6P承蒙招待，感激不尽。\x02",
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x12, 0x10, 400)

    ChrTalk(    #48
        0x12,
        (
            "#1112F#11P哎呀，金先生。\x02\x03",

            "您看起来有点心神不宁，\x01",
            "是发生什么事了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x10,
        (
            "#071F#6P咦，啊……\x01",
            "是大使多心了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x11,
        (
            "#792F#6P呵呵，\x01",
            "怎么说都是和两位美女一起温泉旅行……\x02\x03",

            "#791F确实让人静不下心啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x10,
        "#072F#5P喂、喂，雾香……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x12,
        (
            "#1113F#11P呵呵，是啊……\x02\x03",

            "#1111F我要是再年轻点儿，\x01",
            "也不会对金先生\x01",
            "置之不理呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x10,
        "#073F#6P呃……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x12,
        (
            "#1110F#11P呵呵，\x01",
            "玩笑暂且到此为止，先去吃晚餐吧。\x02\x03",

            "据说毛婆婆\x01",
            "今晚会亲自下厨哦。\x02\x03",

            "严肃的话题\x01",
            "就等餐后再慢慢说吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x10,
        (
            "#075F#6P啊、啊啊……\x01",
            "我十分赞成您的想法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x11,
        "#791F#6P那么，我们走吧。\x02",
    )

    CloseMessageWindow()
    OP_59()

    def lambda_1DAC():
        OP_6B(2800, 3000)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_1DAC)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_20(0xFA0)
    OP_21()
    Sleep(1000)
    OP_A2(0x2506)
    NewScene("ED6_DT21/T3223   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_12_1404 end

    def Function_13_1DD9(): pass

    label("Function_13_1DD9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Sleep(1000)
    OP_22(0x1C2, 0x1, 0x50)
    Sleep(1000)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(19580, 2000, 5840, 0)
    OP_67(0, 7880, -10000, 0)
    OP_6B(3050, 0)
    OP_6C(45000, 0)
    OP_6E(271, 0)

    def lambda_1E4B():
        OP_6D(27070, 2000, 5410, 3500)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_1E4B)

    def lambda_1E63():
        OP_67(0, 7160, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_1E63)

    def lambda_1E7B():
        OP_6B(2330, 3500)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_1E7B)

    def lambda_1E8B():
        OP_6E(341, 3500)
        ExitThread()

    QueueWorkItem(0x17, 3, lambda_1E8B)
    FadeToBright(2000, 0)
    OP_0D()
    OP_72(0x804, 0x0)
    ExitThread()
    OP_72(0x1004, 0x0)
    ExitThread()
    OP_6F(0x4, 0)
    OP_70(0x4, 0x1D)
    OP_73(0x4)
    Sleep(200)
    OP_43(0x12, 0x0, 0x0, 0x9)
    OP_43(0x11, 0x0, 0x0, 0xA)
    OP_43(0x10, 0x0, 0x0, 0xB)
    WaitChrThread(0x17, 0x0)
    Sleep(200)
    OP_24(0x1C2, 0x46)
    Sleep(200)
    OP_24(0x1C2, 0x3C)
    Sleep(200)
    OP_24(0x1C2, 0x32)
    Sleep(200)
    OP_24(0x1C2, 0x28)
    Sleep(200)
    OP_23(0x1C2)
    OP_72(0x4, 0x8)
    ExitThread()
    OP_6F(0x4, 29)
    OP_70(0x4, 0x0)
    OP_22(0x7, 0x0, 0x64)
    WaitChrThread(0x12, 0x0)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x10, 0x0)
    Sleep(500)

    ChrTalk(    #57
        0x12,
        (
            "#1113F#6P呼～\x01",
            "好久没有睡得这么香了。\x02\x03",

            "#1110F你们两位\x01",
            "玩得可开心？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x10,
        "#071F#5P嗯嗯，那当然了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x11,
        (
            "#792F#11P托您的福，好好休养了一番。\x02\x03",

            "#791F至少有足够的精神\x01",
            "向新环境发起挑战了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #60
        0x12,
        "#1111F#6P那、那么……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x11,
        (
            "#791F#11P……谨遵吩咐。\x02\x03",

            "#792F只不过，有一个条件。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x12,
        "#1112F#6P是什么，说来听听？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x11,
        (
            "#792F#11P我纯粹是\x01",
            "基于自己的信念\x01",
            "才置身于某个组织的。\x02\x03",

            "#790F如果对组织的运营\x01",
            "感到哪怕有些许的疑惑的时候……\x02\x03",

            "我将毫不留情\x01",
            "纠正组织本身的存在方式。\x02\x03",

            "如果允许我这么做，\x01",
            "就请代为向总统阁下问好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x12,
        (
            "#1111F#6P呵呵，当然了。\x02\x03",

            "#1113F……游击士协会\x01",
            "在某种意义上来说，\x01",
            "是建立在如履薄冰般的平衡上的组织。\x02\x03",

            "#1110F要挖掘这组织里的人，\x01",
            "说明总统正是在期待\x01",
            "你们完成这种职能。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x11,
        (
            "#792F#11P呵呵，是这样吗。\x02\x03",

            "#790F不过我还要安排工作交接，\x01",
            "回国将在两、三个月后。\x02\x03",

            "这点请您谅解。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x12,
        (
            "#1113F#6P完全没问题。\x02\x03",

            "#1111F那就期待和您\x01",
            "在共和国再见。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x11,
        "#791F#11P嗯嗯，彼此彼此。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_6D(-80, 2120, 14670, 0)
    OP_67(0, 6910, -10000, 0)
    OP_6B(2330, 0)
    OP_6C(45000, 0)
    OP_6E(325, 0)
    SetChrFlags(0x12, 0x80)
    SetChrPos(0x11, 9940, 2000, 14630, 270)
    SetChrPos(0x10, 10440, 2000, 15880, 270)

    def lambda_23C4():
        OP_8E(0xFE, 0x2A8, 0x0, 0x38F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_23C4)
    Sleep(100)

    def lambda_23E4():
        OP_8E(0xFE, 0x1C2, 0x0, 0x3F0C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_23E4)

    def lambda_23FF():
        OP_6D(1860, 0, 16830, 4000)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_23FF)

    def lambda_2417():
        OP_67(0, 5370, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_2417)

    def lambda_242F():
        OP_6B(2490, 4000)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_242F)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x17, 0x0)

    ChrTalk(    #68 op#A
        0x10,
        "#074F#5P#12A唔……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x10, 0xB4)
    Sleep(500)
    OP_8C(0x11, 0, 400)
    Sleep(300)

    ChrTalk(    #69
        0x11,
        "#791F#12P你在考虑什么？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10, 180, 400)
    Sleep(300)

    ChrTalk(    #70
        0x10,
        (
            "#070F#5P啊，关于刚才的事。\x02\x03",

            "你说工作交接完成需要\x01",
            "两、三个月吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x11,
        (
            "#790F#12P嗯嗯，是啊……\x02\x03",

            "这有什么问题吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x10,
        (
            "#573F#5P虽然卡尔瓦德那边比较忙，\x01",
            "但应该也没有什么\x01",
            "特别紧急的工作。\x02\x03",

            "#070F既然如此，\x01",
            "我也暂时待在利贝尔好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x11,
        (
            "#792F#12P还以为你要说什么呢……\x02\x03",

            "#790F我不需要陪同。\x01",
            "你赶快回去吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2300, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #74
        0x10,
        (
            "#075F#5P呼……\x01",
            "真是冷淡的家伙啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x11,
        (
            "#791F#12P呵呵，不好吗。\x02\x03",

            "反正今后就算不愿意，\x01",
            "也得一直见面了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x10,
        "#073F#5P啊……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 270, 400)
    Sleep(300)
    SetChrFlags(0x10, 0x2)
    SetChrChipByIndex(0x10, 9)
    SetChrSubChip(0x10, 0)

    def lambda_26F1():
        OP_8E(0xFE, 0xFFFFF2EA, 0x0, 0x39D0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_26F1)
    Sleep(500)

    ChrTalk(    #77 op#A
        0x10,
        (
            "#573F#5P#20W#15A……哈哈，是啊。\x02\x03",

            "#25A#20W没什么好着急的……吗。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x11, 0x0)
    Sleep(300)

    def lambda_276B():
        OP_6D(-220, 0, 16580, 1500)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_276B)
    OP_8C(0x11, 90, 400)
    WaitChrThread(0x17, 0x0)
    Sleep(300)

    ChrTalk(    #78
        0x11,
        (
            "#790F#6P金……\x02\x03",

            "你在发什么呆？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    ClearChrFlags(0x10, 0x2)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)

    ChrTalk(    #79
        0x10,
        "#073F#5P啊……！？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x11, 400)
    Sleep(300)

    ChrTalk(    #80
        0x10,
        (
            "#075F#11P哦、哦……抱歉。\x02\x03",

            "#072F喂，\x01",
            "你也别一个人走那么快啊！\x02",
        )
    )

    Jump("loc_286C")

    label("loc_286C")

    CloseMessageWindow()

    def lambda_2873():
        OP_6D(-2290, 0, 16590, 1000)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_2873)

    def lambda_288B():

        label("loc_288B")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_288B")

    QueueWorkItem2(0x11, 1, lambda_288B)
    SetChrChipByIndex(0x10, 3)

    def lambda_28A1():
        OP_8E(0xFE, 0xFFFFF290, 0x0, 0x3EA8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_28A1)
    WaitChrThread(0x10, 0x0)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)
    OP_8C(0x10, 180, 400)
    OP_44(0x11, 0x1)
    Sleep(500)
    OP_8C(0x11, 270, 400)

    def lambda_28E2():
        OP_8E(0xFE, 0xFFFFCA72, 0xFFFFF830, 0x3A02, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_28E2)
    Sleep(200)
    OP_8C(0x10, 270, 400)

    def lambda_2909():
        OP_8E(0xFE, 0xFFFFCA68, 0xFFFFF830, 0x3F2A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_2909)
    Sleep(1500)

    def lambda_2929():
        OP_6B(3000, 5000)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_2929)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x17, 0x2)
    OP_20(0xFA0)
    OP_21()
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(350, 400, -1, -1)
    SetChrName("")

    AnonymousTalk(    #81
        "\x07\x00Episode『旅程的终点』　～Fin～\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    OP_C2(0x1, 0x0)
    Call(6, 25)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A1F")
    Sleep(1000)
    OP_28(0x9, 0x4, 0x10)
    OP_28(0x9, 0x4, 0x20)
    OP_3E(0x2D7, 1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #82
        "\x07\x00得到了\x1F\xD7\x02\x07\x00。\x02",
    )

    Jump("loc_29E8")

    label("loc_29E8")

    CloseMessageWindow()
    AddMira(4000)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #83
        "\x07\x00得到了\x07\x02４０００米拉\x07\x00。\x02",
    )

    Jump("loc_2A13")

    label("loc_2A13")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_2A1F")

    OP_A2(0x2505)
    NewScene("ED6_DT21/M7102   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_13_1DD9 end

    SaveToFile()

Try(main)
