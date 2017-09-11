from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T2710_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'T2710.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60016",
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
    )

    ScpFunction(
        "Function_0_66",           # 00, 0
        "Function_1_442",          # 01, 1
        "Function_2_C97",          # 02, 2
        "Function_3_CB3",          # 03, 3
        "Function_4_CE3",          # 04, 4
        "Function_5_D13",          # 05, 5
        "Function_6_D43",          # 06, 6
        "Function_7_D68",          # 07, 7
        "Function_8_DA1",          # 08, 8
        "Function_9_DEA",          # 09, 9
        "Function_10_E38",         # 0A, 10
        "Function_11_E86",         # 0B, 11
        "Function_12_2DFB",        # 0C, 12
        "Function_13_2E1F",        # 0D, 13
        "Function_14_2E48",        # 0E, 14
        "Function_15_35D6",        # 0F, 15
        "Function_16_3F6B",        # 10, 16
        "Function_17_3FAB",        # 11, 17
        "Function_18_3FCF",        # 12, 18
        "Function_19_3FE9",        # 13, 19
        "Function_20_402B",        # 14, 20
        "Function_21_4053",        # 15, 21
        "Function_22_406F",        # 16, 22
        "Function_23_41E8",        # 17, 23
        "Function_24_48DB",        # 18, 24
        "Function_25_50FE",        # 19, 25
    )


    def Function_0_66(): pass

    label("Function_0_66")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    FadeToBright(2000, 0)
    SetMapFlags(0x400000)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    OP_4A(0xB, 255)
    OP_4A(0xC, 255)
    OP_4A(0xD, 255)
    SetChrPos(0xB, 1596, 0, 12441, 90)
    SetChrPos(0xC, 1513, 0, 13617, 90)
    SetChrPos(0xD, 909, 0, 13169, 90)
    OP_51(0xF, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0xF, 0x0)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #0
        0xB,
        "Hmm... I don't hear anything.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xC,
        "Damn it. What's going on?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xD,
        (
            "Is the Royal Army really\x01",
            "going to just roll over\x01",
            "for some bigwig?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)
    OP_4B(0xB, 255)
    Sleep(50)
    OP_4B(0xC, 255)
    Sleep(70)
    OP_4B(0xD, 255)
    SetChrPos(0x101, -550, 0, 3400, 0)
    SetChrPos(0x102, -1460, 0, 2620, 0)
    SetChrPos(0x105, -1000, 0, 1420, 0)
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)

    def lambda_201():
        OP_94(0x1, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_201)

    def lambda_217():
        OP_94(0x1, 0x1, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_217)

    def lambda_22D():
        OP_94(0x1, 0x2, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_22D)
    OP_6D(-550, 0, 8300, 3000)
    WaitChrThread(0x101, 0x1)
    TurnDirection(0x101, 0xB, 400)
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #3
        0x101,
        (
            "#501F...?\x02\x03",

            "What are they doing?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0xB, 400)
    TurnDirection(0x105, 0xB, 400)

    ChrTalk(    #4
        0x102,
        (
            "#010FBy the looks of them, I'd\x01",
            "say they're just ordinary\x01",
            "travelers...\x02\x03",

            "However...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #5
        0x101,
        "#000FHowever? However what?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x102,
        (
            "#013FI have to wonder why there\x01",
            "isn't a single guard.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x102, 400)

    ChrTalk(    #7
        0x105,
        "#044FNow that you mention it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        (
            "#002FMaybe something big is\x01",
            "going on...?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #9
        0x102,
        (
            "#010FThat, I do not know...\x02\x03",

            "...but I think we should ask\x01",
            "a guard when we find one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x101,
        "#000FSounds good to me.\x02",
    )

    CloseMessageWindow()
    ClearMapFlags(0x400000)
    EventEnd(0x0)
    Return()

    # Function_0_66 end

    def Function_1_442(): pass

    label("Function_1_442")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    FadeToBright(2000, 0)
    SetMapFlags(0x400000)
    RemoveParty(0x1, 0xFF)
    RemoveParty(0x4, 0xFF)
    AddParty(0x4, 0xFF)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xE, 0x80)
    OP_4A(0x8, 255)
    OP_4A(0xE, 255)
    OP_69(0x101, 0x0)
    SetChrPos(0x8, -4000, 0, 4000, 90)
    SetChrPos(0x101, -7000, 1000, 3800, 90)
    SetChrPos(0xE, -7000, 1000, 4900, 90)
    SetChrPos(0x105, -8500, 1000, 5200, 180)
    SetChrPos(0xB, 1596, 0, 12441, 90)
    SetChrPos(0xC, 1513, 0, 13617, 90)
    SetChrPos(0xD, 909, 0, 13169, 90)
    OP_43(0x8, 0x1, 0x1, 0x2)
    OP_43(0x101, 0x1, 0x1, 0x3)
    OP_43(0xE, 0x1, 0x1, 0x4)
    OP_43(0x105, 0x1, 0x1, 0x5)
    OP_6D(-1000, 0, 8700, 4000)
    WaitChrThread(0x105, 0x1)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #11
        0x8,
        (
            "Hmm... There's been little\x01",
            "progress to speak of.\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0xF, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0xF, 0x320)

    ChrTalk(    #12
        0x101,
        (
            "#000FSo, what's with those guys\x01",
            "over there?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5DB():
        TurnDirection(0xE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5DB)

    def lambda_5E9():
        TurnDirection(0x105, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5E9)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #13
        0x8,
        (
            "They're the victims of this\x01",
            "current little issue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        (
            "The traveler in question is\x01",
            "currently in the dining hall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x101,
        "#501FIn the dining hall...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        (
            "Yes, we're hoping that food\x01",
            "will persuade him...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        (
            "...for the sake of the\x01",
            "others here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        (
            "#505FPersuade him...?\x02\x03",

            "#002FOkay, just who is this\x01",
            "troublesome traveler?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        "Well, to be honest...\x02",
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xB, 0x8, 400)
    Sleep(400)

    ChrTalk(    #20
        0xB,
        "Hey!\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_805():
        TurnDirection(0xD, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_805)
    TurnDirection(0xC, 0x8, 400)

    def lambda_81A():

        label("loc_81A")

        TurnDirection(0x8, 0xB, 0)
        OP_48()
        Jump("loc_81A")

    QueueWorkItem2(0x8, 1, lambda_81A)

    def lambda_82B():

        label("loc_82B")

        TurnDirection(0x101, 0xB, 0)
        OP_48()
        Jump("loc_82B")

    QueueWorkItem2(0x101, 1, lambda_82B)

    def lambda_83C():

        label("loc_83C")

        TurnDirection(0xE, 0xB, 0)
        OP_48()
        Jump("loc_83C")

    QueueWorkItem2(0xE, 1, lambda_83C)

    def lambda_84D():

        label("loc_84D")

        TurnDirection(0x105, 0xB, 0)
        OP_48()
        Jump("loc_84D")

    QueueWorkItem2(0x105, 1, lambda_84D)

    def lambda_85E():
        OP_69(0x8, 0x7D0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_85E)
    Sleep(400)
    OP_43(0xC, 0x1, 0x1, 0x6)
    OP_43(0xD, 0x1, 0x1, 0x7)
    OP_8E(0xB, 0x0, 0x0, 0x1C3E, 0xBB8, 0x0)
    OP_44(0x8, 0x1)
    OP_44(0x101, 0x1)
    OP_44(0xE, 0x1)
    OP_44(0x105, 0x1)
    TurnDirection(0xB, 0x8, 400)
    OP_44(0xB, 0xFF)

    ChrTalk(    #21
        0xB,
        (
            "You're in charge here, right?\x01",
            "You have to do something!\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xD, 0x1)

    ChrTalk(    #22
        0xD,
        (
            "Are you just going to let\x01",
            "this kind of bullying go\x01",
            "unchallenged?\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xC, 0x1)

    ChrTalk(    #23
        0xC,
        (
            "The Royal Army is supposed\x01",
            "to be on the side of the\x01",
            "citizens, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xC,
        (
            "If so, then do something\x01",
            "about this!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #25
        0x8,
        "Now, hold on, all of you...\x02",
    )

    CloseMessageWindow()
    OP_8E(0xE, 0xFFFFFD58, 0x0, 0x184C, 0xBB8, 0x0)
    OP_8C(0xE, 0, 400)

    ChrTalk(    #26
        0xE,
        "#012FCalm down, please...\x02",
    )

    CloseMessageWindow()
    OP_8C(0xB, 180, 0)
    OP_8C(0xC, 180, 0)
    OP_8C(0xD, 180, 0)

    def lambda_A31():
        OP_6D(-840, 0, 3830, 1000)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_A31)

    def lambda_A49():
        OP_94(0x1, 0xB, 0x0, 0x3E8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_A49)

    def lambda_A5F():
        OP_94(0x1, 0xC, 0x0, 0x3E8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_A5F)

    def lambda_A75():
        OP_94(0x1, 0xD, 0x0, 0x3E8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_A75)
    OP_62(0xE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_AAF():
        OP_94(0x1, 0xE, 0xB4, 0x3E8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_AAF)

    def lambda_AC5():
        OP_94(0x1, 0x8, 0xB4, 0x3E8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_AC5)
    Sleep(200)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_AF2():
        OP_94(0x1, 0x101, 0xB4, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AF2)

    ChrTalk(    #27
        0xB,
        "#4PI'm sick of being calm!\x02",
    )

    CloseMessageWindow()
    OP_43(0xB, 0x1, 0x1, 0x8)
    OP_43(0xC, 0x1, 0x1, 0x9)
    OP_43(0xD, 0x1, 0x1, 0xA)

    ChrTalk(    #28
        0xE,
        (
            "#014F#6PI understand. Just please,\x01",
            "take a step ba--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x101,
        "#004FJoshua! Are you okay?!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x101, 400)

    ChrTalk(    #30
        0xE,
        (
            "#012FI'm... I'm fine...\x02\x03",

            "For now, I want you two to\x01",
            "check on the dining hall!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xE, 0, 400)

    ChrTalk(    #31
        0x101,
        "#002FO-Okay... We will.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #32
        0x101,
        "#002FCome on, let's go.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #33
        0x105,
        "#043F...All right.\x02",
    )

    CloseMessageWindow()
    OP_4B(0xE, 255)
    OP_4B(0x8, 255)
    OP_43(0xB, 0x0, 0x0, 0x2)
    OP_43(0xC, 0x0, 0x0, 0x2)
    OP_43(0xD, 0x0, 0x0, 0x2)
    OP_43(0xB, 0x1, 0x1, 0x8)
    OP_43(0xC, 0x1, 0x1, 0x9)
    OP_43(0xD, 0x1, 0x1, 0xA)
    SetChrFlags(0x8, 0x10)
    OP_28(0x23, 0x1, 0x1000)
    ClearMapFlags(0x400000)
    EventEnd(0x0)
    Return()

    # Function_1_442 end

    def Function_2_C97(): pass

    label("Function_2_C97")

    OP_8E(0xFE, 0x0, 0x0, 0x186A, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_2_C97 end

    def Function_3_CB3(): pass

    label("Function_3_CB3")

    OP_8E(0xFE, 0xFFFFF510, 0x0, 0xFA0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFDA8, 0x0, 0x12C0, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_3_CB3 end

    def Function_4_CE3(): pass

    label("Function_4_CE3")

    OP_8E(0xFE, 0xFFFFF3B2, 0x0, 0x13EC, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF8F8, 0x0, 0x1770, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_4_CE3 end

    def Function_5_D13(): pass

    label("Function_5_D13")

    OP_8E(0xFE, 0xFFFFE4DA, 0x3E8, 0x10CC, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF682, 0x0, 0x10CC, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_5_D13 end

    def Function_6_D43(): pass

    label("Function_6_D43")

    Sleep(800)
    OP_8E(0xC, 0x29E, 0x0, 0x1B30, 0xBB8, 0x0)
    TurnDirection(0xC, 0x8, 400)
    OP_44(0xC, 0xFF)
    Return()

    # Function_6_D43 end

    def Function_7_D68(): pass

    label("Function_7_D68")

    Sleep(600)
    OP_8E(0xD, 0xFFFFFCE0, 0x0, 0x2954, 0xBB8, 0x0)
    OP_8E(0xD, 0xFFFFFCE0, 0x0, 0x1AE0, 0xBB8, 0x0)
    TurnDirection(0xD, 0x8, 400)
    OP_44(0xD, 0xFF)
    Return()

    # Function_7_D68 end

    def Function_8_DA1(): pass

    label("Function_8_DA1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DE9")
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1400)
    TurnDirection(0xFE, 0x8, 400)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1800)
    TurnDirection(0xFE, 0xE, 400)
    Jump("Function_8_DA1")

    label("loc_DE9")

    Return()

    # Function_8_DA1 end

    def Function_9_DEA(): pass

    label("Function_9_DEA")

    Sleep(400)

    label("loc_DEF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E37")
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1400)
    TurnDirection(0xFE, 0x8, 400)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(2000)
    TurnDirection(0xFE, 0xE, 400)
    Jump("loc_DEF")

    label("loc_E37")

    Return()

    # Function_9_DEA end

    def Function_10_E38(): pass

    label("Function_10_E38")

    Sleep(200)

    label("loc_E3D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E85")
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(2000)
    TurnDirection(0xFE, 0x8, 400)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1400)
    TurnDirection(0xFE, 0xE, 400)
    Jump("loc_E3D")

    label("loc_E85")

    Return()

    # Function_10_E38 end

    def Function_11_E86(): pass

    label("Function_11_E86")

    SetMapFlags(0x400000)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x105, 0x80)
    EventBegin(0x0)
    ClearMapFlags(0x1)
    FadeToBright(2000, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x9, 92630, 0, 12500, 90)
    SetChrPos(0x101, 90630, 0, 10900, 90)
    SetChrPos(0x105, 89630, 0, 10900, 90)
    SetChrPos(0x10, 95380, 0, 12000, 90)
    SetChrPos(0x12, 96610, 0, 12000, 270)
    SetChrPos(0x11, 94280, 0, 11200, 90)
    OP_4A(0x12, 255)
    OP_4A(0x9, 255)
    OP_4A(0xA, 255)
    OP_51(0xF, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0xF, 0x0)
    OP_0D()
    OP_28(0x23, 0x1, 0x2)
    OP_28(0x23, 0x1, 0x4)

    ChrTalk(    #34
        0x12,
        "But, sir...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x12,
        (
            "If you reserve all the rooms\x01",
            "AND the dining hall, what will\x01",
            "I tell the other guests?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x12,
        (
            "Why can't you see where I'm\x01",
            "coming from?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x10, 400)

    ChrTalk(    #37
        0x11,
        (
            "#722FYour Grace, I feel I must\x01",
            "agree with him.\x02\x03",

            "Perhaps we should return to\x01",
            "Ruan, as originally planned?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x11, 400)

    ChrTalk(    #38
        0x10,
        (
            "#222FQuiet, Phillip! I like it here.\x02\x03",

            "#220FParticularly since it has such\x01",
            "a lovely view of Air-Letten's\x01",
            "waterfall.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x12, 400)
    OP_8C(0x11, 90, 0)
    OP_62(0x12, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #39
        0x12,
        "But, sir...\x02",
    )

    CloseMessageWindow()
    OP_43(0x12, 0x1, 0x1, 0xC)
    OP_43(0x10, 0x1, 0x1, 0xD)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x105, 0x80)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x105, 0x40)
    SetChrFlags(0x10, 0x40)
    SetChrFlags(0x11, 0x40)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x1E)
    OP_73(0x1)

    def lambda_117F():
        OP_6D(92630, 0, 11500, 2000)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_117F)

    def lambda_1197():
        OP_94(0x1, 0x105, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1197)
    OP_94(0x1, 0x101, 0x0, 0x7D0, 0x7D0, 0x0)

    def lambda_11BC():
        OP_8E(0x101, 0x169D6, 0x0, 0x2CEC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11BC)
    WaitChrThread(0x105, 0x1)
    OP_8E(0x105, 0x169D6, 0x0, 0x2904, 0x7D0, 0x0)
    TurnDirection(0x101, 0x10, 400)
    OP_8C(0x105, 90, 400)
    OP_72(0x1, 0x800)
    OP_22(0x7, 0x0, 0x64)
    OP_6F(0x1, 30)
    OP_70(0x1, 0x0)
    OP_73(0x1)
    OP_71(0x1, 0x800)
    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #40
        0x101,
        (
            "#004F...Urk.\x01",
            "It HAD to be you, didn't it?\x02\x03",

            "You're that self-centered duke\x01",
            "guy from before!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #41
        0x9,
        "...Hmm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x9,
        (
            "Well, well...If it isn't\x01",
            "the bracers.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_12F5():
        TurnDirection(0x105, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_12F5)
    TurnDirection(0x101, 0x9, 400)

    ChrTalk(    #43
        0x9,
        (
            "You're late. We've been waiting\x01",
            "for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x101,
        (
            "#509FDon't tell me...\x02\x03",

            "THAT'S your troublesome\x01",
            "traveler?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x9,
        "Do you see anyone else here?\x02",
    )

    CloseMessageWindow()

    def lambda_1398():
        OP_8C(0x105, 90, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1398)
    TurnDirection(0x101, 0x10, 400)
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #46
        0x101,
        (
            "#007F*sigh* Fine.\x02\x03",

            "It's no wonder we recognized\x01",
            "the guy who was talking to the\x01",
            "chief warrant officer.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x10, 400)

    ChrTalk(    #47
        0x9,
        (
            "The duke there says he intends\x01",
            "to stay here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x9,
        (
            "He insists he has to rent\x01",
            "all the rooms as well as\x01",
            "the dining hall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x101,
        (
            "#509FHe really is as selfish as\x01",
            "selfish gets, isn't he?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x105,
        (
            "#047FOh dear... He is a troublesome\x01",
            "fellow.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #51
        0x9,
        (
            "Royalty or not, what does he\x01",
            "expect us to do? Make everyone\x01",
            "else go camping?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x9,
        (
            "...And that's where you come\x01",
            "in, hopefully. Can you do\x01",
            "something to help?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x9,
        (
            "Ideally, convince him to go back\x01",
            "to Ruan. (Or give him a little\x01",
            "nudge over the falls...)\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_1641():
        TurnDirection(0x105, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1641)
    TurnDirection(0x101, 0x9, 400)
    Sleep(400)

    ChrTalk(    #54
        0x101,
        "#004FYou want ME to do it?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x9,
        (
            "Isn't tactical negotiation\x01",
            "part of your job?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x9,
        (
            "We're just soldiers, you know. We train\x01",
            "with guns and swords, and negotiating\x01",
            "with a sword can be somewhat...messy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x101,
        (
            "#004FA-And what makes you think\x01",
            "I'm any different? I'm good at\x01",
            "hitting stuff, not talking!\x02\x03",

            "#503FThey usually teach that\x01",
            "stuff to someone with a\x01",
            "knack for it...\x02\x03",

            "(Joshua's the guy with the\x01",
            "silver tongue, not me...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x105,
        (
            "#043FBut Estelle...we can't just stand\x01",
            "by while this is going on...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #59
        0x101,
        "#505FHmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x9,
        (
            "Please? Even if you can't\x01",
            "convince him with words,\x01",
            "there's always your staff...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)

    ChrTalk(    #61
        0x101,
        (
            "#007F*grumble* Okay, okay...\x02\x03",

            "Argh...I hate this kinda stuff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x9,
        (
            "Well, I have faith in you,\x01",
            "at least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x101,
        (
            "#509FLet me give it to you straight:\x01",
            "you can have all the faith in\x01",
            "the world, but I don't.\x02\x03",

            "So, don't get your hopes up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x105,
        "#040FI'm sure you'll do fine.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #65
        0x101,
        "#002FW-Well...thanks for that.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)
    Sleep(400)

    ChrTalk(    #66
        0x101,
        "#582FOkay...here goes nothing!\x02",
    )

    CloseMessageWindow()
    Sleep(400)

    def lambda_1A3E():

        label("loc_1A3E")

        TurnDirection(0x9, 0x101, 0)
        OP_48()
        Jump("loc_1A3E")

    QueueWorkItem2(0x9, 1, lambda_1A3E)

    def lambda_1A4F():

        label("loc_1A4F")

        TurnDirection(0x105, 0x101, 0)
        OP_48()
        Jump("loc_1A4F")

    QueueWorkItem2(0x105, 1, lambda_1A4F)

    def lambda_1A60():

        label("loc_1A60")

        TurnDirection(0xA, 0x101, 0)
        OP_48()
        Jump("loc_1A60")

    QueueWorkItem2(0xA, 1, lambda_1A60)
    OP_51(0xF, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x1), scpexpr(EXPR_PUSH_LONG, 0x17494), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x3), scpexpr(EXPR_PUSH_LONG, 0x32C8), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_1AB3():
        OP_69(0xF, 0x7D0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1AB3)
    OP_8E(0x101, 0x16CD8, 0x0, 0x300C, 0x7D0, 0x0)
    OP_8E(0x101, 0x17494, 0x0, 0x32C8, 0x7D0, 0x0)
    TurnDirection(0x101, 0x10, 400)
    OP_44(0x9, 0xFF)
    OP_44(0x105, 0xFF)
    OP_44(0xA, 0xFF)
    OP_62(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x11, 0x101, 400)

    ChrTalk(    #67
        0x11,
        "#721FOh, I remember you...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x11, 400)

    ChrTalk(    #68
        0x101,
        (
            "#506FHey... Uh, fancy seeing\x01",
            "you here.\x02\x03",

            "Where you go, trouble follows, \x01",
            "huh?\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x10, 0xFF)
    OP_44(0x12, 0xFF)
    ClearMapFlags(0x400000)
    OP_62(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_1BBF():
        TurnDirection(0x12, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1BBF)
    TurnDirection(0x10, 0x11, 400)

    ChrTalk(    #69
        0x10,
        (
            "#220FHmm?\x02\x03",

            "Who are you talking to, Phillip?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10, 400)

    ChrTalk(    #70
        0x101,
        "#002F(Okay, gotta start this off right...)\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Hey there, Duke-guy!]\x01",                                 # 0
            "[Greetings, Your Grace. I'm here to collect you.]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1CD0"),
        (1, "loc_2383"),
        (SWITCH_DEFAULT, "loc_2DEE"),
    )


    label("loc_1CD0")

    OP_28(0x23, 0x1, 0x2000)

    ChrTalk(    #71
        0x101,
        "#508FHey there, Duke-guy!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x101, 400)

    ChrTalk(    #72
        0x10,
        (
            "#222F...Harrumph.\x02\x03",

            "You really should have more\x01",
            "respect when addressing your\x01",
            "future king, young lady.\x02\x03",

            "#220FHmph...but no matter.\x01",
            "What do you want?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x101,
        "#000FI came to pick you up.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x10,
        (
            "#223FPick me up?\x02\x03",

            "I don't recall ordering\x01",
            "someone to do so.\x02\x03",

            "And where did you travel from?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[The mayor's estate.]\x01",      # 0
            "[From Hotel Blanche.]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1E93"),
        (1, "loc_1ED3"),
        (SWITCH_DEFAULT, "loc_1F1B"),
    )


    label("loc_1E93")


    ChrTalk(    #75
        0x101,
        (
            "#000FThe mayor's estate.\x02\x03",

            "He asked for me to come here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F1B")

    label("loc_1ED3")


    ChrTalk(    #76
        0x101,
        (
            "#000FFrom Hotel Blanche.\x02\x03",

            "At the personal request\x01",
            "of the owner.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F1B")

    label("loc_1F1B")


    ChrTalk(    #77
        0x10,
        (
            "#220FHmph, I see. That was most\x01",
            "courteous of him.\x02\x03",

            "But I have no desire to return\x01",
            "to Ruan this evening.\x02\x03",

            "I've already decided to stay\x01",
            "here, at Air-Letten.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x101,
        (
            "#000FBut the dinner party at the\x01",
            "estate is starting soon.\x02\x03",

            "I heard that everyone is\x01",
            "waiting for the arrival of\x01",
            "the future king...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x10,
        (
            "#220FAh, in that case, they will\x01",
            "continue to wait indefinitely.\x02\x03",

            "I'm tired of dinner parties.\x01",
            "I have no intention of going.\x02\x03",

            "#225FIf I stay here, I get a lovely\x01",
            "view of the waterfall, and\x01",
            "that is far more interesting.\x02\x03",

            "Ha ha ha... Such are the refined\x01",
            "tastes of the nobility.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(    #80
        0x101,
        (
            "#004FB-But...\x02\x03",

            "Isn't this place a little\x01",
            "low-class for the future\x01",
            "king to be staying at?\x02\x03",

            "I don't even think they offer\x01",
            "fine dining here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x10,
        (
            "#223FHmm... Well, that much is true.\x02\x03",

            "#220FThen, if only for the sake of\x01",
            "proper accommodation...\x02\x03",

            "...Phillip!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_227C():
        TurnDirection(0x12, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_227C)
    TurnDirection(0x11, 0x10, 400)

    ChrTalk(    #82
        0x11,
        "#720FY-Yes, sir?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x11, 400)

    ChrTalk(    #83
        0x10,
        (
            "#220FYou are to arrange for lodging\x01",
            "as soon as possible.\x02\x03",

            "Notify the hotel in Ruan to\x01",
            "deliver the bed as far as\x01",
            "the checkpoint.\x02\x03",

            "And have them ready their best\x01",
            "chef with the best ingredients\x01",
            "for my arrival.\x02",
        )
    )

    CloseMessageWindow()
    Call(1, 15)
    Jump("loc_2DEE")

    label("loc_2383")


    ChrTalk(    #84
        0x101,
        (
            "#500FGreetings, Your Grace.\x01",
            "I'm here to collect you.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x101, 400)

    ChrTalk(    #85
        0x10,
        (
            "#223FCollect me?\x02\x03",

            "I don't recall ordering\x01",
            "someone to do so.\x02\x03",

            "And where did you travel from?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[The mayor's estate.]\x01",      # 0
            "[From Hotel Blanche.]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_24A2"),
        (1, "loc_24E2"),
        (SWITCH_DEFAULT, "loc_252A"),
    )


    label("loc_24A2")


    ChrTalk(    #86
        0x101,
        (
            "#000FThe mayor's estate.\x02\x03",

            "He asked for me to come here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_252A")

    label("loc_24E2")


    ChrTalk(    #87
        0x101,
        (
            "#000FFrom Hotel Blanche.\x02\x03",

            "At the personal request of the owner.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_252A")

    label("loc_252A")


    ChrTalk(    #88
        0x10,
        (
            "#220FAhh... I see. That is quite\x01",
            "admirable of him.\x02\x03",

            "But I have no desire to return\x01",
            "to Ruan on this evening.\x02\x03",

            "I've already decided to stay\x01",
            "here, at Air-Letten.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x101,
        (
            "#002F(Okay, double or nothing...)\x02\x03",

            "(Gotta change his mind, but\x01",
            "make him feel like it's his\x01",
            "idea...)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[At this junky old place?]\x01",           # 0
            "[There is a dinner party at...]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_26C3"),
        (1, "loc_29EB"),
        (SWITCH_DEFAULT, "loc_2DEB"),
    )


    label("loc_26C3")

    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #90
        0x101,
        (
            "#004FYou really intend to stay at\x01",
            "this junky old place?\x02\x03",

            "I mean, look around. I don't\x01",
            "think this place deserves the\x01",
            "business of the next king.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x10,
        (
            "#225FHmph. You declare things I\x01",
            "already know to be true.\x02\x03",

            "I never believed this place\x01",
            "to be worthy of my presence.\x02\x03",

            "It is, however, occasionally\x01",
            "interesting to live as the\x01",
            "common folk do...briefly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x101,
        (
            "#003FWell, I get that...\x02\x03",

            "But I don't think they even\x01",
            "have a high-class chef here.\x02\x03",

            "Not to mention...I'll bet\x01",
            "it's not even very sanitary.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #93
        0x12,
        "(Grrrr...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x10,
        "#223FYou...think so?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10, 180, 400)

    ChrTalk(    #95
        0x10,
        (
            "#222FYes, now that you bring it to\x01",
            "my attention, the place DOES\x01",
            "look a bit on the filthy side.\x02\x03",

            "Hmm...\x02\x03",

            "I suppose I simply cannot stay\x01",
            "at such a place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x101,
        "#002F(Aaaand now for the sales pitch!)\x02",
    )

    CloseMessageWindow()
    Call(1, 14)
    Jump("loc_2DEB")

    label("loc_29EB")


    ChrTalk(    #97
        0x101,
        (
            "#000FI've heard that a dinner party\x01",
            "is being held at the mayor's\x01",
            "estate tonight.\x02\x03",

            "The guests are surely waiting\x01",
            "anxiously for the king-to-be\x01",
            "to make his appearance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x10,
        (
            "#220FAh, in that case, they will\x01",
            "continue to wait indefinitely.\x02\x03",

            "I'm tired of dinner parties.\x01",
            "I have no intention of going.\x02\x03",

            "#225FIf I stay here, I get a lovely\x01",
            "view of the waterfall, and\x01",
            "that is far more interesting.\x02\x03",

            "Ha ha ha... Such are the refined\x01",
            "tastes of the nobility.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(    #99
        0x101,
        (
            "#004FUmm...b-but...\x02\x03",

            "If you wish to stay in such crude\x01",
            "lodgings, that is most certainly\x01",
            "your right...\x02\x03",

            "But a man of your noble\x01",
            "bearing surely deserves\x01",
            "only the finest food!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x10,
        (
            "#223FYou do make a fine point.\x02\x03",

            "#220FThen, if only for the sake of\x01",
            "proper accommodation...\x02\x03",

            "...Phillip\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2CE9():
        TurnDirection(0x12, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2CE9)
    TurnDirection(0x11, 0x10, 400)

    ChrTalk(    #101
        0x11,
        "#720FY-Yes, sir?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x11, 400)

    ChrTalk(    #102
        0x10,
        (
            "#220FYou are to arrange for lodging\x01",
            "as soon as possible.\x02\x03",

            "Notify the hotel in Ruan to\x01",
            "deliver the bed as far as\x01",
            "the checkpoint.\x02\x03",

            "And have them ready their best\x01",
            "chef with the best ingredients\x01",
            "available.\x02",
        )
    )

    CloseMessageWindow()
    Call(1, 15)
    Jump("loc_2DEB")

    label("loc_2DEB")

    Jump("loc_2DEE")

    label("loc_2DEE")

    ClearMapFlags(0x400000)
    EventEnd(0x0)
    SetMapFlags(0x1)
    Return()

    # Function_11_E86 end

    def Function_12_2DFB(): pass

    label("Function_12_2DFB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2E1E")
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(4000)
    Jump("Function_12_2DFB")

    label("loc_2E1E")

    Return()

    # Function_12_2DFB end

    def Function_13_2E1F(): pass

    label("Function_13_2E1F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2E47")
    Sleep(2000)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(2000)
    Jump("Function_13_2E1F")

    label("loc_2E47")

    Return()

    # Function_13_2E1F end

    def Function_14_2E48(): pass

    label("Function_14_2E48")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Okay, let's get you back to Ruan.]\x01",      # 0
            "[Your Grace, by your foot...]\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2EDB"),
        (1, "loc_313E"),
        (SWITCH_DEFAULT, "loc_35D5"),
    )


    label("loc_2EDB")


    ChrTalk(    #103
        0x101,
        (
            "#006FOkay, let's get you back to Ruan.\x02\x03",

            "If we go now, we should get\x01",
            "there while it's still light.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x101, 400)

    ChrTalk(    #104
        0x10,
        (
            "#223FHmm? What are you talking about?\x02\x03",

            "Who said anything about\x01",
            "returning to Ruan?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x101,
        (
            "#004F...Huh?\x02\x03",

            "But you just said that you\x01",
            "couldn't stay in a place\x01",
            "like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x10,
        (
            "#220FHmph. Merely talk for the sake\x01",
            "of propriety.\x02\x03",

            "...Phillip!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_303C():
        TurnDirection(0x12, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_303C)
    TurnDirection(0x11, 0x10, 400)

    ChrTalk(    #107
        0x11,
        "#720FY-Yes, sir!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x11, 400)

    ChrTalk(    #108
        0x10,
        (
            "#220FYou are to arrange for lodging\x01",
            "as soon as possible.\x02\x03",

            "Notify the hotel in Ruan to\x01",
            "deliver the bed as far as\x01",
            "the checkpoint.\x02\x03",

            "And have them ready their best\x01",
            "chef with the best ingredients\x01",
            "available.\x02",
        )
    )

    CloseMessageWindow()
    Call(1, 15)
    Jump("loc_35D5")

    label("loc_313E")

    OP_28(0x23, 0x1, 0x8)

    ChrTalk(    #109
        0x101,
        "#004FYour Grace, by your foot...\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    TurnDirection(0x10, 0x101, 400)

    ChrTalk(    #110
        0x10,
        "#223FHmm? What about my foot?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x101,
        "#509F...There's a huge cockroach.\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_95(0x10, 0x0, 0x0, 0x0, 0x320, 0x2EE0)

    def lambda_3206():
        TurnDirection(0x9, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3206)

    def lambda_3214():
        TurnDirection(0x105, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3214)
    TurnDirection(0x12, 0x10, 400)

    ChrTalk(    #112
        0x10,
        "#226FEEEEEEEEK! Ph-Phillip!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x11,
        "#723FY-Yes, sir!\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x10, 225, 800)
    OP_8C(0x10, 315, 800)
    OP_8C(0x10, 135, 800)

    ChrTalk(    #114
        0x10,
        (
            "#226FWh-Where's the roach?\x01",
            "Where is it?!\x02\x03",

            "Hurry! Hurry up and kill it!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x101,
        (
            "#507F*sigh* Surely, sir, you can\x01",
            "expect no better from the\x01",
            "common peasantry.\x02\x03",

            "Why, I'd wager they even have\x01",
            "monsters infesting the--\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_95(0x10, 0x0, 0x0, 0x0, 0x320, 0x2EE0)

    ChrTalk(    #116
        0x10,
        "#228FEEEEEEK!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x11, 0)

    ChrTalk(    #117
        0x10,
        "#226FE-Enough! Phillip! We're leaving!\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #118
        0x11,
        "#723FYes, sir! As you wish, sir...\x02",
    )

    CloseMessageWindow()

    def lambda_3412():

        label("loc_3412")

        TurnDirection(0x12, 0x10, 0)
        OP_48()
        Jump("loc_3412")

    QueueWorkItem2(0x12, 1, lambda_3412)

    def lambda_3423():

        label("loc_3423")

        TurnDirection(0x9, 0x10, 0)
        OP_48()
        Jump("loc_3423")

    QueueWorkItem2(0x9, 1, lambda_3423)

    def lambda_3434():

        label("loc_3434")

        TurnDirection(0x101, 0x10, 0)
        OP_48()
        Jump("loc_3434")

    QueueWorkItem2(0x101, 1, lambda_3434)

    def lambda_3445():

        label("loc_3445")

        TurnDirection(0x11, 0x10, 0)
        OP_48()
        Jump("loc_3445")

    QueueWorkItem2(0x11, 1, lambda_3445)

    def lambda_3456():

        label("loc_3456")

        TurnDirection(0xA, 0x10, 0)
        OP_48()
        Jump("loc_3456")

    QueueWorkItem2(0xA, 1, lambda_3456)
    OP_8E(0x10, 0x16E04, 0x0, 0x2EE0, 0x1388, 0x0)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x1E)
    OP_43(0x105, 0x1, 0x1, 0x14)
    OP_43(0x11, 0x1, 0x1, 0x15)
    OP_62(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_34A9():
        OP_8E(0xA, 0x169A4, 0x0, 0x21FC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_34A9)
    OP_8E(0x10, 0x1624C, 0x0, 0x2904, 0x1388, 0x0)
    SetChrFlags(0x10, 0x80)
    WaitChrThread(0x11, 0x1)
    TurnDirection(0x11, 0x101, 400)

    ChrTalk(    #119
        0x11,
        "#720F...Thank you so much.\x02",
    )

    CloseMessageWindow()
    OP_73(0x1)
    OP_44(0x12, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0x101, 0xFF)
    OP_44(0x105, 0xFF)
    OP_44(0xA, 0xFF)

    def lambda_3520():

        label("loc_3520")

        TurnDirection(0x12, 0x11, 0)
        OP_48()
        Jump("loc_3520")

    QueueWorkItem2(0x12, 1, lambda_3520)

    def lambda_3531():

        label("loc_3531")

        TurnDirection(0x9, 0x11, 0)
        OP_48()
        Jump("loc_3531")

    QueueWorkItem2(0x9, 1, lambda_3531)

    def lambda_3542():

        label("loc_3542")

        TurnDirection(0x101, 0x11, 0)
        OP_48()
        Jump("loc_3542")

    QueueWorkItem2(0x101, 1, lambda_3542)

    def lambda_3553():

        label("loc_3553")

        TurnDirection(0x105, 0x11, 0)
        OP_48()
        Jump("loc_3553")

    QueueWorkItem2(0x105, 1, lambda_3553)

    def lambda_3564():

        label("loc_3564")

        TurnDirection(0xA, 0x11, 0)
        OP_48()
        Jump("loc_3564")

    QueueWorkItem2(0xA, 1, lambda_3564)

    ChrTalk(    #120
        0x101,
        "#001FThink nothing of it. ♪\x02",
    )

    CloseMessageWindow()
    OP_8E(0x11, 0x1624C, 0x0, 0x2904, 0x1388, 0x0)
    SetChrFlags(0x11, 0x80)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x12, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0x101, 0xFF)
    OP_44(0x105, 0xFF)
    OP_44(0xA, 0xFF)
    NewScene("ED6_DT01/T2710   ._SN", 102, 0, 0)
    IdleLoop()
    Jump("loc_35D5")

    label("loc_35D5")

    Return()

    # Function_14_2E48 end

    def Function_15_35D6(): pass

    label("Function_15_35D6")

    OP_28(0x23, 0x1, 0x10)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #121
        0x101,
        "#004FH-Huh?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x10,
        (
            "#220FAnd then, have the soldiers\x01",
            "set about cleaning the dining\x01",
            "hall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x11,
        (
            "#722FYour Grace, perhaps that\x01",
            "is going a trifle far...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x10,
        (
            "#224FSilence, Phillip!\x02\x03",

            "As the next king, I will have\x01",
            "proper lodging!\x02\x03",

            "As is my right, might I add!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #125
        0x101,
        "#002FOh, cut the crap already.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x101, 400)

    ChrTalk(    #126
        0x10,
        "#222FI...BEG your pardon!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x101,
        (
            "#009FI've been all nice and\x01",
            "courteous, and you STILL\x01",
            "act like a spoiled brat!\x02\x03",

            "If you didn't have Phillip around,\x01",
            "you'd probably just starve!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x1, 0x2000)"), scpexpr(EXPR_END)), "loc_3885")
    OP_62(0x105, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #128
        0x105,
        (
            "#045F(*sigh* Typical Estelle...)\x02\x03",

            "(I wonder if this is really her \x01",
            "idea of 'nice and courteous'...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38B7")

    label("loc_3885")

    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #129
        0x105,
        "#044FE-Estelle?!\x02",
    )

    CloseMessageWindow()

    label("loc_38B7")


    ChrTalk(    #130
        0x10,
        "#222FGrrrr... You insolent whelp!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x9, 400)

    ChrTalk(    #131
        0x10,
        (
            "#224FYou! Soldiers! What do you\x01",
            "think you're doing?\x02\x03",

            "Hurry up and arrest this brat!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x101,
        (
            "#582FThe only one who needs\x01",
            "arresting here...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 45, 1000)
    OP_8C(0x101, 315, 1000)
    OP_8C(0x101, 180, 1000)
    SetChrChipByIndex(0x101, 9)

    ChrTalk(    #133
        0x101,
        "#005F...is YOU, you big jackass!\x02",
    )

    CloseMessageWindow()

    def lambda_39B7():
        TurnDirection(0x12, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_39B7)
    TurnDirection(0x10, 0x101, 0)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_95(0x10, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
    Sleep(400)
    OP_62(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_3A89():
        OP_94(0x1, 0x10, 0xB4, 0x578, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3A89)
    WaitChrThread(0x10, 0x1)

    ChrTalk(    #134
        0x10,
        "#226FAieeeee!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x105,
        "#043FEstelle! Don't!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x101,
        "#005FHyaaaaahhhh!!\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_3B0D():

        label("loc_3B0D")

        TurnDirection(0x9, 0x101, 0)
        OP_48()
        Jump("loc_3B0D")

    QueueWorkItem2(0x9, 1, lambda_3B0D)

    def lambda_3B1E():

        label("loc_3B1E")

        TurnDirection(0xA, 0x101, 0)
        OP_48()
        Jump("loc_3B1E")

    QueueWorkItem2(0xA, 1, lambda_3B1E)
    OP_43(0x10, 0x1, 0x1, 0x10)
    OP_43(0x11, 0x2, 0x1, 0x11)
    OP_43(0x101, 0x1, 0x1, 0x12)
    OP_43(0x105, 0x1, 0x1, 0x13)

    def lambda_3B4B():

        label("loc_3B4B")

        TurnDirection(0x12, 0x10, 0)
        OP_48()
        Jump("loc_3B4B")

    QueueWorkItem2(0x12, 1, lambda_3B4B)

    def lambda_3B5C():

        label("loc_3B5C")

        TurnDirection(0x11, 0x10, 0)
        OP_48()
        Jump("loc_3B5C")

    QueueWorkItem2(0x11, 1, lambda_3B5C)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x12, 0xFF)
    OP_44(0x11, 0xFF)
    OP_44(0x101, 0xFF)
    OP_44(0x105, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    SetChrChipByIndex(0x101, 65535)
    ClearChrFlags(0xE, 0x80)
    Sleep(1000)
    FadeToBright(2000, 0)
    SetChrPos(0x10, 95380, 0, 12000, 90)
    SetChrPos(0x11, 94280, 0, 11200, 90)
    SetChrPos(0x101, 92630, 0, 13400, 135)
    SetChrPos(0xA, 93400, 0, 13300, 315)
    SetChrPos(0x9, 92710, 0, 12520, 0)
    SetChrPos(0x12, 93420, 0, 12620, 315)
    SetChrPos(0xE, 96610, 0, 12500, 270)
    SetChrPos(0x105, 96610, 0, 11500, 270)
    OP_44(0xE, 0xFF)
    OP_43(0x101, 0x1, 0x1, 0x16)
    OP_0D()
    Sleep(400)

    ChrTalk(    #137
        0x10,
        (
            "#220FHmm...\x01",
            "That much is obviously true.\x02\x03",

            "*sigh* I guess it really\x01",
            "doesn't matter.\x02\x03",

            "Come, Phillip.\x01",
            "Let us return to Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x11,
        "#720FYes, sir! As you wish, sir...\x02",
    )

    CloseMessageWindow()

    def lambda_3CE8():

        label("loc_3CE8")

        TurnDirection(0x101, 0x10, 0)
        OP_48()
        Jump("loc_3CE8")

    QueueWorkItem2(0x101, 3, lambda_3CE8)
    SetChrFlags(0x10, 0x40)
    SetChrFlags(0x11, 0x40)
    OP_8E(0x10, 0x16E04, 0x0, 0x2EE0, 0xBB8, 0x0)
    OP_8E(0x10, 0x169B8, 0x0, 0x2A94, 0xBB8, 0x0)
    OP_43(0x11, 0x1, 0x1, 0x15)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x1E)
    OP_73(0x1)
    OP_8E(0x10, 0x1624C, 0x0, 0x2A94, 0xBB8, 0x0)
    SetChrFlags(0x10, 0x8)
    TurnDirection(0x11, 0xE, 400)

    ChrTalk(    #139
        0x11,
        "#720F...Thank you so much.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x11, 400)

    ChrTalk(    #140
        0xE,
        (
            "#015FAnd thank you.\x02\x03",

            "I am simply glad that the duke\x01",
            "was not hurt in any way.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x105, 400)

    ChrTalk(    #141
        0x11,
        (
            "#720FThat would be thanks to this\x01",
            "young lady here.\x02\x03",

            "Her reflexes are remarkable. I'm\x01",
            "not certain I would have been able\x01",
            "to hold back like that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x10,
        "Phillip! What are you doing?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x11,
        "#720FIf you'll please pardon me.\x02",
    )

    CloseMessageWindow()
    OP_8E(0x11, 0x1624C, 0x0, 0x2A94, 0x1388, 0x0)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x10, 0x80)
    OP_72(0x1, 0x800)
    OP_22(0x7, 0x0, 0x64)
    OP_6F(0x1, 30)
    OP_70(0x1, 0x0)
    OP_73(0x1)
    OP_71(0x1, 0x800)

    ChrTalk(    #144
        0xE,
        (
            "#017F...\x02\x03",

            "Phew... Finally.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x105,
        "#045F*sigh* He's finally gone...\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x101, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0x12, 0xFF)
    OP_44(0xA, 0xFF)
    SetChrFlags(0xE, 0x80)
    NewScene("ED6_DT01/T2710   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_15_35D6 end

    def Function_16_3F6B(): pass

    label("Function_16_3F6B")

    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0xFE, 0x172B4, 0x0, 0x1FA4, 0x7D0, 0x0)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0xFE, 0x101, 400)
    Return()

    # Function_16_3F6B end

    def Function_17_3FAB(): pass

    label("Function_17_3FAB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3FCE")
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)
    Jump("Function_17_3FAB")

    label("loc_3FCE")

    Return()

    # Function_17_3FAB end

    def Function_18_3FCF(): pass

    label("Function_18_3FCF")

    SetChrChipByIndex(0x101, 10)
    OP_8E(0xFE, 0x172B4, 0x0, 0x251C, 0x7D0, 0x0)
    Return()

    # Function_18_3FCF end

    def Function_19_3FE9(): pass

    label("Function_19_3FE9")

    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0xFE, 0x16F94, 0x0, 0x2828, 0xBB8, 0x0)
    OP_8E(0xFE, 0x17318, 0x0, 0x22B0, 0xBB8, 0x0)
    TurnDirection(0xFE, 0x101, 400)
    Return()

    # Function_19_3FE9 end

    def Function_20_402B(): pass

    label("Function_20_402B")

    OP_8C(0xFE, 0, 400)
    OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)

    def lambda_4047():

        label("loc_4047")

        TurnDirection(0x105, 0x10, 0)
        OP_48()
        Jump("loc_4047")

    QueueWorkItem2(0x105, 2, lambda_4047)
    Return()

    # Function_20_402B end

    def Function_21_4053(): pass

    label("Function_21_4053")

    OP_8C(0xFE, 270, 400)
    OP_94(0x1, 0xFE, 0x0, 0x64, 0x7D0, 0x0)
    Sleep(1000)
    Return()

    # Function_21_4053 end

    def Function_22_406F(): pass

    label("Function_22_406F")

    OP_43(0xFE, 0x0, 0x0, 0x2)
    OP_4B(0x9, 255)
    OP_4B(0x12, 255)
    OP_4B(0xA, 255)

    label("loc_4082")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_41E7")
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x12, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_40D9():
        OP_94(0x1, 0xFE, 0x0, 0x12C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_40D9)
    Sleep(200)

    def lambda_40F4():
        OP_94(0x1, 0xFE, 0xB4, 0x12C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_40F4)

    def lambda_410A():
        OP_94(0x1, 0xFE, 0xB4, 0x12C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_410A)
    Sleep(200)

    def lambda_4125():
        OP_94(0x1, 0x12, 0xB4, 0x12C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_4125)
    Sleep(2000)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x12, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_4188():
        OP_94(0x1, 0xFE, 0xB4, 0xFFFFFED4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4188)

    def lambda_419E():
        OP_94(0x1, 0xFE, 0xB4, 0xFFFFFED4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_419E)

    def lambda_41B4():
        OP_94(0x1, 0x12, 0xB4, 0xFFFFFED4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_41B4)
    Sleep(200)

    def lambda_41CF():
        OP_94(0x1, 0xFE, 0x0, 0xFFFFFED4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_41CF)
    Sleep(2000)
    Jump("loc_4082")

    label("loc_41E7")

    Return()

    # Function_22_406F end

    def Function_23_41E8(): pass

    label("Function_23_41E8")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    FadeToBright(2000, 0)
    SetChrFlags(0xE, 0x80)
    SetChrPos(0xB, -770, 0, 21500, 0)
    SetChrPos(0xC, -770, 0, 22500, 0)
    SetChrPos(0xD, -770, 0, 23500, 0)
    SetChrPos(0x101, -1000, 0, 9300, 180)
    SetChrPos(0x105, 0, 0, 9300, 180)
    SetChrPos(0x102, -1800, 0, 7800, 90)
    SetChrPos(0x8, 0, 0, 6500, 0)
    SetChrPos(0x9, -1000, 0, 5500, 0)
    SetChrPos(0x12, -2000, 0, 6500, 90)
    SetChrPos(0xA, -4800, 0, 7900, 90)
    OP_51(0xF, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0xF, 0x0)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    OP_4A(0x12, 255)
    OP_4A(0xA, 255)
    OP_0D()

    ChrTalk(    #146
        0x9,
        "And all because of one magic word...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x9,
        "'Cockroach.' Classic.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x9,
        (
            "And she had the guts to say\x01",
            "that to his face...! Ha!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x9,
        "Yeah... I needed a good laugh.\x02",
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #150
        0x8,
        "Hmm... Really? That's a relief.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x8,
        (
            "I'd been worried that we might\x01",
            "have to get rough with him...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x8,
        (
            "But from what Kientz has told\x01",
            "me, everything seems to have\x01",
            "worked out.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x101, 400)

    ChrTalk(    #153
        0x12,
        (
            "Speaking ill of my establishment\x01",
            "certainly seemed to do the\x01",
            "trick, didn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x101,
        (
            "#506FUmmm... Ha ha...\x01",
            "Sorry about that.\x02\x03",

            "I didn't see any other way to\x01",
            "get to him other than to tell\x01",
            "a little white lie or two.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #155
        0x102,
        (
            "#011FStill, it was unexpected.\x02\x03",

            "I didn't know you had it in\x01",
            "you to be that sneaky.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #156
        0x101,
        (
            "#502FHa. You never know what I'm\x01",
            "capable of, when the situation\x01",
            "calls for it.\x02\x03",

            "To be honest, I just tried to\x01",
            "channel Joshua.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #157
        0x105,
        (
            "#040FHa ha. It certainly seemed\x01",
            "like that to me.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #158
        0x101,
        (
            "#001FYeah...and if not, I'd never\x01",
            "have been able to lie with a\x01",
            "straight face like that.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    ChrTalk(    #159
        0x102,
        "#018F...\x02",
    )

    CloseMessageWindow()
    OP_63(0x102)

    ChrTalk(    #160
        0x9,
        (
            "Ha ha ha... Well, lies come\x01",
            "in all shades.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x9,
        (
            "You did it to help others,\x01",
            "so I'm sure that Aidios will\x01",
            "forgive you for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x8,
        "Yes, we greatly appreciate it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x8,
        (
            "May you be equally as determined\x01",
            "in your future duties.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_47DB():
        TurnDirection(0x105, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_47DB)
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #164
        0x101,
        "#006FYep. Take care.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(    #165
        0x102,
        "#010FWell, then...if you'll excuse us.\x02",
    )

    CloseMessageWindow()
    OP_2B(0x23, 0x2)
    Sleep(400)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #166
        "\x07\x00Quest \x07\x02[Make Him Leave!] \x07\x00completed!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_4B(0x8, 255)
    OP_4B(0x9, 255)
    OP_4B(0x12, 255)
    OP_4B(0xA, 255)
    ClearChrFlags(0x101, 0x40)
    ClearChrFlags(0x105, 0x40)
    ClearChrFlags(0x10, 0x40)
    ClearChrFlags(0x11, 0x40)
    NewScene("ED6_DT01/T2700   ._SN", 101, 0, 0)
    IdleLoop()
    SetMapFlags(0x1)
    EventEnd(0x0)
    Return()

    # Function_23_41E8 end

    def Function_24_48DB(): pass

    label("Function_24_48DB")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    FadeToBright(2000, 0)
    SetChrFlags(0xE, 0x80)
    SetChrPos(0xB, -770, 0, 21500, 0)
    SetChrPos(0xC, -770, 0, 22500, 0)
    SetChrPos(0xD, -770, 0, 23500, 0)
    SetChrPos(0x101, -1000, 0, 9300, 180)
    SetChrPos(0x105, 0, 0, 9300, 180)
    SetChrPos(0x102, -1800, 0, 7800, 90)
    SetChrPos(0x8, 0, 0, 6500, 0)
    SetChrPos(0x9, -1000, 0, 5500, 0)
    SetChrPos(0x12, -2000, 0, 6500, 90)
    SetChrPos(0xA, -4800, 0, 7900, 90)
    OP_51(0xF, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0xF, 0x0)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    OP_4A(0x12, 255)
    OP_4A(0xA, 255)
    OP_0D()

    ChrTalk(    #167
        0x9,
        (
            "...Man, this girl is not someone\x01",
            "I'd want mad at me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x9,
        (
            "She had that rod of hers aimed\x01",
            "full tilt right at his noggin!\x01",
            "I so thought she was gonna do it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x9,
        "If you could have only seen it...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x9,
        (
            "And after all that, it took\x01",
            "just one girl to settle it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x8,
        "Hmm... I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x8,
        (
            "I have some concerns about\x01",
            "resorting to such...\x01",
            "bombastic methods...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x8,
        (
            "But I suppose no real harm\x01",
            "was done.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x8, 400)

    ChrTalk(    #174
        0x12,
        (
            "It was like you subdued a criminal,\x01",
            "close enough.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #175
        0x101,
        "#007FI'm really ashamed of myself...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(    #176
        0x102,
        "#017FWe're sorry.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(    #177
        0x8,
        (
            "No, no. None of this would\x01",
            "have happened, were it not\x01",
            "for the duke's selfishness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x8,
        (
            "You did only what you felt\x01",
            "was necessary.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4CC0():
        TurnDirection(0x12, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_4CC0)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #179
        0x8,
        (
            "I do hope that you'll try more\x01",
            "DIPLOMATIC behavior in the\x01",
            "future, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x101,
        "#007F*gulp* I'll try my best.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #181
        0x101,
        "#003FThanks for stopping me, Kloe.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #182
        0x105,
        (
            "#040FIt's no trouble at all.\x02\x03",

            "I don't approve of violence...\x01",
            "but the duke's behavior was\x01",
            "utterly reprehensible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x8,
        (
            "Perhaps there were other means\x01",
            "available, but you did help\x01",
            "the other guests.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x8,
        (
            "And for that, we are truly\x01",
            "grateful.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #185
        0x101,
        (
            "#000FThank you...err, you're welcome.\x02\x03",

            "#001FHee hee... All right!\x02\x03",

            "Hearing you say that makes\x01",
            "me feel a little better.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #186
        0x102,
        (
            "#018FI swear, you can't stay upset\x01",
            "for more than three seconds.\x02\x03",

            "#017FBut I guess that's what\x01",
            "makes you who you are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x105,
        "#041F*giggle*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x8,
        (
            "Well, thank you again for your\x01",
            "help today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x8,
        (
            "May you be equally as determined\x01",
            "in your future duties.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x101,
        "#006FYep. Take care.\x02",
    )

    CloseMessageWindow()

    def lambda_5023():
        TurnDirection(0x105, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5023)
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(    #191
        0x102,
        "#010FWell, then... If you'll excuse us.\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #192
        "\x07\x00Quest \x07\x02[Make Him Leave!] \x07\x00completed!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_4B(0x8, 255)
    OP_4B(0x9, 255)
    OP_4B(0x12, 255)
    OP_4B(0xA, 255)
    ClearChrFlags(0x101, 0x40)
    ClearChrFlags(0x105, 0x40)
    ClearChrFlags(0x10, 0x40)
    ClearChrFlags(0x11, 0x40)
    NewScene("ED6_DT01/T2700   ._SN", 101, 0, 0)
    IdleLoop()
    SetMapFlags(0x1)
    EventEnd(0x0)
    Return()

    # Function_24_48DB end

    def Function_25_50FE(): pass

    label("Function_25_50FE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_517F")
    EventBegin(0x1)
    OP_4A(0xE, 255)
    TurnDirection(0xE, 0x101, 0)

    ChrTalk(    #193
        0xE,
        (
            "#012FCome on, Estelle. Let's check\x01",
            "on the dining hall.\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    OP_8C(0xE, 0, 0)
    OP_4B(0xE, 255)
    Sleep(50)
    EventEnd(0x4)

    label("loc_517F")

    Return()

    # Function_25_50FE end

    SaveToFile()

Try(main)
