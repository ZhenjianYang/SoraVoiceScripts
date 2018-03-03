from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3221   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3221.x',
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
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Mrs. Mao',                             # 9
        'Addy',                                 # 10
        'Zin',                                  # 11
        'Kilika',                               # 12
        'Ambassador Cochrane',                  # 13
        'Glass',                                # 14
        'Glass',                                # 15
        'Horrace',                              # 16
        'Target Camera',                        # 17
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
        'ED6_DT07/CH02430 ._CH',             # 00
        'ED6_DT07/CH01130 ._CH',             # 01
        'ED6_DT07/CH00073 ._CH',             # 02
        'ED6_DT26/CH20815 ._CH',             # 03
        'ED6_DT27/CH03720 ._CH',             # 04
        'ED6_DT27/CH03723 ._CH',             # 05
        'ED6_DT06/CH20021 ._CH',             # 06
        'ED6_DT07/CH01003 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT07/CH02430P._CP',             # 00
        'ED6_DT07/CH01130P._CP',             # 01
        'ED6_DT07/CH00073P._CP',             # 02
        'ED6_DT26/CH20815P._CP',             # 03
        'ED6_DT27/CH03720P._CP',             # 04
        'ED6_DT27/CH03723P._CP',             # 05
        'ED6_DT06/CH20021P._CP',             # 06
        'ED6_DT07/CH01003P._CP',             # 07
    )

    DeclNpc(
        X                   = 2590,
        Z                   = 250,
        Y                   = 5360,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 8490,
        Z                   = 0,
        Y                   = 340,
        Direction           = 102,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Unknown3            = 327686,
        ChipIndex           = 0x6,
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
        Unknown3            = 327686,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 8760,
        Z                   = 200,
        Y                   = 6600,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x135,
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
        "Function_0_20A",          # 00, 0
        "Function_1_22A",          # 01, 1
        "Function_2_22B",          # 02, 2
        "Function_3_3A8",          # 03, 3
        "Function_4_A36",          # 04, 4
        "Function_5_A78",          # 05, 5
    )


    def Function_0_20A(): pass

    label("Function_0_20A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_229")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 6)), scpexpr(EXPR_END)), "loc_229")
    OP_A3(0x2506)
    SetMapFlags(0x10000000)
    Event(0, 5)

    label("loc_229")

    Return()

    # Function_0_20A end

    def Function_1_22A(): pass

    label("Function_1_22A")

    Return()

    # Function_1_22A end

    def Function_2_22B(): pass

    label("Function_2_22B")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_250")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_392")

    label("loc_250")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_269")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_392")

    label("loc_269")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_282")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_392")

    label("loc_282")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29B")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_392")

    label("loc_29B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B4")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_392")

    label("loc_2B4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CD")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_392")

    label("loc_2CD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E6")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_392")

    label("loc_2E6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FF")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_392")

    label("loc_2FF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_318")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_392")

    label("loc_318")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_331")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_392")

    label("loc_331")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34A")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_392")

    label("loc_34A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_363")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_392")

    label("loc_363")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37C")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_392")

    label("loc_37C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_392")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_392")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3A7")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_392")

    label("loc_3A7")

    Return()

    # Function_2_22B end

    def Function_3_3A8(): pass

    label("Function_3_3A8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x13, 0x4)
    SetChrFlags(0x12, 0x4)
    SetChrFlags(0x14, 0x4)
    SetChrPos(0x13, 13110, 200, 10890, 180)
    SetChrPos(0x12, 11150, 100, 10870, 125)
    SetChrPos(0x14, 13070, 200, 8320, 0)
    SetChrChipByIndex(0x14, 5)
    SetChrSubChip(0x14, 0)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x15, 0x4)
    SetChrFlags(0x16, 0x4)
    SetChrPos(0x15, 13250, 800, 9750, 0)
    SetChrPos(0x16, 13300, 800, 8900, 0)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    OP_43(0x10, 0x0, 0x0, 0x2)
    OP_43(0x11, 0x0, 0x0, 0x2)
    OP_6D(-990, 0, 1560, 0)
    OP_67(0, 6700, -10000, 0)
    OP_6B(2580, 0)
    OP_6C(315000, 0)
    OP_6E(326, 0)

    def lambda_4B9():
        OP_6D(11060, 250, 11320, 4000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_4B9)

    def lambda_4D1():
        OP_67(0, 3930, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4D1)

    def lambda_4E9():
        OP_6B(2470, 4000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_4E9)

    def lambda_4F9():
        OP_6E(333, 4000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_4F9)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x0, 0x0)
    Sleep(500)

    ChrTalk(    #0
        0x12,
        (
            "#070F#5PAn intelligence division in Calvard?\x02\x03",

            "Really?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x14,
        (
            "#1110F#6PIt's going to be established quite soon, under \x01",
            "the guidance of the president.\x02\x03",

            "It's become known as the Rocksmith Agency.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x12,
        "#070F#5PHmm... Well, it's appropriate, at least.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x13,
        "#790F#2PThen I presume the reason you're here...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x14,
        (
            "#1110F#6PLikely so.\x02\x03",

            "The president would like you to join this new\x01",
            "agency and work in, and for the good of, the\x01",
            "Republic.\x02\x03",

            "You'll be given an important post, too.\x02\x03",

            "You've proven yourself to have spectacular \x01",
            "information handling and analytical skills\x01",
            "in your position at the guild...\x02\x03",

            "So I can hardly think of a more fitting place\x01",
            "for you to put those skills to use.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x13, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    SetChrSubChip(0x12, 1)
    Sleep(200)

    ChrTalk(    #5
        0x12,
        "#070F#5PUmm... Kilika...\x02",
    )

    CloseMessageWindow()
    OP_63(0x13)
    Sleep(100)
    SetChrSubChip(0x13, 2)
    Sleep(200)

    ChrTalk(    #6
        0x13,
        "#790F#4PDon't worry. I'm listening.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x14,
        (
            "#1110FHaha. It's quite rare that you find it difficult\x01",
            "to make quick judgments, but I suppose no one can\x01",
            "fault you this time.\x02\x03",

            "I won't rush you. Take a night to think long and\x01",
            "hard about it.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x13, 0)
    Sleep(200)
    SetChrSubChip(0x12, 0)
    Sleep(300)
    Fade(300)
    SetChrChipByIndex(0x14, 4)
    SetChrSubChip(0x14, 0)
    SetChrPos(0x14, 12150, 0, 8230, 0)
    OP_6D(10700, 0, 11350, 1000)
    OP_0D()

    ChrTalk(    #8
        0x14,
        (
            "#1110F#6PI'll ask you for your answer again tomorrow.\x02\x03",

            "I'm looking forward to hearing it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x13,
        (
            "#790F#2P...Thank you.\x02\x03",

            "I'll give it some thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x14,
        "#1110F#6PWell, a good night to you both.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_43(0x14, 0x1, 0x0, 0x4)
    Sleep(1500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_20(0x7D0)
    Sleep(2000)
    OP_A2(0x2507)
    NewScene("ED6_DT21/T3201   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_3A8 end

    def Function_4_A36(): pass

    label("Function_4_A36")

    Sleep(300)
    OP_8E(0xFE, 0x283C, 0x0, 0x1CB6, 0x7D0, 0x0)
    OP_8E(0xFE, 0x1B3A, 0xFA, 0x29C2, 0x7D0, 0x0)
    OP_8E(0xFE, 0x15A4, 0xFA, 0x2A1C, 0x7D0, 0x0)
    Return()

    # Function_4_A36 end

    def Function_5_A78(): pass

    label("Function_5_A78")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x13, 0x4)
    SetChrFlags(0x12, 0x4)
    SetChrFlags(0x14, 0x4)
    SetChrPos(0x13, 13110, 200, 10890, 180)
    SetChrPos(0x12, 11150, 100, 10870, 125)
    SetChrPos(0x14, 13070, 200, 8320, 0)
    SetChrChipByIndex(0x14, 5)
    SetChrSubChip(0x14, 0)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x15, 0x4)
    SetChrFlags(0x16, 0x4)
    SetChrPos(0x15, 13250, 800, 9750, 0)
    SetChrPos(0x16, 13300, 800, 8900, 0)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    OP_43(0x10, 0x0, 0x0, 0x2)
    OP_43(0x11, 0x0, 0x0, 0x2)
    OP_6D(-990, 0, 1560, 0)
    OP_67(0, 6700, -10000, 0)
    OP_6B(2580, 0)
    OP_6C(315000, 0)
    OP_6E(326, 0)

    def lambda_B89():
        OP_6D(11060, 250, 11320, 5000)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_B89)

    def lambda_BA1():
        OP_67(0, 3930, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_BA1)

    def lambda_BB9():
        OP_6B(2470, 5000)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_BB9)

    def lambda_BC9():
        OP_6E(333, 5000)
        ExitThread()

    QueueWorkItem(0x18, 3, lambda_BC9)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x18, 0x0)
    Sleep(300)

    ChrTalk(    #11
        0x12,
        (
            "#074F#5PHmm...\x02\x03",

            "#070FSo there's going to be a new intelligence agency\x01",
            "set up in Calvard, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x14,
        (
            "#1110F#6PThat's right. Under the direct guidance of the\x01",
            "president himself.\x02\x03",

            "It's known as the Rocksmith Agency.\x02\x03",

            "...and as the name suggests, it's going to be an\x01",
            "organization that answers directly to him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x12,
        "#073F#5PReally, now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x13,
        (
            "#792F#2P...I see.\x02\x03",

            "#790FI presume that is so that parliament can't have\x01",
            "any influence over its running?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x14,
        (
            "#1111F#6PCorrect.\x02\x03",

            "#1113FPerhaps this new agency's biggest advantage is\x01",
            "that it's separate from parliament, with all of\x01",
            "its issues and vices.\x02\x03",

            "The last thing we need is an organization like\x01",
            "this suffering from parliament's inability to\x01",
            "make prompt decisions or general ineffectuality.\x02\x03",

            "#1110FOr being run in the same opaque and shady manner\x01",
            "by a privileged few as it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x12,
        (
            "#070F#5PHmm... That does sound like a good idea, \x01",
            "I'll admit.\x02\x03",

            "#074FWe're never going to be able to compare to the\x01",
            "Empire's Intelligence Division, or Liberl's old\x01",
            "one, if parliament's at all involved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x14,
        (
            "#1113F#6PQuite.\x02\x03",

            "#1112FIt's very difficult to get anything done in a\x01",
            "nation with such a lack of unity, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x12,
        (
            "#074F#5PI guess that's just the fate of countries that\x01",
            "take in massive amounts of immigrants, though.\x02\x03",

            "#070FHonestly, though, I think the thing that surprises\x01",
            "me the most is that the president's actually being\x01",
            "proactive for once.\x02\x03",

            "He's always struck me as a real conservative, so\x01",
            "this really isn't the kind of thing I thought he\x01",
            "would ever do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x13,
        (
            "#792F#2PThat said, given the state of the Republic right\x01",
            "now, it's hardly surprising that he would choose\x01",
            "to act this way.\x02\x03",

            "Outside our borders, we have the ever-present\x01",
            "hawk faction in the Empire, and inside them,\x01",
            "we have terrorists and extremists...\x02\x03",

            "#790FSomething clearly has to be done, and I think he\x01",
            "knows that as well as anyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x14,
        (
            "#1113F#6PIndeed.\x02\x03",

            "It's clear that in the times ahead of us, we're\x01",
            "going to need to be able to respond flexibly to\x01",
            "a variety of new and unforeseen threats.\x02\x03",

            "#1110F...Regardless, I think my introduction to the\x01",
            "matter has gone on long enough.\x02\x03",

            "I should probably get to the point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x12,
        (
            "#070F#5POh, yeah... You've got something you need to\x01",
            "specifically talk to Kilika about, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x13,
        "#790F#2PI'm guessing the reason you're here...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x14,
        (
            "#1110F#6PI think you're probably right.\x02\x03",

            "#1113FThe president would like you to join this new\x01",
            "agency and work in, and for the good of, the\x01",
            "Republic.\x02\x03",

            "#1112FGiven your skills, I can hardly think of a more\x01",
            "fitting place for you to work.\x02\x03",

            "You'll be given an important post, too, of course.\x02\x03",

            "This is all the will of the president himself,\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x13,
        "#792F#2PI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x12,
        (
            "#075F#5P*sigh* I figured as much...\x02\x03",

            "#070FStill, what led to you being the one to bring\x01",
            "this to Kilika, anyway?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x14,
        (
            "#1111F#6PA fair question, I suppose. Ordinarily, this\x01",
            "would be a scout's work...\x02\x03",

            "#1113FBut I've known the president on a personal\x01",
            "level for quite some time now...\x02\x03",

            "#1110FSo he took it upon himself to ask me to come\x01",
            "to you personally.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x12,
        "#073F#5PI suppose that makes sense...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x13,
        "#790F#2P...So, what's his reason for wanting me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x14,
        (
            "#1110F#6PSurely you know that without asking... Or do you\x01",
            "want to hear it said regardless?\x02\x03",

            "Naturally, your master-class Taito skills are\x01",
            "one reason for you being selected by the\x01",
            "president...\x02\x03",

            "But above all, he wants you for the exceptional \x01",
            "analytical and information handling abilities \x01",
            "you've shown in your position in the guild.\x02\x03",

            "#1111FSurely no further reasons are necessary? You were\x01",
            "practically born to do this job, if you ask me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x13,
        "#792F#2P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x12,
        (
            "#075F#5PStill, you've got some real courage trying to\x01",
            "steal an important member of the guild right\x01",
            "in front of an active bracer.\x02\x03",

            "#070FEspecially given that you were the one who asked\x01",
            "him to be here yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x13,
        (
            "#792F#2P...Well, if she was hoping that you being here\x01",
            "would make me more tempted to accept the offer,\x01",
            "she was very much mistaken.\x02\x03",

            "#790FYou being here will have no influence on my choice\x01",
            "at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x12,
        "#073F#5PUgh... You and your way with words.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x14,
        (
            "#1113F#6P...\x02\x03",

            "#1110FStill... What do you think, Kilika?\x02\x03",

            "I'm not asking for an answer immediately, but \x01",
            "I would like to know what's going through your\x01",
            "mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x13,
        (
            "#792F#2PWell, it's certainly an interesting proposal...\x02\x03",

            "#790FBut I'm not sure I have any reason to accept it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x14,
        (
            "#1113F#6PBut you have no reason to refuse it, either.\x02\x03",

            "#1112FAm I right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x13,
        "#793F#2PW-Well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x12,
        "#074F#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x14,
        (
            "#1110F#6PHaha. It's quite rare that you find it difficult\x01",
            "to make quick judgments, but I suppose no one can\x01",
            "fault you this time.\x02\x03",

            "#1111FI won't rush you. Take a night to think long and\x01",
            "hard about it.\x02\x03",

            "It was so that you could do that I booked a room\x01",
            "here tonight, after all.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x12, 0)
    Sleep(200)
    Fade(500)
    SetChrChipByIndex(0x14, 4)
    SetChrSubChip(0x14, 0)
    SetChrPos(0x14, 12150, 0, 8230, 0)
    OP_6D(10700, 0, 11350, 1000)
    OP_0D()
    Sleep(300)

    ChrTalk(    #40
        0x14,
        (
            "#1110F#6PI'll ask you for your answer again tomorrow.\x02\x03",

            "I'm looking forward to hearing it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x13,
        "#790F#2P...Of course.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x14, 270, 400)
    OP_8C(0x14, 180, 400)
    Sleep(200)
    OP_8E(0x14, 0x3016, 0x0, 0x1CB6, 0x7D0, 0x0)
    TurnDirection(0x14, 0x13, 400)
    Sleep(200)

    ChrTalk(    #42
        0x14,
        (
            "#1113F#6POh, and one more thing before I depart...\x02\x03",

            "#1112F...If you ask me, remaining in your position as\x01",
            "a simple guild receptionist just isn't going to\x01",
            "let you use your abilities to their fullest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x13,
        "#792F#2P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x14,
        "#1111F#6PWell, a good night to you both.\x02",
    )

    CloseMessageWindow()
    OP_43(0x14, 0x1, 0x0, 0x4)
    Sleep(1500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_20(0x7D0)
    Sleep(2000)
    OP_A2(0x2507)
    NewScene("ED6_DT21/T3201   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_A78 end

    SaveToFile()

Try(main)
