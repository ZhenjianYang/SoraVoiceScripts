from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M4300   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M4300.x',
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
        ' ',                                    # 9
        ' ',                                    # 10
        ' ',                                    # 11
        ' ',                                    # 12
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


    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x180,
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
        NpcIndex            = 0x180,
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
        NpcIndex            = 0x180,
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
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_12A",          # 00, 0
        "Function_1_13E",          # 01, 1
        "Function_2_145",          # 02, 2
        "Function_3_77D",          # 03, 3
        "Function_4_7A6",          # 04, 4
        "Function_5_7D4",          # 05, 5
        "Function_6_802",          # 06, 6
        "Function_7_830",          # 07, 7
        "Function_8_983",          # 08, 8
        "Function_9_9C7",          # 09, 9
        "Function_10_9FD",         # 0A, 10
        "Function_11_A25",         # 0B, 11
    )


    def Function_0_12A(): pass

    label("Function_0_12A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_13D")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 2)

    label("loc_13D")

    Return()

    # Function_0_12A end

    def Function_1_13E(): pass

    label("Function_1_13E")

    OP_71(0x410, 0x0)
    ExitThread()
    Return()

    # Function_1_13E end

    def Function_2_145(): pass

    label("Function_2_145")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, 45000, 0, -13660, 270)
    SetChrPos(0x10F, 45000, 0, -13660, 270)
    SetChrPos(0xF0, 45000, 0, -13660, 270)
    SetChrPos(0xF1, 45000, 0, -13660, 270)
    OP_6D(40590, 0, -13160, 0)
    OP_67(0, 7800, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_43(0x109, 0x0, 0x0, 0x3)
    OP_43(0x10F, 0x0, 0x0, 0x4)
    OP_43(0xF0, 0x0, 0x0, 0x5)
    OP_43(0xF1, 0x0, 0x0, 0x6)
    FadeToBright(2000, 0)
    Sleep(1000)

    def lambda_202():
        OP_6D(39070, 0, -13140, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_202)

    def lambda_21A():
        OP_67(0, 7800, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_21A)

    def lambda_232():
        OP_6B(3200, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_232)

    def lambda_242():
        OP_6C(45000, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_242)

    def lambda_252():
        OP_6E(262, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_252)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    WaitChrThread(0x109, 0x1)

    ChrTalk(    #0
        0x10F,
        "#1444F#5POh, my...\x02",
    )

    CloseMessageWindow()

    def lambda_293():
        OP_6D(1080, 0, -19600, 6000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_293)

    def lambda_2AB():
        OP_67(0, 7500, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2AB)

    def lambda_2C3():
        OP_6B(4310, 6000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2C3)

    def lambda_2D3():
        OP_6C(45000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_2D3)

    def lambda_2E3():
        OP_6E(490, 6000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_2E3)
    WaitChrThread(0x109, 0x3)

    def lambda_2F8():
        OP_6C(0, 6000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_2F8)
    WaitChrThread(0x109, 0x0)

    def lambda_30D():
        OP_6D(10, 0, 19140, 6000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_30D)

    def lambda_325():
        OP_67(0, 2200, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_325)

    def lambda_33D():
        OP_6B(4560, 6000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_33D)

    def lambda_34D():
        OP_6E(551, 6000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_34D)
    WaitChrThread(0x109, 0x0)
    Sleep(1000)
    Fade(500)
    OP_6D(39310, 0, -12660, 0)
    OP_67(0, 6240, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(319, 0)
    OP_0D()
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_518")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_401")

    ChrTalk(    #1
        0x10B,
        "#216F#5PW-Whoa... This place is crazy...\x02",
    )

    CloseMessageWindow()
    Jump("loc_477")

    label("loc_401")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_477")

    ChrTalk(    #2
        0x10D,
        (
            "#270F#5PI'd heard about this area from Olivier,\x01",
            "but that hardly compares to seeing it\x01",
            "in person...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_477")


    ChrTalk(    #3
        0x10E,
        (
            "#178F#5PI doubt we'll be able to make our way\x01",
            "through here without a significant amount\x01",
            "of preparation.\x02\x03",

            "#176FMight I suggest we return to base for now?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63F")

    label("loc_518")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_63F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5A8")

    ChrTalk(    #4
        0x102,
        (
            "#1502F#5PWe're not going to be able to get through\x01",
            "here without a lot of preparation beforehand.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_600")

    label("loc_5A8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_600")

    ChrTalk(    #5
        0x107,
        (
            "#065F#5PG-Getting through this place is going to be \x01",
            "pretty tough...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_600")


    ChrTalk(    #6
        0x10E,
        (
            "#175F#5PHmm... Might I suggest we return to base\x01",
            "for now?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_63F")


    ChrTalk(    #7
        0x109,
        (
            "#1063FI think we should go a little farther inside and\x01",
            "see what state the ruin itself is in first.\x02\x03",

            "Kinda hard to know what to prepare for if we\x01",
            "don't know what fiends we're gonna be up\x01",
            "against.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x10E,
        (
            "#176F#5PTrue enough.\x02\x03",

            "#170FLet's advance a little farther before\x01",
            "returning to the garden, then.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x271D)
    OP_28(0x2E, 0x1, 0x2)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_2_145 end

    def Function_3_77D(): pass

    label("Function_3_77D")

    OP_8E(0xFE, 0xA0DC, 0x0, 0xFFFFC96E, 0x7D0, 0x0)
    OP_8E(0xFE, 0x909C, 0x0, 0xFFFFC630, 0x7D0, 0x0)
    Return()

    # Function_3_77D end

    def Function_4_7A6(): pass

    label("Function_4_7A6")

    Sleep(600)
    OP_8E(0xFE, 0xA0DC, 0x0, 0xFFFFC96E, 0x7D0, 0x0)
    OP_8E(0xFE, 0x9132, 0x0, 0xFFFFCBE4, 0x7D0, 0x0)
    Return()

    # Function_4_7A6 end

    def Function_5_7D4(): pass

    label("Function_5_7D4")

    Sleep(1100)
    OP_8E(0xFE, 0xA0DC, 0x0, 0xFFFFC96E, 0x7D0, 0x0)
    OP_8E(0xFE, 0x9664, 0x0, 0xFFFFC586, 0x7D0, 0x0)
    Return()

    # Function_5_7D4 end

    def Function_6_802(): pass

    label("Function_6_802")

    Sleep(1700)
    OP_8E(0xFE, 0xA0DC, 0x0, 0xFFFFC96E, 0x7D0, 0x0)
    OP_8E(0xFE, 0x9678, 0x0, 0xFFFFCD7E, 0x7D0, 0x0)
    Return()

    # Function_6_802 end

    def Function_7_830(): pass

    label("Function_7_830")

    EventBegin(0x0)
    OP_51(0x10, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0x0, 0x1, 0x0, 0xB)
    OP_43(0x1, 0x1, 0x0, 0xA)
    OP_43(0x2, 0x1, 0x0, 0x9)
    OP_43(0x3, 0x1, 0x0, 0x8)
    WaitChrThread(0x3, 0x1)
    OP_30(0x0)
    Sleep(300)
    OP_22(0x9C, 0x0, 0x64)
    Sleep(1000)
    OP_22(0xF7, 0x0, 0x64)
    OP_22(0x68, 0x1, 0x64)
    FadeToDark(2000, 0, -1)
    OP_24(0x68, 0x5A)
    Sleep(400)
    OP_24(0x68, 0x55)
    Sleep(400)
    OP_24(0x68, 0x50)
    Sleep(400)
    OP_24(0x68, 0x4B)
    Sleep(400)
    OP_24(0x68, 0x46)
    Sleep(400)
    OP_24(0x68, 0x41)
    Sleep(400)
    OP_24(0x68, 0x3C)
    Sleep(400)
    OP_23(0x68)
    NewScene("ED6_DT21/U4241   ._SN", 101, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_7_830 end

    def Function_8_983(): pass

    label("Function_8_983")

    OP_92(0xFE, 0x12, 0x0, 0x1770, 0x0)
    OP_92(0xFE, 0x11, 0x0, 0x1770, 0x0)
    OP_92(0xFE, 0x10, 0x0, 0x1770, 0x0)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xFE, 0xAFC8, 0x0, 0xFFFFCAA4, 0x7D0, 0x0)
    Return()

    # Function_8_983 end

    def Function_9_9C7(): pass

    label("Function_9_9C7")

    OP_92(0xFE, 0x11, 0x0, 0x1770, 0x0)
    OP_92(0xFE, 0x10, 0x0, 0x1770, 0x0)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xFE, 0xAFC8, 0x0, 0xFFFFCAA4, 0x7D0, 0x0)
    Return()

    # Function_9_9C7 end

    def Function_10_9FD(): pass

    label("Function_10_9FD")

    OP_92(0xFE, 0x10, 0x0, 0x1770, 0x0)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xFE, 0xAFC8, 0x0, 0xFFFFCAA4, 0x7D0, 0x0)
    Return()

    # Function_10_9FD end

    def Function_11_A25(): pass

    label("Function_11_A25")

    SetChrSubChip(0xFE, 0)
    OP_8E(0xFE, 0xAFC8, 0x0, 0xFFFFCAA4, 0x7D0, 0x0)
    Return()

    # Function_11_A25 end

    SaveToFile()

Try(main)
