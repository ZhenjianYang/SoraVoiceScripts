from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'T0135   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0135.x',
        MapIndex            = 7,
        MapDefaultBGM       = "ed60084",
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
        'Olivier',                              # 10
        'Aina',                                 # 11
        'Faulkner',                             # 12
        'Food',                                 # 13
        'Food',                                 # 14
        'Wine Bottle',                          # 15
        'Wine Bottle',                          # 16
        'Glass',                                # 17
        'Glass',                                # 18
        'Glass',                                # 19
        'Glass',                                # 20
        'Glass',                                # 21
        'Target Camera',                        # 22
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
        'ED6_DT07/CH00033 ._CH',             # 01
        'ED6_DT07/CH02560 ._CH',             # 02
        'ED6_DT07/CH01270 ._CH',             # 03
        'ED6_DT06/CH20049 ._CH',             # 04
        'ED6_DT06/CH20020 ._CH',             # 05
        'ED6_DT06/CH20021 ._CH',             # 06
        'ED6_DT07/CH00020 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT07/CH00023P._CP',             # 00
        'ED6_DT07/CH00033P._CP',             # 01
        'ED6_DT07/CH02560P._CP',             # 02
        'ED6_DT07/CH01270P._CP',             # 03
        'ED6_DT06/CH20049P._CP',             # 04
        'ED6_DT06/CH20020P._CP',             # 05
        'ED6_DT06/CH20021P._CP',             # 06
        'ED6_DT07/CH00020P._CP',             # 07
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

    DeclNpc(
        X                   = 34500,
        Z                   = 0,
        Y                   = 75200,
        Direction           = 90,
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
        X                   = 40550,
        Z                   = 700,
        Y                   = 66950,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 65541,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 39700,
        Z                   = 700,
        Y                   = 67470,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 262149,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 39300,
        Z                   = 700,
        Y                   = 67950,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1835013,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 39100,
        Z                   = 700,
        Y                   = 67050,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1966085,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 38900,
        Z                   = 700,
        Y                   = 68000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1835013,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 40550,
        Z                   = 700,
        Y                   = 68000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1835013,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 38950,
        Z                   = 600,
        Y                   = 67600,
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
        X                   = 40150,
        Z                   = 600,
        Y                   = 67950,
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
        X                   = 40100,
        Z                   = 600,
        Y                   = 66800,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 65542,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_2AA",          # 00, 0
        "Function_1_2C0",          # 01, 1
        "Function_2_2C1",          # 02, 2
        "Function_3_D9A",          # 03, 3
        "Function_4_DE2",          # 04, 4
        "Function_5_E4A",          # 05, 5
        "Function_6_E7B",          # 06, 6
        "Function_7_3111",         # 07, 7
        "Function_8_315F",         # 08, 8
        "Function_9_319C",         # 09, 9
        "Function_10_31F9",        # 0A, 10
    )


    def Function_0_2AA(): pass

    label("Function_0_2AA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BF")
    SetMapFlags(0x10000000)
    Event(0, 2)

    label("loc_2BF")

    Return()

    # Function_0_2AA end

    def Function_1_2C0(): pass

    label("Function_1_2C0")

    Return()

    # Function_1_2C0 end

    def Function_2_2C1(): pass

    label("Function_2_2C1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_C4(0x0, 0x20000000)
    SetChrFlags(0x10, 0x4)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 39580, 200, 68570, 180)
    SetChrFlags(0x11, 0x4)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 39710, 200, 66250, 0)
    SetChrFlags(0x12, 0x4)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 38200, 0, 67800, 121)
    SetChrChipByIndex(0x11, 4)
    SetChrSubChip(0x11, 0)
    SetChrFlags(0x11, 0x2)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    OP_6D(37640, 0, 68540, 0)
    OP_67(0, 5060, -10000, 0)
    OP_6B(3160, 0)
    OP_6C(302000, 0)
    OP_6E(286, 0)
    OP_20(0x0)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0 op#5
        "\x07\x00#150WYear 1202 of the Septian Calendar, Rolent...#20W\x05\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_56(0x0)
    Sleep(1500)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    OP_C4(0x1, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(    #1
        "\x07\x00#70W#1S...Scherazard...#40W\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #2
        "\x07\x00#40W#2S...Scherazard!#20W\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    def lambda_463():
        OP_6B(2960, 7000)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_463)
    FadeToBright(3000, 0)
    Sleep(1500)

    ChrTalk(    #3
        0x10,
        "#026F...Mm?\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_0D()

    def lambda_494():
        OP_9E(0xFE, 0xF, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_494)
    Sleep(1000)
    SetChrSubChip(0x10, 1)
    Sleep(800)
    SetChrSubChip(0x10, 0)
    Sleep(100)
    SetChrSubChip(0x10, 2)
    Sleep(800)
    SetChrSubChip(0x10, 0)
    Sleep(100)
    WaitChrThread(0x1D, 0x0)
    Sleep(500)

    ChrTalk(    #4
        0x10,
        "#029FHuh? ...Where am I?\x02",
    )

    CloseMessageWindow()
    OP_1D(0xBF)
    Sleep(500)

    ChrTalk(    #5
        0x12,
        (
            "#743F#5PYou feeling all right? Sure you haven't had too \x01",
            "much to drink?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x10,
        (
            "#025FBoy, that dream really brought back memories...\x02\x03",

            "Hard to believe I was once that young...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x12,
        (
            "#741F#5PHeehee. I see you've gotten yourself nice and\x01",
            "plastered.\x02\x03",

            "#740FYou might want to watch what you're saying,\x01",
            "though. You're still young, but no one'll believe\x01",
            "it if you start talking like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x11,
        "#038F#100WSh-She's...riiight... Scheraaaaaa...\x02",
    )

    CloseMessageWindow()
    OP_9E(0x11, 0x14, 0x0, 0x1F4, 0x7D0)
    Sleep(500)
    OP_9E(0x11, 0x14, 0x0, 0x1F4, 0xBB8)
    Sleep(1000)
    Fade(500)
    SetChrChipByIndex(0x11, 1)
    ClearChrFlags(0x11, 0x2)
    Sleep(500)

    ChrTalk(    #9
        0x11,
        "#038F#60WI-I-I-I... I-I...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x12,
        (
            "#743F#5PWow. I thought you'd be out for a while longer,\x01",
            "Olivier.\x02\x03",

            "#741FHeehee. Let me pour you another glass, then.\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_22(0xF9, 0x0, 0x64)
    Fade(1000)
    SetChrSubChip(0x1C, 5)
    OP_0D()
    Sleep(300)

    def lambda_7AF():
        OP_9E(0x11, 0xF, 0x0, 0x5DC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_7AF)

    ChrTalk(    #11
        0x11,
        "#036F#100WP-Pleeease...#20W Mercyyyyyy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10,
        "#026FYou can be such a monster.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    SetChrSubChip(0x10, 2)
    Sleep(500)

    ChrTalk(    #13
        0x10,
        "#520FFaulkner, bring Olivier another bottle over!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(500)

    def lambda_879():
        OP_9E(0x11, 0xF, 0x0, 0x5DC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_879)

    ChrTalk(    #14
        0x11,
        "#038F#60W*unintelligible gibberish*\x02",
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(    #15
        0x10,
        (
            "#029FUgh... Looks like Faulkner's gone and left\x01",
            "early again.\x02\x03",

            "Fine. Guess I'll have to go get the bottle myself.\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x11, 0x1, 0x0, 0x5)
    OP_59()
    Sleep(300)
    Fade(800)
    SetChrChipByIndex(0x10, 7)
    SetChrSubChip(0x10, 0)
    SetChrPos(0x10, 38560, 0, 68740, 270)
    OP_22(0x1A, 0x0, 0x64)
    OP_0D()

    def lambda_96A():
        OP_6D(35620, 0, 70400, 6000)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_96A)
    OP_43(0x10, 0x1, 0x0, 0x3)
    Sleep(500)

    ChrTalk(    #16
        0x10,
        (
            "#520F#12PWell, if I'm getting out of my seat, I'm getting\x01",
            "the strongest thing in the house!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    WaitChrThread(0x10, 0x1)
    WaitChrThread(0x1D, 0x0)

    ChrTalk(    #17
        0x10,
        "#521FI spy some brandy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x12,
        (
            "#741F#1PScherazard, he's literally only just gotten up.\x02\x03",

            "At least start him off on some fruit wine before\x01",
            "you start bringing out the big guns.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x10,
        "#520FHe can have both! Problem solved.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x11,
        "#038F#40W#3PSpare meee... I'll dieeeeee...\x02",
    )

    CloseMessageWindow()

    def lambda_B0B():
        OP_6D(37640, 0, 68540, 6000)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_B0B)
    OP_43(0x10, 0x1, 0x0, 0x4)
    Sleep(1000)

    ChrTalk(    #21
        0x10,
        "#026FBy the way, Aina...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    WaitChrThread(0x10, 0x1)
    WaitChrThread(0x1D, 0x0)
    Sleep(300)

    ChrTalk(    #22
        0x10,
        (
            "#027FYou remember when we first met?\x01",
            "How much did you down again?\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    OP_22(0x82, 0x0, 0x64)
    OP_0D()
    Sleep(500)
    OP_44(0x11, 0x1)

    ChrTalk(    #23
        0x12,
        "#743F#11PDown? Down what?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x10,
        "#521FBooze! We're talkin' booze, baby!\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_22(0x172, 0x0, 0x64)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #25
        "\x07\x05Scherazard began pouring alcohol onto Olivier's head.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_22(0xF9, 0x0, 0x64)
    OP_44(0x11, 0xFF)

    def lambda_C72():
        OP_9E(0xFE, 0x19, 0x0, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_C72)

    def lambda_C8C():
        OP_9F(0xFE, 0xFF, 0x0, 0x0, 0xFF, 0x7D0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_C8C)
    Sleep(2300)

    ChrTalk(    #26
        0x12,
        "#741F#11PThat should go in his mouth, Scherazard.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x10,
        (
            "#029FYou schwaaa...?\x02\x03",

            "Oh... Silly me.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D05():
        OP_9E(0xFE, 0x14, 0x0, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_D05)
    Sleep(800)

    ChrTalk(    #28
        0x11,
        "#038FEeeeeeek... Glaaargh...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0x20C, 0x0, 0x64)
    Fade(500)
    SetChrChipByIndex(0x11, 4)
    SetChrFlags(0x11, 0x2)
    Sleep(500)

    def lambda_D64():
        OP_6B(2760, 4000)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_D64)
    Sleep(500)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0xBB8)
    OP_21()
    OP_44(0x1D, 0x0)
    Sleep(1000)
    OP_A2(0x2505)
    NewScene("ED6_DT21/T4100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_2C1 end

    def Function_3_D9A(): pass

    label("Function_3_D9A")


    def lambda_DA0():
        OP_8E(0xFE, 0x8318, 0x0, 0x10D60, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_DA0)
    WaitChrThread(0x10, 0x0)

    def lambda_DC0():
        OP_8E(0xFE, 0x83B8, 0x0, 0x12250, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_DC0)
    WaitChrThread(0x10, 0x0)
    OP_8C(0x10, 270, 500)
    Return()

    # Function_3_D9A end

    def Function_4_DE2(): pass

    label("Function_4_DE2")


    def lambda_DE8():
        OP_8E(0xFE, 0x8318, 0x0, 0x10D60, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_DE8)
    WaitChrThread(0x10, 0x0)

    def lambda_E08():
        OP_8E(0xFE, 0x8D18, 0x0, 0x1093C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_E08)
    WaitChrThread(0x10, 0x0)

    def lambda_E28():
        OP_8E(0xFE, 0x9664, 0x0, 0x102E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_E28)
    WaitChrThread(0x10, 0x0)
    OP_8C(0x10, 90, 500)
    Return()

    # Function_4_DE2 end

    def Function_5_E4A(): pass

    label("Function_5_E4A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E7A")
    Sleep(1500)

    def lambda_E5E():
        OP_9E(0x11, 0xF, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_E5E)
    Sleep(1000)
    Jump("Function_5_E4A")

    label("loc_E7A")

    Return()

    # Function_5_E4A end

    def Function_6_E7B(): pass

    label("Function_6_E7B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrFlags(0x10, 0x4)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 39580, 200, 68570, 180)
    SetChrFlags(0x11, 0x4)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 39710, 200, 66250, 0)
    SetChrFlags(0x12, 0x4)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 38200, 0, 67800, 121)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    OP_6D(37640, 0, 68540, 0)
    OP_67(0, 5070, -10000, 0)
    OP_6B(2960, 0)
    OP_6C(302000, 0)
    OP_6E(286, 0)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #29
        0x11,
        (
            "#030FMy... Rolent's cuisine really is exceptional.\x02\x03",

            "It makes perfect use of seasonal ingredients,\x01",
            "too.\x02\x03",

            "If this were Erebonia, you'd be paying a premium\x01",
            "at a three star restaurant for food like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x10,
        "#020F#2PWow. Sounds like you're quite the fan.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x11,
        (
            "#030FHeh. But of course.\x02\x03",

            "I couldn't ask for a more heavenly situation than\x01",
            "the one I find myself in right now.\x02\x03",

            "Sampling fine food and fine drink while \x01",
            "accompanied by the finest women... What\x01",
            "man wouldn't want to swap with me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x12,
        (
            "#740F#5PHaha...\x02\x03",

            "I see the rumors about you were all true.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x10,
        (
            "#020FYou'll want to watch yourself around this one,\x01",
            "Aina.\x02\x03",

            "He really will go after anything that moves.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 2)
    Sleep(200)

    def lambda_11FE():
        OP_6D(35710, 0, 71540, 1000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_11FE)
    WaitChrThread(0x0, 0x0)

    ChrTalk(    #34
        0x10,
        (
            "#020F#6POh, Faulkner!\x02\x03",

            "We're short on wine over here. Bring us another\x01",
            "two or three bottles!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x12,
        (
            "#740F#5POh, and throw in some Cognac, too. Preferably\x01",
            "Erebonian.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x13, 135, 400)

    ChrTalk(    #36
        0x13,
        "#5PR-Right!\x02",
    )

    CloseMessageWindow()
    OP_62(0x13, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x13, 225, 400)
    OP_8E(0x13, 0x8476, 0x0, 0x122D2, 0xBB8, 0x0)
    OP_8E(0x13, 0x8188, 0x0, 0x12228, 0xBB8, 0x0)

    def lambda_131C():
        OP_6D(37640, 0, 68540, 1500)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_131C)
    WaitChrThread(0x0, 0x0)
    Sleep(200)
    OP_62(0x11, 0x0, 1700, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #37
        0x11,
        (
            "#030FW-Wait a second...\x02\x03",

            "Can't we ease ourselves in a bit before going for\x01",
            "the hard stuff?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    SetChrSubChip(0x10, 0)
    Sleep(200)

    ChrTalk(    #38
        0x10,
        (
            "#020F#2PI think we've been taking this a bit TOO easy, if\x01",
            "you ask me.\x02\x03",

            "We've been talking for ages! Time to get drinking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x12,
        (
            "#740F#5PWell, I don't mind going with a slower pace for a\x01",
            "while.\x02\x03",

            "Still...\x02\x03",

            "Your glass is completely empty, Olivier. That just\x01",
            "won't do.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0xF9, 0x0, 0x64)
    Fade(1000)
    SetChrSubChip(0x1C, 5)
    OP_0D()
    Sleep(300)

    ChrTalk(    #40
        0x11,
        "#030FHa...haha... Th-Thank you...\x02",
    )

    CloseMessageWindow()
    OP_43(0x13, 0x0, 0x0, 0xA)
    WaitChrThread(0x13, 0x0)

    ChrTalk(    #41
        0x13,
        "#5PH-Here you go, here's your drinks.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    OP_0D()
    Sleep(300)

    ChrTalk(    #42
        0x12,
        "#740F#2PThanks.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_43(0x13, 0x1, 0x0, 0x9)
    Sleep(300)

    ChrTalk(    #43
        0x12,
        "#740F#5PWant your Cognac on the rocks, Olivier?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x11,
        "#030F#6P...What?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x12,
        (
            "#740F#5PIt wouldn't be fair of us to be forcing you to \x01",
            "drink nothing but wine, after all.\x02\x03",

            "You're Erebonian, after all. I'm guessing you'd\x01",
            "prefer something a lot stronger.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x10,
        (
            "#020F#2PWell, that makes sense.\x02\x03",

            "No wonder you drink slowly if you're used to \x01",
            "stronger drinks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x11,
        (
            "#030F#6P*cough* *cough*\x02\x03",

            "I-Incidentally, Schera...\x02\x03",

            "Do you go back quite some time with this Aina\x01",
            "lady?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x10,
        (
            "#020F#2PYou could say that, yeah.\x02\x03",

            "I've known her since back when I was a junior\x01",
            "bracer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x11,
        (
            "#030F#6POh my... That must be quite some time, then.\x02\x03",

            "Might I ask how you came to meet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x12,
        (
            "#740F#5PIt was six years ago, in Grancel.\x02\x03",

            "I went to the guild to ask for an escort, and\x01",
            "that was when I first ran into her.\x02",
        )
    )

    CloseMessageWindow()
    OP_AD(0x240074, 0x0, 0x0, 0x190)
    Sleep(1000)
    FadeToDark(0, 0, -1)
    SetMessageWindowPos(330, 300, -1, -1)
    SetChrName("Scherazard")

    AnonymousTalk(    #51
        (
            "#020FI just happened to be in the guild at the time,\x01",
            "you see.\x02\x03",

            "I ended up accepting her request, but it really\x01",
            "didn't seem like something worth my time at first.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(80, 320, -1, -1)
    SetChrName("Olivier")

    AnonymousTalk(    #52
        (
            "#030FStill, I can only assume it turned out to be?\x01",
            "Had she gotten herself caught up in some kind\x01",
            "of trouble?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 30, -1, -1)
    SetChrName("Aina")

    AnonymousTalk(    #53
        (
            "#740FI had. My rich grandfather had died of illness,\x01",
            "you see -- and that was the start of it all.\x02\x03",

            "Because he had left his entire fortune to me.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(330, 300, -1, -1)
    SetChrName("Scherazard")

    AnonymousTalk(    #54
        (
            "#020FAfter that, I'm sure you can imagine how it all\x01",
            "went. \x02\x03",

            "One relative after another wanted the mira she had\x01",
            "inherited...\x02\x03",

            "There were even some who tried to invalidate her\x01",
            "right of succession to get it all for themselves.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(80, 320, -1, -1)
    SetChrName("Olivier")

    AnonymousTalk(    #55
        (
            "#030FOh dear. They sound like really despicable \x01",
            "fellows.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 30, -1, -1)
    SetChrName("Aina")

    AnonymousTalk(    #56
        (
            "#740FIn the end, I found myself a few days before my\x01",
            "right of succession was due to expire, with no\x01",
            "one to turn to...\x02\x03",

            "...and that was why I ended up having to rely on\x01",
            "this scary lady here for help.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(330, 300, -1, -1)
    SetChrName("Scherazard")

    AnonymousTalk(    #57
        "#020FOh, that's real nice.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 30, -1, -1)
    SetChrName("Aina")

    AnonymousTalk(    #58
        (
            "#740FYou can't deny you were scary, though.\x02\x03",

            "I mean, it was pretty clear you hated me at first.\x01",
            "You didn't exactly hide it.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(80, 320, -1, -1)
    SetChrName("Olivier")

    AnonymousTalk(    #59
        (
            "#030FOh?\x02\x03",

            "So you weren't quite this friendly at first,\x01",
            "then?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(330, 300, -1, -1)
    SetChrName("Scherazard")

    AnonymousTalk(    #60
        (
            "#020FWell, I was pretty young at the time. I still had\x01",
            "a lot to learn about the world.\x02\x03",

            "...Although I can't deny I started disliking her\x01",
            "the second I found out she was from a rich family.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(80, 320, -1, -1)
    SetChrName("Olivier")

    AnonymousTalk(    #61
        "#030FTh-That's quite some prejudice from you...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(330, 300, -1, -1)
    SetChrName("Scherazard")

    AnonymousTalk(    #62
        (
            "#020FOh, quiet. \x02\x03",

            "Less talking, more drinking, Mr. 'My Glass is\x01",
            "Empty Yet Again.'\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(80, 320, -1, -1)
    SetChrName("Olivier")

    AnonymousTalk(    #63
        (
            "#030FO-Oh, is it? Oh dear...\x02\x03",

            "Worry not, though. I would much rather focus\x01",
            "myself on your story regardless.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(120, 30, -1, -1)
    SetChrName("Aina")

    AnonymousTalk(    #64
        (
            "#740FWhat's a good story without a drink to go with it?\x01",
            "You can have both! *Pouring*\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0xF9, 0x0, 0x64)
    Sleep(1000)
    SetMessageWindowPos(80, 320, -1, -1)
    SetChrName("Olivier")

    AnonymousTalk(    #65
        "#030FA-Aina?!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(120, 30, -1, -1)
    SetChrName("Aina")

    AnonymousTalk(    #66
        "#740FSo... Umm... Where were we?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(80, 320, -1, -1)
    SetChrName("Olivier")

    AnonymousTalk(    #67
        (
            "#030F*Hic* Y-You were telling me about how Schera ended\x01",
            "up taking your request.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(120, 30, -1, -1)
    SetChrName("Aina")

    AnonymousTalk(    #68
        (
            "#740FOh, right.\x02\x03",

            "Anyway, even with Scherazard's help, we ended up\x01",
            "getting chased around the capital by pursuers...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x1F4)
    Sleep(1000)
    OP_AD(0x240075, 0x0, 0x0, 0x190)
    Sleep(1000)
    SetMessageWindowPos(330, 300, -1, -1)
    SetChrName("Scherazard")

    AnonymousTalk(    #69
        (
            "#020FIt was exhausting, to be honest.\x02\x03",

            "But our little rich girl here didn't have a single\x01",
            "complaint to make.\x02\x03",

            "I think that was about when we finally started\x01",
            "opening up to one another a bit.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 30, -1, -1)
    SetChrName("Aina")

    AnonymousTalk(    #70
        (
            "#740FWell, after being together for that long, it was\x01",
            "basically inevitable we'd grow more familiar with\x01",
            "one another before long.\x02\x03",

            "More than anything else, though, you were really\x01",
            "fascinating to me. \x02\x03",

            "You were like no one I'd met before with my \x01",
            "sheltered upbringing, after all.\x02\x03",

            "So while we might not have gotten along very well\x01",
            "at first, we did end up hitting it off. We even\x01",
            "went out for drinks after all was said and done.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(330, 300, -1, -1)
    SetChrName("Scherazard")

    AnonymousTalk(    #71
        (
            "#020FIt was then that we REALLY started hitting it off,\x01",
            "though.\x02\x03",

            "After all, all my prejudices towards you were well\x01",
            "and truly shattered when I saw how she drank.\x02\x03",

            "That was...not a sight I was ever expecting to see\x01",
            "from a rich girl. Not at all.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(80, 320, -1, -1)
    SetChrName("Olivier")

    AnonymousTalk(    #72
        (
            "#030F*Hic* St-Still... *Hic* If you were drinking six\x01",
            "years ago...\x02\x03",

            "Were you even legally allowed to?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(330, 300, -1, -1)
    SetChrName("Scherazard")

    AnonymousTalk(    #73
        (
            "#020F*sigh* Quiet, drunkard.\x02\x03",

            "The most surprising part of all of this is still\x01",
            "yet to come.\x02\x03",

            "That's what she did with all the money after\x01",
            "finally inheriting it -- she donated the lot!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(80, 320, -1, -1)
    SetChrName("Olivier")

    AnonymousTalk(    #74
        "#030FR-Really...?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x1F4)
    Sleep(1000)
    OP_AD(0x240076, 0x0, 0x0, 0x190)
    Sleep(1000)
    SetMessageWindowPos(100, 30, -1, -1)
    SetChrName("Aina")

    AnonymousTalk(    #75
        (
            "#740FYep. I gave it all to Her Majesty's welfare \x01",
            "foundation.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(330, 300, -1, -1)
    SetChrName("Scherazard")

    AnonymousTalk(    #76
        (
            "#020FThen after all that was done, she just looked like\x01",
            "the weight of the world had been lifted from her\x01",
            "shoulders and started talking about finding a job.\x02\x03",

            "After seeing that, I couldn't bring myself to turn\x01",
            "my back on her.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 30, -1, -1)
    SetChrName("Aina")

    AnonymousTalk(    #77
        (
            "#740FSo that was when she introduced me to the guild \x01",
            "and I was able to find work there.\x02\x03",

            "You really were far too good to me.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(330, 300, -1, -1)
    SetChrName("Scherazard")

    AnonymousTalk(    #78
        (
            "#020FIf that's what you think, perhaps you could act a\x01",
            "little more gratefully towards me.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 30, -1, -1)
    SetChrName("Aina")

    AnonymousTalk(    #79
        (
            "#740FI'm paying you back through my work! Isn't that\x01",
            "enough?\x02\x03",

            "By joining you for drinks, too.\x02\x03",

            "I mean, the only people who don't refuse a request\x01",
            "to drink with you are Cassius and I.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(330, 300, -1, -1)
    SetChrName("Scherazard")

    AnonymousTalk(    #80
        (
            "#020FHeehee. Not any more! ㈱\x02\x03",

            "Now we can add our dear friend Olivier to that\x01",
            "list.\x02\x03",

            "Can't we, Olivier? ㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(80, 320, -1, -1)
    SetChrName("Olivier")

    AnonymousTalk(    #81
        "...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrChipByIndex(0x11, 4)
    SetChrSubChip(0x11, 0)
    SetChrFlags(0x11, 0x2)
    OP_AE(0x1F4)
    FadeToBright(1000, 0)
    Sleep(1000)
    OP_0D()

    ChrTalk(    #82
        0x10,
        "#020F#2PO-Olivier?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x12,
        (
            "#740F#5POh dear...\x02\x03",

            "Looks like our dear friend Olivier isn't with us\x01",
            "any more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x10,
        (
            "#020F#2PBut we were only just getting started!\x02\x03",

            "The night is only just beginning!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x10, 7)
    SetChrSubChip(0x10, 0)
    SetChrPos(0x10, 38570, 0, 68740, 180)
    OP_22(0xA4, 0x0, 0x64)
    OP_0D()

    def lambda_2BC9():
        OP_6D(37250, 0, 68190, 2000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_2BC9)
    OP_8C(0x10, 270, 400)
    OP_8E(0x10, 0x915A, 0x0, 0x10D7E, 0xBB8, 0x0)
    OP_8E(0x10, 0x9218, 0x0, 0x10388, 0xBB8, 0x0)
    OP_8E(0x10, 0x974A, 0x0, 0x10310, 0xBB8, 0x0)
    WaitChrThread(0x0, 0x0)

    ChrTalk(    #85
        0x10,
        (
            "#020F#5PStop pretending to be asleep and get back to\x01",
            "drinking, Olivier!\x02\x03",

            "I know you're not really asleep!\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x11, 0x0, 0x0, 0x8)
    Sleep(1000)

    ChrTalk(    #86
        0x11,
        "#030F#6PWh-Wh-What's going on...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x12,
        (
            "#740F#2PUmm... Scherazard... It might not be my place to\x01",
            "say this...\x02\x03",

            "But I think you should probably take better care\x01",
            "of willing drinking partners. They're few and far\x01",
            "between for you.\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x13, 0x0, 0x0, 0x7)
    WaitChrThread(0x13, 0x0)

    ChrTalk(    #88
        0x13,
        "#5PSch-Schera?! What are you doing?!\x02",
    )

    CloseMessageWindow()
    OP_44(0x11, 0x0)
    Sleep(200)
    OP_8C(0x10, 315, 400)
    Sleep(200)

    ChrTalk(    #89
        0x10,
        (
            "#020F#6POh, look who it is! ㈱\x02\x03",

            "You're just in time to join us for a few drinks in\x01",
            "Olivier's place. ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x13,
        "#5PI-I couldn't possibly! I'm working ere!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x10,
        (
            "#020F#6PAww, come oooon... You wouldn't really say no,\x01",
            "would you?\x02\x03",

            "...If you don't join us, I will strip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x13,
        "#5PWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x12,
        "#740F#2P*sigh* Here we go again...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x13, 90, 400)

    ChrTalk(    #94
        0x13,
        "#5PD-Don't just sigh, Aina! Help me here!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x10,
        "#020F#6PBoy... It sure is hot in here... ㈱\x02",
    )

    CloseMessageWindow()
    OP_62(0x13, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x13, 135, 400)
    Sleep(500)

    ChrTalk(    #96
        0x13,
        "#5PE-Eeeek!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x11,
        "#030F#6PGuhh... Guhh...\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(300)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #98
        (
            "\x07\x05Eventually, the night came to an end.\x02\x03",

            "The unfortunate traveler who had found himself \x01",
            "involved in this potentially fatal drinking \x01",
            "session was fortunately able to escape alive...\x02\x03",

            "But the scars the experience left on his psyche\x01",
            "would perhaps never heal.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    OP_20(0x7D0)
    Sleep(2000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E0, 0)), scpexpr(EXPR_END)), "loc_3107")
    NewScene("ED6_DT21/T0001   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_3110")

    label("loc_3107")

    NewScene("ED6_DT21/T7000   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3110")

    Return()

    # Function_6_E7B end

    def Function_7_3111(): pass

    label("Function_7_3111")

    OP_8C(0xFE, 135, 400)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)
    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0x807A, 0x0, 0x10FAE, 0x1388, 0x0)
    OP_8E(0xFE, 0x90CE, 0x0, 0x10716, 0x1388, 0x0)
    Return()

    # Function_7_3111 end

    def Function_8_315F(): pass

    label("Function_8_315F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_319B")
    OP_9E(0xFE, 0x0, 0x1E, 0x1F4, 0xBB8)
    Sleep(1000)
    OP_9E(0xFE, 0x0, 0x1E, 0x1F4, 0xBB8)
    Sleep(1500)
    Jump("Function_8_315F")

    label("loc_319B")

    Return()

    # Function_8_315F end

    def Function_9_319C(): pass

    label("Function_9_319C")

    OP_8C(0xFE, 315, 400)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0xFE, 0x8296, 0x0, 0x1104E, 0x1388, 0x0)
    OP_8E(0xFE, 0x8426, 0x0, 0x12516, 0x1388, 0x0)
    OP_8E(0xFE, 0x86C4, 0x0, 0x125C0, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_9_319C end

    def Function_10_31F9(): pass

    label("Function_10_31F9")

    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0x821E, 0x0, 0x10F04, 0x7D0, 0x0)
    OP_8E(0xFE, 0x947A, 0x0, 0x10590, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_10_31F9 end

    SaveToFile()

Try(main)
