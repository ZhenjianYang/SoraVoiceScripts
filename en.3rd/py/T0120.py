from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'T0120   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0120.x',
        MapIndex            = 4,
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
        'Estelle',                              # 9
        'Joshua',                               # 10
        'Cassius',                              # 11
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
        'ED6_DT27/CH03000 ._CH',             # 00
        'ED6_DT27/CH03200 ._CH',             # 01
        'ED6_DT07/CH02000 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT27/CH03000P._CP',             # 00
        'ED6_DT27/CH03200P._CP',             # 01
        'ED6_DT07/CH02000P._CP',             # 02
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_122",          # 00, 0
        "Function_1_13F",          # 01, 1
        "Function_2_140",          # 02, 2
        "Function_3_3D6",          # 03, 3
        "Function_4_42F",          # 04, 4
        "Function_5_48D",          # 05, 5
    )


    def Function_0_122(): pass

    label("Function_0_122")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_13E")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)

    label("loc_13E")

    Return()

    # Function_0_122 end

    def Function_1_13F(): pass

    label("Function_1_13F")

    Return()

    # Function_1_13F end

    def Function_2_140(): pass

    label("Function_2_140")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-37870, 0, 67240, 0)
    OP_67(0, 5740, -10000, 0)
    OP_6B(2060, 0)
    OP_6C(315000, 0)
    OP_6E(392, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)

    def lambda_1B7():
        OP_6D(-38620, 0, 68840, 2000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_1B7)

    def lambda_1CF():
        OP_67(0, 5410, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1CF)
    OP_43(0x10, 0x0, 0x0, 0x3)
    OP_43(0x11, 0x0, 0x0, 0x4)
    OP_43(0x12, 0x0, 0x0, 0x5)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x0, 0x0)

    ChrTalk(    #0
        0x10,
        (
            "#1000F#2PGood morning, Mr. Elger!\x02\x03",

            "...Huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x11,
        "#1040F#4PIt looks like he must be out somewhere...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x10,
        (
            "#1000F#2PY-Yeah...\x02\x03",

            "It's not like him to leave the shop empty like\x01",
            "this, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x12,
        (
            "#80FIndeed. Perhaps some sudden business came up\x01",
            "that meant he had to pop out for a while.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x11, 315, 400)
    Sleep(300)

    ChrTalk(    #4
        0x11,
        (
            "#1040F#4PThat sounds like the most likely possibility.\x02\x03",

            "Let's go and see Elissa first, then.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 135, 400)
    Sleep(200)

    ChrTalk(    #5
        0x10,
        "#1000F#5PYeah! Okay.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x2507)
    NewScene("ED6_DT21/T0131   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_2_140 end

    def Function_3_3D6(): pass

    label("Function_3_3D6")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -36690, 0, 63500, 0)

    def lambda_3FD():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3FD)

    def lambda_40F():
        OP_8E(0xFE, 0xFFFF6E10, 0x0, 0x10928, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_40F)
    WaitChrThread(0xFE, 0x1)
    WaitChrThread(0xFE, 0x2)
    Return()

    # Function_3_3D6 end

    def Function_4_42F(): pass

    label("Function_4_42F")

    Sleep(800)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -36690, 0, 63500, 0)

    def lambda_45B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_45B)

    def lambda_46D():
        OP_8E(0xFE, 0xFFFF7216, 0x0, 0x10446, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_46D)
    WaitChrThread(0xFE, 0x1)
    WaitChrThread(0xFE, 0x2)
    Return()

    # Function_4_42F end

    def Function_5_48D(): pass

    label("Function_5_48D")

    Sleep(1500)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -36690, 0, 63500, 0)

    def lambda_4B9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4B9)

    def lambda_4CB():
        OP_8E(0xFE, 0xFFFF6E1A, 0x0, 0x10252, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4CB)
    WaitChrThread(0xFE, 0x1)
    WaitChrThread(0xFE, 0x2)
    Return()

    # Function_5_48D end

    SaveToFile()

Try(main)
