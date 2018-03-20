from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        'Zin',                                  # 9
        'Kilika',                               # 10
        'Ambassador Cochrane',                  # 11
        'Lucky',                                # 12
        'Quantay',                              # 13
        'Faults',                               # 14
        'Tourist',                              # 15
        'Target Camera',                        # 16
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
        "Function_4_8ED",          # 04, 4
        "Function_5_902",          # 05, 5
        "Function_6_962",          # 06, 6
        "Function_7_9C7",          # 07, 7
        "Function_8_A38",          # 08, 8
        "Function_9_1621",         # 09, 9
        "Function_10_1686",        # 0A, 10
        "Function_11_16E4",        # 0B, 11
        "Function_12_1742",        # 0C, 12
        "Function_13_22D8",        # 0D, 13
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
        "\x07\x05Two days later...\x02",
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

    def lambda_4EE():
        OP_8E(0xFE, 0x2698, 0x7D0, 0x3B56, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_4EE)
    Sleep(100)

    def lambda_50E():
        OP_8E(0xFE, 0x2332, 0x7D0, 0x3746, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_50E)

    def lambda_529():
        OP_6D(12680, 2250, 15980, 5500)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_529)
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
            "#070F#5PThis place sure brings back memories.\x02\x03",

            "The atmosphere really is relaxing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x11,
        (
            "#790F#6PYeah...\x02\x03",

            "Especially given how similar it is to our \x01",
            "hometown.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 17420, 2000, 8480, 315)
    Sleep(300)

    NpcTalk(    #3
        0x12,
        "Woman's Voice",
        "#1PAh, you've arrived.\x02",
    )

    CloseMessageWindow()

    def lambda_6A3():
        OP_6D(11890, 2000, 14110, 2500)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_6A3)

    def lambda_6BB():
        OP_67(0, 5090, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_6BB)

    def lambda_6D3():
        OP_6B(2410, 2500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_6D3)

    def lambda_6E3():
        OP_6C(90000, 2500)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_6E3)

    def lambda_6F3():
        OP_6E(339, 2500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_6F3)
    OP_43(0x12, 0x0, 0x0, 0x4)
    Sleep(500)
    OP_8C(0x10, 135, 400)
    OP_8C(0x11, 135, 400)
    WaitChrThread(0x12, 0x0)
    WaitChrThread(0x0, 0x0)
    Sleep(300)

    ChrTalk(    #4
        0x12,
        "#1110F#2PHaha. I've been waiting for the two of you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x10,
        "#070F#6PH-Hey, Ambassador.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x11,
        "#790F#6PThank you for inviting us here today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x12,
        (
            "#1110F#2POh, if anything you're doing me a favor by coming.\x01",
            "There's no need for such formalities.\x02\x03",

            "Well, let's go inside and get to talking.\x02\x03",

            "The sooner we finish the work part of this, the\x01",
            "sooner we can get to relaxing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x10,
        "#070F#6PHaha. Sounds good to me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x11,
        "#790F#6PIndeed.\x02",
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

    def Function_4_8ED(): pass

    label("Function_4_8ED")

    OP_8F(0xFE, 0x2B70, 0x7D0, 0x332C, 0x7D0, 0x0)
    Return()

    # Function_4_8ED end

    def Function_5_902(): pass

    label("Function_5_902")

    OP_8E(0xFE, 0x2ED6, 0x7D0, 0x2D96, 0x1770, 0x0)

    def lambda_91C():
        OP_8E(0xFE, 0x2F58, 0x7D0, 0x56D6, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_91C)
    OP_62(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    WaitChrThread(0xFE, 0x1)
    OP_8E(0xFE, 0x3660, 0xFA0, 0x8AE8, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_5_902 end

    def Function_6_962(): pass

    label("Function_6_962")

    OP_8E(0xFE, 0x2ED6, 0x7D0, 0x2D96, 0x1770, 0x0)

    def lambda_97C():
        OP_8E(0xFE, 0x2F58, 0x7D0, 0x56D6, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_97C)
    Sleep(300)
    OP_62(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    WaitChrThread(0xFE, 0x1)
    OP_8E(0xFE, 0x3660, 0xFA0, 0x8AE8, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_6_962 end

    def Function_7_9C7(): pass

    label("Function_7_9C7")

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

    # Function_7_9C7 end

    def Function_8_A38(): pass

    label("Function_8_A38")

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

    def lambda_AA5():
        OP_6D(27070, 2000, 5410, 3500)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_AA5)

    def lambda_ABD():
        OP_67(0, 7160, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_ABD)

    def lambda_AD5():
        OP_6B(2330, 3500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_AD5)

    def lambda_AE5():
        OP_6E(341, 3500)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_AE5)
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
            "#1113F#6PAah... That was the best night's sleep I've had in\x01",
            "quite some time.\x02\x03",

            "#1110FI hope the two of you enjoyed your stay, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x10,
        "#071F#5PI know I did!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x11,
        (
            "#792F#11PI'm feeling very energized indeed, thank you.\x02\x03",

            "#791FEnergized enough to feel ready to take on a new\x01",
            "position in a new environment, even.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #13
        0x12,
        "#1111F#6PThen...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x11,
        (
            "#792F#11P...I'll accept your offer.\x02\x03",

            "#791FPlease pass that on to the prime minister.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x12,
        (
            "#1111F#6PBut of course!\x02\x03",

            "#1110FHaha. Now I'm feeling even better than I did\x01",
            "earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x11,
        (
            "#790F#1PStill, I'll need two or three months to get \x01",
            "everything ready for my successor.\x02\x03",

            "As such, I won't be able to start work until then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x12,
        (
            "#1110F#6PThat's perfectly understandable.\x02\x03",

            "Well... I look forward to meeting you again in the\x01",
            "Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x11,
        "#790F#2PLikewise.\x02",
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

    def lambda_F4E():
        OP_8E(0xFE, 0x2A8, 0x0, 0x38F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_F4E)
    Sleep(100)

    def lambda_F6E():
        OP_8E(0xFE, 0x1C2, 0x0, 0x3F0C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_F6E)

    def lambda_F89():
        OP_6D(1860, 0, 16830, 4000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_F89)

    def lambda_FA1():
        OP_67(0, 5370, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_FA1)

    def lambda_FB9():
        OP_6B(2490, 4000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_FB9)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(2500)

    ChrTalk(    #19
        0x10,
        "#070F#5PHmm...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x0, 0x0)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x10, 0xB4)
    Sleep(100)
    OP_8C(0x11, 0, 400)

    ChrTalk(    #20
        0x11,
        "#790F#4P...Is something on your mind?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10, 180, 400)

    ChrTalk(    #21
        0x10,
        (
            "#070F#5POh, I was just thinking about what you said back\x01",
            "there.\x02\x03",

            "You said you'll need two or three months to get\x01",
            "everything ready for your successor, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x11,
        (
            "#790F#4PYes, I did...\x02\x03",

            "What of it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x10,
        (
            "#070F#5PWell, it's not like there's any urgent work for me\x01",
            "here or in Calvard...\x02\x03",

            "So I was thinking maybe I could stay here for the\x01",
            "next few months while you get things sorted, then\x01",
            "head back after that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x11,
        (
            "#790F#4PThere's no reason why you should stay around here \x01",
            "in Liberl with me. Go on back to Calvard.\x02\x03",

            "There'll be work waiting for you there, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x10,
        (
            "#070F#5P...\x02\x03",

            "*sigh* There's no need to be that cold with me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x11,
        (
            "#790F#4PHaha. Well, it's the truth.\x02\x03",

            "We'll have more than enough chances to spend time\x01",
            "together after I get to Calvard as it is without\x01",
            "you going out of your way to make more now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x10,
        "#070F#5PKilika...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 270, 400)
    SetChrFlags(0x10, 0x2)
    SetChrChipByIndex(0x10, 9)
    SetChrSubChip(0x10, 0)

    def lambda_1394():
        OP_8E(0xFE, 0xFFFFF2EA, 0x0, 0x39D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_1394)

    ChrTalk(    #28
        0x10,
        (
            "#070F#5P...Haha. I suppose you're right.\x02\x03",

            "There's no need to rush things...\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x11, 0x0)
    Sleep(300)

    def lambda_140A():
        OP_6D(-220, 0, 16580, 1500)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_140A)
    OP_8C(0x11, 90, 400)
    WaitChrThread(0x0, 0x0)
    Sleep(200)

    ChrTalk(    #29
        0x11,
        (
            "#790F#6PZin?\x02\x03",

            "What are you standing there for?\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x10, 0x2)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)

    ChrTalk(    #30
        0x10,
        "#070F#5P...Oh!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10, 270, 400)

    ChrTalk(    #31
        0x10,
        "#070F#2PS-Sorry...\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_14AE():
        OP_6D(-2290, 0, 16590, 1000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_14AE)

    def lambda_14C6():

        label("loc_14C6")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_14C6")

    QueueWorkItem2(0x11, 1, lambda_14C6)
    SetChrChipByIndex(0x10, 3)

    def lambda_14DC():
        OP_8E(0xFE, 0xFFFFF290, 0x0, 0x3EA8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_14DC)
    WaitChrThread(0x10, 0x0)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)
    OP_8C(0x10, 180, 400)
    OP_44(0x11, 0x1)
    Sleep(500)
    OP_8C(0x11, 270, 400)

    def lambda_151D():
        OP_8E(0xFE, 0xFFFFCA72, 0xFFFFF830, 0x3A02, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_151D)
    Sleep(200)
    OP_8C(0x10, 270, 400)

    def lambda_1544():
        OP_8E(0xFE, 0xFFFFCA68, 0xFFFFF830, 0x3F2A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1544)
    Sleep(1500)

    def lambda_1564():
        OP_6B(3000, 5000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_1564)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x0, 0x2)
    OP_20(0x7D0)
    Sleep(2000)
    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1614")
    Sleep(1000)
    OP_28(0x9, 0x4, 0x10)
    OP_28(0x9, 0x4, 0x20)
    OP_3E(0x2D7, 1)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #32
        "\x07\x05Obtained \x1F\xD7\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    AddMira(4000)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #33
        "\x07\x05Obtained \x07\x024,000 mira\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_1614")

    OP_A2(0x2505)
    NewScene("ED6_DT21/M7102   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_8_A38 end

    def Function_9_1621(): pass

    label("Function_9_1621")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 31000, 2500, 4000, 270)

    def lambda_1648():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1648)

    def lambda_165A():
        OP_8E(0xFE, 0x5FDC, 0x7D0, 0x1054, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_165A)
    WaitChrThread(0xFE, 0x1)
    WaitChrThread(0xFE, 0x2)
    Sleep(200)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_9_1621 end

    def Function_10_1686(): pass

    label("Function_10_1686")

    Sleep(800)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 31000, 2500, 3870, 270)

    def lambda_16B2():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_16B2)

    def lambda_16C4():
        OP_8E(0xFE, 0x678E, 0x7D0, 0xF5A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_16C4)
    WaitChrThread(0xFE, 0x1)
    WaitChrThread(0xFE, 0x2)
    Return()

    # Function_10_1686 end

    def Function_11_16E4(): pass

    label("Function_11_16E4")

    Sleep(1500)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 31000, 2500, 4000, 270)

    def lambda_1710():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1710)

    def lambda_1722():
        OP_8E(0xFE, 0x6874, 0x7D0, 0x1310, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1722)
    WaitChrThread(0xFE, 0x1)
    WaitChrThread(0xFE, 0x2)
    Return()

    # Function_11_16E4 end

    def Function_12_1742(): pass

    label("Function_12_1742")

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
        "\x07\x00#40WTwo days later...\x02",
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

    def lambda_1846():
        OP_8E(0xFE, 0x2698, 0x7D0, 0x3B56, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1846)
    Sleep(100)

    def lambda_1866():
        OP_8E(0xFE, 0x2332, 0x7D0, 0x3746, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_1866)

    def lambda_1881():
        OP_6D(12680, 2250, 15980, 6000)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_1881)
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
            "#070F#5PThis place sure brings back memories.\x02\x03",

            "The atmosphere is so relaxing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x11,
        (
            "#792F#6PIt certainly is...\x02\x03",

            "#791FMaybe because it feels so similar to\x01",
            "our hometown.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x10,
        (
            "#075F#5P*sigh* Still, Ambassador Cochrane had me going\x01",
            "for a while.\x02\x03",

            "When I first heard about this whole trip, I thought\x01",
            "it was just gonna be the two of us out here.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x10, 400)
    Sleep(300)

    ChrTalk(    #38
        0x11,
        (
            "#791F#6POh, my... You look almost disappointed that it\x01",
            "isn't. \x02\x03",

            "#792FI'd be happy to take my leave if I'm getting in\x01",
            "the way of your dream date with her.\x02",
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
            "#072F#5PI'm good, thanks... She's not someone I've ever\x01",
            "seen as a potential partner.\x02\x03",

            "Besides, it's you she wants to talk to, not me.\x01",
            "This meeting might as well not be happening if\x01",
            "you're not here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x11,
        (
            "#794F#6PIt never takes much to put you on the\x01",
            "defensive, does it?\x02\x03",

            "Is it beyond you to just play along a little?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x10,
        (
            "#075F#5PGah...\x02\x03",

            "#072FYou just can't help but mess with people,\x01",
            "can you?\x02\x03",

            "With you in charge of the Zeiss guild,\x01",
            "I'm amazed it still has any bracers left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x11,
        (
            "#792F#6PCorrection: I can't help but mess with you.\x01",
            "I don't do this with anyone else.\x02\x03",

            "#791FWould you be happy if that were true?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #43
        0x10,
        "#075F#5P#3SHell no!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 17420, 2000, 8480, 315)
    Sleep(500)

    NpcTalk(    #44
        0x12,
        "Woman's Voice",
        "#1PAh, you've arrived.\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x10, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_1E73():
        OP_6D(11890, 2000, 14110, 2500)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_1E73)

    def lambda_1E8B():
        OP_67(0, 5090, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_1E8B)

    def lambda_1EA3():
        OP_6B(2410, 2500)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_1EA3)

    def lambda_1EB3():
        OP_6C(90000, 2500)
        ExitThread()

    QueueWorkItem(0x17, 3, lambda_1EB3)

    def lambda_1EC3():
        OP_6E(339, 2500)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_1EC3)
    OP_43(0x12, 0x0, 0x0, 0x4)
    Sleep(500)
    OP_8C(0x10, 135, 400)
    OP_8C(0x11, 135, 400)
    WaitChrThread(0x12, 0x0)
    WaitChrThread(0x17, 0x0)
    Sleep(500)

    ChrTalk(    #45
        0x12,
        "#1111F#11PI've been waiting for you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x10,
        "#070F#6PH-Hey, Ambassador.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x11,
        "#792F#6PThank you for inviting us here today.\x02",
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x12, 0x10, 400)

    ChrTalk(    #48
        0x12,
        (
            "#1112F#11PIs something the matter, Zin?\x02\x03",

            "You seem oddly flustered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x10,
        "#071F#6PMe? I-I'm just fine! You're imagining things!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x11,
        (
            "#792F#6PWho could blame him, Ambassador?\x02\x03",

            "#791FAfter all, he's a man on a hot springs trip with two\x01",
            "beautiful women. That's hardy a recipe for a calm\x01",
            "and composed mind, is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x10,
        "#072F#5PKnock it off, Kilika...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x12,
        (
            "#1113F#11PHaha... I suppose not.\x02\x03",

            "#1111FIf I were a little younger, I doubt I would\x01",
            "be able to keep my hands off him myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x10,
        "#073F#6PErk...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x12,
        (
            "#1110F#11PAll right, I suppose that's enough joking around.\x01",
            "We should get our dinner.\x02\x03",

            "Mrs. Mao is going to be making tonight's food\x01",
            "herself, by the sounds of it.\x02\x03",

            "The serious discussion can wait until after that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x10,
        "#075F#6PY-Yeah... That sounds fantastic.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x11,
        "#791F#6PLikewise.\x02",
    )

    CloseMessageWindow()
    OP_59()

    def lambda_22AB():
        OP_6B(2800, 3000)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_22AB)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_20(0xFA0)
    OP_21()
    Sleep(1000)
    OP_A2(0x2506)
    NewScene("ED6_DT21/T3223   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_12_1742 end

    def Function_13_22D8(): pass

    label("Function_13_22D8")

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

    def lambda_234A():
        OP_6D(27070, 2000, 5410, 3500)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_234A)

    def lambda_2362():
        OP_67(0, 7160, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_2362)

    def lambda_237A():
        OP_6B(2330, 3500)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_237A)

    def lambda_238A():
        OP_6E(341, 3500)
        ExitThread()

    QueueWorkItem(0x17, 3, lambda_238A)
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
            "#1113F#6PAhh... That was the best night's sleep I've\x01",
            "had in some time.\x02\x03",

            "#1110FI hope the two of you enjoyed your stay as\x01",
            "well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x10,
        "#071F#5PI know I did!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x11,
        (
            "#792F#11PI'm feeling very refreshed, thank you.\x02\x03",

            "#791FRefreshed enough to feel ready to take on\x01",
            "a new position in a new environment, even.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #60
        0x12,
        "#1111F#6PTh-Then...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x11,
        (
            "#791F#11PI would like to accept your offer.\x02\x03",

            "#792FHowever, I have one condition for doing so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x12,
        "#1112F#6POh? Name it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x11,
        (
            "#792F#11PWhile I am willing to join the president's new\x01",
            "agency, I am not willing to stop living in line\x01",
            "with my own beliefs.\x02\x03",

            "#790FAs such, if I should end up feeling the slightest\x01",
            "doubt about how the agency itself is being run...\x02\x03",

            "...I will do everything in my power to correct it\x01",
            "from the inside using any means at my disposal.\x02\x03",

            "If he still wants my membership after hearing as\x01",
            "much, please tell him that I accept his offer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x12,
        (
            "#1111F#6POh, that won't be a problem at all.\x02\x03",

            "#1113FI think he may well be encouraging you to take\x01",
            "the reins. I believe he chose you expecting you\x01",
            "to fulfill that role should it be deemed necessary.\x02\x03",

            "#1110FAfter all, you have experience in the guild, an\x01",
            "organization which has managed to remain neutral\x01",
            "and independent all this time. That's no mean feat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x11,
        (
            "#792F#11PHaha. I wouldn't be so sure about that.\x02\x03",

            "#790FAlso, I'll need to get things ready for my \x01",
            "successor, so I won't be able to return to\x01",
            "Calvard for two or three months.\x02\x03",

            "As such, I won't be able to start work till\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x12,
        (
            "#1113F#6PThat's perfectly understandable.\x02\x03",

            "#1111FWell...I look forward to meeting you again\x01",
            "in the Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x11,
        "#791F#11PLikewise.\x02",
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

    def lambda_2B18():
        OP_8E(0xFE, 0x2A8, 0x0, 0x38F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_2B18)
    Sleep(100)

    def lambda_2B38():
        OP_8E(0xFE, 0x1C2, 0x0, 0x3F0C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_2B38)

    def lambda_2B53():
        OP_6D(1860, 0, 16830, 4000)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_2B53)

    def lambda_2B6B():
        OP_67(0, 5370, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_2B6B)

    def lambda_2B83():
        OP_6B(2490, 4000)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_2B83)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x17, 0x0)

    ChrTalk(    #68 op#A
        0x10,
        "#074F#5P#12AHmm...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x10, 0xB4)
    Sleep(500)
    OP_8C(0x11, 0, 400)
    Sleep(300)

    ChrTalk(    #69
        0x11,
        "#791F#12PIs something on your mind?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10, 180, 400)
    Sleep(300)

    ChrTalk(    #70
        0x10,
        (
            "#070F#5POh, I was just thinking about what you said back\x01",
            "there.\x02\x03",

            "You said you'll need two or three months to get\x01",
            "everything ready for your successor, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x11,
        (
            "#790F#12PYes, I did...\x02\x03",

            "What of it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x10,
        (
            "#573F#5PWell, while I'm guessing it's pretty busy over in \x01",
            "Calvard right now, too, it doesn't sound as though\x01",
            "there's anything so urgent I need to be there NOW.\x02\x03",

            "#070FSo I was thinking maybe I could stay here for the\x01",
            "next few months while you get things sorted out\x01",
            "before I head back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x11,
        (
            "#792F#12PYou can't be serious...\x02\x03",

            "#790FThere's no reason why you should stay around\x01",
            "here in Liberl with me. Go back to Calvard.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2300, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #74
        0x10,
        (
            "#075F#5P*sigh* You don't have to be so cold.\x01",
            "It's me, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x11,
        (
            "#791F#12PHeehee. Well, it's the truth.\x02\x03",

            "We'll end up spending enough time together whether\x01",
            "we like it or not after I'm home. You don't need to go\x01",
            "out your way to make more now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x10,
        "#073F#5PWell...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 270, 400)
    Sleep(300)
    SetChrFlags(0x10, 0x2)
    SetChrChipByIndex(0x10, 9)
    SetChrSubChip(0x10, 0)

    def lambda_2FC3():
        OP_8E(0xFE, 0xFFFFF2EA, 0x0, 0x39D0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_2FC3)
    Sleep(500)

    ChrTalk(    #77 op#A
        0x10,
        (
            "#573F#5P#20W#15A...Heh. You win.\x02\x03",

            "#20W#25AThere's no need to rush things...\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x11, 0x0)
    Sleep(300)

    def lambda_303A():
        OP_6D(-220, 0, 16580, 1500)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_303A)
    OP_8C(0x11, 90, 400)
    WaitChrThread(0x17, 0x0)
    Sleep(300)

    ChrTalk(    #78
        0x11,
        (
            "#790F#6PZin?\x02\x03",

            "What are you standing there for?\x02",
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
        "#073F#5P...Oh!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x11, 400)
    Sleep(300)

    ChrTalk(    #80
        0x10,
        (
            "#075F#11PS-Sorry...\x02\x03",

            "#072FYou could say that BEFORE starting to walk off\x01",
            "on your own, though!\x02",
        )
    )

    CloseMessageWindow()
    OP_C4(0x1, 0x20000000)

    def lambda_314B():
        OP_6D(-2290, 0, 16590, 1000)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_314B)

    def lambda_3163():

        label("loc_3163")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_3163")

    QueueWorkItem2(0x11, 1, lambda_3163)
    SetChrChipByIndex(0x10, 3)

    def lambda_3179():
        OP_8E(0xFE, 0xFFFFF290, 0x0, 0x3EA8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_3179)
    WaitChrThread(0x10, 0x0)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)
    OP_8C(0x10, 180, 400)
    OP_44(0x11, 0x1)
    Sleep(500)
    OP_8C(0x11, 270, 400)

    def lambda_31BA():
        OP_8E(0xFE, 0xFFFFCA72, 0xFFFFF830, 0x3A02, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_31BA)
    Sleep(200)
    OP_8C(0x10, 270, 400)

    def lambda_31E1():
        OP_8E(0xFE, 0xFFFFCA68, 0xFFFFF830, 0x3F2A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_31E1)
    Sleep(1500)

    def lambda_3201():
        OP_6B(3000, 5000)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_3201)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x17, 0x2)
    OP_20(0xFA0)
    OP_21()
    Sleep(1000)
    OP_F7(0x9, 0x4, 0x0)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(350, 400, -1, -1)
    SetChrName("")

    AnonymousTalk(    #81
        "\x07\x00Side Story [Journey's End] finished!\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32F8")
    Sleep(1000)
    OP_28(0x9, 0x4, 0x10)
    OP_28(0x9, 0x4, 0x20)
    OP_3E(0x2D7, 1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #82
        "\x07\x05Received \x1F\xD7\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    AddMira(4000)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #83
        "\x07\x05Received \x07\x024,000 mira\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_32F8")

    OP_A2(0x2505)
    NewScene("ED6_DT21/M7102   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_13_22D8 end

    SaveToFile()

Try(main)
