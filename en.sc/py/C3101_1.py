from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Function_1_110A",         # 01, 1
        "Function_2_176A",         # 02, 2
        "Function_3_23BF",         # 03, 3
        "Function_4_2E66",         # 04, 4
        "Function_5_3150",         # 05, 5
        "Function_6_3170",         # 06, 6
        "Function_7_31B1",         # 07, 7
        "Function_8_31F2",         # 08, 8
        "Function_9_3212",         # 09, 9
        "Function_10_3264",        # 0A, 10
        "Function_11_32B6",        # 0B, 11
        "Function_12_32D5",        # 0C, 12
        "Function_13_32F4",        # 0D, 13
        "Function_14_3310",        # 0E, 14
        "Function_15_332C",        # 0F, 15
        "Function_16_3348",        # 10, 16
        "Function_17_3364",        # 11, 17
        "Function_18_338E",        # 12, 18
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
        "#1016FThis is kinda weirdly nostalgic, huh?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8A3")
    OP_61(0x106)

    ChrTalk(    #1
        0x106,
        (
            "#051FYeah. We ain't been in here since,\x01",
            "y'know, then.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8A3")

    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #2
        0x101,
        (
            "#1015FLast time, I couldn't really get a feel\x01",
            "for it since it was so dark...\x02\x03",

            "#1011FBut this base is huuuuuuge!\x01",
            "It's really cool!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9A0")
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #3
        0x103,
        (
            "#020FMmm, not so nostalgic for me, but yes...\x01",
            "I can see why they call it a fortress.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9A0")

    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #4
        0x105,
        (
            "#040FThis IS the headquarters for the Royal\x01",
            "Army, remember?\x02\x03",

            "Its purpose is a bit different from that\x01",
            "of the smaller forts and guard posts you\x01",
            "find in the countryside.\x02",
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
            "#030FHmm... I do believe the new meat we're\x01",
            "to grind now awaits us on the counter.\x02",
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

    def lambda_AFB():
        OP_8C(0xF7, 270, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_AFB)
    Sleep(250)

    def lambda_B0E():
        OP_8C(0x101, 270, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B0E)
    Sleep(150)

    def lambda_B21():
        OP_8C(0x105, 270, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_B21)

    def lambda_B2F():
        OP_8E(0xD, 0xFFFFF286, 0x0, 0x60D6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_B2F)

    def lambda_B4A():
        OP_8E(0xE, 0xFFFFF286, 0x0, 0x5C26, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_B4A)

    def lambda_B65():
        OP_8E(0xF, 0xFFFFF286, 0x0, 0x5776, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_B65)

    def lambda_B80():
        OP_8E(0x10, 0xFFFFF286, 0x0, 0x52C6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_B80)

    def lambda_B9B():
        OP_6D(0, 0, 24840, 3000)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_B9B)

    def lambda_BB3():
        OP_67(0, 8119, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_BB3)

    def lambda_BCB():
        OP_6C(0, 3000)
        ExitThread()

    QueueWorkItem(0x25, 3, lambda_BCB)

    def lambda_BDB():
        OP_6B(2970, 3000)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_BDB)
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

    def lambda_C9A():
        OP_94(0x1, 0x0, 0x0, 0x15E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_C9A)
    Sleep(50)

    def lambda_CB5():
        OP_94(0x1, 0x1, 0x0, 0x15E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_CB5)
    Sleep(100)

    def lambda_CD0():
        OP_94(0x1, 0x2, 0x0, 0x15E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_CD0)
    Sleep(50)

    def lambda_CEB():
        OP_94(0x1, 0x3, 0x0, 0x15E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_CEB)
    OP_8E(0xB, 0x0, 0x0, 0x661C, 0x7D0, 0x0)
    WaitChrThread(0x0, 0x1)
    WaitChrThread(0x1, 0x1)
    WaitChrThread(0x2, 0x1)
    WaitChrThread(0x3, 0x1)
    Sleep(400)

    ChrTalk(    #6
        0xB,
        (
            "#700FVery well. With our challengers here,\x01",
            "we'll begin the staged battles.\x02\x03",

            "Your opponents shall be a group\x01",
            "of elite bracers!\x02\x03",

            "I suggest you give them your all. They are\x01",
            "veterans, including the victors of this year's\x01",
            "Martial Arts Competition!\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0xD, 0x0, 0x1, 0x5)
    OP_43(0xE, 0x0, 0x1, 0x6)
    OP_43(0xF, 0x0, 0x1, 0x7)
    OP_43(0x10, 0x0, 0x1, 0x8)

    ChrTalk(    #7
        0xD,
        "#2PThe victors of--?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xF,
        "#3PWe're so dead...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 400)

    ChrTalk(    #9
        0xB,
        (
            "#700FAs explained, you'll be fighting\x01",
            "a two-round combat match.\x02\x03",

            "Keep that in mind, and pace\x01",
            "yourselves accordingly.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xB, 400)

    ChrTalk(    #10
        0x101,
        "#1006F#2PWe're ready!\x02",
    )

    CloseMessageWindow()
    OP_44(0xD, 0x0)
    OP_44(0xE, 0x0)
    OP_44(0xF, 0x0)
    OP_44(0x10, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_F79")

    ChrTalk(    #11
        0x106,
        (
            "#050F#4PI'll go as many rounds as I'm needed.\x02\x03",

            "Let's get this started.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FF2")

    label("loc_F79")


    ChrTalk(    #12
        0x103,
        (
            "#525F#4PHeh! I can go as many rounds\x01",
            "as you like...and more! ㈱\x02\x03",

            "I'm sure you boys will get tired\x01",
            "long before I do!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FF2")

    OP_8C(0xB, 180, 400)

    ChrTalk(    #13
        0xB,
        (
            "#700F#6PNo time like the present, then...\x02\x03",

            "Both sides! Arms at the ready!\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_10A2")
    SetChrChipByIndex(0xF7, 19)
    Jump("loc_10A7")

    label("loc_10A2")

    SetChrChipByIndex(0xF7, 13)

    label("loc_10A7")

    SetChrChipByIndex(0xD, 21)
    SetChrChipByIndex(0xE, 21)
    SetChrChipByIndex(0xF, 21)
    SetChrChipByIndex(0x10, 21)
    OP_0D()

    ChrTalk(    #14
        0xB,
        "#704F#6P#3SBEGIN!\x02",
    )

    CloseMessageWindow()
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x8C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0xC80, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_10F9"),
        (1, "loc_1100"),
        (SWITCH_DEFAULT, "loc_1107"),
    )


    label("loc_10F9")

    Call(1, 1)
    Jump("loc_1107")

    label("loc_1100")

    Call(1, 4)
    Jump("loc_1107")

    label("loc_1107")

    EventEnd(0x0)
    Return()

    # Function_0_AA end

    def Function_1_110A(): pass

    label("Function_1_110A")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1180")
    SetChrChipByIndex(0xF7, 19)
    Jump("loc_1185")

    label("loc_1180")

    SetChrChipByIndex(0xF7, 13)

    label("loc_1185")

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
        "#700FCEASE!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        "#1006F#2PWe win!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_12A5")

    ChrTalk(    #17
        0x106,
        "#051F#4PDidn't even break a sweat.\x02",
    )

    CloseMessageWindow()
    Jump("loc_12EA")

    label("loc_12A5")


    ChrTalk(    #18
        0x103,
        (
            "#027F#4PAww, done already?\x01",
            "I was just starting to enjoy myself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12EA")


    ChrTalk(    #19
        0x105,
        "#040FI'm...glad, I guess.\x02",
    )

    CloseMessageWindow()
    OP_62(0xE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)
    OP_99(0xE, 0x3, 0x0, 0x7D0)

    ChrTalk(    #20
        0xE,
        "#6POw-ow-ow-ow...\x02",
    )

    CloseMessageWindow()

    def lambda_1346():

        label("loc_1346")

        TurnDirection(0xB, 0xE, 400)
        OP_48()
        Jump("loc_1346")

    QueueWorkItem2(0xB, 1, lambda_1346)

    ChrTalk(    #21
        0xB,
        (
            "#700FWhat are you men waiting for?\x02\x03",

            "Withdraw from the field!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xE,
        "#6PS-Sir!\x02",
    )

    CloseMessageWindow()
    OP_43(0xD, 0x1, 0x1, 0x11)
    Sleep(100)
    OP_43(0xF, 0x1, 0x1, 0x11)
    Sleep(50)
    OP_43(0x10, 0x1, 0x1, 0x11)
    OP_8C(0xE, 270, 0)
    SetChrChipByIndex(0xE, 10)

    def lambda_13D3():
        OP_94(0x1, 0xFE, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_13D3)
    WaitChrThread(0x10, 0x1)
    WaitChrThread(0xE, 0x1)
    SetChrFlags(0xE, 0x80)
    OP_44(0xB, 0x1)

    ChrTalk(    #23
        0xB,
        "#704FNext--Officer Belc!\x02",
    )

    CloseMessageWindow()

    def lambda_141A():

        label("loc_141A")

        TurnDirection(0xB, 0x25, 0)
        OP_48()
        Jump("loc_141A")

    QueueWorkItem2(0xB, 1, lambda_141A)
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
        "#2PSir!\x02",
    )

    CloseMessageWindow()

    def lambda_1495():
        OP_94(0x1, 0xD, 0x0, 0x1BBC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1495)

    def lambda_14AB():
        OP_94(0x1, 0x25, 0x0, 0x1BBC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_14AB)

    def lambda_14C1():
        OP_94(0x1, 0xF, 0x0, 0x1BBC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_14C1)

    def lambda_14D7():
        OP_94(0x1, 0x10, 0x0, 0x1BBC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_14D7)
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
        "#1007F#2PThey really aren't gonna let us rest...\x02",
    )

    CloseMessageWindow()
    OP_43(0x104, 0x1, 0x1, 0x12)

    ChrTalk(    #26
        0x104,
        (
            "#035F#2PHeh, oh, dear.\x02\x03",

            "I wish they would at least permit\x01",
            "me to straighten my hair.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x25,
        (
            "#1PHmm. No less than I would have expected\x01",
            "from champions of the arena.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x25,
        (
            "#1PTrying to lower my guard by\x01",
            "giving me an opening, are you?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #29
        0x101,
        (
            "#1019F#2PEr... No...?\x02\x03",

            "I think you're getting a little too\x01",
            "into it, Mr. Belc.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xB,
        (
            "#700F#6PWe're still in training. Please\x01",
            "abstain from personal conversations.\x02\x03",

            "Now then, round two.\x01",
            "Both sides, arms at the ready!\x02\x03",

            "#704F#3SBEGIN!\x02",
        )
    )

    CloseMessageWindow()
    Battle(0xC81, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1759"),
        (1, "loc_1760"),
        (SWITCH_DEFAULT, "loc_1767"),
    )


    label("loc_1759")

    Call(1, 2)
    Jump("loc_1767")

    label("loc_1760")

    Call(1, 4)
    Jump("loc_1767")

    label("loc_1767")

    EventEnd(0x0)
    Return()

    # Function_1_110A end

    def Function_2_176A(): pass

    label("Function_2_176A")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_17E5")
    SetChrChipByIndex(0xF7, 19)
    Jump("loc_17EA")

    label("loc_17E5")

    SetChrChipByIndex(0xF7, 13)

    label("loc_17EA")

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
        "#704F#6PCEASE!\x02",
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
        "#030F#2PAnother victory for us, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        "#1002F#2PYeah, somehow.\x02",
    )

    CloseMessageWindow()
    OP_99(0x25, 0x3, 0x0, 0x7D0)

    ChrTalk(    #34
        0x25,
        "#1PNnnngh... We've lost...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x25, 400)

    ChrTalk(    #35
        0xB,
        (
            "#700F...\x02\x03",

            "Officer Belc. Can you still fight?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x25, 0xB, 400)

    ChrTalk(    #36
        0x25,
        "#1PSir...?\x02",
    )

    CloseMessageWindow()
    OP_62(0x25, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #37
        0x25,
        "#1PYes... yes, sir!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xB,
        "#703FGood. Then get ready.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x25,
        "#1PYessir!\x02",
    )

    CloseMessageWindow()
    OP_43(0xD, 0x1, 0x1, 0x11)
    Sleep(100)
    OP_43(0xF, 0x1, 0x1, 0x11)
    Sleep(50)
    OP_43(0x10, 0x1, 0x1, 0x11)
    OP_8C(0x25, 270, 0)
    SetChrChipByIndex(0x25, 31)

    def lambda_1A2F():
        OP_94(0x1, 0xFE, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_1A2F)
    Sleep(1000)

    def lambda_1A4A():
        OP_8C(0x101, 315, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A4A)

    def lambda_1A58():
        OP_8C(0xF7, 315, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_1A58)

    def lambda_1A66():
        OP_8C(0x104, 315, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1A66)

    def lambda_1A74():
        OP_8C(0x105, 315, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1A74)
    OP_66(0x0)
    OP_6D(2400, 0, 24430, 2000)

    ChrTalk(    #40
        0x101,
        "#1015F#2PUm. Ready for what?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x104,
        (
            "#030F#2PHmmmm, whatever could you mean?\x02\x03",

            "Perhaps you intend to throw us a party\x01",
            "in celebration of our outstanding finesse?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 400)

    ChrTalk(    #42
        0xB,
        "#702F#3PParty...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        "#1002F#2PJust...ignore him.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xB,
        (
            "#703F#3PVery well...\x02\x03",

            "#700FNo, I asked him to prepare for\x01",
            "another round, of course.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #45
        0x101,
        (
            "#1004F#2PWh-Whaaaaaaaa?\x02\x03",

            "You said we'd only be fighting two battles!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1D99")

    ChrTalk(    #46
        0xB,
        (
            "#700F#3PI did. However...\x02\x03",

            "In response, you distinctly proclaimed\x01",
            "that you were okay with any number of\x01",
            "rounds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x106,
        "#552F#4PTch. Didn't think you'd take that seriously...\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(    #48
        0x101,
        (
            "#1009F#5PA-Agate! Look what your big mouth\x01",
            "has gotten us into!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x106,
        (
            "#551F#4PAhh, don't worry about it.\x01",
            "I just got caught up in the moment.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EEB")

    label("loc_1D99")


    ChrTalk(    #50
        0xB,
        (
            "#700F#3PI did. However...\x02\x03",

            "In response, you distinctly proclaimed\x01",
            "that you were okay with any number of\x01",
            "rounds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x103,
        (
            "#023F#4PEr, well, I may have said that...\x01",
            "technically...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #52
        0x101,
        "#1007F#5PSch-Schera!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x103,
        (
            "#025F#4PW-Well, we can't do anything about it now.\x01",
            "What can I say? I was caught up in the moment!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EEB")


    ChrTalk(    #54
        0xB,
        (
            "#700F#3PI'd like to take you up on that offer\x01",
            "and request one more round.\x02\x03",

            "And I shall serve as your final opponent.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xB, 400)

    ChrTalk(    #55
        0x101,
        "#1004F#2PWait, YOU, Colonel?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x104,
        (
            "#031F#2PAh, so at long last, your true intentions\x01",
            "are revealed!\x02\x03",

            "You cannot bear to watch and wait\x01",
            "without testing your own skill as well.\x01",
            "There is no need to hide such feelings, sir!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xB,
        "#701F#3PHaha. Guess I've been seen right through.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_20CA")

    ChrTalk(    #58
        0x106,
        (
            "#051F#4PHeh. All right. I get it.\x02\x03",

            "Bring it, then, Cid!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_211D")

    label("loc_20CA")


    ChrTalk(    #59
        0x103,
        (
            "#027F#4PAhh... I see now.\x02\x03",

            "#525FWell, don't worry, I'm always up for more! ㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_211D")

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

    def lambda_217E():
        OP_6D(0, 0, 24840, 2000)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_217E)

    def lambda_2196():
        OP_94(0x1, 0x25, 0x0, 0x13EC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_2196)

    def lambda_21AC():
        OP_94(0x1, 0xF, 0x0, 0x13EC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_21AC)

    def lambda_21C2():
        OP_94(0x1, 0x10, 0x0, 0x13EC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_21C2)
    WaitChrThread(0x25, 0x1)
    WaitChrThread(0xB, 0x1)
    OP_66(0x1)
    SetChrChipByIndex(0x25, 23)
    SetChrChipByIndex(0xF, 21)
    SetChrChipByIndex(0x10, 21)

    ChrTalk(    #60
        0x25,
        "#1PSorry to keep you waiting, sir.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x25, 400)

    ChrTalk(    #61
        0xB,
        "#700FIt's no problem.\x02",
    )

    CloseMessageWindow()

    def lambda_223E():
        OP_67(0, 19910, -29700, 2000)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_223E)

    def lambda_2256():
        OP_6B(1000, 2000)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_2256)

    def lambda_2266():

        label("loc_2266")

        TurnDirection(0x101, 0xB, 0)
        OP_48()
        Jump("loc_2266")

    QueueWorkItem2(0x101, 1, lambda_2266)

    def lambda_2277():

        label("loc_2277")

        TurnDirection(0xF7, 0xB, 0)
        OP_48()
        Jump("loc_2277")

    QueueWorkItem2(0xF7, 1, lambda_2277)

    def lambda_2288():

        label("loc_2288")

        TurnDirection(0xF8, 0xB, 0)
        OP_48()
        Jump("loc_2288")

    QueueWorkItem2(0xF8, 1, lambda_2288)

    def lambda_2299():

        label("loc_2299")

        TurnDirection(0xF9, 0xB, 0)
        OP_48()
        Jump("loc_2299")

    QueueWorkItem2(0xF9, 1, lambda_2299)
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2301")
    SetChrChipByIndex(0xF7, 19)
    Jump("loc_2306")

    label("loc_2301")

    SetChrChipByIndex(0xF7, 13)

    label("loc_2306")

    OP_0D()

    ChrTalk(    #62
        0xB,
        (
            "#700F#1PNow, then, let us begin.\x02\x03",

            "Are you prepared?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2364")

    ChrTalk(    #63
        0x106,
        "#057F#4PBring it on.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2383")

    label("loc_2364")


    ChrTalk(    #64
        0x103,
        "#022F#4PWhenever you are.\x02",
    )

    CloseMessageWindow()

    label("loc_2383")


    ChrTalk(    #65
        0xB,
        "#704F#1POn your guard!\x02",
    )

    CloseMessageWindow()
    Battle(0xC82, 0x0, 0x0, 0x0, 0xFF)
    OP_28(0x6D, 0x1, 0x4)
    OP_28(0x6D, 0x1, 0x10)
    Call(1, 3)
    EventEnd(0x0)
    Return()

    # Function_2_176A end

    def Function_3_23BF(): pass

    label("Function_3_23BF")

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
        (0, "loc_2452"),
        (1, "loc_264F"),
        (SWITCH_DEFAULT, "loc_28CB"),
    )


    label("loc_2452")

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
            "#1021F#2PO-Okay... We won...\x01",
            "I think...somehow...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x105,
        "#042F#2PThank goodness...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_252D")

    ChrTalk(    #68
        0x106,
        (
            "#551F#4PThat...was rough.\x02\x03",

            "He was knocking us around like twigs...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2578")

    label("loc_252D")


    ChrTalk(    #69
        0x103,
        (
            "#025F#4PThat was close...\x02\x03",

            "I don't think we could've taken\x01",
            "much more.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2578")


    ChrTalk(    #70
        0xB,
        "#703F#1PIncredible... Total defeat.\x02",
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
            "#701F#1PI'm impressed you did so well,\x01",
            "even after back-to-back fights.\x02\x03",

            "You're the perfect model for our soldiers.\x02",
        )
    )

    CloseMessageWindow()
    OP_2B(0x6D, 0x2)
    OP_2C(0x6D, 0x5DC)
    Jump("loc_28CB")

    label("loc_264F")

    OP_28(0x6D, 0x1, 0x40)
    SetChrChipByIndex(0x104, 16)
    SetChrChipByIndex(0x101, 12)
    SetChrChipByIndex(0x105, 18)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2673")
    SetChrChipByIndex(0xF7, 20)
    Jump("loc_2678")

    label("loc_2673")

    SetChrChipByIndex(0xF7, 14)

    label("loc_2678")

    SetChrSubChip(0x104, 3)
    SetChrSubChip(0x101, 3)
    SetChrSubChip(0x105, 3)
    SetChrSubChip(0xF7, 3)
    Sleep(1000)

    ChrTalk(    #72
        0x101,
        (
            "#1021F#2POw, ow...\x02\x03",

            "We...lost, huh...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x105,
        "#541FRnng... Unfortunately...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2736")

    ChrTalk(    #74
        0x106,
        (
            "#056F#4PDamn it. We're pathetic.\x02\x03",

            "Can't believe we got beat like that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2789")

    label("loc_2736")


    ChrTalk(    #75
        0x103,
        (
            "#025F#4PYes, that was...inevitable, I think.\x02\x03",

            "He pushed us right to the edge.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2789")


    ChrTalk(    #76
        0x104,
        (
            "#035F#2POur defeat is absolute. Even our spirits\x01",
            "had the wind knocked from them.\x02",
        )
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
            "#701F#1PNo, being able to fight that well after\x01",
            "back-to-back battles is still quite\x01",
            "impressive.\x02\x03",

            "You've been more than enough of\x01",
            "a model for our soldiers.\x02",
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
    Jump("loc_28CB")

    label("loc_28CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_293B")

    ChrTalk(    #78
        0x106,
        (
            "#053F#4PI think you were the model here.\x02\x03",

            "Hate to admit it, but we learned\x01",
            "a fair bit ourselves.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29A3")

    label("loc_293B")


    ChrTalk(    #79
        0x103,
        (
            "#020F#4PNo, sir, I believe you were the model.\x02\x03",

            "It's humbling to admit,\x01",
            "but we learned a lot here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29A3")


    ChrTalk(    #80
        0x101,
        (
            "#1015F#2PYeah, I don't think we've ever gotten\x01",
            "pounded by arts like that before.\x02\x03",

            "#1006FMaybe we should give our orbment\x01",
            "setup another look.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xB,
        (
            "#701F#1PIf you too learned something from this,\x01",
            "that makes it all worthwhile.\x02\x03",

            "True power doesn't stem from the technique\x01",
            "itself, after all, but from how you use it.\x02\x03",

            "This goes for arts and crafts alike.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x104,
        "#031FExcellent advice!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xB,
        (
            "#701F#1PMembers of the Royal Army train to improve\x01",
            "ourselves no less than bracers.\x02\x03",

            "And we fully intend to continue doing so,\x01",
            "for the sake of lasting peace in this kingdom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x101,
        (
            "#1006F#2PYeah, we're going to keep\x01",
            "training as well.\x02\x03",

            "#1001FIf the chance comes up,\x01",
            "I'd love another shot.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2C76")

    ChrTalk(    #85
        0x106,
        "#051F#4PI'd be okay with that too.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CB1")

    label("loc_2C76")


    ChrTalk(    #86
        0x103,
        (
            "#020F#4PI'd certainly love another round...\x01",
            "some day.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CB1")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_2CC1"),
        (1, "loc_2D55"),
        (SWITCH_DEFAULT, "loc_2D96"),
    )


    label("loc_2CC1")


    ChrTalk(    #87
        0xB,
        (
            "#701F#1PYou have my word that you will have\x01",
            "that chance.\x02\x03",

            "After all, I don't intend to leave\x01",
            "things as they are. I'd like a rematch\x01",
            "myself!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D96")

    label("loc_2D55")


    ChrTalk(    #88
        0xB,
        (
            "#701F#1PYou have my word that you will have\x01",
            "that chance.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D96")

    label("loc_2D96")

    OP_8C(0xB, 45, 400)

    ChrTalk(    #89
        0xB,
        (
            "#704F#1PThis concludes our training, then.\x02\x03",

            "Good work, men.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x17, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #90
        "Quest #CR#[Training Assistance] #CW#completed!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_31(0x0, 0xFE, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2E4A")
    OP_31(0x5, 0xFE, 0x0)
    Jump("loc_2E4F")

    label("loc_2E4A")

    OP_31(0x2, 0xFE, 0x0)

    label("loc_2E4F")

    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/C3100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_23BF end

    def Function_4_2E66(): pass

    label("Function_4_2E66")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2F07")
    SetChrChipByIndex(0xF7, 20)
    Jump("loc_2F0C")

    label("loc_2F07")

    SetChrChipByIndex(0xF7, 14)

    label("loc_2F0C")

    SetChrSubChip(0x104, 3)
    SetChrSubChip(0x101, 3)
    SetChrSubChip(0x105, 3)
    SetChrSubChip(0xF7, 3)
    Sleep(1000)

    ChrTalk(    #91
        0xB,
        "#704F#6PCEASE!\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_62(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #92
        0x101,
        (
            "#1021F#2PAugh, my...everything.\x01",
            "We... We lost.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2FBC")

    ChrTalk(    #93
        0x106,
        "#550F#4PDamn. Let my guard down...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2FF6")

    label("loc_2FBC")


    ChrTalk(    #94
        0x103,
        (
            "#025F#4PMmm... Looks like we weren't\x01",
            "careful enough.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FF6")

    TurnDirection(0xB, 0x101, 400)

    ChrTalk(    #95
        0xB,
        (
            "#702FHmm. I'd hoped for a bit more of\x01",
            "a fight than this...\x02\x03",

            "#703FAnything can happen on the battlefield,\x01",
            "though, I suppose.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xB, 180, 400)

    ChrTalk(    #96
        0xB,
        (
            "#704FThis concludes our training, then.\x02\x03",

            "Good work, men.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x106, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #97
        "Quest #CR#[Training Assistance] #CW#failed...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x6D, 0x1, 0x8)
    OP_31(0x0, 0xFE, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3134")
    OP_31(0x5, 0xFE, 0x0)
    Jump("loc_3139")

    label("loc_3134")

    OP_31(0x2, 0xFE, 0x0)

    label("loc_3139")

    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/C3100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_2E66 end

    def Function_5_3150(): pass

    label("Function_5_3150")

    OP_8C(0xD, 135, 400)
    Sleep(800)
    OP_8C(0xD, 90, 400)
    Sleep(800)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_5_3150 end

    def Function_6_3170(): pass

    label("Function_6_3170")

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

    # Function_6_3170 end

    def Function_7_31B1(): pass

    label("Function_7_31B1")

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

    # Function_7_31B1 end

    def Function_8_31F2(): pass

    label("Function_8_31F2")

    OP_8C(0x10, 90, 400)
    Sleep(800)
    OP_8C(0x10, 45, 400)
    Sleep(800)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_8_31F2 end

    def Function_9_3212(): pass

    label("Function_9_3212")

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

    # Function_9_3212 end

    def Function_10_3264(): pass

    label("Function_10_3264")

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

    # Function_10_3264 end

    def Function_11_32B6(): pass

    label("Function_11_32B6")

    OP_94(0x1, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
    SetChrSubChip(0xFE, 0)
    OP_A6(0x2)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_11_32B6 end

    def Function_12_32D5(): pass

    label("Function_12_32D5")

    OP_94(0x1, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
    SetChrSubChip(0xFE, 0)
    OP_A6(0x3)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_12_32D5 end

    def Function_13_32F4(): pass

    label("Function_13_32F4")

    OP_8E(0xD, 0xFFFFF0C4, 0x0, 0x5EBA, 0x7D0, 0x0)
    OP_8C(0xD, 90, 400)
    Return()

    # Function_13_32F4 end

    def Function_14_3310(): pass

    label("Function_14_3310")

    OP_8E(0xE, 0xFFFFF4AC, 0x0, 0x59D8, 0x7D0, 0x0)
    OP_8C(0xE, 90, 400)
    Return()

    # Function_14_3310 end

    def Function_15_332C(): pass

    label("Function_15_332C")

    OP_8E(0xF, 0xFFFFECDC, 0x0, 0x59D8, 0x7D0, 0x0)
    OP_8C(0xF, 90, 400)
    Return()

    # Function_15_332C end

    def Function_16_3348(): pass

    label("Function_16_3348")

    OP_8E(0x10, 0xFFFFF0C4, 0x0, 0x54F6, 0x7D0, 0x0)
    OP_8C(0x10, 90, 400)
    Return()

    # Function_16_3348 end

    def Function_17_3364(): pass

    label("Function_17_3364")

    OP_99(0xFE, 0x3, 0x0, 0x7D0)
    OP_8C(0xFE, 270, 0)
    SetChrChipByIndex(0xFE, 10)
    OP_94(0x1, 0xFE, 0x0, 0x1F40, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_17_3364 end

    def Function_18_338E(): pass

    label("Function_18_338E")

    SetChrChipByIndex(0x104, 25)
    OP_99(0x104, 0x0, 0xE, 0x7D0)
    WaitChrThread(0x104, 0x0)
    SetChrSubChip(0x104, 14)
    Return()

    # Function_18_338E end

    SaveToFile()

Try(main)
