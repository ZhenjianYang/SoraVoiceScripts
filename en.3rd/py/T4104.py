from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4104   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4104.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60018",
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
        'Major Vander',                         # 9
        'Target Camera',                        # 10
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
        'ED6_DT27/CH03930 ._CH',             # 00
        'ED6_DT07/CH01560 ._CH',             # 01
        'ED6_DT07/CH01200 ._CH',             # 02
        'ED6_DT07/CH01210 ._CH',             # 03
        'ED6_DT07/CH01220 ._CH',             # 04
        'ED6_DT07/CH01230 ._CH',             # 05
        'ED6_DT07/CH01180 ._CH',             # 06
        'ED6_DT07/CH01490 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT27/CH03930P._CP',             # 00
        'ED6_DT07/CH01560P._CP',             # 01
        'ED6_DT07/CH01200P._CP',             # 02
        'ED6_DT07/CH01210P._CP',             # 03
        'ED6_DT07/CH01220P._CP',             # 04
        'ED6_DT07/CH01230P._CP',             # 05
        'ED6_DT07/CH01180P._CP',             # 06
        'ED6_DT07/CH01490P._CP',             # 07
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C1,
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
        "Function_0_12A",          # 00, 0
        "Function_1_153",          # 01, 1
        "Function_2_160",          # 02, 2
        "Function_3_5D6",          # 03, 3
    )


    def Function_0_12A(): pass

    label("Function_0_12A")

    OP_B1("t4104_n")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_152")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_152")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    Event(0, 2)

    label("loc_152")

    Return()

    # Function_0_12A end

    def Function_1_153(): pass

    label("Function_1_153")

    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    OP_71(0x407, 0x0)
    ExitThread()
    Return()

    # Function_1_153 end

    def Function_2_160(): pass

    label("Function_2_160")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_D2(0x2701D2, 0x2701D7, 0xC)
    OP_D2(0x2702C2, 0x2702CC, 0xD)
    OP_D2(0x2702C2, 0x2702CC, 0xE)
    OP_D2(0x2702D6, 0x2702E0, 0xF)
    OP_D2(0x2702DA, 0x2702E4, 0x10)
    OP_D2(0x2702C4, 0x2702CE, 0x11)
    OP_D2(0x2701D2, 0x2701D7, 0x12)
    OP_D2(0x2701D2, 0x2701D7, 0x13)
    OP_6D(1900, 0, -6140, 0)
    OP_67(0, 9420, -10000, 0)
    OP_6B(3640, 0)
    OP_6C(46000, 0)
    OP_6E(402, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 12)
    SetChrSubChip(0x10, 0)
    SetChrPos(0x10, 1000, 0, -3920, 180)
    SetChrPos(0x10E, 1000, 0, -9220, 0)

    def lambda_230():
        OP_6B(3140, 4000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_230)
    FadeToBright(3000, 0)
    OP_0D()
    WaitChrThread(0x11, 0x0)
    Fade(1000)
    OP_6D(2400, 0, -5760, 0)
    OP_67(0, 5340, -10000, 0)
    OP_6B(3140, 0)
    OP_6C(46000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #0
        0x10,
        (
            "#272F#5PThis will be a one-round duel.\x02\x03",

            "#270FBoth arts and items may be used.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #1
        0x10E,
        "Captain Schwarz",
        (
            "#179F#12PSo this was what you had in mind...\x02\x03",

            "#171FI can't say I feel especially confident about\x01",
            "my chances of defeating a warrior of the\x01",
            "famed Vander family, but I'll certainly try.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x10,
        "#277F#5PHah. There's no need to be so modest.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6B(3040, 0)
    SetChrChipByIndex(0x10, 17)
    SetChrSubChip(0x10, 1)
    OP_22(0x1F9, 0x0, 0x64)
    OP_99(0x10, 0x1, 0x6, 0x7D0)
    Sleep(300)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10E, 15)
    SetChrSubChip(0x10E, 0)
    Sleep(700)

    ChrTalk(    #3
        0x10,
        "#272F#5PWell, Captain...\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #4
        0x10,
        "#271F#5P#4S...let us begin!\x02",
    )

    OP_7C(0x0, 0x12C, 0x64, 0x12C)
    CloseMessageWindow()
    OP_41(0xD, 0x0, 0xFF)
    OP_31(0xD, 0x10, 0x5A)
    OP_31(0xD, 0x5, 0xC8)
    OP_31(0xD, 0xFE, 0x0)
    OP_35(0xD, 0xFFFF)
    OP_34(0xD, 0xFFFF)
    OP_35(0xD, 0x0)
    OP_BB(0xD, 0x6, 0x118)
    OP_37(0xD, 0x7F, 0x0)
    OP_37(0xD, 0x7F, 0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4A), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4DC")
    OP_41(0xD, 0x3E8, 0xFF)
    OP_34(0xD, 0x82)
    OP_34(0xD, 0x83)
    OP_34(0xD, 0x39)
    OP_34(0xD, 0x46)
    OP_34(0xD, 0x47)
    OP_34(0xD, 0x16)
    OP_3E(0x207, 2)
    Jump("loc_5A8")

    label("loc_4DC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4A), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_50D")
    OP_41(0xD, 0x3E8, 0xFF)
    OP_34(0xD, 0x82)
    OP_34(0xD, 0x83)
    OP_34(0xD, 0x39)
    OP_34(0xD, 0x46)
    OP_34(0xD, 0x47)
    OP_34(0xD, 0x16)
    OP_3E(0x207, 2)
    Jump("loc_5A8")

    label("loc_50D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4A), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_557")
    OP_41(0xD, 0x49D, 0xFF)
    OP_41(0xD, 0x146, 0xFF)
    OP_34(0xD, 0x82)
    OP_34(0xD, 0x83)
    OP_34(0xD, 0x39)
    OP_34(0xD, 0x46)
    OP_34(0xD, 0x47)
    OP_34(0xD, 0x16)
    OP_3E(0x207, 3)
    OP_34(0xD, 0x50)
    OP_34(0xD, 0x63)
    OP_34(0xD, 0x58)
    OP_34(0xD, 0x60)
    OP_34(0xD, 0x6C)
    Jump("loc_5A8")

    label("loc_557")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4A), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A8")
    OP_41(0xD, 0x49E, 0xFF)
    OP_41(0xD, 0x146, 0xFF)
    OP_34(0xD, 0x82)
    OP_34(0xD, 0x83)
    OP_34(0xD, 0x39)
    OP_34(0xD, 0x46)
    OP_34(0xD, 0x47)
    OP_34(0xD, 0x16)
    OP_3E(0x207, 3)
    OP_34(0xD, 0x50)
    OP_34(0xD, 0x63)
    OP_34(0xD, 0x58)
    OP_34(0xD, 0x60)
    OP_34(0xD, 0x6C)
    OP_3E(0x1FE, 1)
    OP_3E(0x1FF, 1)

    label("loc_5A8")

    ClearMapFlags(0x10)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0x3BA, 0x300003, 0x0, 0x0, 0xFF)
    SetMapFlags(0x10)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 3)
    Return()

    # Function_2_160 end

    def Function_3_5D6(): pass

    label("Function_3_5D6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_31(0xD, 0xFC, 0x0)
    OP_31(0xD, 0xFE, 0x0)
    OP_1D(0xE)
    OP_6D(2400, 0, -5760, 0)
    OP_67(0, 5340, -10000, 0)
    OP_6B(3240, 0)
    OP_6C(46000, 0)
    OP_6E(262, 0)
    OP_D2(0x2701D2, 0x2701D7, 0xC)
    OP_D2(0x2702C2, 0x2702CC, 0xD)
    OP_D2(0x2702C2, 0x2702CC, 0xE)
    OP_D2(0x2702D6, 0x2702E0, 0xF)
    OP_D2(0x2702DA, 0x2702E4, 0x10)
    OP_D2(0x2701D2, 0x2701D7, 0x11)
    OP_D2(0x2701D2, 0x2701D7, 0x12)
    OP_D2(0x2701D2, 0x2701D7, 0x13)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_68B"),
        (0, "loc_698"),
        (SWITCH_DEFAULT, "loc_6A5"),
    )


    label("loc_68B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6A5")

    label("loc_698")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6A5")

    label("loc_6A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6DD")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "◆Won\x01",       # 0
            "◆Lost\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)

    label("loc_6DD")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_6EE"),
        (0, "loc_72C"),
        (SWITCH_DEFAULT, "loc_76A"),
    )


    label("loc_6EE")

    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 14)
    SetChrSubChip(0x10, 0)
    SetChrPos(0x10, 1000, 0, -3920, 180)
    SetChrPos(0x10E, 1000, 0, -9220, 0)
    SetChrChipByIndex(0x10E, 16)
    SetChrSubChip(0x10E, 3)
    Jump("loc_76A")

    label("loc_72C")

    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 14)
    SetChrSubChip(0x10, 0)
    SetChrPos(0x10, 1000, 0, -3920, 180)
    SetChrPos(0x10E, 1000, 0, -9220, 0)
    SetChrChipByIndex(0x10E, 15)
    SetChrSubChip(0x10E, 0)
    Jump("loc_76A")

    label("loc_76A")


    def lambda_770():
        OP_6B(3140, 2000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_770)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x11, 0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_79A"),
        (0, "loc_F4C"),
        (SWITCH_DEFAULT, "loc_18A5"),
    )


    label("loc_79A")


    def lambda_7A0():
        OP_9E(0xFE, 0xA, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10E, 0, lambda_7A0)
    Sleep(1000)

    NpcTalk(    #5
        0x10E,
        "Captain Schwarz",
        (
            "#176F#12P#40W*pant*...*pant*...\x02\x03",

            "#179FUgh... I knew you would be formidable,\x01",
            "but not quite like this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x10,
        "#272F#5PCaptain, may I ask something?\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10, 12)
    SetChrSubChip(0x10, 0)
    OP_0D()
    Sleep(300)

    def lambda_880():
        OP_6D(2400, 0, -6120, 2000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_880)

    def lambda_898():
        OP_8E(0xFE, 0x3E8, 0x0, 0xFFFFE714, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_898)
    WaitChrThread(0x10, 0x1)
    Sleep(500)

    ChrTalk(    #7
        0x10,
        "#270F#5PWhat did you lose by being defeated?\x02",
    )

    CloseMessageWindow()
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x10E, 0xFFFFFED4, 1700, 0x0, 0x1, 0xC8, 0x3)
    Sleep(1000)

    NpcTalk(    #8
        0x10E,
        "Captain Schwarz",
        "#173F#12P...? I'm...not sure I understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x10,
        (
            "#270F#5PThe easiest way to determine the true worth\x01",
            "of something is to imagine how things would\x01",
            "be if you were to lose it.\x02\x03",

            "When you do that, you start to see things for\x01",
            "how they really are beyond simple logic.\x02\x03",

            "#272FImagine you were to vanish from the world,\x01",
            "and yet you still possessed the ability to think.\x02\x03",

            "Would there be anything left lingering on your\x01",
            "mind? Anything that worried you? Something that\x01",
            "you wished you could do?\x02\x03",

            "#277FIf so, that is what you should do most.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #10
        0x10E,
        "Captain Schwarz",
        (
            "#175F#12PThose are excellent questions, Major...\x02\x03",

            "...\x02\x03",

            "#176F(Your Highness...I think I finally know what\x01",
            "to do.)\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Sleep(500)
    Fade(500)
    OP_22(0xD5, 0x0, 0x64)
    OP_99(0x10E, 0x3, 0x2, 0x1F4)
    SetChrChipByIndex(0x10E, 65535)
    SetChrSubChip(0x10E, 0)
    OP_0D()
    Sleep(500)

    NpcTalk(    #11
        0x10E,
        "Captain Schwarz",
        (
            "#179F#12PI cannot thank you enough.\x02\x03",

            "#171FThanks to you, I can finally see the path\x01",
            "I ought to take.\x02\x03",

            "I'll be sure to take all you've taught me\x01",
            "today to heart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10,
        (
            "#275F#5PHaha. Just don't assume I thought of any of\x01",
            "what I've said or done today myself.\x02\x03",

            "I often would cross swords with my uncle to\x01",
            "clear away frustrations from having to deal\x01",
            "with my own insufferable charge.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10)
    Sleep(500)
    OP_8C(0x10, 90, 400)
    Sleep(300)

    ChrTalk(    #13
        0x10,
        (
            "#278F#5P...Well, it's probably about time I thought about\x01",
            "returning to Erebonia.\x02\x03",

            "As much as I hate to admit it, I'm feeling a hint\x01",
            "of concern for his well-being.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #14
        0x10E,
        "Captain Schwarz",
        (
            "#171F#12PHaha... Only a hint?\x02\x03",

            "#179FPlease give my regards to the prince when\x01",
            "you see him, then.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 180, 400)
    Sleep(300)

    ChrTalk(    #15
        0x10,
        (
            "#277F#5PI shall.\x02\x03",

            "And give mine to Princess Klaudia as well.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 0, 500)
    Sleep(300)

    def lambda_F0C():
        OP_6D(2400, 0, -4760, 3000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_F0C)

    def lambda_F24():
        OP_8E(0xFE, 0x3E8, 0x0, 0x15CC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_F24)
    Sleep(300)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Jump("loc_18A5")

    label("loc_F4C")

    Sleep(500)

    NpcTalk(    #16
        0x10E,
        "Captain Schwarz",
        "#176F#12P#40W*pant*...*pant*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x10,
        (
            "#273F#5P...Well, this is a surprise.\x02\x03",

            "#272FI had no idea you were this strong.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #18
        0x10E,
        "Captain Schwarz",
        (
            "#179F#12PHaha. Surely you jest.\x02\x03",

            "#170FI could tell that you were holding back against\x01",
            "me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x10,
        "#278F#5PI only wish I could say that were true.\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10, 12)
    SetChrSubChip(0x10, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #20
        0x10,
        (
            "#277FI'm looking forward to the next chance we have\x01",
            "to do battle now.\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10E, 65535)
    SetChrSubChip(0x10E, 0)
    OP_0D()
    Sleep(500)

    NpcTalk(    #21
        0x10E,
        "Captain Schwarz",
        "#179F#12PI will strive not to let you down.\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10)
    Sleep(500)

    ChrTalk(    #22
        0x10,
        "#272F#5PCaptain...\x02",
    )

    CloseMessageWindow()

    def lambda_117D():
        OP_6D(2400, 0, -6120, 2000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_117D)

    def lambda_1195():
        OP_8E(0xFE, 0x3E8, 0x0, 0xFFFFE714, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1195)
    WaitChrThread(0x10, 0x1)
    Sleep(500)

    ChrTalk(    #23
        0x10,
        (
            "#272F#5PYou said to me that you failed to protect those\x01",
            "you care about most.\x02\x03",

            "#270FWhat did you lose because of that?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10E, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    NpcTalk(    #24
        0x10E,
        "Captain Schwarz",
        "#173F#12P...? I'm...not sure I understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x10,
        (
            "#270F#5PThe easiest way to determine the true worth\x01",
            "of something is to imagine how things would\x01",
            "be if you were to lose it.\x02\x03",

            "When you do that, you start to see things for\x01",
            "how they really are beyond simple logic.\x02\x03",

            "#272FImagine you were to vanish from the world,\x01",
            "and yet you still possessed the ability to think.\x02\x03",

            "Would there be anything left lingering on your\x01",
            "mind? Anything that worried you? Something that\x01",
            "you wished you could do?\x02\x03",

            "#277FIf so, that is what you should do most.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #26
        0x10E,
        "Captain Schwarz",
        (
            "#175F#12PThose are excellent questions, Major...\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10E, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2200)
    OP_63(0x10E)
    Sleep(500)

    NpcTalk(    #27
        0x10E,
        "Captain Schwarz",
        (
            "#176F#12P(Your Highness...I think I finally know what\x01",
            "to do.)\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    NpcTalk(    #28
        0x10E,
        "Captain Schwarz",
        (
            "#179F#12PI cannot thank you enough.\x02\x03",

            "#171FThanks to you, I can finally see the path\x01",
            "I ought to take.\x02\x03",

            "I'll be sure to take all you've taught me\x01",
            "today to heart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x10,
        (
            "#275F#5PHaha. Just don't assume I thought of any of\x01",
            "what I've said or done today myself.\x02\x03",

            "I often would cross swords with my uncle to\x01",
            "clear away frustrations from having to deal\x01",
            "with my own insufferable charge.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10)
    Sleep(500)
    OP_8C(0x10, 90, 400)
    Sleep(500)

    ChrTalk(    #30
        0x10,
        (
            "#278F#5P...Well, it's probably about time I thought about\x01",
            "returning to Erebonia.\x02\x03",

            "As much as I hate to admit it, I'm feeling a hint\x01",
            "of concern for his well-being.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #31
        0x10E,
        "Captain Schwarz",
        (
            "#171F#12PHaha... Only a hint?\x02\x03",

            "#179FPlease give my regards to the prince when\x01",
            "you see him, then.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 180, 400)
    Sleep(300)

    ChrTalk(    #32
        0x10,
        (
            "#277F#5PI shall.\x02\x03",

            "And give mine to Princess Klaudia as well.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 0, 500)
    Sleep(300)

    def lambda_1865():
        OP_6D(2400, 0, -4760, 3000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_1865)

    def lambda_187D():
        OP_8E(0xFE, 0x3E8, 0x0, 0x15CC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_187D)
    Sleep(300)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Jump("loc_18A5")

    label("loc_18A5")

    OP_20(0xFA0)
    OP_21()
    OP_A2(0x2504)
    NewScene("ED6_DT21/T4201   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_5D6 end

    SaveToFile()

Try(main)
