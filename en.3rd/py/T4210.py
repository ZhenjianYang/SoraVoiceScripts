from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4210   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4210.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60017",
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
        'Royal Guardsman',                      # 9
        'Royal Guardsman',                      # 10
        'Butler Phillip',                       # 11
        'Duke Dunan',                           # 12
        'Head Maid Hilda',                      # 13
        'Shea',                                 # 14
        'Archbishop Currant',                   # 15
        'Dummy',                                # 16
        'Target Camera',                        # 17
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


    AddCharChip(
        'ED6_DT07/CH01320 ._CH',             # 00
        'ED6_DT07/CH02140 ._CH',             # 01
        'ED6_DT07/CH02470 ._CH',             # 02
        'ED6_DT27/CH03585 ._CH',             # 03
        'ED6_DT06/CH20127 ._CH',             # 04
        'ED6_DT06/CH20129 ._CH',             # 05
        'ED6_DT07/CH02460 ._CH',             # 06
        'ED6_DT07/CH02540 ._CH',             # 07
        'ED6_DT07/CH01400 ._CH',             # 08
    )

    AddCharChipPat(
        'ED6_DT07/CH01320P._CP',             # 00
        'ED6_DT07/CH02140P._CP',             # 01
        'ED6_DT07/CH02470P._CP',             # 02
        'ED6_DT27/CH03585P._CP',             # 03
        'ED6_DT06/CH20127P._CP',             # 04
        'ED6_DT06/CH20129P._CP',             # 05
        'ED6_DT07/CH02460P._CP',             # 06
        'ED6_DT07/CH02540P._CP',             # 07
        'ED6_DT07/CH01400P._CP',             # 08
    )

    DeclNpc(
        X                   = 5000,
        Z                   = 0,
        Y                   = -5000,
        Direction           = 182,
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
        X                   = -5000,
        Z                   = 0,
        Y                   = -5000,
        Direction           = 182,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 1,
        ChipIndex           = 0x1,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Unknown3            = 7,
        ChipIndex           = 0x7,
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
        Unknown3            = 8,
        ChipIndex           = 0x8,
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
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0xC8,
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
        "Function_0_212",          # 00, 0
        "Function_1_248",          # 01, 1
        "Function_2_258",          # 02, 2
        "Function_3_27C",          # 03, 3
        "Function_4_14E0",         # 04, 4
        "Function_5_1561",         # 05, 5
        "Function_6_15A9",         # 06, 6
        "Function_7_15F1",         # 07, 7
        "Function_8_165C",         # 08, 8
        "Function_9_16A4",         # 09, 9
    )


    def Function_0_212(): pass

    label("Function_0_212")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_247")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_234")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    Event(0, 9)
    Jump("loc_247")

    label("loc_234")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_247")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 3)

    label("loc_247")

    Return()

    # Function_0_212 end

    def Function_1_248(): pass

    label("Function_1_248")

    OP_B1("t4210_n")
    OP_71(0x200, 0x0)
    ExitThread()
    Return()

    # Function_1_248 end

    def Function_2_258(): pass

    label("Function_2_258")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_27B")
    OP_8D(0xFE, -1790, 6330, 1580, 2190, 2000)
    Jump("Function_2_258")

    label("loc_27B")

    Return()

    # Function_2_258 end

    def Function_3_27C(): pass

    label("Function_3_27C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(18400, 2500, 5420, 0)
    OP_67(0, 8320, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(90000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 5040, 0, -6080, 0)
    SetChrPos(0x10E, 14140, 4500, 9980, 135)
    OP_43(0x10E, 0x3, 0x0, 0x4)

    def lambda_2FE():
        OP_6D(9800, 0, -5180, 11500)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_2FE)

    def lambda_316():
        OP_67(0, 4059, -10000, 11500)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_316)

    def lambda_32E():
        OP_6B(3000, 11500)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_32E)

    def lambda_33E():
        OP_6C(45000, 11500)
        ExitThread()

    QueueWorkItem(0x18, 3, lambda_33E)
    FadeToBright(2000, 0)
    OP_0D()

    NpcTalk(    #0 op#A op#5
        0x10E,
        "Captain Schwarz",
        (
            "#176F#6P#18A(A promotion...)\x05\x02\x03",

            "#30A(Ordinarily, receiving one would be a cause\x01",
            "for celebration, but for me...)\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)
    OP_62(0x10E, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2400)
    OP_62(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_62(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_421():
        TurnDirection(0xFE, 0x10E, 500)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_421)
    Sleep(50)

    def lambda_434():
        TurnDirection(0xFE, 0x10E, 500)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_434)
    Sleep(500)

    def lambda_447():
        OP_8E(0xFE, 0x1C0C, 0x0, 0xFFFFE278, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_447)
    Sleep(100)

    def lambda_467():
        OP_8E(0xFE, 0x1CD4, 0x0, 0xFFFFE7C8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_467)
    WaitChrThread(0x11, 0x1)

    def lambda_487():
        TurnDirection(0xFE, 0x10E, 500)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_487)
    WaitChrThread(0x10, 0x1)

    def lambda_49A():
        TurnDirection(0xFE, 0x10E, 500)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_49A)
    WaitChrThread(0x10E, 0x3)
    OP_63(0x10E)
    Sleep(300)
    Fade(100)
    SetChrChipByIndex(0x10, 4)
    SetChrSubChip(0x10, 0)
    SetChrChipByIndex(0x11, 4)
    SetChrSubChip(0x11, 0)
    Sleep(300)

    ChrTalk(    #1
        0x10,
        "Good morning, Captain!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x11,
        "Good morning, Captain!\x02",
    )

    CloseMessageWindow()
    Fade(120)
    SetChrChipByIndex(0x11, 0)
    SetChrSubChip(0x11, 0)
    Sleep(150)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)
    Sleep(280)

    ChrTalk(    #3
        0x11,
        "I hear you've been given the rest of the day off.\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #4
        0x10E,
        "Captain Schwarz",
        (
            "#172F#2PTh-That's right, yes...\x02\x03",

            "#170FI'm amazed you already know that when\x01",
            "I was just told myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x11,
        "It's not all that amazing, really.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x10,
        (
            "Leon was trying to make sure everyone knew over\x01",
            "the communications network from Leiston.\x02\x03",

            "I hear Echo appealed directly to Her Majesty, even.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    NpcTalk(    #7
        0x10E,
        "Captain Schwarz",
        (
            "#173F#2P#3SD-Directly?!#2S\x02\x03",

            "#176F(I can't believe it... He did look like he had\x01",
            "something he wanted to say to me the last\x01",
            "time I saw him...)\x02\x03",

            "(What is it with them?!)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x11,
        (
            "*sigh* I still wish we could have helped with\x01",
            "repairing the Arseille, too, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x11,
        (
            "I hear the repairs are running a little behind\x01",
            "schedule, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x11,
        "I wonder how things are going over there?\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #11
        0x10E,
        "Captain Schwarz",
        (
            "#176F#2PYou needn't worry about the Arseille's repairs.\x02\x03",

            "The only reason those three are still there at\x01",
            "Leiston Fortress is that they wouldn't take no\x01",
            "for an answer and insisted on staying.\x02\x03",

            "#170FThe repairs are currently being carried under \x01",
            "Gustav, the maintenance chief from ZCF.\x01",
            "They'll be completed properly.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10E, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x10E)
    Sleep(500)

    NpcTalk(    #12
        0x10E,
        "Captain Schwarz",
        (
            "#176F#2PIncidentally...\x02\x03",

            "#178F...do you know if Her Highness left already?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x10,
        "Y-Yes, in fact...\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 17100, 1750, 4240, 180)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 17500, 1750, 4240, 180)

    NpcTalk(    #14
        0x13,
        "Man's Voice",
        (
            "#4PKlaudia left not that long ago, if you're looking\x01",
            "for her.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A9D():
        OP_6D(12260, 0, -4620, 5500)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_A9D)

    def lambda_AB5():
        OP_6C(36000, 5500)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_AB5)
    OP_43(0x13, 0x3, 0x0, 0x5)
    OP_62(0x10E, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)
    SetChrChipByIndex(0x11, 0)
    SetChrSubChip(0x11, 0)
    Sleep(300)

    def lambda_B1B():

        label("loc_B1B")

        TurnDirection(0xFE, 0x13, 500)
        OP_48()
        Jump("loc_B1B")

    QueueWorkItem2(0x10E, 2, lambda_B1B)
    Sleep(100)

    def lambda_B31():

        label("loc_B31")

        TurnDirection(0xFE, 0x13, 500)
        OP_48()
        Jump("loc_B31")

    QueueWorkItem2(0x10, 2, lambda_B31)

    def lambda_B42():

        label("loc_B42")

        TurnDirection(0xFE, 0x13, 500)
        OP_48()
        Jump("loc_B42")

    QueueWorkItem2(0x11, 2, lambda_B42)
    Sleep(300)
    OP_43(0x12, 0x3, 0x0, 0x6)
    WaitChrThread(0x13, 0x3)
    OP_44(0x10E, 0x2)
    OP_44(0x10, 0x2)
    OP_44(0x11, 0x2)
    Sleep(500)

    ChrTalk(    #15
        0x13,
        (
            "#220F#2PShe's gone to inspect the royal villa.\x02\x03",

            "Were you not aware of this?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #16
        0x10E,
        "Captain Schwarz",
        (
            "#170FYour Grace...\x02\x03",

            "#176FI-I was not...\x02\x03",

            "I would very much have liked to accompany\x01",
            "her over there, if I am truthful...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x13,
        (
            "#220F#2PHmm... I suppose that comes as no surprise.\x02\x03",

            "You always have been one to put yourself forward\x01",
            "to escort her at every opportunity.\x02\x03",

            "I can't say I understand why... Simple escort jobs\x01",
            "are well below your current rank.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #18
        0x10E,
        "Captain Schwarz",
        "#175FI-I suppose so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x13,
        (
            "#225F#2PStill, I'm sure she's well. She has a number\x01",
            "of trustworthy guardsmen with her.\x02\x03",

            "Try not to fret over her too much.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #20
        0x10E,
        "Captain Schwarz",
        (
            "#178F...Of course. You're right.\x02\x03",

            "Thank you, Your Grace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x13,
        (
            "#220F#2PAnd with that, we're leaving, Phillip.\x01",
            "There is work to be done.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_E80():

        label("loc_E80")

        TurnDirection(0xFE, 0x13, 500)
        OP_48()
        Jump("loc_E80")

    QueueWorkItem2(0x10, 2, lambda_E80)

    def lambda_E91():

        label("loc_E91")

        TurnDirection(0xFE, 0x13, 500)
        OP_48()
        Jump("loc_E91")

    QueueWorkItem2(0x11, 2, lambda_E91)

    def lambda_EA2():
        OP_8C(0xFE, 215, 500)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_EA2)
    OP_43(0x13, 0x3, 0x0, 0x7)
    Sleep(500)

    ChrTalk(    #22 op#A
        0x12,
        "#721F#25AAh... Just a moment, Your Grace...\x02",
    )

    CloseMessageWindow()

    def lambda_EED():
        OP_8E(0xFE, 0x300C, 0x0, 0xFFFFE638, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_EED)
    WaitChrThread(0x12, 0x1)

    def lambda_F0D():
        OP_8E(0xFE, 0x2BC0, 0x0, 0xFFFFE638, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_F0D)
    WaitChrThread(0x12, 0x1)
    Sleep(100)

    ChrTalk(    #23
        0x12,
        "#720F#2P(Please, try not to be too downhearted.)\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x13, 0x3)
    OP_44(0x10, 0x2)
    OP_44(0x11, 0x2)
    SetChrPos(0x13, -1020, 0, -11000, 0)

    ChrTalk(    #24
        0x13,
        (
            "#224F#2PWhat are you doing, Phillip? I said that there\x01",
            "is work to be done!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #25
        0x12,
        "#721F#2PM-My apologies.\x02",
    )

    CloseMessageWindow()
    OP_43(0x12, 0x3, 0x0, 0x8)
    Sleep(2000)

    def lambda_1011():
        OP_6D(10860, 0, -4920, 2500)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_1011)
    WaitChrThread(0x18, 0x1)
    OP_62(0x10E, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10E)
    Sleep(500)

    NpcTalk(    #26
        0x10E,
        "Captain Schwarz",
        (
            "#176F#6P*sigh*...\x02\x03",

            "(It looks as though I missed Her Highness\x01",
            "yet again.)\x02\x03",

            "#175F(Still, we're both so busy with our duties that\x01",
            "it's no wonder it keeps happening...)\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10E, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x12, 0x80)

    ChrTalk(    #27
        0x10,
        "#1PIt's incredible how much Duke Dunan's changed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x11,
        (
            "Tell me about it. Apparently, he's often seen in the\x01",
            "administrative room working genuinely hard lately.\x02\x03",

            "He was the one who proposed paying compensation\x01",
            "out a while back, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x10,
        (
            "#1PI always thought of him as a good-for-nothing slob,\x01",
            "but maybe there's more to him than that.\x02\x03",

            "He's finally showing that he shares Her Majesty's\x01",
            "blood after all!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10E)
    Sleep(500)
    OP_62(0x10E, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(700)
    OP_8C(0x10E, 270, 500)
    Sleep(300)

    NpcTalk(    #30
        0x10E,
        "Captain Schwarz",
        "#177F#2PYou're on duty! Enough idle chatter!\x02",
    )

    CloseMessageWindow()

    def lambda_132A():
        OP_8C(0xFE, 90, 600)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_132A)

    def lambda_1338():
        OP_8C(0xFE, 90, 600)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_1338)
    WaitChrThread(0x10, 0x2)
    Sleep(100)

    ChrTalk(    #31
        0x10,
        "#1PM-My apologies, Captain!\x02",
    )


    ChrTalk(    #32
        0x11,
        "M-My apologies, Captain!\x02",
    )

    OP_56(0x1)
    OP_59()

    NpcTalk(    #33
        0x10E,
        "Captain Schwarz",
        (
            "#176F#2P...As you are seemingly aware, I will be absent\x01",
            "from the castle for the remainder of the day.\x02\x03",

            "#170FI expect the two of you to take care of things\x01",
            "here in my absence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x11,
        "Yes, ma'am!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x10,
        "#1PTake care, ma'am!\x02",
    )

    CloseMessageWindow()

    def lambda_147F():

        label("loc_147F")

        TurnDirection(0xFE, 0x10E, 500)
        OP_48()
        Jump("loc_147F")

    QueueWorkItem2(0x10, 2, lambda_147F)

    def lambda_1490():

        label("loc_1490")

        TurnDirection(0xFE, 0x10E, 500)
        OP_48()
        Jump("loc_1490")

    QueueWorkItem2(0x11, 2, lambda_1490)
    OP_8C(0x10E, 180, 400)

    def lambda_14A8():
        OP_8E(0xFE, 0x2580, 0x0, 0xFFFFC694, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_14A8)
    Sleep(300)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0x3E8)
    OP_21()
    OP_A2(0x2505)
    NewScene("ED6_DT21/T4200   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_27C end

    def Function_4_14E0(): pass

    label("Function_4_14E0")


    def lambda_14E6():
        OP_8E(0xFE, 0x4330, 0x8CA, 0x125C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_14E6)
    WaitChrThread(0x10E, 0x1)

    def lambda_1506():
        OP_8E(0xFE, 0x4330, 0x0, 0xFFFFFDA8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_1506)
    WaitChrThread(0x10E, 0x1)

    def lambda_1526():
        OP_8E(0xFE, 0x2BC0, 0x0, 0xFFFFE5FC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_1526)
    WaitChrThread(0x10E, 0x1)

    def lambda_1546():
        OP_8E(0xFE, 0x2580, 0x0, 0xFFFFE5FC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_1546)
    WaitChrThread(0x10E, 0x1)
    Return()

    # Function_4_14E0 end

    def Function_5_1561(): pass

    label("Function_5_1561")


    def lambda_1567():
        OP_8E(0xFE, 0x42CC, 0x0, 0xFFFFFC7C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_1567)
    WaitChrThread(0x13, 0x1)

    def lambda_1587():
        OP_8E(0xFE, 0x2EE0, 0x0, 0xFFFFE890, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_1587)
    WaitChrThread(0x13, 0x1)
    OP_8C(0x13, 270, 500)
    Return()

    # Function_5_1561 end

    def Function_6_15A9(): pass

    label("Function_6_15A9")


    def lambda_15AF():
        OP_8E(0xFE, 0x445C, 0x0, 0xFFFFFC7C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_15AF)
    WaitChrThread(0x12, 0x1)

    def lambda_15CF():
        OP_8E(0xFE, 0x34BC, 0x0, 0xFFFFECDC, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_15CF)
    WaitChrThread(0x12, 0x1)
    OP_8C(0x12, 270, 500)
    Return()

    # Function_6_15A9 end

    def Function_7_15F1(): pass

    label("Function_7_15F1")

    OP_8C(0x13, 215, 500)

    def lambda_15FE():
        OP_8E(0xFE, 0x25F8, 0x0, 0xFFFFDCD8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_15FE)
    WaitChrThread(0x13, 0x1)

    def lambda_161E():
        OP_6D(8900, 0, -5200, 3000)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_161E)

    def lambda_1636():
        OP_8E(0xFE, 0x14, 0x0, 0xFFFFDCD8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_1636)
    WaitChrThread(0x13, 0x1)
    OP_9F(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Return()

    # Function_7_15F1 end

    def Function_8_165C(): pass

    label("Function_8_165C")

    OP_8C(0x12, 215, 500)

    def lambda_1669():
        OP_8E(0xFE, 0x24F4, 0x0, 0xFFFFDCD8, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1669)
    WaitChrThread(0x12, 0x1)

    def lambda_1689():
        OP_8E(0xFE, 0xFFFFFE34, 0x0, 0xFFFFDCD8, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1689)
    WaitChrThread(0x12, 0x1)
    Return()

    # Function_8_165C end

    def Function_9_16A4(): pass

    label("Function_9_16A4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(1300, 0, -17300, 0)
    OP_67(0, 6080, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x10E, 240, 0, -18340, 0)
    SetChrChipByIndex(0x10E, 3)
    SetChrSubChip(0x10E, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x10, 9150, 0, -10190, 225)
    SetChrPos(0x11, 8530, 0, -9330, 225)
    FadeToBright(2000, 0)
    OP_0D()

    NpcTalk(    #36
        0x10E,
        "Captain Schwarz",
        "#175F*pant*...*pant*...\x02",
    )

    CloseMessageWindow()

    def lambda_1771():
        OP_8E(0xFE, 0x5FA, 0x0, 0xFFFFC037, 0x16A8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1771)
    Sleep(100)

    def lambda_1791():
        OP_8E(0xFE, 0x866, 0x0, 0xFFFFBCDA, 0x16A8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1791)
    WaitChrThread(0x11, 0x1)

    ChrTalk(    #37
        0x11,
        "Captain Schwarz!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x10, 0x0)

    ChrTalk(    #38
        0x10,
        "We've locked the castle gates for the time being.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x10,
        "You aren't hurt, are you?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10E, 2)

    NpcTalk(    #40
        0x10E,
        "Captain Schwarz",
        "#172FN-No... I'm fine...\x02",
    )

    CloseMessageWindow()
    OP_59()
    Sleep(100)
    Fade(500)
    SetChrChipByIndex(0x10E, 65535)
    SetChrSubChip(0x10E, 0)
    Sleep(500)
    OP_8C(0x10E, 45, 400)
    Sleep(500)

    NpcTalk(    #41
        0x10E,
        "Captain Schwarz",
        "#178FWhat just happened?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x10,
        "W-Well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x10,
        (
            "...they appear to be some rather...ardent fans\x01",
            "of yours, Captain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x10,
        (
            "You know, we DID have a rather large number\x01",
            "of fan letters arrive at the castle this morning...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x10,
        "I wonder if that could be related to all of this.\x02",
    )

    CloseMessageWindow()
    OP_62(0x10E, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(800)

    NpcTalk(    #46
        0x10E,
        "Captain Schwarz",
        "#174FF-Fan letters...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x11,
        (
            "Apparently, some magazine company put together\x01",
            "a special feature on you yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x11,
        (
            "It was full of information on what you were up to \x01",
            "on that flying city.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10E, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1400)

    ChrTalk(    #49
        0x10,
        "Oh, that reminds me!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x10,
        (
            "A few people who claimed to be from the Liberl\x01",
            "News came here while you were away.\x02\x03",

            "They said they were putting together a feature \x01",
            "to capitalize on your popularity, so they wanted\x01",
            "to gather material for it...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_62(0x10E, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1700)

    NpcTalk(    #51
        0x10E,
        "Captain Schwarz",
        (
            "#176FI-I think I've heard enough...\x02\x03",

            "I can probably fill in the rest myself.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_8C(0x10E, 180, 400)
    Sleep(500)

    NpcTalk(    #52
        0x10E,
        "Captain Schwarz",
        (
            "#178F(Why am I getting this kind of attention?)\x02\x03",

            "#176F(Fan letters? Magazine articles?)\x02\x03",

            "#176F(Why am I being treated like someone special?\x01",
            "I'm not... Not at all...)\x02\x03",

            "(First Her Majesty praising me more than\x01",
            "I deserve, and now this...)\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10E, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10E)
    Sleep(500)

    NpcTalk(    #53
        0x10E,
        "Captain Schwarz",
        (
            "#175F(All I really wanted to do was to protect Her\x01",
            "Highness. That's all...)\x02\x03",

            "(That's what I want to do now, too...but the\x01",
            "opportunity to actually go with her and escort\x01",
            "her rarely seems to present itself anymore.)\x02\x03",

            "#175F(Must I be forced to accept that this is how\x01",
            "things will be going forward?)\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    OP_9F(0x16, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x14, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x16, 220, 0, -6920, 0)
    SetChrPos(0x14, -180, 0, -5280, 180)
    SetChrPos(0x15, 820, 0, -4860, 180)

    def lambda_1EE4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_1EE4)

    def lambda_1EF6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_1EF6)

    def lambda_1F08():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_1F08)

    def lambda_1F1A():
        OP_6D(1420, 0, -4840, 2000)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_1F1A)

    def lambda_1F32():
        OP_67(0, 4780, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_1F32)

    def lambda_1F4A():
        OP_6B(2800, 2000)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_1F4A)
    WaitChrThread(0x18, 0x0)
    Sleep(300)

    ChrTalk(    #54
        0x14,
        "#710F#1PThank you for your time today, Archbishop.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x16,
        (
            "I will conduct mass again tomorrow at eight o'clock.\x01",
            "Could I ask you to pass that on to Her Majesty?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x14,
        "#713F#1PIt would be my pleasure.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x16, 180, 400)

    def lambda_2033():
        OP_6D(1620, 0, -15900, 4000)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_2033)

    def lambda_204B():
        OP_8E(0xFE, 0xDC, 0x0, 0xFFFFC1D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_204B)
    Sleep(200)

    def lambda_206B():
        OP_8E(0xFE, 0xFFFFFF4C, 0x0, 0xFFFFC838, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_206B)

    def lambda_2086():
        OP_8E(0xFE, 0x334, 0x0, 0xFFFFC9DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_2086)
    WaitChrThread(0x14, 0x1)
    OP_62(0x14, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(    #57
        0x14,
        (
            "#712F#1POh, if it isn't Julia... I wasn't expecting to\x01",
            "find you here.\x02\x03",

            "Is something the matter?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10E, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(300)

    def lambda_215D():

        label("loc_215D")

        TurnDirection(0xFE, 0x16, 500)
        OP_48()
        Jump("loc_215D")

    QueueWorkItem2(0x10E, 2, lambda_215D)
    Sleep(100)

    def lambda_2173():
        OP_8C(0xFE, 270, 500)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_2173)
    Sleep(50)

    def lambda_2186():

        label("loc_2186")

        TurnDirection(0xFE, 0x16, 500)
        OP_48()
        Jump("loc_2186")

    QueueWorkItem2(0x11, 2, lambda_2186)
    Sleep(300)

    NpcTalk(    #58
        0x10E,
        "Captain Schwarz",
        (
            "#173FOh, not at all...\x02\x03",

            "#176FAnd good day to you, Archbishop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x16,
        "#5PIt's good to see you again, Julia.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x16,
        (
            "#5PI haven't seen you for some time.\x01",
            "You had me a little concerned.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #61
        0x10E,
        "Captain Schwarz",
        (
            "#178FI-I'm terribly sorry for worrying you.\x02\x03",

            "I'd also like to apologize for not attending\x01",
            "mass at all of late...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x16,
        (
            "#5POh, it's no trouble. I'm well aware of how busy\x01",
            "you are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x16,
        (
            "#5PAll I'll ask of you in the busy times you face\x01",
            "is this: no matter how busy you may become,\x01",
            "you must never lose sight of yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x16,
        "#5PWhat matters to you most is always close at hand.\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #65
        0x10E,
        "Captain Schwarz",
        (
            "#170FThank you, Archbishop. I'll take what you\x01",
            "have said to heart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x16,
        (
            "#5PHaha. Excellent. Now if you'll excuse me,\x01",
            "I should really be on my way.\x02",
        )
    )

    CloseMessageWindow()
    Fade(100)
    SetChrChipByIndex(0x10, 4)
    SetChrSubChip(0x10, 0)
    SetChrChipByIndex(0x11, 4)
    SetChrSubChip(0x11, 0)
    Sleep(300)
    SetChrPos(0x17, 2620, 0, -17500, 0)

    NpcTalk(    #67
        0x17,
        "Royal Guardsman",
        "#2PGood day, Archbishop!\x02",
    )


    ChrTalk(    #68
        0x11,
        "#1PGood day, Archbishop!\x02",
    )

    OP_56(0x1)
    OP_59()

    def lambda_2512():
        OP_6D(1620, 0, -18000, 2000)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_2512)

    def lambda_252A():
        OP_8E(0xFE, 0xDC, 0x0, 0xFFFFA2A4, 0x528, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_252A)
    Sleep(200)

    def lambda_254A():
        OP_8F(0xFE, 0xFFFFFCF4, 0x0, 0xFFFFB85C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_254A)
    WaitChrThread(0x10E, 0x1)

    def lambda_256A():

        label("loc_256A")

        TurnDirection(0xFE, 0x16, 500)
        OP_48()
        Jump("loc_256A")

    QueueWorkItem2(0x10, 2, lambda_256A)
    Sleep(300)
    OP_62(0x10E, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x10E)
    Sleep(700)
    OP_44(0x10E, 0x2)
    OP_62(0x10E, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(300)

    NpcTalk(    #69 op#A op#5
        0x10E,
        "Captain Schwarz",
        (
            "#173F#27A(Actually...there is one way I may be\x01",
            "able to get out of here...)\x05\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_8E(0x10E, 0xFFFFFD1C, 0x0, 0xFFFFB5C8, 0x9C4, 0x0)
    Sleep(300)
    SetMapFlags(0x20)

    NpcTalk(    #70
        0x10E,
        "Captain Schwarz",
        "#178F#5PArchbishop Currant, please wait!\x02",
    )

    OP_7C(0x0, 0x50, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x16, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(800)
    TurnDirection(0x16, 0x10E, 400)

    def lambda_26B0():
        OP_8F(0xFE, 0xFFFFFF88, 0x0, 0xFFFFA8BC, 0x76C, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_26B0)
    Sleep(300)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0xBB8)
    OP_21()
    Sleep(1000)
    OP_A2(0x2506)
    NewScene("ED6_DT21/T4200   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_9_16A4 end

    SaveToFile()

Try(main)
