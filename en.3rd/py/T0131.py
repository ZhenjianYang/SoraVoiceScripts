from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'T0131   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0131.x',
        MapIndex            = 7,
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
        'Scherazard',                           # 9
        'Faulkner',                             # 10
        'Trent',                                # 11
        'Bottle',                               # 12
        'Bottle',                               # 13
        'Bottle',                               # 14
        'Glass',                                # 15
        'Estelle',                              # 16
        'Joshua',                               # 17
        'Cassius',                              # 18
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
        'ED6_DT07/CH00023 ._CH',             # 00
        'ED6_DT07/CH01270 ._CH',             # 01
        'ED6_DT07/CH01503 ._CH',             # 02
        'ED6_DT06/CH20020 ._CH',             # 03
        'ED6_DT06/CH20021 ._CH',             # 04
        'ED6_DT27/CH03000 ._CH',             # 05
        'ED6_DT27/CH03200 ._CH',             # 06
        'ED6_DT07/CH02000 ._CH',             # 07
        'ED6_DT27/CH03001 ._CH',             # 08
    )

    AddCharChipPat(
        'ED6_DT07/CH00023P._CP',             # 00
        'ED6_DT07/CH01270P._CP',             # 01
        'ED6_DT07/CH01503P._CP',             # 02
        'ED6_DT06/CH20020P._CP',             # 03
        'ED6_DT06/CH20021P._CP',             # 04
        'ED6_DT27/CH03000P._CP',             # 05
        'ED6_DT27/CH03200P._CP',             # 06
        'ED6_DT07/CH02000P._CP',             # 07
        'ED6_DT27/CH03001P._CP',             # 08
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 34500,
        Z                   = 0,
        Y                   = 75200,
        Direction           = 90,
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
        X                   = 39320,
        Z                   = 220,
        Y                   = 70940,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1D5,
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
        Unknown3            = 1835011,
        ChipIndex           = 0x3,
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
        Unknown3            = 1835011,
        ChipIndex           = 0x3,
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
        Unknown3            = 1835011,
        ChipIndex           = 0x3,
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
        Unknown3            = 327684,
        ChipIndex           = 0x4,
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
        Direction           = 180,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
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


    ScpFunction(
        "Function_0_232",          # 00, 0
        "Function_1_26E",          # 01, 1
        "Function_2_26F",          # 02, 2
        "Function_3_852",          # 03, 3
        "Function_4_8CD",          # 04, 4
        "Function_5_948",          # 05, 5
        "Function_6_9D9",          # 06, 6
        "Function_7_A65",          # 07, 7
        "Function_8_ABE",          # 08, 8
        "Function_9_B1C",          # 09, 9
        "Function_10_B7A",         # 0A, 10
        "Function_11_D55",         # 0B, 11
    )


    def Function_0_232(): pass

    label("Function_0_232")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 6)), scpexpr(EXPR_END)), "loc_251")
    OP_A3(0x2506)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 10)
    Jump("loc_26D")

    label("loc_251")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 7)), scpexpr(EXPR_END)), "loc_26D")
    OP_A3(0x2507)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)

    label("loc_26D")

    Return()

    # Function_0_232 end

    def Function_1_26E(): pass

    label("Function_1_26E")

    Return()

    # Function_1_26E end

    def Function_2_26F(): pass

    label("Function_2_26F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(44470, 0, 71430, 0)
    OP_67(0, 5880, -10000, 0)
    OP_6B(2240, 0)
    OP_6C(315000, 0)
    OP_6E(341, 0)
    OP_43(0x17, 0x0, 0x0, 0x7)
    OP_43(0x18, 0x0, 0x0, 0x8)
    OP_43(0x19, 0x0, 0x0, 0x9)
    OP_82(0x80, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x17, 0x0)
    WaitChrThread(0x18, 0x0)
    WaitChrThread(0x19, 0x0)

    ChrTalk(    #0
        0x17,
        "#1000F#5PHuh?\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_31B():
        OP_6D(36910, 0, 74580, 2000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_31B)

    def lambda_333():
        OP_67(0, 5470, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_333)

    def lambda_34B():
        OP_6B(2610, 2000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_34B)

    def lambda_35B():
        OP_6E(355, 2000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_35B)
    WaitChrThread(0x0, 0x0)
    Sleep(1000)
    Fade(500)
    OP_6D(44470, 0, 71430, 0)
    OP_67(0, 5880, -10000, 0)
    OP_6B(2240, 0)
    OP_6C(315000, 0)
    OP_6E(341, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #1
        0x18,
        "#1040F#4PThere's no one here, either...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x17, 90, 400)
    Sleep(200)

    ChrTalk(    #2
        0x17,
        (
            "#1000F#5PTh-That's kind of weird, though.\x02\x03",

            "I mean, normally there'd be at least one\x01",
            "customer here at this time of day...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #3
        0x17,
        (
            "#1000F#5PO-Oh, I know. Maybe someone's up on the second\x01",
            "floor.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_4D9():
        OP_6D(33740, 2000, 65920, 3000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_4D9)

    def lambda_4F1():
        OP_67(0, 6920, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4F1)

    def lambda_509():
        OP_6B(2070, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_509)
    OP_43(0x17, 0x0, 0x0, 0x6)
    WaitChrThread(0x17, 0x0)
    WaitChrThread(0x0, 0x0)
    OP_43(0x17, 0x0, 0x0, 0x5)
    OP_43(0x18, 0x0, 0x0, 0x4)
    OP_43(0x19, 0x0, 0x0, 0x3)
    Fade(500)
    OP_6D(74630, -500, 79590, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2520, 0)
    OP_6C(327000, 0)
    OP_6E(333, 0)

    def lambda_581():
        OP_6D(81700, 0, 81960, 4000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_581)

    def lambda_599():
        OP_67(0, 5700, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_599)

    def lambda_5B1():
        OP_6B(2550, 4000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_5B1)

    def lambda_5C1():
        OP_6C(315000, 4000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_5C1)
    WaitChrThread(0x0, 0x0)
    Sleep(300)
    WaitChrThread(0x17, 0x0)

    ChrTalk(    #4
        0x17,
        "#1000F#5POh...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x18, 0x0)

    ChrTalk(    #5
        0x18,
        "#1040F#5PThere's no one here, either...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x19, 0x0)

    ChrTalk(    #6
        0x19,
        "#80F#5PHmm...\x02",
    )

    CloseMessageWindow()

    def lambda_63E():
        OP_6D(80840, 0, 82080, 1000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_63E)

    def lambda_656():
        OP_67(0, 4980, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_656)

    def lambda_66E():
        OP_6B(2560, 1000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_66E)
    OP_8C(0x17, 270, 400)
    WaitChrThread(0x0, 0x0)

    ChrTalk(    #7
        0x17,
        (
            "#1000F#4PI-I'm not the only one who thinks this is\x01",
            "kinda weird, right?\x02\x03",

            "You don't think something serious could\x01",
            "have happened, do you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x18,
        (
            "#1040F#5PDon't jump to conclusions, Estelle.\x02\x03",

            "It's too early to be making assumptions like that.\x01",
            "Let's at least head over to the guild first.\x02\x03",

            "If something serious really is going on, they likely\x01",
            "already know about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x17,
        (
            "#1000F#4PY-Yeah. Good point.\x02\x03",

            "Let's head over there, then.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x2508)
    NewScene("ED6_DT21/T0121   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_2_26F end

    def Function_3_852(): pass

    label("Function_3_852")

    Sleep(1200)
    SetChrPos(0xFE, 74510, -2000, 81830, 180)
    OP_8E(0xFE, 0x12444, 0x0, 0x13074, 0xBB8, 0x0)
    OP_8E(0xFE, 0x12C50, 0x0, 0x130F6, 0xBB8, 0x0)
    OP_8E(0xFE, 0x12C8C, 0x0, 0x13E70, 0xBB8, 0x0)
    OP_8E(0xFE, 0x1370E, 0x0, 0x13D80, 0xBB8, 0x0)
    OP_8F(0xFE, 0x13C40, 0x0, 0x13EA2, 0xBB8, 0x0)
    Return()

    # Function_3_852 end

    def Function_4_8CD(): pass

    label("Function_4_8CD")

    Sleep(500)
    SetChrPos(0xFE, 74510, -2000, 81830, 180)
    OP_8E(0xFE, 0x12444, 0x0, 0x13074, 0xBB8, 0x0)
    OP_8E(0xFE, 0x12C50, 0x0, 0x130F6, 0xBB8, 0x0)
    OP_8E(0xFE, 0x12C8C, 0x0, 0x13E70, 0xBB8, 0x0)
    OP_8E(0xFE, 0x1370E, 0x0, 0x13D80, 0xBB8, 0x0)
    OP_8F(0xFE, 0x13E48, 0x0, 0x13A60, 0xBB8, 0x0)
    Return()

    # Function_4_8CD end

    def Function_5_948(): pass

    label("Function_5_948")

    SetChrChipByIndex(0xFE, 8)
    SetChrFlags(0xFE, 0x1000)
    SetChrPos(0xFE, 74510, -2000, 81830, 180)

    def lambda_969():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_969)
    OP_8E(0xFE, 0x12444, 0x0, 0x13074, 0x1770, 0x0)
    OP_8E(0xFE, 0x12C50, 0x0, 0x130F6, 0x1770, 0x0)
    OP_8E(0xFE, 0x12C8C, 0x0, 0x13E70, 0x1770, 0x0)
    OP_8E(0xFE, 0x142BC, 0x0, 0x13CB8, 0x1770, 0x0)
    OP_44(0xFE, 0x3)
    ClearChrFlags(0xFE, 0x1000)
    SetChrChipByIndex(0xFE, 5)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_5_948 end

    def Function_6_9D9(): pass

    label("Function_6_9D9")

    OP_8C(0xFE, 270, 400)

    def lambda_9E6():

        label("loc_9E6")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_9E6")

    QueueWorkItem2(0xFE, 3, lambda_9E6)
    SetChrChipByIndex(0xFE, 8)
    SetChrFlags(0xFE, 0x1000)
    OP_8E(0xFE, 0x8FCA, 0x0, 0x10E64, 0x1770, 0x0)
    OP_8E(0xFE, 0x8FB6, 0x0, 0x101B2, 0x1770, 0x0)
    OP_8E(0xFE, 0x8188, 0x7D0, 0x10112, 0x1770, 0x0)

    def lambda_A3F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A3F)
    OP_8E(0xFE, 0x8228, 0xDAC, 0xF816, 0x1770, 0x0)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_6_9D9 end

    def Function_7_A65(): pass

    label("Function_7_A65")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 48000, -500, 70110, 270)

    def lambda_A8C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A8C)

    def lambda_A9E():
        OP_8E(0xFE, 0xAF64, 0x0, 0x11288, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A9E)
    WaitChrThread(0xFE, 0x1)
    WaitChrThread(0xFE, 0x2)
    Return()

    # Function_7_A65 end

    def Function_8_ABE(): pass

    label("Function_8_ABE")

    Sleep(800)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 48000, -500, 70840, 270)

    def lambda_AEA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AEA)

    def lambda_AFC():
        OP_8E(0xFE, 0xB2B6, 0x0, 0x1159E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_AFC)
    WaitChrThread(0xFE, 0x1)
    WaitChrThread(0xFE, 0x2)
    Return()

    # Function_8_ABE end

    def Function_9_B1C(): pass

    label("Function_9_B1C")

    Sleep(1500)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 48000, -500, 69660, 270)

    def lambda_B48():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B48)

    def lambda_B5A():
        OP_8E(0xFE, 0xB5F4, 0x0, 0x10FEA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B5A)
    WaitChrThread(0xFE, 0x1)
    WaitChrThread(0xFE, 0x2)
    Return()

    # Function_9_B1C end

    def Function_10_B7A(): pass

    label("Function_10_B7A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x13, 39180, 800, 67250, 0)
    SetChrPos(0x14, 39830, 800, 67000, 0)
    SetChrPos(0x15, 39230, 800, 67740, 0)
    SetChrPos(0x16, 39940, 800, 67610, 0)
    OP_9F(0x10, 0xFF, 0x37, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 39730, 200, 68530, 180)
    LoadEffect(0x1, "monster\\ms31000.eff")
    OP_6D(37490, 0, 79300, 0)
    OP_67(0, 5000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(314000, 0)
    OP_6E(320, 0)

    def lambda_C76():
        OP_6D(38790, 0, 69360, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_C76)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    Sleep(300)
    OP_22(0x138, 0x0, 0x64)
    PlayEffect(0x1, 0x1, 0x10, 0, 800, 0, 0, 0, 0, 2500, 2500, 2500, 0xFF, 0, 0, 0, 0)

    def lambda_CDC():
        OP_6B(2550, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_CDC)

    def lambda_CEC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x7D0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_CEC)
    Sleep(1500)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    WaitChrThread(0x109, 0x1)
    Sleep(500)
    WaitChrThread(0x10, 0x0)
    Sleep(1000)
    OP_62(0x10, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x2508)
    NewScene("ED6_DT21/T4230   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_10_B7A end

    def Function_11_D55(): pass

    label("Function_11_D55")

    Sleep(500)
    OP_8C(0xFE, 90, 400)
    Sleep(500)
    OP_8C(0xFE, 180, 600)
    OP_8C(0xFE, 270, 600)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    Sleep(500)
    Return()

    # Function_11_D55 end

    SaveToFile()

Try(main)
