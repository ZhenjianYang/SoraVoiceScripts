from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 洛连特

    CreateScenaFile(
        FileName            = 'C3101_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/C3101_1 ._SN',
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
        '',                                     # 9
        '',                                     # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
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


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_EF4",          # 01, 1
        "Function_2_1453",         # 02, 2
        "Function_3_1EEF",         # 03, 3
        "Function_4_26E6",         # 04, 4
        "Function_5_296F",         # 05, 5
        "Function_6_298F",         # 06, 6
        "Function_7_29D0",         # 07, 7
        "Function_8_2A11",         # 08, 8
        "Function_9_2A31",         # 09, 9
        "Function_10_2A83",        # 0A, 10
        "Function_11_2AD5",        # 0B, 11
        "Function_12_2AF4",        # 0C, 12
        "Function_13_2B13",        # 0D, 13
        "Function_14_2B2F",        # 0E, 14
        "Function_15_2B4B",        # 0F, 15
        "Function_16_2B67",        # 10, 16
        "Function_17_2B83",        # 11, 17
        "Function_18_2BAD",        # 12, 18
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x11, 14430, 0, 26280, 90)
    SetChrPos(0x12, 14430, 0, 24350, 90)
    SetChrPos(0x13, 14430, 0, 22420, 90)
    SetChrPos(0x14, 14430, 0, 20490, 90)
    SetChrPos(0x15, 14430, 0, 18560, 90)
    SetChrPos(0x16, 14430, 0, 16630, 90)
    SetChrPos(0x17, 17760, 0, 26280, 270)
    SetChrPos(0x18, 17760, 0, 24350, 270)
    SetChrPos(0x19, 17760, 0, 22420, 270)
    SetChrPos(0x1A, 17760, 0, 20490, 270)
    SetChrPos(0x1B, 17760, 0, 18560, 270)
    SetChrPos(0x1C, 17760, 0, 16630, 270)
    SetChrChipByIndex(0x11, 9)
    SetChrChipByIndex(0x12, 9)
    SetChrChipByIndex(0x13, 9)
    SetChrChipByIndex(0x14, 9)
    SetChrChipByIndex(0x15, 9)
    SetChrChipByIndex(0x16, 9)
    SetChrChipByIndex(0x17, 9)
    SetChrChipByIndex(0x18, 9)
    SetChrChipByIndex(0x19, 9)
    SetChrChipByIndex(0x1A, 9)
    SetChrChipByIndex(0x1B, 9)
    SetChrChipByIndex(0x1C, 9)
    SetChrPos(0x101, 300, 0, 23270, 90)
    SetChrPos(0xF7, -500, 0, 21820, 90)
    SetChrPos(0x104, -1800, 0, 23140, 90)
    SetChrPos(0x105, -2000, 0, 21900, 90)
    SetChrPos(0xD, -11810, 0, 24790, 90)
    SetChrPos(0xE, -11110, 0, 23590, 90)
    SetChrPos(0xF, -12010, 0, 22390, 90)
    SetChrPos(0x10, -11310, 0, 21190, 90)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x2B, 0x80)
    ClearChrFlags(0x2C, 0x80)
    ClearChrFlags(0x2D, 0x80)
    ClearChrFlags(0x2E, 0x80)
    ClearChrFlags(0x2F, 0x80)
    ClearChrFlags(0x30, 0x80)
    ClearChrFlags(0x31, 0x80)
    ClearChrFlags(0x32, 0x80)
    ClearChrFlags(0x33, 0x80)
    ClearChrFlags(0x34, 0x80)
    ClearChrFlags(0x35, 0x80)
    ClearChrFlags(0x36, 0x80)
    ClearChrFlags(0x37, 0x80)
    ClearChrFlags(0x38, 0x80)
    ClearChrFlags(0x39, 0x80)
    ClearChrFlags(0x3A, 0x80)
    ClearChrFlags(0x3B, 0x80)
    ClearChrFlags(0x3C, 0x80)
    ClearChrFlags(0x3D, 0x80)
    ClearChrFlags(0x3E, 0x80)
    ClearChrFlags(0x3F, 0x80)
    ClearChrFlags(0x40, 0x80)
    ClearChrFlags(0x41, 0x80)
    ClearChrFlags(0x42, 0x80)
    ClearChrFlags(0x43, 0x80)
    ClearChrFlags(0x44, 0x80)
    ClearChrFlags(0x45, 0x80)
    ClearChrFlags(0x46, 0x80)
    ClearChrFlags(0x47, 0x80)
    SetChrPos(0x46, -11000, 0, 28500, 90)
    SetChrPos(0x26, -12000, 0, 28000, 90)
    SetChrPos(0x27, -13000, 0, 28000, 90)
    SetChrPos(0x28, -14000, 0, 28000, 90)
    SetChrPos(0x29, -15000, 0, 28000, 90)
    SetChrPos(0x2A, -16000, 0, 28000, 90)
    SetChrPos(0x2B, -17000, 0, 28000, 90)
    SetChrPos(0x2C, -18000, 0, 28000, 90)
    SetChrPos(0x2D, -19000, 0, 28000, 90)
    SetChrPos(0x2E, -12000, 0, 29000, 90)
    SetChrPos(0x2F, -13000, 0, 29000, 90)
    SetChrPos(0x30, -14000, 0, 29000, 90)
    SetChrPos(0x31, -15000, 0, 29000, 90)
    SetChrPos(0x32, -16000, 0, 29000, 90)
    SetChrPos(0x33, -17000, 0, 29000, 90)
    SetChrPos(0x34, -18000, 0, 29000, 90)
    SetChrPos(0x35, -19000, 0, 29000, 90)
    SetChrPos(0x47, 0, 0, 28500, 90)
    SetChrPos(0x36, -8000, 0, 28000, 90)
    SetChrPos(0x37, -7000, 0, 28000, 90)
    SetChrPos(0x38, -6000, 0, 28000, 90)
    SetChrPos(0x39, -5000, 0, 28000, 90)
    SetChrPos(0x3A, -4000, 0, 28000, 90)
    SetChrPos(0x3B, -3000, 0, 28000, 90)
    SetChrPos(0x3C, -2000, 0, 28000, 90)
    SetChrPos(0x3D, -1000, 0, 28000, 90)
    SetChrPos(0x3E, -8000, 0, 29000, 90)
    SetChrPos(0x3F, -7000, 0, 29000, 90)
    SetChrPos(0x40, -6000, 0, 29000, 90)
    SetChrPos(0x41, -5000, 0, 29000, 90)
    SetChrPos(0x42, -4000, 0, 29000, 90)
    SetChrPos(0x43, -3000, 0, 29000, 90)
    SetChrPos(0x44, -2000, 0, 29000, 90)
    SetChrPos(0x45, -1000, 0, 29000, 90)
    OP_6D(23710, 0, 24140, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3830, 0)
    OP_6C(60000, 0)
    OP_6E(262, 0)
    OP_43(0x11, 0x1, 0x0, 0x4)
    OP_43(0x17, 0x1, 0x0, 0x4)
    Sleep(50)
    OP_43(0x12, 0x1, 0x0, 0x4)
    OP_43(0x18, 0x1, 0x0, 0x4)
    Sleep(50)
    OP_43(0x13, 0x1, 0x0, 0x4)
    OP_43(0x19, 0x1, 0x0, 0x4)
    Sleep(50)
    OP_43(0x14, 0x1, 0x0, 0x4)
    OP_43(0x1A, 0x1, 0x0, 0x4)
    Sleep(50)
    OP_43(0x15, 0x1, 0x0, 0x4)
    OP_43(0x1B, 0x1, 0x0, 0x4)
    Sleep(50)
    OP_43(0x16, 0x1, 0x0, 0x4)
    OP_43(0x1C, 0x1, 0x0, 0x4)
    OP_43(0x47, 0x1, 0x1, 0xA)
    OP_43(0x36, 0x1, 0x1, 0xC)
    OP_43(0x37, 0x1, 0x1, 0xC)
    OP_43(0x38, 0x1, 0x1, 0xC)
    OP_43(0x39, 0x1, 0x1, 0xC)
    OP_43(0x3A, 0x1, 0x1, 0xC)
    OP_43(0x3B, 0x1, 0x1, 0xC)
    OP_43(0x3C, 0x1, 0x1, 0xC)
    OP_43(0x3D, 0x1, 0x1, 0xC)
    OP_43(0x3E, 0x1, 0x1, 0xC)
    OP_43(0x3F, 0x1, 0x1, 0xC)
    OP_43(0x40, 0x1, 0x1, 0xC)
    OP_43(0x41, 0x1, 0x1, 0xC)
    OP_43(0x42, 0x1, 0x1, 0xC)
    OP_43(0x43, 0x1, 0x1, 0xC)
    OP_43(0x44, 0x1, 0x1, 0xC)
    OP_43(0x45, 0x1, 0x1, 0xC)
    Sleep(1000)
    OP_43(0x46, 0x1, 0x1, 0x9)
    OP_43(0x26, 0x1, 0x1, 0xB)
    OP_43(0x27, 0x1, 0x1, 0xB)
    OP_43(0x28, 0x1, 0x1, 0xB)
    OP_43(0x29, 0x1, 0x1, 0xB)
    OP_43(0x2A, 0x1, 0x1, 0xB)
    OP_43(0x2B, 0x1, 0x1, 0xB)
    OP_43(0x2C, 0x1, 0x1, 0xB)
    OP_43(0x2D, 0x1, 0x1, 0xB)
    OP_43(0x2E, 0x1, 0x1, 0xB)
    OP_43(0x2F, 0x1, 0x1, 0xB)
    OP_43(0x30, 0x1, 0x1, 0xB)
    OP_43(0x31, 0x1, 0x1, 0xB)
    OP_43(0x32, 0x1, 0x1, 0xB)
    OP_43(0x33, 0x1, 0x1, 0xB)
    OP_43(0x34, 0x1, 0x1, 0xB)
    OP_43(0x35, 0x1, 0x1, 0xB)
    FadeToBright(1000, 0)

    def lambda_71A():
        OP_6D(-5110, 0, 27310, 8000)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_71A)

    def lambda_732():
        OP_6B(3700, 8000)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_732)

    def lambda_742():
        OP_6C(30000, 8000)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_742)
    Sleep(2000)

    def lambda_757():
        OP_8E(0x101, 0x251C, 0x0, 0x5AE6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_757)

    def lambda_772():
        OP_8E(0xF7, 0x2260, 0x0, 0x553C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_772)

    def lambda_78D():
        OP_8E(0x104, 0x1E78, 0x0, 0x5A64, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_78D)

    def lambda_7A8():
        OP_8E(0x105, 0x1CE8, 0x0, 0x558C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7A8)
    Sleep(5000)
    OP_0D()
    Fade(1000)
    OP_44(0xB, 0x0)
    OP_44(0xB, 0x1)
    OP_44(0xB, 0x2)
    OP_6D(9500, 0, 23270, 0)
    OP_67(0, 4840, -10000, 0)
    OP_6B(3540, 0)
    OP_6C(55000, 0)
    OP_6E(262, 0)
    OP_0D()
    WaitChrThread(0x0, 0x1)
    WaitChrThread(0x1, 0x1)
    WaitChrThread(0x2, 0x1)
    WaitChrThread(0x3, 0x1)

    ChrTalk(    #0
        0x101,
        "#1016F啊～感觉好怀念啊。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_87E")
    OP_61(0x106)

    ChrTalk(    #1
        0x106,
        "#051F嗯，自从那次之后就再也没有过。\x02",
    )

    CloseMessageWindow()

    label("loc_87E")

    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #2
        0x101,
        (
            "#1015F上次来的时候因为天色暗\x01",
            "看不太清楚……\x02\x03",

            "#1011F现在这么一看，\x01",
            "这个基地还真是很大呢～\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_926")
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #3
        0x103,
        (
            "#020F真的呢……\x01",
            "和要塞这个称呼是很相称。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_926")

    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #4
        0x105,
        (
            "#040F嗯，因为这里是\x01",
            "王国军的大本营。\x02\x03",

            "所以与各地的要塞关所\x01",
            "在规模上稍有差别。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x104, 270, 400)
    OP_62(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0x104)

    ChrTalk(    #5
        0x104,
        (
            "#030F哎哟，看来快要\x01",
            "开始了嘛。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0xD, 30)
    SetChrChipByIndex(0xE, 30)
    SetChrChipByIndex(0xF, 30)
    SetChrChipByIndex(0x10, 30)

    def lambda_9F3():
        OP_8C(0xF7, 270, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_9F3)
    Sleep(250)

    def lambda_A06():
        OP_8C(0x101, 270, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A06)
    Sleep(150)

    def lambda_A19():
        OP_8C(0x105, 270, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A19)

    def lambda_A27():
        OP_8E(0xD, 0xFFFFF286, 0x0, 0x60D6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_A27)

    def lambda_A42():
        OP_8E(0xE, 0xFFFFF286, 0x0, 0x5C26, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_A42)

    def lambda_A5D():
        OP_8E(0xF, 0xFFFFF286, 0x0, 0x5776, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_A5D)

    def lambda_A78():
        OP_8E(0x10, 0xFFFFF286, 0x0, 0x52C6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_A78)

    def lambda_A93():
        OP_6D(0, 0, 24840, 3000)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_A93)

    def lambda_AAB():
        OP_67(0, 8119, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_AAB)

    def lambda_AC3():
        OP_6C(0, 3000)
        ExitThread()

    QueueWorkItem(0x25, 3, lambda_AC3)

    def lambda_AD3():
        OP_6B(2970, 3000)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_AD3)
    WaitChrThread(0x25, 0x1)
    WaitChrThread(0x25, 0x2)
    WaitChrThread(0x25, 0x3)
    WaitChrThread(0xB, 0x1)
    Sleep(1500)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 0, 0, 32750, 180)
    SetChrPos(0x101, 8500, 0, 23000, 270)
    SetChrPos(0xF7, 9500, 0, 24250, 270)
    SetChrPos(0x104, 9500, 0, 21750, 270)
    SetChrPos(0x105, 10500, 0, 23000, 270)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)

    def lambda_B92():
        OP_94(0x1, 0x0, 0x0, 0x15E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_B92)
    Sleep(50)

    def lambda_BAD():
        OP_94(0x1, 0x1, 0x0, 0x15E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_BAD)
    Sleep(100)

    def lambda_BC8():
        OP_94(0x1, 0x2, 0x0, 0x15E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_BC8)
    Sleep(50)

    def lambda_BE3():
        OP_94(0x1, 0x3, 0x0, 0x15E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_BE3)
    OP_8E(0xB, 0x0, 0x0, 0x661C, 0x7D0, 0x0)
    WaitChrThread(0x0, 0x1)
    WaitChrThread(0x1, 0x1)
    WaitChrThread(0x2, 0x1)
    WaitChrThread(0x3, 0x1)
    Sleep(400)

    ChrTalk(    #6
        0xB,
        (
            "#700F那么现在开始\x01",
            "进行模拟战斗。\x02\x03",

            "这次特别邀请到游击士协会的\x01",
            "精锐来担任对抗部队。\x02\x03",

            "希望各位官兵能尽全力挑战。\x01",
            "其中可是包含了武术大赛冠军的强手。\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0xD, 0x0, 0x1, 0x5)
    OP_43(0xE, 0x0, 0x1, 0x6)
    OP_43(0xF, 0x0, 0x1, 0x7)
    OP_43(0x10, 0x0, 0x1, 0x8)

    ChrTalk(    #7
        0xD,
        "#2P冠、冠军……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xF,
        "#3P这、这可难对付了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 400)

    ChrTalk(    #9
        0xB,
        (
            "#700F和刚才说明过的一样，\x01",
            "预计需要诸位进行二连战。\x02\x03",

            "请牢记这一点\x01",
            "来进行战斗。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xB, 400)

    ChrTalk(    #10
        0x101,
        "#1006F#3P嗯，明白了！\x02",
    )

    CloseMessageWindow()
    OP_44(0xD, 0x0)
    OP_44(0xE, 0x0)
    OP_44(0xF, 0x0)
    OP_44(0x10, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_DC8")

    ChrTalk(    #11
        0x106,
        (
            "#050F#2P几连战都没关系。\x02\x03",

            "赶快开始吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E02")

    label("loc_DC8")


    ChrTalk(    #12
        0x103,
        (
            "#525F#2P呵呵，几连战都没关系哦㈱\x02\x03",

            "我们会奉陪到底的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E02")

    OP_8C(0xB, 180, 400)

    ChrTalk(    #13
        0xB,
        (
            "#700F#5P好，那就开始吧。\x02\x03",

            "──双方预备！\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0xD, 0x1, 0x1, 0xD)
    OP_43(0xE, 0x1, 0x1, 0xE)
    OP_43(0xF, 0x1, 0x1, 0xF)
    OP_43(0x10, 0x1, 0x1, 0x10)
    OP_8C(0x101, 270, 400)
    WaitChrThread(0xD, 0x1)
    WaitChrThread(0xE, 0x1)
    WaitChrThread(0xF, 0x1)
    WaitChrThread(0x10, 0x1)
    Fade(1000)
    SetChrChipByIndex(0x104, 15)
    SetChrChipByIndex(0x101, 11)
    SetChrChipByIndex(0x105, 17)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_E91")
    SetChrChipByIndex(0xF7, 19)
    Jump("loc_E96")

    label("loc_E91")

    SetChrChipByIndex(0xF7, 13)

    label("loc_E96")

    SetChrChipByIndex(0xD, 21)
    SetChrChipByIndex(0xE, 21)
    SetChrChipByIndex(0xF, 21)
    SetChrChipByIndex(0x10, 21)
    OP_0D()

    ChrTalk(    #14
        0xB,
        "#704F#5P#3S比赛开始！\x02",
    )

    CloseMessageWindow()
    Battle(0xC80, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_EE3"),
        (1, "loc_EEA"),
        (SWITCH_DEFAULT, "loc_EF1"),
    )


    label("loc_EE3")

    Call(1, 1)
    Jump("loc_EF1")

    label("loc_EEA")

    Call(1, 4)
    Jump("loc_EF1")

    label("loc_EF1")

    EventEnd(0x0)
    Return()

    # Function_0_AA end

    def Function_1_EF4(): pass

    label("Function_1_EF4")

    EventBegin(0x0)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    OP_6D(0, 0, 24840, 0)
    OP_67(0, 8119, -10000, 0)
    OP_6C(0, 0)
    OP_6B(2970, 0)
    OP_6E(262, 0)
    SetChrChipByIndex(0x104, 15)
    SetChrChipByIndex(0x101, 11)
    SetChrChipByIndex(0x105, 17)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_F6A")
    SetChrChipByIndex(0xF7, 19)
    Jump("loc_F6F")

    label("loc_F6A")

    SetChrChipByIndex(0xF7, 13)

    label("loc_F6F")

    SetChrPos(0x101, 2900, 0, 23000, 270)
    SetChrPos(0xF7, 3900, 0, 24250, 270)
    SetChrPos(0x104, 3900, 0, 21750, 270)
    SetChrPos(0x105, 4900, 0, 23000, 270)
    SetChrPos(0xD, -3900, 0, 24250, 90)
    SetChrPos(0xE, -2900, 0, 23000, 90)
    SetChrPos(0xF, -4900, 0, 23000, 90)
    SetChrPos(0x10, -3900, 0, 21750, 90)
    SetChrChipByIndex(0xD, 22)
    SetChrChipByIndex(0xE, 22)
    SetChrChipByIndex(0xF, 22)
    SetChrChipByIndex(0x10, 22)
    SetChrSubChip(0xD, 3)
    SetChrSubChip(0xE, 3)
    SetChrSubChip(0xF, 3)
    SetChrSubChip(0x10, 3)
    SetChrPos(0xB, 0, 0, 26140, 180)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #15
        0xB,
        "#700F──到此为止！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        "#1006F#3P好，赢了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_108C")

    ChrTalk(    #17
        0x106,
        "#051F#2P果然没问题。\x02",
    )

    CloseMessageWindow()
    Jump("loc_10A6")

    label("loc_108C")


    ChrTalk(    #18
        0x103,
        "#027F#2P果然没问题。\x02",
    )

    CloseMessageWindow()

    label("loc_10A6")


    ChrTalk(    #19
        0x105,
        "#040F……是啊。\x02",
    )

    CloseMessageWindow()
    OP_62(0xE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)
    OP_99(0xE, 0x3, 0x0, 0x7D0)

    ChrTalk(    #20
        0xE,
        "#4P啊，好痛……\x02",
    )

    CloseMessageWindow()

    def lambda_10F6():

        label("loc_10F6")

        TurnDirection(0xB, 0xE, 400)
        OP_48()
        Jump("loc_10F6")

    QueueWorkItem2(0xB, 1, lambda_10F6)

    ChrTalk(    #21
        0xB,
        (
            "#700F你们在发什么呆？\x02\x03",

            "立即撤离。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xE,
        "#4P是、是！\x02",
    )

    CloseMessageWindow()
    OP_43(0xD, 0x1, 0x1, 0x11)
    Sleep(100)
    OP_43(0xF, 0x1, 0x1, 0x11)
    Sleep(50)
    OP_43(0x10, 0x1, 0x1, 0x11)
    OP_8C(0xE, 270, 0)
    SetChrChipByIndex(0xE, 10)

    def lambda_116A():
        OP_94(0x1, 0xFE, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_116A)
    WaitChrThread(0x10, 0x1)
    WaitChrThread(0xE, 0x1)
    SetChrFlags(0xE, 0x80)
    OP_44(0xB, 0x1)

    ChrTalk(    #23
        0xB,
        "#704F──接下来，贝尔克副队长。\x02",
    )

    CloseMessageWindow()

    def lambda_11B8():

        label("loc_11B8")

        TurnDirection(0xB, 0x25, 0)
        OP_48()
        Jump("loc_11B8")

    QueueWorkItem2(0xB, 1, lambda_11B8)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x25, 31)
    SetChrPos(0xD, -10000, 0, 23000, 90)
    SetChrPos(0x25, -12000, 0, 23000, 90)
    SetChrPos(0xF, -11110, 0, 24250, 90)
    SetChrPos(0x10, -11110, 0, 21750, 90)

    ChrTalk(    #24
        0x25,
        "#2P在！\x02",
    )

    CloseMessageWindow()

    def lambda_1233():
        OP_94(0x1, 0xD, 0x0, 0x1BBC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1233)

    def lambda_1249():
        OP_94(0x1, 0x25, 0x0, 0x1BBC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_1249)

    def lambda_125F():
        OP_94(0x1, 0xF, 0x0, 0x1BBC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_125F)

    def lambda_1275():
        OP_94(0x1, 0x10, 0x0, 0x1BBC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1275)
    WaitChrThread(0x25, 0x1)
    SetChrChipByIndex(0x25, 23)
    SetChrChipByIndex(0xD, 21)
    SetChrChipByIndex(0xF, 21)
    SetChrChipByIndex(0x10, 21)
    Sleep(1000)
    OP_44(0xB, 0x1)
    OP_8C(0xB, 180, 400)

    ChrTalk(    #25
        0x101,
        (
            "#1007F#3P看、看来真的\x01",
            "不打算让我们休息了 。\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x104, 0x1, 0x1, 0x12)

    ChrTalk(    #26
        0x104,
        (
            "#035F#3P呼，真是服了。\x02\x03",

            "至少让我整理一下\x01",
            "乱了的头发也好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x25,
        "#4P嗯，不愧是大赛冠军……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x25,
        (
            "#4P故意露出破绽，\x01",
            "打算是想让我们掉以轻心吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #29
        0x101,
        (
            "#1019F#3P不……你错了……\x02\x03",

            "这、这绝对是你\x01",
            "想得太多了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xB,
        (
            "#700F#5P现在还在训练中啊。\x01",
            "不要窃窃私语。\x02\x03",

            "那么第２战──\x02\x03",

            "#704F#3S──比赛开始！\x02",
        )
    )

    CloseMessageWindow()
    Battle(0xC81, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1442"),
        (1, "loc_1449"),
        (SWITCH_DEFAULT, "loc_1450"),
    )


    label("loc_1442")

    Call(1, 2)
    Jump("loc_1450")

    label("loc_1449")

    Call(1, 4)
    Jump("loc_1450")

    label("loc_1450")

    EventEnd(0x0)
    Return()

    # Function_1_EF4 end

    def Function_2_1453(): pass

    label("Function_2_1453")

    EventBegin(0x0)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    OP_6D(0, 0, 24840, 0)
    OP_67(0, 8119, -10000, 0)
    OP_6C(0, 0)
    OP_6B(2970, 0)
    OP_6E(262, 0)
    SetChrChipByIndex(0x104, 15)
    SetChrChipByIndex(0x101, 11)
    SetChrChipByIndex(0x105, 17)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_14CE")
    SetChrChipByIndex(0xF7, 19)
    Jump("loc_14D3")

    label("loc_14CE")

    SetChrChipByIndex(0xF7, 13)

    label("loc_14D3")

    SetChrPos(0x101, 2900, 0, 23000, 270)
    SetChrPos(0xF7, 3900, 0, 24250, 270)
    SetChrPos(0x104, 3900, 0, 21750, 270)
    SetChrPos(0x105, 4900, 0, 23000, 270)
    SetChrPos(0xD, -3900, 0, 24250, 90)
    SetChrPos(0xF, -2900, 0, 23000, 90)
    SetChrPos(0x25, -4900, 0, 23000, 90)
    SetChrPos(0x10, -3900, 0, 21750, 90)
    SetChrPos(0xB, 0, 0, 26140, 180)
    SetChrChipByIndex(0xD, 22)
    SetChrChipByIndex(0x25, 24)
    SetChrChipByIndex(0xF, 22)
    SetChrChipByIndex(0x10, 22)
    SetChrSubChip(0xD, 3)
    SetChrSubChip(0x25, 3)
    SetChrSubChip(0xF, 3)
    SetChrSubChip(0x10, 3)
    Sleep(1000)

    ChrTalk(    #31
        0xB,
        "#704F#5P──到此为止！\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0xF7, 65535)
    SetChrChipByIndex(0x105, 65535)
    SetChrChipByIndex(0x104, 65535)
    OP_0D()

    ChrTalk(    #32
        0x104,
        "#030F#3P呼，我们赢了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        "#1002F#3P嗯，好不容易。\x02",
    )

    CloseMessageWindow()
    OP_99(0x25, 0x3, 0x0, 0x7D0)

    ChrTalk(    #34
        0x25,
        "#4P唔……输了……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x25, 400)

    ChrTalk(    #35
        0xB,
        (
            "#700F……………………\x02\x03",

            "副队长……\x01",
            "还挺得住吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x25, 0xB, 400)

    ChrTalk(    #36
        0x25,
        "#4P……………！？\x02",
    )

    CloseMessageWindow()
    OP_62(0x25, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #37
        0x25,
        "#4P是、是的！　没有问题。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xB,
        (
            "#703F很好……\x01",
            "那么马上做准备。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x25,
        "#4P了解！\x02",
    )

    CloseMessageWindow()
    OP_43(0xD, 0x1, 0x1, 0x11)
    Sleep(100)
    OP_43(0xF, 0x1, 0x1, 0x11)
    Sleep(50)
    OP_43(0x10, 0x1, 0x1, 0x11)
    OP_8C(0x25, 270, 0)
    SetChrChipByIndex(0x25, 31)

    def lambda_171C():
        OP_94(0x1, 0xFE, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_171C)
    Sleep(1000)

    def lambda_1737():
        OP_8C(0x101, 315, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1737)

    def lambda_1745():
        OP_8C(0xF7, 315, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_1745)

    def lambda_1753():
        OP_8C(0x104, 315, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1753)

    def lambda_1761():
        OP_8C(0x105, 315, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1761)
    OP_66(0x0)
    OP_6D(2400, 0, 24430, 2000)

    ChrTalk(    #40
        0x101,
        "#1015F#3P请问，所谓的准备是指……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x104,
        (
            "#030F#3P呵呵，让我猜猜看。\x02\x03",

            "是不是被我华丽的战斗所感动，\x01",
            "而要为我开设庆功宴呢？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 400)

    ChrTalk(    #42
        0xB,
        "#702F#1P庆功宴……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        "#1002F#3P……请你不要理他。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xB,
        (
            "#703F#1P了、了解……\x02\x03",

            "#700F不，准备当然指的是\x01",
            "下一场模拟战斗的准备了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #45
        0x101,
        (
            "#1004F#3P不、不是吧！？\x02\x03",

            "你一开始不是说\x01",
            "『二连战』吗！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_19DF")

    ChrTalk(    #46
        0xB,
        (
            "#700F#1P嗯， 确实这么说过──\x02\x03",

            "不过，你们是这样回答的：\x01",
            "『几连战都没关系』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x106,
        (
            "#552F#2P切……\x01",
            "居然被你记牢了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(    #48
        0x101,
        (
            "#1009F#3P阿、阿加特～～\x01",
            "为什么这么多嘴！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x106,
        (
            "#551F#1P嗯，别介意。\x01",
            "只是一时脱口而出罢了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AC7")

    label("loc_19DF")


    ChrTalk(    #50
        0xB,
        (
            "#700F#1P嗯， 确实这么说过──\x02\x03",

            "不过，你们是这样回答的：\x01",
            "『几连战都没关系』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x103,
        "#023F#2P哎呀，你记得真牢。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #52
        0x101,
        "#1007F#3P雪、雪拉姐～～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x103,
        (
            "#025F#2P看、看来是没办法了。\x01",
            "谁让当时脱口而出说了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AC7")


    ChrTalk(    #54
        0xB,
        (
            "#700F#1P那就满足你们的要求，\x01",
            "再较量一场吧。\x02\x03",

            "就由我亲自来担任──\x01",
            "你们最后的一个对手吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xB, 400)

    ChrTalk(    #55
        0x101,
        "#1004F#3P希、希德中校！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x104,
        (
            "#031F#3P呵呵，总算\x01",
            "露出你真正的想法了吧。\x02\x03",

            "是不是手痒了，迫不及待地要较量一番啊──\x01",
            "有话就直说嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xB,
        "#701F#1P哈哈，被你看穿了啊。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1C1B")

    ChrTalk(    #58
        0x106,
        (
            "#051F#2P哼，果不其然……\x02\x03",

            "正好，我也正想和你比试一下。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C62")

    label("loc_1C1B")


    ChrTalk(    #59
        0x103,
        (
            "#027F#2P呵呵，果然如此……\x02\x03",

            "#525F不过，我并不讨厌你的这种想法哦㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C62")

    WaitChrThread(0x10, 0x1)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x25, 31)
    SetChrChipByIndex(0xF, 10)
    SetChrChipByIndex(0x10, 10)
    SetChrPos(0x25, -10000, 0, 23000, 90)
    SetChrPos(0xF, -9110, 0, 24250, 90)
    SetChrPos(0x10, -9110, 0, 21750, 90)

    def lambda_1CC3():
        OP_6D(0, 0, 24840, 2000)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1CC3)

    def lambda_1CDB():
        OP_94(0x1, 0x25, 0x0, 0x13EC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_1CDB)

    def lambda_1CF1():
        OP_94(0x1, 0xF, 0x0, 0x13EC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1CF1)

    def lambda_1D07():
        OP_94(0x1, 0x10, 0x0, 0x13EC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1D07)
    WaitChrThread(0x25, 0x1)
    WaitChrThread(0xB, 0x1)
    OP_66(0x1)
    SetChrChipByIndex(0x25, 23)
    SetChrChipByIndex(0xF, 21)
    SetChrChipByIndex(0x10, 21)

    ChrTalk(    #60
        0x25,
        "#4P让您久等了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x25, 400)

    ChrTalk(    #61
        0xB,
        "#700F辛苦你了────\x02",
    )

    CloseMessageWindow()

    def lambda_1D70():
        OP_67(0, 19910, -29700, 2000)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_1D70)

    def lambda_1D88():
        OP_6B(1000, 2000)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_1D88)

    def lambda_1D98():

        label("loc_1D98")

        TurnDirection(0x101, 0xB, 0)
        OP_48()
        Jump("loc_1D98")

    QueueWorkItem2(0x101, 1, lambda_1D98)

    def lambda_1DA9():

        label("loc_1DA9")

        TurnDirection(0xF7, 0xB, 0)
        OP_48()
        Jump("loc_1DA9")

    QueueWorkItem2(0xF7, 1, lambda_1DA9)

    def lambda_1DBA():

        label("loc_1DBA")

        TurnDirection(0xF8, 0xB, 0)
        OP_48()
        Jump("loc_1DBA")

    QueueWorkItem2(0xF8, 1, lambda_1DBA)

    def lambda_1DCB():

        label("loc_1DCB")

        TurnDirection(0xF9, 0xB, 0)
        OP_48()
        Jump("loc_1DCB")

    QueueWorkItem2(0xF9, 1, lambda_1DCB)
    OP_8E(0xB, 0xFFFFF4AC, 0x0, 0x59D8, 0x7D0, 0x0)
    OP_8C(0xB, 90, 400)
    OP_44(0x101, 0x1)
    OP_44(0xF7, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    WaitChrThread(0x25, 0x1)
    WaitChrThread(0x25, 0x2)
    Fade(1000)
    SetChrChipByIndex(0xB, 32)
    SetChrChipByIndex(0x104, 15)
    SetChrChipByIndex(0x101, 11)
    SetChrChipByIndex(0x105, 17)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1E33")
    SetChrChipByIndex(0xF7, 19)
    Jump("loc_1E38")

    label("loc_1E33")

    SetChrChipByIndex(0xF7, 13)

    label("loc_1E38")

    OP_0D()

    ChrTalk(    #62
        0xB,
        (
            "#700F#2P那么就开始吧。\x02\x03",

            "──准备好了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1E91")

    ChrTalk(    #63
        0x106,
        "#057F#1P嗯，随时可以开始。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1EB1")

    label("loc_1E91")


    ChrTalk(    #64
        0x103,
        "#022F#1P嗯，随时可以开始。\x02",
    )

    CloseMessageWindow()

    label("loc_1EB1")


    ChrTalk(    #65
        0xB,
        "#704F#2P好，那就接招吧！\x02",
    )

    CloseMessageWindow()
    Battle(0xC82, 0x0, 0x0, 0x0, 0xFF)
    OP_28(0x6D, 0x1, 0x4)
    OP_28(0x6D, 0x1, 0x10)
    Call(1, 3)
    EventEnd(0x0)
    Return()

    # Function_2_1453 end

    def Function_3_1EEF(): pass

    label("Function_3_1EEF")

    EventBegin(0x0)
    OP_6D(0, 0, 24840, 0)
    OP_67(0, 19910, -29700, 0)
    OP_6B(1000, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 2900, 0, 23000, 270)
    SetChrPos(0xF7, 3900, 0, 24250, 270)
    SetChrPos(0x104, 3900, 0, 21750, 270)
    SetChrPos(0x105, 4900, 0, 23000, 270)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1F82"),
        (1, "loc_2133"),
        (SWITCH_DEFAULT, "loc_22FB"),
    )


    label("loc_1F82")

    OP_28(0x6D, 0x1, 0x20)
    SetChrChipByIndex(0xB, 33)
    SetChrChipByIndex(0x25, 24)
    SetChrChipByIndex(0xF, 22)
    SetChrChipByIndex(0x10, 22)
    SetChrSubChip(0xB, 3)
    SetChrSubChip(0x25, 3)
    SetChrSubChip(0xF, 3)
    SetChrSubChip(0x10, 3)
    Sleep(1000)

    ChrTalk(    #66
        0x101,
        (
            "#1021F#3P总、总算是\x01",
            "赢了啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x105,
        "#042F#3P嗯、嗯……好不容易。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_203F")

    ChrTalk(    #68
        0x106,
        (
            "#551F#2P呼，不好对付。\x02\x03",

            "想不到会被压制到如此程度……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2077")

    label("loc_203F")


    ChrTalk(    #69
        0x103,
        (
            "#025F#2P啊，好危险。\x02\x03",

            "想不到会被压制到如此程度……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2077")


    ChrTalk(    #70
        0xB,
        "#703F#1P了不起……我输得心服口服。\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_99(0xB, 0x3, 0x0, 0x7D0)
    Fade(1000)
    SetChrChipByIndex(0xB, 3)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0xF7, 65535)
    SetChrChipByIndex(0x105, 65535)
    SetChrChipByIndex(0x104, 65535)
    OP_0D()

    ChrTalk(    #71
        0xB,
        (
            "#701F#1P连战之后还能\x01",
            "做到这样，真是名不虚传。\x02\x03",

            "对士兵们来说\x01",
            "你们为我们提供了最佳的榜样。\x02",
        )
    )

    CloseMessageWindow()
    OP_2B(0x6D, 0x2)
    OP_2C(0x6D, 0x5DC)
    Jump("loc_22FB")

    label("loc_2133")

    OP_28(0x6D, 0x1, 0x40)
    SetChrChipByIndex(0x104, 16)
    SetChrChipByIndex(0x101, 12)
    SetChrChipByIndex(0x105, 18)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2157")
    SetChrChipByIndex(0xF7, 20)
    Jump("loc_215C")

    label("loc_2157")

    SetChrChipByIndex(0xF7, 14)

    label("loc_215C")

    SetChrSubChip(0x104, 3)
    SetChrSubChip(0x101, 3)
    SetChrSubChip(0x105, 3)
    SetChrSubChip(0xF7, 3)
    Sleep(1000)

    ChrTalk(    #72
        0x101,
        (
            "#1021F#3P啊，好痛……\x02\x03",

            "……输、输了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x105,
        "#541F嗯，很遗憾……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_21FD")

    ChrTalk(    #74
        0x106,
        (
            "#056F#2P可恶，真丢人。\x02\x03",

            "想不到会被压制到如此程度……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2235")

    label("loc_21FD")


    ChrTalk(    #75
        0x103,
        (
            "#025F#2P啊，失败了。\x02\x03",

            "想不到会被压制到如此程度……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2235")


    ChrTalk(    #76
        0x104,
        "#035F#3P呼，输得心服口服。\x02",
    )

    CloseMessageWindow()
    Fade(1000)
    SetChrChipByIndex(0xB, 3)
    SetChrChipByIndex(0x25, 8)
    SetChrChipByIndex(0x10, 5)
    SetChrChipByIndex(0xF, 5)
    OP_0D()

    ChrTalk(    #77
        0xB,
        (
            "#701F#1P不，连战之后还能做到\x01",
            "这种程度是很了不起的。\x02\x03",

            "已经足够成为士兵们的\x01",
            "好榜样了。\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    SetChrChipByIndex(0xF7, 65535)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x105, 65535)
    SetChrChipByIndex(0x104, 65535)
    SetChrSubChip(0xF7, 0)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x104, 0)
    SetChrSubChip(0x105, 0)
    OP_0D()
    Jump("loc_22FB")

    label("loc_22FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_234D")

    ChrTalk(    #78
        0x106,
        (
            "#053F#2P这是我们应该说的才对。\x02\x03",

            "虽然不甘心，可还是学到了不少东西。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2395")

    label("loc_234D")


    ChrTalk(    #79
        0x103,
        (
            "#020F#2P这是我们应该说的才对。\x02\x03",

            "虽然不甘心，可还是学到了不少东西。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2395")


    ChrTalk(    #80
        0x101,
        (
            "#1015F#3P嗯，还是第一次被魔法\x01",
            "折磨到这种程度。\x02\x03",

            "#1006F让我也想重新\x01",
            "检视一下自己的导力器了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xB,
        (
            "#701F#1P如果你们能这么想，\x01",
            "那这场战斗就更有意义了。\x02\x03",

            "问题并非是用什么，\x01",
            "而在于怎样用。\x02\x03",

            "无论是魔法还是战技，\x01",
            "我觉得在这方面都是一样的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x104,
        "#031F原来如此，实在是真知灼见啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xB,
        (
            "#701F#1P我们王国军也要继续钻研，\x01",
            "不甘落后于诸位游击士们。\x02\x03",

            "为了王国的和平，今后也希望大家能和我们一起\x01",
            "继续互相切磋下去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x101,
        (
            "#1006F#3P嗯，我们也会努力进步的。\x02\x03",

            "#1001F有机会的话\x01",
            "再比试吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_259A")

    ChrTalk(    #85
        0x106,
        "#051F#2P是啊，请你们务必指教。\x02",
    )

    CloseMessageWindow()
    Jump("loc_25BE")

    label("loc_259A")


    ChrTalk(    #86
        0x103,
        "#020F#2P是啊，请你们务必指教。\x02",
    )

    CloseMessageWindow()

    label("loc_25BE")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_25CE"),
        (1, "loc_260C"),
        (SWITCH_DEFAULT, "loc_262B"),
    )


    label("loc_25CE")


    ChrTalk(    #87
        0xB,
        (
            "#701F#1P嗯，一言为定。\x02\x03",

            "老是输的话\x01",
            "我晚上会睡不好的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_262B")

    label("loc_260C")


    ChrTalk(    #88
        0xB,
        "#701F#1P嗯，一言为定。\x02",
    )

    CloseMessageWindow()
    Jump("loc_262B")

    label("loc_262B")

    OP_8C(0xB, 45, 400)

    ChrTalk(    #89
        0xB,
        (
            "#704F#1P──现在宣布训练结束。\x02\x03",

            "各位官兵辛苦了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x17, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #90
        "\x07\x02任务【特别训练参加邀请】\x07\x00完成了！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_31(0x0, 0xFE, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_26CA")
    OP_31(0x5, 0xFE, 0x0)
    Jump("loc_26CF")

    label("loc_26CA")

    OP_31(0x2, 0xFE, 0x0)

    label("loc_26CF")

    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/C3100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_1EEF end

    def Function_4_26E6(): pass

    label("Function_4_26E6")

    EventBegin(0x0)
    OP_6D(0, 0, 24840, 0)
    OP_67(0, 8119, -10000, 0)
    OP_6C(0, 0)
    OP_6B(2970, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 2900, 0, 23000, 270)
    SetChrPos(0xF7, 3900, 0, 24250, 270)
    SetChrPos(0x104, 3900, 0, 21750, 270)
    SetChrPos(0x105, 4900, 0, 23000, 270)
    SetChrChipByIndex(0x104, 16)
    SetChrChipByIndex(0x101, 12)
    SetChrChipByIndex(0x105, 18)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2787")
    SetChrChipByIndex(0xF7, 20)
    Jump("loc_278C")

    label("loc_2787")

    SetChrChipByIndex(0xF7, 14)

    label("loc_278C")

    SetChrSubChip(0x104, 3)
    SetChrSubChip(0x101, 3)
    SetChrSubChip(0x105, 3)
    SetChrSubChip(0xF7, 3)
    Sleep(1000)

    ChrTalk(    #91
        0xB,
        "#704F#5P──到此为止！\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_62(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #92
        0x101,
        (
            "#1021F#3P不、不好……\x01",
            "输了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2824")

    ChrTalk(    #93
        0x106,
        "#550F#1P切，大意了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_283E")

    label("loc_2824")


    ChrTalk(    #94
        0x103,
        "#025F#1P啊，大意了。\x02",
    )

    CloseMessageWindow()

    label("loc_283E")

    TurnDirection(0xB, 0x101, 400)

    ChrTalk(    #95
        0xB,
        (
            "#702F呼，本来还希望\x01",
            "你们再努力一点……\x02\x03",

            "#703F在战场上什么都有可能发生。\x01",
            "这样的结果也是没办法的。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xB, 180, 400)

    ChrTalk(    #96
        0xB,
        (
            "#704F──那么，我宣布训练结束。\x02\x03",

            "各位官兵辛苦了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x106, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #97
        "\x07\x02任务【特别训练参加邀请】\x07\x00失败了……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x6D, 0x1, 0x8)
    OP_31(0x0, 0xFE, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2953")
    OP_31(0x5, 0xFE, 0x0)
    Jump("loc_2958")

    label("loc_2953")

    OP_31(0x2, 0xFE, 0x0)

    label("loc_2958")

    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/C3100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_26E6 end

    def Function_5_296F(): pass

    label("Function_5_296F")

    OP_8C(0xD, 135, 400)
    Sleep(800)
    OP_8C(0xD, 90, 400)
    Sleep(800)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_5_296F end

    def Function_6_298F(): pass

    label("Function_6_298F")

    OP_62(0xE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0xE, 180, 400)
    Sleep(800)
    OP_8C(0xE, 90, 400)
    Sleep(800)
    OP_63(0xE)
    OP_8C(0xE, 135, 400)
    Sleep(800)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_6_298F end

    def Function_7_29D0(): pass

    label("Function_7_29D0")

    OP_8C(0xF, 0, 400)
    Sleep(800)
    OP_62(0xF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0xF, 90, 400)
    Sleep(800)
    OP_8C(0xF, 45, 400)
    Sleep(800)
    OP_63(0xF)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_7_29D0 end

    def Function_8_2A11(): pass

    label("Function_8_2A11")

    OP_8C(0x10, 90, 400)
    Sleep(800)
    OP_8C(0x10, 45, 400)
    Sleep(800)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_8_2A11 end

    def Function_9_2A31(): pass

    label("Function_9_2A31")

    OP_94(0x1, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Sleep(1000)
    OP_A2(0x2)
    OP_8C(0xFE, 180, 400)
    OP_94(0x1, 0xFE, 0x0, 0x708, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    OP_94(0x1, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_9_2A31 end

    def Function_10_2A83(): pass

    label("Function_10_2A83")

    OP_94(0x1, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Sleep(1000)
    OP_A2(0x3)
    OP_8C(0xFE, 180, 400)
    OP_94(0x1, 0xFE, 0x0, 0x708, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    OP_94(0x1, 0xFE, 0x0, 0x157C, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_10_2A83 end

    def Function_11_2AD5(): pass

    label("Function_11_2AD5")

    OP_94(0x1, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
    SetChrSubChip(0xFE, 0)
    OP_A6(0x2)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_11_2AD5 end

    def Function_12_2AF4(): pass

    label("Function_12_2AF4")

    OP_94(0x1, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
    SetChrSubChip(0xFE, 0)
    OP_A6(0x3)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_12_2AF4 end

    def Function_13_2B13(): pass

    label("Function_13_2B13")

    OP_8E(0xD, 0xFFFFF0C4, 0x0, 0x5EBA, 0x7D0, 0x0)
    OP_8C(0xD, 90, 400)
    Return()

    # Function_13_2B13 end

    def Function_14_2B2F(): pass

    label("Function_14_2B2F")

    OP_8E(0xE, 0xFFFFF4AC, 0x0, 0x59D8, 0x7D0, 0x0)
    OP_8C(0xE, 90, 400)
    Return()

    # Function_14_2B2F end

    def Function_15_2B4B(): pass

    label("Function_15_2B4B")

    OP_8E(0xF, 0xFFFFECDC, 0x0, 0x59D8, 0x7D0, 0x0)
    OP_8C(0xF, 90, 400)
    Return()

    # Function_15_2B4B end

    def Function_16_2B67(): pass

    label("Function_16_2B67")

    OP_8E(0x10, 0xFFFFF0C4, 0x0, 0x54F6, 0x7D0, 0x0)
    OP_8C(0x10, 90, 400)
    Return()

    # Function_16_2B67 end

    def Function_17_2B83(): pass

    label("Function_17_2B83")

    OP_99(0xFE, 0x3, 0x0, 0x7D0)
    OP_8C(0xFE, 270, 0)
    SetChrChipByIndex(0xFE, 10)
    OP_94(0x1, 0xFE, 0x0, 0x1F40, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_17_2B83 end

    def Function_18_2BAD(): pass

    label("Function_18_2BAD")

    SetChrChipByIndex(0x104, 25)
    OP_99(0x104, 0x0, 0xE, 0x7D0)
    WaitChrThread(0x104, 0x0)
    SetChrSubChip(0x104, 14)
    Return()

    # Function_18_2BAD end

    SaveToFile()

Try(main)
