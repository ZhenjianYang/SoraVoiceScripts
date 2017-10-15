from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'E0013_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/E0013_1 ._SN',
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
        "Function_1_A05",          # 01, 1
        "Function_2_A79",          # 02, 2
        "Function_3_AAB",          # 03, 3
        "Function_4_ADD",          # 04, 4
        "Function_5_B34",          # 05, 5
        "Function_6_BC5",          # 06, 6
        "Function_7_C14",          # 07, 7
        "Function_8_C63",          # 08, 8
        "Function_9_CC3",          # 09, 9
        "Function_10_1964",        # 0A, 10
        "Function_11_19B7",        # 0B, 11
        "Function_12_1A07",        # 0C, 12
        "Function_13_1A5C",        # 0D, 13
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x72), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28B")
    SetChrPos(0x101, 87360, 0, -6520, 0)
    SetChrPos(0x103, 86500, 100, -7110, 0)
    SetChrPos(0xF8, 87360, 100, -7640, 0)
    SetChrPos(0xF9, 86500, 100, -8410, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12B")
    SetChrPos(0xF9, 87360, 100, -7640, 0)
    SetChrPos(0xF8, 86500, 100, -8410, 0)

    label("loc_12B")

    OP_6D(87000, 0, 4940, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(2000, 0)

    def lambda_177():
        OP_6D(87000, 0, -2480, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_177)
    Sleep(400)

    def lambda_194():
        OP_8E(0xFE, 0x15540, 0x0, 0xFFFFF8A8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_194)
    Sleep(1000)

    def lambda_1B4():
        OP_8E(0xFE, 0x151E4, 0x0, 0xFFFFF466, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1B4)
    Sleep(600)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F9")

    def lambda_1E1():
        OP_8E(0xFE, 0x151E4, 0x0, 0xFFFFEEA8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 0, lambda_1E1)
    Jump("loc_214")

    label("loc_1F9")


    def lambda_1FF():
        OP_8E(0xFE, 0x15540, 0x0, 0xFFFFF222, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 0, lambda_1FF)

    label("loc_214")

    Sleep(200)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_244")

    def lambda_22C():
        OP_8E(0xFE, 0x15540, 0x0, 0xFFFFF222, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_22C)
    Jump("loc_25F")

    label("loc_244")


    def lambda_24A():
        OP_8E(0xFE, 0x151E4, 0x0, 0xFFFFEEA8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_24A)

    label("loc_25F")

    WaitChrThread(0x101, 0x0)
    Sleep(400)
    OP_8C(0x101, 90, 400)
    Sleep(400)
    OP_8C(0x101, 315, 400)
    Sleep(800)
    OP_8C(0x101, 0, 400)
    Jump("loc_400")

    label("loc_28B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x71), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34D")
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x103, 0x80)
    SetChrFlags(0xF8, 0x80)
    SetChrFlags(0xF9, 0x80)
    OP_6D(96680, 0, 3000, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(312, 0)
    OP_6F(0x2, 59)
    FadeToBright(2000, 0)

    def lambda_2FE():
        OP_6D(87190, 0, 2230, 8000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2FE)
    Sleep(1500)
    Sleep(400)
    OP_43(0x101, 0x0, 0x1, 0x1)
    Sleep(1000)
    OP_43(0x103, 0x0, 0x1, 0x2)
    Sleep(1000)
    OP_43(0xF8, 0x0, 0x1, 0x3)
    Sleep(600)
    OP_43(0xF9, 0x0, 0x1, 0x4)
    WaitChrThread(0x101, 0x0)
    Jump("loc_400")

    label("loc_34D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_400")
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x103, 0x80)
    SetChrFlags(0xF8, 0x80)
    SetChrFlags(0xF9, 0x80)
    OP_6D(82680, 0, 3000, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(312, 0)
    FadeToBright(2000, 0)

    def lambda_3B9():
        OP_6D(87180, 0, 3000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3B9)
    Sleep(3000)
    OP_43(0x101, 0x0, 0x1, 0x5)
    Sleep(1000)
    OP_43(0x103, 0x0, 0x1, 0x6)
    Sleep(1000)
    OP_43(0xF8, 0x0, 0x1, 0x7)
    Sleep(600)
    OP_43(0xF9, 0x0, 0x1, 0x8)
    WaitChrThread(0x101, 0x0)

    label("loc_400")


    ChrTalk(    #0
        0x101,
        "#1004FWow, it's REALLY dark in here.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_463")

    ChrTalk(    #1
        0x107,
        "#060FYeah, all the lights are out.\x02",
    )

    CloseMessageWindow()
    Jump("loc_56D")

    label("loc_463")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A2")

    ChrTalk(    #2
        0x105,
        "#040FYeah, all the orbal lights are out.\x02",
    )

    CloseMessageWindow()
    Jump("loc_56D")

    label("loc_4A2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_512")

    ChrTalk(    #3
        0x108,
        (
            "#070FWell, none of the orbal lights are\x01",
            "working, and there's no moon out\x01",
            "tonight, either.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56D")

    label("loc_512")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_56D")

    ChrTalk(    #4
        0x104,
        (
            "#030FIndeed. With the lights extinguished,\x01",
            "it's black as ebony in here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_56D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_601")

    ChrTalk(    #5
        0x106,
        (
            "#552FStill, kinda creepy bein' in the middle\x01",
            "of all these rows of empty seats.\x02\x03",

            "Feel like I can hear people talkin'\x01",
            "even now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_751")

    label("loc_601")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_66D")

    ChrTalk(    #6
        0x104,
        (
            "#030FEven in the darkness, however,\x01",
            "I can feel the hum of energy from\x01",
            "the passengers.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_751")

    label("loc_66D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6CD")

    ChrTalk(    #7
        0x108,
        (
            "#070FIt still feels like there are passengers\x01",
            "around in a weird way, huh?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_751")

    label("loc_6CD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_751")

    ChrTalk(    #8
        0x105,
        (
            "#040FDoesn't it kind of feel like there are\x01",
            "still passengers around?\x02\x03",

            "It reminds me of the schoolhouse\x01",
            "at night.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_751")


    ChrTalk(    #9
        0x103,
        (
            "#026FYes, it's a little creepy, to be honest.\x02\x03",

            "Feels like something's waiting to leap\x01",
            "out at us from the dark.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_9E(0x101, 0xA, 0x0, 0x1F4, 0xBB8)
    Sleep(400)

    ChrTalk(    #10
        0x101,
        "#1019FUgh...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_843")

    ChrTalk(    #11
        0x103,
        "#023FOh, still bad with ghost stories?\x02",
    )

    CloseMessageWindow()
    Jump("loc_880")

    label("loc_843")


    ChrTalk(    #12
        0x103,
        (
            "#023FOh? I thought you'd conquered\x01",
            "your fear of ghosts?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_880")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x72), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_896")
    OP_8C(0x101, 180, 400)
    Jump("loc_89D")

    label("loc_896")

    OP_8C(0x101, 0, 400)

    label("loc_89D")


    ChrTalk(    #13
        0x101,
        (
            "#1022FThat's enough ghost talk, thanks!\x02\x03",

            "#1005FC'mon, let's find this freakin' cat\x01",
            "and get out of here!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_936")

    ChrTalk(    #14
        0x108,
        "#070FRight, let's go.\x02",
    )

    CloseMessageWindow()
    Jump("loc_9FC")

    label("loc_936")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_971")

    ChrTalk(    #15
        0x106,
        "#050FSounds like a plan. Let's move.\x02",
    )

    CloseMessageWindow()
    Jump("loc_9FC")

    label("loc_971")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9D3")

    ChrTalk(    #16
        0x104,
        (
            "#030FShall we?\x02\x03",

            "We don't want to keep that poor\x01",
            "maintenance worker waiting.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9FC")

    label("loc_9D3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9FC")

    ChrTalk(    #17
        0x105,
        "#040FRight, let's go.\x02",
    )

    CloseMessageWindow()

    label("loc_9FC")

    OP_28(0x74, 0x1, 0x4000)
    EventEnd(0x0)
    Return()

    # Function_0_AA end

    def Function_1_A05(): pass

    label("Function_1_A05")

    SetChrPos(0xFE, 90790, 100, 2860, 270)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x157A2, 0x0, 0xB2C, 0x7D0, 0x0)
    OP_8E(0xFE, 0x153CE, 0x0, 0x726, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(1000)
    Sleep(400)
    OP_8C(0x101, 270, 400)
    Sleep(800)
    OP_8C(0x101, 135, 400)
    Sleep(800)
    OP_8C(0x101, 180, 400)
    Sleep(1000)
    Return()

    # Function_1_A05 end

    def Function_2_A79(): pass

    label("Function_2_A79")

    SetChrPos(0xFE, 90790, 100, 2860, 270)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x1511C, 0x0, 0xB2C, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_2_A79 end

    def Function_3_AAB(): pass

    label("Function_3_AAB")

    SetChrPos(0xFE, 90790, 100, 2860, 270)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x156D0, 0x0, 0xB2C, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_3_AAB end

    def Function_4_ADD(): pass

    label("Function_4_ADD")

    SetChrPos(0xFE, 90790, 100, 2860, 270)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x15C34, 0x0, 0xB2C, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    OP_72(0x2, 0x800)
    OP_70(0x2, 0x0)
    OP_22(0x7, 0x0, 0x64)
    OP_73(0x2)
    Sleep(1000)
    OP_71(0x2, 0x800)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_4_ADD end

    def Function_5_B34(): pass

    label("Function_5_B34")

    SetChrPos(0xFE, 82560, 100, 2860, 270)
    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_B5B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B5B)
    OP_8E(0xFE, 0x14FD2, 0x0, 0xB2C, 0x7D0, 0x0)
    OP_8E(0xFE, 0x153CE, 0x0, 0x726, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(1000)
    Sleep(400)
    OP_8C(0x101, 270, 400)
    Sleep(800)
    OP_8C(0x101, 135, 400)
    Sleep(800)
    OP_8C(0x101, 180, 400)
    Sleep(1000)
    Return()

    # Function_5_B34 end

    def Function_6_BC5(): pass

    label("Function_6_BC5")

    SetChrPos(0xFE, 82560, 100, 2860, 270)
    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_BEC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BEC)
    OP_8E(0xFE, 0x15694, 0x0, 0xB2C, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_6_BC5 end

    def Function_7_C14(): pass

    label("Function_7_C14")

    SetChrPos(0xFE, 82560, 100, 2860, 270)
    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_C3B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C3B)
    OP_8E(0xFE, 0x150F4, 0x0, 0xB2C, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_7_C14 end

    def Function_8_C63(): pass

    label("Function_8_C63")

    SetChrPos(0xFE, 82560, 100, 2860, 270)
    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_C8A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C8A)
    OP_8E(0xFE, 0x14A8C, 0x0, 0xB2C, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    OP_22(0x7, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_8_C63 end

    def Function_9_CC3(): pass

    label("Function_9_CC3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_CDD")
    Return()

    label("loc_CDD")

    EventBegin(0x0)
    SoundLoad(348)
    Fade(1000)
    OP_6D(30000, 0, 7620, 0)
    OP_67(0, 10620, -10000, 0)
    SetChrPos(0x101, 30000, 0, 5860, 0)
    SetChrPos(0xF7, 29320, 0, 4760, 0)
    SetChrPos(0xF8, 30680, 0, 4760, 0)
    SetChrPos(0xF9, 30000, 0, 3770, 0)
    OP_6D(30270, 0, 6020, 0)
    OP_67(0, 10620, -10000, 0)
    OP_6B(2160, 0)
    OP_6C(59000, 0)
    OP_6E(262, 0)
    OP_0D()
    SetChrPos(0x8, 27420, 400, 10420, 90)
    OP_22(0x192, 0x0, 0x64)

    NpcTalk(    #18
        0x8,
        "Cat Voice",
        "#6PNyaa～go!\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x101)

    ChrTalk(    #19
        0x101,
        "#1004F#4PHey!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E19")

    ChrTalk(    #20
        0x107,
        "#064FThat was a...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_EA8")

    label("loc_E19")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E41")

    ChrTalk(    #21
        0x105,
        "#044FWas that...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_EA8")

    label("loc_E41")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E6C")

    ChrTalk(    #22
        0x104,
        "#033FOh, that was...\x02",
    )

    CloseMessageWindow()
    Jump("loc_EA8")

    label("loc_E6C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EA8")

    ChrTalk(    #23
        0x106,
        (
            "#052FHey, doesn't that sound\x01",
            "like a cat?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EA8")


    def lambda_EAE():
        OP_6D(30000, 0, 7620, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_EAE)

    def lambda_EC6():
        OP_6C(40000, 2000)
        ExitThread()

    QueueWorkItem(0xF7, 3, lambda_EC6)

    def lambda_ED6():
        OP_67(0, 10620, -10000, 2000)
        ExitThread()

    QueueWorkItem(0xF8, 3, lambda_ED6)
    OP_43(0x8, 0x0, 0x1, 0xA)

    def lambda_EF5():
        OP_94(0x1, 0x101, 0x0, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_EF5)
    Sleep(150)

    def lambda_F10():
        OP_94(0x1, 0xF7, 0x0, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_F10)
    Sleep(150)

    def lambda_F2B():
        OP_94(0x1, 0xF8, 0x0, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_F2B)
    Sleep(150)

    def lambda_F46():
        OP_94(0x1, 0xF9, 0x0, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_F46)
    WaitChrThread(0x8, 0x0)
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #24
        0x8,
        "#1PNya～～go.\x02",
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x101, 2)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_F90")
    OP_A2(0x1)

    label("loc_F90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_100E")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Completed 'Lost Kitten'\x01",            # 0
            "Didn't Complete 'Lost Kitten'\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1002"),
        (1, "loc_1008"),
        (SWITCH_DEFAULT, "loc_100E"),
    )


    label("loc_1002")

    OP_A2(0x1)
    Jump("loc_100E")

    label("loc_1008")

    OP_A3(0x1)
    Jump("loc_100E")

    label("loc_100E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1071")

    ChrTalk(    #25
        0x101,
        (
            "#1016F#4PThere you are, Aryll.\x02\x03",

            "Oh, you silly kitty.\x01",
            "You always do stuff like this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10B3")

    label("loc_1071")


    ChrTalk(    #26
        0x101,
        (
            "#1001F#4PFinally found yooou!\x02\x03",

            "I bet you're Aryll, aren'cha?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10B3")


    ChrTalk(    #27
        0x103,
        (
            "#020F#2PWheat-colored fur, just like we'd heard.\x02\x03",

            "This must be our cat.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_113B")

    ChrTalk(    #28
        0x105,
        (
            "#048FThank goodness.\x01",
            "She looks okay.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_126C")

    label("loc_113B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_116D")

    ChrTalk(    #29
        0x107,
        "#561FYay! The kitty's safe!\x02",
    )

    CloseMessageWindow()
    Jump("loc_126C")

    label("loc_116D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11E6")

    ChrTalk(    #30
        0x104,
        (
            "#030FIndeed, she looks to be unharmed.\x02\x03",

            "It's always a relief to find a beloved\x01",
            "pet safe and sound.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_126C")

    label("loc_11E6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_126C")

    ChrTalk(    #31
        0x106,
        (
            "#051FYeah, she looks fine.\x02\x03",

            "Sheesh... Glad that's over.\x01",
            "That was a hell of a lot more\x01",
            "work than I thought it'd be.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_126C")


    ChrTalk(    #32
        0x101,
        (
            "#1015F#4PYou little troublemaker. We ended\x01",
            "up walking all over the place thanks\x01",
            "to you!\x02\x03",

            "What were you doing hiding in here,\x01",
            "anyway?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 0, 400)
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #33
        0x8,
        "#2PMyaon?\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x9, 27420, 400, 10420, 90)
    SetChrPos(0xA, 27420, 400, 10420, 90)
    SetChrPos(0xB, 27420, 400, 10420, 90)
    OP_22(0x15C, 0x0, 0x64)

    ChrTalk(    #34
        0x9,
        "Mya～u!\x02",
    )

    CloseMessageWindow()
    OP_22(0x15C, 0x0, 0x64)

    ChrTalk(    #35
        0xA,
        "Mya～u!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x101,
        "#1011F#4PHm...?\x02",
    )

    CloseMessageWindow()

    def lambda_1383():
        OP_6D(30000, 0, 7000, 2000)
        ExitThread()

    QueueWorkItem(0xF6, 3, lambda_1383)

    def lambda_139B():
        OP_6B(2350, 2000)
        ExitThread()

    QueueWorkItem(0xF9, 3, lambda_139B)

    def lambda_13AB():
        OP_6C(0, 2000)
        ExitThread()

    QueueWorkItem(0xF7, 3, lambda_13AB)

    def lambda_13BB():
        OP_67(0, 10680, -10000, 2000)
        ExitThread()

    QueueWorkItem(0xF8, 3, lambda_13BB)
    OP_43(0x9, 0x0, 0x1, 0xB)
    OP_43(0xA, 0x0, 0x1, 0xC)
    OP_43(0xB, 0x0, 0x1, 0xD)
    Sleep(3000)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_143C")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_147A")

    label("loc_143C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1463")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_147A")

    label("loc_1463")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_147A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14A1")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_14DF")

    label("loc_14A1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14C8")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_14DF")

    label("loc_14C8")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_14DF")


    ChrTalk(    #37
        0x101,
        "#1004F#6PWH-WHAAAAAA?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1525")

    ChrTalk(    #38
        0x107,
        "#065FK-Kittens...?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_15B7")

    label("loc_1525")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_154A")

    ChrTalk(    #39
        0x105,
        "#044FKittens?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_15B7")

    label("loc_154A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_157A")

    ChrTalk(    #40
        0x104,
        "#031FAn unexpected twist!\x02",
    )

    CloseMessageWindow()
    Jump("loc_15B7")

    label("loc_157A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15B7")

    ChrTalk(    #41
        0x106,
        "#052FOkay, I did not see that one coming.\x02",
    )

    CloseMessageWindow()

    label("loc_15B7")

    WaitChrThread(0xB, 0x0)

    ChrTalk(    #42
        0x103,
        (
            "#021FWell, aren't they adorable! ㈱\x01",
            "They look like newborns, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        "#1015FS-So she gave birth to them here?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16D6")

    ChrTalk(    #44
        0x108,
        (
            "#070FYeah, that must be why she snuck\x01",
            "off.\x02\x03",

            "Must've taken a lot of work to find a\x01",
            "safe enough place to give birth. This is\x01",
            "one tough cat momma!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18B2")

    label("loc_16D6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_179E")

    ChrTalk(    #45
        0x106,
        (
            "#051FThinkin' about it, yeah, that's probably\x01",
            "why she came here.\x02\x03",

            "Cats like safe, out-of-the-way places for\x01",
            "givin' birth. Man, you want to talk about\x01",
            "a mother's determination...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18B2")

    label("loc_179E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1819")

    ChrTalk(    #46
        0x105,
        (
            "#047FActually, that makes a lot of sense.\x02\x03",

            "She was trying to find the safest place\x01",
            "for her children.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18B2")

    label("loc_1819")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18B2")

    ChrTalk(    #47
        0x107,
        (
            "#060FMaybe that's why she snuck away?\x01",
            "She was looking for a safe place for\x01",
            "the kittens.\x02\x03",

            "#067FEven cats can be great mommies,\x01",
            "heehee.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18B2")


    ChrTalk(    #48
        0x101,
        (
            "#1007F#6PYeah, but did she have to get\x01",
            "on the ship?\x02\x03",

            "#1000FWell, whatever. Let's go report.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x103,
        (
            "#021FYes, let's.\x02\x03",

            "I'm sure Ida will be quite happy!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T0136   ._SN", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_9_CC3 end

    def Function_10_1964(): pass

    label("Function_10_1964")

    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0x724C, 0xC8, 0x28B4, 0xBB8, 0x0)
    OP_8E(0xFE, 0x7530, 0x0, 0x24CC, 0xBB8, 0x0)
    OP_8E(0xFE, 0x7530, 0x0, 0x1F54, 0x3E8, 0x0)
    OP_8C(0xFE, 180, 400)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_10_1964 end

    def Function_11_19B7(): pass

    label("Function_11_19B7")

    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0x724C, 0xC8, 0x28B4, 0x3E8, 0x0)
    OP_8E(0xFE, 0x767A, 0x0, 0x22E2, 0x3E8, 0x0)
    OP_43(0x9, 0x2, 0x0, 0x2)
    TurnDirection(0xFE, 0x8, 400)
    ClearChrFlags(0xFE, 0x4)
    OP_A6(0x0)
    OP_43(0x9, 0x1, 0x0, 0x3)
    Return()

    # Function_11_19B7 end

    def Function_12_1A07(): pass

    label("Function_12_1A07")

    Sleep(1500)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0x724C, 0xC8, 0x28B4, 0x3E8, 0x0)
    OP_8E(0xFE, 0x73E6, 0x0, 0x23DC, 0x3E8, 0x0)
    OP_43(0xA, 0x2, 0x0, 0x2)
    TurnDirection(0xFE, 0x8, 400)
    ClearChrFlags(0xFE, 0x4)
    OP_A6(0x0)
    OP_43(0xA, 0x1, 0x0, 0x3)
    Return()

    # Function_12_1A07 end

    def Function_13_1A5C(): pass

    label("Function_13_1A5C")

    Sleep(3000)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0x724C, 0xC8, 0x28B4, 0x3E8, 0x0)
    OP_8E(0xFE, 0x751C, 0x0, 0x25F8, 0x3E8, 0x0)
    OP_43(0xB, 0x2, 0x0, 0x2)
    TurnDirection(0xFE, 0x8, 400)
    ClearChrFlags(0xFE, 0x4)
    OP_A2(0x0)
    OP_43(0xB, 0x1, 0x0, 0x3)
    Return()

    # Function_13_1A5C end

    SaveToFile()

Try(main)
